# Change History for nasa.json (Part 55)

### Changes from 31606f9 to dd2190f (Part 44/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2753316241-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL21.003",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL21.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL21.003",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL21.003",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2753316241-NSIDC_CPRD",
+            "issued": "2018-10-14",
+            "keyword": [
+                "earth science",
+                "sea surface topography",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL21.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-10-14T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Polar Sea Surface Height Anomaly V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-ISSNA%2FISSWA-5-MIDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Images of the icy Saturnian satellites Mimas, Enceladus, Tethys, \nDione, Rhea, Iapetus, and Phoebe, derived by the Voyager and Cassini\ncameras are used to produce new local highresolution image mosaics \nas well as global mosaics. These global mosaics are valuable both \nfor scientific interpretation and for the planning of future flybys \nlater in the ongoing Cassini orbital tour. Furthermore, these \nglobal mosaics can be extended to standard cartographic products.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-issna-isswa-5-midr-v1.0_a3c8-kib6",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "enceladus",
                 "phoebe",
@@ -453471,252 +453473,264 @@
                 "dione",
                 "cassini-huygens"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-ISSNA%2FISSWA-5-MIDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-issna-isswa-5-midr-v1.0_a3c8-kib6",
-            "description": "Images of the icy Saturnian satellites Mimas, Enceladus, Tethys, \nDione, Rhea, Iapetus, and Phoebe, derived by the Voyager and Cassini\ncameras are used to produce new local highresolution image mosaics \nas well as global mosaics. These global mosaics are valuable both \nfor scientific interpretation and for the planning of future flybys \nlater in the ongoing Cassini orbital tour. Furthermore, these \nglobal mosaics can be extended to standard cartographic products.",
-            "title": "CASSINI ORBITER SATURN ISSNA/ISSWA 5 \n                              MIDR VERSION 1.0",
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
+            "title": "CASSINI ORBITER SATURN ISSNA/ISSWA 5 \n                              MIDR VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-EXT3-MTP031-V2.0",
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
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the EXTENSION 3 MTP031 phase, which occurred from 2016-06-29 to 2016-07-27 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-ext3-mtp031-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-EXT3-MTP031-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-ext3-mtp031-v2.0",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the EXTENSION 3 MTP031 phase, which occurred from 2016-06-29 to 2016-07-27 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 EXTENSION 3 MTP031 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 EXTENSION 3 MTP031 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0024",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2007-05-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0024.",
-            "issued": "2013-12-04",
-            "temporal": "2001-05-23T00:00:00Z/2002-09-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-25",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
-                "air quality",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DR. SPYROS PANDIS",
                 "hasEmail": "mailto:spyros@andrew.cmu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2350080114-LARC_ASDC",
             "description": "NARSTO_EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite Pittsburgh Gas Concentration and Particulate matter (PM) Physical Properties Data product. Data was obtained between May 23, 2001 and September 1, 2002 during the Pittsburgh Air Quality Study (PAQS). The data set provides Particulate Matter Composition Data of the following types: \r\n1) Total, Organic, and Hydrogen Peroxide data \r\n2) Filter based measurement of PM10 and PM2.5 Mass concentration using a Dichotomous sampler \r\n3) Epiphaniometer total particle active surface area\r\n4) Filter based measurement of PM2.5 Mass using the Federal Reference Method\r\n5) Integrating nephelometer based measurement of PM2.5 light scattering\r\n6) TSI Scanning Mobility Particle Sizer (Long-column/model 3936L10)\r\n7) Measurements of PM mass size distribution using a MOUDI cascade impactor\r\n8) In-situ VOC measurements by pre-concentration and gc/msd/fid9) Surface air concentrations of O3, NO, NOx, SO2, CO, and PM2.5 mass. \r\n\r\nPittsburgh Air Quality Study (PAQS), along with the Pittsburgh Supersite Program, was a comprehensive, multi-disciplinary investigation to characterize the ambient PM in the Pittsburgh region, to improve understanding the links between ambient PM and public health, and to develop new instrumentation for PM measurements. The Pittsburgh supersite was designed to achieve several objectives: to determine the physical and chemical characteristics of PM in the Pittsburgh region; to develop and evaluate the next generation of atmospheric aerosol monitoring techniques; to update emission profiles for important regional sources; to quantify the impact of the various sources on the local PM concentrations; and to predict changes in the PM characteristics due to proposed changes in emissions. The last objective was based on concurrent modeling studies and was designed to support the development of regulations. These objectives were addressed through four components of the research: (1) ambient monitoring at a central site and a set of satellite sites in the region; (2) an instrument development and evaluation study; (3) a data analysis and synthesis component; and (4) a comprehensive modeling component. \r\n\r\nThe central supersite was located on a grassy hill in a large urban park adjacent to the Carnegie Mellon University campus, approximately 6km east of downtown Pittsburgh. It was separated from the city in the predominant upwind direction (south and west) by roughly 1km of parkland. It was at least several hundred meters from any other major source of air pollution: the site was positioned approximately 50m past the end of a dead end street, and several hundred meters from the nearest heavily traveled street. Five additional sites were operated as Satellite sites to character the spatial variation of the PM. The measurement campaign lasted for 14 months (July 2001-September 2002). Intensive monitoring was performed during two periods, from 1 July to 3 August, 2001 (ESP01) and 1 January to 15 January, 2002 (ESP02). Baseline monitoring was conducted for the rest of the study. Baseline measurements included daily filter samples for fine particle mass and composition (OC/EC, major ions, elemental composition). The U.S. EPA Particulate Matter (PM) super sites Program was an ambient air monitoring research program from 1999-2004 designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. Eight geographically diverse projects were chosen to specifically address these EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different method",
-            "title": "NARSTO EPA Supersite (SS) Pittsburgh Gas Concentration and Particulate matter (PM) Physical Properties Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0024",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0024",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2350080114-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2350080114-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0024",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0024",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_pittsburgh_gas_pm_property_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_PITTSBURGH Gas Conc and PM Physical Properties Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_PITTSBURGH Gas Conc and PM Physical Properties Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_pittsburgh_gas_pm_property_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Final_QA_Report.pdf",
-                    "description": "Quality Assurance Final Report for the Pittsburgh Air Quality Study Pittsburgh Supersite June 30, 2001 - September 30, 2002",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance Final Report for the Pittsburgh Air Quality Study Pittsburgh Supersite June 30, 2001 - September 30, 2002",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Final_QA_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Final_Report.pdf",
-                    "description": "Pittsburgh Air Quality Study (PAQS) Final Report",
                     "@type": "dcat:Distribution",
+                    "description": "Pittsburgh Air Quality Study (PAQS) Final Report",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Pittsburgh_Final_Report.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_PITTSBURGH_GAS_PM_PROPERTY_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2350080114-LARC_ASDC",
+            "issued": "2013-12-04",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "air quality",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0024",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "40.44 -79.94",
+            "temporal": "2001-05-23T00:00:00Z/2002-09-01T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Pittsburgh Gas Concentration and Particulate matter (PM) Physical Properties Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M15-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m15-str-refl-v1.0_a3f5-ajv3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M15-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m15-str-refl-v1.0_a3f5-ajv3",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP015 RDR-STR-REFL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP015 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a3f5-ttma",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The International Space Station (ISS) is a unique habitat for humans and microorganisms. Here, we report the results of the ISS experiment EXTREMOPHILES, including the analysis of microbial communities from several areas aboard at three time points. We assess microbial diversity, distribution, functional capacity and resistance profile using a combination of cultivation-independent analyses (amplicon and shot-gun sequencing) and cultivation-dependent analyses (physiological and genetic characterization of microbial isolates, antibiotic resistance tests, co-incubation experiments). We show that the ISS microbial communities are highly similar to those present in ground-based confined indoor environments and are subject to fluctuations, although a core microbiome persists over time and locations. The genomic and physiological features selected by ISS conditions do not appear to be directly relevant to human health, although adaptations towards biofilm formation and surface interactions were observed. Our results do not raise direct reason for concern with respect to crew health, but indicate a potential threat towards material integrity in moist areas.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-279",
+                    "mediaType": "text/html",
+                    "title": "International Space Station flight project EXTREMOPHILES"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-279_a3f5-ttma",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "spaceflight",
                 "sample location",
@@ -453727,536 +453741,500 @@
                 "data transformation",
                 "amplicon sequencing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a3f5-ttma",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-279_a3f5-ttma",
-            "description": "The International Space Station (ISS) is a unique habitat for humans and microorganisms. Here, we report the results of the ISS experiment EXTREMOPHILES, including the analysis of microbial communities from several areas aboard at three time points. We assess microbial diversity, distribution, functional capacity and resistance profile using a combination of cultivation-independent analyses (amplicon and shot-gun sequencing) and cultivation-dependent analyses (physiological and genetic characterization of microbial isolates, antibiotic resistance tests, co-incubation experiments). We show that the ISS microbial communities are highly similar to those present in ground-based confined indoor environments and are subject to fluctuations, although a core microbiome persists over time and locations. The genomic and physiological features selected by ISS conditions do not appear to be directly relevant to human health, although adaptations towards biofilm formation and surface interactions were observed. Our results do not raise direct reason for concern with respect to crew health, but indicate a potential threat towards material integrity in moist areas.",
-            "title": "International Space Station flight project EXTREMOPHILES",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-279",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "International Space Station flight project EXTREMOPHILES"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "International Space Station flight project EXTREMOPHILES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Analysis_ER2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-11-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Analysis_ER2_Data_1.",
-            "issued": "1995-04-27",
-            "temporal": "1995-03-24T00:00:00Z/1996-12-21T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-20",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science",
-                "clouds",
-                "atmospheric winds",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Leslie Lait",
                 "hasEmail": "mailto:leslie.r.lait@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2769488162-LARC_ASDC",
             "description": "STRAT_Analysis_ER2_Data is the modeled trajectories and meteorological data along the flight path for the ER-2 aircraft collected during the Stratospheric Tracers of Atmospheric Transport (STRAT) campaign. Data collection for this product is complete.\r\n\r\nThe STRAT campaign was a field campaign conducted by NASA from May 1995 to February 1996. The primary goal of STRAT was to collect measurements of the change of long-lived tracers and functions of altitude, latitude, and season. These measurements were taken to aid with determining rates for global-scale transport and future distributions of high-speed civil transport (HSCT) exhaust that was emitted into the lower atmosphere. STRAT had four main objectives:  defining the rate of transport of trace gases from the stratosphere and troposphere (i.e., HSCT exhaust emissions), improving the understanding of dynamical coupling rates for transport of trace gases between tropical regions and higher latitudes and lower altitudes (between tropical regions, higher latitudes, and lower altitudes are where most ozone resides), improving understanding of chemistry in the upper troposphere and lower stratosphere, and finally, providing data sets for testing two-dimensional and three-dimensional models used in assessments of impacts from stratospheric aviation.  \r\n\r\nTo accomplish these objectives, the STRAT Science Team conducted various surface-based remote sensing and in-situ measurements. NASA flew the ER-2 aircraft along with balloons such as ozonesondes and radiosondes just below the tropopause in the Northern Hemisphere to collect data. Along with the ER-2 and balloons, NASA also utilized satellite imagery, theoretical models, and ground sites. The ER-2 collected data on HOx, NOy, CO2, ozone, water vapor, and temperature. The ER-2 also collected in-situ stratospheric measurements of N2O, CH4, CO, HCL, and NO using the Aircraft Laser Infrared Absorption Spectrometer (ALIAS). Ozonesondes and radiosondes were also deployed to collect data on CO2, NO/NOy, air temperature, pressure, and 3D wind. These balloons also took in-situ measurements of N2O, CFC-11, CH4, CO, HCL, and NO2 using the ALIAS. Ground stations were responsible for taking measurements of O3, ozone mixing ratio, pressure, and temperature. Satellites took infrared images of the atmosphere with the goal of aiding in completing STRAT objectives. Pressure and temperature models were created to help plan the mission.",
-            "title": "STRAT Analysis Model Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_Analysis_ER2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTRAT_Analysis_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/strat",
-                    "description": "ESPO Home Page for STRAT",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for STRAT",
+                    "downloadURL": "https://espo.nasa.gov/strat",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/strat/content/STRAT_Science_Overview",
-                    "description": "STRAT Science Overview",
                     "@type": "dcat:Distribution",
+                    "description": "STRAT Science Overview",
+                    "downloadURL": "https://espo.nasa.gov/strat/content/STRAT_Science_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2769488162-LARC_ASDC",
-                    "description": "Earthdata Search for STRAT_Analysis_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for STRAT_Analysis_ER2_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2769488162-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Analysis_ER2_Data_1",
-                    "description": "DOI for https://search.earthdata.nasa.gov/search/granules?p=C2769488162-LARC_ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for https://search.earthdata.nasa.gov/search/granules?p=C2769488162-LARC_ASDC",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Analysis_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/Analysis_ER2_Data_1/",
-                    "description": "ASDC Direct Data Download for STRAT_Analysis_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for STRAT_Analysis_ER2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/STRAT/Analysis_ER2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2769488162-LARC_ASDC",
+            "issued": "1995-04-27",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science",
+                "clouds",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STRAT_Analysis_ER2_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-12-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-2.14 -180.0 -2.14 180.0 68.23 180.0 68.23 -180.0 -2.14 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-03-24T00:00:00Z/1996-12-21T00:00:00Z",
             "theme": [
                 "STRAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STRAT Analysis Model Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-EXT1-V1.0",
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
+            "description": "This data set contains CODMAC\nlevel 4 science data acquired by the ROSINA COPS sensor between\n2015-12-30 and 2016-04-05 during the Extension phase 1 of the\nRosetta mission to comet 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-ext1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-EXT1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-ext1-v1.0",
-            "description": "This data set contains CODMAC\nlevel 4 science data acquired by the ROSINA COPS sensor between\n2015-12-30 and 2016-04-05 during the Extension phase 1 of the\nRosetta mission to comet 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 4 EXT1 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 4 EXT1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0412-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-06T14:23:25.000 to 2014-11-06T23:09:52.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0412-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0412-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0412-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-06T14:23:25.000 to 2014-11-06T23:09:52.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0412 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0412 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3WRAS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending 28-Day Running Mean Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3WRAS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending 28-Day Running Mean Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "ocean winds",
-                "earth science"
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
-            "identifier": "C2491757185-POCLOUD",
-            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal\ntime scales. This particular data set is the 28-Day running mean, Ascending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending 28-Day Running Mean Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending 28-Day Running Mean Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMIA_28DAY-RUNNINGMEAN_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal\ntime scales. This particular data set is the 28-Day running mean, Ascending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WRAS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WRAS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMIA_28DAY-RUNNINGMEAN_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMIA_28DAY-RUNNINGMEAN_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
-                    "description": "Information on observatory maneuvers, anomalies and other events",
                     "@type": "dcat:Distribution",
+                    "description": "Information on observatory maneuvers, anomalies and other events",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757185-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757185-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757185-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757185-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMIA_28DAY-RUNNINGMEAN_V5.jpg",
+            "identifier": "C2491757185-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "ocean winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3WRAS",
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
+            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending 28-Day Running Mean Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:55:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending 28-Day Running Mean Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-J-IRIS-5-GRS-ATMOS-PARAMS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The data set contains Jovian atmospheric parameters derived from spectra obtained with the Voyager infrared interferometer spectrometer (IRIS). The data set is ordered by time as measured by the Flight Data System Count (FDSC). This represents the data frame number modulo 60. Also included in the data set are information on pointing and associated geometry of the measurements and brightness temperatures obtained from measured radiances at selected wavenumbers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-j-iris-5-grs-atmos-params-v1.0_a3kd-qime",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "voyager",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-J-IRIS-5-GRS-ATMOS-PARAMS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-j-iris-5-grs-atmos-params-v1.0_a3kd-qime",
-            "description": "The data set contains Jovian atmospheric parameters derived from spectra obtained with the Voyager infrared interferometer spectrometer (IRIS). The data set is ordered by time as measured by the Flight Data System Count (FDSC). This represents the data frame number modulo 60. Also included in the data set are information on pointing and associated geometry of the measurements and brightness temperatures obtained from measured radiances at selected wavenumbers.",
-            "title": "VG1/VG2 JUPITER IRIS DERIVED GREAT RED SPOT PARAMETERS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1/VG2 JUPITER IRIS DERIVED GREAT RED SPOT PARAMETERS V1.0"
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
-                "incident",
-                "arrival",
-                "rnav",
-                "aviation",
-                "safety"
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
-            "identifier": "NASA-825",
             "description": "A sampling of reports from flight crew of rotary wing aircraft.",
-            "title": "Aviation Safety Reporting System: Rotary Wing Aircraft Flight Crew Reports",
-            "programCode": [
-                "026:021"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -454264,164 +454242,200 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-825",
+            "issued": "2018-06-25",
+            "keyword": [
+                "incident",
+                "arrival",
+                "rnav",
+                "aviation",
+                "safety"
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
+            "title": "Aviation Safety Reporting System: Rotary Wing Aircraft Flight Crew Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625655-GES_DISC.html",
             "citation": "Goddard Laboratory for Atmospheres at NASA GSFC. 1995-01-01. TOVSADTN. Version 01. TOVS GLA DAILY GRIDS from TIROSN V01. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOVSADTN_01.html. Digital Science Data.",
-            "issued": "1978-11-29",
-            "temporal": "1978-11-29T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1979-07-01",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "land surface",
-                "oceans",
-                "atmospheric temperature",
-                "earth science",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "ocean temperature",
-                "precipitation",
-                "surface thermal properties",
-                "atmosphere",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOEL SUSSKIND",
                 "hasEmail": "mailto:joel.susskind-1@nasa.gov"
             },
+            "creator": "Goddard Laboratory for Atmospheres at NASA GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1274625655-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This dataset (TOVSADTN) contains the TIROS Operational Vertical Sounder (TOVS) level 3 geophysical parameters derived using data from TIROS-N and the physical retrieval method of Susskind et al. (1984) and processed by the Satellite Data Utilization Office of the Goddard Laboratory for Atmospheres at NASA/GSFC. This method, which is hydrodynamic model- and a priori data-dependent, is designated as the so-called Path A scheme by the TOVS Pathfinder Science Working Group. The 20 channel High resolution Infrared Radiation Sounder 2 (HIRS2) and the 4 channel Microwave Sounding Unit (MSU) aboard the NOAA-xx series of Polar Orbiting Satellites are used to produce global fields of the 3-dimensional temperature-moisture structure of the atmosphere. In addition to profiles of temperature and moisture, the HIRS2/MSU data are used to derive important quantities such as land and sea surface temperature, outgoing longwave radiation, cloud fraction, cloudtop height, total ozone overburden and precipitation estimates.\n\nThe Path A system steps through an interactive forecast-retrieval-analysis cycle. In each 6 hour synoptic period, a 2nd order General Circulation Model (Takacs et al., 1994) is used to generate the 6 hour forecast fields of temperature and humidity. These global fields are used as the first guess for all soundings occuring within a 6 hour time window centered upon the forecast time. These retrievals are then assimilated with all available insitu measurements (such as radiosonde and ship reports) in the 6 hour interval using an Optimal Interpolation (OI) analysis scheme developed by the Data Assimilation Office of the Goddard Laboratory for Atmospheres. This analysis is then used to specify the initial conditions for the next 6 hour forecast, thus completing the cycle.\n\nThe retrieval algorithm itself is a physical method based on the iterative relaxation technique originally proposed by Chahine (1968). The basic approach consists of modifying the temperature profile from the previous iteration by an amount proportional to the difference between the observed brightness temperatures and the brightness temperatures computed from the trial parameters using the full radiative transfer equation applied at the observed satellite zenith angle. For the case of the temperature profile, the updated layer mean temperatures are given as a linear combination of multichannel brightness temperature differences with the coefficients given by the channel weighting functions. Constraints are imposed upon the solution in order to ensure stability and convergence of the iterative process. For more details see Susskind et al (1984).\n\nThere are level 3 data product files for five TOVS satellites, each of which is in the HDF format and each representative of a different averaging time period. All files contain the same number of geophysical parameter arrays stored as HDF Scientific Data Sets (SDSs). The time periods include daily, 5 day (pentad) and monthly, with the AM and PM portions of the orbits treated separately.  All data are mapped to a 1 degree longitude by 1 degree latitude global grid.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TOVSADTN",
-            "creator": "Goddard Laboratory for Atmospheres at NASA GSFC",
-            "title": "TOVS GLA DAILY GRIDS from TIROSN V01 (TOVSADTN) at GES DISC",
-            "graphic-preview-description": "TOVSADTN image",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADTN_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADTN_01.png",
-                    "description": "TOVSADTN image",
                     "@type": "dcat:Distribution",
+                    "description": "TOVSADTN image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADTN_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSADTN_01.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSADTN_01.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_Starter_Kit.pdf",
-                    "description": "This document is TOVS legacy documentation.  Some information may be obsolete.",
                     "@type": "dcat:Distribution",
+                    "description": "This document is TOVS legacy documentation.  Some information may be obsolete.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_Starter_Kit.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADTN",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADTN",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSADTN+001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSADTN+001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADND/doc/README.TOVSPathA.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSADND/doc/README.TOVSPathA.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_PATHFINDER_PATH_A_DATASET_GUIDE.pdf",
-                    "description": "This document is a TOVS legacy data guide.  Some information may be obsolete.",
                     "@type": "dcat:Distribution",
+                    "description": "This document is a TOVS legacy data guide.  Some information may be obsolete.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOVS/TOVS_PATHFINDER_PATH_A_DATASET_GUIDE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "TOVSADTN image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSADTN_01.png",
+            "identifier": "C1274625655-GES_DISC",
+            "issued": "1978-11-29",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "land surface",
+                "oceans",
+                "atmospheric temperature",
+                "earth science",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "ocean temperature",
+                "precipitation",
+                "surface thermal properties",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625655-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1979-07-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TOVSADTN",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-11-29T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "TOVS Pathfinder",
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOVS GLA DAILY GRIDS from TIROSN V01 (TOVSADTN) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-2-EDR-EROS%2FORBIT-V1.0",
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
+            "description": "This data set contains the NEAR magnetometer (MAG) data for the EROS/ORBIT phase. The data set begins on 2000-01-11T00:00:00.000 and ends 2001-02-12T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw magnetometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-2-edr-eros-orbit-v1.0_a3mx-4wgm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-2-EDR-EROS%2FORBIT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-2-edr-eros-orbit-v1.0_a3mx-4wgm",
-            "description": "This data set contains the NEAR magnetometer (MAG) data for the EROS/ORBIT phase. The data set begins on 2000-01-11T00:00:00.000 and ends 2001-02-12T23:59:59.999 . The data are raw telemetry data, provided in engineering units, that have been reformatted into FITS file format (NASA Office of Science and Technology (NOST), 100-1.0). In addition to the raw magnetometer data, a calibration file and algorithm are available. This data set is archived as a set of CDROM images as a part of the NEAR EDR volume set.",
-            "title": "NEAR MAG DATA FOR EROS/ORBIT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR MAG DATA FOR EROS/ORBIT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a3s4-zqy3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Prolonged skeletal unloading through bedrest results in bone loss similar to that observed in elderly osteoporotic patients but with an accelerated timeframe. This rapid effect on weight-bearing bones is also observed in astronauts who lose up to 2% of their bone mass per month spent in Space. Despite important implications for Spaceflight travellers and bedridden patients on Earth the exact mechanisms involved in disuse osteoporosis have not been elucidated. Parathyroid hormone-related protein (PTHrP) regulates many physiological processes including skeletal development and has been proposed as a gravisensor. To investigate the role of PTHrP in microgravity-induced bone loss trabecular osteoblasts (TOs) from Pthrp+/+ and -/- mice were exposed to simulated microgravity for 6 days. Viability of TOs decreased in inverse proportion to PTHrP expression levels. Microarray analysis of Pthrp+/+ TOs after 6 days at 0g revealed expression changes in genes encoding prolactins,apoptosis and survival molecules bone metabolism and extra-cellular matrix composition proteins chemokines IGF family and Wnt-related signalling molecules. Importantly 88% of 0g-induced expression changes in Pthrp+/+ cells overlap those observed in Pthrp-/- cells in normal gravity. Pulsatile treatment with PTHrP1-36 peptide during microgravity exposure reversed a large proportion of 0g-induced changes in Pthrp+/+ TOs. Our results confirm PTHrP efficacy as an anabolic agent to prevent microgravity-induced cell death in TOs. Total RNA samples extracted from Pthrp+/+and -/- trabecular osteoblasts (TOs) exposed for 6 days to simulated 0g in Synthecon rotating cell or left 6 days in culture at 1g. Cells had either been treated with a pulsatile treatment (2 h/day) of PTHrP1-36 peptide (10-8M) or received a change in growth medium. In total: 8 different conditions with 2 replicates each i.e. Pthrp+/+ TOs at 0g or 1g with or without PTHrP1-36 treatment and Pthrp-/- TOs at 0g or 1 g,with or without PTHrP1-36 treatment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-107",
+                    "mediaType": "text/html",
+                    "title": "The Role of PTHrP in Osteoblast Response to Microgravity: Implications for Osteoporosis Development."
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-107_a3s4-zqy3",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse78980-1",
                 "array scanning protocol",
@@ -454436,47 +454450,35 @@
                 "hybridization protocol",
                 "labelling protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a3s4-zqy3",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-107_a3s4-zqy3",
-            "description": "Prolonged skeletal unloading through bedrest results in bone loss similar to that observed in elderly osteoporotic patients but with an accelerated timeframe. This rapid effect on weight-bearing bones is also observed in astronauts who lose up to 2% of their bone mass per month spent in Space. Despite important implications for Spaceflight travellers and bedridden patients on Earth the exact mechanisms involved in disuse osteoporosis have not been elucidated. Parathyroid hormone-related protein (PTHrP) regulates many physiological processes including skeletal development and has been proposed as a gravisensor. To investigate the role of PTHrP in microgravity-induced bone loss trabecular osteoblasts (TOs) from Pthrp+/+ and -/- mice were exposed to simulated microgravity for 6 days. Viability of TOs decreased in inverse proportion to PTHrP expression levels. Microarray analysis of Pthrp+/+ TOs after 6 days at 0g revealed expression changes in genes encoding prolactins,apoptosis and survival molecules bone metabolism and extra-cellular matrix composition proteins chemokines IGF family and Wnt-related signalling molecules. Importantly 88% of 0g-induced expression changes in Pthrp+/+ cells overlap those observed in Pthrp-/- cells in normal gravity. Pulsatile treatment with PTHrP1-36 peptide during microgravity exposure reversed a large proportion of 0g-induced changes in Pthrp+/+ TOs. Our results confirm PTHrP efficacy as an anabolic agent to prevent microgravity-induced cell death in TOs. Total RNA samples extracted from Pthrp+/+and -/- trabecular osteoblasts (TOs) exposed for 6 days to simulated 0g in Synthecon rotating cell or left 6 days in culture at 1g. Cells had either been treated with a pulsatile treatment (2 h/day) of PTHrP1-36 peptide (10-8M) or received a change in growth medium. In total: 8 different conditions with 2 replicates each i.e. Pthrp+/+ TOs at 0g or 1g with or without PTHrP1-36 treatment and Pthrp-/- TOs at 0g or 1 g,with or without PTHrP1-36 treatment.",
-            "title": "The Role of PTHrP in Osteoblast Response to Microgravity: Implications for Osteoporosis Development.",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-107",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "The Role of PTHrP in Osteoblast Response to Microgravity: Implications for Osteoporosis Development."
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "The Role of PTHrP in Osteoblast Response to Microgravity: Implications for Osteoporosis Development."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.52-color-survey&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains 52-color IR data  of asteroids, taken using a double circularly variable filter. The     short wavelength portion of the CVF covered the octave from 0.8 to 1.6 microns with 3 percent resolution, while the long wavelength portion   covered 1.5 to 2.6 microns with 5 percent resolution.  Most of the     data are unpublished other than in this PDS data set.",
+            "identifier": "urn:nasa:pds:gbo.ast.52-color-survey",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "(25) phocaea",
                 "none",
@@ -454600,235 +454602,209 @@
                 "(264) libussa",
                 "(258) tyche"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.52-color-survey&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.52-color-survey",
-            "description": "This data set contains 52-color IR data  of asteroids, taken using a double circularly variable filter. The     short wavelength portion of the CVF covered the octave from 0.8 to 1.6 microns with 3 percent resolution, while the long wavelength portion   covered 1.5 to 2.6 microns with 5 percent resolution.  Most of the     data are unpublished other than in this PDS data set.",
-            "title": "52-COLOR ASTEROID SURVEY",
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
+            "title": "52-COLOR ASTEROID SURVEY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0309-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-21T16:47:05.000 to 2014-09-22T02:47:04.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0309-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0309-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0309-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-21T16:47:05.000 to 2014-09-22T02:47:04.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0309 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0309 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-PCME-V1.0",
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
-                "pluto"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "During the period 1985-1990, the earth entered the orbital plane of Pluto and its moon Charon, and the mutual eclipse events were observed from ground-based observatories. A subset of these data are included in this data set, and more will be added in future updates. The current version contains photoelectric photometry data from thirty-nine events observed at Mauna Kea Observatory by Tholen, and CCD photometry data from fifteen events observed at Palomar Observatory by Buratti and colleagues.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-pcme-v1.0_a48s-xu9p",
+            "issued": "2018-06-26",
+            "keyword": [
+                "pluto"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-PCME-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-pcme-v1.0_a48s-xu9p",
-            "description": "During the period 1985-1990, the earth entered the orbital plane of Pluto and its moon Charon, and the mutual eclipse events were observed from ground-based observatories. A subset of these data are included in this data set, and more will be added in future updates. The current version contains photoelectric photometry data from thirty-nine events observed at Mauna Kea Observatory by Tholen, and CCD photometry data from fifteen events observed at Palomar Observatory by Buratti and colleagues.",
-            "title": "PLUTO-CHARON MUTUAL EVENTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PLUTO-CHARON MUTUAL EVENTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPFLX-3-RDR-HALLEY-V1.0",
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
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Photometry and Polarimetry Network collected 18495 fluxes for the Narrowband Photometry Subnetwork. These data span the dates from 1985 August 24 to 1987 March 04.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppflx-3-rdr-halley-v1.0_a49u-my9j",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPFLX-3-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppflx-3-rdr-halley-v1.0_a49u-my9j",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The Photometry and Polarimetry Network collected 18495 fluxes for the Narrowband Photometry Subnetwork. These data span the dates from 1985 August 24 to 1987 March 04.",
-            "title": "IHW COMET HALLEY PHOTOMETRIC FLUXES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY PHOTOMETRIC FLUXES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/AMSR2/GCOMW1/3A-DAY/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_3GPROFGCOMW1AMSR2_DAY. Version 07. GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/AMSR2/GCOMW1/3A-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_DAY_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-02-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "precipitation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264134685-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\n3GPROF products provide global gridded monthly/daily precipitation averages from multiple satellites that can be used for climate studies. The 3GPROF products are based on retrievals from high-quality microwave sensors, which are sensitive to liquid and ice-phase precipitation hydrometeors in the atmosphere.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3GPROFGCOMW1AMSR2_DAY",
-            "creator": "GPM Science Team",
-            "title": "GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2_DAY) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from AMSR2 (25 km x 25 km)(GPM_3GPROFGCOMW1AMSR2_DAY)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_DAY_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSR2%2FGCOMW1%2F3A-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSR2%2FGCOMW1%2F3A-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_DAY_07.png",
-                    "description": "Surface Precipitation from AMSR2 (25 km x 25 km)(GPM_3GPROFGCOMW1AMSR2_DAY)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from AMSR2 (25 km x 25 km)(GPM_3GPROFGCOMW1AMSR2_DAY)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_DAY_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_DAY_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3GPROFGCOMW1AMSR2_DAY_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFGCOMW1AMSR2_DAY.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3GPROFGCOMW1AMSR2_DAY.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFGCOMW1AMSR2_DAY.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L3/GPM_3GPROFGCOMW1AMSR2_DAY.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFGCOMW1AMSR2_DAY_07.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/dods/GPM_3GPROFGCOMW1AMSR2_DAY_07.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFGCOMW1AMSR2_DAY_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3GPROFGCOMW1AMSR2_DAY_07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm.nasa.gov",
-                    "description": "GPM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GPM Project Home Page",
+                    "downloadURL": "https://gpm.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/doc/README.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
@@ -454838,161 +454814,196 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/stout/helpdesk/filespec.GPM.V7.pdf",
-                    "description": "FILE SPECIFICATION DOCUMENT",
                     "@type": "dcat:Distribution",
+                    "description": "FILE SPECIFICATION DOCUMENT",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/stout/helpdesk/filespec.GPM.V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://suzaku.eorc.jaxa.jp/GCOM_W/w_amsr2/amsr2_body_main.html",
-                    "description": "Instrument Description from JAXA",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from JAXA",
+                    "downloadURL": "https://suzaku.eorc.jaxa.jp/GCOM_W/w_amsr2/amsr2_body_main.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/amsr2.php",
-                    "description": "Instrument Description from NOAA",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from NOAA",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/amsr2.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/gpm_anomalous.html",
-                    "description": "GPM and partner sensors anomalous events",
                     "@type": "dcat:Distribution",
+                    "description": "GPM and partner sensors anomalous events",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/gpm_anomalous.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 }
             ],
+            "graphic-preview-description": "Surface Precipitation from AMSR2 (25 km x 25 km)(GPM_3GPROFGCOMW1AMSR2_DAY)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3GPROFGCOMW1AMSR2_DAY_07.png",
+            "identifier": "C2264134685-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/AMSR2/GCOMW1/3A-DAY/07",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_3GPROFGCOMW1AMSR2_DAY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-02-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM AMSR-2 on GCOM-W1 (GPROF) Radiometer Precipitation Profiling L3 1 day 0.25 degree x 0.25 degree V07 (GPM_3GPROFGCOMW1AMSR2_DAY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=V15%2FV16-V-ROE-5-OCC-ELECTRON-DENS-V1.0",
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
-                "venus",
-                "venera 15 and 16"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains 29 ionospheric electron density profiles (EDS files)\nderived from Venera 15 and 16 radio occultation data. A total of 155\nprofiles are believed to be available and it is hoped that all will\neventually be archived.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.v15-v16-v-roe-5-occ-electron-dens-v1.0_a4ag-mvzb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "venera 15 and 16"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=V15%2FV16-V-ROE-5-OCC-ELECTRON-DENS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.v15-v16-v-roe-5-occ-electron-dens-v1.0_a4ag-mvzb",
-            "description": "This dataset contains 29 ionospheric electron density profiles (EDS files)\nderived from Venera 15 and 16 radio occultation data. A total of 155\nprofiles are believed to be available and it is hoped that all will\neventually be archived.",
-            "title": "V15/V16 VENUS ROE 5 OCC ELECTRON DENS V1.0",
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
+            "title": "V15/V16 VENUS ROE 5 OCC ELECTRON DENS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5D50JXV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Unified Sea Ice Thickness Climate Data Record, 1947 Onward, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5D50JXV.",
-            "issued": "1947-01-01",
-            "temporal": "1947-01-01T00:00:00Z/2017-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-01",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "cryosphere",
-                "snow/ice",
-                "sea ice"
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
-            "identifier": "C1386206541-NSIDCV0",
             "description": "The Unified Sea Ice Thickness Climate Data Record, 1947 Onward is the result of a concerted effort to collect as many observations as possible of Arctic and Antarctic sea ice draft, freeboard, and thickness and to format them consistently with clear documentation, allowing the scientific community to better utilize what is now a considerable body of observations.",
-            "title": "Unified Sea Ice Thickness Climate Data Record, 1947 Onward, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5D50JXV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5D50JXV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G10006_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G10006_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5D50JXV",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5D50JXV",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5D50JXV",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5D50JXV",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206541-NSIDCV0",
+            "issued": "1947-01-01",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "cryosphere",
+                "snow/ice",
+                "sea ice"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5D50JXV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 60.0 180.0 90.0",
+            "temporal": "1947-01-01T00:00:00Z/2017-01-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Unified Sea Ice Thickness Climate Data Record, 1947 Onward, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a4dq-tqd3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John M. Kusterer",
+                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
+            },
+            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consists of half orbit (Night and Day) emissivity and cloud particle data assigned to IIR pixels on a 1 km grid centered on the Lidar track.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l2_swath_beta_v3_30_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000139",
             "issued": "2018-06-25",
-            "temporal": "2011-11-01/2013-02-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "atmospheric science",
                 "satellite",
@@ -455002,1057 +455013,1027 @@
                 "cloud",
                 "eos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a4dq-tqd3",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000139",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consists of half orbit (Night and Day) emissivity and cloud particle data assigned to IIR pixels on a 1 km grid centered on the Lidar track.",
-            "title": "CALIPSO Imaging Infrared Radiometer L2 Data Swath V3",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l2_swath_beta_v3_30_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2011-11-01/2013-02-28",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Imaging Infrared Radiometer L2 Data Swath V3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0608-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-27T22:22:20.000 to 2015-02-28T00:18:56.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0608-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0608-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0608-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-27T22:22:20.000 to 2015-02-28T00:18:56.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0608 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0608 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0863-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-28T06:05:20.000 to 2015-06-28T16:06:39.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0863-v1.0_a4gi-zm9i",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0863-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0863-v1.0_a4gi-zm9i",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-28T06:05:20.000 to 2015-06-28T16:06:39.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0863 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0863 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT3-MTP035-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Ext3 Phase from 26th Sep 2016 to 30th Sep 2016 when at the vicinity of target 67P/CG. 30th Sep 2016 is the end of the Rosetta mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext3-mtp035-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT3-MTP035-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext3-mtp035-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Ext3 Phase from 26th Sep 2016 to 30th Sep 2016 when at the vicinity of target 67P/CG. 30th Sep 2016 is the end of the Rosetta mission.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 3 MTP035 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 3 MTP035 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PWS-2-SA-4.0SEC",
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
+            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 1 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Jovian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of intensities (16 channels) is the time of the beginning of the scan. During data gaps where complete 4-second spectra are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. When one or more channels are missing within a scan, the missing measurements are zero-filled. Data are edited but not calibrated. The data numbers in this data set can be plotted in raw form for event searches and simple trend analysis since they are roughly proportional to the log of the electric field strength. Calibration procedures and tables are provided for use with this data set described below.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pws-2-sa-4.0sec_a4xk-fugm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PWS-2-SA-4.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pws-2-sa-4.0sec_a4xk-fugm",
-            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 1 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Jovian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of intensities (16 channels) is the time of the beginning of the scan. During data gaps where complete 4-second spectra are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. When one or more channels are missing within a scan, the missing measurements are zero-filled. Data are edited but not calibrated. The data numbers in this data set can be plotted in raw form for event searches and simple trend analysis since they are roughly proportional to the log of the electric field strength. Calibration procedures and tables are provided for use with this data set described below.",
-            "title": "VOYAGER 1 JUP PLASMA SPECTROMETER EDITED SPEC 4.0SEC",
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
+            "title": "VOYAGER 1 JUP PLASMA SPECTROMETER EDITED SPEC 4.0SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-DAN-3%2F4-RDR-V1.0",
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
-                "mars science laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Reduced housekeeping and scientific data collected from the Dynamic Albedo of Neutron Detector (DAN) aboard the Mars Science Laboratory.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-dan-3-4-rdr-v1.0_a4xp-i9b7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-DAN-3%2F4-RDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-dan-3-4-rdr-v1.0_a4xp-i9b7",
-            "description": "Reduced housekeeping and scientific data collected from the Dynamic Albedo of Neutron Detector (DAN) aboard the Mars Science Laboratory.",
-            "title": "MSL DYNAMIC ALBEDO OF NEUTRONS LEVEL 3/4 RDR V1.0",
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
+            "title": "MSL DYNAMIC ALBEDO OF NEUTRONS LEVEL 3/4 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1095",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cardoso, M.F., G.C. Hurtt, B. Moore, C.A. Nobre, and H. Bain. 2012. LBA-ECO LC-08 Passive Ground-based Fire Data, Para and Mato Grosso Brazil: 2001-2002. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1095",
-            "issued": "2023-10-03",
-            "temporal": "2002-07-12T00:00:00Z/2002-07-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "human dimensions",
-                "natural hazards",
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
-            "identifier": "C2780129991-ORNL_CLOUD",
             "description": "This data set reports observations of fires in the vicinity of Maraba, Para, Brazil, from November 3-5th, 2001, and in Mato Grosso, Brazil, between Cuiaba and Alta Floresta, for July 12-15th, 2002. These ground-based data were collected by visual inspection from roads primarily during daylight hours. Data include fire position and time, estimates of fire size, and type of vegetation burned. There is one comma-delimited ASCII file with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-08 Passive Ground-based Fire Data, Para and Mato Grosso Brazil: 2001-2002",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1095",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1095",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC08_Fire_Observations/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC08_Fire_Observations/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC08_Fire_Observations.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC08_Fire_Observations.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1095",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1095",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_Fire_Observations/comp/LC08_Fire_Observations.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_Fire_Observations/comp/LC08_Fire_Observations.pdf",
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
+            "identifier": "C2780129991-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "human dimensions",
+                "natural hazards",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1095",
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
             "spatial": "-56.5 -15.7 -55.1 -9.7",
+            "temporal": "2002-07-12T00:00:00Z/2002-07-15T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-08 Passive Ground-based Fire Data, Para and Mato Grosso Brazil: 2001-2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ102GDC_NRT.021",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2022-01-26. VIIRS/JPSS1 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m NRT. Version 2.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ102GDC_NRT.021. https://doi.org/10.5067/VIIRS/VJ102GDC.021.",
-            "issued": "2022-01-20",
-            "temporal": "2022-01-20T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-01",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VINCENT Chiang",
                 "hasEmail": "mailto:kwo-fu.chiang@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2210613276-LANCEMODIS",
-            "description": "The VIIRS/JPSS1 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m Near Real Time (NRT) product, short-name VJ102GDC_NRT contains unaggregated, calibrated TOA radiances for those VIIRS sub-pixel samples that are aggregated along-scan during post-calibration ground processing. In other words, this file contains the calibrated M1 - M5, M7 and M13 dual gain band data from the nadir and near-nadir zones that would otherwise be discarded following post-calibration aggregation/Earth View Radiometric Calibration Unit.\r\n\r\nThe Level-1 and Level-2 swath products are generated from the processing of 6 minutes of VIIRS data acquired during the JPSS1 satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 micron to 11.45 micron. There are also 7 dual-gain VIIRS bands. The dual gain moderate resolution bands (M1 to M5, M7 and M13) have 6304 samples and the other moderate resolution bands have 3200.\r\n\r\nFor additional information, see the Algorithm Theoretical Basis Document (ATBD) for the L1B product (https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/NASARevisedJPSSVIIRSRadCalATBD2014.pdf). The document describes how VIIRS operates in space and provides the equations implemented by the L1B software to generate the MODIS Level-1 intermediate products. It is a summary document that presents the formulae and error budges used to transform VIIRS digital counts to radiance and reflectance.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS1 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750 m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/JPSS1 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m Near Real Time (NRT) product, short-name VJ102GDC_NRT contains unaggregated, calibrated TOA radiances for those VIIRS sub-pixel samples that are aggregated along-scan during post-calibration ground processing. In other words, this file contains the calibrated M1 - M5, M7 and M13 dual gain band data from the nadir and near-nadir zones that would otherwise be discarded following post-calibration aggregation/Earth View Radiometric Calibration Unit.\r\n\r\nThe Level-1 and Level-2 swath products are generated from the processing of 6 minutes of VIIRS data acquired during the JPSS1 satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 micron to 11.45 micron. There are also 7 dual-gain VIIRS bands. The dual gain moderate resolution bands (M1 to M5, M7 and M13) have 6304 samples and the other moderate resolution bands have 3200.\r\n\r\nFor additional information, see the Algorithm Theoretical Basis Document (ATBD) for the L1B product (https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/NASARevisedJPSSVIIRSRadCalATBD2014.pdf). The document describes how VIIRS operates in space and provides the equations implemented by the L1B software to generate the MODIS Level-1 intermediate products. It is a summary document that presents the formulae and error budges used to transform VIIRS digital counts to radiance and reflectance.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ102GDC_NRT.021",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ102GDC_NRT.021",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
                     "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ102GDC_NRT/",
-                    "description": "Direct access to data from MODAPS public site.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to data from MODAPS public site.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ102GDC_NRT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2210613276-LANCEMODIS",
+            "issued": "2022-01-20",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ102GDC_NRT.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-02-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-01-20T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750 m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1677",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cuenca, R., and Y. Hagimoto. 2019. AirMOSS: In Situ Soil Moisture and Tree Measurements, Harvard Forest, 2012-2013. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1677",
-            "issued": "2019-11-12",
-            "temporal": "2012-10-15T00:00:00Z/2013-08-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "ecosystems",
-                "land surface",
-                "soils",
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
-            "identifier": "C2258527524-ORNL_CLOUD",
             "description": "This dataset provides in situ measurements of soil temperature, moisture, conductivity, measured diameter of tree at breast height (DBH) and total height collected at the Harvard Forest, Petersham, Massachusetts, USA, during October 2012 and July - August 2013. These measurements were collected in support of the Airborne Microwave Observatory of Subcanopy and Subsurface (AirMOSS) project to validate root-zone soil measurements and carbon flux model estimates.",
-            "graphic-preview-description": "Canopy image taken at Harvard Forest, 2012-10-18, Transect 2, plot 56. Source: companion file Photos_2012-10-18.zip.",
-            "title": "AirMOSS: In Situ Soil Moisture and Tree Measurements, Harvard Forest, 2012-2013",
-            "graphic-preview-file": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_Field_Data_Harvard_Fig1.JPG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1677",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1677",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_Field_Data_Harvard/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_Field_Data_Harvard/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_Field_Data_Harvard.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_Field_Data_Harvard.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1677",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1677",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/AirMOSS_Field_Data_Harvard.pdf",
-                    "description": "AirMOSS: In Situ Soil Moisture and Tree Measurements, Harvard Forest, 2012-2013: AirMOSS_Field_Data_Harvard.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: In Situ Soil Moisture and Tree Measurements, Harvard Forest, 2012-2013: AirMOSS_Field_Data_Harvard.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/AirMOSS_Field_Data_Harvard.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2012-10-15.zip",
-                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2012-10-15.zip",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2012-10-15.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2012-10-15.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2012-10-18.zip",
-                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2012-10-18.zip",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2012-10-18.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2012-10-18.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2013-07-10.zip",
-                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2013-07-10.zip",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2013-07-10.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2013-07-10.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2013-07-12.zip",
-                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2013-07-12.zip",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2013-07-12.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2013-07-12.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2013-08-19.zip",
-                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2013-08-19.zip",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2013-08-19.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2013-08-19.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2013-08-22.zip",
-                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2013-08-22.zip",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: Soil Moisture Profiles and Tree Measurements, Harvard Forest, 2012-2013: Photos_2013-08-22.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_Field_Data_Harvard/comp/Photos_2013-08-22.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_Field_Data_Harvard_Fig1.JPG",
-                    "description": "Canopy image taken at Harvard Forest, 2012-10-18, Transect 2, plot 56. Source: companion file Photos_2012-10-18.zip.",
                     "@type": "dcat:Distribution",
+                    "description": "Canopy image taken at Harvard Forest, 2012-10-18, Transect 2, plot 56. Source: companion file Photos_2012-10-18.zip.",
+                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_Field_Data_Harvard_Fig1.JPG",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airmoss.ornl.gov",
-                    "description": "AirMOSS campaign site",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS campaign site",
+                    "downloadURL": "https://airmoss.ornl.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Canopy image taken at Harvard Forest, 2012-10-18, Transect 2, plot 56. Source: companion file Photos_2012-10-18.zip.",
+            "graphic-preview-file": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_Field_Data_Harvard_Fig1.JPG",
+            "identifier": "C2258527524-ORNL_CLOUD",
+            "issued": "2019-11-12",
+            "keyword": [
+                "ecosystems",
+                "land surface",
+                "soils",
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1677",
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
             "spatial": "-72.18 42.54 -71.18 42.55",
+            "temporal": "2012-10-15T00:00:00Z/2013-08-22T23:59:59Z",
             "theme": [
                 "AirMOSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMOSS: In Situ Soil Moisture and Tree Measurements, Harvard Forest, 2012-2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/6T1X2JVKREZU",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Little Washita Micronet Soil Moisture Data: Oklahoma, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/6T1X2JVKREZU.",
-            "issued": "2003-06-01",
-            "temporal": "2003-06-01T00:00:00Z/2003-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-08-31",
-            "keyword": [
-                "earth science",
-                "soils",
-                "agriculture",
-                "land temperature",
-                "land surface"
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
-            "identifier": "C1386204245-NSIDCV0",
             "description": "This data set contains soil moisture data from the Little Washita Creek Watershed in southwestern Oklahoma, USA.",
-            "title": "SMEX03 Little Washita Micronet Soil Moisture Data: Oklahoma, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6T1X2JVKREZU",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6T1X2JVKREZU",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ground_soil_moisture/soil_moisture_network/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ground_soil_moisture/soil_moisture_network/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ground_soil_moisture/soil_moisture_network/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ground_soil_moisture/soil_moisture_network/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6T1X2JVKREZU",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/6T1X2JVKREZU",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6T1X2JVKREZU",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/6T1X2JVKREZU",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204245-NSIDCV0",
+            "issued": "2003-06-01",
+            "keyword": [
+                "earth science",
+                "soils",
+                "agriculture",
+                "land temperature",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/6T1X2JVKREZU",
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
             "spatial": "-98.2 34.8 -97.9 35.1",
+            "temporal": "2003-06-01T00:00:00Z/2003-08-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Little Washita Micronet Soil Moisture Data: Oklahoma, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206624-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seasonal frost penetration, Sleepers River Research Watershed, Vermont, USA, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1983-01-01",
-            "temporal": "1983-01-01T00:00:00Z/1992-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1992-12-31",
-            "keyword": [
-                "snow/ice",
-                "biosphere",
-                "cryosphere",
-                "earth science",
-                "frozen ground",
-                "land surface",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Roberts",
                 "hasEmail": "mailto:wproberts@rsgisc.crrel.usace.army.mil"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206624-NSIDCV0",
             "description": "The frost tube network is located within a 3.25-square-mile sub-watershed of the Sleepers River Research Watershed near Danville, Vermont, USA. Tubes were positioned in forested and non-forested cover types. The forest cover includes beech, birch, maple hardwoods with a 7% slope and 240 degree aspect, mixed conifer (spruce and balsam) and hardwoods with a 3% slope and 240 degree aspect, and coniferous forest with a 3% slope and 240 degree aspect. The open areas include two large non-cultivated agricultural fields (with approximate 5% slopes and aspects of 240 and 15 degrees) and a small heavily instrumented opening. Site data were generally recorded weekly. Snow depth was measured with a metal meter ruler while frost readings were measured from a plastic tube filled with methylene blue dye suspended in a PVC outer tube. Data cover winter seasons 1983-84 to 1992-93 only. These data are presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Seasonal frost penetration, Sleepers River Research Watershed, Vermont, USA, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD278_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD278_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD278/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD278/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD278/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD278/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206624-NSIDCV0",
+            "issued": "1983-01-01",
+            "keyword": [
+                "snow/ice",
+                "biosphere",
+                "cryosphere",
+                "earth science",
+                "frozen ground",
+                "land surface",
+                "vegetation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206624-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1992-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-72.177 44.422 -72.039 44.53",
+            "temporal": "1983-01-01T00:00:00Z/1992-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Seasonal frost penetration, Sleepers River Research Watershed, Vermont, USA, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL20.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Sea Ice Freeboard V004. Version 004. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL20.004.",
-            "issued": "2018-10-14",
-            "temporal": "2018-10-14T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-31",
-            "keyword": [
-                "cryosphere",
-                "sea ice",
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
-            "identifier": "C2753295020-NSIDC_CPRD",
             "description": "ATL20 contains daily and monthly gridded estimates of sea ice freeboard, derived from along-track freeboard estimates in the ATLAS/ICESat-2 L3A Sea Ice Freeboard product (ATL10). Data are gridded at 25 km using the SSM/I Polar Stereographic Projection.",
-            "title": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Sea Ice Freeboard V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL20.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL20.004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL20+V004",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL20+V004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2753295020-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2753295020-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL20.004",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL20.004",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL20.004",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL20.004",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2753295020-NSIDC_CPRD",
+            "issued": "2018-10-14",
+            "keyword": [
+                "cryosphere",
+                "sea ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL20.004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-10-14T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3B Daily and Monthly Gridded Sea Ice Freeboard V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1155",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bliss, N. 2013. LBA-ECO LC-08 Soil, Vegetation, and Land Cover Maps for Brazil and South America. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1155",
-            "issued": "2013-04-15",
-            "temporal": "1981-01-01T00:00:00Z/1991-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-18",
-            "keyword": [
-                "land surface",
-                "vegetation",
-                "biosphere",
-                "land use/land cover",
-                "earth science",
-                "soils"
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
-            "identifier": "C2768945067-ORNL_CLOUD",
             "description": "This data set provides (1) soil maps for Brazil that are digital versions of the MAPA DE SOLOS DO BRASIL (EMBRAPA, 1981) classified at three levels of detail, 19-class, 70-class and 249-class; (2) vegetation maps for Brazil that are digital versions of the MAPA DE VEGETACAO DO BRASIL (IBGE, 1988) classified at three levels of detail, 13-class, 59-class, and an overprint (combination) class; and (3) a land cover map for all of South America that was derived from National Oceanic and Atmospheric Administration (NOAA) Advanced Very High Resolution Radiometer (AVHRR) data over the time period 1987 through 1991 (Stone et al., 1994).The seven soil, vegetation, and general land cover classification maps are provided as GeoTIFF files (*.tif) files. There are also three companion files (.pdf), one each, for the soil, vegetation, and land cover maps, with information on  map units, class values, codes, and descriptions.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-08 Soil, Vegetation, and Land Cover Maps for Brazil and South America",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1155_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1155",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1155",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC08_EOS_Maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC08_EOS_Maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC08_EOS_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC08_EOS_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1155",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1155",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_EOS_Maps/comp/BrazilVegMap_class_aux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_EOS_Maps/comp/BrazilVegMap_class_aux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_EOS_Maps/comp/Brazil_Soils_Map_class_aux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_EOS_Maps/comp/Brazil_Soils_Map_class_aux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_EOS_Maps/comp/LC08_EOS_Maps.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_EOS_Maps/comp/LC08_EOS_Maps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_EOS_Maps/comp/SA_lc_Map_41class_aux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC08_EOS_Maps/comp/SA_lc_Map_41class_aux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1155_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1155_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1155",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1155",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1155_1_fit.png",
+            "identifier": "C2768945067-ORNL_CLOUD",
+            "issued": "2013-04-15",
+            "keyword": [
+                "land surface",
+                "vegetation",
+                "biosphere",
+                "land use/land cover",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1155",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-81.36 -34.84 -30.0 12.47",
+            "temporal": "1981-01-01T00:00:00Z/1991-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-08 Soil, Vegetation, and Land Cover Maps for Brazil and South America"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/651/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bryan Matthews",
                 "hasEmail": "mailto:bryan.l.matthews@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_651",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 673",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_1.zip",
-                    "description": "Tail 673 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 673 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_2.zip",
-                    "description": "Tail 673 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 673 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_3.zip",
-                    "description": "Tail 673 Set 3",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 673 Set 3",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_4.zip",
-                    "description": "Tail 673 Set 4",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 673 Set 4",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_5.zip",
-                    "description": "Tail 673 Set 5",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 673 Set 5",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_6.zip",
-                    "description": "Tail 673 Set 6",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 673 Set 6",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_7.zip",
-                    "description": "Tail 673 Set 7",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 673 Set 7",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_8.zip",
-                    "description": "Tail_673 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_673 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_8.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_9.zip",
-                    "description": "Tail_673 Set 9\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_673 Set 9\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_673_9.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_673_9.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_651",
+            "issued": "2012-12-04",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/651/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 673"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHRC/AMSU-A/DATA401",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Spencer, Roy W and John R Christy.2018. AMSU/MSU Lowstratosphere Day/Month Temperature Anomalies and Annual Cycle V6 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GHRC/AMSU-A/DATA401",
-            "issued": "2018-10-24",
-            "temporal": "1978-01-01T00:00:00Z/2022-05-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmospheric temperature",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C1996545162-GHRC_DAAC",
             "description": "The AMSU/MSU Lowstratosphere Day/Month Temperature Anomalies and Annual Cycle V6 dataset consists of temperature anomalies and annual cycle temperatures derived from the Microwave Sounding Unit (MSU) and the Advanced Microwave Sounding Unit-A (AMSU-A) radiance data since January 1978. All products are derived for the lower stratosphere. The dataset begins on January 1, 1978 and is still currently ongoing. The data are available in netCDF-4 and ASCII formats.",
-            "title": "AMSU/MSU Lowstratosphere Day/Month Temperature Anomalies and Annual Cycle V6",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHRC%2FAMSU-A%2FDATA401",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHRC%2FAMSU-A%2FDATA401",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=msutls",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=msutls",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/airtemp_climatology/doc/msut_v6_dataset.pdf",
-                    "description": "AMSU/MSU Day/Month Temperature Anomalies and Annual Cycle V6 Datasets User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "AMSU/MSU Day/Month Temperature Anomalies and Annual Cycle V6 Datasets User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/airtemp_climatology/doc/msut_v6_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1007/s13143-017-0010-y",
-                    "description": "UAH Version 6 global satellite temperature products: Methodology and results",
                     "@type": "dcat:Distribution",
+                    "description": "UAH Version 6 global satellite temperature products: Methodology and results",
+                    "downloadURL": "https://doi.org/10.1007/s13143-017-0010-y",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/airtemp_climatology/doc/CDRP-ATBD-0108_Rev3_MeanLayerTemperature-UAH-JRC-170601.pdf",
-                    "description": "Mean Layer Temperature - UAH - Climate Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Mean Layer Temperature - UAH - Climate Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/airtemp_climatology/doc/CDRP-ATBD-0108_Rev3_MeanLayerTemperature-UAH-JRC-170601.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
+            "identifier": "C1996545162-GHRC_DAAC",
+            "issued": "2018-10-24",
+            "keyword": [
+                "atmospheric temperature",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHRC/AMSU-A/DATA401",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-01-01T00:00:00Z/2022-05-03T00:00:00Z",
             "theme": [
                 "NOT APPLICABLE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSU/MSU Lowstratosphere Day/Month Temperature Anomalies and Annual Cycle V6"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a5a8-w6pp",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-02-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "atmospheric correction",
-                "ocean winds",
-                "aerosol",
-                "misr"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kirk Knobelspiesse",
                 "hasEmail": "mailto:kirk.knobelspiesse@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA"
-            },
-            "identifier": "https://data.nasa.gov/api/views/a5a8-w6pp",
             "description": "This dataset shows an example result from the MISR Maximum Likelihood (MLI) algorithm, which uses the MISR 866nm channel multi-angle observations to derive 4 parameters:\n- Aerosol Optical Depth (866nm)\n- Aerosol fine side mode fraction\n- Aerosol \"relative humidity\" (water content)\n- Ocean surface wind speed\n\nAn information content assessment of the parameters of this retrieval can be found here:\nhttps://amt.copernicus.org/preprints/amt-2020-423/\n\nThe ultimate goal is to produce a research evaluation dataset with the MISR MLI algorithm. Results, and they become ready, will be posted here. MISR MLI is intended to act as an atmospheric correction that can be applied to coincident MODIS-Terra observations.",
-            "title": "MOCMAC_MISR_MLI",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -456060,460 +456041,458 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.nasa.gov/api/views/a5a8-w6pp",
+            "issued": "2021-02-11",
+            "keyword": [
+                "atmospheric correction",
+                "ocean winds",
+                "aerosol",
+                "misr"
+            ],
+            "landingPage": "https://data.nasa.gov/d/a5a8-w6pp",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA"
+            },
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MOCMAC_MISR_MLI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/doi:10.5067/YDY73WVBPISF",
             "citation": "Daniel Tong at Geroge Mason University . 2023-04-18. HAQES_NA_PM25_BC_CENSUS. Version 1. HAQES 3-Hourly Ensemble mean surface PM2.5 Black Carbon concentration at census level, North America V1.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/doi:10.5067/YDY73WVBPISF. https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_BC_CENSUS_1.html. Digital Science Data.",
-            "issued": "2023-04-15",
-            "temporal": "2022-11-01T00:00:00Z/2023-05-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-15",
-            "references": [
-                "https://doi.org/%20http%3A//doi.org/10.1016/j.atmosenv.2015.11.004"
-            ],
-            "keyword": [
-                "public health",
-                "air quality",
-                "human dimensions",
-                "aerosols",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Suhung Shen",
                 "hasEmail": "mailto:suhung.shen-1@nasa.gov"
             },
+            "creator": "Daniel Tong at Geroge Mason University",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2623694409-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product provides HAQES 3-hourly ensemble mean surface PM2.5 Black Carbon concentration at the census level over the continental United States (CONUS). \n\nThe Hazardous Air Quality Ensemble System (HAQES) is a real-time ensemble forecast of hazardous air quality events, such as wildfires, dust storms, and Volcanic eruptions. Both regional and global models from multiple agencies are used to create the ensemble, including the Goddard Earth Observing System (GEOS) from the National Aeronautics and Space Administration (NASA), the Navy Aerosol Analysis and Prediction System (NAAPS) from Naval Research Laboratory, the Global Ensemble Forecast System Aerosols (GEFS), High-Resolution Rapid Refresh (HRRR), and National Oceanic and Atmospheric Administration-U.S. Environmental Protection Agency (NOAA-EPA) Atmosphere-Chemistry Coupler-Community Multiscale Air Quality model (NACC-CMAQ) from NOAA.  The prototypes of HAQES products were developed by the George Mason University Air Quality Laboratory as part of the NASA Health Air Quality Applied Science Team (HAQAST).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HAQES_NA_PM25_BC_CENSUS",
-            "creator": "Daniel Tong at Geroge Mason University",
-            "graphic-preview-description": "Sample image: The surface PM2.5 black carbon concentration at the census level from the HAQES model for November 12, 2022 at 18:00Z.",
-            "title": "HAQES 3-Hourly Ensemble mean surface PM2.5 Black Carbon concentration at census level, North America V1 (HAQES_NA_PM25_BC_CENSUS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_BC_CENSUS_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYDY73WVBPISF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FYDY73WVBPISF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_BC_CENSUS_1.png",
-                    "description": "Sample image: The surface PM2.5 black carbon concentration at the census level from the HAQES model for November 12, 2022 at 18:00Z.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image: The surface PM2.5 black carbon concentration at the census level from the HAQES model for November 12, 2022 at 18:00Z.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_BC_CENSUS_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_BC_CENSUS.1/doc/README_HAQES_PM25_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_BC_CENSUS.1/doc/README_HAQES_PM25_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_BC_CENSUS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_BC_CENSUS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_BC_CENSUS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_BC_CENSUS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQES_NA_PM25_BC_CENSUS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQES_NA_PM25_BC_CENSUS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Sample image: The surface PM2.5 black carbon concentration at the census level from the HAQES model for November 12, 2022 at 18:00Z.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_BC_CENSUS_1.png",
+            "identifier": "C2623694409-GES_DISC",
+            "issued": "2023-04-15",
+            "keyword": [
+                "public health",
+                "air quality",
+                "human dimensions",
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/doi:10.5067/YDY73WVBPISF",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/%20http%3A//doi.org/10.1016/j.atmosenv.2015.11.004"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "HAQES_NA_PM25_BC_CENSUS",
             "spatial": "-132.0 21.0 -58.5 53.5",
+            "temporal": "2022-11-01T00:00:00Z/2023-05-08T00:00:00Z",
             "theme": [
                 "HAQAST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HAQES 3-Hourly Ensemble mean surface PM2.5 Black Carbon concentration at census level, North America V1 (HAQES_NA_PM25_BC_CENSUS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-EXT3-V2.0",
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
+            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the extended mission 3 phase (EXT3). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jul 2016 and 30 Sep 2016. This version of the data has been reprocessed to remove an error introduced in the previous version.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-ext3-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-EXT3-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-ext3-v2.0",
-            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the extended mission 3 phase (EXT3). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 01 Jul 2016 and 30 Sep 2016. This version of the data has been reprocessed to remove an error introduced in the previous version.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 3 EXT3 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P RPCIES 3 EXT3 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-HGAAPM-V1.0",
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
+            "description": "This CODMAC level 3 data set contains the key parameters of the HGA Housekeeping. In particular, it provides information on the measured Azimuth & Elevation angles, as well as different pointing errors and displacement errors.  It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-hgaapm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-HGAAPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-hgaapm-v1.0",
-            "description": "This CODMAC level 3 data set contains the key parameters of the HGA Housekeeping. In particular, it provides information on the measured Azimuth & Elevation angles, as well as different pointing errors and displacement errors.  It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA HIGH GAIN ANTENNA             \n                             ENGINEERING DATA",
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
+            "title": "ROSETTA HIGH GAIN ANTENNA             \n                             ENGINEERING DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/664/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bryan Matthews",
                 "hasEmail": "mailto:bryan.l.matthews@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_664",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 687",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_1.zip",
-                    "description": "Tail 687 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 687 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_2.zip",
-                    "description": "Tail 687 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 687 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_3.zip",
-                    "description": "Tail_687 Set 3\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_687 Set 3\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_4.zip",
-                    "description": "Tail_687 Set 4\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_687 Set 4\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_5.zip",
-                    "description": "Tail_687 Set 5\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_687 Set 5\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_6.zip",
-                    "description": "Tail_687 Set 6\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_687 Set 6\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_7.zip",
-                    "description": "Tail_687 Set 7\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_687 Set 7\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_8.zip",
-                    "description": "Tail_687 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_687 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_8.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_9.zip",
-                    "description": "Tail_687 Set 9\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_687 Set 9\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_687_9.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_687_9.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_664",
+            "issued": "2012-12-04",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/664/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 687"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/512/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-01-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
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
-            "identifier": "DASHLINK_512",
             "description": "Software Health Management (SWHM) is a new field that is concerned with the development of tools and technologies to enable automated detection, diagnosis, prediction, and mitigation of adverse events due to software anomalies.\r\nSignificant effort has been expended in the last several decades in the\r\ndevelopment of verification and validation methods for software\r\nintensive systems, but it is becoming increasingly more apparent that this is\r\nnot enough to guarantee that a complex software system\r\nmeets all safety and reliability requirements. \r\n\r\nModern software systems can exhibit a variety of failure modes which can go undetected in a verification and validation process.  While standard techniques for error handling, fault detection and isolation\r\ncan have significant benefits for many systems, it is becoming increasingly evident that new technologies and methods are necessary for the development of techniques to detect, diagnose, predict, and then mitigate the adverse events due to software that has already undergone significant verification and validation procedures.\r\nThese software faults often arise due to the interaction between the software\r\nand the operating environment.\r\nUnanticipated environmental changes lead to software anomalies that may have significant impact on the overall success of the mission.\r\nBecause software is ubiquitous, it is not sufficient that errors are\r\ndetected only after they occur. Rather, software must be instrumented and\r\nmonitored for failures before they happen.\r\nThis prognostic capability will yield safer and more dependable systems for the future.  This paper addresses the motivation, needs, and requirements of software health management as a new discipline.\r\n\r\nPublished in the Proceedings of the IEEE Conference on Space Mission Challenges for Information Technology, Palo Alto, CA, August 2011.",
-            "title": "The Case for Software Health Management",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/swhm.pdf",
-                    "description": "swhm.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "swhm.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/swhm.pdf",
+                    "mediaType": "application/pdf",
                     "title": "swhm.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_512",
+            "issued": "2012-01-27",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/512/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "The Case for Software Health Management"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/123",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Blad, B. L., and E. A. Walter-Shea. 1994. Surface Radiance Data: UNL (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.),Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/123",
-            "issued": "2024-05-05",
-            "temporal": "1987-05-30T00:00:00Z/1989-08-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "land surface",
-                "surface thermal properties",
-                "surface radiative properties",
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation",
-                "atmospheric water vapor"
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
-            "identifier": "C2980692342-ORNL_CLOUD",
             "description": "Canopy IR & air temperature, albedo, incoming and reflected shortwave, humidity",
-            "graphic-preview-description": "Browse Image",
-            "title": "Surface Radiance Data: UNL (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F123",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F123",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_unl_surf/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_unl_surf/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Surface_Radiance_Data_UNL.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Surface_Radiance_Data_UNL.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/123",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/123",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_unl_surf/comp/Surface_Radiance_Data_UNL.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_unl_surf/comp/Surface_Radiance_Data_UNL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_unl_surf/comp/surf_rad.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_unl_surf/comp/surf_rad.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_unl_surf/comp/unl_surf.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_unl_surf/comp/unl_surf.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
+            "identifier": "C2980692342-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "land surface",
+                "surface thermal properties",
+                "surface radiative properties",
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/123",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-96.59 38.98 -96.47 39.12",
+            "temporal": "1987-05-30T00:00:00Z/1989-08-11T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Surface Radiance Data: UNL (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0003. http://eosweb.larc.nasa.gov/project/scarb/scarb_table.",
-            "issued": "1999-11-15",
-            "temporal": "1995-06-01T00:00:00Z/1995-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "forest science",
-                "agriculture",
-                "biosphere",
-                "earth science",
-                "ecological dynamics"
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
-            "identifier": "C1337195037-LARC_ASDC",
             "description": "SCAR_B_G8_FIRE data are Smoke/Sulfates, Clouds and Radiation Experiment in Brazil, GOES-8 ABBA Diurnal Fire Product (1995 Fire Season) data.Smoke/Sulfates, Clouds and Radiation - Brazil (SCAR-B) data include physical and chemical components of the Earth's surface, the atmosphere and the radiation field collected in Brazil with an emphasis in biomass burning. SCAR-B, the third SCAR experiment, was completed in September 1995, studied the effects of biomass burning on atmospheric processes and aids in the preparation of new techniques for remote sensing of these processes from space.The objectives for the SCAR mission are: to advance our knowledge of how the physical, chemical and radiative processes in our atmosphere are affected by sulfate aerosol and smoke from biomass burning; to improve our expertise at remotely sensing smoke, water vapor, clouds, vegetation and fires; and to assess the effects of deforestation and biomass burning on tropical landscapes.The Cooperative Institute for Meteorological Satellite Studies (CIMSS) at the University of Wisconsin-Madison has produced diurnal GOES-8 derived fire products for the 1995 fire season (June-October 1995) with version 5.5 of the GOES-8 Automated Biomass Burning Algorithm (ABBA). The diurnal fire products were produced for 1145, 1445, 1745, and 2045 UTC coinciding with peak burning hours.The GOES-8 Automated Biomass Burning Algorithm (ABBA) fire products are derived from Geostationary Operational Environmental Satellite (GOES)-8 imager radiances from bands 1 (visible), 2 (3.9 micron), and 4 (11 micron).",
-            "title": "Smoke/Sulfates, Clouds and Radiation Experiment in Brazil (SCAR-B) Data Set Version 5.5",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FSCAR_B%2F0003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FSCAR_B%2F0003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -456565,27 +456544,50 @@
                     "title": "View this dataset's product usage"
                 }
             ],
+            "identifier": "C1337195037-LARC_ASDC",
+            "issued": "1999-11-15",
+            "keyword": [
+                "forest science",
+                "agriculture",
+                "biosphere",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-75.77 -39.87 -36.12 0.13",
+            "temporal": "1995-06-01T00:00:00Z/1995-10-31T23:59:59Z",
             "theme": [
                 "SCAR-B",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Smoke/Sulfates, Clouds and Radiation Experiment in Brazil (SCAR-B) Data Set Version 5.5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000. This version V2.0 supersedes previous deliveries of the same dataset. Note that the two datasets RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04-V1.0 and RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04B-V1.0 have been merged into one dataset: RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m04-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "achernar",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
@@ -456596,371 +456598,371 @@
                 "beta car",
                 "alpha sco"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m04-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000. This version V2.0 supersedes previous deliveries of the same dataset. Note that the two datasets RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04-V1.0 and RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04B-V1.0 have been merged into one dataset: RO-C-OSINAC-3-PRL-67PCHURYUMOV-M04-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
-            "title": "ROSETTA-ORBITER PRELANDING OSINAC 3 RDR MTP004 V2.0",
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
+            "title": "ROSETTA-ORBITER PRELANDING OSINAC 3 RDR MTP004 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSX-D-SPIRIT3-3-MSXZODY-V1.0",
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
-                "dust",
-                "midcourse space experiment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Midcourse Space Experiment (MSX) mid-infrared emission measurements from the zodiacal dust cloud in spectral bands centered at 8.3 12, 15, and 21 microns.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msx-d-spirit3-3-msxzody-v1.0_a5p6-g7rz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dust",
+                "midcourse space experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSX-D-SPIRIT3-3-MSXZODY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msx-d-spirit3-3-msxzody-v1.0_a5p6-g7rz",
-            "description": "The Midcourse Space Experiment (MSX) mid-infrared emission measurements from the zodiacal dust cloud in spectral bands centered at 8.3 12, 15, and 21 microns.",
-            "title": "MSX ZODIACAL DUST DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSX ZODIACAL DUST DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-09-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1.",
-            "issued": "2021-03-19",
-            "temporal": "2013-08-01T00:00:00Z/2013-09-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "atmospheric radiation",
-                "infrared wavelengths",
-                "atmosphere"
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
-            "identifier": "C2119341672-LARC_ASDC",
             "description": "SEAC4RS_Radiation_AircraftInSitu_ER2_Data are in-situ radiation data collected onboard the ER-2 aircraft during the Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEA4CRS) airborne field study. Data collection for this product is complete.\r\n\r\nThe Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEAC4RS) airborne field study was conducted in August and September of 2013. The field operation was based in Houston, Texas. The primary SEAC4RS science objectives are: to determine how pollutant emissions are redistributed via deep convection throughout the troposphere; to determine the evolution of gases and aerosols in deep convective outflow and the implications for upper troposphere and lower stratosphere (UT/LS) chemistry; to identify the influences and feedbacks of aerosol particles from anthropogenic pollution and biomass burning on meteorology and climate through changes in the atmospheric heat budget (i.e., semi-direct effect) or through microphysical changes in clouds (i.e., indirect effects); and lastly, to serve as a calibration and validation test bed for future satellite instruments and missions.\r\n\r\nThe airborne observational data were collected from three aircraft platforms: the NASA DC-8, ER-2, and SPEC LearJet. Both the NASA DC-8 and ER-2 aircraft were instrumented for comprehensive in-situ and remote sensing measurements of trace gas, aerosol properties, and cloud properties. In addition, radiative fluxes and meteorological parameters were also recorded. The NASA DC-8 was mostly responsible for tropospheric sampling, while the NASA ER-2 operated in the lower stratospheric regime. The SPEC LearJet was dedicated to in-situ cloud characterizations. To accomplish the science objectives, the flight plans were designed to investigate the influence of biomass burning and pollution, their temporal evolution, and ultimately, impacts on meteorological processes which can, in turn, feedback on regional air quality. With respect to meteorological feedbacks, the opportunity to examine the impact of polluting aerosols on cloud properties and dynamics was of particular interest.",
-            "title": "SEAC4RS ER-2 Aircraft In-Situ Radiation Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to Cite ASDC Data",
                     "@type": "dcat:Distribution",
+                    "description": "How to Cite ASDC Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/SEAC4RS_DraftPlan_20130409b_USA.pdf",
-                    "description": "SEAC4RS Draft Plan",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Draft Plan",
+                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/SEAC4RS_DraftPlan_20130409b_USA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
-                    "description": "SEAC4RS/DC3 Data Management Plan",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS/DC3 Data Management Plan",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/seac4rs",
-                    "description": "SEAC4RS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Project Home Page",
+                    "downloadURL": "https://espo.nasa.gov/seac4rs",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/topics/earth/features/seac4rs_2013.html",
-                    "description": "SEAC4RS nasa.gov feature article",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS nasa.gov feature article",
+                    "downloadURL": "https://www.nasa.gov/topics/earth/features/seac4rs_2013.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015JD024297",
-                    "description": "SEAC4RS Overview Paper",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Overview Paper",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015JD024297",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
-                    "description": "DOI data set landing page for SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341672-LARC_ASDC",
-                    "description": "Earthdata Search for SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341672-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/Radiation_AircraftInSitu_ER2_Data_1/",
-                    "description": "ASDC Direct Data Download for SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/Radiation_AircraftInSitu_ER2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2119341672-LARC_ASDC",
+            "issued": "2021-03-19",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "atmospheric radiation",
+                "infrared wavelengths",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_Radiation_AircraftInSitu_ER2_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>15.0 -127.0 15.0 -82.0 53.0 -82.0 53.0 -127.0 15.0 -127.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-08-01T00:00:00Z/2013-09-24T23:59:59.999Z",
             "theme": [
                 "SEAC4RS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEAC4RS ER-2 Aircraft In-Situ Radiation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ERBE/S10_WFOV_NF_NAT_L3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-09-08. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ERBE/S10_WFOV_NF_NAT_L3.",
-            "issued": "1999-09-03",
-            "temporal": "1984-11-01T00:00:00Z/1990-02-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-04",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "BRUCE, DR. BARKSTROM",
                 "hasEmail": "mailto:b.r.barkstrom@larc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000802-LARC_ASDC",
             "description": "ERBE_S10_WFOV_NF_NAT_1 is the Earth Radiation Budget Experiment (ERBE) S-10 Wide Field of View (WFOV) Numerical Filter (NF) Earth Flux and Albedo data product. Data collection for this product is complete. It is available in the Native (NAT) Format.\r\n\r\nERBE was a multi-satellite system designed to measure the Earth's radiation budget. The ERBE instruments flew on a mid-inclination National Aeronautics and Space Administration (NASA) Earth Radiation Budget Satellite (ERBS) and two sun-synchronous National Oceanic and Atmospheric Administration (NOAA) satellites (NOAA-9 and NOAA-10). Each satellite carried both a scanner and a non-scanner instrument package. The non-scanner instrument package contained four Earth-viewing channels and a solar monitor. The Earth-viewing channels had two spatial resolutions: a horizon-to-horizon view of the Earth, and a field-of-view limited to about 1000 km in diameter. The former was called WFOV and the latter the medium field-of-view (MFOV) channels. The solar monitor was a direct descendant of the Solar Maximum Mission's Active Cavity Radiometer Irradiance Monitor detector. Due to the concern for spectral flatness and high accuracy, all five of the channels were active cavity radiometers. The MFOV (medium-field-of-view) SF (shape factor) S-10 contained inverted daily, monthly hourly, and monthly averages of shortwave and long-wave radiant fluxes at the top-of-the-atmosphere for one month. This data set was produced for each of the satellites (ERBS and NOAA-9) and the combination of satellites, which were operational during the data month. The values for this data set were derived using the shape factor technique (Smith et al. 1986). As described in the Earth Radiant Fluxes and Albedo, Scanner S-9, Non-scanner S-10/S-10N User's Guide, the data contains a 30 byte header, 67 scale factors which were used to scale the data in the first record, and 26 scale factors which were used to scale the data in the second record. The data set also contained two records for each processed region. The first record was of fixed length (990 words) and contained averaged data. The second record was of variable length and contained individual hour box estimates. The length of the second record, in words, was calculated by multiplying the number of hour boxes (978th word of record one) by the number of values stored for each hour box (38 for the non-scanner).",
-            "title": "Earth Radiation Budget Experiment (ERBE) S-10 Wide Field of View (WFOV) Numerical Filter (NF) Earth Flux and Albedo",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS10_WFOV_NF_NAT_L3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS10_WFOV_NF_NAT_L3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/ERBE",
-                    "description": "ASDC Data and Information for ERBE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for ERBE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/ERBE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ERBE/S10_WFOV_NF_NAT_L3",
-                    "description": "DOI data set landing page for ERBE_S10_WFOV_NF_NAT_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ERBE_S10_WFOV_NF_NAT_1",
+                    "downloadURL": "https://doi.org/10.5067/ERBE/S10_WFOV_NF_NAT_L3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000802-LARC_ASDC",
-                    "description": "Earthdata Search for ERBE_S10_WFOV_NF_NAT_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ERBE_S10_WFOV_NF_NAT_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000802-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/gbytes.c",
-                    "description": "Tools for storage/retrieval of arbitrary size bytes from 32 bit words - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Tools for storage/retrieval of arbitrary size bytes from 32 bit words - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/gbytes.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/io.c",
-                    "description": "Readme to work with FORTRAN - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to work with FORTRAN - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/io.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_project.pdf",
-                    "description": "ERBE Langley ASDC Project Document",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE Langley ASDC Project Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_s9_s10.pdf",
-                    "description": "ERBE Earth Radiant Fluxes and Albedo for Month (Scanner) (S-9)/Earth Radiant Fluxes and Albedo for Month (Nonscanner) (S-10) Langley ASDC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE Earth Radiant Fluxes and Albedo for Month (Scanner) (S-9)/Earth Radiant Fluxes and Albedo for Month (Nonscanner) (S-10) Langley ASDC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_s9_s10.pdf",
+                    "mediaType": "application/pdf",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s10_wfov_nf_nat.txt",
-                    "description": "ERBE S-10 Readme",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE S-10 Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s10_wfov_nf_nat.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/s10tape_regions.txt",
-                    "description": "ERBE tape region directory",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE tape region directory",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/s10tape_regions.txt",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/s9-10_readsoftware.zip",
-                    "description": "Read Software Package - ERBE_S9-10_Read_Software - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - ERBE_S9-10_Read_Software - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/s9-10_readsoftware.zip",
+                    "mediaType": "application/zip",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/GEWEX-RFA",
-                    "description": "ASDC Data and Information for GEWEX-RFA",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for GEWEX-RFA",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/GEWEX-RFA",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/a-burning-question",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"A Burning Question\" By Annette Varani",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"A Burning Question\" By Annette Varani",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/a-burning-question",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/absorption-of-solar-radiation-by-clouds-observations-versus-models",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"Absorption of Solar Radiation by Clouds: Observations versus Models\"",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"Absorption of Solar Radiation by Clouds: Observations versus Models\"",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/absorption-of-solar-radiation-by-clouds-observations-versus-models",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/QuestionConvection",
-                    "description": "NASA Earth Observatory Article: NASA Earth Observatory Article",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: NASA Earth Observatory Article",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/QuestionConvection",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/erbe_overview.pdf",
-                    "description": "ERBE Overview Document",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE Overview Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/erbe_overview.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S10/WFOV_NF_NAT_1/",
-                    "description": "ASDC Direct Data Download for ERBE_S10_WFOV_NF_NAT_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ERBE_S10_WFOV_NF_NAT_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S10/WFOV_NF_NAT_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000802-LARC_ASDC",
+            "issued": "1999-09-03",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ERBE/S10_WFOV_NF_NAT_L3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-01-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1984-11-01T00:00:00Z/1990-02-28T23:59:59.999Z",
             "theme": [
                 "ERBE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Earth Radiation Budget Experiment (ERBE) S-10 Wide Field of View (WFOV) Numerical Filter (NF) Earth Flux and Albedo"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC1-67PCHURYUMOV-M13-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc1-67pchuryumov-m13-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "calibration",
@@ -456969,72 +456971,82 @@
                 "dark",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC1-67PCHURYUMOV-M13-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc1-67pchuryumov-m13-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission at the comet 67P, covering the period from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSIWAC 2 EDR MTP013 V2.0",
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
+            "title": "ROSETTA-ORBITER COMET ESCORT 1 OSIWAC 2 EDR MTP013 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SA-ISSNA-5-PHOEBESHAPE-V2.0",
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
-                "cassini-huygens",
-                "s9 phoebe"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The shape model of Phoebe derived by Robert Gaskell from Cassini images. The model is provided in the implicitly connected quadrilateral (ICQ) format. This version of the model was prepared on August 4, 2012. Vertex-facet versions of the models are also provided.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sa-issna-5-phoebeshape-v2.0_a5va-exzy",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "s9 phoebe"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SA-ISSNA-5-PHOEBESHAPE-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sa-issna-5-phoebeshape-v2.0_a5va-exzy",
-            "description": "The shape model of Phoebe derived by Robert Gaskell from Cassini images. The model is provided in the implicitly connected quadrilateral (ICQ) format. This version of the model was prepared on August 4, 2012. Vertex-facet versions of the models are also provided.",
-            "title": "GASKELL PHOEBE SHAPE MODEL V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GASKELL PHOEBE SHAPE MODEL V2.0"
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
+                    "downloadURL": "http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/photon/",
+                    "mediaType": "image/fits"
+                }
+            ],
+            "identifier": "NASA-0000211",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "solar flares",
                 "space science",
@@ -457047,106 +457059,70 @@
                 "lat",
                 "astrophysics"
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
-            "identifier": "NASA-0000211",
-            "description": "Fermi is a powerful space observatory that will open a wide window on the universe. Gamma rays are the highest-energy form of light, and the gamma-ray sky is spectacularly different from the one we perceive with our own eyes. With a huge leap in all key capabilities, Fermi data will enable scientists to answer persistent questions across a broad range of topics, including supermassive black-hole systems, pulsars, the origin of cosmic rays, and searches for signals of new physics.",
-            "title": "LAT Pass 7 Reprocessed Weekly Files",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/photon/",
-                    "mediaType": "image/fits"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT Pass 7 Reprocessed Weekly Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-3-P-V1.0",
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
-                "viking",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the martian surface atmospheric pressure readings obtained through much of the duration of the Viking Lander 1 and 2 missions (data are included for Viking Lander 1 sols 0 - 2245 and Viking Lander 2 sols 0 - 1050). The data are derived from the ambient pressure sensor carried onboard the Landers and values are presented on a point by point basis. The sampling rate was variable throughout the mission maximum sampling rate was one measurement per second, but ranged up to 65 minutes for Lander 1 and 105 minutes for Lander 2. For further background information on the Viking Meteorology Instrument System (VMIS) and results from this experiment, see CHAMBERLAIN_ETAL1976, HESS_ETAL_1976A, HESS_ETAL_1976B, and HESS_ETAL_1977. For discussions of analyses of experiment data, see also TILLMAN_1977, HESS_ETAL_1980, and TILLMAN_1988. An earlier version of this data set is archived at the NSSDC (NSSDC ID 75-075C-07D and 75-083C-07D).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-3-p-v1.0_a64e-h5q9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "viking",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-3-P-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-3-p-v1.0_a64e-h5q9",
-            "description": "This data set contains the martian surface atmospheric pressure readings obtained through much of the duration of the Viking Lander 1 and 2 missions (data are included for Viking Lander 1 sols 0 - 2245 and Viking Lander 2 sols 0 - 1050). The data are derived from the ambient pressure sensor carried onboard the Landers and values are presented on a point by point basis. The sampling rate was variable throughout the mission maximum sampling rate was one measurement per second, but ranged up to 65 minutes for Lander 1 and 105 minutes for Lander 2. For further background information on the Viking Meteorology Instrument System (VMIS) and results from this experiment, see CHAMBERLAIN_ETAL1976, HESS_ETAL_1976A, HESS_ETAL_1976B, and HESS_ETAL_1977. For discussions of analyses of experiment data, see also TILLMAN_1977, HESS_ETAL_1980, and TILLMAN_1988. An earlier version of this data set is archived at the NSSDC (NSSDC ID 75-075C-07D and 75-083C-07D).",
-            "title": "VL1/VL2 MARS METEOROLOGY DATA CALIBRATED DATA PRESSURE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VL1/VL2 MARS METEOROLOGY DATA CALIBRATED DATA PRESSURE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-02-06",
-            "temporal": "2021-02-06T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coords",
-                "trajectory",
-                "space",
-                "location",
-                "coordinates",
-                "topo",
-                "iss",
-                "international",
-                "ephemeris",
-                "station"
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
-            "identifier": "nasa-iss-data_2021-02-06",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-02-06",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -457269,319 +457245,354 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-02-06",
+            "issued": "2021-02-06",
+            "keyword": [
+                "coords",
+                "trajectory",
+                "space",
+                "location",
+                "coordinates",
+                "topo",
+                "iss",
+                "international",
+                "ephemeris",
+                "station"
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
+            "temporal": "2021-02-06T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-02-06"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PRA-4-SUMM-BROWSE-48SEC-V1.0",
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
-                "voyager",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pra-4-summ-browse-48sec-v1.0_a64r-u95s",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PRA-4-SUMM-BROWSE-48SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pra-4-summ-browse-48sec-v1.0_a64r-u95s",
-            "description": "not applicable",
-            "title": "VG2 JUP PRA RESAMPLED SUMMARY BROWSE 48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 JUP PRA RESAMPLED SUMMARY BROWSE 48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1102-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-15T10:18:00.000 to 2015-10-15T17:26:17.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1102-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1102-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1102-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-15T10:18:00.000 to 2015-10-15T17:26:17.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1102 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1102 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-E-CONSERT-2-EAR2-V1.0",
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
-                "earth",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the EAR2 (Earth swing-by 2) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-e-consert-2-ear2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-E-CONSERT-2-EAR2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-e-consert-2-ear2-v1.0",
-            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the EAR2 (Earth swing-by 2) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER EARTH\n                           CONSERT 2 EAR2 V1.0",
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
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER EARTH\n                           CONSERT 2 EAR2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alcross_mmt_ccd47&version=1.0",
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
-                "lunar crater observation and sensing satellite",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains data collected from the MMT Observatory  CCD47 instrument during observations of the impact of the LCROSS spacecraft on the moon on October 9, 2009. The bundle contains raw data products.",
+            "identifier": "urn:nasa:pds:lcross_mmt_ccd47",
+            "issued": "2021-05-21",
+            "keyword": [
+                "lunar crater observation and sensing satellite",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alcross_mmt_ccd47&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:lcross_mmt_ccd47",
-            "description": "This bundle contains data collected from the MMT Observatory  CCD47 instrument during observations of the impact of the LCROSS spacecraft on the moon on October 9, 2009. The bundle contains raw data products.",
-            "title": "LCROSS MMT Observatory CCD47 Data Bundle",
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
+            "title": "LCROSS MMT Observatory CCD47 Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-EROS%2FORBIT-V1.0",
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
+            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-eros-orbit-v1.0_a6b9-iqdy",
+            "issued": "2018-06-26",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-EROS%2FORBIT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-eros-orbit-v1.0_a6b9-iqdy",
-            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
-            "title": "NEAR SPICE KERNELS EROS/ORBIT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR SPICE KERNELS EROS/ORBIT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD09GST.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-02-07. MODIS/Aqua Surface Reflectance Quality Daily L2G Global 1km SIN Grid NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MYD09GST.NRT.061.",
-            "issued": "2021-02-07",
-            "temporal": "2021-02-07T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-16",
-            "keyword": [
-                "earth science",
-                "national geospatial data asset",
-                "land surface",
-                "ngda",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MODAPS USER SUPPORT TEAM",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
-            },
-            "identifier": "C2007631676-LANCEMODIS",
-            "description": "The MODIS/Aqua Surface Reflectance Quality Daily L2G Global 1km SIN Grid Near Real Time (NRT) product, short name MYD09GST, is a restructured version of its primary input, the state QA data in MYD09_L2. This product summarizes the quality of the MYD09 products, specifically atmospheric and other correction states. The product contains quality assurance data pertaining to cloud and  cloud shadow, land and water designations, aerosols, and the data source of corrections performed on the file. The data set also contains the number of  observations for each pixel.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Aqua Surface Reflectance Quality Daily L2G Global 1km SIN Grid NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Surface Reflectance Quality Daily L2G Global 1km SIN Grid Near Real Time (NRT) product, short name MYD09GST, is a restructured version of its primary input, the state QA data in MYD09_L2. This product summarizes the quality of the MYD09 products, specifically atmospheric and other correction states. The product contains quality assurance data pertaining to cloud and  cloud shadow, land and water designations, aerosols, and the data source of corrections performed on the file. The data set also contains the number of  observations for each pixel.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09GST.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD09GST.NRT.061",
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
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MYD09GST",
-                    "description": "Direct access to the download site and directory hosting the MYD09GST 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MYD09GST 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MYD09GST",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2007631676-LANCEMODIS",
+            "issued": "2021-02-07",
+            "keyword": [
+                "earth science",
+                "national geospatial data asset",
+                "land surface",
+                "ngda",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD09GST.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-07T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Surface Reflectance Quality Daily L2G Global 1km SIN Grid NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NDC8-E-ASAR-4-RADAR-V1.0",
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
-                "geologic remote sensing field experiment",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "AIRSAR is the Jet Propulsion Laboratory's airborne polarimetric SAR that operates at C (5.66 cm), L (23.98 cm), and P (68.13 cm) wavelengths in a polarimetric mode (Zebker et al., 1987). AIRSAR acquires data that can be processed to backscatter image formats with range and azimuth resolutions of approximately 20 meters. The pixel values are expressed in radar backscatter cross section as 32-bit numbers. The cross section is the area of a half sphere that would scatter the amount of power received by the antenna.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ndc8-e-asar-4-radar-v1.0_a6db-dvmv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "geologic remote sensing field experiment",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NDC8-E-ASAR-4-RADAR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ndc8-e-asar-4-radar-v1.0_a6db-dvmv",
-            "description": "AIRSAR is the Jet Propulsion Laboratory's airborne polarimetric SAR that operates at C (5.66 cm), L (23.98 cm), and P (68.13 cm) wavelengths in a polarimetric mode (Zebker et al., 1987). AIRSAR acquires data that can be processed to backscatter image formats with range and azimuth resolutions of approximately 20 meters. The pixel values are expressed in radar backscatter cross section as 32-bit numbers. The cross section is the area of a half sphere that would scatter the amount of power received by the antenna.",
-            "title": "NASA DC-8 EARTH AIRSAR RESAMPLED RADAR IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NASA DC-8 EARTH AIRSAR RESAMPLED RADAR IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a6f6-sy24",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l1-valstage1-v3-00_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000193",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2009-06-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "satellite",
                 "climate",
@@ -457591,225 +457602,228 @@
                 "cloud",
                 "radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a6f6-sy24",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000193",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L1B Profile Data V3-00",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l1-valstage1-v3-00_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2009-06-10",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L1B Profile Data V3-00"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT2-MTP028-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Extension 2 Phase from 5th April 2016 to 3rd May 2016 when at the vicinity of target 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, clarification of calibration target, document updates and resolve other minor outstanding errata.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext2-mtp028-v1.1",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "alpha lyr",
                 "zeta cas",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT2-MTP028-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext2-mtp028-v1.1",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Extension 2 Phase from 5th April 2016 to 3rd May 2016 when at the vicinity of target 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, clarification of calibration target, document updates and resolve other minor outstanding errata.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 2 MTP028 V1.1",
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
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 2 MTP028 V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/20",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kustas, W. 1994. Bowen Ratio Surface Flux: GSFC (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/20",
-            "issued": "2024-05-05",
-            "temporal": "1987-05-26T00:00:00Z/1987-10-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "agriculture",
-                "earth science",
-                "land surface",
-                "atmosphere",
-                "precipitation",
-                "soils",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric water vapor",
-                "atmospheric winds"
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
-            "identifier": "C2979986671-ORNL_CLOUD",
             "description": "Surface flux measurements by Bowen Ratio technique during FIFE",
-            "graphic-preview-description": "Browse Image",
-            "title": "Bowen Ratio Surface Flux: GSFC (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_flux_30_min_brg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_flux_30_min_brg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Bowen_Ratio_GSFC.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Bowen_Ratio_GSFC.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/20",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/20",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brg/comp/Bowen_Ratio_GSFC.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brg/comp/Bowen_Ratio_GSFC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brg/comp/sflux_bg.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brg/comp/sflux_bg.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brg/comp/sf_30min.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_flux_30_min_brg/comp/sf_30min.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
+            "identifier": "C2979986671-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "agriculture",
+                "earth science",
+                "land surface",
+                "atmosphere",
+                "precipitation",
+                "soils",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric water vapor",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/20",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-96.61 38.98 -96.45 39.11",
+            "temporal": "1987-05-26T00:00:00Z/1987-10-16T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Bowen Ratio Surface Flux: GSFC (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3281-V1.0",
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
-                "mars",
-                "mars express"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-08T07:26:07.000 to 2012-05-08T09:25:54.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3281-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3281-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3281-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-08T07:26:07.000 to 2012-05-08T09:25:54.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3281 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3281 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a6mm-szmt",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The Heat Shock Factor A2 (HsfA2) as a part of the HSF network is essential to the plant  s response to almost any environmental stress and to the cellular homeostatic control mechanisms. Plant cell cultures disabled in HsfA2 function were grown aboard the International Space Station (ISS) in order to ascertain whether or not they use the same terrestrially effective systems to adapt to the novel environment of spaceflight. Cultured lines of Arabidopsis thaliana derived from wild type (WT) cultivar Col-0 and from a knock-out line deficient in the gene encoding HSFA2 (HSFA2 KO) were launched to the ISS on SpaceX-2 as part of the Cellular Expression Logic (CEL) experiment of the BRIC17 spaceflight mission and were fixed in-flight after 10 days on orbit. Microarray gene expression data were analyzed using a two-part comparative approach. First differentially expressed genes were identified between the environments (spaceflight to ground) within cells of the same genotype which represented physiological adaptation to the spaceflight environment. Second gene expression profiles were identified between the genotypes (HSFA2 KO to WT) within the same environment defining genes uniquely required by the two genotypes in the ground and spaceflight adapted states. The physiological state of the cells as a result of disabling a gene has tremendous control over the mechanisms induced to adapt to the environment of spaceflight. The HsfA2 demonstrated a role in the physiological adaptation to the spaceflight environment since the cells disabled in the HsfA2 gene used substantially different genes to achieve the spaceflight adapted state than the WT cells. The endoplasmic reticulum (ER) stress and unfolded protein response (UPR) define the HSFA2 KO cells   physiological state regardless of the environment and likely result from the deficiency in the chaperone-mediated protein folding machinery. HsfA2 seems to have a universal stress response role but also specific roles in the physiological adaptation to spaceflight through cell wall remodeling signal perception and transduction and starch biosynthesis. Implementation of knock-out cells identified a set of genes with a required expression level in order for a cell to achieve a spaceflight-adapted state. The HSFA2 KO cells helped to unravel the HsfA2-dependent genes of the adaption of wild type cells to the environment of spaceflight.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-205",
+                    "mediaType": "text/html",
+                    "title": "HSFA2 functions in the physiological adaptation of undifferentiated plant cells to spaceflight microgravity environment"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-205_a6mm-szmt",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "rna extraction",
                 "spaceflight",
@@ -457823,139 +457837,134 @@
                 "genotype",
                 "genelab microarray data processing protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a6mm-szmt",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-205_a6mm-szmt",
-            "description": "The Heat Shock Factor A2 (HsfA2) as a part of the HSF network is essential to the plant  s response to almost any environmental stress and to the cellular homeostatic control mechanisms. Plant cell cultures disabled in HsfA2 function were grown aboard the International Space Station (ISS) in order to ascertain whether or not they use the same terrestrially effective systems to adapt to the novel environment of spaceflight. Cultured lines of Arabidopsis thaliana derived from wild type (WT) cultivar Col-0 and from a knock-out line deficient in the gene encoding HSFA2 (HSFA2 KO) were launched to the ISS on SpaceX-2 as part of the Cellular Expression Logic (CEL) experiment of the BRIC17 spaceflight mission and were fixed in-flight after 10 days on orbit. Microarray gene expression data were analyzed using a two-part comparative approach. First differentially expressed genes were identified between the environments (spaceflight to ground) within cells of the same genotype which represented physiological adaptation to the spaceflight environment. Second gene expression profiles were identified between the genotypes (HSFA2 KO to WT) within the same environment defining genes uniquely required by the two genotypes in the ground and spaceflight adapted states. The physiological state of the cells as a result of disabling a gene has tremendous control over the mechanisms induced to adapt to the environment of spaceflight. The HsfA2 demonstrated a role in the physiological adaptation to the spaceflight environment since the cells disabled in the HsfA2 gene used substantially different genes to achieve the spaceflight adapted state than the WT cells. The endoplasmic reticulum (ER) stress and unfolded protein response (UPR) define the HSFA2 KO cells   physiological state regardless of the environment and likely result from the deficiency in the chaperone-mediated protein folding machinery. HsfA2 seems to have a universal stress response role but also specific roles in the physiological adaptation to spaceflight through cell wall remodeling signal perception and transduction and starch biosynthesis. Implementation of knock-out cells identified a set of genes with a required expression level in order for a cell to achieve a spaceflight-adapted state. The HSFA2 KO cells helped to unravel the HsfA2-dependent genes of the adaption of wild type cells to the environment of spaceflight.",
-            "title": "HSFA2 functions in the physiological adaptation of undifferentiated plant cells to spaceflight microgravity environment",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-205",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "HSFA2 functions in the physiological adaptation of undifferentiated plant cells to spaceflight microgravity environment"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "HSFA2 functions in the physiological adaptation of undifferentiated plant cells to spaceflight microgravity environment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567946-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2013-01-01. Group on Earth Observations (GEO) Global Agricultural Monitoring (GLAM) - Uganda. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
-            "issued": "1972-01-01",
-            "temporal": "1972-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "earth science",
-                "agricultural plant science",
-                "food science",
-                "plant commodities",
-                "agriculture"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EUGENE FOSNIGHT",
                 "hasEmail": "mailto:fosnight@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220567946-USGS_LTA",
-            "description": "The objective of GEO is to fulfil a vision of a world where decisions and actions are informed by coordinated, comprehensive and sustained Earth Observation (EO). This is being pursued mainly through the added value of co-ordinating existing institutions, organised communities, space agencies, in-situ monitoring agencies, scientific institutions, research centres, universities, modelling centres, technology developers and other groups that deal with one or more aspects of EO. To reach this over arching goal, GEO focuses on capacity development in three dimensions: infrastructure, individuals and institutions. In the field of agriculture, the general goal is to promote the utilisation of Earth observations for advancing sustainable agriculture, aquaculture and fisheries. Key issues include early warning, risk assessment, food security, market efficiency and combating desertification.\n\n(Source: http://www.research-europe.com/index.php/2011/08/joao-soares-secretariat-expert-for-agriculture-group-on-earth-observations/)",
             "creator": "U.S. Geological Survey",
-            "title": "USGS Group on Earth Observations (GEO) Global Agricultural Monitoring (GLAM) Uganda",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The objective of GEO is to fulfil a vision of a world where decisions and actions are informed by coordinated, comprehensive and sustained Earth Observation (EO). This is being pursued mainly through the added value of co-ordinating existing institutions, organised communities, space agencies, in-situ monitoring agencies, scientific institutions, research centres, universities, modelling centres, technology developers and other groups that deal with one or more aspects of EO. To reach this over arching goal, GEO focuses on capacity development in three dimensions: infrastructure, individuals and institutions. In the field of agriculture, the general goal is to promote the utilisation of Earth observations for advancing sustainable agriculture, aquaculture and fisheries. Key issues include early warning, risk assessment, food security, market efficiency and combating desertification.\n\n(Source: http://www.research-europe.com/index.php/2011/08/joao-soares-secretariat-expert-for-agriculture-group-on-earth-observations/)",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.earthobservations.org/geoss_ag_tar.shtml",
-                    "description": "\n         Group on Earth Observations (GEO) Global Agricultural Monitoring (GLAM)\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Group on Earth Observations (GEO) Global Agricultural Monitoring (GLAM)\n      ",
+                    "downloadURL": "http://www.earthobservations.org/geoss_ag_tar.shtml",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C1220567946-USGS_LTA",
+            "issued": "1972-01-01",
+            "keyword": [
+                "earth science",
+                "agricultural plant science",
+                "food science",
+                "plant commodities",
+                "agriculture"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567946-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOI/USGS/EROS"
+            },
             "spatial": "29.5 -1.5 35.0 4.0",
+            "temporal": "1972-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "GLAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Group on Earth Observations (GEO) Global Agricultural Monitoring (GLAM) Uganda"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0035-3-SDSSMOC-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Sloan Digital Sky Survey (SDSS) Moving Object Catalog 3rd release lists astrometric and photometric data for moving objects detected in the SDSS. The catalog includes various identification parameters, SDSS astrometric measurements (five SDSS magnitudes and their errors), and orbital elements for previously cataloged asteroids. The data set also includes a list of the runs from which data are included, and filter response curves.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0035-3-sdssmoc-v2.0_a6nn-w84h",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "asteroid",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0035-3-SDSSMOC-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0035-3-sdssmoc-v2.0_a6nn-w84h",
-            "description": "The Sloan Digital Sky Survey (SDSS) Moving Object Catalog 3rd release lists astrometric and photometric data for moving objects detected in the SDSS. The catalog includes various identification parameters, SDSS astrometric measurements (five SDSS magnitudes and their errors), and orbital elements for previously cataloged asteroids. The data set also includes a list of the runs from which data are included, and filter response curves.",
-            "title": "SDSS MOVING OBJECT CATALOG V2.0",
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
+            "title": "SDSS MOVING OBJECT CATALOG V2.0"
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
+            "description": "EPPS, GRNS, MAG, MASCS, MDIS, MLA, RSS, SPICE, XRS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090415.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-777",
+            "issued": "2018-06-25",
             "keyword": [
                 "mascs",
                 "mag",
@@ -457968,141 +457977,110 @@
                 "xrs",
                 "grns"
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
-            "identifier": "NASA-777",
-            "description": "EPPS, GRNS, MAG, MASCS, MDIS, MLA, RSS, SPICE, XRS",
-            "title": "PDS MESSENGER Data Release 4",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090415.shtml",
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
+            "title": "PDS MESSENGER Data Release 4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3398-V1.0",
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
-                "mars",
-                "mars express"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-09-10T04:55:39.000 to 2012-09-10T07:35:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3398-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3398-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3398-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-09-10T04:55:39.000 to 2012-09-10T07:35:09.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3398 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3398 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0789-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-19T00:01:25.000 to 2015-05-19T06:53:22.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0789-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0789-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0789-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-19T00:01:25.000 to 2015-05-19T06:53:22.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0789 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0789 V1.0"
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
-                "models",
-                "turbulence",
-                "incompressible",
-                "flow",
-                "cases"
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
-            "identifier": "NASA-845__14",
             "description": "This grouping contains more recent incompressible-flow cases.",
-            "title": "Collaborative Testing of Turbulence Models: More Recent Incompressible Flow Cases",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -458110,710 +458088,708 @@
                     "mediaType": "application/x-gzip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-845__14",
+            "issued": "2018-06-25",
+            "keyword": [
+                "models",
+                "turbulence",
+                "incompressible",
+                "flow",
+                "cases"
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
+            "title": "Collaborative Testing of Turbulence Models: More Recent Incompressible Flow Cases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Aerosol_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Aerosol_AircraftInSitu_DC8_Data_1.",
-            "issued": "2022-09-12",
-            "temporal": "2002-12-13T00:00:00Z/2003-02-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-13",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bruce Anderson",
                 "hasEmail": "mailto:bruce.e.anderson@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836911-LARC_ASDC",
             "description": "SOLVE2_Aerosol_AircraftInSItu_DC8_Data is the in-situ aerosol data for the DC-8 aircraft collected during the SAGE III Ozone Loss and Validation Experiment II (SOLVE II). Data were collected by instruments such as the TSI Model 3760 Concdensation Nuclei Counter (TSI 3760), TSI 3563 Nephelometer, Cloud, Aerosol, and Precipitation Spectrometer (CAPS), Condensation Nuclei Counter (CNC), Focused Cavity Aerosol Spectrometer II (FCAS II), and the Nucleation-Mode Aerosol Size Spectrometer II (N-MASS). Data collection for this product is complete. \r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE II DC-8 Aircraft In-situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE2_Aerosol_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE2_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cloud1.arc.nasa.gov/solve/index.html",
-                    "description": "SOLVE Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "SOLVE Project Home Page",
+                    "downloadURL": "https://cloud1.arc.nasa.gov/solve/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/solve",
-                    "description": "ESPO Home Page for SOLVE",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for SOLVE",
+                    "downloadURL": "https://espo.nasa.gov/solve",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to Cite ASDC Data",
                     "@type": "dcat:Distribution",
+                    "description": "How to Cite ASDC Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/solve/content/SOLVE_Science_Overview",
-                    "description": "SOLVE I Science Overview",
                     "@type": "dcat:Distribution",
+                    "description": "SOLVE I Science Overview",
+                    "downloadURL": "https://espo.nasa.gov/solve/content/SOLVE_Science_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cloud1.arc.nasa.gov/solveII/presentation_files/Newman_021218.pdf",
-                    "description": "SOLVE II Science Overview",
                     "@type": "dcat:Distribution",
+                    "description": "SOLVE II Science Overview",
+                    "downloadURL": "https://cloud1.arc.nasa.gov/solveII/presentation_files/Newman_021218.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cloud1.arc.nasa.gov/solveII/presentation_files/Margitan_021218.pdf",
-                    "description": "SOLVE II Balloon Campaign Overview",
                     "@type": "dcat:Distribution",
+                    "description": "SOLVE II Balloon Campaign Overview",
+                    "downloadURL": "https://cloud1.arc.nasa.gov/solveII/presentation_files/Margitan_021218.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2003JD004348",
-                    "description": "Measurements of ice water content in tropopause region Arctic cirrus during the SAGE III Ozone Loss and Validation Experiment (SOLVE)",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of ice water content in tropopause region Arctic cirrus during the SAGE III Ozone Loss and Validation Experiment (SOLVE)",
+                    "downloadURL": "https://doi.org/10.1029/2003JD004348",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2001JD002040",
-                    "description": "Chlorine budget and partitioning during the Stratospheric Aerosol and Gas Experiment (SAGE) III Ozone Loss and Validation Experiment (SOLVE)",
                     "@type": "dcat:Distribution",
+                    "description": "Chlorine budget and partitioning during the Stratospheric Aerosol and Gas Experiment (SAGE) III Ozone Loss and Validation Experiment (SOLVE)",
+                    "downloadURL": "https://doi.org/10.1029/2001JD002040",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/acp-5-1311-2005",
-                    "description": "Aerosol optical depth measurements by airborne sun photometer in SOLVE II: Comparisons to SAGE III, POAM III and airborne spectrometer measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Aerosol optical depth measurements by airborne sun photometer in SOLVE II: Comparisons to SAGE III, POAM III and airborne spectrometer measurements",
+                    "downloadURL": "https://doi.org/10.5194/acp-5-1311-2005",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Aerosol_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE2_Aerosol_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE2_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Aerosol_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836911-LARC_ASDC",
+            "issued": "2022-09-12",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Aerosol_AircraftInSitu_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-9.1 -180.0 -9.1 180.0 90.0 180.0 90.0 -180.0 -9.1 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2002-12-13T00:00:00Z/2003-02-06T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE II DC-8 Aircraft In-situ Aerosol Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V16.0",
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
+            "description": "This data set is intended to include all published groundbased asteroid radar detections. The file is based on the collection of asteroid radar detections established by Steven J. Ostro and currently maintained by Lance A.M. Benner. The file includes disc-integrated radar properties extracted from the published papers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v16.0_a72h-jtis",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V16.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v16.0_a72h-jtis",
-            "description": "This data set is intended to include all published groundbased asteroid radar detections. The file is based on the collection of asteroid radar detections established by Steven J. Ostro and currently maintained by Lance A.M. Benner. The file includes disc-integrated radar properties extracted from the published papers.",
-            "title": "ASTEROID RADAR V16.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID RADAR V16.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/468",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Christie, E.K. 2014. NPP Grassland: Charleville, Australia, 1973-1974, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/468",
-            "issued": "2013-11-12",
-            "temporal": "1942-01-01T00:00:00Z/1994-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
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
-            "identifier": "C2751944333-ORNL_CLOUD",
             "description": "This data set contains three ASCII files (.txt format). One file provides above- and below-ground biomass, productivity, litterfall, and bioelement data for a native C3 grassland near Charleville (-26.40 S, 146.27 E, Elevation 304 m) in southern Queensland, northeast Australia. The second file provides above- and below-ground biomass and productivity estimates for an introduced C4 grassland near Charleville. The third file contains climate data (precipitation and maximum/minimum temperature) recorded a weather station located at the Charleville Airport for the period 1942-1994. The NPP studies were carried out over a 12-month period from 1973 to 1974 using harvest techniques with a view to parameterizing a simulation model of primary production and livestock carrying capacity. Peak above-ground standing crop at the end of the summer season was 122 g/m2 and 154 g/m2 for the native and introduced grasslands, respectively. Maximum below-ground standing crop was markedly different, at 110 g/m2 and 400 g/m2, respectively, suggesting a significant difference in shoot/root allocation. Annual net primary production was estimated as the sum of above-ground peak standing crop (live + dead) and root increment. These values were 182 and 319 g/m2/yr for the native and introduced grasslands, respectively. Additional data on litter production and nutrient dynamics are available for the native grassland site. Data on soil moisture, determined gravimetrically with each biomass harvest, are available in the literature.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Charleville, Australia, 1973-1974, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F468",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F468",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_CHR/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_CHR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_CHR.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_CHR.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/468",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/468",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_CHR/comp/NPP_CHR.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_CHR/comp/NPP_CHR.pdf",
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
+            "identifier": "C2751944333-ORNL_CLOUD",
+            "issued": "2013-11-12",
+            "keyword": [
+                "biosphere",
+                "ecological dynamics",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/468",
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
             "spatial": "-26.4 146.27",
+            "temporal": "1942-01-01T00:00:00Z/1994-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Charleville, Australia, 1973-1974, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/318",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ryan, M.G., and M. Lavigne. 1999. BOREAS TE-02 Wood Respiration Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/318",
-            "issued": "2023-11-22",
-            "temporal": "1994-06-01T00:00:00Z/1994-09-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "ecosystems",
-                "vegetation",
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2808127572-ORNL_CLOUD",
             "description": "Contains wood respiration data collected by TE-02.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-02 Wood Respiration Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F318",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F318",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te2wdrsp/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/te2wdrsp/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE02_Wood_Resp.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE02_Wood_Resp.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/318",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/318",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2wdrsp/comp/TE02_Wood_Resp.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2wdrsp/comp/TE02_Wood_Resp.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2wdrsp/comp/TE02_Wood_Resp.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2wdrsp/comp/TE02_Wood_Resp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2wdrsp/comp/TE02_Wood_Resp.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2wdrsp/comp/TE02_Wood_Resp.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2wdrsp/comp/te2wdrsp.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/te2wdrsp/comp/te2wdrsp.def",
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
+            "identifier": "C2808127572-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "ecosystems",
+                "vegetation",
+                "earth science",
+                "biosphere",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/318",
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
             "spatial": "-98.67 55.88 -98.48 55.93",
+            "temporal": "1994-06-01T00:00:00Z/1994-09-25T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-02 Wood Respiration Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/TARA_OCEANS_EXPEDITION/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/TARA_OCEANS_EXPEDITION/DATA001.",
-            "issued": "2009-09-13",
-            "temporal": "2009-09-13T00:53:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
-                "ocean optics",
-                "ocean chemistry",
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
-            "identifier": "C1633360675-OB_DAAC",
             "description": "The Tara Oceans expedition, a 2.5-year long and 57,000 mile long trajectory, was conceived to provide a snapshot of the distribution of planktonic organisms in the world ocean, providing 'A global-scale study of morphological, genetic, and functional biodiversity of plankton organisms in relation to the changing physico-chemical parameters of the oceans' (Karsenti et al., 2011). The expedition took place from September 2009 to March 2012, spanned the majority of the world's oceans, and included, besides a large array of biological sampling, hydrographic measurements, optical measurements of surface hyper-spectral particulate absorption and attenuation, hyper-spectral reflectance and HPLC pigments.E. Karsenti, S.G. Acinas, P. Bork, C. Bowler, C. De Vargas, J. Raes, and 22 co-authors, A holistic approach to marine eco-systems biology, PLoS Biol. 9, e1001177, (2011), doi:10.1371/journal.pbio.1001177.",
-            "title": "Tara Oceans Expedition",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTARA_OCEANS_EXPEDITION%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FTARA_OCEANS_EXPEDITION%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Tara_Oceans_expedition/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Tara_Oceans_expedition/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360675-OB_DAAC",
+            "issued": "2009-09-13",
+            "keyword": [
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/TARA_OCEANS_EXPEDITION/DATA001",
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
+            "temporal": "2009-09-13T00:53:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tara Oceans Expedition"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD10A1F.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS/Aqua CGF Snow Cover Daily L3 Global 500m SIN Grid V061. Version 61. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD10A1F.061.",
-            "issued": "2002-07-04",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "snow/ice",
-                "ngda",
-                "national geospatial data asset",
-                "earth science",
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
-            "identifier": "C1646609745-NSIDC_ECS",
             "description": "This global Level-3 data set (MYD10A1F) provides daily cloud-free snow cover derived from the MODIS/Aqua Snow Cover Daily L3 Global 500m SIN Grid data set (MYD10A1). Grid cells\u00a0in MYD10A1 which are obscured by cloud cover are filled by retaining clear-sky views of the surface from previous days. A separate parameter is provided\u00a0which tracks\u00a0the number of days in each cell since the last clear-sky observation. Each data granule contains a 10\u00b0 x 10\u00b0 tile projected to the 500 m sinusoidal grid.\n\nThe terms \"Version 61\" and \"Collection 6.1\" are used interchangeably in reference to this release of MODIS data.",
-            "title": "MODIS/Aqua CGF Snow Cover Daily L3 Global 500m SIN Grid V061",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD10A1F.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD10A1F.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/daac/subscriptions.html",
-                    "description": "Subscribe to have new data automatically sent when the data become available.",
                     "@type": "dcat:Distribution",
+                    "description": "Subscribe to have new data automatically sent when the data become available.",
+                    "downloadURL": "http://nsidc.org/daac/subscriptions.html",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOSA/MYD10A1F.061/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOSA/MYD10A1F.061/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MYD10A1F+V061",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MYD10A1F+V061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/MYD10A1F/versions/61/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/MYD10A1F/versions/61/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10A1F.061",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10A1F.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10A1F.061",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10A1F.061",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1646609745-NSIDC_ECS",
+            "issued": "2002-07-04",
+            "keyword": [
+                "snow/ice",
+                "ngda",
+                "national geospatial data asset",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD10A1F.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua CGF Snow Cover Daily L3 Global 500m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-COSAC-2-PDCS-V1.0",
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
+            "description": "This archive contains edited data (CODMAC level 2) from the COSAC instrument onboard ROSETTA Lander, acquired during the PDCS (comet) phase. It also contains documentation which describes the COSAC experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-cosac-2-pdcs-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-COSAC-2-PDCS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-cosac-2-pdcs-v1.0",
-            "description": "This archive contains edited data (CODMAC level 2) from the COSAC instrument onboard ROSETTA Lander, acquired during the PDCS (comet) phase. It also contains documentation which describes the COSAC experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL COSAC 2 PDCS V1.0",
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
+            "title": "ROSETTA-LANDER CAL COSAC 2 PDCS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5880/GFZ.GRACE_06_GAC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GRACE. 2018-08-31. GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS GFZ (GAC). Version 6.0. GRACE_GAC_L2_GRAV_GFZ_RL06. JPL PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, GFZ. https://doi.org/10.5880/GFZ.GRACE_06_GAC. https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/. GRACE, GFZ, 2018-08-31, GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAC, https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/.",
-            "issued": "2018-08-06",
-            "temporal": "2002-04-05T00:00:00Z/2017-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-06",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "gravity/gravitational field"
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
-            "identifier": "C2491772121-POCLOUD",
-            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of geopotential field derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements and a non-tidal oceanic and atmospheric model produced by the German Research Centre for Geosciences (GFZ).  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
-            "release-place": "JPL PO.DAAC",
-            "series-name": "GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS GFZ (GAC)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GRACE",
-            "title": "GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAC",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAC_L2_GRAV_GFZ_RL06.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of geopotential field derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements and a non-tidal oceanic and atmospheric model produced by the German Research Centre for Geosciences (GFZ).  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5880%2FGFZ.GRACE_06_GAC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5880%2FGFZ.GRACE_06_GAC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ProdSpecDoc_v4.6.pdf",
-                    "description": "Product Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product Specification Document",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ProdSpecDoc_v4.6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/retired/docs/L2-GFZ_ProcStds_RL06_DRAFT.pdf",
-                    "description": "GFZ Level-2 Processing Standards Document For Level-2 Product RL06",
                     "@type": "dcat:Distribution",
+                    "description": "GFZ Level-2 Processing Standards Document For Level-2 Product RL06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/retired/docs/L2-GFZ_ProcStds_RL06_DRAFT.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAC_L2_GRAV_GFZ_RL06.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAC_L2_GRAV_GFZ_RL06.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
-                    "description": "GRACE Mission Page",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE Mission Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-UserHandbook_v4.0.pdf",
-                    "description": "Level-2 Gravity Field Product User Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Level-2 Gravity Field Product User Handbook",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/L2-UserHandbook_v4.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ReleaseNotes_gfz_RL06.pdf",
-                    "description": "Release Notes for GRACE L-2 products - version GFZ RL-06",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes for GRACE L-2 products - version GFZ RL-06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ReleaseNotes_gfz_RL06.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/L2/GFZ/RL06/README.txt",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/L2/GFZ/RL06/README.txt",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772121-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772121-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772121-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772121-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAC_L2_GRAV_GFZ_RL06.jpg",
+            "identifier": "C2491772121-POCLOUD",
+            "issued": "2018-08-06",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://doi.org/10.5880/GFZ.GRACE_06_GAC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL PO.DAAC",
+            "series-name": "GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS GFZ (GAC)",
             "spatial": "-180.0 -88.0 180.0 88.0",
+            "temporal": "2002-04-05T00:00:00Z/2017-07-01T00:00:00Z",
             "theme": [
                 "GRACE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRACE NON-TIDAL ATMOSPHERE AND OCEAN GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-12-21",
-            "temporal": "2021-12-21T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "trajectory",
-                "coordinates",
-                "coords",
-                "ephemeris",
-                "international",
-                "iss",
-                "location",
-                "space",
-                "station",
-                "topo"
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
-            "identifier": "nasa-iss-data_2021-12-21_a77a-ss64",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-12-21",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -458936,94 +458912,119 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-12-21_a77a-ss64",
+            "issued": "2021-12-21",
+            "keyword": [
+                "trajectory",
+                "coordinates",
+                "coords",
+                "ephemeris",
+                "international",
+                "iss",
+                "location",
+                "space",
+                "station",
+                "topo"
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
+            "temporal": "2021-12-21T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-12-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1043-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-19T10:19:40.000 to 2015-09-19T17:32:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1043-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1043-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1043-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-19T10:19:40.000 to 2015-09-19T17:32:59.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1043 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1043 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214336717-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
-            "issued": "2012-05-14",
-            "temporal": "2008-04-28T21:10:16Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "tectonics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@asf.alaska.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ASF"
-            },
-            "identifier": "C1214336717-ASF",
             "description": "UAVSAR Repeat Pass Interferometry Scene Metadata",
-            "title": "UAVSAR_INSAR_METADATA",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.asf.alaska.edu/",
-                    "description": "ASF data search and download interface",
                     "@type": "dcat:Distribution",
+                    "description": "ASF data search and download interface",
+                    "downloadURL": "https://search.asf.alaska.edu/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1214336717-ASF",
+            "issued": "2012-05-14",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "tectonics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214336717-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>64.623877 -9.140625 81.898451 -7.734375 83.84881 -34.453125 83.559717 -78.925781 77.915669 -124.804688 64.320872 -150.996094 55.776573 165.585938 45.58329 137.636719 36.456636 127.96875 29.840644 129.023438 18.646245 -159.433594 -47.989922 -76.640625 -47.989922 -64.6875 -37.160317 -52.382812 64.623877 -9.140625</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2008-04-28T21:10:16Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Aklavik Highway",
                 "Aleutians, AK",
@@ -459225,173 +459226,186 @@
                 "Yukon Flats West",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UAVSAR_INSAR_METADATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/913/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-07-02",
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
-            "identifier": "DASHLINK_913",
             "description": "Ballscrew jam fault datasets (diagnostic and prognostic)",
-            "title": "2010_09_09 Lab",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_09.zip",
-                    "description": "2010_09_09.zip",
                     "@type": "dcat:Distribution",
+                    "description": "2010_09_09.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_09.zip",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "2010_09_09.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_913",
+            "issued": "2014-07-02",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/913/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "2010_09_09 Lab"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/932",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Still, C.J., J.A. Berry, G.J. Collatz, R.S. Defries, F.G. Hall, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2009. ISLSCP II C4 Vegetation Percentage. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/932",
-            "issued": "2023-10-15",
-            "temporal": "1993-01-01T00:00:00Z/1998-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "atmospheric radiation",
-                "biosphere",
-                "earth science",
-                "land use/land cover",
-                "national geospatial data asset",
-                "ngda",
-                "surface radiative properties",
-                "land surface",
-                "vegetation",
-                "atmosphere"
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
-            "identifier": "C2784880272-ORNL_CLOUD",
             "description": "The photosynthetic composition (C3 or C4) of vegetation on the land surface is essential for accurate simulations of biosphere-atmosphere exchanges of carbon, water, and energy. C3 and C4 plants have different responses to light, temperature, CO2, and nitrogen; they also differ in physiological functions like stomatal conductance and isotope fractionation. A fine-scale distribution of these plant types is essential for earth science modeling.The C4 percentage is determined from data sets that describe the continuous distribution of plant growth forms (i.e., the percent of a grid cell covered by herbaceous or woody vegetation), climate classifications, the fraction of a grid cell covered in croplands, and national crop type harvest area statistics. The staff from the International Satellite Land Surface Climatology Project (ISLSCP) Initiative II have made the original data set consistent with the ISLSCP-2 land/water mask. This data set contains a single file in ArcInfo ASCIIGRID format.This data set is one of the products of the International Satellite Land-Surface Climatology Project, Initiative II (ISLSCP II) data collection which contains 50 global time series data sets for the ten-year period 1986 to 1995. Selected data sets span even longer periods. ISLSCP II is a consistent collection of data sets that were compiled from existing data sources and algorithms, and were designed to satisfy the needs of modelers and investigators of the global carbon, water and energy cycle. The data were acquired from a number of U.S. and international agencies, universities, and institutions. The global data sets were mapped at consistent spatial (1, 0.5 and 0.25 degrees) and temporal (monthly, with meteorological data at finer (e.g., 3-hour)) resolutions and reformatted into a common ASCII format. The data and documentation have undergone two peer reviews.ISLSCP is one of several projects of Global Energy and Water Cycle Experiment (GEWEX) [http://www.gewex.org/] and has the lead role in addressing land-atmosphere interactions -- process modeling, data retrieval algorithms, field experiment design and execution, and the development of global data sets.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II C4 Vegetation Percentage",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/932_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F932",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F932",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/vegetation/c4_percent_1deg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/vegetation/c4_percent_1deg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/c4_percent_1deg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/c4_percent_1deg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/932",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/932",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/c4_percent_1deg/comp/0_c4_percent_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/c4_percent_1deg/comp/0_c4_percent_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/c4_percent_1deg/comp/1_c4_percent_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/vegetation/c4_percent_1deg/comp/1_c4_percent_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/932_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/932_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=932",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=932",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/932/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/932/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/932_1_fit.png",
+            "identifier": "C2784880272-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "atmospheric radiation",
+                "biosphere",
+                "earth science",
+                "land use/land cover",
+                "national geospatial data asset",
+                "ngda",
+                "surface radiative properties",
+                "land surface",
+                "vegetation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/932",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1993-01-01T00:00:00Z/1998-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II C4 Vegetation Percentage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a7fg-4h9i",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Bacterial behavior has been observed to change during spaceflight. Higher final cell counts enhanced biofilm formation increased virulence and reduced susceptibility to antibiotics have been reported to occur for cells cultured in space . Most of these phenomena are theorized as being an indirect effect of an altered extracellular environment where the carbon source uptake is inhibited and excreted acidic byproducts buildup around the cell due to the lack of gravity-driven transport forces. However to date neither spaceflight results ground-based studies physical measurement techniques nor computational approaches have provided sufficient evidence needed to confirm this model. Gene expression data from the Antibiotic Effectiveness in Space (AES-1) experiment however have now allowed us to look into the biomolecular processes behind these observations and showed a systematic activation of glucose starvation and acid resistance genes. These results corroborate the reduced mass transport model proposed to govern bacterial responses to spaceflight. Furthermore the gene expression data suggests that metabolism was stimulated in space which could play a role in causing the observed increase in bacterial cell concentrations in microgravity. Similarly the decrease in extracellular pH may also be involved with the reported increase in virulence in space.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-95",
+                    "mediaType": "text/html",
+                    "title": "A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-95_a7fg-4h9i",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid extraction",
                 "treatment protocol",
@@ -459402,157 +459416,145 @@
                 "sequence analysis data transformation",
                 "nucleic acid sequencing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a7fg-4h9i",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-95_a7fg-4h9i",
-            "description": "Bacterial behavior has been observed to change during spaceflight. Higher final cell counts enhanced biofilm formation increased virulence and reduced susceptibility to antibiotics have been reported to occur for cells cultured in space . Most of these phenomena are theorized as being an indirect effect of an altered extracellular environment where the carbon source uptake is inhibited and excreted acidic byproducts buildup around the cell due to the lack of gravity-driven transport forces. However to date neither spaceflight results ground-based studies physical measurement techniques nor computational approaches have provided sufficient evidence needed to confirm this model. Gene expression data from the Antibiotic Effectiveness in Space (AES-1) experiment however have now allowed us to look into the biomolecular processes behind these observations and showed a systematic activation of glucose starvation and acid resistance genes. These results corroborate the reduced mass transport model proposed to govern bacterial responses to spaceflight. Furthermore the gene expression data suggests that metabolism was stimulated in space which could play a role in causing the observed increase in bacterial cell concentrations in microgravity. Similarly the decrease in extracellular pH may also be involved with the reported increase in virulence in space.",
-            "title": "A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-95",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "A Molecular Genetic Basis Explaining Altered Bacterial Behavior in Space"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1163",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "French, N.H.F., D. McKenzie, N. Hamermesh, and J.L. Mccarty. 2013. NACP Integrated Wildland and Cropland 30-m Fuel Characteristics Map, U.S.A., 2010. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1163",
-            "issued": "2022-11-21",
-            "temporal": "2010-01-01T00:00:00Z/2010-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "earth science",
-                "ecological dynamics",
-                "land surface",
-                "land use/land cover"
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
-            "identifier": "C2552181939-ORNL_CLOUD",
             "description": "The data set provides a 30-m comprehensive fuelbed characteristics map for both the wildland and cropland areas of the conterminous United States (CONUS) for 2010. This integrated product is the result of combining the spatially discrete Fuel Characteristic Classification System (FCCS) data of the US Forest Service (USFS) with the crop-and grassland-specific information of the US Department of Agricultures (USDA's) Cropland Data Layer (CDL).  By combining the spatially discrete details of the FCCS data set with the crop-and grassland-specific information of the CDL, a more robust map of fuelbed characteristics is available. The merged product has an advantage over the original FCCS map for estimating emissions from burned areas due to the integration of the fuelbed characteristics for agricultural areas from the CDL.There are three GeoTIFF format files and three comma-separated companion files distributed with this data set. The three tif files provided are very large and exceed the size limits of a standard GeoTIFF file format (4 GB). File sizes range from 20 to 30 GB. Compressed file sizes range from 2 to 3 GB. They are in a format that is called a BigTIFF file. ArcGIS 10.0 and ERDAS Imagine are able to read these files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP Integrated Wildland and Cropland 30-m Fuel Characteristics Map, U.S.A., 2010",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1163",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1163",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_Wild_Cropland_Fuel_Map/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_Wild_Cropland_Fuel_Map/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_Wild_Cropland_Fuel_Map.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_Wild_Cropland_Fuel_Map.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1163",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1163",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Wild_Cropland_Fuel_Map/comp/CDL-FCCS_Crosswalk.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Wild_Cropland_Fuel_Map/comp/CDL-FCCS_Crosswalk.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Wild_Cropland_Fuel_Map/comp/Double_crop_codes.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Wild_Cropland_Fuel_Map/comp/Double_crop_codes.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Wild_Cropland_Fuel_Map/comp/FuelbedCodes.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Wild_Cropland_Fuel_Map/comp/FuelbedCodes.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Wild_Cropland_Fuel_Map/comp/NACP_Wild_Cropland_Fuel_Map.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_Wild_Cropland_Fuel_Map/comp/NACP_Wild_Cropland_Fuel_Map.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
+            "identifier": "C2552181939-ORNL_CLOUD",
+            "issued": "2022-11-21",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science",
+                "ecological dynamics",
+                "land surface",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1163",
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
             "spatial": "-126.46 26.52 -67.96 49.79",
+            "temporal": "2010-01-01T00:00:00Z/2010-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP Integrated Wildland and Cropland 30-m Fuel Characteristics Map, U.S.A., 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-EXT1-67PCHURYUMOV-M25-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-ext1-67pchuryumov-m25-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "dark",
@@ -459562,60 +459564,37 @@
                 "earth",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-EXT1-67PCHURYUMOV-M25-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-ext1-67pchuryumov-m25-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 2 EXT1-MTP025 EDR V3.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 2 EXT1-MTP025 EDR V3.0"
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
-                "spice",
-                "themis",
-                "grs",
-                "pds"
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
-            "identifier": "NASA-679",
             "description": "GRS, THEMIS, SPICE",
-            "title": "PDS Odyssey Data Release 20",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -459623,981 +459602,969 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-679",
+            "issued": "2018-06-25",
+            "keyword": [
+                "spice",
+                "themis",
+                "grs",
+                "pds"
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
+            "title": "PDS Odyssey Data Release 20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1161",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kellndorfer, J., W. Walker, K. Kirsch, G. Fiske, J. Bishop, L. Lapoint, M. Hoppus, and J. Westfall. 2013. NACP Aboveground Biomass and Carbon Baseline Data, V.2 (NBCD 2000), U.S.A., 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1161",
-            "issued": "2013-05-29",
-            "temporal": "1999-01-01T00:00:00Z/2002-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2539954386-ORNL_CLOUD",
             "description": "The NBCD 2000 (National Biomass and Carbon Dataset for the Year 2000) data set provides a high-resolution (30 m) map of year-2000 baseline estimates of basal area-weighted canopy height, aboveground live dry biomass, and standing carbon stock for the conterminous United States. This data set distributes, for each of 66 map zones, a set of six raster files in GeoTIFF format. There is a detailed README companion file for each map zone. There is also an ArcGIS shapefile (mapping_zone_shapefile.shp) with the boundaries of all the map zones. A mosaic image of biomass at 240 m resolution for the whole conterminous U.S. is also included.Please read this important note regarding the differences of Version 2 from Version 1 of the NBCD 2000 data. With Version 1, in some mapping zones, certain land cover types (in particular Shrubs, NLCD Type 52) were missing from and unaccounted for in modeled estimates because of a lack of reference data. In Version 1, when landcover types were missing in the models, the model for the deciduous tree cover type was applied. While more woody vegetation was mapped, the authors think this had little effect on model performance as in most cases NLCD version 1 cover type was not a strong predictor of modeled estimates (See companion Mapping Zone Readme files). In Version 2, after renewed modeling efforts and user feedback, these previously unaccounted for cover types are now included in modeled estimates.All 66 mapping zones were updated with the previously unmapped land cover types now mapped. The authors recommend use of the new version for all analyses and will only support the updated version.Development of the data set used an empirical modeling approach that combined USDA Forest Service Forest Inventory and Analysis (FIA) data with high-resolution InSAR data acquired from the 2000 Shuttle Radar Topography Mission (SRTM) and optical remote sensing data acquired from the Landsat ETM+ sensor. Three-season Landsat ETM+ data were systematically compiled by the Multi-Resolution Land Characteristics Consortium (MRLC) between 1999 and 2002 for the entire U.S. and were the foundation for development of both the USGS National Land Cover Dataset 2001 (NLCD 2001) and the Landscape Fire and Resource Management Planning Tools Project (LANDFIRE). Products from both the NLCD 2001 (landcover and canopy density) and LANDFIRE (existing vegetation type) projects as well as topographic information from the USGS National Elevation Dataset (NED) were used within the NBCD 2000 project as spatial predictor layers for canopy height and biomass estimation. Forest survey data provided by the USDA Forest Service FIA program were made available to the project under a national Memorandum of Understanding. The response variables (canopy height and biomass) used in model development and validation were derived from the FIA database (FIADB). Production of the NLCD 2001 and LANDFIRE projects was based on a mapping zone approach in which the conterminous U.S. was split into 66 ecoregionally distinct mapping zones. This mapping zone approach was also adopted by the NBCD 2000 project.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP Aboveground Biomass and Carbon Baseline Data, V.2 (NBCD 2000), U.S.A., 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1161_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1161",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1161",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/NBCD2000_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/NBCD2000_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NBCD_2000_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NBCD_2000_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1161",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1161",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_2000_V2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_2000_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ01_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ01_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ02_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ02_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ03_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ03_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ04_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ04_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ05_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ05_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ06_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ06_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ07_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ07_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ08_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ08_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ09_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ09_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ10_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ10_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ12_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ12_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ13_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ13_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ14_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ14_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ15_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ15_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ16_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ16_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ17_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ17_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ18_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ18_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ19_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ19_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ20_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ20_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ21_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ21_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ22_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ22_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ23_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ23_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ24_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ24_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ25_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ25_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ26_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ26_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ27_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ27_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ28_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ28_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ29_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ29_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ30_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ30_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ31_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ31_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ32_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ32_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ33_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ33_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ34_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ34_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ35_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ35_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ36_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ36_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ37a_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ37a_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ37b_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ37b_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ38_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ38_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ39_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ39_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ40_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ40_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ41_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ41_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ42_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ42_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ43_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ43_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ44_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ44_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ45_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ45_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ46_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ46_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ47_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ47_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ48_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ48_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ49_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ49_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ50_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ50_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ51_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ51_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ52_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ52_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ53_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ53_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ54_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ54_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ55_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ55_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ56_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ56_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ57_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ57_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ58_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ58_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ59_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ59_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ60_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ60_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ61_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ61_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ62_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ62_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ63_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ63_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ64_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ64_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ65_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ65_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ66_README_v2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NBCD2000_V2/comp/NBCD_MZ66_README_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1161_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1161_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1161",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1161",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1161_1_fit.png",
+            "identifier": "C2539954386-ORNL_CLOUD",
+            "issued": "2013-05-29",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1161",
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
             "spatial": "-126.46 26.52 -67.96 49.79",
+            "temporal": "1999-01-01T00:00:00Z/2002-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP Aboveground Biomass and Carbon Baseline Data, V.2 (NBCD 2000), U.S.A., 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TCSP/AMPR/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A and Daniel J Cecil.2006. TCSP AMPR BRIGHTNESS TEMPERATURE (TB) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/TCSP/AMPR/DATA101",
-            "issued": "2006-03-22",
-            "temporal": "2005-07-05T18:18:36Z/2005-07-27T11:08:28Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "microwave",
-                "earth science",
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
-            "identifier": "C1979948426-GHRC_DAAC",
             "description": "The TCSP AMPR Brightness Temperature (TB) dataset consists of brightness temperature measurements from July 5, 2005 to July 27, 2005. The Advanced Microwave Precipitation Radiometer (AMPR) remotely senses passive microwave signatures of geophysical parameters from an airborne platform. The instrument is a low noise system which can provide multi-frequency microwave imagery with high spatial and temporal resolution. AMPR data are collected at a combination of frequencies (10.7, 19.35, 37.1, and 85.5 GHz) unique to current NASA aircraft instrumentation. These frequencies are well suited to the study of rain cloud systems, but are also useful to studies of various ocean and land surface processes. AMPR data were collected at four microwave frequencies (10.7, 19.35, 37.1 and 85.5 GHz).",
-            "graphic-preview-description": "N/A",
-            "title": "TCSP AMPR BRIGHTNESS TEMPERATURE (TB) V2",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/tcsp/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FAMPR%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FAMPR%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspampr",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspampr",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/tcsp/browse/tcsp_ampr_20050706_222309-224103.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/tcsp/browse/tcsp_ampr_20050706_222309-224103.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/ampr/ampr_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/ampr/ampr_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/ampr.pdf",
-                    "description": "Brief Instrument Description of the Advanced Microwave Precipitation Radiometer (AMPR)",
                     "@type": "dcat:Distribution",
+                    "description": "Brief Instrument Description of the Advanced Microwave Precipitation Radiometer (AMPR)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/ampr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/example_ampr_read_program.f",
-                    "description": "Example program to read AMPR data from a text file into arrays",
                     "@type": "dcat:Distribution",
+                    "description": "Example program to read AMPR data from a text file into arrays",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/example_ampr_read_program.f",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/TCSP",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/TCSP",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/tcsp/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/tcsp/browse/",
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
+            "graphic-preview-description": "N/A",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/tcsp/browse/",
+            "identifier": "C1979948426-GHRC_DAAC",
+            "issued": "2006-03-22",
+            "keyword": [
+                "microwave",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/TCSP/AMPR/DATA101",
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
             "spatial": "-100.187 4.52679 -49.7154 25.2555",
+            "temporal": "2005-07-05T18:18:36Z/2005-07-27T11:08:28Z",
             "theme": [
                 "TCSP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TCSP AMPR BRIGHTNESS TEMPERATURE (TB) V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0371-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-19T15:15:40.000 to 2014-10-19T22:01:23.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0371-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0371-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0371-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-19T15:15:40.000 to 2014-10-19T22:01:23.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0371 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0371 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS DAILY FROM DMSP F14 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA301",
-            "issued": "2012-08-08",
-            "temporal": "1997-05-08T00:00:00Z/2008-08-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "ocean winds",
-                "atmospheric water vapor",
-                "atmosphere",
-                "atmospheric winds",
-                "clouds",
-                "earth science",
-                "oceans",
-                "precipitation"
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
-            "identifier": "C1979923944-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids Daily from DMSP F14 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F14 daily.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS DAILY FROM DMSP F14 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F14%2FSSMI%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F14%2FSSMI%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif14d",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif14d",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/2000/f14_ssmi_20000512v7_A_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/2000/f14_ssmi_20000512v7_A_WS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/2000/f14_ssmi_20000512v7_A_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/2000/f14_ssmi_20000512v7_A_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/2000/f14_ssmi_20000512v7_A_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/2000/f14_ssmi_20000512v7_A_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/2000/f14_ssmi_20000512v7_A_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/2000/f14_ssmi_20000512v7_A_CW.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/SSMI_Data_in_NetCDF.docx",
-                    "description": "GHRC at UAH - SSM/I and SSMIS Data in NetCDF User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GHRC at UAH - SSM/I and SSMIS Data in NetCDF User's Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/SSMI_Data_in_NetCDF.docx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/MEASURES/SSMI-SSMIS/DATA301",
-                    "description": "Digital Object Identifier for a collection of related datasets",
                     "@type": "dcat:Distribution",
+                    "description": "Digital Object Identifier for a collection of related datasets",
+                    "downloadURL": "http://dx.doi.org/10.5067/MEASURES/SSMI-SSMIS/DATA301",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/ssmi_netcdf/ssmi_ssmis_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/ssmi_netcdf/ssmi_ssmis_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/rain.pdf",
-                    "description": "SSM/I Rain Retrievals Within an Unified All-Weather Ocean Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "SSM/I Rain Retrievals Within an Unified All-Weather Ocean Algorithm",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/rain.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ssmi.pdf",
-                    "description": "A Well Calibrated Ocean Algorithm for SSM/I",
                     "@type": "dcat:Distribution",
+                    "description": "A Well Calibrated Ocean Algorithm for SSM/I",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ssmi.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/Hilburn_V7_Poster_AMS_SatMet_2010_Annapolis.pdf",
-                    "description": "Description of Remote Sensing Systems Version-7 Geophysical Retrievals",
                     "@type": "dcat:Distribution",
+                    "description": "Description of Remote Sensing Systems Version-7 Geophysical Retrievals",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/Hilburn_V7_Poster_AMS_SatMet_2010_Annapolis.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f14/daily/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f14/daily/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/AMSR_Ocean_Algorithm_Version_2_Supplement_1.pdf",
-                    "description": "AMSR Ocean Algorithm documentation supplement",
                     "@type": "dcat:Distribution",
+                    "description": "AMSR Ocean Algorithm documentation supplement",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/AMSR_Ocean_Algorithm_Version_2_Supplement_1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/AMSR_Ocean_Algorithm_Version_2.pdf",
-                    "description": "AMSR Ocean Algorithm documentation",
                     "@type": "dcat:Distribution",
+                    "description": "AMSR Ocean Algorithm documentation",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/AMSR_Ocean_Algorithm_Version_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/2012_Wentz_011012_Version-7_SSMI_Calibration.pdf",
-                    "description": "SSM/I Version-7 Calibration Report",
                     "@type": "dcat:Distribution",
+                    "description": "SSM/I Version-7 Calibration Report",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/2012_Wentz_011012_Version-7_SSMI_Calibration.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ReadNetCDF.c",
-                    "description": "netCDF read software",
                     "@type": "dcat:Distribution",
+                    "description": "netCDF read software",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/ReadNetCDF.c",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/",
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
+            "graphic-preview-description": "N/A",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f14/daily/browse/",
+            "identifier": "C1979923944-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "ocean winds",
+                "atmospheric water vapor",
+                "atmosphere",
+                "atmospheric winds",
+                "clouds",
+                "earth science",
+                "oceans",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F14/SSMI/DATA301",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1997-05-08T00:00:00Z/2008-08-08T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS DAILY FROM DMSP F14 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0954-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-10T10:11:40.000 to 2015-08-10T17:26:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0954-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0954-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0954-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-10T10:11:40.000 to 2015-08-10T17:26:09.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0954 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0954 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/SITUTTDUKYZE",
             "citation": "Vrije Universiteit Amsterdam (Richard de Jeu) and NASA GSFC (Manfred Owe). Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng). 2014-09-15. LPRM_AMSR2_DS_D_SOILM3. Version 001. AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 10 km x 10 km descending V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/SITUTTDUKYZE. https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSR2_DS_D_SOILM3_001.html.",
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
-                "soils",
-                "surface thermal properties",
-                "vegetation",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RICHARD DE JEU",
                 "hasEmail": "mailto:Richard.de.jeu@falw.vu.nl"
             },
-            "identifier": "C1235316199-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "description": "AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 10 km x 10 km descending V001 is a Level 3 (gridded) data set. Its land surface parameters, surface soil moisture, land surface (skin) temperature, and vegetation water content, are derived from passive microwave remote sensing data from the Advanced Microwave Scanning Radiometer 2 (AMSR2), using the Land Parameter Retrieval Model (LPRM). There are two files per day, one ascending (daytime) and one descending (nighttime), archived as two different products. This document is for the nighttime product. The data set covers the period from May 2012, when the Japan Aerospace Exploration Agency (JAXA) Global Change Observation Mission-1st Water GCOM-W1 satellite was launched, to the present.\n\nThe LPRM is based on a forward radiative transfer model to retrieve surface soil moisture and vegetation optical depth. The land surface temperature is derived separately from the AMSR2's Ka-band (36.5 GHz). A unique feature of this method is that it can be applied at any microwave frequency, making it very suitable to exploit all the available passive microwave data from various satellites.\n\nInput data are from the AMSR2 spatial-resolution-matched brightness temperatures (L1SGRTBR) product, nighttime passes, as processed using LPRM (i.e., LPRM/AMSR2/GCOM-W1 Downscaled Level 2 product, LPRM_AMSR2_DS_SOILM2_V001).",
-            "editor": "Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng)",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "LPRM_AMSR2_DS_D_SOILM3",
             "creator": "Vrije Universiteit Amsterdam (Richard de Jeu) and NASA GSFC (Manfred Owe)",
-            "title": "AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 10 km x 10 km descending V001 (LPRM_AMSR2_DS_D_SOILM3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LPRM_AMSR2_DS_D_SOILM3_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 10 km x 10 km descending V001 is a Level 3 (gridded) data set. Its land surface parameters, surface soil moisture, land surface (skin) temperature, and vegetation water content, are derived from passive microwave remote sensing data from the Advanced Microwave Scanning Radiometer 2 (AMSR2), using the Land Parameter Retrieval Model (LPRM). There are two files per day, one ascending (daytime) and one descending (nighttime), archived as two different products. This document is for the nighttime product. The data set covers the period from May 2012, when the Japan Aerospace Exploration Agency (JAXA) Global Change Observation Mission-1st Water GCOM-W1 satellite was launched, to the present.\n\nThe LPRM is based on a forward radiative transfer model to retrieve surface soil moisture and vegetation optical depth. The land surface temperature is derived separately from the AMSR2's Ka-band (36.5 GHz). A unique feature of this method is that it can be applied at any microwave frequency, making it very suitable to exploit all the available passive microwave data from various satellites.\n\nInput data are from the AMSR2 spatial-resolution-matched brightness temperatures (L1SGRTBR) product, nighttime passes, as processed using LPRM (i.e., LPRM/AMSR2/GCOM-W1 Downscaled Level 2 product, LPRM_AMSR2_DS_SOILM2_V001).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSITUTTDUKYZE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSITUTTDUKYZE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -460607,95 +460574,109 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSR2_DS_D_SOILM3_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSR2_DS_D_SOILM3_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSR2_DS_D_SOILM3.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSR2_DS_D_SOILM3.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LPRM_AMSR2_DS_D_SOILM3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LPRM_AMSR2_DS_D_SOILM3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/LPRM_AMSR2_DS_D_SOILM3.001/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/LPRM_AMSR2_DS_D_SOILM3.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSR2_DS_D_SOILM3.001/doc/README_LPRM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSR2_DS_D_SOILM3.001/doc/README_LPRM.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LPRM_AMSR2_DS_D_SOILM3_001.png",
+            "identifier": "C1235316199-GES_DISC",
+            "issued": "2014-09-17",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils",
+                "surface thermal properties",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SITUTTDUKYZE",
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
+            "series-name": "LPRM_AMSR2_DS_D_SOILM3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-07-03T00:57:31Z/2022-01-17T00:00:00Z",
             "theme": [
                 "GCOM-W",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 10 km x 10 km descending V001 (LPRM_AMSR2_DS_D_SOILM3) at GES DISC"
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
-                "rss",
-                "pds"
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
-            "identifier": "NASA-770",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (21)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -460703,157 +460684,157 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-770",
+            "issued": "2018-06-25",
+            "keyword": [
+                "rss",
+                "pds"
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
+            "title": "PDS Odyssey Radio Science Data (21)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Sondes_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-10-16. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Sondes_Data_1.",
-            "issued": "1995-12-05",
-            "temporal": "1995-12-03T00:00:00Z/1996-02-19T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-01-31",
-            "keyword": [
-                "earth science",
-                "atmospheric winds",
-                "altitude",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Henry Selkirk",
                 "hasEmail": "mailto:henry.selkirk@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2736723318-LARC_ASDC",
             "description": "TOTE-VOTE_Sondes_Data_1 is the radiosonde data collected during the Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) campaign. Data collection for this product is complete.\r\n\r\nThe Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) campaign was conducted by NASA from December 1995 to February 1996. TOTE-VOTE took place in the Pacific region with the goal of gaining a better understanding of background transport processes from tropical/polar regions to midlatitudes. Nineteen flights were conducted using the NASA DC-8 aircraft and balloon sondes with the purpose of measuring the transport of filaments of air moved in or out of the arctic polar vortex and the tropical stratospheric reservoir. TOTE-VOTE also utilized ground-based instruments along with aircrafts.\r\n\r\nVarious instrumentation was used during TOTE-VOTE in order to achieve the mission objectives. The DC-8 aircraft was equipped with the NCAR NOxyO3 instrument, the NASA Langley Airborne Differential Absorption Lidar (DIAL) system, the Forward Scattering Spectrometer Probe (FSSP), the Microwave Temperature Profiler (MTP), the Multiple-Angle Aerosol Spectrometer Probe (MASP), and the diode laser spectrometer system, historically known as the Differential Absorption Carbon monOxide Measurement (DACOM). The NCAR NOxyO3 is a type of 4-channel chemiluminescence instrument that was used to quantify NOx (NO and NO2), NOy (total reactive nitrogen), and ozone (O3) in the air. The DIAL system used four lasers to make DIAL O3 profiles, along with collecting data on aerosol backscattering, aerosol depolarization ratio, aerosol extinction, and aerosol optical depth. The FSSP is an optical particle counter that measured particle size distribution. The MTP is a passive microwave radiometer that measured natural thermal emissions and was used during TOTE-VOTE to record temperature. The MASP spectrometer collected in-situ measurements of particle concentration, particle size distribution, and particle extinction. Along with the MASP\u2019s in-situ measurements, the DACOM spectrometer utilized three diode lasers at different wavelengths to take in-situ measurements of N2O, CO, CH4, and CO2 for TOTE-VOTE. Ground-based instruments collected lidar data while balloon sondes gathered information on wind direction, wind speed, atmospheric pressure, and air temperature.",
-            "title": "Tropical Ozone Transport Experiment - Vortex Ozone Transport Experiment (TOTE-VOTE) Sonde Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTOTE-VOTE_Sondes_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTOTE-VOTE_Sondes_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to Cite ASDC Data",
                     "@type": "dcat:Distribution",
+                    "description": "How to Cite ASDC Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science-data.larc.nasa.gov/lidar/tvo/totevote.html",
-                    "description": "TOTE-VOTE DIAL Aerosol and Ozone Distribution Images",
                     "@type": "dcat:Distribution",
+                    "description": "TOTE-VOTE DIAL Aerosol and Ozone Distribution Images",
+                    "downloadURL": "https://science-data.larc.nasa.gov/lidar/tvo/totevote.html",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900648",
-                    "description": "Aircraft observations of thin cirrus clouds near the tropical tropopause",
                     "@type": "dcat:Distribution",
+                    "description": "Aircraft observations of thin cirrus clouds near the tropical tropopause",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2000JD900648",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/1998GL900066",
-                    "description": "The in-flight sensitivity of Gold-Tube NOy converters to HCN",
                     "@type": "dcat:Distribution",
+                    "description": "The in-flight sensitivity of Gold-Tube NOy converters to HCN",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/1998GL900066",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JD03129",
-                    "description": "Lidar temperature measurements during the Tropical Ozone Transport Experiment (TOTE)/Vortex Ozone Transport Experiment (VOTE) mission",
                     "@type": "dcat:Distribution",
+                    "description": "Lidar temperature measurements during the Tropical Ozone Transport Experiment (TOTE)/Vortex Ozone Transport Experiment (VOTE) mission",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/97JD03129",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98GL00231",
-                    "description": "Correlative stratospheric ozone measurements with the airborne UV DIAL system during TOTE/VOTE",
                     "@type": "dcat:Distribution",
+                    "description": "Correlative stratospheric ozone measurements with the airborne UV DIAL system during TOTE/VOTE",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/98GL00231",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOTE-VOTE/Sondes_Data_1/",
-                    "description": "ASDC Direct Data Download for TOTE-VOTE_Sondes_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TOTE-VOTE_Sondes_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOTE-VOTE/Sondes_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736723318-LARC_ASDC",
-                    "description": "Earthdata Search for TOTE-VOTE_Sondes_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TOTE-VOTE_Sondes_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736723318-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Sondes_Data_1",
-                    "description": "DOI for TOTE-VOTE_Sondes_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for TOTE-VOTE_Sondes_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Sondes_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2736723318-LARC_ASDC",
+            "issued": "1995-12-05",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "altitude",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Sondes_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-54.5 -180.0 -54.5 179.22 82.5 179.22 82.5 -180.0 -54.5 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-12-03T00:00:00Z/1996-02-19T00:00:00Z",
             "theme": [
                 "TOTE-VOTE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tropical Ozone Transport Experiment - Vortex Ozone Transport Experiment (TOTE-VOTE) Sonde Data"
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
-                "pds",
-                "rss"
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
-            "identifier": "NASA-728",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (75)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -460861,380 +460842,375 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-728",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "rss"
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
+            "title": "PDS Odyssey Radio Science Data (75)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-5-ESC2-V2.0",
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
+            "description": "This data set contains CODMAC level 5 science data acquired by the DFMS and RTOF ROSINA sensors between 2015-03-11 and 2015-06-30 during the Escort phase 2 of the Rosetta mission at the comet 67P/CG. V2.0: Some minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-5-esc2-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-5-ESC2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-5-esc2-v2.0",
-            "description": "This data set contains CODMAC level 5 science data acquired by the DFMS and RTOF ROSINA sensors between 2015-03-11 and 2015-06-30 during the Escort phase 2 of the Rosetta mission at the comet 67P/CG. V2.0: Some minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 5\n                                      ESC2 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 5\n                                      ESC2 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/MURI_HI/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/MURI_HI/DATA001.",
-            "issued": "2012-05-31",
-            "temporal": "2012-05-31T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "earth science",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C1633360508-OB_DAAC",
             "description": "Measurements taken by the RV Kilo Moana in 2012 near the Hawaiian Islands.",
-            "title": "A Multi University Research Initiative (MURI) near the Hawaiian Islands",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMURI_HI%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMURI_HI%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MURI_HI/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MURI_HI/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360508-OB_DAAC",
+            "issued": "2012-05-31",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/MURI_HI/DATA001",
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
+            "temporal": "2012-05-31T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "A Multi University Research Initiative (MURI) near the Hawaiian Islands"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CH4NS.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-08-22. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2CH4NS.008. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "atmospheric temperature",
-                "clouds",
-                "earth science"
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
-            "identifier": "C1619005680-LARC",
             "description": "TL2CH4NS_8 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Methane Nadir Special Observation Version 8 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these sets. Thus, each limb standard product consisted of three swath objects, one for each observation, Limb 1, Limb",
-            "title": "TES/Aura L2 Methane Nadir Special Observation V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CH4NS.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2CH4NS.008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CH4NS.008",
-                    "description": "DOI data set landing page for TL2CH4NS_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2CH4NS_8",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2CH4NS.008",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CH4NS.008/contents.html",
-                    "description": "OPeNDAP data access for TL2CH4NS_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2CH4NS_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2CH4NS.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1619005680-LARC",
-                    "description": "Earthdata Search for TL2CH4NS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2CH4NS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1619005680-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CH4NS.008/",
-                    "description": "ASDC Direct Data Download for TL2CH4NS_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2CH4NS_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2CH4NS.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2SpecObs.cgi",
-                    "description": "Report of TES Level 2 Special Observation Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Special Observation Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2SpecObs.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_Products_Data_Quality_V008.pdf",
-                    "description": "Aura-TES L2 Products: Version 8 Data Quality Description",
                     "@type": "dcat:Distribution",
+                    "description": "Aura-TES L2 Products: Version 8 Data Quality Description",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_Products_Data_Quality_V008.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/TES_Validation_Report_v8_Final.pdf",
-                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Data Validation Report (Version F08_12 data) - Version 8.0",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Data Validation Report (Version F08_12 data) - Version 8.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/TES_Validation_Report_v8_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
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
+            "identifier": "C1619005680-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "atmospheric temperature",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CH4NS.008",
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
+            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L2 Methane Nadir Special Observation V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0818-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-30T09:28:05.000 to 2015-05-30T11:35:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0818-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0818-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0818-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-30T09:28:05.000 to 2015-05-30T11:35:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0818 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0818 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI1B2_TERRAIN_NRT_L1.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Near Real Time Level 1B2 terrain-projected Radiance parameters;See ProductionDateTime for published date.",
-            "issued": "2015-04-01",
-            "temporal": "2021-10-11T03:27:20.409Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-21",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "User Representative",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "identifier": "C1000000140-LARC",
             "description": "This file contains Terrain-projected TOA Radiance,resampled at the surface and topographically corrected, as well as geometrically corrected by PGE22.  It is used for MISR Near Real Time processing, and is derived from session-based Level 0 input files.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Near Real Time (NRT) Level 1B2 Terrain Data V001",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI1B2_TERRAIN_NRT_L1.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI1B2_TERRAIN_NRT_L1.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C1000000140-LARC",
+            "issued": "2015-04-01",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI1B2_TERRAIN_NRT_L1.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-06-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-10-11T03:27:20.409Z/2022-01-17T00:00:00Z",
             "theme": [
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Near Real Time (NRT) Level 1B2 Terrain Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA332",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRH3QP5. Version 006. AIRS/Aqua L3 5-day Quantization in Physical Units (AIRS+AMSU+HSB) 5 degrees x 5 degrees V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA332. https://disc.gsfc.nasa.gov/datacollection/AIRH3QP5_006.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2003-02-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-02-06",
-            "keyword": [
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "clouds",
-                "earth science"
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
-            "identifier": "C1238517199-GES_DISC",
-            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The quantization products (QP) are distributional summaries derived from the Level-2 standard retrieval products (of swath type) to provide a more comprehensive set of statistical summaries than the traditional means and standard deviation. The QP products combine the Level 2 standard data parameters over grid cells of 5 x 5 deg spatial extent for temporal periods of five days. Pentads always start on the 1st, 6th, 11th, 16th, 21st, and 26th days of the month and may contain as few as 3 days of data or as much as 6 days. They preserve the multivariate distributional features of the original data and so provide a compressed data set that more accurately describes the disparate atmospheric states that is in the original Level-2 swath data set. The geophysical parameters are: Air Temperature and Water Vapor profiles (11 levels/layers), Cloud fraction (vertical distribution).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRH3QP5",
             "creator": "AIRS Science Team/Joao Teixeira",
-            "title": "AIRS/Aqua L3 5-day Quantization in Physical Units (AIRS+AMSU+HSB) 5 degrees x 5 degrees V006 (AIRH3QP5) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3QP5_006.gif",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The quantization products (QP) are distributional summaries derived from the Level-2 standard retrieval products (of swath type) to provide a more comprehensive set of statistical summaries than the traditional means and standard deviation. The QP products combine the Level 2 standard data parameters over grid cells of 5 x 5 deg spatial extent for temporal periods of five days. Pentads always start on the 1st, 6th, 11th, 16th, 21st, and 26th days of the month and may contain as few as 3 days of data or as much as 6 days. They preserve the multivariate distributional features of the original data and so provide a compressed data set that more accurately describes the disparate atmospheric states that is in the original Level-2 swath data set. The geophysical parameters are: Air Temperature and Water Vapor profiles (11 levels/layers), Cloud fraction (vertical distribution).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA332",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA332",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -461244,436 +461220,471 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRH3QP5_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRH3QP5_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRH3QP5.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRH3QP5.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRH3QP5.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRH3QP5.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRH3QP5+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRH3QP5+006",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRS_V6.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRS_V6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3QP5_006.gif",
+            "identifier": "C1238517199-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA332",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-02-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRH3QP5",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2003-02-06T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 5-day Quantization in Physical Units (AIRS+AMSU+HSB) 5 degrees x 5 degrees V006 (AIRH3QP5) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aladee_ldex&version=1.2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This archive bundle includes data taken  by the Lunar Dust Experiment (LDEX) instrument aboard the Lunar        Atmosphere and Dust Environment Explorer (LADEE) spacecraft.  These    data are generated by dust impacts on the LDEX detector.  Both reduced and calibrated data are included in this bundle.",
+            "identifier": "urn:nasa:pds:ladee_ldex_a88v-uu47",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "ladee",
                 "dust"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aladee_ldex&version=1.2",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ladee_ldex_a88v-uu47",
-            "description": "This archive bundle includes data taken  by the Lunar Dust Experiment (LDEX) instrument aboard the Lunar        Atmosphere and Dust Environment Explorer (LADEE) spacecraft.  These    data are generated by dust impacts on the LDEX detector.  Both reduced and calibrated data are included in this bundle.",
-            "title": "LADEE LUNAR DUST EXPERIMENT",
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
+            "title": "LADEE LUNAR DUST EXPERIMENT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-5-IRGEO-V1.0",
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
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-5-irgeo-v1.0_a8ba-qura",
+            "issued": "2018-06-26",
+            "keyword": [
+                "2001 mars odyssey",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-5-IRGEO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-5-irgeo-v1.0_a8ba-qura",
-            "description": "TBD",
-            "title": "ODYSSEY THEMIS IR RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ODYSSEY THEMIS IR RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/b6b1-2b69",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Silalirijiit Project: Community created weather station network, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/b6b1-2b69.",
-            "issued": "2009-01-01",
-            "temporal": "2009-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "community-based monitoring",
-                "weather forecast",
-                "atmosphere"
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
-            "identifier": "C1728290548-NSIDCV0",
             "description": "Clyde River (Kangiqtugaapik), Nunavut, is located on the east coast of Baffin Island. Starting in 2009, local hunters and Elders partnered with researchers from the University of Colorado Boulder and Colorado State University to initiate the Silalirijiit Project.\n\nAn Inuktitut word, Silalirijiit (pronounced see-lah-LEE-ree-yeet) means \"those who work with or think about weather.\" This project links Inuit knowledge with climate science and environmental modeling to understand weather patterns and their changes in the Clyde River area.",
-            "title": "Silalirijiit Project: Community created weather station network, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fb6b1-2b69",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fb6b1-2b69",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eloka-arctic.org/communities/clyderiver.html",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://eloka-arctic.org/communities/clyderiver.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/b6b1-2b69",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/b6b1-2b69",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/b6b1-2b69",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/b6b1-2b69",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C1728290548-NSIDCV0",
+            "issued": "2009-01-01",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "community-based monitoring",
+                "weather forecast",
+                "atmosphere"
             ],
+            "landingPage": "https://doi.org/10.7265/b6b1-2b69",
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
+            "temporal": "2009-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Silalirijiit Project: Community created weather station network, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_Cloud_AircraftInSitu_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-03-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/ORACLES_Cloud_AircraftInSitu_Data_1.",
-            "issued": "2019-11-06",
-            "temporal": "2016-08-24T00:00:00Z/2018-10-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-19",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paquita Zuidema",
                 "hasEmail": "mailto:pzuidema@miami.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1703976416-LARC_ASDC",
             "description": "ORACLES_Cloud_AircraftInSitu_Data are in situ cloud measurements collected onboard the P-3 Orion or ER-2 aircraft during the ObseRvations of Aerosols above CLouds and their intEractionS (ORACLES) campaign. These measurements were collected from August 19, 2016 \u2013 October 27, 2016, August 1, 2017 \u2013 September 4, 2017 and September 21, 2018 \u2013 October 27, 2018. ORACLES provides multi-year airborne observations over the complete vertical column of key parameters that drive aerosol-cloud interactions in the southeast Atlantic, an area with some of the largest inter-model differences in aerosol forcing assessments on the planet. The P-3 Orion aircraft was utilized as a low-flying platform for simultaneous in situ and remote sensing measurements of aerosols and clouds and was supplemented by ER-2 remote sensing during the 2016 campaign. Data collection for this product is complete.\r\n\r\nSouthern Africa produces almost one-third of the Earth\u2019s biomass burning aerosol particles. The ORACLES (ObseRvations of Aerosols above CLouds and their intEractionS) experiment was a five year investigation with three intensive observation periods (August 19, 2016 \u2013 October 27, 2016; August 1, 2017 \u2013 September 4, 2017; September 21, 2018 \u2013 October 27, 2018) and was designed to study key processes that determine the climate impacts of African biomass burning aerosols. ORACLES provided multi-year airborne observations over the complete vertical column of the key parameters that drive aerosol-cloud interactions in the southeast Atlantic, an area with some of the largest inter-model differences in aerosol forcing assessments. These inter-model differences in aerosol and cloud distributions, as well as their combined climatic effects in the SE Atlantic are partly due to the persistence of aerosols above clouds. The varying separation of cloud and aerosol layers sampled during ORACLES allow for a process-oriented understanding of how variations in radiative heating profiles impact cloud properties, which is expected to improve model simulations for other remote regions experience long-range aerosol transport above clouds. ORACLES utilized two NASA aircraft, the P-3 and ER-2. The P-3 was used as a low-flying platform for simultaneous in situ and remote sensing measurements of aerosols and clouds in all three campaigns, supplemented by ER-2 remote sensing in 2016. ER-2 observations will be used to enhance satellite-based remote sensing by resolving variability within a particular scene, and by guiding the development of new and improved remote sensing techniques.",
-            "title": "ORACLES Cloud Aircraft InSitu Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FORACLES_Cloud_AircraftInSitu_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FORACLES_Cloud_AircraftInSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/oracles",
-                    "description": "ESPO home page for ORACLES",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO home page for ORACLES",
+                    "downloadURL": "https://espo.nasa.gov/oracles",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_Cloud_AircraftInSitu_Data_1",
-                    "description": "DOI data set landing page for ORACLES_Cloud_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ORACLES_Cloud_AircraftInSitu_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_Cloud_AircraftInSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703976416-LARC_ASDC",
-                    "description": "Earthdata Search for ORACLES_Cloud_AircraftInSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ORACLES_Cloud_AircraftInSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703976416-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/oracles_home.html",
-                    "description": "ORACLES Enhanced Modis Airborne Simulator (eMAS) Data",
                     "@type": "dcat:Distribution",
+                    "description": "ORACLES Enhanced Modis Airborne Simulator (eMAS) Data",
+                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/oracles_home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.nasa.gov/content/An_overview_of_the_ORACLES_ObseRvations_of_Aerosols_above_CLouds_and_their_intEractionS_0",
-                    "description": "ORACLES Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "ORACLES Mission Overview",
+                    "downloadURL": "https://airbornescience.nasa.gov/content/An_overview_of_the_ORACLES_ObseRvations_of_Aerosols_above_CLouds_and_their_intEractionS_0",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.nasa.gov/category/Mission/ORACLES",
-                    "description": "NASA Airborne Science ORACLES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Airborne Science ORACLES Posts",
+                    "downloadURL": "https://airbornescience.nasa.gov/category/Mission/ORACLES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/ames/earthscience/news/Making-It-Work-In-The-Field-With-Oracles",
-                    "description": "NASA.gov Article \u201cMaking It Work in the Field with ORACLES\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cMaking It Work in the Field with ORACLES\u201d",
+                    "downloadURL": "https://www.nasa.gov/centers/ames/earthscience/news/Making-It-Work-In-The-Field-With-Oracles",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/oracles/",
-                    "description": "NASA Earth Expeditions ORACLES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions ORACLES Posts",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/oracles/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/image-feature/looking-back-at-the-science-and-lessons-learned-from-oracles",
-                    "description": "NASA.gov Article \u201cLooking back at the science and lessons learned from ORACLES\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cLooking back at the science and lessons learned from ORACLES\u201d",
+                    "downloadURL": "https://www.nasa.gov/image-feature/looking-back-at-the-science-and-lessons-learned-from-oracles",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ORACLES/2016",
-                    "description": "ORACLES Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "ORACLES Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ORACLES/2016",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ORACLES/Cloud_AircraftInSitu_Data_1/",
-                    "description": "ASDC Direct Data Download for ORACLES_Cloud_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ORACLES_Cloud_AircraftInSitu_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ORACLES/Cloud_AircraftInSitu_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ORACLES/Cloud_AircraftInSitu_Data_1/contents.html",
-                    "description": "OPeNDAP data access for ORACLES_Cloud_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for ORACLES_Cloud_AircraftInSitu_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/ORACLES/Cloud_AircraftInSitu_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1703976416-LARC_ASDC",
+            "issued": "2019-11-06",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_Cloud_AircraftInSitu_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-78.0 -78.0 -78.0 119.5 40.0 119.5 40.0 -78.0 -78.0 -78.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2016-08-24T00:00:00Z/2018-10-27T23:59:59.999Z",
             "theme": [
                 "ORACLES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ORACLES Cloud Aircraft InSitu Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945527-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ocean temperature",
-                "ngda",
-                "national geospatial data asset",
-                "oceans",
-                "earth science"
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
-            "identifier": "C1641945527-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Regional 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version R2019.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L2/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MODIS-Aqua/L2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L2/SST/R2019.0",
-                    "description": "MODIS-Aqua L2 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L2 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L2/SST/R2019.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1641945527-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ocean temperature",
+                "ngda",
+                "national geospatial data asset",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1641945527-OB_DAAC.html",
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
+            "temporal": "2002-07-04T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua MODIS Regional 11\u00b5m Day/Night Sea Surface Temperature (SST) - Near Real Time (NRT) Data, version R2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a8dm-w4n2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John M. Kusterer",
+                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
+            },
+            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist of half orbit (Night and Day) emissivity and cloud particle data related to pixels that have been co-located to the Lidar track.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l2_swath-beta-v2-02_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000140",
             "issued": "2018-06-25",
-            "temporal": "2008-09-14/2011-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "cloud",
                 "satellite",
@@ -461683,356 +461694,359 @@
                 "atmospheric science",
                 "climate"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a8dm-w4n2",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000140",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist of half orbit (Night and Day) emissivity and cloud particle data related to pixels that have been co-located to the Lidar track.",
-            "title": "CALIPSO Imaging Infrared Radiometer L2 Data Swath V2-02",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_iir_l2_swath-beta-v2-02_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-09-14/2011-01-17",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Imaging Infrared Radiometer L2 Data Swath V2-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/PR2/DATA003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Im, Eastwood.2002. CAMEX-4 2ND GENERATION PRECIPITATION RADAR [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/PR2/DATA003",
-            "issued": "2002-06-19",
-            "temporal": "2001-08-18T18:39:23Z/2001-09-25T00:59:14Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
-            "keyword": [
-                "radar",
-                "spectral/engineering",
-                "earth science"
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
-            "identifier": "C1979097458-GHRC_DAAC",
             "description": "The CAMEX-4 2nd Generation Precipitation Radar dataset was collected by the Second Generation Precipitation Radar (PR-2), which is a dual-frequency, Doppler, dual-polarization radar system that includes digital, real-time pulse compression, extremely compact RF electronics, and a large deployable dual-frequency cylindrical parabolic antenna subsystem.  The PR-2 Doppler radar was used during the CAMEX-4 campaign to collect data for studying tropical storms and cyclones.",
-            "graphic-preview-description": "N/A",
-            "title": "CAMEX-4 2ND GENERATION PRECIPITATION RADAR V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/PR-2/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FPR2%2FDATA003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FPR2%2FDATA003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4dpr2",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4dpr2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/PR-2/browse/c4dpr2_2001.0909_010412_1849_KuLdr.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/PR-2/browse/c4dpr2_2001.0909_010412_1849_KuLdr.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4dpr2/c4dpr2_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4dpr2/c4dpr2_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4dpr2/CAM4_user.doc",
-                    "description": "User\u00bf\u00bf\u00bfs Guide to CAMEX-4 PR-2 Data",
                     "@type": "dcat:Distribution",
+                    "description": "User\u00bf\u00bf\u00bfs Guide to CAMEX-4 PR-2 Data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4dpr2/CAM4_user.doc",
+                    "mediaType": "application/msword",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4dpr2/read_pr-2_lev1b_hdf.pro",
-                    "description": "An IDL Procedure for reading a JPL PR-2 data file",
                     "@type": "dcat:Distribution",
+                    "description": "An IDL Procedure for reading a JPL PR-2 data file",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/camex4/c4dpr2/read_pr-2_lev1b_hdf.pro",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/camex4",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/camex4",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/PR-2/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/PR-2/browse/",
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
+            "graphic-preview-description": "N/A",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex4/PR-2/browse/",
+            "identifier": "C1979097458-GHRC_DAAC",
+            "issued": "2002-06-19",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/PR2/DATA003",
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
             "spatial": "-88.215 16.5617 -58.6883 39.2033",
+            "temporal": "2001-08-18T18:39:23Z/2001-09-25T00:59:14Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 2ND GENERATION PRECIPITATION RADAR V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1806",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Christensen, A.I., T.M. Pavelsky, D.J. Jensen, and K. Liu. 2020. Pre-Delta-X: River Discharge Channel Surveys across Atchafalaya Basin, LA, USA, 2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1806",
-            "issued": "2020-08-25",
-            "temporal": "2016-10-15T00:00:00Z/2016-10-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "geomorphic landforms/processes",
-                "ecosystems",
-                "terrestrial hydrosphere",
-                "biosphere",
-                "surface water"
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
-            "identifier": "C2025124066-ORNL_CLOUD",
             "description": "This dataset provides river discharge measurements collected at selected locations across the Atchafalaya River Basin, within the Mississippi River Delta (MRD) floodplain in coastal Louisiana, USA. The measurements were made during the Pre-Delta-X campaign on October 15 to 20, 2016. Seventy-five channel surveys were conducted with a SonTek RiverSurveyor M9 acoustic doppler current profiler (ADCP) on selected wide channels (~100 m) and a few selected (~10 m) narrow channels. ADCP data provide near-instantaneous estimates of river discharge across the sampled channels. Sites coincided with AirSWOT swaths in the Atchafalaya River Basin and water level measurement locations. This in situ dataset was used to calibrate and validate Delta-X hydrodynamic models.",
-            "graphic-preview-description": "Measurement of river discharge across channels. The acoustic doppler current profiler (ADCP) was mounted on a hydro board, which was allowed to drift alongside the boat while maintaining a transect perpendicular to flow. The impact from the boat was limited by slowly crabbing across each channel, allowing the ADCP to remain on the upstream side of the boat.",
-            "title": "Pre-Delta-X: River Discharge Channel Surveys across Atchafalaya Basin, LA, USA, 2016",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_ADCP_Measurements_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1806",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1806",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/deltax/PreDeltaX_ADCP_Measurements/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/deltax/PreDeltaX_ADCP_Measurements/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_ADCP_Measurements.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_ADCP_Measurements.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1806",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1806",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/PreDeltaX_ADCP_Measurements/comp/PreDeltaX_ADCP_Measurements.pdf",
-                    "description": "Pre-Delta-X: River Discharge Channel Surveys across Atchafalaya Basin, LA, USA, 2016: PreDeltaX_ADCP_Measurements.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Pre-Delta-X: River Discharge Channel Surveys across Atchafalaya Basin, LA, USA, 2016: PreDeltaX_ADCP_Measurements.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/PreDeltaX_ADCP_Measurements/comp/PreDeltaX_ADCP_Measurements.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_ADCP_Measurements_Fig1.png",
-                    "description": "Measurement of river discharge across channels. The acoustic doppler current profiler (ADCP) was mounted on a hydro board, which was allowed to drift alongside the boat while maintaining a transect perpendicular to flow. The impact from the boat was limited by slowly crabbing across each channel, allowing the ADCP to remain on the upstream side of the boat.",
                     "@type": "dcat:Distribution",
+                    "description": "Measurement of river discharge across channels. The acoustic doppler current profiler (ADCP) was mounted on a hydro board, which was allowed to drift alongside the boat while maintaining a transect perpendicular to flow. The impact from the boat was limited by slowly crabbing across each channel, allowing the ADCP to remain on the upstream side of the boat.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_ADCP_Measurements_Fig1.png",
+                    "mediaType": "image/png",
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
+            "graphic-preview-description": "Measurement of river discharge across channels. The acoustic doppler current profiler (ADCP) was mounted on a hydro board, which was allowed to drift alongside the boat while maintaining a transect perpendicular to flow. The impact from the boat was limited by slowly crabbing across each channel, allowing the ADCP to remain on the upstream side of the boat.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_ADCP_Measurements_Fig1.png",
+            "identifier": "C2025124066-ORNL_CLOUD",
+            "issued": "2020-08-25",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "geomorphic landforms/processes",
+                "ecosystems",
+                "terrestrial hydrosphere",
+                "biosphere",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1806",
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
             "spatial": "-91.44 29.44 -91.21 29.74",
+            "temporal": "2016-10-15T00:00:00Z/2016-10-20T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-Delta-X: River Discharge Channel Surveys across Atchafalaya Basin, LA, USA, 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M07-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m07-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M07-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m07-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP007 RDR-REFLECT V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP007 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-2-LAUNCH-V1.1",
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
+            "description": "This data set contains Raw data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-2-launch-v1.1_a8g8-2vnw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-2-LAUNCH-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-2-launch-v1.1_a8g8-2vnw",
-            "description": "This data set contains Raw data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the post-launch checkout mission phase.",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-PFES-3-RDR-SPECTRUM-V1.0",
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
-                "geologic remote sensing field experiment",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Portable Field Emission Spectrometer (PFES) data were acquired on July 15 and 17, 1989. A total of 31 measurements were collected for GRSFE. Of these measurements, 13 were calibrations and 18 were of representative surfaces. The data were collected primarily to support the calibration of the TIMS data and to assist in interpreting spectral mixing in the mid-infrared. Sites were selected for calibration that covered a range of emissivities. On July 15, PFES data were collected at Kelso Dunes and the Cima Volcanic Field as part of the Calibration Team effort. Daedalus and SIRIS data were collected over the same sites. For the PFES data, the Kelso Dunes Bright Target site represented the silica-rich endmember and the Cima basalt tephra Dark Target site represented the more silica-poor endmember. On July 17, PFES data were collected at two of the modelling sites at Lunar Lake (the playa and the cobble sites). Several spectra were also collected at the playa surface next to the Lunar Lake thermistor site.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-pfes-3-rdr-spectrum-v1.0_a8hh-y5bv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "geologic remote sensing field experiment",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-PFES-3-RDR-SPECTRUM-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-pfes-3-rdr-spectrum-v1.0_a8hh-y5bv",
-            "description": "Portable Field Emission Spectrometer (PFES) data were acquired on July 15 and 17, 1989. A total of 31 measurements were collected for GRSFE. Of these measurements, 13 were calibrations and 18 were of representative surfaces. The data were collected primarily to support the calibration of the TIMS data and to assist in interpreting spectral mixing in the mid-infrared. Sites were selected for calibration that covered a range of emissivities. On July 15, PFES data were collected at Kelso Dunes and the Cima Volcanic Field as part of the Calibration Team effort. Daedalus and SIRIS data were collected over the same sites. For the PFES data, the Kelso Dunes Bright Target site represented the silica-rich endmember and the Cima basalt tephra Dark Target site represented the more silica-poor endmember. On July 17, PFES data were collected at two of the modelling sites at Lunar Lake (the playa and the cobble sites). Several spectra were also collected at the playa surface next to the Lunar Lake thermistor site.",
-            "title": "FIELD EXP EARTH PFES CALIBRATED RDR SPECTRUM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "FIELD EXP EARTH PFES CALIBRATED RDR SPECTRUM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a8iy-5k5y",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "NASA  s Rodent Research (RR) project is playing a critical role in advancing biomedical research on the physiological effects of space environments. Due to the limited resources for conducting biological experiments aboard the International Space Station (ISS) it is imperative to use crew time efficiently while maximizing high-quality science return. NASA  s GeneLab project has as its primary objectives to 1) further increase the value of these experiments using a multi-omics systems biology-based approach and 2) disseminate these data without restrictions to the scientific community. The current investigation assessed viability of RNA DNA and protein extracted from archived RR-1 tissue samples for epigenomic transcriptomic and proteomic assays. During the first RR spaceflight experiment a variety of tissue types were harvested from subjects snap-frozen or RNAlater-preserved and then stored at least a year at -80C after return to Earth. They were then prioritized for this investigation based on likelihood of significant scientific value for spaceflight research. All tissues were made available to GeneLab through the bio-specimen sharing program managed by the Ames Life Science Data Archive and included mouse adrenal glands quadriceps gastrocnemius tibialis anterior extensor digitorum longus soleus eye and kidney. We report here protocols for and results of these tissue extractions and thus the feasibility and value of these kinds of omics analyses. In addition to providing additional opportunities for investigation of spaceflight effects on the mouse transcriptome and proteome in new kinds of tissues our results may also be of value to program managers for the prioritization of ISS crew time for rodent research activities.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-105",
+                    "mediaType": "text/html",
+                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse tibialis anterior muscle transcriptomic proteomic and epigenomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-105_a8iy-5k5y",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "epitranscriptomics",
                 "mass spectrometry",
@@ -462049,437 +462063,437 @@
                 "5mc total rna methylation analysis",
                 "rna library construction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a8iy-5k5y",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-105_a8iy-5k5y",
-            "description": "NASA  s Rodent Research (RR) project is playing a critical role in advancing biomedical research on the physiological effects of space environments. Due to the limited resources for conducting biological experiments aboard the International Space Station (ISS) it is imperative to use crew time efficiently while maximizing high-quality science return. NASA  s GeneLab project has as its primary objectives to 1) further increase the value of these experiments using a multi-omics systems biology-based approach and 2) disseminate these data without restrictions to the scientific community. The current investigation assessed viability of RNA DNA and protein extracted from archived RR-1 tissue samples for epigenomic transcriptomic and proteomic assays. During the first RR spaceflight experiment a variety of tissue types were harvested from subjects snap-frozen or RNAlater-preserved and then stored at least a year at -80C after return to Earth. They were then prioritized for this investigation based on likelihood of significant scientific value for spaceflight research. All tissues were made available to GeneLab through the bio-specimen sharing program managed by the Ames Life Science Data Archive and included mouse adrenal glands quadriceps gastrocnemius tibialis anterior extensor digitorum longus soleus eye and kidney. We report here protocols for and results of these tissue extractions and thus the feasibility and value of these kinds of omics analyses. In addition to providing additional opportunities for investigation of spaceflight effects on the mouse transcriptome and proteome in new kinds of tissues our results may also be of value to program managers for the prioritization of ISS crew time for rodent research activities.",
-            "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse tibialis anterior muscle transcriptomic proteomic and epigenomic data",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-105",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse tibialis anterior muscle transcriptomic proteomic and epigenomic data"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse tibialis anterior muscle transcriptomic proteomic and epigenomic data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/LIS/LIS/DATA302",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Albrecht, Rachel I, Steve  Goodman, Dennis  Buechler, Richard J. Blakeslee and Hugh  Christian.2016. LIS 0.1 DEGREE VERY HIGH RESOLUTION GRIDDED LIGHTNING MONTHLY CLIMATOLOGY (VHRMC) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/LIS/LIS/DATA302",
-            "issued": "2016-03-02",
-            "temporal": "1998-01-01T00:00:00Z/2013-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmospheric electricity",
-                "weather events",
-                "atmosphere",
-                "earth science"
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
-            "identifier": "C1979883359-GHRC_DAAC",
             "description": "The LIS 0.1 Degree Very High Resolution Gridded Lightning Monthly Climatology (VHRMC) dataset consists of gridded monthly climatologies of total lightning flash rates seen by the Lightning Imaging Sensor (LIS) from January 1, 1998 through December 31, 2013. LIS is an instrument on the Tropical Rainfall Measurement Mission satellite (TRMM) used to detect the distribution and variability of total lightning occurring in the Earth's tropical and subtropical regions. This information can be used for severe storm detection and analysis, and also for lightning-atmosphere interaction studies. The gridded climatologies include annual mean flash rate, mean diurnal cycle of flash rate with 24 hour resolution, and mean annual cycle of flash rate with daily, monthly, or seasonal resolution. All datasets are in 0.1 degree spatial resolution. The mean annual cycle of flash rate datasets (i.e., daily, monthly or seasonal) have both 49-day and 1 degree boxcar moving averages to remove diurnal cycle and smooth regions with low flash rate, making the results more robust.",
-            "graphic-preview-description": "N/A",
-            "title": "LIS 0.1 DEGREE VERY HIGH RESOLUTION GRIDDED LIGHTNING MONTHLY CLIMATOLOGY (VHRMC) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRMC/animations/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLIS%2FDATA302",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLIS%2FDATA302",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=lisvhrmc",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=lisvhrmc",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/ghrc/lis/lisvhrc/VHRMC/lisvhrmc_monthly_july.JPG",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/ghrc/lis/lisvhrc/VHRMC/lisvhrmc_monthly_july.JPG",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/LIS/LIS/DATA306",
-                    "description": "Collection DOI for set of related datasets",
                     "@type": "dcat:Distribution",
+                    "description": "Collection DOI for set of related datasets",
+                    "downloadURL": "http://dx.doi.org/10.5067/LIS/LIS/DATA306",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/LIS_VHRES_Guide.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/LIS_VHRES_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/BAMS-D-14-00193.1",
-                    "description": "Where are the lightning hotspots on Earth?",
                     "@type": "dcat:Distribution",
+                    "description": "Where are the lightning hotspots on Earth?",
+                    "downloadURL": "http://dx.doi.org/10.1175/BAMS-D-14-00193.1",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/read_example-LIS_VHRC.R",
-                    "description": "LIS Very  High Resolution Climatology Data Reader Code",
                     "@type": "dcat:Distribution",
+                    "description": "LIS Very  High Resolution Climatology Data Reader Code",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/doc/read_example-LIS_VHRC.R",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/data/data_lis_vhr-climatology.html",
-                    "description": "Google Earth Tool",
                     "@type": "dcat:Distribution",
+                    "description": "Google Earth Tool",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/data/data_lis_vhr-climatology.html",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/highlights-albrecht-et-als-where-are-lightning-hotspots-earth%E2%80%99-publication",
-                    "description": "Highlights from Albrecht et. al's 'Where Are the Lightning Hotspots on Earth?' publication",
                     "@type": "dcat:Distribution",
+                    "description": "Highlights from Albrecht et. al's 'Where Are the Lightning Hotspots on Earth?' publication",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/highlights-albrecht-et-als-where-are-lightning-hotspots-earth%E2%80%99-publication",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRMC/animations/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRMC/animations/",
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
+            "graphic-preview-description": "N/A",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS/VHRMC/animations/",
+            "identifier": "C1979883359-GHRC_DAAC",
+            "issued": "2016-03-02",
+            "keyword": [
+                "atmospheric electricity",
+                "weather events",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/LIS/LIS/DATA302",
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
             "spatial": "-180.0 -38.0 180.0 38.0",
+            "temporal": "1998-01-01T00:00:00Z/2013-12-31T23:59:59Z",
             "theme": [
                 "LIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LIS 0.1 DEGREE VERY HIGH RESOLUTION GRIDDED LIGHTNING MONTHLY CLIMATOLOGY (VHRMC) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1649",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lin, B., J.F. Campbell, J. Dobler, E.V. Browell, S.A. Kooi, S. Pal, T. Fan, W. Erxleben, D. Mcgregor, M.D. Obland, and C. O'Dell. 2018. ACT-America: L2 Remotely Sensed Column-average CO2 by Airborne Lidar, Eastern USA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1649",
-            "issued": "2021-01-03",
-            "temporal": "2016-05-27T14:53:00Z/2018-05-20T21:13:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C2706335063-ORNL_CLOUD",
             "description": "This dataset provides Level 2 (L2) remotely sensed column-average carbon dioxide (CO2) concentrations measured during airborne campaigns in Summer 2016, Winter 2017, Fall 2017, and Spring 2018 conducted over central and eastern regions of the United States for the Atmospheric Carbon and Transport (ACT-America) project. Column-average CO2 concentrations were measured at 0.1 second frequency during flights of the C-130 Hercules aircraft at altitudes up to 8 km with a Multi-functional Fiber Laser Lidar (MFLL; Harris Corporation). The MFLL is a set of Continuous-Wave (CW) lidar instruments consisting of an intensity modulated multi-frequency single-beam synchronous-detection Laser Absorption Spectrometer (LAS) operating at 1571 nm for measuring the column amount of CO2 number density and range between the aircraft and the surface or to cloud tops, and surface reflectance and a Pseudo-random Noise (PN) altimeter at 1596 nm for measuring the path length from the aircraft to the scattering surface and/or cloud tops. The MFLL was onboard all ACT-America seasonal campaigns, except Summer 2019. Complete aircraft flight information, interpolated to the 0.1 second column CO2 reporting frequency, are included, but not limited to, latitude, longitude, altitude, and attitude. Processing for this Level 2 (L2) product included additional processing and calibration procedures described in this document as applied to retrieval of column CO2 from L1 MFLL data. Data users should use this L2 data unless different CO2 retrieval criteria are preferred.",
-            "graphic-preview-description": "Column-average CO2 measured during the first 20 minutes of flight off the coast of New Jersey on July 11 for the Summer 2016 campaign.",
-            "title": "ACT-America: L2 Remotely Sensed Column-average CO2 by Airborne Lidar, Eastern USA",
-            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_MFFLL_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1649",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1649",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/actamerica/ACTAMERICA_MFFLL/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/actamerica/ACTAMERICA_MFFLL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_MFFLL.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_MFFLL.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1649",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1649",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_MFFLL/comp/ACTAMERICA_MFFLL.pdf",
-                    "description": "ACT-America: L2 Remotely Sensed Column-average CO2 by Airborne Lidar, Eastern USA: ACTAMERICA_MFFLL.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L2 Remotely Sensed Column-average CO2 by Airborne Lidar, Eastern USA: ACTAMERICA_MFFLL.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA_MFFLL/comp/ACTAMERICA_MFFLL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_MFFLL_Fig1.png",
-                    "description": "Column-average CO2 measured during the first 20 minutes of flight off the coast of New Jersey on July 11 for the Summer 2016 campaign.",
                     "@type": "dcat:Distribution",
+                    "description": "Column-average CO2 measured during the first 20 minutes of flight off the coast of New Jersey on July 11 for the Summer 2016 campaign.",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_MFFLL_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://actamerica.ornl.gov",
-                    "description": "ACT-America Campaign Site",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America Campaign Site",
+                    "downloadURL": "https://actamerica.ornl.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1649/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1649/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Column-average CO2 measured during the first 20 minutes of flight off the coast of New Jersey on July 11 for the Summer 2016 campaign.",
+            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA_MFFLL_Fig1.png",
+            "identifier": "C2706335063-ORNL_CLOUD",
+            "issued": "2021-01-03",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1649",
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
             "spatial": "-106.05 27.23 -71.91 49.11",
+            "temporal": "2016-05-27T14:53:00Z/2018-05-20T21:13:00Z",
             "theme": [
                 "ACT-America",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACT-America: L2 Remotely Sensed Column-average CO2 by Airborne Lidar, Eastern USA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/H66DGC3ICJMQ",
             "citation": "Kevin W. Bowman. 2023-02-13. TRPSYL2ALLCRSMGLOS. Version 1. TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/H66DGC3ICJMQ. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGLOS_1.html. Digital Science Data.",
-            "issued": "2023-02-17",
-            "temporal": "2016-01-02T00:00:00Z/2023-03-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-17",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2569847612-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Summary Product contains the vertical distribution of six retrieved atmospheric gases (CH4, CO, HDO, NH3, O3 and PAN), along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream summary product is centered on a 3x3 degree region over Los Angeles for the time period from 2016-01-02 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2ALLCRSMGLOS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Summary Product V1 (TRPSYL2ALLCRSMGLOS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGLOS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FH66DGC3ICJMQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FH66DGC3ICJMQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGLOS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGLOS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGLOS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGLOS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLOS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLOS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2ALLCRSMGLOS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2ALLCRSMGLOS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLOS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLOS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLOS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGLOS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_H2O_L2_Product_User_Guide_v1_20210202.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_H2O_L2_Product_User_Guide_v1_20210202.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/TROPESS_ATBDv1.1.pdf",
-                    "description": "ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/TROPESS_ATBDv1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGLOS_Sample.png",
+            "identifier": "C2569847612-GES_DISC",
+            "issued": "2023-02-17",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/H66DGC3ICJMQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-17",
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
+            "series-name": "TRPSYL2ALLCRSMGLOS",
             "spatial": "-120.0 33.0 -117.0 36.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-03-06T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Los Angeles Megacity, Summary Product V1 (TRPSYL2ALLCRSMGLOS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-POS-6-SUMM-S3COORDS-V1.1",
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
-                "voyager",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pos-6-summ-s3coords-v1.1_a8nn-htm2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-POS-6-SUMM-S3COORDS-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pos-6-summ-s3coords-v1.1_a8nn-htm2",
-            "description": "not applicable",
-            "title": "VG1 JUP EPHEMERIS SYSTEM III (1965) COORDS BROWSE V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 JUP EPHEMERIS SYSTEM III (1965) COORDS BROWSE V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/a8nx-hpth",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Age plays a major role in tumor incidence and is an important consideration when modeling the carcinogenesis process or estimating cancer risks. Epidemiological data show that from adolescence through middle age cancer incidence increases with age. This effect is commonly attributed to a lifetime accumulation of cellular particularly DNA damage. However during middle-age the incidence begins to decelerate and for many tumor sites it actually decreases at sufficiently advanced ages. We investigated if the observed deceleration and potential decrease in incidence could be attributed to a decreased capacity of older hosts to support tumor progression and whether HZE (high atomic number (Z) high energy (E)) radiation differentially modulates tumor progression in young versus middle-age hosts issues relevant to estimating carcinogenesis risk for astronauts. Lewis lung carcinoma (LLC) cells were injected into syngeneic mice (143 and 551 days old) which were then subject to whole-body 56Fe irradiation (1GeV/amu). Three findings emerged: 1) among unirradiated animals substantial inhibition of tumor progression and significantly decreased tumor growth rates were seen for middle-aged mice compared to young mice; 2) whole-body 56Fe irradiation (1GeV/amu) inhibited tumor progression in both young and in middle-aged mice (with greater suppression seen in case of young animals) with little effect on tumor growth rates; and 3) 56Fe irradiation (1GeV/amu) suppressed tumor progression in young mice to a degree not significantly different than transiting from young to middle-aged. Thus 56Fe irradiation (1GeV/amu) acted similar to aging with respect to tumor progression. We further investigated the molecular underpinnings driving the radiation modulation of tumor dynamics in young and middle-aged mice. Through global gene expression analysis the key players FASN AKT1 and the CXCL12/CXCR4 complex were determined to be contributory. In sum these findings demonstrate a reduced capacity of middle-aged hosts to support the progression phase of carcinogenesis and identify molecular factors contributory to HZE radiation modulation of tumor progression as a function of age. For genome-wide expression profiling of tumor tissue Mouse WG-6 BeadArray chips (Illumina San Diego CA) were used. Total RNA was amplified with the Ambion Illumina TotalPrep Amplification Kit (Ambion Austin TX) and labeled from all replicate biological samples for each condition. The number of tumor sample replicates used from each condition is as follows: 10 samples from young unirradiated mice 8 samples from young irradiated mice 7 samples from middle-aged unirradiated mice 5 samples from middle-aged irradiated mice. Total RNA was isolated and purified using Trizol (Invitrogen) or RNeasy (Qiagen) quantified and qualified using Agilent Bioanalyzer (Agilent) and samples were deemed suitable for amplification and hybridization if they had O.D. 260/280 = 1.7 - 2.1 28s/18s = 2:1 RIN (RNA integrity number) >7. Total RNA of 500ng per sample was amplified using Ambion TotalPrep (Ambion) and 1.5ug of the product was loaded onto the chips. Following hybridization at 55C the chips were washed and then scanned using the Illumina iScan (Illumina) and the data were analyzed using GenomeStudio (Illumina). Data were first analyzed for gene expression and then culled for present genes (genes that meet the criteria of detection p-value < 0.05). Expression above background was included in an expressed genes working data set for further analyses. Rank variant normalization was applied to the data before extensive analysis. Differential gene expression analysis was used to compare to the reference group young unirradiated mice and genes were then evaluated and validated.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-88",
+                    "mediaType": "text/html",
+                    "title": "Age and Space Irradiation Modulate Tumor Progression: Implications for Carcinogenesis Risk"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-88_a8nx-hpth",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "rna extraction",
                 "normalization data transformation",
@@ -462496,504 +462510,499 @@
                 "sample collection",
                 "treatment protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/a8nx-hpth",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-88_a8nx-hpth",
-            "description": "Age plays a major role in tumor incidence and is an important consideration when modeling the carcinogenesis process or estimating cancer risks. Epidemiological data show that from adolescence through middle age cancer incidence increases with age. This effect is commonly attributed to a lifetime accumulation of cellular particularly DNA damage. However during middle-age the incidence begins to decelerate and for many tumor sites it actually decreases at sufficiently advanced ages. We investigated if the observed deceleration and potential decrease in incidence could be attributed to a decreased capacity of older hosts to support tumor progression and whether HZE (high atomic number (Z) high energy (E)) radiation differentially modulates tumor progression in young versus middle-age hosts issues relevant to estimating carcinogenesis risk for astronauts. Lewis lung carcinoma (LLC) cells were injected into syngeneic mice (143 and 551 days old) which were then subject to whole-body 56Fe irradiation (1GeV/amu). Three findings emerged: 1) among unirradiated animals substantial inhibition of tumor progression and significantly decreased tumor growth rates were seen for middle-aged mice compared to young mice; 2) whole-body 56Fe irradiation (1GeV/amu) inhibited tumor progression in both young and in middle-aged mice (with greater suppression seen in case of young animals) with little effect on tumor growth rates; and 3) 56Fe irradiation (1GeV/amu) suppressed tumor progression in young mice to a degree not significantly different than transiting from young to middle-aged. Thus 56Fe irradiation (1GeV/amu) acted similar to aging with respect to tumor progression. We further investigated the molecular underpinnings driving the radiation modulation of tumor dynamics in young and middle-aged mice. Through global gene expression analysis the key players FASN AKT1 and the CXCL12/CXCR4 complex were determined to be contributory. In sum these findings demonstrate a reduced capacity of middle-aged hosts to support the progression phase of carcinogenesis and identify molecular factors contributory to HZE radiation modulation of tumor progression as a function of age. For genome-wide expression profiling of tumor tissue Mouse WG-6 BeadArray chips (Illumina San Diego CA) were used. Total RNA was amplified with the Ambion Illumina TotalPrep Amplification Kit (Ambion Austin TX) and labeled from all replicate biological samples for each condition. The number of tumor sample replicates used from each condition is as follows: 10 samples from young unirradiated mice 8 samples from young irradiated mice 7 samples from middle-aged unirradiated mice 5 samples from middle-aged irradiated mice. Total RNA was isolated and purified using Trizol (Invitrogen) or RNeasy (Qiagen) quantified and qualified using Agilent Bioanalyzer (Agilent) and samples were deemed suitable for amplification and hybridization if they had O.D. 260/280 = 1.7 - 2.1 28s/18s = 2:1 RIN (RNA integrity number) >7. Total RNA of 500ng per sample was amplified using Ambion TotalPrep (Ambion) and 1.5ug of the product was loaded onto the chips. Following hybridization at 55C the chips were washed and then scanned using the Illumina iScan (Illumina) and the data were analyzed using GenomeStudio (Illumina). Data were first analyzed for gene expression and then culled for present genes (genes that meet the criteria of detection p-value < 0.05). Expression above background was included in an expressed genes working data set for further analyses. Rank variant normalization was applied to the data before extensive analysis. Differential gene expression analysis was used to compare to the reference group young unirradiated mice and genes were then evaluated and validated.",
-            "title": "Age and Space Irradiation Modulate Tumor Progression: Implications for Carcinogenesis Risk",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-88",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Age and Space Irradiation Modulate Tumor Progression: Implications for Carcinogenesis Risk"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Age and Space Irradiation Modulate Tumor Progression: Implications for Carcinogenesis Risk"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3WCAE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Mission Cumulative Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3WCAE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Mission Cumulative Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T01:45:23Z/2015-06-07T11:41:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "ocean winds",
-                "oceans",
-                "earth science"
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
-            "identifier": "C2491757191-POCLOUD",
-            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales.\nThis particular data set is the mission series mean or cumulative, Ascending wind speed product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Mission Cumulative Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Mission Cumulative Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMIA_CUMULATIVE_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales.\nThis particular data set is the mission series mean or cumulative, Ascending wind speed product for version 5.0 of the Aquarius data set. Only retrieved values for Ascending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WCAE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WCAE",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMIA_CUMULATIVE_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMIA_CUMULATIVE_V5.jpg",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
-                    "description": "Information on observatory maneuvers, anomalies and other events",
                     "@type": "dcat:Distribution",
+                    "description": "Information on observatory maneuvers, anomalies and other events",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757191-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757191-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757191-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757191-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMIA_CUMULATIVE_V5.jpg",
+            "identifier": "C2491757191-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "ocean winds",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3WCAE",
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
+            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Mission Cumulative Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T01:45:23Z/2015-06-07T11:41:38Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Ascending Mission Cumulative Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCICA-2-EAR2-RAW-V1.0",
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
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RAW DATA from the RPCICA instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcica-2-ear2-raw-v1.0_a8rk-afas",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCICA-2-EAR2-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcica-2-ear2-raw-v1.0_a8rk-afas",
-            "description": "This dataset contains RAW DATA from the RPCICA instrument.",
-            "title": "ROSETTA-ORBITER EARTH RPCICA 2 EAR2 UNCALIBRATED V1.0",
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
+            "title": "ROSETTA-ORBITER EARTH RPCICA 2 EAR2 UNCALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V7.0",
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
-                "support archives",
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set lists name, designation(s), and discovery circumstances for all asteroids numbered as of the given stop date. It is compiled and maintain by David Tholen, and updated on a yearly basis.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v7.0_a8th-vrta",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V7.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v7.0_a8th-vrta",
-            "description": "This data set lists name, designation(s), and discovery circumstances for all asteroids numbered as of the given stop date. It is compiled and maintain by David Tholen, and updated on a yearly basis.",
-            "title": "ASTEROID NAMES AND DISCOVERY V7.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID NAMES AND DISCOVERY V7.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-3-RDR-VESTA-IMAGES-V1.0",
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
-                "4 vesta"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract                                                                   ========                                                                   Framing Camera 2 is one of two identical units flying on Dawn            spacecraft. This dataset includes the Reduced Data Record (RDR) version  of all available images acquired during the Vesta Encounter (Approach,   Survey, Transfer to HAMO, HAMO, Transfer to LAMO, LAMO, Transfer to      HAMO2, HAMO-2, and Transfer to Ceres). In addition to the imagery,       anciliary information is stored within the image headers, as well as a   detailed account of all the reference files used for the calibration.    Calibration files needed for further processing are archived as a        separate data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-3-rdr-vesta-images-v1.0_a8u9-qefw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC2-3-RDR-VESTA-IMAGES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc2-3-rdr-vesta-images-v1.0_a8u9-qefw",
-            "description": "Abstract                                                                   ========                                                                   Framing Camera 2 is one of two identical units flying on Dawn            spacecraft. This dataset includes the Reduced Data Record (RDR) version  of all available images acquired during the Vesta Encounter (Approach,   Survey, Transfer to HAMO, HAMO, Transfer to LAMO, LAMO, Transfer to      HAMO2, HAMO-2, and Transfer to Ceres). In addition to the imagery,       anciliary information is stored within the image headers, as well as a   detailed account of all the reference files used for the calibration.    Calibration files needed for further processing are archived as a        separate data set.",
-            "title": "DAWN FC2 CALIBRATED VESTA IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN FC2 CALIBRATED VESTA IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/1VSYYGQHJXIT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia Multitemporal Landslide Inventories V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/1VSYYGQHJXIT.",
-            "issued": "2009-12-01",
-            "temporal": "2009-12-01T00:00:00Z/2018-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-31",
-            "keyword": [
-                "earth science",
-                "erosion/sedimentation",
-                "land surface"
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
-            "identifier": "C2045817406-NSIDC_ECS",
             "description": "The mountains of Nepal are one of the most hazardous environments in the world, with frequent landslides caused by tectonic activity, extreme rainfall and infrastructure development. As a landlocked country, Nepal relies on proper functioning of major transportation networks such as the highways to sustain and improve the livelihoods of the population. Every year there are reports of landslides blocking the highways, especially during the rainy season; however, the frequency and location of landslides along the highway corridors are not well reported. RapidEye satellite imagery was used to create annual landslide initiation point inventories along three important highways in Nepal: the Arniko, Karnali, and Pasang Lhamu highway.",
-            "title": "High Mountain Asia Multitemporal Landslide Inventories V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1VSYYGQHJXIT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1VSYYGQHJXIT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_MTLI.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_MTLI.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA_MTLI+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HMA_MTLI+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_MTLI/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_MTLI/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1VSYYGQHJXIT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/1VSYYGQHJXIT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1VSYYGQHJXIT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/1VSYYGQHJXIT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2045817406-NSIDC_ECS",
+            "issued": "2009-12-01",
+            "keyword": [
+                "earth science",
+                "erosion/sedimentation",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/1VSYYGQHJXIT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "81.24 27.54 86.03 29.32",
+            "temporal": "2009-12-01T00:00:00Z/2018-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia Multitemporal Landslide Inventories V001"
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
+            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090518.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-612",
+            "issued": "2018-06-25",
             "keyword": [
                 "mtes",
                 "spice",
@@ -463005,363 +463014,367 @@
                 "mb",
                 "mi"
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
-            "identifier": "NASA-612",
-            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 20",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090518.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1175-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-12T07:48:40.000 to 2015-11-12T09:34:33.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1175-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1175-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1175-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-12T07:48:40.000 to 2015-11-12T09:34:33.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1175 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1175 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/W2WMLRUQOCA8",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLASIC07 In Situ Soil Moisture Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/W2WMLRUQOCA8.",
-            "issued": "2007-06-07",
-            "temporal": "2007-06-07T00:00:00Z/2007-07-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-07-07",
-            "keyword": [
-                "earth science",
-                "soils",
-                "land surface"
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
-            "identifier": "C1000001442-NSIDC_ECS",
             "description": "This data set is comprised of several parameters from in situ measurements collected for the Cloud and Land Surface Interaction Campaign 2007 (CLASIC07).",
-            "title": "CLASIC07 In Situ Soil Moisture Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW2WMLRUQOCA8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW2WMLRUQOCA8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/CL07SM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/CL07SM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001442-NSIDC_ECS&m=25.751953125%21-97.716796875%214%211%210%210%2C2&q=CLASIC07&ok=CLASIC07",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001442-NSIDC_ECS&m=25.751953125%21-97.716796875%214%211%210%210%2C2&q=CLASIC07&ok=CLASIC07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/CL07SM/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/CL07SM/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W2WMLRUQOCA8",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/W2WMLRUQOCA8",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W2WMLRUQOCA8",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/W2WMLRUQOCA8",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001442-NSIDC_ECS",
+            "issued": "2007-06-07",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/W2WMLRUQOCA8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-07-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.59 34.91 -97.95 35.21",
+            "temporal": "2007-06-07T00:00:00Z/2007-07-07T23:59:59.999Z",
             "theme": [
                 "CLASIC07",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLASIC07 In Situ Soil Moisture Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-EPAC-4-SUMM-PSTL2-FLUX-1HR-V1.0",
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
-                "ulysses",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Ulysses Energetic Particle Composition Experiment (EPAC) 1 hour averaged sectored proton flux data from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-28. These data were recorded by Proton Spectral Telescope 2 (PSTL2).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-epac-4-summ-pstl2-flux-1hr-v1.0_a8yk-rcur",
+            "issued": "2018-06-26",
+            "keyword": [
+                "ulysses",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-EPAC-4-SUMM-PSTL2-FLUX-1HR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-epac-4-summ-pstl2-flux-1hr-v1.0_a8yk-rcur",
-            "description": "This data set contains Ulysses Energetic Particle Composition Experiment (EPAC) 1 hour averaged sectored proton flux data from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-28. These data were recorded by Proton Spectral Telescope 2 (PSTL2).",
-            "title": "ULYSSES JUPITER EPAC PSTL2 PROTON SPECTRAL DATA 1 HR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES JUPITER EPAC PSTL2 PROTON SPECTRAL DATA 1 HR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/38/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elizabeth Foughty",
                 "hasEmail": "mailto:elizabeth.a.foughty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_38",
             "description": "It is becoming increasingly clear that the next generation of web search and advertising will rely on a deeper understanding of user intent and task modeling, and a correspondingly richer interpretation of content on the web. How we get there, in particular, how we understand web content in richer terms than bags of words and links, is a wide open and fascinating question. I will discuss some of the options here, and look closely at the role that information extraction can play.\r\n\r\n**Speaker Bio**\r\n\r\nRaghu Ramakrishnan is Chief Scientist for Audience and Cloud Computing at Yahoo!, and is a Research Fellow, heading the Community Systems area in Yahoo! Research. He was Professor of Computer Sciences at the University of Wisconsin-Madison, and was founder and CTO of QUIQ, a company that pioneered question-answering communities, powering Ask Jeeves' AnswerPoint as well as customer-support for companies such as Compaq. His research has influenced query optimization in commercial database systems, and the design of window functions in SQL:1999. His paper on the Birch clustering algorithm received the SIGMOD 10-Year Test-of-Time award, and he has written the widely-used text \"Database Management Systems\" (with Johannes Gehrke).\r\n\r\nHe is Chair of ACM SIGMOD, on the Board of Directors of ACM SIGKDD and the Board of Trustees of the VLDB Endowment, and has served as editor-in-chief of the Journal of Data Mining and Knowledge Discovery, associate editor of ACM Transactions on Database Systems, and the Database area editor of the Journal of Logic Programming. Ramakrishnan is a Fellow of the Association for Computing Machinery (ACM) and the Institute of Electrical and Electronics Engineers (IEEE), and has received several awards, including a Distinguished Alumnus Award from IIT Madras, a Packard Foundation Fellowship in Science and Engineering, an NSF Presidential Young Investigator Award, and an ACM SIGMOD Contributions Award.",
-            "title": "Ramakrishnan: Semantics on the Web",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/vnd.ms-powerpoint",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/nasa-cidu.ppt",
-                    "description": "nasa-cidu.ppt",
                     "@type": "dcat:Distribution",
+                    "description": "nasa-cidu.ppt",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/nasa-cidu.ppt",
+                    "mediaType": "application/vnd.ms-powerpoint",
                     "title": "nasa-cidu.ppt"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_38",
+            "issued": "2010-09-10",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/38/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Ramakrishnan: Semantics on the Web"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIRO-2-GRND-THERMAL-VAC-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, for the ground thermal-vacuum tests performed at NASA/JPL for the MIRO instrument of the Rosetta mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-miro-2-grnd-thermal-vac-v1.0_a8zw-u8sj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIRO-2-GRND-THERMAL-VAC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-miro-2-grnd-thermal-vac-v1.0_a8zw-u8sj",
-            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, for the ground thermal-vacuum tests performed at NASA/JPL for the MIRO instrument of the Rosetta mission.",
-            "title": "ROSETTA-ORBITER CAL MIRO 2 GRND THERMAL-VAC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL MIRO 2 GRND THERMAL-VAC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H41V5BWK",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "United States Census Bureau - USCB. 1990-12-31. Public Use Microdata Samples (PUMS). Version 1.00. Washington, DC. Archived by National Aeronautics and Space Administration, U.S. Government, United States Census Bureau (USCB). https://doi.org/10.7927/H41V5BWK. https://doi.org/10.7927/H41V5BWK.",
-            "issued": "1990-12-31",
-            "temporal": "1940-01-01T00:00:00Z/1990-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1990-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4Z60KZ9",
-                "https://doi.org/10.7927/H4G44N6R",
-                "https://doi.org/10.7927/H4BG2KWB",
-                "https://doi.org/10.7927/H47P8W9V",
-                "https://doi.org/10.7927/H43X84KH",
-                "https://doi.org/10.7927/H4057CV3",
-                "https://doi.org/10.7927/H4QN64NG",
-                "https://doi.org/10.7927/H46Q1V51",
-                "https://doi.org/10.7927/H4TD9V7F",
-                "https://doi.org/10.7927/H42Z13FP"
-            ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
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
-            "identifier": "C179001948-SEDAC",
-            "description": "The Public Use Microdata Samples (PUMS) are computer-accessible files containing records for a sample of housing Units, with information on the characteristics of each housing Unit and the people in it for 1940-1990. Within the limits of sample size and geographical detail, these files allow users to prepare virtually any tabulations they require. Each datafile is documented in a codebook containing a data dictionary and supporting appendix information. Electronic versions for the codebooks are only available for the 1980 and 1990 datafiles. Identifying information has been removed to protect the confidentiality of the respondents. PUMS is produced by the United States Census Bureau (USCB) and is distributed by USCB, Inter-university Consortium for Political and Social Research (ICPSR), and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Washington, DC",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "United States Census Bureau - USCB",
-            "title": "Public Use Microdata Samples (PUMS)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-public-use-microdata-samples/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Public Use Microdata Samples (PUMS) are computer-accessible files containing records for a sample of housing Units, with information on the characteristics of each housing Unit and the people in it for 1940-1990. Within the limits of sample size and geographical detail, these files allow users to prepare virtually any tabulations they require. Each datafile is documented in a codebook containing a data dictionary and supporting appendix information. Electronic versions for the codebooks are only available for the 1980 and 1990 datafiles. Identifying information has been removed to protect the confidentiality of the respondents. PUMS is produced by the United States Census Bureau (USCB) and is distributed by USCB, Inter-university Consortium for Political and Social Research (ICPSR), and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH41V5BWK",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH41V5BWK",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-public-use-microdata-samples/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-public-use-microdata-samples/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-public-use-microdata-samples/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-public-use-microdata-samples/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-public-use-microdata-samples",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-public-use-microdata-samples",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-public-use-microdata-samples/sedac-logo.jpg",
+            "identifier": "C179001948-SEDAC",
+            "issued": "1990-12-31",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H41V5BWK",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1990-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4Z60KZ9",
+                "https://doi.org/10.7927/H4G44N6R",
+                "https://doi.org/10.7927/H4BG2KWB",
+                "https://doi.org/10.7927/H47P8W9V",
+                "https://doi.org/10.7927/H43X84KH",
+                "https://doi.org/10.7927/H4057CV3",
+                "https://doi.org/10.7927/H4QN64NG",
+                "https://doi.org/10.7927/H46Q1V51",
+                "https://doi.org/10.7927/H4TD9V7F",
+                "https://doi.org/10.7927/H42Z13FP"
+            ],
+            "release-place": "Washington, DC",
             "spatial": "-180.0 18.0 -66.0 73.0",
+            "temporal": "1940-01-01T00:00:00Z/1990-12-31T00:00:00Z",
             "theme": [
                 "ACRP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Public Use Microdata Samples (PUMS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567147-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2010-01-01. USGS Global Forest Observations Initiative (GFOI) Borneo Island. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "JOHN FAUNDEEN",
+                "hasEmail": "mailto:faundeen@usgs.gov"
+            },
+            "creator": "U.S. Geological Survey",
+            "description": "The Forest Carbon Tracking Task (GEO FCT) has been established to support countries wanting to establish national forest-change, carbon estimation and reporting systems. It will facilitate access to long-term satellite, airborne and in situ data, provide the associated analysis and prediction tools, and create the appropriate framework and technical standards for a global network of national forest carbon tracking systems. The task follows the guidelines set out by the United Nations Framework Convention on Climate Change (UNFCCC). Its outputs will be available to support interested countries in their efforts to implement the Convention. The task is being carried out by a partnership of GEO member governments, key UN bodies, space agencies, the science community and the private sector.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Group on Earth Observations (GEO) Forest Carbon Tracking (FCT) home page.",
+                    "downloadURL": "http://www.gfoi.org/rd/forest-carbon-tracking/",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
+                }
+            ],
+            "identifier": "C1220567147-USGS_LTA",
             "issued": "1972-09-05",
-            "temporal": "1972-09-05T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "habitat conversion/fragmentation",
                 "forest science",
@@ -463372,331 +463385,299 @@
                 "human dimensions",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "JOHN FAUNDEEN",
-                "hasEmail": "mailto:faundeen@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567147-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-25",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DOI/USGS/EROS"
             },
-            "identifier": "C1220567147-USGS_LTA",
-            "description": "The Forest Carbon Tracking Task (GEO FCT) has been established to support countries wanting to establish national forest-change, carbon estimation and reporting systems. It will facilitate access to long-term satellite, airborne and in situ data, provide the associated analysis and prediction tools, and create the appropriate framework and technical standards for a global network of national forest carbon tracking systems. The task follows the guidelines set out by the United Nations Framework Convention on Climate Change (UNFCCC). Its outputs will be available to support interested countries in their efforts to implement the Convention. The task is being carried out by a partnership of GEO member governments, key UN bodies, space agencies, the science community and the private sector.",
-            "creator": "U.S. Geological Survey",
-            "title": "USGS Global Forest Observations Initiative (GFOI) Borneo Island",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.gfoi.org/rd/forest-carbon-tracking/",
-                    "description": "Group on Earth Observations (GEO) Forest Carbon Tracking (FCT) home page.",
-                    "@type": "dcat:Distribution",
-                    "title": "The dataset's project home page"
-                }
-            ],
             "spatial": "107.27 -5.32 121.3 8.2",
+            "temporal": "1972-09-05T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) Borneo Island"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-2-RVM1-CHECKOUT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the RENDEZVOUS MANOEUVRE 1 mission phase, covering the period  from 2010-09-04T00:00:00.000 to 2011-07-13T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-2-rvm1-checkout-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "dark",
                 "international rosetta mission",
                 "bias"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-2-RVM1-CHECKOUT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-2-rvm1-checkout-v1.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the RENDEZVOUS MANOEUVRE 1 mission phase, covering the period  from 2010-09-04T00:00:00.000 to 2011-07-13T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 2 RVM1 EDR V1.0",
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
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 2 RVM1 EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL12.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3A Ocean Surface Height V006. Version 006. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL12.006.",
-            "issued": "2018-10-14",
-            "temporal": "2018-10-13T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "sea surface topography"
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
-            "identifier": "C2613553216-NSIDC_CPRD",
             "description": "This data set (ATL12) contains along-track sea surface height of the global open ocean, including the ice-free seasonal ice zone and near-coast regions. Estimates of height distributions, significant wave height, sea state bias, and 10 m heights are also provided. The data were acquired by the Advanced Topographic Laser Altimeter System (ATLAS) instrument on board the Ice, Cloud and land Elevation Satellite-2 (ICESat-2) observatory.",
-            "title": "ATLAS/ICESat-2 L3A Ocean Surface Height V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL12.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL12.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL12+V006",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL12+V006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2613553216-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2613553216-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL12.006",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL12.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL12.006",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL12.006",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2613553216-NSIDC_CPRD",
+            "issued": "2018-10-14",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL12.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-10-13T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3A Ocean Surface Height V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/606",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Smith, E.A., J. Lamm, and J.J. Gu. 2001. BOREAS Follow-On HMet-01 Merged SSM/I and Rain Gauge Precipitation Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/606",
-            "issued": "2024-04-27",
-            "temporal": "1996-06-01T00:00:00Z/1996-10-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-28",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "precipitation"
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
-            "identifier": "C2956533064-ORNL_CLOUD",
             "description": "A gridded data set has been assembled over the BOREAS hydro-meteorological study region that combines a precipitation data set based on a rain gauge network with precipitation estimates based on SSM/I satellite images.  The result is an hourly precipitation data set covering 122 consecutive days beginning on June 1, 1996.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Follow-On HMet-01 Merged SSM/I and Rain Gauge Precipitation Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F606",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F606",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HMET/BFO_hmet01_ssmi_precip/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HMET/BFO_hmet01_ssmi_precip/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/hmet01_ssmi_precip_doc.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/hmet01_ssmi_precip_doc.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/606",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/606",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet01_ssmi_precip/comp/0_hmet01_ssmi_filecounts.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet01_ssmi_precip/comp/0_hmet01_ssmi_filecounts.dat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet01_ssmi_precip/comp/0_hmet01_ssmi_lat_lon.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet01_ssmi_precip/comp/0_hmet01_ssmi_lat_lon.dat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet01_ssmi_precip/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet01_ssmi_precip/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet01_ssmi_precip/comp/hmet01_ssmi_precip_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HMET/BFO_hmet01_ssmi_precip/comp/hmet01_ssmi_precip_doc.pdf",
+                    "mediaType": "application/pdf",
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
+            "identifier": "C2956533064-ORNL_CLOUD",
+            "issued": "2024-04-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/606",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-107.0 52.0 -96.0 57.0",
+            "temporal": "1996-06-01T00:00:00Z/1996-10-01T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Follow-On HMet-01 Merged SSM/I and Rain Gauge Precipitation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_met_bundle&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The original PHX MET dataset was submitted in 2008 by Cameron Dickinon",
+            "identifier": "urn:nasa:pds:phx_met_bundle_a974-fms7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phoenix meterology temperature pressure mars",
                 "mars",
                 "phoenix"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_met_bundle&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:phx_met_bundle_a974-fms7",
-            "description": "The original PHX MET dataset was submitted in 2008 by Cameron Dickinon",
-            "title": "Phoenix MET Bundle",
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
+            "title": "Phoenix MET Bundle"
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
-                "rss",
-                "pds"
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
-            "identifier": "NASA-761",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (37, 38)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -463704,196 +463685,217 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-761",
+            "issued": "2018-06-25",
+            "keyword": [
+                "rss",
+                "pds"
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
+            "title": "PDS Odyssey Radio Science Data (37, 38)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-5-RDR-MULTISPECTRAL-V1.0",
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
-                "mars reconnaissance orbiter",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains CRISM Multispectral Reduced Data Records (MRDRs). MRDRs are organized into 30 subdirectories named by the Mars Chart containing the MRDR, e.g. MC01. Latitude and longitude limits of Mars Charts are given below. An MRDR consists of several or more strips of multispectral survey data mosaicked into a map tile. Thus a map tile is constructed from a large number of TRDRs. The mosaic is uncontrolled (accepting existing pointing data often resulting in image mismatch at seams within a mosaic). The tile contains up to four images: radiance extracted from temporary TRDRs Lambert albedo summary products DDR data used to generate the first three images, augmented with additional positional information The MRDR also contains up to two text files, one listing the wavelengths present and ther other listing the SPICE metakernels used for map projection of each constituent observation on the tile. Each file has a separate label. For every latitude or longitude in an MRDR, there is a radiance and all the information providing traceability to through I/F to Lambert albedo corrected for atmospheric, photometric, and thermal emission effects, plus the information needed to reconstruct the map projection. A global pattern of 1964 such tiles is being used, forming the major data product for multispectral survey observations. Multiple MRDRs are in each of the 30 subdirectories.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-5-rdr-multispectral-v1.0_a9d2-ku67",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars reconnaissance orbiter",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-5-RDR-MULTISPECTRAL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-5-rdr-multispectral-v1.0_a9d2-ku67",
-            "description": "This dataset contains CRISM Multispectral Reduced Data Records (MRDRs). MRDRs are organized into 30 subdirectories named by the Mars Chart containing the MRDR, e.g. MC01. Latitude and longitude limits of Mars Charts are given below. An MRDR consists of several or more strips of multispectral survey data mosaicked into a map tile. Thus a map tile is constructed from a large number of TRDRs. The mosaic is uncontrolled (accepting existing pointing data often resulting in image mismatch at seams within a mosaic). The tile contains up to four images: radiance extracted from temporary TRDRs Lambert albedo summary products DDR data used to generate the first three images, augmented with additional positional information The MRDR also contains up to two text files, one listing the wavelengths present and ther other listing the SPICE metakernels used for map projection of each constituent observation on the tile. Each file has a separate label. For every latitude or longitude in an MRDR, there is a radiance and all the information providing traceability to through I/F to Lambert albedo corrected for atmospheric, photometric, and thermal emission effects, plus the information needed to reconstruct the map projection. A global pattern of 1964 such tiles is being used, forming the major data product for multispectral survey observations. Multiple MRDRs are in each of the 30 subdirectories.",
-            "title": "MRO CRISM MULTISPECTRAL REDUCED DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO CRISM MULTISPECTRAL REDUCED DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-NALT-IGDR-1.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-06-01. SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SGDR. Version 2.0. SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SGDR, Version 2.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWOT-NALT-IGDR-1.0.",
-            "issued": "2022-06-28",
-            "temporal": "2022-12-16T00:00:00Z/2023-11-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-28",
-            "keyword": [
-                "oceans",
-                "ocean waves",
-                "sea surface topography",
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
-            "identifier": "C2799465529-POCLOUD",
-            "description": "Same as L2_NALT_GDR, using preliminary values for some auxiliary data. Uses Medium-accuracy (preliminary) Orbit Ephemeris (MOE). Available with latency of < 1.5 days. Discrete measurements at nadir for each half orbit, along the ground track. Available in netCDF-4 file format.",
-            "series-name": "SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SGDR",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SGDR, Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_IGDR_1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Same as L2_NALT_GDR, using preliminary values for some auxiliary data. Uses Medium-accuracy (preliminary) Orbit Ephemeris (MOE). Available with latency of < 1.5 days. Discrete measurements at nadir for each half orbit, along the ground track. Available in netCDF-4 file format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-IGDR-1.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-IGDR-1.0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://swot.jpl.nasa.gov",
-                    "description": "SWOT Mission Page",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Mission Page",
+                    "downloadURL": "https://swot.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://swot.jpl.nasa.gov",
-                    "description": "SWOT Mission Page",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Mission Page",
+                    "downloadURL": "https://swot.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/swot",
-                    "description": "SWOT Mission Page at NASA",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Mission Page at NASA",
+                    "downloadURL": "https://www.nasa.gov/swot",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/missions/surface-water-and-ocean-topography-swot",
-                    "description": "SWOT Mission Page at JPL",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Mission Page at JPL",
+                    "downloadURL": "https://www.jpl.nasa.gov/missions/surface-water-and-ocean-topography-swot",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/swot",
-                    "description": "SWOT Mission Page at PO.DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Mission Page at PO.DAAC",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/swot",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.aviso.altimetry.fr/en/missions/current-missions/swot.html",
-                    "description": "SWOT Mission Page at AVISO",
                     "@type": "dcat:Distribution",
+                    "description": "SWOT Mission Page at AVISO",
+                    "downloadURL": "https://www.aviso.altimetry.fr/en/missions/current-missions/swot.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Data Subscriber",
                     "downloadURL": "https://github.com/podaac/data-subscriber",
-                    "mediaType": "text/html",
-                    "description": "Data Subscriber"
+                    "mediaType": "text/html"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2628600898-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2628600898-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2628600898-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2628600898-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_IGDR_1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_IGDR_1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SALP-ST-M-EA-17043-CN_0103_20220411_Rev1.3.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SALP-ST-M-EA-17043-CN_0103_20220411_Rev1.3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_IGDR_1.0.jpg",
+            "identifier": "C2799465529-POCLOUD",
+            "issued": "2022-06-28",
+            "keyword": [
+                "oceans",
+                "ocean waves",
+                "sea surface topography",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-NALT-IGDR-1.0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-06-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "series-name": "SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SGDR",
             "spatial": "-180.0 -77.6 180.0 77.6",
+            "temporal": "2022-12-16T00:00:00Z/2023-11-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Nadir Altimeter Interim Geophysical Data Record with Waveforms - SGDR, Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-CIRS-5-CUBES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set comprises uncalibrated\nand calibrated data from the Cassini Composite Infrared Spectrometer\n(CIRS) instrument. The basic data is comprised of uncalibrated raw spectra,\nalong with along with pointing and geometry information, and\nhousekeeping information. Also included are calibrated power spectra,\nand documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-cirs-5-cubes-v1.0_a9ei-a2ri",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dione",
                 "phoebe",
@@ -463917,203 +463919,184 @@
                 "hyperion",
                 "helene"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-CIRS-5-CUBES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-cirs-5-cubes-v1.0_a9ei-a2ri",
-            "description": "This data set comprises uncalibrated\nand calibrated data from the Cassini Composite Infrared Spectrometer\n(CIRS) instrument. The basic data is comprised of uncalibrated raw spectra,\nalong with along with pointing and geometry information, and\nhousekeeping information. Also included are calibrated power spectra,\nand documentation.",
-            "title": "CASSINI SATURN CIRS SPECTRAL CUBES RECORDS V1.0",
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
+            "title": "CASSINI SATURN CIRS SPECTRAL CUBES RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-LECP-4-SUMM-SCAN-24SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Description of the PDS LECP Uranus Scan data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-lecp-4-summ-scan-24sec-v1.0_a9fs-rjyh",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "comet sl9/jupiter collision",
                 "uranus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-LECP-4-SUMM-SCAN-24SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-lecp-4-summ-scan-24sec-v1.0_a9fs-rjyh",
-            "description": "Description of the PDS LECP Uranus Scan data.",
-            "title": "VG2 URA LECP RESAMPLED SUMMARY SCAN AVERAGED 24SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 URA LECP RESAMPLED SUMMARY SCAN AVERAGED 24SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR6%2FMR7-M-IRS-3-V1.0",
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
-                "mariner69",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set is a partial collection of spectra in digital form from the Mariner 6 and 7 Infrared Spectrometer experiments. All Mars and near-Mars sky spectra are included here, as well as some relevant laboratory spectra of blackbody sources. Lacking are the inflight spectra of reference targets including the wavelength calibration spectra. The IRS data are arranged as a single set of 512 spectra calibration spectra, followed by 122 Mariner 6 spectra, followed by 354 Mariner 7 spectra. The latter set is larger because the long-wavelength channel detector system failed on Mariner 6. These spectra are presented here in raw form, as originally supplied to the NSSDC on microfiche. Note that the geometry information in the spectrum headers was revised by the producer in 1984 to account for the revision in the location of the Mars pole following Mariner 9 observations.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr6-mr7-m-irs-3-v1.0_a9gd-s6qy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mariner69",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR6%2FMR7-M-IRS-3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr6-mr7-m-irs-3-v1.0_a9gd-s6qy",
-            "description": "This data set is a partial collection of spectra in digital form from the Mariner 6 and 7 Infrared Spectrometer experiments. All Mars and near-Mars sky spectra are included here, as well as some relevant laboratory spectra of blackbody sources. Lacking are the inflight spectra of reference targets including the wavelength calibration spectra. The IRS data are arranged as a single set of 512 spectra calibration spectra, followed by 122 Mariner 6 spectra, followed by 354 Mariner 7 spectra. The latter set is larger because the long-wavelength channel detector system failed on Mariner 6. These spectra are presented here in raw form, as originally supplied to the NSSDC on microfiche. Note that the geometry information in the spectrum headers was revised by the producer in 1984 to account for the revision in the location of the Mars pole following Mariner 9 observations.",
-            "title": "MR6/MR7 MARS INFRARED SPECTROMETER CALIBRATED DATA V1.0",
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
+            "title": "MR6/MR7 MARS INFRARED SPECTROMETER CALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-APD-POLARIMETRY-V1.0",
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
-                "support archives",
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Asteroid Polarimetric Database (APD) is compiled by Dmitrij Lupishko of Kharkov University. This database tabulates the original data comprising degree of polarization as a function of phase angle of the asteroid, and additional parameters where available. This data set, together with 'polar.tab' containing the TRIAD polarimetry, includes most if not all existing asteroid polarimetry data published by 1995. The APD is an ongoing compilation and this data set will be updated yearly.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-apd-polarimetry-v1.0_a9h4-8g94",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-APD-POLARIMETRY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-apd-polarimetry-v1.0_a9h4-8g94",
-            "description": "The Asteroid Polarimetric Database (APD) is compiled by Dmitrij Lupishko of Kharkov University. This database tabulates the original data comprising degree of polarization as a function of phase angle of the asteroid, and additional parameters where available. This data set, together with 'polar.tab' containing the TRIAD polarimetry, includes most if not all existing asteroid polarimetry data published by 1995. The APD is an ongoing compilation and this data set will be updated yearly.",
-            "title": "ASTEROID POLARIMETRIC DATABASE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID POLARIMETRIC DATABASE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-5-LUNAR-FIELD-BINS-V1.0",
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Lunar Prospector magnetometer (MAG) Level 3 Data (CODMAC Level 5).\nRegional Field Bins at the S/C Altitude.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-5-lunar-field-bins-v1.0_a9hz-6rpr",
+            "issued": "2021-05-21",
             "keyword": [
                 "lunar prospector",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-5-LUNAR-FIELD-BINS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-5-lunar-field-bins-v1.0_a9hz-6rpr",
-            "description": "Lunar Prospector magnetometer (MAG) Level 3 Data (CODMAC Level 5).\nRegional Field Bins at the S/C Altitude.",
-            "title": "LP MOON MAG LEVEL 5 LUNAR MAGNETIC FIELD BINS V1.0",
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
+            "title": "LP MOON MAG LEVEL 5 LUNAR MAGNETIC FIELD BINS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/roc/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "curve code augmentation",
-                "roc",
-                "receiver operating characteristic"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dennis Koga",
                 "hasEmail": "mailto:dennis.koga@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Ames Research Center"
-            },
-            "identifier": "OCIO-Fitara-144",
             "description": "ROC (Receiver Operating Characteristic) curve Code Augmentation was written by Rodney Martin and John Stutz at NASA Ames Research Center and is a modification of ROC Curve code originally authored by G.C. Cawley that provides additional functionality. The inclusion of more detailed bookkeeping of new and existing internal data structures that provide more visibility into various performance measures is one of the new features.",
-            "title": "ARC Code TI: ROC Curve Code Augmentation",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -464121,299 +464104,317 @@
                     "mediaType": "application/x-zip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-144",
+            "issued": "2015-01-07",
+            "keyword": [
+                "curve code augmentation",
+                "roc",
+                "receiver operating characteristic"
+            ],
+            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/roc/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Ames Research Center"
+            },
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "ARC Code TI: ROC Curve Code Augmentation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT3-MTP031-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 31 period of the EXTENSION 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext3-mtp031-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT3-MTP031-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext3-mtp031-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 31 period of the EXTENSION 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 3\n    MTP031 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 3\n    MTP031 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/MetNav_Aircraft_InSitu_P3B_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2024-09-06. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/MetNav_Aircraft_InSitu_P3B_Data_1.",
-            "issued": "2001-02-15",
-            "temporal": "2001-02-10T00:00:00Z/2002-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2001-04-10",
-            "keyword": [
-                "platform characteristics",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "earth science",
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric temperature",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2812963039-LARC_CLOUD",
             "description": "TRACE-P_MetNav_Aircraft_InSitu_P3B_Data is the in situ meteorology and navigation data collected onboard the P-3B aircraft during the Transport and Chemical Evolution over the Pacific (TRACE-P) suborbital campaign. Data from the P-3B Turbulent Air Motion Measurement System (TAMMS) is featured in this collection. Data collection for this product is complete.\r\n\r\nThe NASA TRACE-P mission was a part of NASA\u2019s Global Tropospheric Experiment (GTE) \u2013 an assemblage of missions conducted from 1983-2001 with various research goals and objectives.\u202fTRACE-P was a multi-organizational campaign with NASA, the National Center for Atmospheric Research (NCAR), and several US universities.\u202fTRACE-P deployed\u202fits payloads in the Pacific between the months of March and April 2001 with the goal of studying the air chemistry emerging\u202ffrom Asia\u202fto the western Pacific.\u202fAlong with this, TRACE-P had the objective\u202fstudying\u202fthe chemical evolution of the air as it moved away from Asia.\u202f \r\n\r\nIn order to accomplish its goals, the NASA DC-8 aircraft and NASA P-3B aircraft were deployed, each equipped with various instrumentation.\u202fTRACE-P also relied on ground sites,\u202fand\u202fsatellites\u202fto collect data. The DC-8 aircraft was equipped with 19 instruments in total\u202fwhile the P-3B\u202fboasted\u202f21 total instruments.\u202fSome instruments on the DC-8 include the Nephelometer, the GCMS, the Nitric Oxide Chemiluminescence, the Differential Absorption Lidar (DIAL), and the Dual Channel Collectors and Fluorometers, HPLC. The Nephelometer was utilized to gather data on various\u202fwavelengths\u202fincluding\u202faerosol\u202fscattering\u202f(450, 550, 700nm), aerosol absorption (565nm), equivalent BC mass, and air density ratio. The GCMS was responsible for capturing a multitude of compounds in the atmosphere, some of which include CH4, CH3CHO, CH3Br, CH3Cl, CHBr3, and C2H6O.\u202fDIAL was used for a variety of measurements, some of which include aerosol wavelength dependence (1064/587nm), IR aerosol scattering ratio (1064nm),\u202ftropopause heights and ozone columns, visible aerosol scattering ratio, composite tropospheric ozone cross-sections, and visible aerosol depolarization. Finally, the Dual Channel Collectors and Fluorometers, HPLC collected data on H2O2, CH3OOH, and CH2O in the atmosphere.\u202fThe P-3B aircraft was equipped with various instruments for TRACE-P, some of which include\u202fthe MSA/CIMS, the Non-dispersive IR Spectrometer, the PILS-Ion Chromatograph, and the\u202fCondensation particle counter and Pulse Height Analysis (PHA). The\u202fMSA/CIMS measured OH, H2SO4, MSA, and HNO3. The Non-dispersive IR Spectrometer took measurements on CO2 in the atmosphere. The PILS-Ion Chromatograph recorded measurements of compounds and elements in the atmosphere, including sodium, calcium, potassium, magnesium, chloride, NH4, NO3, and SO4. Finally, the Condensation particle counter and PHA was used to gather data on total UCN, UCN 3-8nm, and UCN 3-4nm. Along with the aircrafts, ground stations measured air quality from China along with C2H2, C2H6, CO, and HCN.\u202fFinally, satellites imagery was used to collect a multitude of data, some of the uses were to observe the history of lightning flashes,\u202fSeaWiFS\u202fcloud imagery, 8-day exposure to TOMS aerosols, and\u202fSeaWiFS\u202faerosol optical thickness. The imagery was used to best aid in planning for the aircraft deployment.",
-            "title": "TRACE-P In Situ P-3B Meteorology and Navigation Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-P%2FMetNav_Aircraft_InSitu_P3B_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTRACE-P%2FMetNav_Aircraft_InSitu_P3B_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/tracep.htm",
-                    "description": "TRACE-P Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRACE-P Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/tracep.htm",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/WhitePaper.htm",
-                    "description": "TRACE-P White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "TRACE-P White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/tracep/WhitePaper.htm",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2002JD003276",
-                    "description": "Transport and Chemical Evolution over the Pacific (TRACE-P)aircraft mission: Design, execution, and first results",
                     "@type": "dcat:Distribution",
+                    "description": "Transport and Chemical Evolution over the Pacific (TRACE-P)aircraft mission: Design, execution, and first results",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/epdf/10.1029/2002JD003276",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-gte.larc.nasa.gov/gte_hmpg.htm#table",
-                    "description": "GTE Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GTE Home Page",
+                    "downloadURL": "https://www-gte.larc.nasa.gov/gte_hmpg.htm#table",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_fmt.pdf",
-                    "description": "GTE Data Format",
                     "@type": "dcat:Distribution",
+                    "description": "GTE Data Format",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_fmt.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to Cite ASDC Data",
                     "@type": "dcat:Distribution",
+                    "description": "How to Cite ASDC Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2812963039-LARC_CLOUD",
-                    "description": "Earthdata Search for TRACE-P_MetNav_Aircraft_InSitu_P3B_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TRACE-P_MetNav_Aircraft_InSitu_P3B_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2812963039-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/MetNav_Aircraft_InSitu_P3B_Data_1",
-                    "description": "DOI data set landing page for TRACE-P_MetNav_Aircraft_InSitu_P3B_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TRACE-P_MetNav_Aircraft_InSitu_P3B_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/MetNav_Aircraft_InSitu_P3B_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2812963039-LARC_CLOUD",
+            "issued": "2001-02-15",
+            "keyword": [
+                "platform characteristics",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science",
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric temperature",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TRACE-P/MetNav_Aircraft_InSitu_P3B_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2001-04-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 6.89 180.0 40.95",
+            "temporal": "2001-02-10T00:00:00Z/2002-03-01T00:00:00Z",
             "theme": [
                 "TRACE-P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRACE-P In Situ P-3B Meteorology and Navigation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/EPEA/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/EPEA/DATA001.",
-            "issued": "2012-07-02",
-            "temporal": "2012-07-02T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
-                "ocean optics",
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
-            "identifier": "C1633360228-OB_DAAC",
             "description": "The EPEA (Estaci&oacute;n Permanente de Estudios Ambientales) time series station was started in 2000 and since 2003 belongs to ANTARES (www.antares.ws), a network of Latin American time series stations whose main goal is the study of long-term changes in coastal ecosystems to distinguish those due to natural variability from those due to external perurbations (anthropogenic effects).Different research groups at the INIDEP (the National Institute of Fisheries Research and Development of Argentina) sample at the EPEA station, monitoring chemical, environmental and bio-optical variables as well as the bacterioplankton, phytoplankton, zooplankton, and the icthyoplankton communities. EPEA station is located on the Argentine shelf (38&deg;28'S, 57&deg;41'W), 27.0 nautical miles from Mar del Plata city and 13.5 nautical miles from the coast and has a depth of 50m. EPEA is characterized by a temperate regime, with annual sea surface temperatures between 10&deg;C and 21&deg;C and salinity values ranging between 33.5 and 34.1. Occasionally the site can receive less salty waters coming from the North, influenced by the La Plata River, driving salinity values to less than 31.0. Its oceanographic regime is described as the transition between high salinity coastal waters to the medium shelf (Guerrero et al., 1997).",
-            "title": "ANTARES monitoring station at the EPEA Station on the Argentina shelf",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FEPEA%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FEPEA%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/EPEA/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/EPEA/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360228-OB_DAAC",
+            "issued": "2012-07-02",
+            "keyword": [
+                "ocean chemistry",
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "ocean optics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/EPEA/DATA001",
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
+            "temporal": "2012-07-02T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ANTARES monitoring station at the EPEA Station on the Argentina shelf"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CXEQS8KVIXEI",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge Narrow Swath ATM L1B Elevation and Return Strength V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CXEQS8KVIXEI.",
-            "issued": "2013-03-20",
-            "temporal": "2013-03-20T00:00:00Z/2019-11-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-20",
-            "keyword": [
-                "earth science",
-                "cryospheric indicators",
-                "climate indicators"
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
-            "identifier": "C1000000060-NSIDC_ECS",
             "description": "This data set contains spot elevation measurements of Greenland, Arctic, and Antarctic sea ice acquired using the NASA Airborne Topographic Mapper (ATM) narrow-swath instrumentation. The data were collected as part of Operation IceBridge funded aircraft survey campaigns.",
-            "title": "IceBridge Narrow Swath ATM L1B Elevation and Return Strength V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCXEQS8KVIXEI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCXEQS8KVIXEI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/icebridge/portal/",
-                    "description": "Tool to visualize, search, and download IceBridge data.",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to visualize, search, and download IceBridge data.",
+                    "downloadURL": "https://nsidc.org/icebridge/portal/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILNSA1B.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILNSA1B.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000060-NSIDC_ECS&m=-30.515625%21-0.5625%211%211%210%210%2C2&tl=1514139825%214%21%21&q=ILNSA1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000060-NSIDC_ECS&m=-30.515625%21-0.5625%211%211%210%210%2C2&tl=1514139825%214%21%21&q=ILNSA1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILNSA1B/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILNSA1B/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CXEQS8KVIXEI",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CXEQS8KVIXEI",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CXEQS8KVIXEI",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CXEQS8KVIXEI",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000060-NSIDC_ECS",
+            "issued": "2013-03-20",
+            "keyword": [
+                "earth science",
+                "cryospheric indicators",
+                "climate indicators"
+            ],
+            "landingPage": "https://doi.org/10.5067/CXEQS8KVIXEI",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-11-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2013-03-20T00:00:00Z/2019-11-20T23:59:59.999Z",
             "theme": [
                 "2013_AN_NASA",
                 "2013_GR_NASA",
@@ -464429,189 +464430,167 @@
                 "2019_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge Narrow Swath ATM L1B Elevation and Return Strength V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1201-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-19T09:00:45.000 to 2015-11-19T14:02:16.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1201-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1201-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1201-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-19T09:00:45.000 to 2015-11-19T14:02:16.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1201 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1201 V1.0"
         },
         {
```

