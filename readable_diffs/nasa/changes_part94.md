# Change History for nasa.json (Part 94)

### Changes from 31606f9 to dd2190f (Part 83/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cpex/cpex_dropsonde_readme.pdf",
-                    "description": "CPEX Dropsonde Data Readme",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX Dropsonde Data Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cpex/cpex_dropsonde_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ams.confex.com/ams/2019Annual/meetingapp.cgi/Paper/354310",
-                    "description": "AGU Poster # 262: The Doppler Aerosol Wind (DAWN) Lidar during CPEX 2017: Performance Assessment",
                     "@type": "dcat:Distribution",
+                    "description": "AGU Poster # 262: The Doppler Aerosol Wind (DAWN) Lidar during CPEX 2017: Performance Assessment",
+                    "downloadURL": "https://ams.confex.com/ams/2019Annual/meetingapp.cgi/Paper/354310",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/CPEX/DAWN_DC8_1",
-                    "description": "DOI data set landing page for CPEX_DAWN_DC8_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CPEX_DAWN_DC8_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/CPEX/DAWN_DC8_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/clouds-in-a-clear-sky",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"Clouds in a Clear Sky\" By Annette Varani",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: \"Clouds in a Clear Sky\" By Annette Varani",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/clouds-in-a-clear-sky",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/news/nasas-cpex-tackles-a-weather-fundamental",
-                    "description": "JPL.NASA.gov Article \"NASA's CPEX Tackles a Weather Fundamental\"",
                     "@type": "dcat:Distribution",
+                    "description": "JPL.NASA.gov Article \"NASA's CPEX Tackles a Weather Fundamental\"",
+                    "downloadURL": "https://www.jpl.nasa.gov/news/nasas-cpex-tackles-a-weather-fundamental",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CPEX/DAWN_DC8_1/",
-                    "description": "ASDC Direct Data Download for CPEX_DAWN_DC8_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CPEX_DAWN_DC8_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CPEX/DAWN_DC8_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1604278273-LARC_ASDC",
+            "issued": "2019-03-07",
+            "keyword": [
+                "atmospheric winds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/CPEX/DAWN_DC8_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>16.0 -97.0 16.0 -69.0 29.0 -69.0 29.0 -97.0 16.0 -97.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2017-05-27T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CPEX DAWN WIND PROFILES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-VIS-2-EDR-BR-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes sub-sampled versions of Viking Orbiter images that are intended to facilitate rapid viewing of the image collection. The image data in these browse images have been reduced in size by sub-sampling the original image by a factor of 4 in both lines and samples. Thus, the data volume has been reduced by a factor of 16. A Viking Orbiter browse image contains 264 lines and 300 samples. A filtering procedure was used in generating the browse images because Viking Orbiter images commonly contain noisy data or are missing data. The brightness value of a pixel in a browse image is the median brightness value of an array of 4 by 4 pixels from the original image. If the 4 by 4 array of original pixels contained zero values, those zero value pixels were not used in determining the median value. Of course, if the entire 4 by 4 array contained zero value pixels, the corresponding pixel in the browse image was assigned a zero value.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-vis-2-edr-br-v2.0_hict-vatr",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deimos",
                 "mars",
@@ -867242,37 +867244,47 @@
                 "star",
                 "viking"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-VIS-2-EDR-BR-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-vis-2-edr-br-v2.0_hict-vatr",
-            "description": "This data set includes sub-sampled versions of Viking Orbiter images that are intended to facilitate rapid viewing of the image collection. The image data in these browse images have been reduced in size by sub-sampling the original image by a factor of 4 in both lines and samples. Thus, the data volume has been reduced by a factor of 16. A Viking Orbiter browse image contains 264 lines and 300 samples. A filtering procedure was used in generating the browse images because Viking Orbiter images commonly contain noisy data or are missing data. The brightness value of a pixel in a browse image is the median brightness value of an array of 4 by 4 pixels from the original image. If the 4 by 4 array of original pixels contained zero values, those zero value pixels were not used in determining the median value. Of course, if the entire 4 by 4 array contained zero value pixels, the corresponding pixel in the browse image was assigned a zero value.",
-            "title": "VO1/VO2 MARS VISUAL IMAGING SS EXPRMNT DATA REC BROWSE V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VO1/VO2 MARS VISUAL IMAGING SS EXPRMNT DATA REC BROWSE V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243253631-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1B Sigma Naught Low Res Product Version 2",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1243253631-ASF",
             "issued": "2015-07-31",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-07",
             "keyword": [
                 "spectral/engineering",
                 "smap",
@@ -867285,989 +867297,953 @@
                 "earth observation satellites",
                 "active remote sensing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243253631-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-05-07",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1243253631-ASF",
-            "description": "SMAP Level 1B Sigma Naught Low Res Product Version 2",
-            "title": "SMAP_L1B_SIGMA_NAUGHT_LOW_RES_V002",
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
+            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP_L1B_SIGMA_NAUGHT_LOW_RES_V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0124",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-26. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0124.",
-            "issued": "1999-10-26",
-            "temporal": "1987-06-30T00:00:00Z/1987-07-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric winds",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001241-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.The Colorado State University surface radiation data set was collected from the radiometric ground station on San Nicolas Island, California. These data were collected during the FIRE marine stratocumulus IFO. The data consists of ten minute averages of wind speed, wind direction, air temperature, relative humidity and shortwave (.3 - 2.8 microns), near IR (.7 - 2.8 microns), and longwave (4 - 50 microns) radiation.",
-            "title": "First ISCCP Regional Experiment (FIRE) Marine Stratocumulus Colorado State University (CSU) Surface Radiation Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0124",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0124",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001241-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_MS_CSU_RADSURF_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_MS_CSU_RADSURF_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001241-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ms_csu_dataset.pdf",
-                    "description": "FIRE Marine Stratocumulus Colorado State University (CSU) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Marine Stratocumulus Colorado State University (CSU) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ms_csu_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/ms_csu_radsurf.hdr",
-                    "description": "RAD_SURF - Surface Radiometric and Met. data (tape files table)",
                     "@type": "dcat:Distribution",
+                    "description": "RAD_SURF - Surface Radiometric and Met. data (tape files table)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/ms_csu_radsurf.hdr",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/ms_csu_radsurf.toc",
-                    "description": "FIRE_MS_CSU_RADSURF_1 data table",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE_MS_CSU_RADSURF_1 data table",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/ms_csu_radsurf.toc",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ms_csu_radsurf.ps",
-                    "description": "FIRE Marine Stratocumulus sample read software and data files - Direct File Download (.ps) Readme",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Marine Stratocumulus sample read software and data files - Direct File Download (.ps) Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ms_csu_radsurf.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ms_csu_radsurf_sdfinfo.ps",
-                    "description": "Standard Data Format for FIRE Readme - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "Standard Data Format for FIRE Readme - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ms_csu_radsurf_sdfinfo.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_lib.c",
-                    "description": "fsdf_lib Program for reading FIRE Cirrus I, Cirrus II, and MS data sets - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "fsdf_lib Program for reading FIRE Cirrus I, Cirrus II, and MS data sets - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_lib.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_sdf.h",
-                    "description": "Program to Read D2 HDF Format Files Produced by ISCCP - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to Read D2 HDF Format Files Produced by ISCCP - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_sdf.h",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/firesdf_read.c",
-                    "description": "Readme to produce a general read program for users to access FIRE data set files in Standard Data Format (SDF) - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to produce a general read program for users to access FIRE data set files in Standard Data Format (SDF) - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/firesdf_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fsdf_header.c",
-                    "description": "SDF_HEADER used to parse the FIRE SDF defined header file, and two supporting functions (SDF_DDR, DDR_VAR) - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "SDF_HEADER used to parse the FIRE SDF defined header file, and two supporting functions (SDF_DDR, DDR_VAR) - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fsdf_header.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fsdf_vtoc.c",
-                    "description": "VTOC_read Program for reading records of FIRE Standard Data Format (SDF) Table Of Contents (VTOC) - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "VTOC_read Program for reading records of FIRE Standard Data Format (SDF) Table Of Contents (VTOC) - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fsdf_vtoc.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci1",
-                    "description": "Makefile.fci1 Release: 1.1 Date: 7/29/94",
                     "@type": "dcat:Distribution",
+                    "description": "Makefile.fci1 Release: 1.1 Date: 7/29/94",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fci1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0124",
-                    "description": "DOI data set landing page for FIRE_MS_CSU_RADSURF_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_MS_CSU_RADSURF_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0124",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_MS_CSU_RADSURF/",
-                    "description": "ASDC Direct Data Download for FIRE_MS_CSU_RADSURF_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_MS_CSU_RADSURF_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_MS_CSU_RADSURF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_MS_CSU_RADSURF/contents.html",
-                    "description": "OPeNDAP data access for FIRE_MS_CSU_RADSURF_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_MS_CSU_RADSURF_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_MS_CSU_RADSURF/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001241-LARC_ASDC",
+            "issued": "1999-10-26",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric winds",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0124",
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
             "spatial": "33.24 -119.4",
+            "temporal": "1987-06-30T00:00:00Z/1987-07-19T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Marine Stratocumulus Colorado State University (CSU) Surface Radiation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-MOTHEFAM-V1.0",
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
+            "description": "This dataset contains an updated compilation of asteroid families and clusters, resulting from the application of the Hierarchical Clustering Method (HCM) on a set of around 120,000 asteroids with available proper elements. Whenever available, the classification in the Bus taxonomy is provided for family members, based on spectra from the SMASS, SMASS2 and S3OS2 spectroscopic surveys.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-mothefam-v1.0_higz-v6cr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-VARGBDET-5-MOTHEFAM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-vargbdet-5-mothefam-v1.0_higz-v6cr",
-            "description": "This dataset contains an updated compilation of asteroid families and clusters, resulting from the application of the Hierarchical Clustering Method (HCM) on a set of around 120,000 asteroids with available proper elements. Whenever available, the classification in the Bus taxonomy is provided for family members, based on spectra from the SMASS, SMASS2 and S3OS2 spectroscopic surveys.",
-            "title": "MOTHE-DINIZ ASTEROID DYNAMICAL FAMILIES V1.0",
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
+            "title": "MOTHE-DINIZ ASTEROID DYNAMICAL FAMILIES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5M-3VF44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Ocean Three-Dimensional Volume Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5M-3VF44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Ocean Three-Dimensional Volume Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4); 10.5067/ECL5M-3VF44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "models",
-                "earth science reanalyses/assimilation models",
-                "oceans",
-                "earth science",
-                "ocean circulation",
-                "earth science services"
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
-            "identifier": "C1991543739-POCLOUD",
-            "description": "This dataset provides monthly-averaged ocean three-dimensional volume fluxes on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean Three-Dimensional Volume Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides monthly-averaged ocean three-dimensional volume fluxes on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-3VF44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-3VF44",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/ecco",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/ecco",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ecco-group.org",
-                    "description": "The project website for the ECCO Consortium.",
                     "@type": "dcat:Distribution",
+                    "description": "The project website for the ECCO Consortium.",
+                    "downloadURL": "https://www.ecco-group.org",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/",
-                    "description": "Software maintained by ECCO Consortium on GitHub.",
                     "@type": "dcat:Distribution",
+                    "description": "Software maintained by ECCO Consortium on GitHub.",
+                    "downloadURL": "https://github.com/ECCO-GROUP/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/ECCO-v4-Configurations/tree/master/ECCOv4%20Release%204",
-                    "description": "ECCO Version 4 Release 4 model configuration maintained by the ECCO Consortium on GitHub",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 model configuration maintained by the ECCO Consortium on GitHub",
+                    "downloadURL": "https://github.com/ECCO-GROUP/ECCO-v4-Configurations/tree/master/ECCOv4%20Release%204",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_reproduction_howto.pdf",
-                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_reproduction_howto.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ecco-v4-python-tutorial.readthedocs.io/",
-                    "description": "Python Tutorials for ECCO Central Production Version 4 (ECCO V4)",
                     "@type": "dcat:Distribution",
+                    "description": "Python Tutorials for ECCO Central Production Version 4 (ECCO V4)",
+                    "downloadURL": "https://ecco-v4-python-tutorial.readthedocs.io/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_user_guide.pdf",
-                    "description": "ECCO Version 4 Release 4 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 User Guide",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_synopsis.pdf",
-                    "description": "Synopsis of ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO Version 4 Release 4",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_synopsis.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dspace.mit.edu/handle/1721.1/110380",
-                    "description": "Synopsis of ECCO 'Central Estimate' global ocean and sea-ice state estimate, Version 4 Release 3",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO 'Central Estimate' global ocean and sea-ice state estimate, Version 4 Release 3",
+                    "downloadURL": "https://dspace.mit.edu/handle/1721.1/110380",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_overview_plots.pdf",
-                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_overview_plots.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5M-3VF44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECL5M-3VF44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543739-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543739-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543739-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543739-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OCEAN_3D_VOLUME_FLUX_LLC0090GRID_MONTHLY_V4R4.jpg",
+            "identifier": "C1991543739-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "models",
+                "earth science reanalyses/assimilation models",
+                "oceans",
+                "earth science",
+                "ocean circulation",
+                "earth science services"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5M-3VF44",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.5281/zenodo.3765928"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
             "theme": [
                 "ECCO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECCO Ocean Three-Dimensional Volume Fluxes - Monthly Mean llc90 Grid (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V9.0",
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
+            "description": "Absolute magnitudes and slopes, mostly IAU-adopted with exceptions noted, for all asteroids numbered as of the 2005 April 7 batch of Minor Planet Circulars.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v9.0_hiiw-js55",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTERMAG-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astermag-v9.0_hiiw-js55",
-            "description": "Absolute magnitudes and slopes, mostly IAU-adopted with exceptions noted, for all asteroids numbered as of the 2005 April 7 batch of Minor Planet Circulars.",
-            "title": "ASTEROID ABSOLUTE MAGNITUDES V9.0",
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
+            "title": "ASTEROID ABSOLUTE MAGNITUDES V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10765",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-11-01",
-            "temporal": "2010-11-01T00:00:00Z/2013-10-01T00:00:00Z",
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
-                "wallops flight facility",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Samuel Krucker",
                 "hasEmail": "mailto:krucker@ssl.berkeley.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10765",
             "description": "&lt;p&gt;\r\n\tParticle acceleration in solar flares and its contribution to coronal heating are among the main&amp;nbsp; unsolved problems in heliophysics. Accelerated electrons in a plasma radiate hard X-ray (HXR)&amp;nbsp; emission through the well-known process of bremsstrahlung. HXR observations therefore are a&amp;nbsp; powerful diagnostic tool, providing quantitative measurements of flare-accelerated electrons. Since&amp;nbsp; bremsstrahlung emission depends on the density of the ambient medium, solar HXR emission is&amp;nbsp; usually brightest from below the transition region, where the density increases rapidly towards the&amp;nbsp; photosphere. Electron beams entering the chromosphere lose energy quickly through collisions and&amp;nbsp; produce relatively intense HXR emission at the footpoints of magnetic field lines. Electron beams&amp;nbsp; moving in the relatively tenuous corona suffer very few collisions, losing little energy and producing&amp;nbsp; only faint HXR emission. Present-day HXR instrumentation does not have the sensitivity to see&amp;nbsp; faint HXR emission from electrons traveling in the corona, nor the dynamic range to see such&amp;nbsp; faint emission in the presence of bright HXR footpoint emission in the chromosphere. Existing&amp;nbsp; observations therefore show us only where energetic electrons are stopped, but not where they&amp;nbsp; are accelerated, nor along what path they escape from the acceleration site. The most sensitive&amp;nbsp; solar HXR observations so far are provided by the Reuven Ramaty High Energy Spectroscopic&amp;nbsp; Imager (RHESSI) (Lin et al. 2002). These measurements are obtained with a non-focusing rotation&amp;nbsp; modulation collimator (RMC) imaging technique (Hurford et al. 2002). RMCs and other types&amp;nbsp; of non-focusing imaging, however, have intrinsically limited dynamic range and sensitivity. HXR&amp;nbsp; focusing optics can overcome both of these limitations (Section 1.2.2).&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;\r\n\tThe Focusing Optics X-ray Solar Imager (FOXSI) is a sounding rocket payload funded under the&amp;nbsp; NASA Low Cost Access to Space (LCAS) program to test HXR focusing optics combined with&amp;nbsp; silicon strip detectors for solar observations (Krucker et al. 2009). The FOXSI program is being led&amp;nbsp; by the Space Sciences Laboratory at UC Berkeley in collaboration with the Marshall Space Flight&amp;nbsp; Center (MSFC) and the Japan Aerospace Exploration Agency (JAXA). FOXSI is on schedule&amp;nbsp; and on budget for a launch in October 2010. FOXSI will offer imaging spectroscopy and&amp;nbsp; unprecedented HXR sensitivity and dynamic range. FOXSI will be !100 times more sensitive than&amp;nbsp; RHESSI at 10 keV, and, for the first time, detect the non-thermal counterparts of quiet sun network&amp;nbsp; flares (Section 1.2.4).&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;\r\n\tHere we propose a continuation of the FOXSI program which includes data analysis&amp;nbsp; and a second flight with an upgraded version of FOXSI. At moderate cost, we propose to&amp;nbsp; enhance the effective area, in particular at higher energies (by a factor of !4 at 15 keV), by adding&amp;nbsp; 3 more shells to the existing 7-shell optics (see Figure 9). Furthermore, our Japanese collaborators&amp;nbsp; will provide, at no cost, newly available double-sided cadmium telluride (CdTe) detectors as&amp;nbsp; a replacement for the Si detectors to allow us to take full advantage of the effective area at higher&amp;nbsp; energies. A second flight will therefore not only allow us to continue testing HXR focusing&amp;nbsp; optics for solar observations and also test newly developed CdTe strip detectors&amp;nbsp; in flight but is also expected to provide a significant increase in scientific return. In&amp;nbsp; this two year proposal, the first year (2011) will be used to upgrade the FOXSI payload and to&amp;nbsp; analyze data from the first flight, while the second flight is planned for the midd",
-            "title": "The Focusing Optics X-ray Solar Imager (FOXSI): Update &amp; Second Launch Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10765",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10765",
+            "issued": "2010-11-01",
+            "keyword": [
+                "project",
+                "wallops flight facility",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10765",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
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
+            "temporal": "2010-11-01T00:00:00Z/2013-10-01T00:00:00Z",
+            "title": "The Focusing Optics X-ray Solar Imager (FOXSI): Update &amp; Second Launch Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-CR4A-CRUISE4A-V1.0",
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
-                "unknown"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Payload Checkout 8 (PC8) was an active checkout where a target independent opportunity to perform interactive operations and request spacecraft pointing was given to all Rosetta payload t All Rosetta payload took part in this scenario.The Active Payl Checkout 8 ran for 2 consecutive days (05-06 July2008) plus 26 consecutive days starting on the 9th July 2008 until the 1st A 2008. This is approximately twice the allocated time of the ac PC6 scenario that preceded it. PC8 consists of two pha similar to the previous Passive Payload Checkouts the 2nd phas an active test; GD02 is a Non nominal operational configuratio test (Only Impact Sensor operational and cover closed), in GD0 we have successfully tested a non-standard configuration, in was a test to investigate interference from other instruments. Redundant I/Fs in sequence and executing similar procedures fo two cases. GD02, GD03 and GD_INT were executed only on Main I/ ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalized for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-cr4a-cruise4a-v1.0_hijg-wtwh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-CR4A-CRUISE4A-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-cr4a-cruise4a-v1.0_hijg-wtwh",
-            "description": "Payload Checkout 8 (PC8) was an active checkout where a target independent opportunity to perform interactive operations and request spacecraft pointing was given to all Rosetta payload t All Rosetta payload took part in this scenario.The Active Payl Checkout 8 ran for 2 consecutive days (05-06 July2008) plus 26 consecutive days starting on the 9th July 2008 until the 1st A 2008. This is approximately twice the allocated time of the ac PC6 scenario that preceded it. PC8 consists of two pha similar to the previous Passive Payload Checkouts the 2nd phas an active test; GD02 is a Non nominal operational configuratio test (Only Impact Sensor operational and cover closed), in GD0 we have successfully tested a non-standard configuration, in was a test to investigate interference from other instruments. Redundant I/Fs in sequence and executing similar procedures fo two cases. GD02, GD03 and GD_INT were executed only on Main I/ ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalized for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
-            "title": "ROSETTA-ORBITER CHECK GIADA 2 CR4A CRUISE4A V1.0",
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
+            "title": "ROSETTA-ORBITER CHECK GIADA 2 CR4A CRUISE4A V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Merge_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-03-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Merge_Data_1.",
-            "issued": "2021-06-10",
-            "temporal": "2011-06-29T00:00:00Z/2011-08-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-21",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "aerosols",
-                "atmospheric water vapor",
-                "atmosphere",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Crawford",
                 "hasEmail": "mailto:james.h.crawford@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2241876240-LARC_ASDC",
             "description": "DISCOVERAQ_Maryland_Merge_Data contains pre-generated merged data files created from measurements obtained onboard the P-3B aircraft during the Maryland (Baltimore-Washington) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Maryland deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Maryland Deployment P-3B Aircraft Merged Data Files",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Merge_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Merge_Data_1",
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
-                    "downloadURL": "https://discover-aq.larc.nasa.gov/science/",
-                    "description": "DISCOVER-AQ Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "DISCOVER-AQ Project Home Page",
+                    "downloadURL": "https://discover-aq.larc.nasa.gov/science/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/discover-aq/docs/Crawford_DISCOVER-AQ_Overview_05Oct2010.pdf",
-                    "description": "DISCOVER-AQ Overview Presentation",
                     "@type": "dcat:Distribution",
+                    "description": "DISCOVER-AQ Overview Presentation",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/discover-aq/docs/Crawford_DISCOVER-AQ_Overview_05Oct2010.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/mission_pages/discover-aq/index.html",
-                    "description": "NASA DISCOVER-AQ Mission Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA DISCOVER-AQ Mission Page",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/discover-aq/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://discover-aq.larc.nasa.gov/wp-content/uploads/sites/140/2020/05/DISCOVER-AQ_TraceabilityMatrixPage16.pdf",
-                    "description": "DISCOVER-AQ Science Traceability Matrix",
                     "@type": "dcat:Distribution",
+                    "description": "DISCOVER-AQ Science Traceability Matrix",
+                    "downloadURL": "https://discover-aq.larc.nasa.gov/wp-content/uploads/sites/140/2020/05/DISCOVER-AQ_TraceabilityMatrixPage16.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://discover-aq.larc.nasa.gov/wp-content/uploads/sites/140/2020/05/DISCOVER-AQ_science.pdf",
-                    "description": "DISCOVER-AQ Science Plan",
                     "@type": "dcat:Distribution",
+                    "description": "DISCOVER-AQ Science Plan",
+                    "downloadURL": "https://discover-aq.larc.nasa.gov/wp-content/uploads/sites/140/2020/05/DISCOVER-AQ_science.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/earthmatters/2011/07/",
-                    "description": "DISCOVER-AQ Earth Observatory Posts",
                     "@type": "dcat:Distribution",
+                    "description": "DISCOVER-AQ Earth Observatory Posts",
+                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/earthmatters/2011/07/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/earthmatters/2011/07/15/not-your-average-video-traffic-report/",
-                    "description": "\u201cNot Your Average Video Traffic Report\u201d DISCOVER-AQ Earth Observatory Post",
                     "@type": "dcat:Distribution",
+                    "description": "\u201cNot Your Average Video Traffic Report\u201d DISCOVER-AQ Earth Observatory Post",
+                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/earthmatters/2011/07/15/not-your-average-video-traffic-report/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discover-aq.larc.nasa.gov/media/#news",
-                    "description": "DISCOVER-AQ News Releases",
                     "@type": "dcat:Distribution",
+                    "description": "DISCOVER-AQ News Releases",
+                    "downloadURL": "https://discover-aq.larc.nasa.gov/media/#news",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Merge_Data_1",
-                    "description": "DOI Data Set Landing Page for DISCOVERAQ_Maryland_Merge_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for DISCOVERAQ_Maryland_Merge_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Merge_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2241876240-LARC_ASDC",
-                    "description": "Earthdata Search for DISCOVERAQ_Maryland_Merge_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DISCOVERAQ_Maryland_Merge_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2241876240-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Merge_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Merge_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Merge_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Merge_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2241876240-LARC_ASDC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "aerosols",
+                "atmospheric water vapor",
+                "atmosphere",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Merge_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.0 -85.0 30.0 -70.0 45.0 -70.0 45.0 -85.0 30.0 -85.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2011-06-29T00:00:00Z/2011-08-02T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Maryland Deployment P-3B Aircraft Merged Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-3-EDR-GZ-V1.0",
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
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-3-edr-gz-v1.0_hin3-wksr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-3-EDR-GZ-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-3-edr-gz-v1.0_hin3-wksr",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET SPEC CALIBRATED EXPERIMENT DATA RECORD GZ V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET SPEC CALIBRATED EXPERIMENT DATA RECORD GZ V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-LAUNCH-V2.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-launch-v2.0_hinb-c6kp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-LAUNCH-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-launch-v2.0_hinb-c6kp",
-            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS SDC POST-LAUNCH CHECKOUT V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS SDC POST-LAUNCH CHECKOUT V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/IOP/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/IOP/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "earth science",
-                "ecosystems",
-                "biosphere"
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
-            "identifier": "C2340494129-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Mapped Inherent Optical Properties (IOP) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FIOP%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FIOP%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/IOP/2022",
-                    "description": "VIIRS-Suomi-NPP L3M Inherent Optical Properties (IOP) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M Inherent Optical Properties (IOP) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/IOP/2022",
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
+            "identifier": "C2340494129-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "earth science",
+                "ecosystems",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/IOP/2022",
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
+            "temporal": "2012-01-02T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi-NPP VIIRS Global Mapped Inherent Optical Properties (IOP) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1861",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Anthony, K.W., P. Hanke, and P. Lindgren. 2021. ABoVE: Methane Ebullition Hotspots in Frozen Lakes near Fairbanks, Alaska, Oct 2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1861",
-            "issued": "2022-05-10",
-            "temporal": "2014-10-08T00:00:00Z/2014-10-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "climate indicators",
-                "terrestrial hydrosphere indicators",
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "snow/ice",
-                "paleoclimate indicators"
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
-            "identifier": "C2143401746-ORNL_CLOUD",
             "description": "This dataset includes maps of the locations and number of methane ebullition hotspots in 15 frozen lakes in the southern portion of the Goldstream Valley and the surrounding landscape just north of Fairbanks, Alaska, USA. Hotspots were identified from early winter high resolution aerial photographs acquired three days after lake-ice formation in October 2014. Hotspot ebullition seeps are defined as point-sources of high ebullition that release methane from lake sediments year-round. High rates of bubbling impede ice formation. In early winter, bubbling leads to dark, round open holes in lake ice which were visible in the aerial photos. This project investigated the role of theromkarst lakes in thawing of permafrost and mobilization of organic carbon in frozen soils.",
-            "graphic-preview-description": "Location of 15 lakes surveyed for methane ebullition hotspots (green points) north of Fairbanks, AK, on October 8, 2014. Inset shows detail of Eagle Lake with locations of 43 hotspots (red points) detected by openings in lake ice.",
-            "title": "ABoVE: Methane Ebullition Hotspots in Frozen Lakes near Fairbanks, Alaska, Oct 2014",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Methane_Ebullition_Lakes_AK_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1861",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1861",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Methane_Ebullition_Lakes_AK/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Methane_Ebullition_Lakes_AK/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Methane_Ebullition_Lakes_AK.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Methane_Ebullition_Lakes_AK.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1861",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1861",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Methane_Ebullition_Lakes_AK/comp/Methane_Ebullition_Lakes_AK.pdf",
-                    "description": "ABoVE: Methane Ebullition Hotspots in Frozen Lakes near Fairbanks, Alaska, Oct 2014: Methane_Ebullition_Lakes_AK.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Methane Ebullition Hotspots in Frozen Lakes near Fairbanks, Alaska, Oct 2014: Methane_Ebullition_Lakes_AK.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Methane_Ebullition_Lakes_AK/comp/Methane_Ebullition_Lakes_AK.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Methane_Ebullition_Lakes_AK_Fig1.jpg",
-                    "description": "Location of 15 lakes surveyed for methane ebullition hotspots (green points) north of Fairbanks, AK, on October 8, 2014. Inset shows detail of Eagle Lake with locations of 43 hotspots (red points) detected by openings in lake ice.",
                     "@type": "dcat:Distribution",
+                    "description": "Location of 15 lakes surveyed for methane ebullition hotspots (green points) north of Fairbanks, AK, on October 8, 2014. Inset shows detail of Eagle Lake with locations of 43 hotspots (red points) detected by openings in lake ice.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Methane_Ebullition_Lakes_AK_Fig1.jpg",
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
+            "graphic-preview-description": "Location of 15 lakes surveyed for methane ebullition hotspots (green points) north of Fairbanks, AK, on October 8, 2014. Inset shows detail of Eagle Lake with locations of 43 hotspots (red points) detected by openings in lake ice.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Methane_Ebullition_Lakes_AK_Fig1.jpg",
+            "identifier": "C2143401746-ORNL_CLOUD",
+            "issued": "2022-05-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "climate indicators",
+                "terrestrial hydrosphere indicators",
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "snow/ice",
+                "paleoclimate indicators"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1861",
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
             "spatial": "-147.94 64.86 -147.77 64.94",
+            "temporal": "2014-10-08T00:00:00Z/2014-10-08T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Methane Ebullition Hotspots in Frozen Lakes near Fairbanks, Alaska, Oct 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-06-03",
-            "temporal": "2021-06-03T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coords",
-                "station",
-                "ephemeris",
-                "international",
-                "iss",
-                "location",
-                "topo",
-                "space",
-                "coordinates",
-                "trajectory"
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
-            "identifier": "nasa-iss-data_2021-06-03_his8-ymzd",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-06-03",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -868390,466 +868366,492 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-06-03_his8-ymzd",
+            "issued": "2021-06-03",
+            "keyword": [
+                "coords",
+                "station",
+                "ephemeris",
+                "international",
+                "iss",
+                "location",
+                "topo",
+                "space",
+                "coordinates",
+                "trajectory"
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
+            "temporal": "2021-06-03T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-06-03"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-HGCOORDS-9.60SEC-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-hgcoords-9.60sec-v1.0_hisq-iw4h",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-HGCOORDS-9.60SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-hgcoords-9.60sec-v1.0_hisq-iw4h",
-            "description": "not applicable",
-            "title": "VG1 JUP MAG RESAMPLED HELIOGRAPHIC (RTN) COORDS 9.60SEC V1.0",
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
+            "title": "VG1 JUP MAG RESAMPLED HELIOGRAPHIC (RTN) COORDS 9.60SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MI-5-ANAGLYPH-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mi-5-anaglyph-ops-v1.0_hita-i7pv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MI-5-ANAGLYPH-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mi-5-anaglyph-ops-v1.0_hita-i7pv",
-            "description": "not applicable",
-            "title": "MER 1 MARS MICROSCOPIC IMAGER ANAGLYPH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS MICROSCOPIC IMAGER ANAGLYPH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0721-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-21T08:08:35.000 to 2015-04-21T10:14:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0721-v1.0_hitd-kkc3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0721-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0721-v1.0_hitd-kkc3",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-21T08:08:35.000 to 2015-04-21T10:14:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0721 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0721 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ainsight_cameras&version=1.0",
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
-                "insight"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "InSight Cameras Experiment Data Record (EDR) and Reduced Data Record (RDR) Data Products",
+            "identifier": "urn:nasa:pds:insight_cameras",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "insight"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Ainsight_cameras&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:insight_cameras",
-            "description": "InSight Cameras Experiment Data Record (EDR) and Reduced Data Record (RDR) Data Products",
-            "title": "InSight Cameras Bundle",
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
+            "title": "InSight Cameras Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0060",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0060.",
-            "issued": "1999-11-03",
-            "temporal": "1992-06-02T00:00:00Z/1992-06-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
-            "keyword": [
-                "microwave",
-                "atmospheric water vapor",
-                "atmosphere",
-                "spectral/engineering",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ALAIN WEILL",
                 "hasEmail": "mailto:alain.weill@cetp.ipsl.fr"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001044-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.SOFIA (Surface of the Ocean, Fluxes and Interaction with the Atmosphere) is a research program carried out by French groups from the Centre de Recherches en Physique de l'Environnement (CRPE), Laboratoire l'Aerologie (LA)-Toulouse, Centre de Meteorologie Marine (CMM)-Brest, Institut Francais de Rechercher sur la Mer (IFREMER)-Brest, Service d'Aeronomie-Paris, and Laboratoire de Meteorologie Dynamique (LMD)-Palaiseau with cooperation from Centre National de Recherche Meteorologique (CNRM)-Toulouse.The scientific objective of SOFIA during ASTEX was the study of energy transfer (heat, humidity and momentum fluxes) between the sea surface and the atmospheric boundary layer at scales ranging from the local scale to the mesoscale (50 km). The general concept of the program was to develop a measurement strategy based on nested boxes in which instrumentation would be used to estimate and quantify fluxes. These instruments, from which flux estimates at different scales would be measured, were used in connection with satellite measurements to understand and, hence, to validate the satellite integration of fluxes, particularly in the presence of mesoscale oceanic andatmospheric structures responsible for spatial inhomogeneity of fluxes.Data were collected using a DRAKKAR, an upward pointing, two channel microwave radiometer. Its channels are 23.8 and 36.5 GHz, and the antenna aperture is about 15 degrees. It was developed at CRPE based upon the the ATSR/M (ERS-1/MWR) design. Its basic sampling was 0.5 seconds during ASTEX. Calibration was performed prior to the campaign and verified using a cold load on June 12, 1995, and verified again after return to France.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) SOFIA Le Suroit Microwave Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0060",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0060",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001044-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_SOF_SUR_DRAK_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_SOF_SUR_DRAK_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001044-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sof_sur_drak_read.c",
-                    "description": "Program RD_AX_DRAKKR.c - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Program RD_AX_DRAKKR.c - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sof_sur_drak_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sof_sur_nav_dat_read.c",
-                    "description": "Readme to read the SOFIA-SUROIT_NAV FIRE_ASTEX_NAT data file - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to read the SOFIA-SUROIT_NAV FIRE_ASTEX_NAT data file - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sof_sur_nav_dat_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sof_sur_drak_info1",
-                    "description": "DRAKKAR Data Overview Readme",
                     "@type": "dcat:Distribution",
+                    "description": "DRAKKAR Data Overview Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sof_sur_drak_info1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sof_sur_drak.ps",
-                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sof_sur_drak.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0060",
-                    "description": "DOI data set landing page for FIRE_AX_SOF_SUR_DRAK_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_SOF_SUR_DRAK_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0060",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_sofia_dataset.pdf",
-                    "description": "FIRE ASTEX Surface of the Ocean, Fluxes and Interaction with the Atmosphere (SOFIA) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Surface of the Ocean, Fluxes and Interaction with the Atmosphere (SOFIA) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_sofia_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_SOF_SUR_DRAK/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_SOF_SUR_DRAK_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_SOF_SUR_DRAK_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_SOF_SUR_DRAK/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_SOF_SUR_DRAK/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_SOF_SUR_DRAK_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_SOF_SUR_DRAK_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_SOF_SUR_DRAK/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001044-LARC_ASDC",
+            "issued": "1999-11-03",
+            "keyword": [
+                "microwave",
+                "atmospheric water vapor",
+                "atmosphere",
+                "spectral/engineering",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0060",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>34.5 -26.8 34.5 -23.2 37.8 -23.2 37.8 -26.8 34.5 -26.8</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-02T00:00:00Z/1992-06-19T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) SOFIA Le Suroit Microwave Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC2-67P-M15-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc2-67p-m15-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC2-67P-M15-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc2-67p-m15-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC2-MTP015 DDR-GEO V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC2-MTP015 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000501-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "2006-06-12",
-            "temporal": "2004-07-01T00:00:00Z/2004-08-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-25",
-            "keyword": [
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000501-LARC_ASDC",
             "description": "INTEX-A Ozonesonde data.",
-            "title": "INTEXA_O3SONDES",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000501-LARC_ASDC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000501-LARC_ASDC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1000000501-LARC_ASDC",
+            "issued": "2006-06-12",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000501-LARC_ASDC.html",
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
+            "temporal": "2004-07-01T00:00:00Z/2004-08-13T23:59:59Z",
             "theme": [
                 "INTEXA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "INTEXA_O3SONDES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-COSIMA-3-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Rosetta COSIMA data contains the operational history of the 72 dust collecting substrates from the installation inside the instrument. The operations are either expose, storage, spectra, total intensity, heating, imaging or grain lists. The data is grouped by the substrate and time. Up to the 2014-08 the aim of the data has been the instrument health and operational functionality, not statistically significant substrate background spectra. From 2014-08 onward the D0 substrate set was used to collect dust collected in the vicinity of 67P/CHURYUMOV GERASIMENKO 1 (1969 R1) and dust analysis with TOF-SIMS. From 2014-10-23 onward due to an instrument failure, the SIMS data became scientifically unusable. While other SIMS parameter sets were tested, substrates CF were exposed from mid 2015-12 and C7 from mid 2015-02. This data set supersedes all previous COSIMA datasets, like RO-C-COSIMA-3-V1.0, RO-CAL-COSIMA-2-V1.0 and RO-CAL-COSIMA-3-V3.0 Also, in the above previous versions, the values of the temperature in the HK data where given in Celsius although Kelvin was written in the description of the table in the FMT file",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cosima-3-v2.0_hiwm-42ag",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-COSIMA-3-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cosima-3-v2.0_hiwm-42ag",
-            "description": "The Rosetta COSIMA data contains the operational history of the 72 dust collecting substrates from the installation inside the instrument. The operations are either expose, storage, spectra, total intensity, heating, imaging or grain lists. The data is grouped by the substrate and time. Up to the 2014-08 the aim of the data has been the instrument health and operational functionality, not statistically significant substrate background spectra. From 2014-08 onward the D0 substrate set was used to collect dust collected in the vicinity of 67P/CHURYUMOV GERASIMENKO 1 (1969 R1) and dust analysis with TOF-SIMS. From 2014-10-23 onward due to an instrument failure, the SIMS data became scientifically unusable. While other SIMS parameter sets were tested, substrates CF were exposed from mid 2015-12 and C7 from mid 2015-02. This data set supersedes all previous COSIMA datasets, like RO-C-COSIMA-3-V1.0, RO-CAL-COSIMA-2-V1.0 and RO-CAL-COSIMA-3-V3.0 Also, in the above previous versions, the values of the temperature in the HK data where given in Celsius although Kelvin was written in the description of the table in the FMT file",
-            "title": "ROSETTA-ORBITER 67P COSIMA 3\n                                      V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P COSIMA 3\n                                      V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M12-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m12-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "dark",
@@ -868857,76 +868859,86 @@
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M12-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m12-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 2 ESC1-MTP012 EDR V3.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 2 ESC1-MTP012 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC2-67PCHURYUMOV-M16-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc2-67pchuryumov-m16-v3.0",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC2-67PCHURYUMOV-M16-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc2-67pchuryumov-m16-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 ESC2-MTP016 RDR V3.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 ESC2-MTP016 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567922-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ANNIEPAT JOHNSON",
+                "hasEmail": "mailto:lta@usgs.gov"
+            },
+            "description": "Developments in mapping methodology, new sources of input data, and changes in the mapping legend for the 2001 National Land Cover Database (NLCD2001) will confound any direct comparison between NLCD2001 and National Land Cover Dataset 1992 (NLCD1992). Users are cautioned that direct comparison of these two independently created land cover products is not recommended. This NLCD 1992/2001 Retrofit Land Cover Change Product was developed to offer users more accurate direct change analysis between the two products.\n\nThe NLCD 1992/2001 Retrofit Land Cover Change Product uses a specially developed methodology to provide land cover change information at the Anderson Level I classification scale (Anderson et al., 1976*), relying on decision tree classification of Landsat satellite imagery from circa 1992 and 2001. Unchanged pixels between the two dates are coded with the NLCD01 Anderson Level I class code, while changed pixels are labeled with a \"from-to\" land cover change value. Additional details about this product are available in the metadata included in the multi-zone downloadable zip file. This product is designed for regional application only and is not recommended for local scales.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1220567922-USGS_LTA",
             "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2001-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2001-12-31",
             "keyword": [
                 "geomorphic landforms/processes",
                 "topography",
@@ -868938,266 +868950,268 @@
                 "erosion/sedimentation",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ANNIEPAT JOHNSON",
-                "hasEmail": "mailto:lta@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567922-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2001-12-31",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DOI/USGS/EROS"
             },
-            "identifier": "C1220567922-USGS_LTA",
-            "description": "Developments in mapping methodology, new sources of input data, and changes in the mapping legend for the 2001 National Land Cover Database (NLCD2001) will confound any direct comparison between NLCD2001 and National Land Cover Dataset 1992 (NLCD1992). Users are cautioned that direct comparison of these two independently created land cover products is not recommended. This NLCD 1992/2001 Retrofit Land Cover Change Product was developed to offer users more accurate direct change analysis between the two products.\n\nThe NLCD 1992/2001 Retrofit Land Cover Change Product uses a specially developed methodology to provide land cover change information at the Anderson Level I classification scale (Anderson et al., 1976*), relying on decision tree classification of Landsat satellite imagery from circa 1992 and 2001. Unchanged pixels between the two dates are coded with the NLCD01 Anderson Level I class code, while changed pixels are labeled with a \"from-to\" land cover change value. Additional details about this product are available in the metadata included in the multi-zone downloadable zip file. This product is designed for regional application only and is not recommended for local scales.",
-            "title": "NLCD 1992/2001 Retrofit Land Cover Change Product",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2001-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NLCD 1992/2001 Retrofit Land Cover Change Product"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TOCC1-V1.0",
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
-                "titan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Titan Occultation Experiment (TOCC1) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 28, 2007, during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tocc1-v1.0_hj29-c4ha",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TOCC1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tocc1-v1.0_hj29-c4ha",
-            "description": "The Cassini Radio Science Titan Occultation Experiment (TOCC1) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 28, 2007, during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - TOCC1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TOCC1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-5-EROS%2FSHAPE%2FGRAVITY-V1.0",
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
+            "description": "NEAR Eros shape/gravity science derived data from NEAR NAV team at JPL.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-5-eros-shape-gravity-v1.0_hj2i-hn33",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-5-EROS%2FSHAPE%2FGRAVITY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-5-eros-shape-gravity-v1.0_hj2i-hn33",
-            "description": "NEAR Eros shape/gravity science derived data from NEAR NAV team at JPL.",
-            "title": "NEAR EROS NLR DERIVED PRODUCTS - SHAPE MODEL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR EROS NLR DERIVED PRODUCTS - SHAPE MODEL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-RAD-2-EDR-V1.0",
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
-                "mars science laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the EDR data from the MSL Radiation Assessment Detector (RAD) instrument. The EDR data are raw data reconstructed from telemetry data products.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rad-2-edr-v1.0_hj3a-m4gj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-RAD-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rad-2-edr-v1.0_hj3a-m4gj",
-            "description": "This data set contains the EDR data from the MSL Radiation Assessment Detector (RAD) instrument. The EDR data are raw data reconstructed from telemetry data products.",
-            "title": "MSL MARS RADIATION ASSESSMENT DETECTOR EDR",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL MARS RADIATION ASSESSMENT DETECTOR EDR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-POS-4-SUMM-HGCOORDS-V1.0",
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
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of Voyager 2 Saturn encounter ephemeris data in Heliographic coordinates covering the period 1981-08-24 to 1981-09-02. Two versions, both covering the same time period, but containing slightly different data, are provided. One version was generated by the Voyager MAG team from Voyager 2 SEDR, the other by the PDS/PPI node using the VG2_SAT.TSP and PCK00006.TPC SPICE kernels.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pos-4-summ-hgcoords-v1.0_hj45-ts89",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-POS-4-SUMM-HGCOORDS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pos-4-summ-hgcoords-v1.0_hj45-ts89",
-            "description": "This data set consists of Voyager 2 Saturn encounter ephemeris data in Heliographic coordinates covering the period 1981-08-24 to 1981-09-02. Two versions, both covering the same time period, but containing slightly different data, are provided. One version was generated by the Voyager MAG team from Voyager 2 SEDR, the other by the PDS/PPI node using the VG2_SAT.TSP and PCK00006.TPC SPICE kernels.",
-            "title": "VG2 SAT EPHEMERIS HELIOGRAPHIC COORDS\nBROWSE V1.0",
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
+            "title": "VG2 SAT EPHEMERIS HELIOGRAPHIC COORDS\nBROWSE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa17sep&version=1.0",
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
-                "moon",
-                "apollo 17"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains two comma-delimited ASCII files of calibrated lunar surface electromagnetic field and navigation (range) data from the Surface Electrical Properties (SEP) Experiment at the Apollo 17 landing site for the time span of 11-13 December 1972. One file contains straightened science and navigation (range) data; the other file contains only unstraightened science data. These data were extracted from binary files held on magnetic tape at the NASA Space Science Data Coordinated Archive as data set PSPG-00559, then reformatted to ASCII. This bundle also contains a high-resolution digital reproduction of the SEP final technical report that contains plots of the complete set of processed lunar field data, as decibal values versus range, and explanations the data processing and calibration techniques implemented by the SEP instrument team.",
+            "identifier": "urn:nasa:pds:a17sep",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "apollo 17"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa17sep&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:a17sep",
-            "description": "This bundle contains two comma-delimited ASCII files of calibrated lunar surface electromagnetic field and navigation (range) data from the Surface Electrical Properties (SEP) Experiment at the Apollo 17 landing site for the time span of 11-13 December 1972. One file contains straightened science and navigation (range) data; the other file contains only unstraightened science data. These data were extracted from binary files held on magnetic tape at the NASA Space Science Data Coordinated Archive as data set PSPG-00559, then reformatted to ASCII. This bundle also contains a high-resolution digital reproduction of the SEP final technical report that contains plots of the complete set of processed lunar field data, as decibal values versus range, and explanations the data processing and calibration techniques implemented by the SEP instrument team.",
-            "title": "Apollo 17 Surface Electrical Properties Experiment Calibrated ASCII Data Bundle",
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
+            "title": "Apollo 17 Surface Electrical Properties Experiment Calibrated ASCII Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0539-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-16T10:14:16.000 to 2015-01-16T11:36:06.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0539-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0539-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0539-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-16T10:14:16.000 to 2015-01-16T11:36:06.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0539 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0539 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/hjbw-ww9w",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The vestibular system receives a permanent influence from gravity and reflexively controls equilibrium. If we assume gravity has remained constant during the species   evolution will its sensory system adapt to abrupt loss of that force? We address this question in the land snail Helix lucorum exposed to 30 days of near weightlessness aboard the Bion-M1 satellite and studied geotactic behavior of postflight snails differential gene expressions in statocyst transcriptome and electrophysiological responses of mechanoreceptors to applied tilts. Each approach revealed plastic changes in the snail  s vestibular system assumed in response to spaceflight. Absence of light during the mission also affected statocyst physiology as revealed by comparison to dark-conditioned control groups. Readaptation to normal tilt responses occurred at ~20 h following return to Earth. Despite the permanence of gravity the snail responded in a compensatory manner to its loss and readapted once gravity was restored.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-192",
+                    "mediaType": "text/html",
+                    "title": "Adaptive changes in the vestibular system of land snail to a 30-day spaceflight and readaptation on return to Earth"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-192_hjbw-ww9w",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "food deprivation",
                 "water deprivation",
@@ -869209,467 +869223,429 @@
                 "library construction",
                 "animal housing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/hjbw-ww9w",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-192_hjbw-ww9w",
-            "description": "The vestibular system receives a permanent influence from gravity and reflexively controls equilibrium. If we assume gravity has remained constant during the species   evolution will its sensory system adapt to abrupt loss of that force? We address this question in the land snail Helix lucorum exposed to 30 days of near weightlessness aboard the Bion-M1 satellite and studied geotactic behavior of postflight snails differential gene expressions in statocyst transcriptome and electrophysiological responses of mechanoreceptors to applied tilts. Each approach revealed plastic changes in the snail  s vestibular system assumed in response to spaceflight. Absence of light during the mission also affected statocyst physiology as revealed by comparison to dark-conditioned control groups. Readaptation to normal tilt responses occurred at ~20 h following return to Earth. Despite the permanence of gravity the snail responded in a compensatory manner to its loss and readapted once gravity was restored.",
-            "title": "Adaptive changes in the vestibular system of land snail to a 30-day spaceflight and readaptation on return to Earth",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-192",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Adaptive changes in the vestibular system of land snail to a 30-day spaceflight and readaptation on return to Earth"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC1-67PCHURYUMOV-M10-V3.0",
-            "bureauCode": [
-                "026:00"
-            ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
+            ],
+            "title": "Adaptive changes in the vestibular system of land snail to a 30-day spaceflight and readaptation on return to Earth"
+        },
+        {
+            "@type": "dcat:Dataset",
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
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc1-67pchuryumov-m10-v3.0_hjbx-ikzv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC1-67PCHURYUMOV-M10-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc1-67pchuryumov-m10-v3.0_hjbx-ikzv",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC1-MTP010 RDR V3.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC1-MTP010 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C%2FSW-MISCHA-3-RDR-ORIGINAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes the original Vega 2 MISCHA data delivery to PDS. The data were provided by Magda Delva of the MISCHA instrument team. The data are provided in ASCII format as well as the original IBM/PC binary format in which they were delivered to PDS. This data set was created for purposes of 'safing' these data. Significant concerns exist with regards to data quality. Instrument offsets (zero-levels) were highly unstable after 21 Feb 1986. In addition the instrument failed just prior to closest approach to comet Halley.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-sw-mischa-3-rdr-original-v1.0_hjc3-c3zf",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "solar wind",
                 "vega 1",
                 "halley",
                 "1p/halley 1 (1682 q1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA2-C%2FSW-MISCHA-3-RDR-ORIGINAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega2-c-sw-mischa-3-rdr-original-v1.0_hjc3-c3zf",
-            "description": "This data set includes the original Vega 2 MISCHA data delivery to PDS. The data were provided by Magda Delva of the MISCHA instrument team. The data are provided in ASCII format as well as the original IBM/PC binary format in which they were delivered to PDS. This data set was created for purposes of 'safing' these data. Significant concerns exist with regards to data quality. Instrument offsets (zero-levels) were highly unstable after 21 Feb 1986. In addition the instrument failed just prior to closest approach to comet Halley.",
-            "title": "VEGA2 ORIGINAL MISCHA DATA SUBMISSION",
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
+            "title": "VEGA2 ORIGINAL MISCHA DATA SUBMISSION"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3YXTPM48L5GY",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Airborne Cloud Radar (ACR) Reflectivity, Wakasa Bay, Japan, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/3YXTPM48L5GY.",
-            "issued": "2003-01-14",
-            "temporal": "2003-01-14T00:00:00Z/2003-02-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-02-03",
-            "keyword": [
-                "atmosphere",
-                "spectral/engineering",
-                "radar",
-                "earth science",
-                "clouds",
-                "atmospheric radiation"
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
-            "identifier": "C1386204153-NSIDCV0",
             "description": "This data set includes 94 GHz co- and cross-polarized radar reflectivity. The Airborne Cloud Radar (ACR) sensor was mounted to a NASA P-3 aircraft flown over the Sea of Japan, the Western Pacific Ocean, and the Japanese Islands.",
-            "title": "Airborne Cloud Radar (ACR) Reflectivity, Wakasa Bay, Japan, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3YXTPM48L5GY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3YXTPM48L5GY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/rainfall/wakasa_bay/ACR",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/rainfall/wakasa_bay/ACR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/rainfall/wakasa_bay/ACR",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/rainfall/wakasa_bay/ACR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3YXTPM48L5GY",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/3YXTPM48L5GY",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3YXTPM48L5GY",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/3YXTPM48L5GY",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204153-NSIDCV0",
+            "issued": "2003-01-14",
+            "keyword": [
+                "atmosphere",
+                "spectral/engineering",
+                "radar",
+                "earth science",
+                "clouds",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/3YXTPM48L5GY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-02-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "130.0 30.0 150.0 40.0",
+            "temporal": "2003-01-14T00:00:00Z/2003-02-03T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Cloud Radar (ACR) Reflectivity, Wakasa Bay, Japan, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-ESC1-MTP010-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the ESCORT 1 MTP010 phase, which occurred from 2014-11-22 to 2014-12-20",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-esc1-mtp010-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-ESC1-MTP010-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-esc1-mtp010-v1.0",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the ESCORT 1 MTP010 phase, which occurred from 2014-11-22 to 2014-12-20",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 2 ESCORT 1 MTP010 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P VIRTIS 2 ESCORT 1 MTP010 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/9PH5QU4CL9E8",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2TUNXCSP. Version 5.12.4. MERRA-2 tavgU_2d_csp_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,COSP Satellite Simulator V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/9PH5QU4CL9E8. https://disc.gsfc.nasa.gov/datacollection/M2TUNXCSP_5.12.4.html. Digital Science Data.",
-            "issued": "2007-06-14",
-            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "references": [
-                "https://doi.org/10.1175/JCLI-D-16-0758.1",
-                "https://doi.org/10.5194/gmd-8-1339-2015",
-                "https://doi.org/10.1175/JCLI-D-16-0609.1",
-                "https://doi.org/10.1175/JCLI-D-16-0613.1",
-                "https://doi.org/10.1175/JCLI-D-16-0570.1",
-                "https://doi.org/10.1175/JCLI-D-16-0720.1",
-                "https://doi.org/NASA/TM%E2%80%932015-104606/Vol.%2043",
-                "https://doi.org/10.1177/1094342005056120"
-            ],
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812871-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TUNXCSP (or  tavgU_2d_csp_Nx) is a time-averaged 2-dimensional monthly diurnal means data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of parameters from CFMIP Observations Simulator Package(COSP), such as ISCCP total cloud area fraction, MODIS cloud fraction water (ice) mean, MODIS cloud fraction low (mid,high) mean, modis cloud particle size water (ice) mean.  CFMIP is the abbreviation of Cloud Feedback Model Intercomparison Project.  This data collection is the monthly mean of data fields for each hour and time-stamped with the central time of an hour starting from 00:30 UTC, e.g.: 00:30, 01:30, \u2026 , 23:30 UTC.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TUNXCSP",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2TUNXCSP variable",
-            "title": "MERRA-2 tavgU_2d_csp_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,COSP Satellite Simulator 0.625 x 0.5 degree V5.12.4 (M2TUNXCSP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNXCSP_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9PH5QU4CL9E8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9PH5QU4CL9E8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNXCSP_5.12.4.png",
-                    "description": "M2TUNXCSP variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2TUNXCSP variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNXCSP_5.12.4.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=MERRA",
-                    "description": "How to read and plot the data.",
                     "@type": "dcat:Distribution",
+                    "description": "How to read and plot the data.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=MERRA",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TUNXCSP_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TUNXCSP_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNXCSP.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNXCSP.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TUNXCSP",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TUNXCSP",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2TUNXCSP.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2TUNXCSP.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2TUNXCSP.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2TUNXCSP.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2TUNXCSP.5.12.4_Aggregation.ncml",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation/catalog.html?dataset=merra2_diurnal_aggregation%2FM2TUNXCSP.5.12.4_Aggregation.ncml",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/docs/",
-                    "description": "The GMAO MERRA-2 documentation and FAQs",
                     "@type": "dcat:Distribution",
+                    "description": "The GMAO MERRA-2 documentation and FAQs",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/docs/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf",
-                    "description": "MERRA-2 File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "MERRA-2 File Specification Document",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNXCSP.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNXCSP.5.12.4/doc/MERRA2.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=MERRA-2+Data+Access+%E2%80%93+Quick+Guide",
-                    "description": "MERRA-2 Data Access \u2013 Quick Start Guide",
                     "@type": "dcat:Distribution",
+                    "description": "MERRA-2 Data Access \u2013 Quick Start Guide",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=MERRA-2+Data+Access+%E2%80%93+Quick+Guide",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Records+of+MERRA-2+Data+Reprocessing+and+Service+Changes",
-                    "description": "Records of MERRA-2 Data Reprocessing and Service Changes",
                     "@type": "dcat:Distribution",
+                    "description": "Records of MERRA-2 Data Reprocessing and Service Changes",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Records+of+MERRA-2+Data+Reprocessing+and+Service+Changes",
+                    "mediaType": "text/html",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/faqs?keywords=MERRA-2&page=1",
-                    "description": "FAQs about MERRA-2 data access",
                     "@type": "dcat:Distribution",
+                    "description": "FAQs about MERRA-2 data access",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/faqs?keywords=MERRA-2&page=1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "M2TUNXCSP variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNXCSP_5.12.4.png",
+            "identifier": "C1276812871-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/9PH5QU4CL9E8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-07-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JCLI-D-16-0758.1",
+                "https://doi.org/10.5194/gmd-8-1339-2015",
+                "https://doi.org/10.1175/JCLI-D-16-0609.1",
+                "https://doi.org/10.1175/JCLI-D-16-0613.1",
+                "https://doi.org/10.1175/JCLI-D-16-0570.1",
+                "https://doi.org/10.1175/JCLI-D-16-0720.1",
+                "https://doi.org/NASA/TM%E2%80%932015-104606/Vol.%2043",
+                "https://doi.org/10.1177/1094342005056120"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "M2TUNXCSP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavgU_2d_csp_Nx: 2d,diurnal,Time-averaged,Single-Level,Assimilation,COSP Satellite Simulator 0.625 x 0.5 degree V5.12.4 (M2TUNXCSP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-LECP-3-RDR-NEAR-ENC-400MSEC-V1.0",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This near encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 1 while the spacecraft was within the very close vicinity of Jupiter. This instrument measures the intensities of in-situ charged particles ( >15 keV electrons and >30 keV ions) with various levels of discrimination based on energy range and mass species.  The LECP data are globally calibrated to the extent possible. Particles include low energy electrons, protons, alpha particles, medium energy protons and ions, high energy and intensity protons, electrons, alpha particles, and Z >= nuclei.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-lecp-3-rdr-near-enc-400msec-v1.0_hjer-97w6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-LECP-3-RDR-NEAR-ENC-400MSEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-lecp-3-rdr-near-enc-400msec-v1.0_hjer-97w6",
-            "description": "This near encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 1 while the spacecraft was within the very close vicinity of Jupiter. This instrument measures the intensities of in-situ charged particles ( >15 keV electrons and >30 keV ions) with various levels of discrimination based on energy range and mass species.  The LECP data are globally calibrated to the extent possible. Particles include low energy electrons, protons, alpha particles, medium energy protons and ions, high energy and intensity protons, electrons, alpha particles, and Z >= nuclei.",
-            "title": "VG1 LECP 0.4 SEC HIGH RESOLUTION JUPITER NEAR ENCOUNTER DATA",
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
+            "title": "VG1 LECP 0.4 SEC HIGH RESOLUTION JUPITER NEAR ENCOUNTER DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2913021415-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2024-04-01. OCO2_L1aIn_Sample. Version 11.2. OCO-2 Level 1A collated, parsed, science or calibration data V11.2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_11.2.html. Digital Science Data.",
-            "issued": "2024-04-01",
-            "temporal": "2019-11-30T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-01",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "infrared wavelengths",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KRISTAN MORGAN",
                 "hasEmail": "mailto:kristan.l.morgan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2913021415-GES_DISC",
-            "description": "Version 11.2 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Sample Mode of operation.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L1aIn_Sample",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 1A collated, parsed, science or calibration data V11.2 (OCO2_L1aIn_Sample) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11.2 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Sample Mode of operation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -869678,561 +869654,587 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_11.2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_11.2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1aIn_Sample",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1aIn_Sample",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Sample.11.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Sample.11.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov2.jpl.nasa.gov/",
-                    "description": "OCO-2 Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 Project Home Page",
+                    "downloadURL": "https://ocov2.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Sample.11.2/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Sample.11.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L1aIn.V7.pdf",
-                    "description": "Level 1A Software Interfase Specification.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1A Software Interfase Specification.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L1aIn.V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf",
-                    "description": "README document.",
                     "@type": "dcat:Distribution",
+                    "description": "README document.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_V11_OCO3_V10_DUG.pdf",
-                    "description": "USER'S GUIDE",
                     "@type": "dcat:Distribution",
+                    "description": "USER'S GUIDE",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_V11_OCO3_V10_DUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?title=How+to+download+a+spatial+and+variable+subset+of+Level+1B+data+using+OPeNDAP",
-                    "description": "Subset recipe using OPeNDAP",
                     "@type": "dcat:Distribution",
+                    "description": "Subset recipe using OPeNDAP",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?title=How+to+download+a+spatial+and+variable+subset+of+Level+1B+data+using+OPeNDAP",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/nasa/RtRetrievalFramework",
-                    "description": "This software (NASA NTR-49044) retrieves a set of atmospheric/surface/instrument parameters from a simultaneous fit to spectra from multiple absorption bands. The software uses an iterative, non-linear retrieval technique (optimal estimation). After the retrieval process has converged, the software performs an error analysis. The products of the software include all quantities needed to understand the information content of the measurement, its uncertainty, and its dependence on interfering atmospheric properties.\n\nJet Propulsion Laboratory, California Institute of Technology.\nCopyright 2016 California Institute of Technology.\nU.S. Government sponsorship acknowledged.",
                     "@type": "dcat:Distribution",
+                    "description": "This software (NASA NTR-49044) retrieves a set of atmospheric/surface/instrument parameters from a simultaneous fit to spectra from multiple absorption bands. The software uses an iterative, non-linear retrieval technique (optimal estimation). After the retrieval process has converged, the software performs an error analysis. The products of the software include all quantities needed to understand the information content of the measurement, its uncertainty, and its dependence on interfering atmospheric properties.\n\nJet Propulsion Laboratory, California Institute of Technology.\nCopyright 2016 California Institute of Technology.\nU.S. Government sponsorship acknowledged.",
+                    "downloadURL": "https://github.com/nasa/RtRetrievalFramework",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov2.jpl.nasa.gov/science/publications/",
-                    "description": "Publications from the Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "Publications from the Science Team",
+                    "downloadURL": "https://ocov2.jpl.nasa.gov/science/publications/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO+Known+Data+Issues",
-                    "description": "OCO-2 Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 Data Gaps",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO+Known+Data+Issues",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
-                    "description": "OCO-2 Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
+            "identifier": "C2913021415-GES_DISC",
+            "issued": "2024-04-01",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "infrared wavelengths",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2913021415-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_L1aIn_Sample",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2024-04-22T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 1A collated, parsed, science or calibration data V11.2 (OCO2_L1aIn_Sample) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT2-MTP028-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase Extension 2 from 5th April 2016 to 3rd May 2016 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext2-mtp028-v1.0_hjgk-dyzk",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "alpha lyr",
                 "zeta cas",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-EXT2-MTP028-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-ext2-mtp028-v1.0_hjgk-dyzk",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase Extension 2 from 5th April 2016 to 3rd May 2016 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 2 MTP028 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 ROSETTA EXTENSION 2 MTP028 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203IMG.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2024-01-18. VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375 m. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/VJ203IMG.002. https://doi.org/10.5067/VIIRS/VJ203IMG.002.",
-            "issued": "2023-09-25",
-            "temporal": "2023-02-10T00:00:00Z/2024-06-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-05",
-            "keyword": [
-                "sensor characteristics",
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths"
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
-            "identifier": "C2839117635-LAADS",
-            "description": "The VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375 m, short-name VJ203IMG is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-derived NASA Visible-Infrared Imaging-Radiometer Suite (VIIRS) L1 terrain-corrected geolocation product and contains the derived line-of-sight (LOS) vectors for each of the 375-m image-resolution or I-bands.  The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform\u2019s ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry.  It produces geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel.  The VJ203IMG product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, and quality flag for every pixel location.  VJ203IMG provides a fundamental input to derive a number of VIIRS I-band higher-level products.\r\n\r\n\r\nThe J2 VIIRS geolocation underwent an on-orbit validation.  Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands.  The Day-Night band (DNB) geolocation error of about 2000 m was corrected.  Further, the geolocation biases in the scan profile were also corrected. For more information and documents, visit LAADS product page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/VJ203IMG",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375 m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375 m, short-name VJ203IMG is the Joint Polar-orbiting Satellite System-2 (JPSS-2/NOAA-21) platform-derived NASA Visible-Infrared Imaging-Radiometer Suite (VIIRS) L1 terrain-corrected geolocation product and contains the derived line-of-sight (LOS) vectors for each of the 375-m image-resolution or I-bands.  The geolocation algorithm uses a number of inputs that include an Earth ellipsoid, geoid, and a digital terrain model along with the SNPP platform\u2019s ephemeris and attitude data, and knowledge of the VIIRS sensor and satellite geometry.  It produces geodetic coordinates (latitude and longitude), and related parameters for each VIIRS L1 pixel.  The VJ203IMG product includes geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, sensor zenith and azimuth angles, land/water mask, and quality flag for every pixel location.  VJ203IMG provides a fundamental input to derive a number of VIIRS I-band higher-level products.\r\n\r\n\r\nThe J2 VIIRS geolocation underwent an on-orbit validation.  Geolocation errors of about 350 m in the along-scan direction and about 165 m in the along-track direction were corrected for the image-resolution bands and moderate-resolution bands.  The Day-Night band (DNB) geolocation error of about 2000 m was corrected.  Further, the geolocation biases in the scan profile were also corrected. For more information and documents, visit LAADS product page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/VJ203IMG",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203IMG.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ203IMG.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ203IMG.002",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ203IMG.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ203IMG--5200",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VJ203IMG--5200",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5200/VJ203IMG/",
-                    "description": "Direct access to VJ103IMG C2 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to VJ103IMG C2 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5200/VJ203IMG/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/hyrax/allData/5200/VJ203IMG/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/hyrax/allData/5200/VJ203IMG/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2839117635-LAADS",
+            "issued": "2023-09-25",
+            "keyword": [
+                "sensor characteristics",
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ203IMG.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-06-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-02-10T00:00:00Z/2024-06-10T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS2 Imagery Resolution Terrain Corrected Geolocation 6-Min L1 Swath 375 m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0943-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-05T04:58:45.000 to 2015-08-05T09:52:32.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0943-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0943-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0943-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-05T04:58:45.000 to 2015-08-05T09:52:32.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0943 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0943 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2346",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bloom, A.A., K.W. Bowman, M. Lee, A.J. Turner, R. Schroeder, J.R. Worden, R.J. Weidner, K.C. McDonald, and D.J. Jacob. 2024. CMS: Global 0.5-deg Wetland Methane Emissions and Uncertainty (WetCHARTs v1.3.3). ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2346",
-            "issued": "2024-09-06",
-            "temporal": "2001-01-01T00:00:00Z/2022-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-12",
-            "keyword": [
-                "atmosphere",
-                "ecosystems",
-                "earth science",
-                "atmospheric chemistry",
-                "biosphere",
-                "air quality"
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
-            "identifier": "C3236621594-ORNL_CLOUD",
             "description": "This dataset provides global monthly wetland methane (CH4) emissions estimates at 0.5 by 0.5-degree resolution for the period 2001-01-01 to 2022-08-31 that were derived from an ensemble of multiple terrestrial biosphere models, wetland extent scenarios, and CH4:C temperature dependencies that encompass the main sources of uncertainty in wetland CH4 emissions. There are 18 model configurations. WetCHARTs v1.3.3 is an updated product of WetCHARTs v1.3.1 dataset. The intended use of this product is as a process-informed wetland CH4 emission data set for atmospheric chemistry and transport modeling. Users can compare estimates by model configuration to explore variability and sensitivity with respect to ensemble members. The data are provided in netCDF format.",
-            "graphic-preview-description": "Estimated daily emissions of methane from wetlands (mg CH4 m-2 d-1) in North America for July 2010.  Estimates were produced using the WetCHARTs v1.3.3 model using ensemble member 1931, which includes a global scale factor of 124.5 Tg CH4 y-1, the CARDAMOM heterotrophic respiration model, a temperature-dependent CH4:C q10=3, and extent parameterization based on the Global Lakes and Wetlands Database. Source: WetCHARTs_v1_3_3_2010.nc",
-            "title": "CMS: Global 0.5-deg Wetland Methane Emissions and Uncertainty (WetCHARTs v1.3.3)",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/MonthlyWetland_CH4_WetCHARTsV2_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2346",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2346",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/MonthlyWetland_CH4_WetCHARTsV2/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/MonthlyWetland_CH4_WetCHARTsV2/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/MonthlyWetland_CH4_WetCHARTsV2_2346.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/MonthlyWetland_CH4_WetCHARTsV2_2346.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/MonthlyWetland_CH4_WetCHARTsV2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/MonthlyWetland_CH4_WetCHARTsV2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2346",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2346",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/MonthlyWetland_CH4_WetCHARTsV2_2346.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/MonthlyWetland_CH4_WetCHARTsV2_2346.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/MonthlyWetland_CH4_WetCHARTsV2/comp/MonthlyWetland_CH4_WetCHARTsV2.pdf",
-                    "description": "CMS: Global 0.5-deg Wetland Methane Emissions and Uncertainty (WetCHARTs v1.3.3): MonthlyWetland_CH4_WetCHARTsV2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "CMS: Global 0.5-deg Wetland Methane Emissions and Uncertainty (WetCHARTs v1.3.3): MonthlyWetland_CH4_WetCHARTsV2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/MonthlyWetland_CH4_WetCHARTsV2/comp/MonthlyWetland_CH4_WetCHARTsV2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/MonthlyWetland_CH4_WetCHARTsV2_Fig1.jpg",
-                    "description": "Estimated daily emissions of methane from wetlands (mg CH4 m-2 d-1) in North America for July 2010.  Estimates were produced using the WetCHARTs v1.3.3 model using ensemble member 1931, which includes a global scale factor of 124.5 Tg CH4 y-1, the CARDAMOM heterotrophic respiration model, a temperature-dependent CH4:C q10=3, and extent parameterization based on the Global Lakes and Wetlands Database. Source: WetCHARTs_v1_3_3_2010.nc",
                     "@type": "dcat:Distribution",
+                    "description": "Estimated daily emissions of methane from wetlands (mg CH4 m-2 d-1) in North America for July 2010.  Estimates were produced using the WetCHARTs v1.3.3 model using ensemble member 1931, which includes a global scale factor of 124.5 Tg CH4 y-1, the CARDAMOM heterotrophic respiration model, a temperature-dependent CH4:C q10=3, and extent parameterization based on the Global Lakes and Wetlands Database. Source: WetCHARTs_v1_3_3_2010.nc",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/MonthlyWetland_CH4_WetCHARTsV2_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Estimated daily emissions of methane from wetlands (mg CH4 m-2 d-1) in North America for July 2010.  Estimates were produced using the WetCHARTs v1.3.3 model using ensemble member 1931, which includes a global scale factor of 124.5 Tg CH4 y-1, the CARDAMOM heterotrophic respiration model, a temperature-dependent CH4:C q10=3, and extent parameterization based on the Global Lakes and Wetlands Database. Source: WetCHARTs_v1_3_3_2010.nc",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/MonthlyWetland_CH4_WetCHARTsV2_Fig1.jpg",
+            "identifier": "C3236621594-ORNL_CLOUD",
+            "issued": "2024-09-06",
+            "keyword": [
+                "atmosphere",
+                "ecosystems",
+                "earth science",
+                "atmospheric chemistry",
+                "biosphere",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2346",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2001-01-01T00:00:00Z/2022-08-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS: Global 0.5-deg Wetland Methane Emissions and Uncertainty (WetCHARTs v1.3.3)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/206",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "San Jose, J., and R.A. Montes. 2014. NPP Grassland: Calabozo, Venezuela, 1969-1987, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/206",
-            "issued": "2023-08-17",
-            "temporal": "1968-01-01T00:00:00Z/1987-04-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "ecological dynamics",
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
-            "identifier": "C2752562626-ORNL_CLOUD",
             "description": "This data set contains four ASCII text files for a 260-hectare humid Trachypogon savanna at the Estacion Biologica de Los Llanos, Calabozo, Venezuela (8.93 N, -67.42 W, Elevation 98 m). Two data files contain monthly estimates of above-ground biomass for the period January 1969 to October 1969, one file for each treatment (burned and unburned plots). These files also provide one estimate of below-ground biomass. Another NPP data file contains monthly estimates of above- and below-ground biomass, LAI, and nitrogen content of living and dead leaves and stems and below-ground biomass for an unburned area of the Calabozo savanna for March 1986 to April 1987. The fourth data file contains precipitation and maximum/minimum temperature data from a nearby weather station at Estacion Biologica de Los Llanos (8.88 N, -67.32 W, Elevation 86 m) for the period 1968-1986. Harvest methods were used to estimate above- and below-ground biomass. Total NPP (above- plus below-ground productivity) was estimated at 682 g/m2/yr for unburned and 755 g/m2/yr for burned grassland plots in 1969. Later TNPP estimates (1986/87) for the unburned grassland ranged from 823 to 1,310 g/m2/yr.Revision Notes: Only the documentation for this data set has been modified. The data files have been checked for accuracy and are identical to those originally published in 1998.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Calabozo, Venezuela, 1969-1987, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F206",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F206",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_CLB/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_CLB/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_CLB.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_CLB.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/206",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/206",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_CLB/comp/NPP_CLB.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_CLB/comp/NPP_CLB.pdf",
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
+            "identifier": "C2752562626-ORNL_CLOUD",
+            "issued": "2023-08-17",
+            "keyword": [
+                "ecological dynamics",
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/206",
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
             "spatial": "8.93 -67.42",
+            "temporal": "1968-01-01T00:00:00Z/1987-04-15T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Calabozo, Venezuela, 1969-1987, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/840",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Moody, E.G., M.D. King, S.E. Platnick, C. Schaaf, and F. Gao. 2006. SAFARI 2000 MODIS L3 Albedo and Land Cover Data, Southern Africa, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/840",
-            "issued": "2023-10-18",
-            "temporal": "2000-07-11T00:00:00Z/2000-10-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
-                "ngda",
-                "national geospatial data asset",
-                "land use/land cover",
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
-            "identifier": "C2789103516-ORNL_CLOUD",
             "description": "The Filled Land Surface Albedo Product for Southern Africa, which is generated from MOD43B3 Product (the official Terra/MODIS-derived Land Surface Albedo - http://geography.bu.edu/brdf/userguide/albedo.html ), is a subset of the global data set of spatially complete albedo maps computed for both white-sky and black-sky at 10 wavelengths (0.47mm, 0.55mm, 0.67mm, 0.86mm, 1.24mm, 1.64mm, 2.1mm, and broadband 0.3-0.7mm, 0.3-5.0mm, and 0.7-5.0mm). An exception is that no 2.1mm data for black-sky is being archived at this time. The data spatial extent is from approximately 5 degrees N to -30 degrees S latitude and 5 minutes E to 60 degrees E longitude and covers 7 sixteen day periods starting on July 11 through October 15, 2000.Map Products, containing spatially complete land surface albedo data, are generated at 1-minute resolution on an equal-angle grid. The maps are stored in separate HDF files for each wavelength, each 16-day period and each albedo type (white- and black-sky). Data belonging to black sky and white sky albedo have been zipped separately. This format allows the user to have flexibility to download and store only the data absolutely needed.The One-Minute Land Ecosystem Classification Product is a global (static map) data set of the International Geosphere-Biosphere Programme (IGBP) classification scheme stored on an equal-angle rectangular grid at 1-minute resolution. The dataset is generated from the official MODIS land ecosystem classification dataset, MOD12Q1 for year 2000, day 289 data (October 15, 2000). This dataset is used in generating the spatially complete albedo maps, but is also a stand-alone product designed for use by the user community. The Land Ecosystem Classification Map File product file is stored in Hierarchical Data Format (HDF).",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 MODIS L3 Albedo and Land Cover Data, Southern Africa, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F840",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F840",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/modis_l3_albedo/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/modis_l3_albedo/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/S2K_MODIS_L3_albedo_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/S2K_MODIS_L3_albedo_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/840",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/840",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/modis_l3_albedo/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/modis_l3_albedo/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/modis_l3_albedo/comp/S2K_MODIS_L3_albedo_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/modis_l3_albedo/comp/S2K_MODIS_L3_albedo_guide.pdf",
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
+            "identifier": "C2789103516-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "ngda",
+                "national geospatial data asset",
+                "land use/land cover",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/840",
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
             "spatial": "5.0 -30.0 60.0 5.0",
+            "temporal": "2000-07-11T00:00:00Z/2000-10-15T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 MODIS L3 Albedo and Land Cover Data, Southern Africa, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH%2FSW-EPPS-3-FIPS-DDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract\n========\nThis data set consists of the MESSENGER Energetic Particle and\nPlasma Spectrometer (EPPS) calibrated observations, also known\nas DDRs. The system encompasses 2 instrument subsystems - the\nEnergetic Particle Spectrometer (EPS) and the Fast Imaging Plasma\nSpectrometer (FIPS). This data set contains FIPS instrument data.\nFIPS covers the energy/charge range of < 46 eV/q to 13 keV/q.\nThere are five FIPS DDR data products.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-sw-epps-3-fips-ddr-v1.0_hk52-nmgk",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "venus",
                 "calibration",
@@ -870240,61 +870242,37 @@
                 "mercury",
                 "messenger"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH%2FSW-EPPS-3-FIPS-DDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-sw-epps-3-fips-ddr-v1.0_hk52-nmgk",
-            "description": "Abstract\n========\nThis data set consists of the MESSENGER Energetic Particle and\nPlasma Spectrometer (EPPS) calibrated observations, also known\nas DDRs. The system encompasses 2 instrument subsystems - the\nEnergetic Particle Spectrometer (EPS) and the Fast Imaging Plasma\nSpectrometer (FIPS). This data set contains FIPS instrument data.\nFIPS covers the energy/charge range of < 46 eV/q to 13 keV/q.\nThere are five FIPS DDR data products.",
-            "title": "MESSENGER E/V/H/SW EPPS CALIBRATED FIPS\n                                      V1.0",
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
+            "title": "MESSENGER E/V/H/SW EPPS CALIBRATED FIPS\n                                      V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/turntable",
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
-                "dish",
-                "satellite",
-                "3d model",
-                "turntable"
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
-            "identifier": "NASA-336",
             "description": "Dish Turntable. Polygons: 552 Vertices: 630",
-            "title": "NASA 3D Models: Dish Turntable",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -870302,897 +870280,898 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-336",
+            "issued": "2018-06-25",
+            "keyword": [
+                "dish",
+                "satellite",
+                "3d model",
+                "turntable"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/turntable",
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
+            "title": "NASA 3D Models: Dish Turntable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/QOFZLQYMGA72",
             "citation": "Kevin W. Bowman. 2021-07-09. TRPSDL2CH4CRS1FS. Version 1. TROPESS CrIS-JPSS1 L2 Methane for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/QOFZLQYMGA72. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2CH4CRS1FS_1.html. Digital Science Data.",
-            "issued": "2021-05-18",
-            "temporal": "2021-04-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-18",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.5194/amt-14-335-2021"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2088007541-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-JPSS1 L2 Methane for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of methane (CH4), formal uncertainties, and diagnostic information measured by the CrIS instrument on the JPSS-1 (NOAA-20) satellite. The forward stream standard product is global for the time period from 2021-04-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 26 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2CH4CRS1FS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-JPSS1 CH4 (Forward Stream, Standard Product) at 383 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-JPSS1 L2 Methane for Forward Stream, Standard Product V1 (TRPSDL2CH4CRS1FS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2CH4CRS1FS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQOFZLQYMGA72",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQOFZLQYMGA72",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2CH4CRS1FS_Sample.png",
-                    "description": "TROPESS CrIS-JPSS1 CH4 (Forward Stream, Standard Product) at 383 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-JPSS1 CH4 (Forward Stream, Standard Product) at 383 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2CH4CRS1FS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2CH4CRS1FS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2CH4CRS1FS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2CH4CRS1FS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2CH4CRS1FS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2CH4CRS1FS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2CH4CRS1FS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2CH4CRS1FS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2CH4CRS1FS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2CH4CRS1FS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2CH4CRS1FS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CH4_L2_Product_Quick_Start_User_Guide_20210402.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CH4_L2_Product_Quick_Start_User_Guide_20210402.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-JPSS1 CH4 (Forward Stream, Standard Product) at 383 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2CH4CRS1FS_Sample.png",
+            "identifier": "C2088007541-GES_DISC",
+            "issued": "2021-05-18",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/QOFZLQYMGA72",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.5194/amt-14-335-2021"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2CH4CRS1FS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-04-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-JPSS1 L2 Methane for Forward Stream, Standard Product V1 (TRPSDL2CH4CRS1FS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3303-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-27T08:58:48.000 to 2012-07-27T12:04:30.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3303-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3303-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3303-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-27T08:58:48.000 to 2012-07-27T12:04:30.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3303 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3303 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MPFL-M-ASIMET-4-DDR-EDL-V1.0",
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
-                "mars pathfinder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Mars Pathfinder bounced down and rolled to a stop on the surface of Mars on July 4, 1997. It landed in an ancient floodplain in the Ares Vallis region of Chryse Planitia at 19.1 degrees North Areocentric latitude, and 326.48 degrees East longitude.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mpfl-m-asimet-4-ddr-edl-v1.0_hkbd-a76b",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars pathfinder"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MPFL-M-ASIMET-4-DDR-EDL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mpfl-m-asimet-4-ddr-edl-v1.0_hkbd-a76b",
-            "description": "Mars Pathfinder bounced down and rolled to a stop on the surface of Mars on July 4, 1997. It landed in an ancient floodplain in the Ares Vallis region of Chryse Planitia at 19.1 degrees North Areocentric latitude, and 326.48 degrees East longitude.",
-            "title": "MPFL MARS ATM STRUCT INST AND MET PKG DERIVED EDL V1.0",
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
+            "title": "MPFL MARS ATM STRUCT INST AND MET PKG DERIVED EDL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0037-5-BENNUSHAPE-V1.0",
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
-                "101955 bennu"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "We present the three-dimensional shape of near-Earth asteroid (101955) Bennu (provisional designation 1999 RQ36) based on radar images and optical lightcurves (Nolan et al., 2013). Bennu was observed both in 1999 at its discovery apparition, and in 2005 using the 12.6-cm radar at the Arecibo Observatory and the 3.5-cm radar at the Goldstone tracking station. Data obtained in both apparitions were used to construct a shape model of this object. Observations were also obtained at many other wavelengths to characterize this object, some of which were used to further constrain the shape modeling (Clark et al., 2011; Hergenrother et al., 2013; Krugly et al., 1999).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0037-5-bennushape-v1.0_hkcr-ywr2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "101955 bennu"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0037-5-BENNUSHAPE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0037-5-bennushape-v1.0_hkcr-ywr2",
-            "description": "We present the three-dimensional shape of near-Earth asteroid (101955) Bennu (provisional designation 1999 RQ36) based on radar images and optical lightcurves (Nolan et al., 2013). Bennu was observed both in 1999 at its discovery apparition, and in 2005 using the 12.6-cm radar at the Arecibo Observatory and the 3.5-cm radar at the Goldstone tracking station. Data obtained in both apparitions were used to construct a shape model of this object. Observations were also obtained at many other wavelengths to characterize this object, some of which were used to further constrain the shape modeling (Clark et al., 2011; Hergenrother et al., 2013; Krugly et al., 1999).",
-            "title": "ASTEROID (101955) BENNU SHAPE MODEL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID (101955) BENNU SHAPE MODEL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHVRS-3UO28",
             "citation": "NOAA/NESDIS/STAR. 2021-11-25. GHRSST Level 3U SST v2.80 dataset from VIIRS on S-NPP Satellite. Version 2.80. GHRSST Level 3U NOAA/NESDIS/STAR SST from VIIRS on S-NPP Satellite. Suitland, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHVRS-3UO28. https://www.star.nesdis.noaa.gov/star/index.php.",
-            "issued": "2019-03-07",
-            "temporal": "2012-02-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-07",
-            "references": [
-                "https://doi.org/10.1002/2013JD020637",
-                "https://doi.org/10.1175/2010JTECHA1413.1"
-            ],
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
-            "identifier": "C2147485059-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The Joint Polar Satellite System (JPSS), starting with S-NPP launched on 28 October 2011, is the new generation of the US Polar Operational Environmental Satellites (POES). The ACSPO SNPP/VIIRS L3U (Level 3 Uncollated) product is a gridded version of the ACSPO NPP/VIIRS L2P product available here https://podaac.jpl.nasa.gov/dataset/VIIRS_NPP-STAR-L2P-v2.80 . The L3U output files are 10-minute granules in netCDF4 format, compliant with the Group for High Resolution Sea Surface Temperature (GHRSST) Data Specification version 2 (GDS2). There are 144 granules per 24hr interval, with a total data volume of 0.5GB/day. Fill values are reported at all invalid pixels, including pixels with >5 km inland. For each valid water pixel (defined as ocean, sea, lake or river, and up to 5 km inland), the following layers are reported: SSTs, a subset of l2p_flags (including day/night, land, ice, twilight, and glint flags), wind speed, and ACSPO SST minus reference (Canadian Met Centre 0.1deg L4 SST; available at https://www.doi.org/10.5067/GHCMC-4FM03). Only L2P SSTs with QL=5 were gridded, so all valid SSTs are recommended for the users. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (SSES bias and standard deviation) are reported in each pixel with valid SST. The ACSPO VIIRS L3U product is monitored and validated against iQuam in situ data in SQUAM. The v2.80 is an updated version from the v2.61 with several L2P algorithm improvements including two added thermal front layers, mitigated warm biases in the high latitudes, and improved clear-sky mask.",
-            "release-place": "Suitland, MD, USA",
-            "series-name": "GHRSST Level 3U SST v2.80 dataset from VIIRS on S-NPP Satellite",
             "creator": "NOAA/NESDIS/STAR",
-            "title": "GHRSST Level 3U NOAA STAR SST v2.80 from VIIRS on S-NPP Satellite",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-STAR-L3U-v2.80.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Joint Polar Satellite System (JPSS), starting with S-NPP launched on 28 October 2011, is the new generation of the US Polar Operational Environmental Satellites (POES). The ACSPO SNPP/VIIRS L3U (Level 3 Uncollated) product is a gridded version of the ACSPO NPP/VIIRS L2P product available here https://podaac.jpl.nasa.gov/dataset/VIIRS_NPP-STAR-L2P-v2.80 . The L3U output files are 10-minute granules in netCDF4 format, compliant with the Group for High Resolution Sea Surface Temperature (GHRSST) Data Specification version 2 (GDS2). There are 144 granules per 24hr interval, with a total data volume of 0.5GB/day. Fill values are reported at all invalid pixels, including pixels with >5 km inland. For each valid water pixel (defined as ocean, sea, lake or river, and up to 5 km inland), the following layers are reported: SSTs, a subset of l2p_flags (including day/night, land, ice, twilight, and glint flags), wind speed, and ACSPO SST minus reference (Canadian Met Centre 0.1deg L4 SST; available at https://www.doi.org/10.5067/GHCMC-4FM03). Only L2P SSTs with QL=5 were gridded, so all valid SSTs are recommended for the users. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (SSES bias and standard deviation) are reported in each pixel with valid SST. The ACSPO VIIRS L3U product is monitored and validated against iQuam in situ data in SQUAM. The v2.80 is an updated version from the v2.61 with several L2P algorithm improvements including two added thermal front layers, mitigated warm biases in the high latitudes, and improved clear-sky mask.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHVRS-3UO28",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHVRS-3UO28",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-STAR-L3U-v2.80.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-STAR-L3U-v2.80.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=7&t=298",
-                    "description": "Sea Surface Temperature measurement description.",
                     "@type": "dcat:Distribution",
+                    "description": "Sea Surface Temperature measurement description.",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=7&t=298",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
-                    "description": "Documentation on the GDS version 2 format specification",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation on the GDS version 2 format specification",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
-                    "description": "In situ SST Quality Monitor (iQUAM)",
                     "@type": "dcat:Distribution",
+                    "description": "In situ SST Quality Monitor (iQUAM)",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "GHRSST Global Data Assembly Center",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Global Data Assembly Center",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/micros/",
-                    "description": "Monitoring of IR Clear-sky Radiances over Oceans for SST",
                     "@type": "dcat:Distribution",
+                    "description": "Monitoring of IR Clear-sky Radiances over Oceans for SST",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/micros/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
-                    "description": "SST Quality Monitor (SQUAM)",
                     "@type": "dcat:Distribution",
+                    "description": "SST Quality Monitor (SQUAM)",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2147485059-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2147485059-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2147485059-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2147485059-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ghrsst.org/",
-                    "description": "GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project",
+                    "downloadURL": "https://www.ghrsst.org/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_NPP-STAR-L3U-v2.80.jpg",
+            "identifier": "C2147485059-POCLOUD",
+            "issued": "2019-03-07",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHVRS-3UO28",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1002/2013JD020637",
+                "https://doi.org/10.1175/2010JTECHA1413.1"
+            ],
+            "release-place": "Suitland, MD, USA",
+            "series-name": "GHRSST Level 3U SST v2.80 dataset from VIIRS on S-NPP Satellite",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-02-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 3U NOAA STAR SST v2.80 from VIIRS on S-NPP Satellite"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/708",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ward, D. 2004. SAFARI 2000 Atmospheric Aerosol Measurements, Hand-held Hazemeters, Zambia. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/708",
-            "issued": "2023-10-18",
-            "temporal": "2000-06-01T00:00:00Z/2000-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
-                "atmospheric water vapor",
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
-            "identifier": "C2788378273-ORNL_CLOUD",
             "description": "In conjunction with the AERONET (AErosol RObotic NETwork) participation in SAFARI 2000, the USDA Forest Service deployed handheld hazemeters in western Zambia from mid-June to late September 2000. Thirty-eight hazemeters were deployed within a 900 km x 900 km region in western Zambia to verify and study the aerosol properties in MODIS data. The handheld measurements were compared with satellite measurements. The hazemeter data were used to examine the effects of inhomogeneous atmosphere on MODIS aerosol product validation and to investigate the dependency of MODIS aerosol measurements on look angle and ground vegetation.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Atmospheric Aerosol Measurements, Hand-held Hazemeters, Zambia",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F708",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F708",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/handheld_haze/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/handheld_haze/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_hazemeter_zamb.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_hazemeter_zamb.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/708",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/708",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/handheld_haze/comp/hazemeter_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/handheld_haze/comp/hazemeter_doc.pdf",
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
+            "identifier": "C2788378273-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/708",
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
             "spatial": "21.55 -18.7 34.45 -7.69",
+            "temporal": "2000-06-01T00:00:00Z/2000-09-30T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Atmospheric Aerosol Measurements, Hand-held Hazemeters, Zambia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/1SF2KW5EIGOB",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Boise River Basin SnowMicroPen (SMP) Raw Penetration Force Profiles V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/1SF2KW5EIGOB.",
-            "issued": "2019-12-18",
-            "temporal": "2019-12-18T00:00:00Z/2020-01-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-24",
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
-            "identifier": "C2759079563-NSIDC_ECS",
             "description": "This data set contains raw penetration force profiles from the SnowEx 2020 Time Series campaign in the Boise River Basin in Idaho. Measurements were taken using the SnowMicroPen (SMP), a digital snow penetrometer, from three snow pits. The data files contain force measurements of the snowpack from the top of the snow surface to the ground. Measurements took place approximately weekly between 18 December 2019 and 24 January 2020.",
-            "title": "SnowEx20 Boise River Basin SnowMicroPen (SMP) Raw Penetration Force Profiles V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1SF2KW5EIGOB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1SF2KW5EIGOB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BR_BSU_SMP.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BR_BSU_SMP.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_BR_BSU_SMP+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_BR_BSU_SMP+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BR_BSU_SMP/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BR_BSU_SMP/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BR_BSU_SMP.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BR_BSU_SMP.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_BR_BSU_SMP+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_BR_BSU_SMP+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BR_BSU_SMP/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BR_BSU_SMP/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BR_BSU_SMP.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BR_BSU_SMP.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_BR_BSU_SMP+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX20_BR_BSU_SMP+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BR_BSU_SMP/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BR_BSU_SMP/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1SF2KW5EIGOB",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/1SF2KW5EIGOB",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1SF2KW5EIGOB",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/1SF2KW5EIGOB",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2759079563-NSIDC_ECS",
+            "issued": "2019-12-18",
+            "keyword": [
+                "snow/ice",
+                "terrestrial hydrosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/1SF2KW5EIGOB",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-116.0909 43.75724 -115.23445 44.30331",
+            "temporal": "2019-12-18T00:00:00Z/2020-01-24T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Boise River Basin SnowMicroPen (SMP) Raw Penetration Force Profiles V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A15A-L-SWS-4-SOLAR-WIND-1HR-AVG-V1.0",
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
-                "apollo 15",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains tables of time ordered, hourly averaged plasma parameters, mainly of the solar wind, as observed on the Moon at the Apollo 15 ALSEP site by the Apollo 15 Solar Wind Spectrometer from 31 July 1971 through 30 June 1972.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a15a-l-sws-4-solar-wind-1hr-avg-v1.0_hkkk-cpmy",
+            "issued": "2018-06-26",
+            "keyword": [
+                "apollo 15",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A15A-L-SWS-4-SOLAR-WIND-1HR-AVG-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a15a-l-sws-4-solar-wind-1hr-avg-v1.0_hkkk-cpmy",
-            "description": "This data set contains tables of time ordered, hourly averaged plasma parameters, mainly of the solar wind, as observed on the Moon at the Apollo 15 ALSEP site by the Apollo 15 Solar Wind Spectrometer from 31 July 1971 through 30 June 1972.",
-            "title": "APOLLO 15 ALSEP/SWS SOLAR WIND 1-HR AVG TABLES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "APOLLO 15 ALSEP/SWS SOLAR WIND 1-HR AVG TABLES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1889",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ray, E.A. 2021. ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1889",
-            "issued": "2022-01-26",
-            "temporal": "2016-07-29T00:00:00Z/2018-05-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric winds",
-                "atmosphere",
-                "clouds",
-                "atmospheric pressure",
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
-            "identifier": "C2704882261-ORNL_CLOUD",
             "description": "This dataset contains back trajectories, boundary layer influences, and convective influences of air parcels along NASA DC-8 aircraft's flight tracks during the four ATom campaigns that occurred from 2016 to 2018. Back trajectories were interpolated using National Centers for Environmental Prediction (NCEP) Global Forecast System (GFS) and Modern-Era Retrospective analysis for Research and Applications, Version 2 (MERRA2) meteorology. Back trajectory analysis determines the origin of air masses by modeling the path of an air parcel backward in time. It can be used to better understand the sources of atmospheric compounds. Boundary layer Influences were determined based on 30 Day Back Trajectories. The atmospheric boundary layer is the lowest part of the troposphere that is directly influenced by earth's surface. The boundary layer influences wind patterns and thus the dispersal of pollutants and other atmospheric compounds of interest. Convective influences were based on 10 Day Back Trajectories and NASA Langley cloud products. Convective influences model the effects of convection on the movement of water vapor through the atmosphere, which influences cloud behavior.",
-            "graphic-preview-description": "Fire influences for air parcels on the ATom-2 research flight that occurred on 2017-02-15.",
-            "title": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_FlightTrack_Influences_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1889",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1889",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_FlightTrack_Influences/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_FlightTrack_Influences/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_FlightTrack_Influences.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_FlightTrack_Influences.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1889",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1889",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_FlightTrack_Influences/comp/ATom_FlightTrack_Influences.pdf",
-                    "description": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018: ATom_FlightTrack_Influences.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018: ATom_FlightTrack_Influences.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_FlightTrack_Influences/comp/ATom_FlightTrack_Influences.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_FlightTrack_Influences/comp/BackTraj_data_dictionary.csv",
-                    "description": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018: BackTraj_data_dictionary.csv",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018: BackTraj_data_dictionary.csv",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_FlightTrack_Influences/comp/BackTraj_data_dictionary.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_FlightTrack_Influences/comp/BdyInfluence_data_dictionary.csv",
-                    "description": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018: BdyInfluence_data_dictionary.csv",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018: BdyInfluence_data_dictionary.csv",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_FlightTrack_Influences/comp/BdyInfluence_data_dictionary.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_FlightTrack_Influences/comp/ConvectInfluence_data_dictionary.csv",
-                    "description": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018: ConvectInfluence_data_dictionary.csv",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018: ConvectInfluence_data_dictionary.csv",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_FlightTrack_Influences/comp/ConvectInfluence_data_dictionary.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_FlightTrack_Influences_Fig1.jpg",
-                    "description": "Fire influences for air parcels on the ATom-2 research flight that occurred on 2017-02-15.",
                     "@type": "dcat:Distribution",
+                    "description": "Fire influences for air parcels on the ATom-2 research flight that occurred on 2017-02-15.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_FlightTrack_Influences_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/campaign/",
-                    "description": "ATom campaign page",
                     "@type": "dcat:Distribution",
+                    "description": "ATom campaign page",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/campaign/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Fire influences for air parcels on the ATom-2 research flight that occurred on 2017-02-15.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_FlightTrack_Influences_Fig1.jpg",
+            "identifier": "C2704882261-ORNL_CLOUD",
+            "issued": "2022-01-26",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "clouds",
+                "atmospheric pressure",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1889",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-07-29T00:00:00Z/2018-05-21T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: Back Trajectories and Influences of Air Parcels Along Flight Track, 2016-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-FL-2-RAW-V1.0",
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
-                "lunar crater observation and sensing satellite",
-                "sun"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Raw, uncalibrated flash mode spectra from the Near Infrared Spectrometer 2 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-fl-2-raw-v1.0_hkmz-eyfq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "lunar crater observation and sensing satellite",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-FL-2-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-fl-2-raw-v1.0_hkmz-eyfq",
-            "description": "Raw, uncalibrated flash mode spectra from the Near Infrared Spectrometer 2 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER FLASH 2 RAW V1.0",
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
+            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER FLASH 2 RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-C-ITS-2-NAV-9P-ENCOUNTER-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw comet 9P/Tempel 1 and calibration images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the impactor spacecraft as well as for scientific investigations. These data were collected from 6 May to 4 July 2005. In this version 1.1 of the data set, the values for the INTEGRATION_DURATION keyword in the PDS data labels were corrected. This revised data set supersedes version 1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-c-its-2-nav-9p-encounter-v1.1_hkqm-bmeu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "9p/tempel 1 (1867 g1)",
                 "deep impact"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-C-ITS-2-NAV-9P-ENCOUNTER-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-c-its-2-nav-9p-encounter-v1.1_hkqm-bmeu",
-            "description": "This data set contains raw comet 9P/Tempel 1 and calibration images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the impactor spacecraft as well as for scientific investigations. These data were collected from 6 May to 4 July 2005. In this version 1.1 of the data set, the values for the INTEGRATION_DURATION keyword in the PDS data labels were corrected. This revised data set supersedes version 1.0.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - RAW ITS NAV IMAGES V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - RAW ITS NAV IMAGES V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1418",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Moghaddam, M., A. Tabatabaeenejad, R.H. Chen, S.S. Saatchi, S. Jaruwatanadilok, M. Burgin, X. Duan, and M.L. Truong-Loi. 2016. AirMOSS: L2/3 Volumetric Soil Moisture Profiles Derived From Radar, 2012-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1418",
-            "issued": "2018-03-06",
-            "temporal": "2012-09-18T00:00:00Z/2015-09-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "land surface",
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
-            "identifier": "C2274733329-ORNL_CLOUD",
             "description": "This dataset provides level 2/3 root zone soil moisture (RZSM) estimates at multiple depths at 90-m spatial resolution from the Airborne Microwave Observatory of Subcanopy and Subsurface (AirMOSS) radar instrument collected over ten sites across North America. AirMOSS produces estimates of RZSM with data from a P-band synthetic aperture radar (SAR) flown on a NASA Gulfstream-III aircraft. The resulting soil moisture estimates capture the effects of gradients of soil, topography, and vegetation heterogeneity over an area of approximately 100km x 25km at each of the study sites. AirMOSS flight campaigns took place at least biannually from 2012 to 2015 at each site.",
-            "graphic-preview-description": "Browse Image",
-            "title": "AirMOSS: L2/3 Volumetric Soil Moisture Profiles Derived From Radar, 2012-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1418_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1418",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1418",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L2_3_RZ_Soil_Moisture/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L2_3_RZ_Soil_Moisture/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L2_3_RZ_Soil_Moisture.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L2_3_RZ_Soil_Moisture.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1418",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1418",
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
@@ -871208,903 +871187,904 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1418_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1418_1_fit.png",
+                    "mediaType": "image/png",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1418/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1418/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1418_1_fit.png",
+            "identifier": "C2274733329-ORNL_CLOUD",
+            "issued": "2018-03-06",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1418",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-123.28 9.88 -68.32 54.13",
+            "temporal": "2012-09-18T00:00:00Z/2015-09-29T23:59:59Z",
             "theme": [
                 "AirMOSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMOSS: L2/3 Volumetric Soil Moisture Profiles Derived From Radar, 2012-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-3-KEMCRUISE1-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the                      New Horizons Alice Ultraviolet Imaging Spectrograph instrument           during the CRUISE TO FIRST KBO ENCOUNTER mission phase.                  This is VERSION 2.0 of this data set.                                    This data set contains data acquired by the spacecraft between           01/11/2017 and 08/13/2018. This is the complete dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-3-kemcruise1-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "sky",
                 "new horizons kuiper belt extended mission",
                 "rho leo"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-ALICE-3-KEMCRUISE1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-alice-3-kemcruise1-v2.0",
-            "description": "This data set contains Calibrated data taken by the                      New Horizons Alice Ultraviolet Imaging Spectrograph instrument           during the CRUISE TO FIRST KBO ENCOUNTER mission phase.                  This is VERSION 2.0 of this data set.                                    This data set contains data acquired by the spacecraft between           01/11/2017 and 08/13/2018. This is the complete dataset.",
-            "title": "NEW HORIZONS                            \n      ALICE KEMCRUISE1                                                        \n      CALIBRATED V2.0",
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
+            "title": "NEW HORIZONS                            \n      ALICE KEMCRUISE1                                                        \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/882/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
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
-            "identifier": "DASHLINK_882",
             "description": "As fault diagnosis and prognosis systems in aerospace applications become more capable, the ability to utilize information supplied by them becomes increasingly important. While certain types of vehicle health data can be effectively processed and acted upon by crew or support personnel, others, due to their complexity or time constraints, require either automated or semi-automated reasoning. Prognostics-enabled Decision Making (PDM) is an emerging research area that aims to integrate prognostic health information and knowledge about the future operating conditions into the process of selecting subsequent actions for the system. The newly developed PDM algorithms require suitable software and hardware platforms for testing under realistic fault scenarios. The paper describes the development of such a platform, based on the K11 planetary rover prototype. A variety of injectable fault modes are being investigated for electrical, mechanical, and power subsystems of the testbed, along with methods for data collection and processing. In addition to the hardware platform, a software simulator with matching capabilities has been developed. The simulator allows for prototyping and initial validation of the algorithms prior to their deployment on the K11. The simulator is also available to the PDM algorithms to assist with the reasoning process. A reference set of diagnostic, prognostic, and decision making algorithms is also described, followed by an overview of the current test scenarios and the results of their execution on the simulator.",
-            "title": "Development of a Mobile Robot Test Platform and Methods for Validation of Prognostics-Enabled Decision Making Algorithms",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Balaban_et_al._-_2013_-_Development_of_a_Mobile_Robot_Test_Platform_and_Methods_for_Validation_of_Prognostics-Enabled_Decision_Making_Al.pdf",
-                    "description": "Balaban et al. - 2013 - Development of a Mobile Robot Test Platform and Methods for Validation of Prognostics-Enabled Decision Making Al.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Balaban et al. - 2013 - Development of a Mobile Robot Test Platform and Methods for Validation of Prognostics-Enabled Decision Making Al.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Balaban_et_al._-_2013_-_Development_of_a_Mobile_Robot_Test_Platform_and_Methods_for_Validation_of_Prognostics-Enabled_Decision_Making_Al.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Balaban et al. - 2013 - Development of a Mobile Robot Test Platform and Methods for Validation of Prognostics-Enabled Decision Making Al.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_882",
+            "issued": "2013-12-25",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/882/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Development of a Mobile Robot Test Platform and Methods for Validation of Prognostics-Enabled Decision Making Algorithms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MASTCAM-4-RDR-Z-V1.0",
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
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mastcam-4-rdr-z-v1.0_hkt8-nmrz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MASTCAM-4-RDR-Z-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mastcam-4-rdr-z-v1.0_hkt8-nmrz",
-            "description": "NULL",
-            "title": "MSL MARS MAST CAMERA 4 RDR\n                                      ZSTACK V1.0",
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
+            "title": "MSL MARS MAST CAMERA 4 RDR\n                                      ZSTACK V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/651",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Norby, R.J., M.F. Cotrufo, P. Ineson, E.G. O'Neill, and J.G. Canadell. 2002. Effects of Elevated Carbon Dioxide on Litter Chemistry and Decomposition . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/651",
-            "issued": "2002-12-11",
-            "temporal": "1993-01-01T00:00:00Z/2000-11-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
-            "keyword": [
-                "ecological dynamics",
-                "earth science",
-                "vegetation",
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
-            "identifier": "C2761762163-ORNL_CLOUD",
             "description": "The results of published and unpublished experiments investigating the impacts of elevated carbon dioxide on the chemistry (nitrogen and lignin concentration) of leaf litter and the decomposition of plant tissues are assembled in a format appropriate for statistical meta-analysis of the effect of carbon dioxide.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Effects of Elevated Carbon Dioxide on Litter Chemistry and Decomposition",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F651",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F651",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/litter_decomp/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/litter_decomp/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Norby_CO2_litter2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/Norby_CO2_litter2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/651",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/651",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/litter_decomp/comp/Litter_quality_variables.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/litter_decomp/comp/Litter_quality_variables.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/litter_decomp/comp/Litter_refs.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/litter_decomp/comp/Litter_refs.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/litter_decomp/comp/Norby_CO2_litter2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/litter_decomp/comp/Norby_CO2_litter2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
+            "identifier": "C2761762163-ORNL_CLOUD",
+            "issued": "2002-12-11",
+            "keyword": [
+                "ecological dynamics",
+                "earth science",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/651",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -47.31 179.41 76.63",
+            "temporal": "1993-01-01T00:00:00Z/2000-11-21T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Effects of Elevated Carbon Dioxide on Litter Chemistry and Decomposition"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/2YJ7GZPW2NNB",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VIIRS/JPSS1 CGF Snow Cover Daily L3 Global 375m SIN Grid V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/2YJ7GZPW2NNB.",
-            "issued": "2018-01-05",
-            "temporal": "2018-01-05T00:00:00Z/2024-12-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-05",
-            "keyword": [
-                "earth science",
-                "snow/ice",
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
-            "identifier": "C2317026377-NSIDC_ECS",
             "description": "This data set contains daily 'cloud-free' snow cover produced from the VIIRS/JPSS-1 Snow Cover Daily L3 Global 375m SIN Grid, Version 2 snow cover product. A cloud-gap-filled algorithm is utilized to replace \u2018cloud-covered\u2019 pixels with \u2018cloud-free pixels\u2019 for the purpose of estimating the snow cover that may exist under current cloud cover. The data are provided daily and mapped to a 375 m sinusoidal grid.",
-            "title": "VIIRS/JPSS1 CGF Snow Cover Daily L3 Global 375m SIN Grid V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2YJ7GZPW2NNB",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2YJ7GZPW2NNB",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VJ110A1F.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/VIIRS/VJ110A1F.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VJ110A1F+V002",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VJ110A1F+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/VJ110A1F/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/VJ110A1F/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/2YJ7GZPW2NNB",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/2YJ7GZPW2NNB",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/2YJ7GZPW2NNB",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/2YJ7GZPW2NNB",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2317026377-NSIDC_ECS",
+            "issued": "2018-01-05",
+            "keyword": [
+                "earth science",
+                "snow/ice",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/2YJ7GZPW2NNB",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-05T00:00:00Z/2024-12-09T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 CGF Snow Cover Daily L3 Global 375m SIN Grid V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67PCHURYUMOV-M11-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission, covering the period from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67pchuryumov-m11-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "16 cyg b",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67PCHURYUMOV-M11-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67pchuryumov-m11-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission, covering the period from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP011 RDR V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP011 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GRIP/LASE/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ismail, Syed, Richard A Ferrare, Jonathan Hair, Amin  Nehrir, Susan Kooi, Anthony Notari, Carolyn Butler, Marta Fenn and James Collins.2011. GRIP LIDAR ATMOSPHERIC SENSING EXPERIMENT (LASE) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GRIP/LASE/DATA201",
-            "issued": "2011-06-02",
-            "temporal": "2010-08-13T16:18:14Z/2010-09-25T17:17:56Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
-            "keyword": [
-                "lidar",
-                "earth science",
-                "atmospheric water vapor",
-                "aerosols",
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
-            "identifier": "C1979855347-GHRC_DAAC",
             "description": "The GRIP Lidar Atmospheric Sensing Experiment (LASE) dataset was collected by NASA's Lidar Atmospheric Sensing Experiment (LASE) system, which is an airborne Differential Absorption Lidar (DIAL) system used to measure water vapor, aerosols, and clouds throughout the troposphere. LASE is onboard the NASA DC-8 aircraft and probes the atmosphere using lasers to transmit light in the 815-nm absorption band of water vapor. Pulses of laser light are fired vertically below the aircraft. A small fraction of the transmitted laser light is reflected from the atmosphere back to the aircraft and collected with a telescope receiver. The received light indicates the amount of water vapor along the path of the laser beam. LASE operated in the Genesis and Rapid Intensification Processes (GRIP) experiment with data spanning between August 13, 2010 through September 25, 2010.  The major goal was to better understand how tropical storms form and develop into major hurricanes. NASA used the DC-8 aircraft, the WB-57 aircraft and the Global Hawk Unmanned Airborne System (UAS), configured with a suite of in situ and remote sensing instruments that were used to observe and characterize the lifecycle of hurricanes.",
-            "graphic-preview-description": "N/A",
-            "title": "GRIP LIDAR ATMOSPHERIC SENSING EXPERIMENT (LASE) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRIP%2FLASE%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGRIP%2FLASE%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=griplase",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=griplase",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/GRIP_LASE_20100828_AER_R1.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/GRIP_LASE_20100828_AER_R1.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/GRIP_LASE_20100828_H2O_lin_R1.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/GRIP_LASE_20100828_H2O_lin_R1.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/GRIP_LASE_20100828_H2O_R1.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/GRIP_LASE_20100828_H2O_R1.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/grip/griplase/griplase_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/grip/griplase/griplase_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/grip/griplase/read_lase_gh.c",
-                    "description": "demonstrate reading LASE SOLVE/AFWEX data files",
                     "@type": "dcat:Distribution",
+                    "description": "demonstrate reading LASE SOLVE/AFWEX data files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/grip/griplase/read_lase_gh.c",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/GRIP",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/GRIP",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/grip/LASE/browse/",
+            "identifier": "C1979855347-GHRC_DAAC",
+            "issued": "2011-06-02",
+            "keyword": [
+                "lidar",
+                "earth science",
+                "atmospheric water vapor",
+                "aerosols",
+                "atmosphere",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GRIP/LASE/DATA201",
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
             "spatial": "-117.083 12.0 -55.3183 34.7533",
+            "temporal": "2010-08-13T16:18:14Z/2010-09-25T17:17:56Z",
             "theme": [
                 "GRIP (HURRICANE)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRIP LIDAR ATMOSPHERIC SENSING EXPERIMENT (LASE) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-3-CR4B-CALIB2-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the CRUISE 4-2\nmission phase where the primary target was the SOLAR WIND. It contains\ninstrument outputs in volts and amperes, calibrated and corrected for\ninstrument offsets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-3-cr4b-calib2-v1.0_hkyh-jzdd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-3-CR4B-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-3-cr4b-calib2-v1.0_hkyh-jzdd",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the CRUISE 4-2\nmission phase where the primary target was the SOLAR WIND. It contains\ninstrument outputs in volts and amperes, calibrated and corrected for\ninstrument offsets.",
-            "title": "ROSETTA-ORBITER SW RPCLAP 3\nCR4B CALIB2 V1.0",
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
+            "title": "ROSETTA-ORBITER SW RPCLAP 3\nCR4B CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-2HRNR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2021-06-22. Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NRT Reduced Ocean Surface Topography . Version F. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-2HRNR.",
-            "issued": "2020-12-07",
-            "temporal": "2020-12-07T14:20:01.399Z/2023-05-29T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-26",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
-                "sea surface topography",
-                "ocean waves"
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
-            "identifier": "C1968980549-POCLOUD",
-            "description": "Provides L2 high resolution (HR) near real time (NRT; 3-hour latency) altimetry from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft. It contains Sea Surface Height (SSH), Sea Surface Height Anomalies (SSHA) and Significant Wave Height (SWH), along with 1 Hz Ku-band measurements processed from L1B altimetry including the range, orbital altitude, time, and water vapour. It also includes altimetry corrections, significant wave height and wind-speed from the AMR-C. This release is reduced to exclude the 20 Hz observations that are included in the standard product. The S6A NRT product is analogous to the Jason-3 OGDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NRT Reduced Ocean Surface Topography",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides L2 high resolution (HR) near real time (NRT; 3-hour latency) altimetry from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft. It contains Sea Surface Height (SSH), Sea Surface Height Anomalies (SSHA) and Significant Wave Height (SWH), along with 1 Hz Ku-band measurements processed from L1B altimetry including the range, orbital altitude, time, and water vapour. It also includes altimetry corrections, significant wave height and wind-speed from the AMR-C. This release is reduced to exclude the 20 Hz observations that are included in the standard product. The S6A NRT product is analogous to the Jason-3 OGDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2HRNR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2HRNR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/missions/sentinel-6/",
-                    "description": "The mission page for Sentinel-6A MF on the NASA Jet Propulsion Laboratory (JPL) website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the NASA Jet Propulsion Laboratory (JPL) website.",
+                    "downloadURL": "https://www.jpl.nasa.gov/missions/sentinel-6/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sealevel.jpl.nasa.gov/missions/jasoncs/",
-                    "description": "The mission page for Sentinel-6A MF on the NASA Ocean Surface Topography (OST) website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the NASA Ocean Surface Topography (OST) website.",
+                    "downloadURL": "https://sealevel.jpl.nasa.gov/missions/jasoncs/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-6",
-                    "description": "The mission page for Sentinel-6A MF on the European Space Agency (ESA) website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the European Space Agency (ESA) website.",
+                    "downloadURL": "https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Sentinel-6",
-                    "description": "The mission page for Sentinel-6A MF on the PO.DAAC website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the PO.DAAC website.",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Sentinel-6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.eumetsat.int/sentinel-6",
-                    "description": "The mission page for Sentinel-6A MF on the EUMETSAT website.",
                     "@type": "dcat:Distribution",
+                    "description": "The mission page for Sentinel-6A MF on the EUMETSAT website.",
+                    "downloadURL": "https://www.eumetsat.int/sentinel-6",
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
-                    "downloadURL": "https://github.com/podaac/sentinel6",
-                    "description": "Jupyter notebooks to access and manipulate data from Sentinel-6A MF.",
                     "@type": "dcat:Distribution",
+                    "description": "Jupyter notebooks to access and manipulate data from Sentinel-6A MF.",
+                    "downloadURL": "https://github.com/podaac/sentinel6",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.eumetsat.int/altimetry-resources",
-                    "description": "Documentation hosted by EUMETSAT including the Generic File Naming Convention, and the Level 1 and Level 2 Product Format Specifications.",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation hosted by EUMETSAT including the Generic File Naming Convention, and the Level 1 and Level 2 Product Format Specifications.",
+                    "downloadURL": "https://www.eumetsat.int/altimetry-resources",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewforum.php?f=97",
-                    "description": "PO.DAAC Forum Page for Sentinel-6A MF",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Forum Page for Sentinel-6A MF",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewforum.php?f=97",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968980549-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968980549-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968980549-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968980549-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_RED_OST_NRT_F.jpg",
+            "identifier": "C1968980549-POCLOUD",
+            "issued": "2020-12-07",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "sea surface topography",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-2HRNR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.rse.2021.112395"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "-180.0 -66.15 180.0 66.15",
+            "temporal": "2020-12-07T14:20:01.399Z/2023-05-29T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NRT Reduced Ocean Surface Topography"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0041",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2005-01-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0041.",
-            "issued": "2004-12-16",
-            "temporal": "2000-08-02T00:00:00Z/2000-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C2349162385-LARC_ASDC",
             "description": "NARSTO_EPA_HOUSTON_TEXAQS2000_CAMS_DATA is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Houston, Texas Air Quality Study 2000 (TexAQS2000) Texas Natural Resource Conservation Commission (TNRCC) continuous ambient monitoring stations (CAMS) Air Quality Data. This data set contains 5-minute air quality measurements collected in Texas during August and September 2000 at 85 CAMS during TEXAQS2000. Measurements include carbon monoxide (CO), sulfur dioxide (SO2), nitrogen oxide (NO), nitrogen dioxide (NO2), oxides of nitrogen (NOx), total reactive nitrogen species (NOy), ozone, particulate matter (PM) 2.5 mass, hydrogen sulfide (H2S), wind speed, wind direction, maximum wind gust, air temperature, dewpoint temperature, humidity, precipitation, surface pressure, radiation, and visibility. CAMS are operated by the Texas Commission on Environmental Quality (TCEQ), local city or county governments, or private monitoring networks. Important monitoring site information: The site information data table in each of the 85 data files may not contain the latest TCEQ site information. A companion file site information spreadsheet (.csv) that lists data for all 85 sites is the latest TCEQ site information. The site information data tables in the 85 data files will not be updated. The 85 site spreadsheet companion document is the official source of site data, and this data is listed in the TEXAQS2000 CAMS guide document.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Houston, Texas Air Quality Study 2000 (TexAQS2000) Texas Natural Resource Conservation Commission (TNRCC) continuous ambient monitoring stations (CAMS) Air Quality Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0041",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0041",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2349162385-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_CAMS_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_CAMS_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2349162385-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0041",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_CAMS_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_CAMS_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0041",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_houston_texaqs2000_cams_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_HOUSTONTEXAQS2000 TNRCC CAMS Air Quality Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_HOUSTONTEXAQS2000 TNRCC CAMS Air Quality Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_houston_texaqs2000_cams_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Houston_Final_Report.pdf",
-                    "description": "Gulf Coast Aerosol Research and Characterization Program (Houston Supersite) FINAL REPORT - April 2005",
                     "@type": "dcat:Distribution",
+                    "description": "Gulf Coast Aerosol Research and Characterization Program (Houston Supersite) FINAL REPORT - April 2005",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Houston_Final_Report.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_HOUSTON_TEXAQS2000_CAMS_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_CAMS_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_CAMS_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_HOUSTON_TEXAQS2000_CAMS_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2349162385-LARC_ASDC",
+            "issued": "2004-12-16",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0041",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>27.76 -98.62 27.76 -93.76 33.36 -93.76 33.36 -98.62 27.76 -98.62</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-08-02T00:00:00Z/2000-09-30T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Houston, Texas Air Quality Study 2000 (TexAQS2000) Texas Natural Resource Conservation Commission (TNRCC) continuous ambient monitoring stations (CAMS) Air Quality Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XRS-2-EDR-CRUISE2-V1.0",
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
-                "near earth asteroid rendezvous",
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains X-Ray Spectrometer (XRS) observations made during the second cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xrs-2-edr-cruise2-v1.0_hm4m-rrqv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XRS-2-EDR-CRUISE2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xrs-2-edr-cruise2-v1.0_hm4m-rrqv",
-            "description": "This data set contains X-Ray Spectrometer (XRS) observations made during the second cruise phase of the NEAR mission. The individual observations are combined into a single file per day for each sensor.",
-            "title": "NEAR XRS SPECTRA FOR CRUISE 2 PHASE",
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
+            "title": "NEAR XRS SPECTRA FOR CRUISE 2 PHASE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/SPEX-PR/RADIANCE/ELLIPSOID_V006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-05-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AIRCRAFT/AIRMSPI/SPEX-PR/RADIANCE/ELLIPSOID_V006. http://eosweb.larc.nasa.gov/project/airmspi/airmspi_table.",
-            "issued": "2018-04-02",
-            "temporal": "2016-02-02T00:00:00Z/2016-02-09T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-23",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "ultraviolet wavelengths",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID, DR. DINER",
                 "hasEmail": "mailto:david.j.diner@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1517289471-LARC_ASDC",
             "description": "AirMSPI_SPEX-PR_Ellipsoid-projected_Georegistered_Radiance_Data is an AirMSPI ellipsoid-projected georegistered radiance product acquired during the SPEX engineering flights + Porter Ranch gas leak overflights (SPEX-PR) flight campaign.\nAirMSPI Level 1B2 products contain radiometric and polarimetric images of clouds, aerosols, and the surface of the Earth. In particular, products contain map-projected data at 8 wavelengths: 355, 380, 445, 470, 555, 660, 865, and 935 nm. The data products include radiance, time, solar zenith, solar azimuth, view zenith, and view azimuth for all spectral bands. Wavelengths for which polarization information is available (470, 660, and 865 nm) also include the Stokes parameters Q and U, as well as degree of linear polarization (DOLP) and angle of linear polarization (AOLP). Q, U, and AOLP are reported relative to both the scattering- and view meridian planes. Files are distributed in HDF-EOS-5 format.\nThis release of AirMSPI data contains all targets acquired during the SPEX engineering flights + Porter Ranch gas leak overflights (SPEX-PR) flight campaign, which was based out of Armstrong Flight Research Center in Palmdale, CA. The SPEX engineering flights conducted on February 2 through February 5, 2016 focused on the checkout of another polarimeter, SPEX airborne, built by SRON Netherlands Institute for Space Research, with AirMSPI providing validation. On February 9, the ER-2 overflew the Porter Ranch, California natural gas leak with AirMSPI and the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) collecting data.",
-            "title": "AirMSPI verison 6 ellipsoid-projected georegistered radiance product acquired during the SPEX-PR flight campaign",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FSPEX-PR%2FRADIANCE%2FELLIPSOID_V006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAIRCRAFT%2FAIRMSPI%2FSPEX-PR%2FRADIANCE%2FELLIPSOID_V006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -872180,643 +872160,638 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1517289471-LARC_ASDC",
+            "issued": "2018-04-02",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "ultraviolet wavelengths",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/AIRCRAFT/AIRMSPI/SPEX-PR/RADIANCE/ELLIPSOID_V006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-121.0 31.0 -117.0 39.0",
+            "temporal": "2016-02-02T00:00:00Z/2016-02-09T23:59:59Z",
             "theme": [
                 "AIRMSPI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMSPI verison 6 ellipsoid-projected georegistered radiance product acquired during the SPEX-PR flight campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/541/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-02-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nikunj Oza",
                 "hasEmail": "mailto:Nikunj.C.Oza@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_541",
             "description": "As the amount of textual information grows explosively in various kinds of business systems, it becomes more and more desirable to analyze both structured data records and unstructured text data simultaneously. Although online analytical processing (OLAP) techniques have been proven very useful for analyzing and mining structured data, they face challenges in handling text data. On the other hand, probabilistic topic models are among the most effective approaches to latent topic analysis and mining on text data. In this paper, we study a new data model called topic cube to combine OLAP with probabilistic topic modeling and enable OLAP on the dimension of text data in a multidimensional text database. Topic cube extends the traditional data cube to cope with a topic hierarchy and stores probabilistic content measures of text documents learned through a probabilistic topic model. To materialize topic cubes efficiently, we propose two heuristic aggregations to speed up the iterative Expectation-Maximization (EM) algorithm for estimating topic models by leveraging the models learned on component data cells to choose a good starting point for iteration. Experimental results show that these heuristic aggregations are much faster than the baseline method of computing each topic cube from scratch. We also discuss some potential uses of topic cube and show sample experimental results.",
-            "title": "Topic Modeling for OLAP on Multidimensional Text Databases: Topic Cube and its Applications",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/zhzh09.pdf",
-                    "description": "zhzh09.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "zhzh09.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/zhzh09.pdf",
+                    "mediaType": "application/pdf",
                     "title": "zhzh09.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_541",
+            "issued": "2012-02-26",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/541/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Topic Modeling for OLAP on Multidimensional Text Databases: Topic Cube and its Applications"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-ESC1-V2.0",
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
+            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the comet escort 1 phase (ESC1). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 20 Nov 2014 and 10 Mar 2015. This version of the data has been reprocessed to remove an error introduced in the previous version.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-esc1-v2.0_hmah-npct",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCIES-3-ESC1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcies-3-esc1-v2.0_hmah-npct",
-            "description": "This dataset contains CALIBRATED DATA of the Rosetta RPCIES instrument taken during the comet escort 1 phase (ESC1). The target of this phase was comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). Included are the data taken between 20 Nov 2014 and 10 Mar 2015. This version of the data has been reprocessed to remove an error introduced in the previous version.",
-            "title": "ROSETTA-ORBITER 67P RPCIES 3 ESC1 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P RPCIES 3 ESC1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/UO3Q64CTTS1U",
             "citation": "AIRS project. 2019-12-15. AIRS3STD. Version 7.0. Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V7.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/UO3Q64CTTS1U. https://disc.gsfc.nasa.gov/datacollection/AIRS3STD_7.0.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.5194/acp-14-399-2014"
-            ],
-            "keyword": [
-                "atmospheric pressure",
-                "air quality",
-                "surface thermal properties",
-                "surface radiative properties",
-                "ocean temperature",
-                "oceans",
-                "land surface",
-                "earth science",
-                "altitude",
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LENA IREDELL",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "AIRS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1701805652-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. The AIRS Level 3 Daily Gridded Product contains standard retrieval means, standard deviations and input counts. Each file covers a temporal period of 24 hours for either the descending (equatorial crossing North to South at 1:30 AM local time) or ascending (equatorial crossing South to North at 1:30 PM local time) orbit. The data starts at the international dateline and progresses westward (as do the subsequent orbits of the satellite) so that neighboring gridded cells of data are no more than a swath of time apart (about 90 minutes). The two parts of a scan line crossing the dateline are included in separate L3 files, according to the date, so that data points in a grid box are always coincident in time. The edge of the AIRS Level 3 gridded cells is at the date line (the 180E/W longitude boundary). When plotted, this produces a map with 0 degrees longitude in the center of the image unless the bins are reordered. This method is preferred because the left (West) side of the image and the right (East) side of the image contain data farthest apart in time. The gridding scheme used by AIRS is the same as used by TOVS Pathfinder to create Level 3 products. The daily Level 3 products have gores between satellite paths where there is no coverage for that day. The geophysical parameters have been averaged and binned into 1 x 1 deg grid cells, from -180.0 to +180.0 deg longitude and from -90.0 to +90.0 deg latitude. For each grid map of 4-byte floating-point mean values there is a corresponding 4-byte floating-point map of standard deviation and a 2-byte integer grid map of counts. The counts map provides the user with the number of points per bin that were included in the mean and can be used to generate custom multi-day maps from the daily gridded products. The thermodynamic parameters are: Skin Temperature (land and sea surface), Air Temperature at the surface, Profiles of Air Temperature and Water Vapor, Tropopause Characteristics, Column Precipitable Water, Cloud Amount/Frequency, Cloud Height, Cloud Top Pressure, Cloud Top Temperature, Reflectance, Emissivity, Surface Pressure, Cloud Vertical Distribution. The trace gases parameters are: Total Amounts and Vertical Profiles of Carbon Monoxide, Methane, and Ozone. The actual names of the variables in the data files should be inferred from the Processing File Description document.\n\n\nThe value for each grid box is the sum of the values that fall within the 1x1 area divided by the number of points in the\nbox.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS3STD",
-            "creator": "AIRS project",
-            "graphic-preview-description": "Sample data of the \"Aqua/AIRS Level 3 daily standard physical retrieval product\".",
-            "title": "Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V7.0 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3STD_7.0.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUO3Q64CTTS1U",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUO3Q64CTTS1U",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3STD_7.0.png",
-                    "description": "Sample data of the \"Aqua/AIRS Level 3 daily standard physical retrieval product\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"Aqua/AIRS Level 3 daily standard physical retrieval product\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3STD_7.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3STD_7.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS3STD_7.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3STD.7.0/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRS3STD.7.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3STD.7.0",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRS3STD.7.0",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3STD+7.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS3STD+7.0",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_the_AIRS_Mission.pdf",
-                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of the AIRS Mission: Instruments, Processing Algorithms, Products, and Documentation",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/Overview_of_the_AIRS_Mission.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf",
-                    "description": "AIRS Version 7 Level 3 Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Version 7 Level 3 Product User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/V7_L3_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Sample data of the \"Aqua/AIRS Level 3 daily standard physical retrieval product\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS3STD_7.0.png",
+            "identifier": "C1701805652-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "atmospheric pressure",
+                "air quality",
+                "surface thermal properties",
+                "surface radiative properties",
+                "ocean temperature",
+                "oceans",
+                "land surface",
+                "earth science",
+                "altitude",
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/UO3Q64CTTS1U",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1117/1.JRS.8.084994",
+                "https://doi.org/10.5194/acp-14-399-2014"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRS3STD",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2025-01-20T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua/AIRS L3 Daily Standard Physical Retrieval (AIRS-only) 1 degree x 1 degree V7.0 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HP-SSA-GCMS-3-FCO%2FDESCENT-V1.0",
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
-                "titan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hp-ssa-gcms-3-fco-descent-v1.0_hmfk-9xmd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=HP-SSA-GCMS-3-FCO%2FDESCENT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.hp-ssa-gcms-3-fco-descent-v1.0_hmfk-9xmd",
-            "description": "Unknown",
-            "title": "HUYGENS TITAN GAS CHROMATOGRAPH MASS SPEC 3 DESCENT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "HUYGENS TITAN GAS CHROMATOGRAPH MASS SPEC 3 DESCENT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-LAUNCH-V1.1",
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
-                "solar wind",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-launch-v1.1_hmg2-juqs",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-LAUNCH-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-launch-v1.1_hmg2-juqs",
-            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS PEPSSI POST-LAUNCH CHECKOUT V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS PEPSSI POST-LAUNCH CHECKOUT V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AKASA-XOGD1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Shailen Desai. 2013-12-03. SARAL Near-Real-Time Value-added Operational Geophysical Data Record Sea Surface Height Anomaly. Version f. ALTIKA_SARAL_L2_OST_XOGDR. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, JPL. https://doi.org/10.5067/AKASA-XOGD1. Shailen Desai, JPL, 2013-12-03, SARAL Near-Real-Time Value-added Operational Geophysical Data Record Sea Surface Height Anomaly, .",
-            "issued": "2013-10-24",
-            "temporal": "2020-03-18T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean waves",
-                "sea surface topography"
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
-            "identifier": "C2251465126-POCLOUD",
-            "description": "These data are near-real-time (NRT) (within 7-9 hours of measurement) sea surface height anomalies (SSHA) from the AltiKa altimeter onboard the Satellite with ARgos and ALtiKa (SARAL).  SARAL is a French(CNES)/Indian(SARAL) collaborative mission to measure sea surface height using the Ka-band AltiKa altimeter and was launched February 25, 2013. The major difference between these data and the Operational Geophysical Data Record (OGDR) data produced by the project is that the orbit from SARAL has been adjusted using SSHA differences with those from the OSTM/Jason-2 GPS-OGDR-SSHA product at inter-satellite crossover locations. This produces a more accurate NRT orbit altitude for SARAL with accuracy of 1.5 cm (RMS), taking advantage of the 1 cm (radial RMS) accuracy of the GPS-based orbit used for the OSTM/Jason-2 GPS-OGDR-SSHA product. This dataset also contains all data from the project (reduced) OGDR, and improved altimeter wind speeds and sea state bias correction. More information on the SARAL mission can be found at: http://www.aviso.oceanobs.com/en/missions/current-missions/saral.html",
-            "release-place": "JPL",
-            "series-name": "SARAL Near-Real-Time Value-added Operational Geophysical Data Record Sea Surface Height Anomaly",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Shailen Desai",
-            "title": "SARAL Near-Real-Time Value-added Operational Geophysical Data Record Sea Surface Height Anomaly",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ALTIKA_SARAL_L2_OST_XOGDR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "These data are near-real-time (NRT) (within 7-9 hours of measurement) sea surface height anomalies (SSHA) from the AltiKa altimeter onboard the Satellite with ARgos and ALtiKa (SARAL).  SARAL is a French(CNES)/Indian(SARAL) collaborative mission to measure sea surface height using the Ka-band AltiKa altimeter and was launched February 25, 2013. The major difference between these data and the Operational Geophysical Data Record (OGDR) data produced by the project is that the orbit from SARAL has been adjusted using SSHA differences with those from the OSTM/Jason-2 GPS-OGDR-SSHA product at inter-satellite crossover locations. This produces a more accurate NRT orbit altitude for SARAL with accuracy of 1.5 cm (RMS), taking advantage of the 1 cm (radial RMS) accuracy of the GPS-based orbit used for the OSTM/Jason-2 GPS-OGDR-SSHA product. This dataset also contains all data from the project (reduced) OGDR, and improved altimeter wind speeds and sea state bias correction. More information on the SARAL mission can be found at: http://www.aviso.oceanobs.com/en/missions/current-missions/saral.html",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAKASA-XOGD1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAKASA-XOGD1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ALTIKA_SARAL_L2_OST_XOGDR.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ALTIKA_SARAL_L2_OST_XOGDR.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/saral/preview/L2/XOGDR-SSHA/docs/README_JPLNRTSSHASRL.txt",
-                    "description": "User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/saral/preview/L2/XOGDR-SSHA/docs/README_JPLNRTSSHASRL.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2251465126-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2251465126-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2251465126-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2251465126-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "description": "Data Subscriber",
                     "downloadURL": "https://github.com/podaac/data-subscriber",
-                    "mediaType": "text/html",
-                    "description": "Data Subscriber"
+                    "mediaType": "text/html"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ALTIKA_SARAL_L2_OST_XOGDR.jpg",
+            "identifier": "C2251465126-POCLOUD",
+            "issued": "2013-10-24",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean waves",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/AKASA-XOGD1",
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
+            "series-name": "SARAL Near-Real-Time Value-added Operational Geophysical Data Record Sea Surface Height Anomaly",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2020-03-18T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "SARAL",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SARAL Near-Real-Time Value-added Operational Geophysical Data Record Sea Surface Height Anomaly"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-XYZ-OPS-V1.0",
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
-                "phoenix",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains xyz data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-xyz-ops-v1.0_hmj2-8vp9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-XYZ-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-xyz-ops-v1.0_hmj2-8vp9",
-            "description": "The Surface Stereo Imager (SSI) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This SSI Imaging Operations RDR data set contains xyz data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 XYZ OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 5 XYZ OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_KONVEX_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-05-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/AIRMISR_KONVEX_1. http://eosweb.larc.nasa.gov/project/airmisr/airmisr_table.",
-            "issued": "2001-05-21",
-            "temporal": "1999-07-13T00:00:00Z/1999-07-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "visible wavelengths",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
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
-            "identifier": "C1000000722-LARC_ASDC",
             "description": "The AIRMISR_KONVEX data were acquired during the KONza Validation EXperiment (KONVEX) which occurred 11 - 18 July 1999. The AIRMISR_KONVEX data were obtained on 13 July 1999, flight #36 only. The Jet Propulsion Laboratory (JPL) in Pasadena, California provided the data. The Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) is an airborne instrument for obtaining multi-angle imagery similar to that of the satellite-borne Multi-angle Imaging SpectroRadiometer (MISR) instrument, which is designed to contribute to studies of the Earth's ecology and climate. AirMISR flies on the NASA ER-2 aircraft. The Jet Propulsion Laboratory in Pasadena, California built the instrument for NASA. Unlike the satellite-borne MISR instrument, which has nine cameras oriented at various angles, AirMISR uses a single camera in a pivoting gimbal mount. A data run by the ER-2 aircraft is divided into nine segments, each with the camera positioned to a MISR look angle. The gimbal rotates between successive segments, such that each segment acquires data over the same area on the ground as the previous segment. This process is repeated until all nine angles of the target area are collected. The swath width, which varies from 11 km in the nadir to 32 km at the most oblique angle, is governed by the camera's instantaneous field-of-view of 7 meters cross-track x 6 meters along-track in the nadir view and 21 meters x 55 meters at the most oblique angle. The along-track image length at each angle is dictated by the timing required to obtain overlap imagery at all angles, and varies from about 9 km in the nadir to 26 km at the most oblique angle. Thus, the nadir image dictates the area of overlap that is obtained from all nine angles. A complete flight run takes approximately 13 minutes. The 9 camera viewing angles are:0 degrees or nadir26.1 degrees, fore and aft45.6 degrees, fore and aft60.0 degrees, fore and aft70.5 degrees, fore and aft For each of the camera angles, images are obtained at 4 spectral bands. The spectral bands can be used to identify vegetation and aerosols, estimate surface reflectance and ocean color studies. The center wavelengths of the 4 spectral bands are:443 nanometers, blue555 nanometers, green670 nanometers, red865 nanometers, near-infrared Two types of AirMISR data products are available - the Level 1 Radiometric product (L1B1) and the Level 1 Georectified radiance product (L1B2).",
-            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the KONza Validation EXperiment (KONVEX)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_KONVEX_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_KONVEX_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/airmisr/airmisr_table",
-                    "description": "EOSWEB Data and Information for AirMISR",
                     "@type": "dcat:Distribution",
+                    "description": "EOSWEB Data and Information for AirMISR",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/airmisr/airmisr_table",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000722-LARC_ASDC",
-                    "description": "Earthdata Search for AIRMISR_KONVEX_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AIRMISR_KONVEX_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000722-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/airmisr/airmisr_read_software.pdf",
-                    "description": "AirMISR Read Software Document Readme",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Read Software Document Readme",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/airmisr/airmisr_read_software.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/airmisr/readme/readme_airmisr_konvex",
-                    "description": "Readme Information about the AirMISR data taken during the KONza Validation EXperiment(KONVEX) including implementation of the sample READ software",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the AirMISR data taken during the KONza Validation EXperiment(KONVEX) including implementation of the sample READ software",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/airmisr/readme/readme_airmisr_konvex",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/airmisr/read_software/read_airmisr.pro",
-                    "description": "Readme to open and read AIRMISR L1B2 GP (Georectified Radiance Product) HDF-EOS data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to open and read AIRMISR L1B2 GP (Georectified Radiance Product) HDF-EOS data files",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/airmisr/read_software/read_airmisr.pro",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/airmisr/quality_summaries/airmisr_konvex.pdf",
-                    "description": "Quality Summary: AirMISR KONVEX",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: AirMISR KONVEX",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/sites/default/files/project/airmisr/quality_summaries/airmisr_konvex.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMISR/AIRMISR_KONVEX/contents.html",
-                    "description": "OPeNDAP data access for AIRMISR_KONVEX_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for AIRMISR_KONVEX_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMISR/AIRMISR_KONVEX/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_KONVEX_1",
-                    "description": "DOI data set landing page for AIRMISR_KONVEX_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AIRMISR_KONVEX_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_KONVEX_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1000000722-LARC_ASDC",
+            "issued": "2001-05-21",
+            "keyword": [
+                "visible wavelengths",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_KONVEX_1",
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
             "spatial": "-96.9 38.8 -96.2 39.3",
+            "temporal": "1999-07-13T00:00:00Z/1999-07-13T23:59:59Z",
             "theme": [
                 "AIRMISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the KONza Validation EXperiment (KONVEX)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YAE_L3.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Aerosol Product covering a year's products;See ProductionDateTime for Published date.",
-            "issued": "2003-12-03",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-05-05",
-            "keyword": [
-                "nasa"
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
-            "identifier": "C43677733-LARC",
             "description": "This file contains the MISR Level 3 Component Global Aerosol Product covering a year",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Component Global Aerosol Product covering a year V004",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YAE_L3.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YAE_L3.004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C43677733-LARC",
+            "issued": "2003-12-03",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YAE_L3.004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-05-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Component Global Aerosol Product covering a year V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPM/VIRS/TRMM/1B/07",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2021-07-29. GPM_1BVIRS. GPM VIRS on TRMM Radiance L1B 1.5 hours 2 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/VIRS/TRMM/1B/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1BVIRS_07.html. Digital Science Data.",
-            "issued": "2021-07-21",
-            "temporal": "1997-12-20T00:00:00Z/2014-03-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-21",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "sensor characteristics",
-                "infrared wavelengths",
-                "platform characteristics",
-                "visible wavelengths"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2264132644-GES_DISC",
-            "description": "This is the new (GPM-formated) TRMM product. It replaces the old TRMM_1B01\n\n Version 07 is the current version of the data set. Previous versions have been superseded by Version 07.\n\nThis TRMM Visible and Infrared Scanner (VIRS) Level 1B Calibrated Radiance Product (1B01) contains calibrated radiances and auxiliary geolocation information from the five channels of the VIRS instrument, for each pixel of each scan. The data are stored in the Hierarchical Data Format (HDF), which includes both core and product specific metadata applicable to the VIRS measurements. A file contains a single orbit of data with a file size of about 95 MB. The EOSDIS \"swath\" structure is used to accommodate the actual geophysical data arrays. There are 16 files of VIRS 1B01 data produced per day.\n\nFor channels 1 and 2, Level 1B radiances are derived from the Level 1A (1A01) sensor counts by computing calibration parameters (gain and offset) derived from the counts registered during space and solar and/or lunar views. New calibration parameters are produced every one to four weeks. Channels 3, 4, and 5 are calibrated using the internal blackbody and the space view. These calibration parameters, together with a quadratic term determined pre-launch, are used to generate a counts vs. radiance curve for each band, which is then used to convert the earth-view pixel counts to spectral radiances.\n\nGeolocation and channel data are written out for each pixel along the scan, whereas the time stamp, scan status (containing scan quality information), navigation, calibration coefficients, and solar/satellite geometry are specified on a per-scan basis. There are in general 18026 scans along the orbit pre-boost and 18223 post-boost, with each scan consisting of 261 pixels. The scan width is about 720 km pre-boost and 833 km post-boost.\n\nChanges in horizontal resolution resulting from the TRMM boost that occurred on 24 August 2001:\n\nPre-Boost (before 7 August 2001): Temporal Resolution: 91.5 min/orbit ~ 16 orbits/day; Swath Width: 720 km; Horizontal Resolution: 2.2 km \n\nPost-Boost (after 24 August 2001): Temporal Resolution: 92.5 min/orbit ~ 16 orbits/day; Swath Width: 833 km; Horizontal Resolution: 2.4 km",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_1BVIRS",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "GPM VIRS on TRMM Radiance L1B 1.5 hours 2 km V07 (GPM_1BVIRS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1B-BR.TRMM.VIRS.Tb2017.20050829-S013444-E030706.044376.V05A.PNG",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This is the new (GPM-formated) TRMM product. It replaces the old TRMM_1B01\n\n Version 07 is the current version of the data set. Previous versions have been superseded by Version 07.\n\nThis TRMM Visible and Infrared Scanner (VIRS) Level 1B Calibrated Radiance Product (1B01) contains calibrated radiances and auxiliary geolocation information from the five channels of the VIRS instrument, for each pixel of each scan. The data are stored in the Hierarchical Data Format (HDF), which includes both core and product specific metadata applicable to the VIRS measurements. A file contains a single orbit of data with a file size of about 95 MB. The EOSDIS \"swath\" structure is used to accommodate the actual geophysical data arrays. There are 16 files of VIRS 1B01 data produced per day.\n\nFor channels 1 and 2, Level 1B radiances are derived from the Level 1A (1A01) sensor counts by computing calibration parameters (gain and offset) derived from the counts registered during space and solar and/or lunar views. New calibration parameters are produced every one to four weeks. Channels 3, 4, and 5 are calibrated using the internal blackbody and the space view. These calibration parameters, together with a quadratic term determined pre-launch, are used to generate a counts vs. radiance curve for each band, which is then used to convert the earth-view pixel counts to spectral radiances.\n\nGeolocation and channel data are written out for each pixel along the scan, whereas the time stamp, scan status (containing scan quality information), navigation, calibration coefficients, and solar/satellite geometry are specified on a per-scan basis. There are in general 18026 scans along the orbit pre-boost and 18223 post-boost, with each scan consisting of 261 pixels. The scan width is about 720 km pre-boost and 833 km post-boost.\n\nChanges in horizontal resolution resulting from the TRMM boost that occurred on 24 August 2001:\n\nPre-Boost (before 7 August 2001): Temporal Resolution: 91.5 min/orbit ~ 16 orbits/day; Swath Width: 720 km; Horizontal Resolution: 2.2 km \n\nPost-Boost (after 24 August 2001): Temporal Resolution: 92.5 min/orbit ~ 16 orbits/day; Swath Width: 833 km; Horizontal Resolution: 2.4 km",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FVIRS%2FTRMM%2F1B%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FVIRS%2FTRMM%2F1B%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -872826,1030 +872801,1064 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1BVIRS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1BVIRS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1/GPM_1BVIRS.07",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L1/GPM_1BVIRS.07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L1/GPM_1BVIRS.07/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L1/GPM_1BVIRS.07/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1BVIRS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1BVIRS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm.nasa.gov",
-                    "description": "TRMM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Project Home Page",
+                    "downloadURL": "https://gpm.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/formatChangesV7.pdf",
-                    "description": "Comparison between TRMM versions 6 and 7.",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison between TRMM versions 6 and 7.",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/formatChangesV7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/README.TRMM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/README.TRMM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/anomalous.html",
-                    "description": "TRMM Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Data Gaps",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/anomalous.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1B-BR.TRMM.VIRS.Tb2017.20050829-S013444-E030706.044376.V05A.PNG",
+            "identifier": "C2264132644-GES_DISC",
+            "issued": "2021-07-21",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "sensor characteristics",
+                "infrared wavelengths",
+                "platform characteristics",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/VIRS/TRMM/1B/07",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-07-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_1BVIRS",
             "spatial": "-180.0 -38.0 180.0 38.0",
+            "temporal": "1997-12-20T00:00:00Z/2014-03-21T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM VIRS on TRMM Radiance L1B 1.5 hours 2 km V07 (GPM_1BVIRS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1263",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kaptue, A.T., N.P. Hanan, L. Prihodko, and J.A. Ramirez. 2015. Spatio-temporal Characteristics of Rainfall in Africa, 0.25 degrees, from 1998-2012. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1263",
-            "issued": "2023-10-02",
-            "temporal": "1998-01-01T00:00:00Z/2012-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
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
-            "identifier": "C2776874873-ORNL_CLOUD",
             "description": "This data set describes rainfall distribution statistics over the African continent, including Madagascar. The rainfall estimates are based on data from the NASA Tropical Rainfall Measuring Mission (TRMM) measured between 1998 and 2012. Rainfall patterns were quantified using a gamma-based function and two Markov chain parameters with the aim to summarize the rainfall pattern to a small number of parameters and processes. These summary statistics are suitable for temporal downscaling.These data provide gridded (0.25 x 0.25-degree) estimates of 14-year mean monthly rainfall total amount (mm), frequency (count), intensity (mm/hr), and duration (hrs) of rainfall, as well as Markov chain and gamma-distribution parameters for use in temporal downscaling. The data are presented as a series of 12 netCDF (*.nc) files.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Spatio-temporal Characteristics of Rainfall in Africa, 0.25 degrees, from 1998-2012",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1263_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1263",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1263",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/African_Rainfall_Patterns/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/African_Rainfall_Patterns/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/African_Rainfall_Patterns.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/African_Rainfall_Patterns.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1263",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1263",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/African_Rainfall_Patterns/comp/African_Rainfall_Patterns.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/African_Rainfall_Patterns/comp/African_Rainfall_Patterns.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/African_Rainfall_Patterns/comp/read_rainfall_stat.R",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/African_Rainfall_Patterns/comp/read_rainfall_stat.R",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1263_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1263_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1263/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1263/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1263_1_fit.png",
+            "identifier": "C2776874873-ORNL_CLOUD",
+            "issued": "2023-10-02",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1263",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-20.0 -40.0 55.0 40.0",
+            "temporal": "1998-01-01T00:00:00Z/2012-12-31T23:59:59Z",
             "theme": [
                 "Climate",
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Spatio-temporal Characteristics of Rainfall in Africa, 0.25 degrees, from 1998-2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M01-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m01-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M01-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m01-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP001 RDR V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP001 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-VIS-CERES-SPECTRA-V1.0",
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
-                "1 ceres",
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This volume contains the digital\nnumbers (DN) contained in the telemetry (TM) packages of the VIR-VIS\ninstrument on board of the spacecraft DAWN. The data are from the\nCeres Encounter and Extended mission phases, which occurred 2014-12-26\nto 2017-04-29.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-vis-ceres-spectra-v1.0_hmpf-x94x",
+            "issued": "2021-05-21",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-VIS-CERES-SPECTRA-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-vis-ceres-spectra-v1.0_hmpf-x94x",
-            "description": "This volume contains the digital\nnumbers (DN) contained in the telemetry (TM) packages of the VIR-VIS\ninstrument on board of the spacecraft DAWN. The data are from the\nCeres Encounter and Extended mission phases, which occurred 2014-12-26\nto 2017-04-29.",
-            "title": "DAWN VIR RAW (EDR) CERES VISIBLE SPECTRA \n                                      V1.0",
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
+            "title": "DAWN VIR RAW (EDR) CERES VISIBLE SPECTRA \n                                      V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR13-V1.0",
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
-                "titan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR13) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 26 and 28, 2009, during he Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr13-v1.0_hmu5-irdq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR13-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr13-v1.0_hmu5-irdq",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR13) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 26 and 28, 2009, during he Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR13 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TIGR13 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1262-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-16T17:59:55.000 to 2015-12-17T03:32:22.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1262-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1262-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1262-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-16T17:59:55.000 to 2015-12-17T03:32:22.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1262 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1262 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-MRI-2-NAV-9P-CRUISE-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw calibration and test images acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the cruise phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the flyby spacecraft. These data were collected from 14 January to 25 April 2005. Test images of comet 9P/Tempel 1 were acquired on 25 April. In this version 1.1 of the data set, the values for the INTEGRATION_DURATION keyword in the PDS data labels were corrected. This revised data set supersedes version 1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-mri-2-nav-9p-cruise-v1.1_hmx5-5a4z",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deep impact",
                 "9p/tempel 1 (1867 g1)",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-MRI-2-NAV-9P-CRUISE-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-mri-2-nav-9p-cruise-v1.1_hmx5-5a4z",
-            "description": "This data set contains raw calibration and test images acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the cruise phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the flyby spacecraft. These data were collected from 14 January to 25 April 2005. Test images of comet 9P/Tempel 1 were acquired on 25 April. In this version 1.1 of the data set, the values for the INTEGRATION_DURATION keyword in the PDS data labels were corrected. This revised data set supersedes version 1.0.",
-            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW MRI NAV IMAGES V1.1",
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
+            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW MRI NAV IMAGES V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625796319-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2006), Terra/MISR Level 1, Ellipsoid Product subset for the GoMACCS region, version 3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-22",
-            "temporal": "2006-07-30T16:37:49.880Z/2006-10-16T17:48:48.136Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-22",
-            "keyword": [
-                "visible wavelengths",
-                "spectral/engineering",
-                "earth science"
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
-            "identifier": "C1625796319-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 1B2 Ellipsoid Product subset for the GoMACCS region V003 contains Ellipsoid-projected TOA Radiance, resampled at the surface and topographically corrected, as well as geometrically corrected by PGE22.",
-            "title": "MISR Level 1B2 Ellipsoid Product subset for the GoMACCS region V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1625796319-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1625796319-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1625796319-LARC",
+            "issued": "2019-07-22",
+            "keyword": [
+                "visible wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1625796319-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-07-30T16:37:49.880Z/2006-10-16T17:48:48.136Z",
             "theme": [
                 "GOMACCS_2006",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 1B2 Ellipsoid Product subset for the GoMACCS region V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/440/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marilyn Smith",
                 "hasEmail": "mailto:marilyn.smith@ae.gatech.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_440",
             "description": "This RSW gridset is designed as the medium size mixed element grid for use with cell-centered unstructured meshes.\r\n\r\nUG3      : Grid File Name    = rsw_med_mixedcc.b8.ugrid\r\nUG3      : Quad Surface Faces=     13056\r\nUG3      : Tria Surface Faces=    107586\r\nUG3      : Nodes             =   3819936\r\nUG3      : Total Elements    =   8667521\r\nUG3      : Hex Elements      =         0\r\nUG3      : Pent_5 Elements   =     18324\r\nUG3      : Pent_6 Elements   =   7010592\r\nUG3      : Tet Elements      =   1638605\r\nUG3      : BL Tet Elements   =     18000",
-            "title": "RSW Mixed Element Cell-Centered Medium Mesh",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.b8.ugrid",
-                    "description": "ugrid file",
                     "@type": "dcat:Distribution",
+                    "description": "ugrid file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.b8.ugrid",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_mixedcc.b8.ugrid"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.cgns",
-                    "description": "CGNS Format Grid File",
                     "@type": "dcat:Distribution",
+                    "description": "CGNS Format Grid File",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.cgns",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_mixedcc.cgns"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.info",
-                    "description": "Grid Information",
                     "@type": "dcat:Distribution",
+                    "description": "Grid Information",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.info",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_mixedcc.info"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.mapbc",
-                    "description": "Mapbc file (FUN3D)",
                     "@type": "dcat:Distribution",
+                    "description": "Mapbc file (FUN3D)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.mapbc",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_mixedcc.mapbc"
                 },
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.surf.gz",
-                    "description": "surface grid (gzipped)",
                     "@type": "dcat:Distribution",
+                    "description": "surface grid (gzipped)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.surf.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "rsw_med_mixedcc.surf.gz"
                 },
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.tags",
-                    "description": "tag file",
                     "@type": "dcat:Distribution",
+                    "description": "tag file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/rsw_med_mixedcc.tags",
+                    "mediaType": "application/octet-stream",
                     "title": "rsw_med_mixedcc.tags"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_440",
+            "issued": "2011-07-19",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/440/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW Mixed Element Cell-Centered Medium Mesh"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-CR2-PC1-2-V3.0",
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
-                "checkout"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCRUISE 2 mission phase. This release supersedes version 1.0. Version 2.0 was never generated\nfor pre-comet phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-cr2-pc1-2-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-CR2-PC1-2-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-cr2-pc1-2-v3.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCRUISE 2 mission phase. This release supersedes version 1.0. Version 2.0 was never generated\nfor pre-comet phases.",
-            "title": "ROSETTA-ORBITER CHECK MIDAS 3 CR2 PC1-2 V3.0",
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
+            "title": "ROSETTA-ORBITER CHECK MIDAS 3 CR2 PC1-2 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-KECK1LWS%2FETAL-5-DELBO-V1.0",
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
-                "support archives",
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains radiometric albedos and diameters for Near Earth Asteroids (NEAs) derived by three different thermal models and reported in Delbo (2004) [DELBO2004]. The observed infrared fluxes on which the derivations were based are also included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-keck1lws-etal-5-delbo-v1.0_hmzv-jk5i",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-KECK1LWS%2FETAL-5-DELBO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-keck1lws-etal-5-delbo-v1.0_hmzv-jk5i",
-            "description": "This data set contains radiometric albedos and diameters for Near Earth Asteroids (NEAs) derived by three different thermal models and reported in Delbo (2004) [DELBO2004]. The observed infrared fluxes on which the derivations were based are also included.",
-            "title": "DELBO THERMAL INFRARED ASTEROID DIAMETERS AND ALBEDOS V1.0",
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
+            "title": "DELBO THERMAL INFRARED ASTEROID DIAMETERS AND ALBEDOS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M09-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-10-24 to 2014-11-21.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m09-v1.0_hn37-8njb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M09-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m09-v1.0_hn37-8njb",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-10-24 to 2014-11-21.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 009 V1.0",
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
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 009 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC5-V1.0",
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
-                "titan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Titan Bistatic and Occultation Experiment (TBOC5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 4 and June 22, 2009, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc5-v1.0_hn45-w4cv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC5-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc5-v1.0_hn45-w4cv",
-            "description": "The Cassini Radio Science Titan Bistatic and Occultation Experiment (TBOC5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on April 4 and June 22, 2009, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TBOC5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TBOC5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/doi:10.5067/8V8LF6311A0J",
             "citation": "Daniel Tong at Geroge Mason University . 2023-04-18. HAQES_NA_PM25_TOT_CENSUS. Version 1. HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration at census level, North America V1.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/doi:10.5067/8V8LF6311A0J. https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_CENSUS_1.html. Digital Science Data.",
-            "issued": "2023-04-15",
-            "temporal": "2022-01-02T00:00:00Z/2023-05-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-15",
-            "references": [
-                "https://doi.org/%20http%3A//doi.org/10.1016/j.atmosenv.2015.11.004"
-            ],
-            "keyword": [
-                "public health",
-                "human dimensions",
-                "air quality",
-                "atmosphere",
-                "earth science",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Suhung Shen",
                 "hasEmail": "mailto:suhung.shen-1@nasa.gov"
             },
+            "creator": "Daniel Tong at Geroge Mason University",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2623694394-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product provides HAQES 3-hourly ensemble mean surface total PM2.5 concentration at the census level over the continental United States (CONUS). \n\nThe Hazardous Air Quality Ensemble System (HAQES) is a real-time ensemble forecast of hazardous air quality events, such as wildfires, dust storms, and Volcanic eruptions. Both regional and global models from multiple agencies are used to create the ensemble, including the Goddard Earth Observing System (GEOS) from the National Aeronautics and Space Administration (NASA), the Navy Aerosol Analysis and Prediction System (NAAPS) from Naval Research Laboratory, the Global Ensemble Forecast System Aerosols (GEFS), High-Resolution Rapid Refresh (HRRR), and National Oceanic and Atmospheric Administration-U.S. Environmental Protection Agency (NOAA-EPA) Atmosphere-Chemistry Coupler-Community Multiscale Air Quality model (NACC-CMAQ) from NOAA.  The prototypes of HAQES products were developed by the George Mason University Air Quality Laboratory as part of the NASA Health Air Quality Applied Science Team (HAQAST).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HAQES_NA_PM25_TOT_CENSUS",
-            "creator": "Daniel Tong at Geroge Mason University",
-            "graphic-preview-description": "Sample image: The surface total PM2.5 concentration at the census level from the HAQES model for November 12, 2022 at 18:00Z.",
-            "title": "HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration at census level, North America V1 (HAQES_NA_PM25_TOT_CENSUS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_CENSUS_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8V8LF6311A0J",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8V8LF6311A0J",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_CENSUS_1.png",
-                    "description": "Sample image: The surface total PM2.5 concentration at the census level from the HAQES model for November 12, 2022 at 18:00Z.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image: The surface total PM2.5 concentration at the census level from the HAQES model for November 12, 2022 at 18:00Z.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_CENSUS_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT_CENSUS.1/doc/README_HAQES_PM25_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT_CENSUS.1/doc/README_HAQES_PM25_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_CENSUS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_CENSUS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT_CENSUS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT_CENSUS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQES_NA_PM25_TOT_CENSUS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQES_NA_PM25_TOT_CENSUS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Sample image: The surface total PM2.5 concentration at the census level from the HAQES model for November 12, 2022 at 18:00Z.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_CENSUS_1.png",
+            "identifier": "C2623694394-GES_DISC",
+            "issued": "2023-04-15",
+            "keyword": [
+                "public health",
+                "human dimensions",
+                "air quality",
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/doi:10.5067/8V8LF6311A0J",
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
+            "series-name": "HAQES_NA_PM25_TOT_CENSUS",
             "spatial": "-132.0 21.0 -58.5 53.5",
+            "temporal": "2022-01-02T00:00:00Z/2023-05-08T00:00:00Z",
             "theme": [
                 "HAQAST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration at census level, North America V1 (HAQES_NA_PM25_TOT_CENSUS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/588CX4CQWVV4",
             "citation": "Goddard Space Flight Center (GSFC). 2022-12-12. SCAMSN6IM. Version 001. SCAMS/Nimbus-6 Images of Brightness Temperatures, Water Vapor and Temperature on 70-mm Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/588CX4CQWVV4. https://disc.gsfc.nasa.gov/datacollection/SCAMSN6IM_001.html. Digital Science Data.",
-            "issued": "2022-03-24",
-            "temporal": "1975-06-15T00:00:00Z/1976-05-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-24",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "Goddard Space Flight Center (GSFC)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2563801376-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The SCAMSN6IM data product consists of images of brightness temperatures, water vapor and temperature on 70 mm film strips from the Nimbus-6 Scanning Microwave Spectrometer. Each display contains eight vertical strips of data from one orbit. All strips have the same geographic coverage, but each represents a different parameter. The first three are brightness temperatures for channels 2 (31.65 GHz) and 3 (52.85 GHz) and their differences. The next two represent retrieved water vapor and liquid water from clouds or precipitation over the oceans, respectively. The remaining three strips on the right represent inverted mean temperatures for atmospheric layers 1000-500 mbar, 500-250 mbar, and 250-100 mbar, respectively. The first five parameters are displayed in 18-step gray levels, the values of which can be found in a table in each of the first five volumes of \"The Nimbus 6 Data Catalog.\" The last three parameters are displayed by contour bands (labeled on the side) that are spaced 4 K apart. Spatial resolution on the ground for the parameters varies from 145 km at nadir to 330 km at the scan extremes. The images are saved as TIFF digital files. About 3-5 months of images are archived into a ZIP file. Additional information can be found in section 2.4.1 of \"The Nimbus 6 User's Guide.\"\n\nThe SCAMS experiment on Nimbus-6 is a follow on to the successful Nimbus-5 NEMS experiment. SCAMS continuously monitored emitted microwave radiation at frequencies of 22.235, 31.65, 52.85, 53.85 and 55.45 GHz. The three channels near the 5.0-mm oxygen absorption band were used primarily to deduce atmospheric temperature profiles. The two channels near 10 mm permitted water vapor and cloud water content over calm oceans to be estimated separately. The instrument, a Dicke-superheterodyne type, scanned +/- 45 degrees normal to the orbital plane with a 10 degree field of view. The three oxygen channels shared common signal and reference antennas. Both water vapor channels had their own signals and reference antennas. The absolute rms accuracy of the oxygen channels was better than 2 Kelvin and that of the water vapor channels better than 1 Kelvin.\n\nThe SCAMS Principal Investigator was Prof. David H. Staelin from MIT. The Nimbus-6 SCAMS images are available from June 15, 1975 (day of year 166) through May 31, 1976 (day of year 152).\n\nThis product was previously available from the NSSDC with the identifier ESAD-00200 (old ID 75-052A-10B).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SCAMSN6IM",
-            "creator": "Goddard Space Flight Center (GSFC)",
-            "title": "SCAMS/Nimbus-6 Images of Brightness Temperatures, Water Vapor and Temperature on 70-mm Film V001 (SCAMSN6IM) at GES DISC",
-            "graphic-preview-description": "SCAMS",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SCAMSN6IM_001.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F588CX4CQWVV4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F588CX4CQWVV4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SCAMSN6IM_001.jpg",
-                    "description": "SCAMS",
                     "@type": "dcat:Distribution",
+                    "description": "SCAMS",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SCAMSN6IM_001.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCAMSN6IM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SCAMSN6IM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus6_SCAMS_Level2/SCAMSN6IM.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus6_SCAMS_Level2/SCAMSN6IM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus6_SCAMS_Level2/SCAMSN6IM.001/doc/README.SCAMSN6IM.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus6_SCAMS_Level2/SCAMSN6IM.001/doc/README.SCAMSN6IM.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusVIUG.pdf",
-                    "description": "Nimbus 6 User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 6 User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusVIUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus6.tar.gz",
-                    "description": "Nimbus 6 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 6 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus6.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "SCAMS",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SCAMSN6IM_001.jpg",
+            "identifier": "C2563801376-GES_DISC",
+            "issued": "2022-03-24",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/588CX4CQWVV4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SCAMSN6IM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1975-06-15T00:00:00Z/1976-05-31T23:59:59.999Z",
             "theme": [
                 "CWIC",
                 "geospatial"
-            ],
-            "language": [
-                "en-US"
-            ]
+            ],
+            "title": "SCAMS/Nimbus-6 Images of Brightness Temperatures, Water Vapor and Temperature on 70-mm Film V001 (SCAMSN6IM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHMG1-2PO01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NOAA/NESDIS/OSPO. 2023-03-16. GHRSST L2P Indian Ocean Regional Skin SST from SEVIRI on MSG-1 satellite. Version 1.0. GHRSST Level 2P Indian Ocean Regional Skin Sea Surface Temperature v1.0 from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation-1 (MSG-1) satellite. Camp Springs, MD (USA). Archived by National Aeronautics and Space Administration, U.S. Government, JPL/PODAAC. https://doi.org/10.5067/GHMG1-2PO01.",
-            "issued": "2018-09-18",
-            "temporal": "2018-09-18T00:00:00Z/2022-06-01T23:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-09-18",
-            "keyword": [
-                "earth science",
-                "ocean temperature",
-                "oceans"
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
-            "identifier": "C2098739529-POCLOUD",
-            "description": "The GHRSST L2P MSG01 SST v1.0 dataset is produced by the US National Oceanic and Atmospheric Administration (NOAA) National Environmental Satellite, Data, and Information Service (NESDIS) from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) onboard the Meteosat-8 (MSG1) satellite. It provides the full disk SEVIRI imagery covering the Indian Ocean region from its position at 45.5\u00b0E longitude. The L2P SST is produced at approximately 3 km resolution with a 15 minute duty cycle. The full data records stretch from Sept. 18, 2018 to June 1, 2022. After June 1, 2022, the Meteosat-9 (MSG2) took over as the prime geostationary satellite for the Indian Ocean region (MSG02-OSPO-L2P-v1.0). Be aware that the granules before Dec. 1, 2022 contain some uncorrected metadata errors. <br><br>\r\n\r\nThe SST measurements from SEVIRI are key parameters in study of the weather, atmosphere, climate and ocean environments. Meteosat satellites have been providing crucial data for weather forecasting since 1977.  <br><br>\r\n\r\nThis L2P SST product which includes Single Sensor Error Statistics (i.e., uncertainty statistics) follows the GHRSST Data Processing Specification (GDS) version 2.0 format guidelines. Please refer to the user guide for more information.",
-            "release-place": "Camp Springs, MD (USA)",
-            "series-name": "GHRSST L2P Indian Ocean Regional Skin SST from SEVIRI on MSG-1 satellite",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NOAA/NESDIS/OSPO",
-            "title": "NOAA GHRSST Level 2P Indian Ocean Regional Skin Sea Surface Temperature v1.0 from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation-1 (MSG-1) satellite",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MSG01-OSPO-L2P-v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The GHRSST L2P MSG01 SST v1.0 dataset is produced by the US National Oceanic and Atmospheric Administration (NOAA) National Environmental Satellite, Data, and Information Service (NESDIS) from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) onboard the Meteosat-8 (MSG1) satellite. It provides the full disk SEVIRI imagery covering the Indian Ocean region from its position at 45.5\u00b0E longitude. The L2P SST is produced at approximately 3 km resolution with a 15 minute duty cycle. The full data records stretch from Sept. 18, 2018 to June 1, 2022. After June 1, 2022, the Meteosat-9 (MSG2) took over as the prime geostationary satellite for the Indian Ocean region (MSG02-OSPO-L2P-v1.0). Be aware that the granules before Dec. 1, 2022 contain some uncorrected metadata errors. <br><br>\r\n\r\nThe SST measurements from SEVIRI are key parameters in study of the weather, atmosphere, climate and ocean environments. Meteosat satellites have been providing crucial data for weather forecasting since 1977.  <br><br>\r\n\r\nThis L2P SST product which includes Single Sensor Error Statistics (i.e., uncertainty statistics) follows the GHRSST Data Processing Specification (GDS) version 2.0 format guidelines. Please refer to the user guide for more information.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMG1-2PO01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMG1-2PO01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MSG01-OSPO-L2P-v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MSG01-OSPO-L2P-v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ghrsst.org",
-                    "description": "GHRSST Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project Home Page",
+                    "downloadURL": "https://www.ghrsst.org",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
-                    "description": "Documentation on the GDS version 2 format specification",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation on the GDS version 2 format specification",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2098739529-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2098739529-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2098739529-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2098739529-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MSG01-OSPO-L2P-v1.0.jpg",
+            "identifier": "C2098739529-POCLOUD",
+            "issued": "2018-09-18",
+            "keyword": [
+                "earth science",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHMG1-2PO01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-09-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Camp Springs, MD (USA)",
+            "series-name": "GHRSST L2P Indian Ocean Regional Skin SST from SEVIRI on MSG-1 satellite",
             "spatial": "-81.0 -73.0 81.0 73.0",
+            "temporal": "2018-09-18T00:00:00Z/2022-06-01T23:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA GHRSST Level 2P Indian Ocean Regional Skin Sea Surface Temperature v1.0 from the Spinning Enhanced Visible and InfraRed Imager (SEVIRI) on the Meteosat Second Generation-1 (MSG-1) satellite"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/QL4HIMU3TQ3U",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Landsat Thematic Mapper Imagery: Alabama, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/QL4HIMU3TQ3U.",
-            "issued": "2002-07-07",
-            "temporal": "2002-07-07T00:00:00Z/2003-06-23T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-06-23",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
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
-            "identifier": "C1386250380-NSIDCV0",
             "description": "This data set provides imagery developed from Landsat 5 Thematic Mapper (TM) and Landsat 7 Enhanced Thematic Mapper (ETM+) data for use in studying land cover features during the Soil Moisture Experiment 2003 (SMEX03).",
-            "title": "SMEX03 Landsat Thematic Mapper Imagery: Alabama, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQL4HIMU3TQ3U",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQL4HIMU3TQ3U",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/TM_GEOTIFF",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/TM_GEOTIFF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/TM_GEOTIFF",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/satellite/TM_GEOTIFF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QL4HIMU3TQ3U",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/QL4HIMU3TQ3U",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QL4HIMU3TQ3U",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/QL4HIMU3TQ3U",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250380-NSIDCV0",
+            "issued": "2002-07-07",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/QL4HIMU3TQ3U",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-06-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-87.1 34.6 -85.7 35.2",
+            "temporal": "2002-07-07T00:00:00Z/2003-06-23T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Landsat Thematic Mapper Imagery: Alabama, Version 1"
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
+            "description": "APXS, Atmospheric Opacity, HAZCAM, NAVCAM, MI, PANCAM, RAT, Rover Motion Counter, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130222.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-490",
+            "issued": "2018-06-25",
             "keyword": [
                 "apxs",
                 "atmospheric opacity",
@@ -873862,156 +873871,123 @@
                 "rover motion counter",
                 "spice"
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
-            "identifier": "NASA-490",
-            "description": "APXS, Atmospheric Opacity, HAZCAM, NAVCAM, MI, PANCAM, RAT, Rover Motion Counter, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 35",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130222.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 35"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3320-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-06-21T06:10:31.000 to 2012-06-21T08:49:04.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3320-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3320-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3320-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-06-21T06:10:31.000 to 2012-06-21T08:49:04.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3320 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3320 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567904-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "surface radiative properties",
-                "topography",
-                "earth science",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNIEPAT JOHNSON",
                 "hasEmail": "mailto:lta@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220567904-USGS_LTA",
             "description": "The surface reflectance CDR is generated from specialized software called Landsat Ecosystem Disturbance Adaptive Processing System (LEDAPS). LEDAPS was originally developed through a National Aeronautics and Space Administration (NASA) Making Earth System Data Records for Use in Research Environments (MEaSUREs)grant by NASA Goddard Space Flight Center (GSFC) and the University of Maryland (Masek et al., 2006). The software applies Moderate Resolution Imaging Spectroradiometer (MODIS) atmospheric correction routines to Level-1 Landsat Thematic Mapper (TM) or Enhanced Thematic Mapper Plus (ETM+)data. Water,vapor, ozone, geopotential height, aerosol optical thickness,and digital elevation are input with Landsat data to the Second Simulation of a Satellite Signal in the Solar Spectrum (6S) radiative transfer models to generate top of atmosphere (TOA)reflectance, surface reflectance, brightness temperature, and masks for clouds, cloud shadows, adjacent clouds, land, and water.  The result is delivered as the Landsat surface reflectance CDR.",
-            "title": "Land Surface Reflectance - GLS2010",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Data set searching and ordering capabilities are available through EarthExplorer at the above URL.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Data set searching and ordering capabilities are available through EarthExplorer at the above URL.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1220567904-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "surface radiative properties",
+                "topography",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567904-USGS_LTA.html",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Land Surface Reflectance - GLS2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-09-05",
-            "temporal": "2021-09-05T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "topo",
-                "space",
-                "location",
-                "iss",
-                "international",
-                "ephemeris",
-                "coords",
-                "coordinates",
-                "trajectory",
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
-            "identifier": "nasa-iss-data_2021-09-05_hn8j-cnmz",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-09-05",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -874134,401 +874110,427 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-09-05_hn8j-cnmz",
+            "issued": "2021-09-05",
+            "keyword": [
+                "topo",
+                "space",
+                "location",
+                "iss",
+                "international",
+                "ephemeris",
+                "coords",
+                "coordinates",
+                "trajectory",
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
+            "temporal": "2021-09-05T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-09-05"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "http://techport.nasa.gov/view/10856",
-            "issued": "2018-06-25",
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
                 "fn": "Lisa May",
                 "hasEmail": "mailto:lisa.may@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10856",
             "description": "&lt;p&gt;\r\n\tNASA&amp;rsquo;s Mars Exploration Program (MEP) calls for a series of highly ambitious missions over the next decade and beyond. The overall goals of the MEP must be achieved with relatively low mission risk and within tightly constrained cost resources. The current overarching scientific goals of the MEP are: life, climate, geology, and preparation for human exploration. These have a common, measurable link: water. For Mars (like Earth), water is central to the planet&amp;rsquo;s history; it is also the primary reason for interest in it as a potentially habitable world. No new proposals are being solicited or funded in FY 2012 under this project line. Proposals for Mars instrument technology development are now included in PIDDP and no new awards will be provided under the Mars Instrument Development Program (MIDP).&lt;/p&gt;",
-            "title": "Mars Technology Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10856",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10856",
+            "issued": "2018-06-25",
+            "keyword": [
+                "active",
+                "project",
+                "nasa headquarters"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10856",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
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
+            "title": "Mars Technology Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1876",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Newman, P.A., and S. Pawson. 2021. ATom: GEOS-5 Derived Meteorological Conditions and Tagged Tracers Along Flight Tracks. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1876",
-            "issued": "2022-01-03",
-            "temporal": "2016-07-29T00:00:00Z/2018-05-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "earth science",
-                "environmental impacts",
-                "human dimensions"
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
-            "identifier": "C2677009033-ORNL_CLOUD",
             "description": "This dataset provides modeled meteorological conditions and tagged-CO tracer concentrations along ATom flight paths derived from the Goddard Earth Observing System Version 5 (GEOS-5) data assimilation products from the Global Modeling and Assimilation Office (GMAO) at NASA's Goddard Space Flight Center. The GMAO \"GEOS fp\" forward processing system ingests satellite, ground-based, and airborne data, using a sophisticated model along with the data's statistical properties to obtain global three-dimensional data gridded fields at regular time intervals. These data are from the GMAO model output that were fitted to the ATom flight tracks by interpolating the GMAO model output to the horizontal ATom flight tracks for each of the 4 ATom Deployments.  The dataset also provides tagged-CO tracer concentrations, which represent the contribution of specific regional sources to the total simulated CO. The data products produced are consistent with both the original measurements and the physical laws governing the atmosphere. To provide some meteorological context for the ATom flights, the GEOS5 gridded data are interpolated in space and time to the flight tracks.",
-            "graphic-preview-description": "An example of aerosols modeled by GEOS-5. Source: NASA, 2020",
-            "title": "ATom: GEOS-5 Derived Meteorological Conditions and Tagged Tracers Along Flight Tracks",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/Interpolated_Met_Products_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1876",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1876",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/Interpolated_Met_Products/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/Interpolated_Met_Products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/Interpolated_Met_Products.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/Interpolated_Met_Products.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1876",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1876",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/Interpolated_Met_Products/comp/Interpolated_Met_Products.pdf",
-                    "description": "ATom: GEOS-5 Derived Meteorological Conditions and Tagged Tracers Along Flight Tracks: Interpolated_Met_Products.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: GEOS-5 Derived Meteorological Conditions and Tagged Tracers Along Flight Tracks: Interpolated_Met_Products.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/Interpolated_Met_Products/comp/Interpolated_Met_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/Interpolated_Met_Products_Fig1.jpg",
-                    "description": "An example of aerosols modeled by GEOS-5. Source: NASA, 2020",
                     "@type": "dcat:Distribution",
+                    "description": "An example of aerosols modeled by GEOS-5. Source: NASA, 2020",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/Interpolated_Met_Products_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/campaign/",
-                    "description": "ATom campaign page",
                     "@type": "dcat:Distribution",
+                    "description": "ATom campaign page",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/campaign/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "An example of aerosols modeled by GEOS-5. Source: NASA, 2020",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/Interpolated_Met_Products_Fig1.jpg",
+            "identifier": "C2677009033-ORNL_CLOUD",
+            "issued": "2022-01-03",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "earth science",
+                "environmental impacts",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1876",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-07-29T00:00:00Z/2018-05-21T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: GEOS-5 Derived Meteorological Conditions and Tagged Tracers Along Flight Tracks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-3/EDOP/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hood, Robbie E.2019. CAMEX-3 ER-2 Doppler Radar (EDOP) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-3/EDOP/DATA101",
-            "issued": "2019-11-27",
-            "temporal": "1998-08-08T16:12:00Z/1998-09-27T20:29:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-20",
-            "keyword": [
-                "radar",
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
-            "identifier": "C1995565983-GHRC_DAAC",
             "description": "The CAMEX-3 ER-2 Doppler Radar (EDOP) dataset is a browse-only dataset that consists of plotted reflectivity and Doppler velocity data collected by the ER-2 Doppler Radar (EDOP) during the third field campaign in the Convection And Moisture EXperiment (CAMEX) series, CAMEX-3. This field campaign took place from August to September 1998 based out of Patrick Air Force Base in Florida, with the purpose of studying the various aspects of tropical cyclones in the region. EDOP was mounted onboard the NASA ER-2 high-altitude research aircraft from which it obtained vertical profiles of convection within tropical cyclones. The daily browse files are available from August 5 through September 27, 1998 in GIF format.",
-            "graphic-preview-description": "Browse Sample",
-            "title": "CAMEX-3 ER-2 Doppler Radar (EDOP) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/camex3/er2edop/EDOP_980902_2151-2204_n.gif",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FEDOP%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FEDOP%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=er2edop",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=er2edop",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/camex3/er2edop/EDOP_980902_2151-2204_n.gif",
-                    "description": "Browse Sample",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Sample",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/camex3/er2edop/EDOP_980902_2151-2204_n.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/armstrong/news/FactSheets/FS-046-DFRC.html",
-                    "description": "NASA Armstrong Fact Sheet: ER-2 High-Altitude Airborne Science Aircraft",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Armstrong Fact Sheet: ER-2 High-Altitude Airborne Science Aircraft",
+                    "downloadURL": "https://www.nasa.gov/centers/armstrong/news/FactSheets/FS-046-DFRC.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/er2edop/doc/er2edop_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/camex3/er2edop/doc/er2edop_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(1996)013%3C0795:TERSOT%3E2.0.CO;2",
-                    "description": "The EDOP Radar System on the High-Altitude NASA ER-2 Aircraft",
                     "@type": "dcat:Distribution",
+                    "description": "The EDOP Radar System on the High-Altitude NASA ER-2 Aircraft",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(1996)013%3C0795:TERSOT%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C1310:EDRIOT%3E2.0.CO;2",
-                    "description": "ER-2 Doppler Radar (EDOP) Investigations of the Eyewall of Hurricane Bonnie During CAMEX-3",
                     "@type": "dcat:Distribution",
+                    "description": "ER-2 Doppler Radar (EDOP) Investigations of the Eyewall of Hurricane Bonnie During CAMEX-3",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C1310:EDRIOT%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JAS3607.1",
-                    "description": "Overview of the Convection and Moisture Experiment (CAMEX)",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of the Convection and Moisture Experiment (CAMEX)",
+                    "downloadURL": "https://doi.org/10.1175/JAS3607.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/camex3",
-                    "description": "CAMEX-3 Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "CAMEX-3 Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/camex3",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
+            "graphic-preview-description": "Browse Sample",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/camex3/er2edop/EDOP_980902_2151-2204_n.gif",
+            "identifier": "C1995565983-GHRC_DAAC",
+            "issued": "2019-11-27",
+            "keyword": [
+                "radar",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-3/EDOP/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-89.971 13.976 -63.22 34.588",
+            "temporal": "1998-08-08T16:12:00Z/1998-09-27T20:29:00Z",
             "theme": [
                 "CAMEX-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-3 ER-2 Doppler Radar (EDOP) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/750",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Turner, D.P., W.D. Ritts, and M.J. Gregory. 2006. BigFoot NPP Surfaces for North and South American Sites, 2000-2004. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/750",
-            "issued": "2023-07-26",
-            "temporal": "2000-01-01T00:00:00Z/2004-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-01",
-            "keyword": [
-                "ecological dynamics",
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
-            "identifier": "C2751481549-ORNL_CLOUD",
             "description": "The BigFoot project gathered Net Primary Production (NPP) data for nine EOS Land Validation Sites located from Alaska to Brazil from 2000 to 2004. Each site is representative of one or two distinct biomes, including the Arctic tundra; boreal evergreen needleleaf forest; temperate cropland, grassland, evergreen needleleaf forest, and deciduous broadleaf forest; desert grassland and shrubland; and tropical evergreen broadleaf forest. BigFoot was funded by NASA's Terrestrial Ecology Program.For more details on the BigFoot Project, please visit the website: http://www.fsl.orst.edu/larse/bigfoot/index.html.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BigFoot NPP Surfaces for North and South American Sites, 2000-2004",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/750_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F750",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F750",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/bigfoot_val/NPP_surfaces/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/bigfoot_val/NPP_surfaces/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/NPP_surfaces_750.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/NPP_surfaces_750.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BIGFOOT_VAL/guides/bf_npp_surf_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BIGFOOT_VAL/guides/bf_npp_surf_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/750",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/750",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/NPP_surfaces_750.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/NPP_surfaces_750.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bigfoot_val/LAI_surfaces/comp/bf_npp_surf_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bigfoot_val/LAI_surfaces/comp/bf_npp_surf_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bigfoot_val/LAI_surfaces/comp/BigFoot_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/bigfoot_val/LAI_surfaces/comp/BigFoot_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/750_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/750_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=750",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=750",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/750_1_fit.png",
+            "identifier": "C2751481549-ORNL_CLOUD",
+            "issued": "2023-07-26",
+            "keyword": [
+                "ecological dynamics",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/750",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-156.61 -2.86 -54.96 71.27",
+            "temporal": "2000-01-01T00:00:00Z/2004-12-31T23:59:59Z",
             "theme": [
                 "BigFoot",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BigFoot NPP Surfaces for North and South American Sites, 2000-2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IRRDR-CLEANED-EXT3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Mars Express SPICAM level 1A IR data set contains clean measurements from the infrared SPICAM spectrometer collected during the nominal MARS phases",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-irrdr-cleaned-ext3-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet",
                 "calibration",
@@ -874540,1031 +874542,1031 @@
                 "sky",
                 "deimos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IRRDR-CLEANED-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-irrdr-cleaned-ext3-v1.0",
-            "description": "The Mars Express SPICAM level 1A IR data set contains clean measurements from the infrared SPICAM spectrometer collected during the nominal MARS phases",
-            "title": "MEX EXT3 SPICAM MARS CLEANED IR RDR V1.0",
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
+            "title": "MEX EXT3 SPICAM MARS CLEANED IR RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII%2FHRIV%2FMRI-6-TEMPS-V1.0",
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
-                "deep impact",
-                "9p/tempel 1 (1867 g1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Resampled (raw, averaged) temperature measurements from 27 sensors located in the HRII, HRIV, and MRI instruments and on the HRI and MRI telescopes, instrument platform, and solar wings of the Deep Impact flyby spacecraft. The data begin on 15 January 2005, three days after launch, and continue through 9 July 2005, five days after the encounter with comet 9P/Tempel 1.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-hriv-mri-6-temps-v1.0_hney-8zqi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "deep impact",
+                "9p/tempel 1 (1867 g1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII%2FHRIV%2FMRI-6-TEMPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-hriv-mri-6-temps-v1.0_hney-8zqi",
-            "description": "Resampled (raw, averaged) temperature measurements from 27 sensors located in the HRII, HRIV, and MRI instruments and on the HRI and MRI telescopes, instrument platform, and solar wings of the Deep Impact flyby spacecraft. The data begin on 15 January 2005, three days after launch, and continue through 9 July 2005, five days after the encounter with comet 9P/Tempel 1.",
-            "title": "DEEP IMPACT HRII/HRIV/MRI INSTRUMENT TEMPERATURES V1.0",
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
+            "title": "DEEP IMPACT HRII/HRIV/MRI INSTRUMENT TEMPERATURES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MB2LMT_L1.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-30. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Terra/MISR/MB2LMT_L1.002. https://asdc.larc.nasa.gov/project/MISR.",
-            "issued": "2003-02-13",
-            "temporal": "2000-02-27T00:00:00Z/2022-03-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID, DR. DINER",
                 "hasEmail": "mailto:david.j.diner@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C43677676-LARC",
             "description": "MB2LMT_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 1B2 Local Mode Terrain Radiance Data Version 2 product. It contains the terrain-projected Top-of-Atmosphere (TOA) radiance for the single local mode scene, resampled at the surface and topographically corrected. \r\rMISR itself is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the affects of sunlight on Earth, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 1B2 Local Mode Terrain Radiance Data V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMB2LMT_L1.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMB2LMT_L1.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C43677676-LARC",
-                    "description": "Earthdata Search for MB2LMT_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MB2LMT_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C43677676-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MB2LMT.002/contents.html",
-                    "description": "OPeNDAP data access for MB2LMT_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MB2LMT_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MB2LMT.002/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
-                    "description": "MISR Level 1 Production Report",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Production Report",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/ecs_pge_history_L1_PR.cgi",
+                    "mediaType": "text/html",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
-                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 1 Products Quality Statement - August 29, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L1_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MB2LMT_L1.002",
-                    "description": "DOI data set landing page for MB2LMT_2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MB2LMT_2",
+                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MB2LMT_L1.002",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MB2LMT.002/",
-                    "description": "ASDC Direct Data Download for MB2LMT_2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MB2LMT_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MB2LMT.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/maturity_def.pdf",
-                    "description": "MISR Maturity Level Definitions",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Maturity Level Definitions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/maturity_def.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.html",
-                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Level 1A CCD, 1B1, 1B2, and Browse Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge1.html",
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
-                    "description": "MISR Quality Statements for Current Products",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements for Current Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
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
+            "identifier": "C43677676-LARC",
+            "issued": "2003-02-13",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MB2LMT_L1.002",
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
+            "temporal": "2000-02-27T00:00:00Z/2022-03-30T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 1B2 Local Mode Terrain Radiance Data V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263929262-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "atmosphere",
-                "ocean optics",
-                "earth science",
-                "atmospheric radiation",
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
-            "identifier": "C2263929262-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Sentinel-3A OLCI Level-3B Global Binned Earth-observation Reduced-Resolution (ERR) Inherent Optical Properties (IOP), Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/S3A-OLCI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/S3A-OLCI/",
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
+            "identifier": "C2263929262-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmosphere",
+                "ocean optics",
+                "earth science",
+                "atmospheric radiation",
+                "oceans"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263929262-OB_DAAC.html",
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
+            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3A OLCI Level-3B Global Binned Earth-observation Reduced-Resolution (ERR) Inherent Optical Properties (IOP), Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3307830227-OMINRT.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/OMISIPS.",
-            "issued": "2024-11-22",
-            "temporal": "2018-01-16T00:00:00Z/2024-12-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-22",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/OMISIPS"
-            },
-            "identifier": "C3307830227-OMINRT",
             "description": "Version 2.6 is the current version of this data product, and supersedes all previous versions.The OMPS-N21 L2 LP Ozone (O3) Vertical Profile swath daily Center slit collection contains ozone measured by the Ozone Mapping and Profiling Suite (OMPS) Limb-Profiler (LP) sensor on the NOAA-N21 satellite in Near Real Time (NRT). The LP ozone product measures the vertical distribution of ozone in the stratosphere and lower mesosphere. The algorithm derives ozone profile values along with errors in the UV from 29.5 km and 52.5 km, and in the visible from cloud top to 37.5 km (when there are no clouds the lower limit is 12.5 km). See the README for full description of the product and updated retrieval algorithm.Each granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-90 to  90 degrees latitude), and there are about 14.5 orbits per day, the data from the center of the LP three slits are used to make a vertical profile. The profile is measured from the ground up to about 60 km with a vertical resolution of the retrieved profiles of approximately 1.8 km.The data are written using the Hierarchical Data Format Version 5 or HDF5.",
-            "title": "OMPS-N21 LP NRT L2 LP Ozone (O3) Vertical Profile swath daily Center slit V2.6",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C3307830227-OMINRT.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C3307830227-OMINRT.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C3307830227-OMINRT",
+            "issued": "2024-11-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3307830227-OMINRT.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/OMISIPS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-16T00:00:00Z/2024-12-02T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS-N21 LP NRT L2 LP Ozone (O3) Vertical Profile swath daily Center slit V2.6"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/2A99C60CG7WC",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2TUNPTRB. Version 5.12.4. MERRA-2 tavgU_3d_trb_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/2A99C60CG7WC. https://disc.gsfc.nasa.gov/datacollection/M2TUNPTRB_5.12.4.html. Digital Science Data.",
-            "issued": "2007-06-14",
-            "temporal": "1980-01-01T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-07-07",
-            "references": [
-                "https://doi.org/10.1175/JCLI-D-16-0758.1",
-                "https://doi.org/10.5194/gmd-8-1339-2015",
-                "https://doi.org/10.1175/JCLI-D-16-0609.1",
-                "https://doi.org/10.1175/JCLI-D-16-0613.1",
-                "https://doi.org/10.1175/JCLI-D-16-0570.1",
-                "https://doi.org/10.1175/JCLI-D-16-0720.1",
-                "https://doi.org/NASA/TM\u20132015-104606/Vol. 43",
-                "https://doi.org/10.1177/1094342005056120"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric winds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812934-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2TUNPTRB (or  tavgU_3d_trb_Np) is a 3-dimensional monthly diurnal means data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of turbulence diagnostics on 42 pressure levels, such as total scalar diffusivity, total momentum diffusivity, momentum diffusivity from Louis, and Richardson number from Louis. The information on the pressure levels can be found in the section 4.2 of the MERRA-2 File Specification document.  This data collection is the monthly mean of data fields for each 3-hour and time-stamped at the central time starting from 01:30 UTC, e.g.: 01:30, 04:30, \u2026 , 22:30 UTC.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2TUNPTRB",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2TUNPTRB variable",
-            "title": "MERRA-2 tavgU_3d_trb_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNPTRB) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNPTRB_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2A99C60CG7WC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2A99C60CG7WC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNPTRB_5.12.4.png",
-                    "description": "M2TUNPTRB variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2TUNPTRB variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNPTRB_5.12.4.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=MERRA",
-                    "description": "How to read and plot the data.",
                     "@type": "dcat:Distribution",
+                    "description": "How to read and plot the data.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=MERRA",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TUNPTRB_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2TUNPTRB_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNPTRB.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNPTRB.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TUNPTRB",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2TUNPTRB",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2TUNPTRB.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2TUNPTRB.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2TUNPTRB.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2_DIURNAL/M2TUNPTRB.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation//M2TUNPTRB.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_DIURNAL_aggregation//M2TUNPTRB.5.12.4/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/docs/",
-                    "description": "The GMAO MERRA-2 documentation and FAQs",
                     "@type": "dcat:Distribution",
+                    "description": "The GMAO MERRA-2 documentation and FAQs",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/docs/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf",
-                    "description": "MERRA-2 File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "MERRA-2 File Specification Document",
+                    "downloadURL": "https://gmao.gsfc.nasa.gov/pubs/docs/Bosilovich785.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNPTRB.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2_DIURNAL/M2TUNPTRB.5.12.4/doc/MERRA2.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/mission-project?title=MERRA-2",
-                    "description": "MERRA-2 Data Access \u2013 Quick Start Guide",
                     "@type": "dcat:Distribution",
+                    "description": "MERRA-2 Data Access \u2013 Quick Start Guide",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/mission-project?title=MERRA-2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Records+of+MERRA-2+Data+Reprocessing+and+Service+Changes",
-                    "description": "Records of MERRA-2 Data Reprocessing and Service Changes",
                     "@type": "dcat:Distribution",
+                    "description": "Records of MERRA-2 Data Reprocessing and Service Changes",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Records+of+MERRA-2+Data+Reprocessing+and+Service+Changes",
+                    "mediaType": "text/html",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/faqs?keywords=MERRA-2&page=1",
-                    "description": "FAQs about MERRA-2 data access",
                     "@type": "dcat:Distribution",
+                    "description": "FAQs about MERRA-2 data access",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/faqs?keywords=MERRA-2&page=1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "M2TUNPTRB variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2TUNPTRB_5.12.4.png",
+            "identifier": "C1276812934-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/2A99C60CG7WC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-07-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JCLI-D-16-0758.1",
+                "https://doi.org/10.5194/gmd-8-1339-2015",
+                "https://doi.org/10.1175/JCLI-D-16-0609.1",
+                "https://doi.org/10.1175/JCLI-D-16-0613.1",
+                "https://doi.org/10.1175/JCLI-D-16-0570.1",
+                "https://doi.org/10.1175/JCLI-D-16-0720.1",
+                "https://doi.org/NASA/TM\u20132015-104606/Vol. 43",
+                "https://doi.org/10.1177/1094342005056120"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "M2TUNPTRB",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavgU_3d_trb_Np: 3d,diurnal,Time-Averaged,Pressure-Level,Assimilation,Turbulence Diagnostics 0.625 x 0.5 degree V5.12.4 (M2TUNPTRB) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D80.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D80. Version 001. VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M1 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D80.001. https://doi.org/10.5067/VIIRS/VNP43D80.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "surface radiative properties"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1607353742-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Nadir BRDF-Adjusted Reflectance (NBAR) for Band M1 (VNP43D80) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D80 through VNP43D89 are the NBAR products of the VNP43D BRDF/Albedo product suite. NBAR values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) included in the VNP43MA4 (https://doi.org/10.5067/VIIRS/VNP43MA4.001) product. In addition to the bands included in VNP43MA4, this product suite includes NBAR values for the VIIRS Day/Night Band (DNB). The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon. Details regarding methodology are available on the VNP43MA4 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D80 is the NBAR for VIIRS band M1 (0.412 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D80",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M1 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Nadir BRDF-Adjusted Reflectance (NBAR) for Band M1 (VNP43D80) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D80 through VNP43D89 are the NBAR products of the VNP43D BRDF/Albedo product suite. NBAR values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) included in the VNP43MA4 (https://doi.org/10.5067/VIIRS/VNP43MA4.001) product. In addition to the bands included in VNP43MA4, this product suite includes NBAR values for the VIIRS Day/Night Band (DNB). The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon. Details regarding methodology are available on the VNP43MA4 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D80 is the NBAR for VIIRS band M1 (0.412 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D80.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D80.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
-                    "description": "Product Quality information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Product Quality information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D80.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D80.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D80.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D80.001/",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset through a directory map"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607353742-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607353742-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D80.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D80.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs/viirs_user_guide/vnp43d_cmg_30_arc-second_products",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs/viirs_user_guide/vnp43d_cmg_30_arc-second_products",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D80",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D80",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
-                    "description": "Validation at stage 2 has been achieved for the VIIRS BRDF/Albedo product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 2 has been achieved for the VIIRS BRDF/Albedo product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
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
                 }
             ],
+            "identifier": "C1607353742-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D80.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "VNP43D80",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo NBAR at Solar Noon Band M1 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-VIR-3-RDR-IR-CRUISE-SPECTRA-V1.0",
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
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the spectral      radiance (W/(m**2*sr*micron)) data from the Dawn VIR instrument         IR channel for all cruise mission phases. The data are from the         cruise phase from launch to Vesta (Sep 2009-May 2011), and Vesta        to Ceres (Sep 2012-Dec 2014).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-vir-3-rdr-ir-cruise-spectra-v1.0_hnnk-zify",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-X-VIR-3-RDR-IR-CRUISE-SPECTRA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-x-vir-3-rdr-ir-cruise-spectra-v1.0_hnnk-zify",
-            "description": "This data set contains the spectral      radiance (W/(m**2*sr*micron)) data from the Dawn VIR instrument         IR channel for all cruise mission phases. The data are from the         cruise phase from launch to Vesta (Sep 2009-May 2011), and Vesta        to Ceres (Sep 2012-Dec 2014).",
-            "title": "DAWN VIR CAL (RDR) CRUISE CHECKOUT/CALIB IR SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN VIR CAL (RDR) CRUISE CHECKOUT/CALIB IR SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TNO-PHOT-V2.0",
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
+            "description": "Published colors of Trans-Neptunian objects through December 2001.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-tno-phot-v2.0_hnnm-sjcc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-TNO-PHOT-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-tno-phot-v2.0_hnnm-sjcc",
-            "description": "Published colors of Trans-Neptunian objects through December 2001.",
-            "title": "TRANS-NEPTUNIAN OBJECT PHOTOMETRY V2.0",
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
+            "title": "TRANS-NEPTUNIAN OBJECT PHOTOMETRY V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-J-SAAO-3-EDR-SL9-V1.0",
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
-                "pds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-j-saao-3-edr-sl9-v1.0_hnqh-pbvr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pds"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-J-SAAO-3-EDR-SL9-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-j-saao-3-edr-sl9-v1.0_hnqh-pbvr",
-            "description": "TBD",
-            "title": "SOUTH AFRICAN ASTRON. OBS. IMAGE DATA FROM SL9 IMPACTS",
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
+            "title": "SOUTH AFRICAN ASTRON. OBS. IMAGE DATA FROM SL9 IMPACTS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/856/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jose Celaya Galvan",
                 "hasEmail": "mailto:jose.r.celayagalvan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_856",
             "description": "A remaining useful life prediction methodology for electrolytic capacitors is presented. This methodology is based on the Kalman filter framework and an empirical degradation model. Electrolytic capacitors are used in several applications ranging from power supplies on critical avionics equipment to power drivers for electro-mechanical actuators. These devices are known for their comparatively low reliability and given their criticality in electronics subsystems they are a good candidate for component level prognostics and health management. Prognostics provides a way to assess remaining useful life of a capacitor based on its current state of health and its anticipated future usage and operational conditions. We present here also, experimental results of an accelerated aging test under electrical stresses. The data obtained in this test form the basis for a remaining life prediction algorithm where a model of the degradation process is suggested. This preliminary remaining life prediction algorithm serves as a demonstration of how prognostics methodologies could be used for electrolytic capacitors. In addition, the use degradation progression data from accelerated aging, provides an avenue for validation of applications of the Kalman filter based prognostics methods typically used for remaining useful life predictions in other applications.",
-            "title": "A Model-Based Prognostics Methodology For Electrolytic Capacitors Based On Electrical Overstress Accelerated Aging",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/phmc_11_010.pdf",
-                    "description": "Full paper PDF",
                     "@type": "dcat:Distribution",
+                    "description": "Full paper PDF",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/phmc_11_010.pdf",
+                    "mediaType": "application/pdf",
                     "title": "phmc_11_010.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_856",
+            "issued": "2013-12-12",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/856/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Model-Based Prognostics Methodology For Electrolytic Capacitors Based On Electrical Overstress Accelerated Aging"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-A-FPA-3-RDR-IMPS-V3.0",
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
-                "infrared astronomical satellite",
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The data presented with this data set include: (a) 8210 individual sightings associated with 2004 asteroids, (b) averaged radiometric diameters and geometric albedos derived from individual observations for 1796 numbered asteroids and 88 unnumbered asteroids (as of 1983) whose orbital elements were determined using astrometry from two or more apparitions; (c) an entry for each of 120 asteroids for which there is an accepted sighting; (d) entries for each of 4677 numbered asteroids and 2632 unnumbered asteroids (as of 1985) for which associations were sought in the IRAS data; (e) A summary of the number of times each asteroid was predicted to be scanned, and possible reasons for any failure to be detected.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-a-fpa-3-rdr-imps-v3.0_hnsd-xx6s",
+            "issued": "2018-06-26",
+            "keyword": [
+                "infrared astronomical satellite",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-A-FPA-3-RDR-IMPS-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-a-fpa-3-rdr-imps-v3.0_hnsd-xx6s",
-            "description": "The data presented with this data set include: (a) 8210 individual sightings associated with 2004 asteroids, (b) averaged radiometric diameters and geometric albedos derived from individual observations for 1796 numbered asteroids and 88 unnumbered asteroids (as of 1983) whose orbital elements were determined using astrometry from two or more apparitions; (c) an entry for each of 120 asteroids for which there is an accepted sighting; (d) entries for each of 4677 numbered asteroids and 2632 unnumbered asteroids (as of 1985) for which associations were sought in the IRAS data; (e) A summary of the number of times each asteroid was predicted to be scanned, and possible reasons for any failure to be detected.",
-            "title": "IRAS MINOR PLANET SURVEY ASTEROIDS V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IRAS MINOR PLANET SURVEY ASTEROIDS V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-I0039-2-SBN0007%2FKECKIIESI-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "CCD images of comet 81P/Wild 2 taken 2003 December 19-21 UT with the ESI instrument on Keck II in support of the Stardust encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-i0039-2-sbn0007-keckiiesi-v1.0_hnti-hvn6",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "star",
@@ -875572,69 +875574,45 @@
                 "calibration",
                 "81p/wild 2 (1978 a2)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-I0039-2-SBN0007%2FKECKIIESI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-i0039-2-sbn0007-keckiiesi-v1.0_hnti-hvn6",
-            "description": "CCD images of comet 81P/Wild 2 taken 2003 December 19-21 UT with the ESI instrument on Keck II in support of the Stardust encounter.",
-            "title": "KECK II ESI IMAGES OF 81P/WILD 2",
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
+            "title": "KECK II ESI IMAGES OF 81P/WILD 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2507",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schwartz, M., Livesey, N. and Read, W.. 2020-06-11. ML2GPH. Version 005. MLS/Aura Level 2 Geopotential Height V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2507. https://disc.gsfc.nasa.gov/datacollection/ML2GPH_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
-            "keyword": [
-                "earth science",
-                "altitude",
-                "atmosphere"
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
-            "identifier": "C1729925152-GES_DISC",
-            "description": "ML2GPH is the EOS Aura Microwave Limb Sounder (MLS) standard product for geopotential height derived from radiances measured by the 118 and 240 GHz radiometers. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 261 and 0.001 hPa, and the vertical resolution varies between ~3.6 and 6 km. Users of the ML2GPH data product should read section 3.8 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2GPH",
             "creator": "Schwartz, M., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Geopotential Height V005 (ML2GPH) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2GPH_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2GPH is the EOS Aura Microwave Limb Sounder (MLS) standard product for geopotential height derived from radiances measured by the 118 and 240 GHz radiometers. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 261 and 0.001 hPa, and the vertical resolution varies between ~3.6 and 6 km. Users of the ML2GPH data product should read section 3.8 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2507",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2507",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -875644,109 +875622,112 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2GPH_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2GPH_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2GPH.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2GPH.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2GPH.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2GPH.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2GPH_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2GPH_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2GPH_005.png",
+            "identifier": "C1729925152-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "earth science",
+                "altitude",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2507",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML2GPH",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Geopotential Height V005 (ML2GPH) at GES DISC"
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
-            "identifier": "NASA-721",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (82)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -875754,150 +875735,149 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-721",
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
+            "title": "PDS Odyssey Radio Science Data (82)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0004.",
-            "issued": "1999-10-13",
-            "temporal": "1995-08-01T00:00:00Z/1995-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric water vapor",
-                "earth science",
-                "aerosols"
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
-            "identifier": "C2184041855-LARC_ASDC",
             "description": "SCAR_B_AERONET data are Smoke, Clouds and Radiation Brazil (SCARB) Aerosol Robotic Network (AERONET) data for aerosol characterization.Smoke/Sulfates, Clouds and Radiation - Brazil (SCAR-B) data include physical and chemical components of the Earth's surface, the atmosphere and the radiation field collected in Brazil with an emphasis in biomass burning.The objectives for the SCAR mission are: to advance our knowledge of how the physical, chemical and radiative processes in our atmosphere are affected by sulfate aerosol and smoke from biomass burning; to improve our expertise at remotely sensing smoke, water vapor, clouds, vegetation and fires; and to assess the effects of deforestation and biomass burning on tropical landscapes.AERONET (AErosol RObotic NETwork) is an optical ground based aerosol monitoring network and data archive supported by NASA's Earth Observing System and expanded by federation with many non-NASA institutions. The network hardware consists of identical automatic sun-sky scanning spectral radiometers owned by national agencies and universities. Data from this collaboration provides globally distributed near real time observations of aerosol spectral optical depths, aerosol size distributions, and precipitable water in diverse aerosol regimes. The data undergo preliminary processing (real time data), reprocessing (final calibration ~6 mo. after data collection), quality assurance, archiving and distribution from NASA's Goddard Space Flight Center master archive and several identical data bases maintained globally. The data provide algorithm validation of satellite aerosol retrievals and as well as characterization of aerosol properties that are unavailable from satellite sensors.",
-            "title": "Sulfates, Clouds and Radiation Brazil (SCAR-B) AERONET (AErosol RObotic NETwork) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FSCAR_B%2F0004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FSCAR_B%2F0004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/SCAR-B",
-                    "description": "ASDC Data and Information for SCAR-B",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for SCAR-B",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/SCAR-B",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1337195036-LARC_ASDC",
-                    "description": "Earthdata Search for SCAR_B_AERONET_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SCAR_B_AERONET_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1337195036-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SCAR-B/SCAR_B_AERONET/contents.html",
-                    "description": "OPeNDAP data access for SCAR_B_AERONET_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for SCAR_B_AERONET_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SCAR-B/SCAR_B_AERONET/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0004",
-                    "description": "DOI data set landing page for SCAR_B_AERONET_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for SCAR_B_AERONET_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0004",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/scarb/guide/scar_project.pdf",
-                    "description": "SCAR Langley DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "SCAR Langley DAAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/scarb/guide/scar_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SCAR-B/SCAR_B_AERONET/",
-                    "description": "ASDC Direct Data Download for SCAR_B_AERONET_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SCAR_B_AERONET_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SCAR-B/SCAR_B_AERONET/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/scara/scar_summaries.html",
-                    "description": "ASDC List of MODIS Airborne Simularot (MAS) Flight Line Information by Date",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MODIS Airborne Simularot (MAS) Flight Line Information by Date",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/scara/scar_summaries.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2184041855-LARC_ASDC",
+            "issued": "1999-10-13",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric water vapor",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/SCAR_B/0004",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-20.45 -62.87 -20.45 -47.9 -2.43 -47.9 -2.43 -62.87 -20.45 -62.87</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-08-01T00:00:00Z/1995-09-30T23:59:59.999Z",
             "theme": [
                 "SCAR-B",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sulfates, Clouds and Radiation Brazil (SCAR-B) AERONET (AErosol RObotic NETwork) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://turbmodels.larc.nasa.gov/kkl.html",
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
-                "chien"
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
-            "identifier": "NASA-836",
             "description": "This web page gives detailed information on the equations for various forms of the Chien k-epsilon turbulence model.",
-            "title": "Wilcox k-omega Turbulence Model",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -875905,158 +875885,180 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-836",
+            "issued": "2018-06-25",
+            "keyword": [
+                "models",
+                "turbulence",
+                "chien"
+            ],
+            "landingPage": "http://turbmodels.larc.nasa.gov/kkl.html",
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
+            "title": "Wilcox k-omega Turbulence Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M02-V3.0",
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
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m02-v3.0_hnz9-6kpz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M02-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m02-v3.0_hnz9-6kpz",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 PRL-MTP002 RDR V3.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 PRL-MTP002 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_AircraftInSitu_WB57_Water_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-10-10. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_AircraftInSitu_WB57_Water_Data_1.",
-            "issued": "2022-07-14",
-            "temporal": "2022-07-14T00:00:00Z/2022-09-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Benjamin Clouser",
                 "hasEmail": "mailto:bclouser@uchicago.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2609920136-LARC_ASDC",
             "description": "ACCLIP_AircraftInSitu_WB57_Water_Data is the in-situ water data collection during the Asian Summer Monsoon Chemical & Climate Impact Project (ACCLIP). Data from the Chicago Water Isotope Spectrometer\r\n(ChiWIS) is featured in this collection. Data collection for this product is complete.\r\n\r\nACCLIP is an international, multi-organizational suborbital campaign that aims to study aerosols and chemical transport that is associated with the Asian Summer Monsoon (ASM) in the Western Pacific region from 15 July 2022 to 31 August 2022. The ASM is the largest meteorological pattern in the Northern Hemisphere (NH) during the summer and is associated with persistent convection and large anticyclonic flow patterns in the upper troposphere and lower stratosphere (UTLS). This leads to significant enhancements in the UTLS of trace species that originate from pollution or biomass burning. Convection connected to the ASM occurs over South, Southeast, and East Asia, a region with complex and rapidly changing emissions due to its high population density and economic growth. Pollution that reaches the UTLS from this region can have significant effects on the climate and chemistry of the atmosphere, making it important to have an accurate representation and understanding of ASM transport, chemical, and microphysical processes for chemistry-climate models to characterize these interactions and for predicting future impacts on climate.\r\n\r\nThe ACCLIP campaign is conducted by the National Aeronautics and Space Administration (NASA) and the National Center for Atmospheric Research (NCAR) with the primary goal of investigating the impacts of Asian gas and aerosol emissions on global chemistry and climate. The NASA WB-57 and NCAR G-V aircraft are outfitted with state-of-the-art sensors to accomplish this. ACCLIP seeks to address four scientific objectives related to its main goal. The first is to investigate the transport pathways of ASM uplifted air from inside of the anticyclone to the global UTLS. Another objective is to sample the chemical content of air processed in the ASM in order to quantify the role of the ASM in transporting chemically active species and short-lived climate forcing agents to the UTLS to determine their impact on stratospheric ozone chemistry and global climate. Third, information is obtained on aerosol size, mass, and chemical composition that is necessary for determining the radiative effects of the ASM to constrain models of aerosol formation and for contrasting the organic-rich ASM UTLS aerosol population with that of the background aerosols. Last, ACCLIP seeks to measure the water vapor distribution associated with the monsoon dynamical structure to evaluate transport across the tropopause and determine the role of the ASM in water vapor transport in the stratosphere.",
-            "title": "ACCLIP WB-57 Aircraft Water In-situ Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FACCLIP_AircraftInSitu_WB57_Water_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FACCLIP_AircraftInSitu_WB57_Water_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/acclip/index.html",
-                    "description": "ACCLIP Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ACCLIP Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/acclip/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/acclip/content/ACCLIP",
-                    "description": "ACCLIP ESPO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ACCLIP ESPO Home Page",
+                    "downloadURL": "https://espo.nasa.gov/acclip/content/ACCLIP",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/acclip",
-                    "description": "ACCLIP NCAR Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ACCLIP NCAR Home Page",
+                    "downloadURL": "https://www2.acom.ucar.edu/acclip",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACCLIP/AircraftInSitu_WB57_Water_Data_1/",
-                    "description": "ASDC Direct Data Download for ACCLIP_AircraftInSitu_WB57_Water_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ACCLIP_AircraftInSitu_WB57_Water_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ACCLIP/AircraftInSitu_WB57_Water_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2609920136-LARC_ASDC",
-                    "description": "Earthdata Search for ACCLIP_AircraftInSitu_WB57_Water_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ACCLIP_AircraftInSitu_WB57_Water_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2609920136-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_AircraftInSitu_WB57_Water_Data_1",
-                    "description": "DOI for ACCLIP_AircraftInSitu_WB57_Water_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for ACCLIP_AircraftInSitu_WB57_Water_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_AircraftInSitu_WB57_Water_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2609920136-LARC_ASDC",
+            "issued": "2022-07-14",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACCLIP_AircraftInSitu_WB57_Water_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>16.6 -180.0 16.6 180.0 61.5 180.0 61.5 -180.0 16.6 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2022-07-14T00:00:00Z/2022-09-14T23:59:59.999Z",
             "theme": [
                 "ACCLIP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACCLIP WB-57 Aircraft Water In-situ Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-DDR-APC-LIGHTCURVE-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Asteroid Photometric Catalog (3rd update), Lagerkvist, et.al., 1993 [LAGERKVISTETAL1993], is a compilation of all asteroid lightcurve photometry published up to and including the year 1992. The dataset includes the lightcurves in digital form and a table of references to all original publications.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-ddr-apc-lightcurve-v1.1_hp2e-t72d",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "324 bamberga",
                 "7 iris",
@@ -876760,243 +876762,243 @@
                 "136 austria",
                 "1368 numidia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-DDR-APC-LIGHTCURVE-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-ddr-apc-lightcurve-v1.1_hp2e-t72d",
-            "description": "The Asteroid Photometric Catalog (3rd update), Lagerkvist, et.al., 1993 [LAGERKVISTETAL1993], is a compilation of all asteroid lightcurve photometry published up to and including the year 1992. The dataset includes the lightcurves in digital form and a table of references to all original publications.",
-            "title": "ASTEROID PHOTOMETRIC CATALOG V1.1",
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
+            "title": "ASTEROID PHOTOMETRIC CATALOG V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-4-CR4B-RESAMPLED-V3.0",
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
-                "checkout",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RESAMPLED DATA of the Cruise Phase 4-2, named\nCR4B. Included are the data of the Passive Checkout PC9 from\nJanuary 31, 2009  until February 01 , 2009.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-4-cr4b-resampled-v3.0_hp2k-6u4w",
+            "issued": "2021-05-21",
+            "keyword": [
+                "checkout",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-4-CR4B-RESAMPLED-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-4-cr4b-resampled-v3.0_hp2k-6u4w",
-            "description": "This dataset contains RESAMPLED DATA of the Cruise Phase 4-2, named\nCR4B. Included are the data of the Passive Checkout PC9 from\nJanuary 31, 2009  until February 01 , 2009.",
-            "title": "ROSETTA-ORBITER CHECK RPCMAG 4 CR4B RESAMPLED V3.0",
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
+            "title": "ROSETTA-ORBITER CHECK RPCMAG 4 CR4B RESAMPLED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR19-V1.0",
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
-                "cassini-huygens",
-                "titan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini LGA Radio Science Titan Gravity Science Experiment (TIGR19) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 16, 2015, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr19-v1.0_hp3e-x4hn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR19-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr19-v1.0_hp3e-x4hn",
-            "description": "The Cassini LGA Radio Science Titan Gravity Science Experiment (TIGR19) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 16, 2015, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR19 V1.0",
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
+            "title": "CASSINI RSS RAW DATA SET - TIGR19 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5H12ZX4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Environmental Working Group Joint U.S.-Russian Atlas of the Arctic Ocean, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5H12ZX4.",
-            "issued": "1948-01-01",
-            "temporal": "1948-01-01T00:00:00Z/1993-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1993-12-31",
-            "keyword": [
-                "ocean pressure",
-                "ocean circulation",
-                "earth science",
-                "oceans",
-                "salinity/density",
-                "ocean temperature"
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
-            "identifier": "C1386246245-NSIDCV0",
             "description": "The Environmental Working Group (EWG) was established in June 1995 under the framework of the U.S.-Russian Joint Commission on Economic and Technological Cooperation. In January 1996, the EWG Arctic Climatology Group took on the task of compiling digital data on arctic regions to expand scientific understanding of the Arctic. This work resulted in a set of three atlases on arctic oceanography, sea ice, and meteorology. These atlases are distributed via FTP.\n\nThe Environmental Working Group Joint U.S.-Russian Atlas of the Arctic Ocean was developed by specialists from the Environmental Research Institute of Michigan with Russian and U.S. partners. The Atlas consist of separate volumes for winter and summer, with the following file names G01961a and G01961b respectively. More than 1.3 million individual temperature and salinity observations collected from Russian and western drifting stations, ice breakers, and airborne expeditions were used to develop the products contained in the winter volume. \n\nThe primary products of the Atlas are gridded mean fields for decadal periods (1950s,1960s, 1970s, 1980s) of temperature, salinity, density and dynamic height, Atlantic water layer depth, and temperature and salinity profiles and transects. The original individual observations that were used to derive these fields are not provided with the Atlas and are not available. \n\nNote that the Polar Science Center Hydrographic Climatology (PHC) ocean database (version 3.0) is available from the Polar Science Center, Applied Physics Laboratory, University of Washington. This is a global gridded database with a high quality description of arctic seas achieved by merging data from several sources, including data from the Environmental Working Group Joint U.S.-Russian Atlas of the Arctic Ocean.  The PHC or later versions may be more suitable for your research. Inquires may be sent to: Michael Steele, Applied Physics Laboratory, 1013 NE 40th Street, Seattle, WA 98105",
-            "title": "Environmental Working Group Joint U.S.-Russian Atlas of the Arctic Ocean, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5H12ZX4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5H12ZX4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G01961_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G01961_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/noaa/ewg/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "http://nsidc.org/noaa/ewg/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G01961_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G01961_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/noaa/ewg/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "http://nsidc.org/noaa/ewg/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5H12ZX4",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5H12ZX4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5H12ZX4",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5H12ZX4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246245-NSIDCV0",
+            "issued": "1948-01-01",
+            "keyword": [
+                "ocean pressure",
+                "ocean circulation",
+                "earth science",
+                "oceans",
+                "salinity/density",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5H12ZX4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1993-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 60.0 180.0 90.0",
+            "temporal": "1948-01-01T00:00:00Z/1993-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Environmental Working Group Joint U.S.-Russian Atlas of the Arctic Ocean, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-3-RADCAL-SCI-V2.0",
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
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Mars Exploration Rover 2 Pancam Radiometrically Calibrated Reduced Data Record",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-3-radcal-sci-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-3-RADCAL-SCI-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-3-radcal-sci-v2.0",
-            "description": "Mars Exploration Rover 2 Pancam Radiometrically Calibrated Reduced Data Record",
-            "title": "MER 2 MARS PANCAM RADIOMETRICALLY\n                                   CALIBRATED RDR V2.0",
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
+            "title": "MER 2 MARS PANCAM RADIOMETRICALLY\n                                   CALIBRATED RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-3-VIRS-CDR-CALDATA-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS calibrated observations, also known as CDRs. The MASCS VIRS experiment is a  fixed concave grating spectrograph with a beam splitter that simultaneously disperses the spectrum onto two photodiode arrays.  There are two VIRS CDR data products, one for each array, which  result in coverage of the wavelength ranges of the visible (VIS)  and near infrared (NIR).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-3-virs-cdr-caldata-v1.0_hp6m-96kn",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "messenger",
                 "calibration",
@@ -877004,109 +877006,108 @@
                 "mercury",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-3-VIRS-CDR-CALDATA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-3-virs-cdr-caldata-v1.0_hp6m-96kn",
-            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS calibrated observations, also known as CDRs. The MASCS VIRS experiment is a  fixed concave grating spectrograph with a beam splitter that simultaneously disperses the spectrum onto two photodiode arrays.  There are two VIRS CDR data products, one for each array, which  result in coverage of the wavelength ranges of the visible (VIS)  and near infrared (NIR).",
-            "title": "MESSENGER E/V/H MASCS 3 VIRS\n                                      CALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER E/V/H MASCS 3 VIRS\n                                      CALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AATE4JJ91EHC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge UAF Lidar Scanner L1B Geolocated Surface Elevation Triplets V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/AATE4JJ91EHC.",
-            "issued": "2009-08-19",
-            "temporal": "2009-08-19T00:00:00Z/2020-06-05T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-05",
-            "keyword": [
-                "earth science",
-                "glaciers/ice sheets",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Larsen",
                 "hasEmail": "mailto:Chris.Larsen@gi.alaska.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1000001041-NSIDC_ECS",
             "description": "This data set contains scanning laser altimetry data points of Alaskan glaciers and parts of East and West Antarctica acquired by the airborne University of Alaska Fairbanks (UAF) Glacier Lidar system. The data were collected as part of NASA Operation IceBridge funded campaigns.",
-            "title": "IceBridge UAF Lidar Scanner L1B Geolocated Surface Elevation Triplets V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAATE4JJ91EHC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAATE4JJ91EHC",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILAKS1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILAKS1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001041-NSIDC_ECS&m=-113.0625%2134.875%210%211%210%210%2C2&tl=1528235765%214%21%21&q=ILAKS1B&ok=ILAKS1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001041-NSIDC_ECS&m=-113.0625%2134.875%210%211%210%210%2C2&tl=1528235765%214%21%21&q=ILAKS1B&ok=ILAKS1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILAKS1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILAKS1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AATE4JJ91EHC",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/AATE4JJ91EHC",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AATE4JJ91EHC",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/AATE4JJ91EHC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001041-NSIDC_ECS",
+            "issued": "2009-08-19",
+            "keyword": [
+                "earth science",
+                "glaciers/ice sheets",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AATE4JJ91EHC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2009-08-19T00:00:00Z/2020-06-05T23:59:59.999Z",
             "theme": [
                 "2009_AK_UAF",
                 "2010_AK_UAF",
@@ -877123,52 +877124,29 @@
                 "2020_AK_UAF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge UAF Lidar Scanner L1B Geolocated Surface Elevation Triplets V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2015",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lambert, A., Livesey, N. and Read, W.. 2015-02-19. ML2IWC. Version 004. MLS/Aura Level 2 Cloud Ice Product V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2015. https://disc.gsfc.nasa.gov/datacollection/ML2IWC_004.html. Digital Science Data.",
-            "issued": "2015-02-19",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
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
-            "identifier": "C1251101649-GES_DISC",
-            "description": "ML2IWC is the EOS Aura Microwave Limb Sounder (MLS) standard product for cloud ice water content derived from radiances measured by the 240 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 82.5 hPa, and the vertical resolution is about 3 km. Users of the ML2IWC data product should read sections 3.15 and 3.16 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2IWC",
             "creator": "Lambert, A., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Cloud Ice Product V004 (ML2IWC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2IWC_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2IWC is the EOS Aura Microwave Limb Sounder (MLS) standard product for cloud ice water content derived from radiances measured by the 240 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 82.5 hPa, and the vertical resolution is about 3 km. Users of the ML2IWC data product should read sections 3.15 and 3.16 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2015",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2015",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -877178,690 +877156,691 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2IWC_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2IWC_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2IWC.004/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2IWC.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2IWC.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2IWC.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2IWC_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2IWC_004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/v4-2_data_quality_document.pdf",
-                    "description": "Data Quality and Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality and Description Document",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/v4-2_data_quality_document.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2IWC_004.png",
+            "identifier": "C1251101649-GES_DISC",
+            "issued": "2015-02-19",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2015",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-02-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML2IWC",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Cloud Ice Product V004 (ML2IWC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000540-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 2 Aerosol subset for the ICARTT region;See ProductionDateTime for published Date.",
-            "issued": "2015-09-24",
-            "temporal": "2004-07-31T00:00:00Z/2004-11-02T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-24",
-            "keyword": [
-                "aerosols",
-                "air quality",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C1000000540-LARC",
             "description": "MISR Level 2 Aerosol Product containing aerosol optical depth and particle type, with associated atmospheric data over the ICARTT_2004 theme.",
-            "title": "MISR L2 Aerosol Product subset for the ICARTT region V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000540-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000540-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1000000540-LARC",
+            "issued": "2015-09-24",
+            "keyword": [
+                "aerosols",
+                "air quality",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000540-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-09-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-07-31T00:00:00Z/2004-11-02T23:59:59Z",
             "theme": [
                 "ICARTT_2004",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR L2 Aerosol Product subset for the ICARTT region V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-SW-MAG-4-SUMM-HGCOORDS-1HR-V1.0",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains Voyager 2 magnetometer data from the interplanetary cruise averaged to 1 hour samples in Heliographic coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-sw-mag-4-summ-hgcoords-1hr-v1.0_hpbc-htrn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-SW-MAG-4-SUMM-HGCOORDS-1HR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-sw-mag-4-summ-hgcoords-1hr-v1.0_hpbc-htrn",
-            "description": "This dataset contains Voyager 2 magnetometer data from the interplanetary cruise averaged to 1 hour samples in Heliographic coordinates.",
-            "title": "VOYAGER 2 SOLAR WIND MAGNETIC FIELD HGCOORDS HOUR AVGS V1.0",
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
+            "title": "VOYAGER 2 SOLAR WIND MAGNETIC FIELD HGCOORDS HOUR AVGS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-XYZ-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-xyz-ops-v1.0_hpcy-nsfq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-XYZ-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-xyz-ops-v1.0_hpcy-nsfq",
-            "description": "NULL",
-            "title": "MER 1 MARS NAVIGATION CAMERA\n                                      XYZ RDR OPS V1.0",
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
+            "title": "MER 1 MARS NAVIGATION CAMERA\n                                      XYZ RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3A/OLCI/L2/ERR/IOP/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3A/OLCI/L2/ERR/IOP/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "atmosphere",
-                "ocean optics",
-                "atmospheric radiation"
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
-            "identifier": "C2250401098-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3A OLCI Level-2 Earth-observation Reduced-Resolution (ERR) Inherent Optical Properties (IOP) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3A%2FOLCI%2FL2%2FERR%2FIOP%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3A%2FOLCI%2FL2%2FERR%2FIOP%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "identifier": "C2250401098-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "atmosphere",
+                "ocean optics",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3A/OLCI/L2/ERR/IOP/2022",
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
+            "temporal": "2016-04-25T00:00:00Z/2024-04-22T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3A OLCI Level-2 Earth-observation Reduced-Resolution (ERR) Inherent Optical Properties (IOP) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D75.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D75. Version 001. VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M11 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D75.001. https://doi.org/10.5067/VIIRS/VNP43D75.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
-                "land surface"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1607345704-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo white-sky albedo for band M11 (VNP43D75) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D75 is the WSA for VIIRS band M11 (2.25 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D75",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M11 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo white-sky albedo for band M11 (VNP43D75) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D75 is the WSA for VIIRS band M11 (2.25 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D75.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D75.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
-                    "description": "Product Quality information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Product Quality information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D75.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D75.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D75.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D75.001/",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset through a directory map"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607345704-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607345704-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D75.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D75.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs/viirs_user_guide/vnp43d_cmg_30_arc-second_products",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs/viirs_user_guide/vnp43d_cmg_30_arc-second_products",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D75",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D75",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
-                    "description": "Validation at stage 2 has been achieved for the VIIRS BRDF/Albedo product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 2 has been achieved for the VIIRS BRDF/Albedo product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/Albedo_Val.html",
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
                 }
             ],
+            "identifier": "C1607345704-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D75.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "VNP43D75",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M11 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acorss_titan_ionosphere&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Cassini radio occultations of the Titan ionosphere",
+            "identifier": "urn:nasa:pds:corss_titan_ionosphere",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "cassini orbiter rss titan",
                 "cassini",
                 "titan"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acorss_titan_ionosphere&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:corss_titan_ionosphere",
-            "description": "Cassini radio occultations of the Titan ionosphere",
-            "title": "Titan Ionosphere Bundle",
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
+            "title": "Titan Ionosphere Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0890-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-11T15:05:15.000 to 2015-07-11T17:41:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0890-v1.0_hpft-mfes",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0890-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0890-v1.0_hpft-mfes",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-11T15:05:15.000 to 2015-07-11T17:41:57.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0890 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0890 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-SSP00",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Drushka, K., E. Thompson and W. Asher. 2019-10-24. SPURS-2 Towed surface salinity profile (SSP) data for the E. Tropical Pacific R/V Revelle cruises. Version 1.0. SPURS-2 Field Campaign Surface Salinity Profiler Data Products. APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-SSP00. http://podaac.jpl.nasa.gov/SPURS. Drushka, K., E. Thompson and W. Asher, SPURS Data Management PI, Fred Bingham, 2019-10-24, SPURS-2 Towed surface salinity profile (SSP) data for the E. Tropical Pacific R/V Revelle cruises, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-10-09",
-            "temporal": "2016-08-27T07:52:23Z/2017-11-11T07:35:01Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-09",
-            "keyword": [
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
-                "ocean circulation",
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
-            "identifier": "C2491772351-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. The towed Surface Salinity Profiler (SSP) platform is a converted paddleboard with a keel and surfboard outrigger that is tethered to the ship and skims the sea surface beyond the ships wake. Below the paddleboard are salinity and temperature sensors at depths of 10, 30, 50 and 100cm, and microstructure sensors that measure turbulence. The SSP was deployed 19 times throughout the first SPURS-2 cruise, totaling over 200 hours of measurements, and a further 15 times during the 2017 cruise.  SSP deployment is most informative when there is a rain event leading to near-surface ocean stratification. The SSP then measures how the ocean changes over the periods before, during, and after rain, and how rainwater mixes into the ocean during recovery. All SSP data files are in netCDF format with standards compliant metadata.",
-            "release-place": "APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA",
-            "series-name": "SPURS-2 Towed surface salinity profile (SSP) data for the E. Tropical Pacific R/V Revelle cruises",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Drushka, K., E. Thompson and W. Asher",
-            "title": "SPURS-2 Towed surface salinity profile (SSP) data for the E. Tropical Pacific R/V Revelle cruises",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_SSP.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. The towed Surface Salinity Profiler (SSP) platform is a converted paddleboard with a keel and surfboard outrigger that is tethered to the ship and skims the sea surface beyond the ships wake. Below the paddleboard are salinity and temperature sensors at depths of 10, 30, 50 and 100cm, and microstructure sensors that measure turbulence. The SSP was deployed 19 times throughout the first SPURS-2 cruise, totaling over 200 hours of measurements, and a further 15 times during the 2017 cruise.  SSP deployment is most informative when there is a rain event leading to near-surface ocean stratification. The SSP then measures how the ocean changes over the periods before, during, and after rain, and how rainwater mixes into the ocean during recovery. All SSP data files are in netCDF format with standards compliant metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-SSP00",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-SSP00",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
-                    "description": "Data Submission Report, Instrument Calibration Report, etc",
                     "@type": "dcat:Distribution",
+                    "description": "Data Submission Report, Instrument Calibration Report, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://spurs.jpl.nasa.gov/",
-                    "description": "Project Website for SPURS",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for SPURS",
+                    "downloadURL": "http://spurs.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
-                    "description": "Field Campaign and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_SSP.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_SSP.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772351-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772351-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772351-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772351-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_SSP.jpg",
+            "identifier": "C2491772351-POCLOUD",
+            "issued": "2019-10-09",
+            "keyword": [
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "ocean circulation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-SSP00",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "APL, University of Washington, 1013 NE 40th St, Seattle, WA 98105, USA",
+            "series-name": "SPURS-2 Towed surface salinity profile (SSP) data for the E. Tropical Pacific R/V Revelle cruises",
             "spatial": "-140.969 6.546 -123.203 16.502",
+            "temporal": "2016-08-27T07:52:23Z/2017-11-11T07:35:01Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 Towed surface salinity profile (SSP) data for the E. Tropical Pacific R/V Revelle cruises"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HOOSSU1KAQUT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Soil Climate Analysis Network (SCAN): Alabama, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/HOOSSU1KAQUT.",
-            "issued": "2003-06-01",
-            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-31",
-            "keyword": [
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "agriculture",
-                "atmospheric winds",
-                "earth science",
-                "precipitation",
-                "soils",
-                "atmosphere"
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
-            "identifier": "C1386204209-NSIDCV0",
             "description": "This data set includes soil moisture measurements for the Georgia study region and is part of the Soil Moisture Experiment 2003 (SMEX03).",
-            "title": "SMEX03 Soil Climate Analysis Network (SCAN): Alabama, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHOOSSU1KAQUT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHOOSSU1KAQUT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/SCAN/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/SCAN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/SCAN/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Alabama/ground_soil_moisture/SCAN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HOOSSU1KAQUT",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/HOOSSU1KAQUT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HOOSSU1KAQUT",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/HOOSSU1KAQUT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204209-NSIDCV0",
+            "issued": "2003-06-01",
+            "keyword": [
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "agriculture",
+                "atmospheric winds",
+                "earth science",
+                "precipitation",
+                "soils",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/HOOSSU1KAQUT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-87.0 34.43 -86.1 35.13",
+            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Soil Climate Analysis Network (SCAN): Alabama, Version 1"
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
-                "knowledge",
-                "ask the academy",
-                "appel"
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
-            "identifier": "NASA-862__49",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -877869,202 +877848,237 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__49",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "knowledge",
+                "ask the academy",
+                "appel"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCLAP-2-AST1-EDITED2-V1.0",
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
-                "2867 steins",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the STEINS FLY-BY mission\nphase where the primary target was the asteroid 2867 STEINS. It contains\nuncalibrated raw data, i.e. the digital output of the instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpclap-2-ast1-edited2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "2867 steins",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCLAP-2-AST1-EDITED2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpclap-2-ast1-edited2-v1.0",
-            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the STEINS FLY-BY mission\nphase where the primary target was the asteroid 2867 STEINS. It contains\nuncalibrated raw data, i.e. the digital output of the instrument.",
-            "title": "ROSETTA-ORBITER STEINS\nRPCLAP 2 AST1 EDITED2 V1.0",
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
+            "title": "ROSETTA-ORBITER STEINS\nRPCLAP 2 AST1 EDITED2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/371",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Valentine, D. 1998. BOREAS TF-11 CO2 and CH4 Flux Data from the SSA-Fen. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/371",
-            "issued": "2023-11-22",
-            "temporal": "1994-06-08T00:00:00Z/1994-09-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "soils",
-                "ground water",
-                "earth science",
-                "land surface",
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
-            "identifier": "C2808131130-ORNL_CLOUD",
             "description": "Contains CH4 and CO2 static chamber fluxes at the SSA-FEN.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-11 CO2 and CH4 Flux Data from the SSA-Fen",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F371",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F371",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf11flux/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf11flux/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF11_CH4_CO2_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF11_CH4_CO2_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/371",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/371",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11flux/comp/tf11flux.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11flux/comp/tf11flux.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11flux/comp/TF11_CH4_CO2_Flux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11flux/comp/TF11_CH4_CO2_Flux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11flux/comp/TF11_CH4_CO2_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11flux/comp/TF11_CH4_CO2_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11flux/comp/TF11_CH4_CO2_Flux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11flux/comp/TF11_CH4_CO2_Flux.txt",
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
+            "identifier": "C2808131130-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "soils",
+                "ground water",
+                "earth science",
+                "land surface",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/371",
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
             "spatial": "53.8 -104.62",
+            "temporal": "1994-06-08T00:00:00Z/1994-09-15T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-11 CO2 and CH4 Flux Data from the SSA-Fen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-S-CRS-3-ENC-15.0MIN-V1.0",
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
-                "pioneer 11",
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-s-crs-3-enc-15.0min-v1.0_hpsf-2zsi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "pioneer 11",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-S-CRS-3-ENC-15.0MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-s-crs-3-enc-15.0min-v1.0_hpsf-2zsi",
-            "description": "not applicable",
-            "title": "P11 CRS 15 MINUTE SATURN ENCOUNTER DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "P11 CRS 15 MINUTE SATURN ENCOUNTER DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/hpte-qe5p",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Mice were flown onboard STS-135 and returned to Earth for analysis. Livers were collected within 3-4 hours of landing and snap frozen in liquid nitrogen. Samples were shipped to UCI Genomics High Throughput Facility for analysis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-25",
+                    "mediaType": "text/html",
+                    "title": "STS-135 Liver Transcriptomics"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-25_hpte-qe5p",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample collection",
                 "labeling",
@@ -878075,277 +878089,242 @@
                 "space flight",
                 "nucleic acid hybridization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/hpte-qe5p",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-25_hpte-qe5p",
-            "description": "Mice were flown onboard STS-135 and returned to Earth for analysis. Livers were collected within 3-4 hours of landing and snap frozen in liquid nitrogen. Samples were shipped to UCI Genomics High Throughput Facility for analysis.",
-            "title": "STS-135 Liver Transcriptomics",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-25",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "STS-135 Liver Transcriptomics"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STS-135 Liver Transcriptomics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M06-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-08-01 to 2014-09-02.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m06-v1.0_hpv4-a48m",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-PRL-67PCHURYUMOV-M06-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-prl-67pchuryumov-m06-v1.0_hpv4-a48m",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-08-01 to 2014-09-02.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 006 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 3 RDR MTP 006 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H42R3PMN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seirup, L., and G. Yetman. 2006-05-31. U.S. Census Grids (Summary File 3), 2000. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H42R3PMN. https://doi.org/10.7927/H42R3PMN.",
-            "issued": "2006-05-31",
-            "temporal": "2000-04-01T00:00:00Z/2000-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2006-05-31",
-            "references": [
-                "https://doi.org/10.7927/H4JS9NC2"
-            ],
-            "keyword": [
-                "earth science",
-                "population",
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
-            "identifier": "C179001956-SEDAC",
-            "description": "The U.S. Census Grids (Summary File 3), 2000 data set contains grids of demographic and socioeconomic data from the year 2000 U.S. census in ASCII and GeoTIFF  formats. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 2000 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Seirup, L., and G. Yetman",
-            "title": "U.S. Census Grids (Summary File 3), 2000",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The U.S. Census Grids (Summary File 3), 2000 data set contains grids of demographic and socioeconomic data from the year 2000 U.S. census in ASCII and GeoTIFF  formats. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 2000 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH42R3PMN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH42R3PMN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file3-2000/poverty-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file3-2000/poverty-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file3-2000/maps",
+            "identifier": "C179001956-SEDAC",
+            "issued": "2006-05-31",
+            "keyword": [
+                "earth science",
+                "population",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H42R3PMN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2006-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4JS9NC2"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 17.0 -65.0 72.0",
+            "temporal": "2000-04-01T00:00:00Z/2000-04-01T00:00:00Z",
             "theme": [
                 "USCG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. Census Grids (Summary File 3), 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-3-EAR1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 3 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first earth swing-by phase of the Rosetta mission, which occurred 2004-10-17 to 2005-04-04.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-3-ear1-v1.0_hpz6-hrcw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "international rosetta mission",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-3-EAR1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-3-ear1-v1.0_hpz6-hrcw",
-            "description": "This data set contains CODMAC level 3 instrument checkout data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the first earth swing-by phase of the Rosetta mission, which occurred 2004-10-17 to 2005-04-04.",
-            "title": "ROSETTA-ORBITER CAL ALICE 3 EAR1 V1.0",
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
+            "title": "ROSETTA-ORBITER CAL ALICE 3 EAR1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0422-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-11T14:48:05.000 to 2014-11-12T03:03:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0422-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0422-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0422-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-11T14:48:05.000 to 2014-11-12T03:03:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0422 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0422 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/archives/past-issues/",
+            "accrualPeriodicity": "R/P3M",
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
-                "knowledge",
-                "sharing",
-                "appel",
-                "ask magazine"
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
-            "identifier": "NASA-860__18",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -878353,649 +878332,682 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__18",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge",
+                "sharing",
+                "appel",
+                "ask magazine"
+            ],
+            "landingPage": "http://appel.nasa.gov/archives/past-issues/",
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
+            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-L-NIMS-3-TUBE-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-l-nims-3-tube-v1.0_hqaw-9dvz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-L-NIMS-3-TUBE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-l-nims-3-tube-v1.0_hqaw-9dvz",
-            "description": "Unknown",
-            "title": "NIMS SPECTRAL IMAGE TUBES OF THE MOON: E1 & E2 ENCOUNTERS",
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
+            "title": "NIMS SPECTRAL IMAGE TUBES OF THE MOON: E1 & E2 ENCOUNTERS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0032",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2010-11-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0032.",
-            "issued": "2013-11-18",
-            "temporal": "2001-03-14T00:00:00Z/2003-06-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols"
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
-            "identifier": "C2338659926-LARC_ASDC",
             "description": "NARSTO_EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Los Angeles Harvard/EPA Annular Denuder System (HEADS) Data product. This product was collected between December 2001 and June 2003. The HEADS model URG-2000-30DI was used to collect the Particulate Matter (PM) 2.5 mass concentration data episodically from December 6, 2001 - August 21, 2002. It was also used to collect sulfate and nitrate ions at Claremont from September 28, 2001 - August 6, 2002, at Riverside from March 14 - June 6 2001, and the University of Southern California from October 8, 2002 - June 11, 2003. HEADS uses chemically coated annular denuder tubes to selectively remove gaseous pollutants before PM. The overall objective of the Los Angeles Supersite in Southern California Particle Center and Supersite (SCPCS) was to conduct monitoring and research that contributes to a better understanding of the measurement, sources, size distribution, chemical composition and physical state, spatial and temporal variability, and linkages to health effects of airborne particulate matter in the Los Angeles Basin (LAB). The EPA PM Supersites Program was an ambient air monitoring research program designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. \r\n\r\nEight geographically diverse projects were chosen to specifically address these EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Los Angeles Harvard/EPA Annular Denuder System (HEADS) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0032",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0032",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2338659926-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2338659926-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0032",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0032",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_los_angeles_heads_part_ions_mass.pdf",
-                    "description": "Guide for NARSTO EPA_SS_LOS_ANGELES PM2.5 Composition and Mass Data (HEADS)",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_LOS_ANGELES PM2.5 Composition and Mass Data (HEADS)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_los_angeles_heads_part_ions_mass.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Los_Angeles_Final_Report.pdf",
-                    "description": "Executive Summary for the Southern California Supersite (EPA: CR-82805901) Final Report \u2013 March 30, 2005",
                     "@type": "dcat:Distribution",
+                    "description": "Executive Summary for the Southern California Supersite (EPA: CR-82805901) Final Report \u2013 March 30, 2005",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Los_Angeles_Final_Report.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_LOS_ANGELES_HEADS_PART_IONS_MASS_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2338659926-LARC_ASDC",
+            "issued": "2013-11-18",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0032",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>33.96 -117.72 33.96 -117.33 34.13 -117.33 34.13 -117.72 33.96 -117.72</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2001-03-14T00:00:00Z/2003-06-11T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Los Angeles Harvard/EPA Annular Denuder System (HEADS) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-GST-3-RDR-GEOGRAPHOS-RADAR-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Delay-Doppler images and continuous wave, dual-polarization spectra of 1620 Geographos taken during the August 1994 closest approach to Earth (0.0333AU at minimum).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-gst-3-rdr-geographos-radar-v1.1_hqdv-wcqf",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "1620 geographos",
                 "geographos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-GST-3-RDR-GEOGRAPHOS-RADAR-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-gst-3-rdr-geographos-radar-v1.1_hqdv-wcqf",
-            "description": "Delay-Doppler images and continuous wave, dual-polarization spectra of 1620 Geographos taken during the August 1994 closest approach to Earth (0.0333AU at minimum).",
-            "title": "GEOGRAPHOS RADAR V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GEOGRAPHOS RADAR V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331490676-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ngda",
-                "earth science",
-                "oceans",
-                "ocean chemistry",
-                "national geospatial data asset"
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
-            "identifier": "C2331490676-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Terra MODIS Global Mapped Particulate Inorganic Carbon (PIC) - Near Real Time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/Terra-MODIS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Mapped/Terra-MODIS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/PIC/2022",
-                    "description": "MODIS-Terra L3M Particulate Inorganic Carbon (PIC) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3M Particulate Inorganic Carbon (PIC) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/PIC/2022",
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
+            "identifier": "C2331490676-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ngda",
+                "earth science",
+                "oceans",
+                "ocean chemistry",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331490676-OB_DAAC.html",
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
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS Global Mapped Particulate Inorganic Carbon (PIC) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/CATS/L1B_D-M7.1-V3-00",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/CATS/L1B_D-M7.1-V3-00. https://asdc.larc.nasa.gov/project/CATS-ISS.",
-            "issued": "2018-08-13",
-            "temporal": "2015-02-10T00:00:00Z/2015-03-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-13",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science",
-                "aerosols"
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
-            "identifier": "C1587325115-LARC_ASDC",
             "description": "CATS-ISS_L1B_D-M7.1-V3-00 is the Cloud-Aerosol Transport System (CATS) International Space Station (ISS) Level 1B Day Mode 7.1 Version 3-00 data product. The collection spans from February 10, 2015 through March 21, 2015. CATS, which was launched on January 10, 2015, was a lidar remote sensing instrument that provided range-resolved profile measurements of atmospheric aerosols and clouds from the ISS. CATS was intended to operate on-orbit for up to three years. CATS provides vertical profiles at three wavelengths, orbiting between ~230 and ~270 miles above the Earth's surface at a 51-degree inclination with nearly a three-day repeat cycle. For the first time, scientists were able to study diurnal (day-to-night) changes in cloud and aerosol effects from space by observing the same spot on Earth at different times each day. Level 1B data have been calibrated and annotated with ancillary meteorological data and processed to sensor units.",
-            "graphic-preview-description": "CATS Browse and Granule Availability",
-            "title": "CATS-ISS Level 1B Day Mode 7.1 Version 3-00",
-            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL1B_D-M7.1-V3-00",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
```

