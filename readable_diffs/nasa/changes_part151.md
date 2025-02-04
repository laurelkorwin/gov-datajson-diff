# Change History for nasa.json (Part 151)

### Changes from 31606f9 to dd2190f (Part 140/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://subset.larc.nasa.gov/tes/login.php",
-                    "description": "TES Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "TES Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/tes/login.php",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 }
             ],
+            "identifier": "C1331182615-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "earth science",
+                "air quality",
+                "atmosphere",
+                "clouds",
+                "atmospheric temperature",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2CO2N_L2.007",
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
+            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L2 Carbon Dioxide Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L4B/GSM/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L4B/GSM/2022.",
-            "issued": "2023-11-16",
-            "temporal": "1997-09-04T00:00:00Z/2010-12-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-16",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C2802700401-OB_DAAC",
             "description": "The SeaWiFS instrument was launched by Orbital Sciences Corporation on the OrbView-2 (a.k.a. SeaStar) satellite in August 1997, and collected data from September 1997 until the end of mission in December 2010. SeaWiFS had 8 spectral bands from 412 to 865 nm. It collected global data at 4 km resolution, and local data (limited onboard storage and direct broadcast) at 1 km. The mission and sensor were optimized for ocean color measurements, with a local noon (descending) equator crossing time orbit, fore-and-aft tilt capability, full dynamic range, and low polarization sensitivity.",
-            "title": "OrbView-2 SeaWiFS 4B Global Binned Garver-Siegel-Maritorena Model (GSM) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FORBVIEW-2%2FSeaWiFS%2FL4B%2FGSM%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FORBVIEW-2%2FSeaWiFS%2FL4B%2FGSM%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-4%20Binned/SeaWiFS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-4%20Binned/SeaWiFS/",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ORBVIEW-2/SeaWiFS/L4B/GSM/2022",
-                    "description": "OrbView-2 SeaWiFS Level-4B Garver-Siegel-Maritorena Model (GSM) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OrbView-2 SeaWiFS Level-4B Garver-Siegel-Maritorena Model (GSM) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ORBVIEW-2/SeaWiFS/L4B/GSM/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2802700401-OB_DAAC",
+            "issued": "2023-11-16",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L4B/GSM/2022",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-16",
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
+            "title": "OrbView-2 SeaWiFS 4B Global Binned Garver-Siegel-Maritorena Model (GSM) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-RDR-HGCOORDS-9.60SEC-V1.0",
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
+            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data given in Heliographic coordinates and averaged from the 60 ms instrument sample rate to a 9.6 second resampled rate. The data set consists of the following columns: 1) UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock (m65536:mod60:fds-line), 3) magnetometer id (1 = LFM, 2 = HFM), 4) Br (radial, Sun to spacecraft, B-field component), 5) Bt (azimuthal B-field component, positive in the direction of planetary orbital motion), 6) Bn (North/South B-field component, positive northward), 7) Bmag (magnitude of the averaged components), 8) avg_Bmag (average of the magnetic field magnitudes), 9) delta (latitude = arcsin(Bn/Bmag)), 10) lambda (longitude = 180. - atan(Bt/Br)), 11-13) rms vectors, 14) npts (number of points in average). All magnetic field observations are measured in nanoTesla. All of the magnetic field data are calibrated (see the instrument calibration description for more details).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-rdr-hgcoords-9.60sec-v1.0_ujn6-cyty",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-RDR-HGCOORDS-9.60SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-rdr-hgcoords-9.60sec-v1.0_ujn6-cyty",
-            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data given in Heliographic coordinates and averaged from the 60 ms instrument sample rate to a 9.6 second resampled rate. The data set consists of the following columns: 1) UT of the sample in the format yyyy-mm-ddThh:mm:ss.sssZ, 2) spacecraft clock (m65536:mod60:fds-line), 3) magnetometer id (1 = LFM, 2 = HFM), 4) Br (radial, Sun to spacecraft, B-field component), 5) Bt (azimuthal B-field component, positive in the direction of planetary orbital motion), 6) Bn (North/South B-field component, positive northward), 7) Bmag (magnitude of the averaged components), 8) avg_Bmag (average of the magnetic field magnitudes), 9) delta (latitude = arcsin(Bn/Bmag)), 10) lambda (longitude = 180. - atan(Bt/Br)), 11-13) rms vectors, 14) npts (number of points in average). All magnetic field observations are measured in nanoTesla. All of the magnetic field data are calibrated (see the instrument calibration description for more details).",
-            "title": "VG2 JUP MAG RESAMPLED HELIOGRAPHIC (RTN)\n    COORDS 9.60SEC V1.0",
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
+            "title": "VG2 JUP MAG RESAMPLED HELIOGRAPHIC (RTN)\n    COORDS 9.60SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-4-MARS-MARS-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-4-mars-mars-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phobos",
                 "vega",
@@ -1472535,1344 +1472537,1344 @@
                 "21 lutetia",
                 "16 cyg b"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-4-MARS-MARS-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-4-mars-mars-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER MARS OSIWAC 4 MARS RDR-STRLIGHT V1.0",
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
+            "title": "ROSETTA-ORBITER MARS OSIWAC 4 MARS RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PREFIRE-SAT1/PREFIRE/PAYLOAD_L0.R01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "PREFIRE_SAT1_0-PAYLOAD. Version R01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/PREFIRE-SAT1/PREFIRE/PAYLOAD_L0.R01. https://asdc.larc.nasa.gov/project/PREFIRE/PREFIRE_SAT1_0-PAYLOAD_R01.",
-            "issued": "2024-06-07",
-            "temporal": "2024-06-01T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-30",
-            "references": [
-                "https://doi.org/10.1175/BAMS-D-20-0155.1"
-            ],
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Erin Hokanson Wagner",
                 "hasEmail": "mailto:prefire-sdps.admin@office365.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C3255933578-LARC_CLOUD",
             "description": "Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 1 Raw Payload (PREFIRE_SAT1_0-PAYLOAD) contains the uncurated raw measurements from one of two PREFIRE Thermal Infrared Spectrometers (TIRS-PREFIRE), which is a push broom spectrometer with 63 channels measuring mid- and far-infrared (FIR) radiation from approximately 5 to 53 \u00b5m. Most polar emissions are in the FIR but have not been measured on a large scale. PREFIRE aims to fill knowledge gaps in the global energy budget by more accurately characterizing polar emissions. This information will then be assimilated into global circulation and other climate models to predict future climates more accurately.\r\n\r\nThis collection contains the raw and uncurated digital number counts for TIRS-PREFIRE aboard PREFIRE Satellite 1 (PREFIRE-SAT1). Data retrieval started in May TBD, 2024, and is ongoing. Geographic coverage is global, with the greatest concentration of data in the polar regions. This data has a temporal resolution of 0.707 seconds and is available in binary format.\r\n\r\nRaw, uncurated digital number counts for the sister instrument aboard PREFIRE-SAT2 can be found in the PREFIRE_SAT2_0-PAYLOAD collection.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 1 Raw Payload R01",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/prefire.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPREFIRE-SAT1%2FPREFIRE%2FPAYLOAD_L0.R01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPREFIRE-SAT1%2FPREFIRE%2FPAYLOAD_L0.R01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/prefire.png",
-                    "description": "Mission Logo",
                     "@type": "dcat:Distribution",
+                    "description": "Mission Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/prefire.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/PREFIRE",
-                    "description": "PREFIRE Data Set Landing Page ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "PREFIRE Data Set Landing Page ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/PREFIRE",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science.jpl.nasa.gov/projects/prefire/",
-                    "description": "NASA JPL PREFIRE Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL PREFIRE Project Page",
+                    "downloadURL": "https://science.jpl.nasa.gov/projects/prefire/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://prefire.ssec.wisc.edu/",
-                    "description": "University of Wisconsin PREFIRE Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "University of Wisconsin PREFIRE Project Page",
+                    "downloadURL": "https://prefire.ssec.wisc.edu/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science.nasa.gov/mission/prefire/",
-                    "description": "NASA PREFIRE Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA PREFIRE Project Page",
+                    "downloadURL": "https://science.nasa.gov/mission/prefire/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PREFIRE-SAT1/PREFIRE/PAYLOAD_L0.R01",
-                    "description": "DOI data set landing page for PREFIRE_SAT1_0-PAYLOAD_R01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for PREFIRE_SAT1_0-PAYLOAD_R01",
+                    "downloadURL": "https://doi.org/10.5067/PREFIRE-SAT1/PREFIRE/PAYLOAD_L0.R01",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3255933578-LARC_CLOUD",
-                    "description": "Earthdata Search for PREFIRE_SAT1_0-PAYLOAD_R01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for PREFIRE_SAT1_0-PAYLOAD_R01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3255933578-LARC_CLOUD",
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
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/prefire.png",
+            "identifier": "C3255933578-LARC_CLOUD",
+            "issued": "2024-06-07",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/PREFIRE-SAT1/PREFIRE/PAYLOAD_L0.R01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
+            "references": [
+                "https://doi.org/10.1175/BAMS-D-20-0155.1"
+            ],
             "spatial": "-180.0 -84.0 180.0 84.0",
+            "temporal": "2024-06-01T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "PREFIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Polar Radiant Energy in the Far InfraRed Experiment (PREFIRE) Satellite 1 Raw Payload R01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYDBMSS.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Aqua Atmosphere BELMANIP Subsetting Product. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MYDBMSS.061. https://doi.org/10.5067/MODIS/MYDBMSS.061.",
-            "issued": "2017-10-01",
-            "temporal": "2002-07-04T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-10",
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering",
-                "national geospatial data asset",
-                "ngda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASAD ULLAH",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1444780364-LAADS",
-            "description": "The MODIS/Aqua Atmosphere BELMANIP subsetting Product (MYDBMSS) consists of MODIS Atmosphere and Ancillary Products subsets that are generated over the Bench-mark Land Multisite Analysis and Intercomparison of Products (BELMANIP) sites. The BELMANIP sites is a network of sites, distributed globally and consist of existing networks such as Earth Observing System (EOS) Core Sites, Bigfoot, Validation of Land European Remote sensing Instruments (VALERI), a global network of micrometeorological flux measurement (FLUXNET), the aerosol robotic network (AERONET) and a set of additional sites.The process of generating cutouts for these sites involves locating and identifying a subset of sites taken from global BELMANIP sites that are within the spatial coverage of a 5 minute Level 2 MODIS granule and extracting 0.5 x 0.5 degree cutouts. The MODBMSS data set consists of subsets for approximately 445 sites around the globe. There is one file per site with 55 Science Data Sets (SDS) such as at-aperture radiances for 36 discrete MODIS bands, Cloud Mask, and Water Vapor, etc.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Atmosphere BELMANIP Subsetting Product",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Atmosphere BELMANIP subsetting Product (MYDBMSS) consists of MODIS Atmosphere and Ancillary Products subsets that are generated over the Bench-mark Land Multisite Analysis and Intercomparison of Products (BELMANIP) sites. The BELMANIP sites is a network of sites, distributed globally and consist of existing networks such as Earth Observing System (EOS) Core Sites, Bigfoot, Validation of Land European Remote sensing Instruments (VALERI), a global network of micrometeorological flux measurement (FLUXNET), the aerosol robotic network (AERONET) and a set of additional sites.The process of generating cutouts for these sites involves locating and identifying a subset of sites taken from global BELMANIP sites that are within the spatial coverage of a 5 minute Level 2 MODIS granule and extracting 0.5 x 0.5 degree cutouts. The MODBMSS data set consists of subsets for approximately 445 sites around the globe. There is one file per site with 55 Science Data Sets (SDS) such as at-aperture radiances for 36 discrete MODIS bands, Cloud Mask, and Water Vapor, etc.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDBMSS.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDBMSS.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDBMSS.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDBMSS.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDBMSS--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDBMSS--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDBMSS/",
-                    "description": "Direct access to MYDBMSS C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MYDBMSS C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDBMSS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDBMSS/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDBMSS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1444780364-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "infrared wavelengths",
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYDBMSS.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Atmosphere BELMANIP Subsetting Product"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/AST_L1T.031",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA LP DAAC. 2021-07-07. AST_L1T.031. ASTER Level 1 Precision Terrain Corrected Registered At-Sensor Radiance V031. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ASTER/AST_L1T.031. https://doi.org/10.5067/ASTER/AST_L1T.031. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-07-07",
-            "temporal": "2000-03-04T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-07",
-            "keyword": [
-                "national geospatial data asset",
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths",
-                "infrared wavelengths",
-                "ngda"
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
-            "identifier": "C2052604735-LPDAAC_ECS",
-            "description": "The Terra Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Level 1 Precision Terrain Corrected Registered At-Sensor Radiance (AST_L1T) Version 3.1 data contains calibrated at-sensor radiance, which corresponds with the ASTER Level 1B AST_L1B  (https://doi.org/10.5067/ASTER/AST_L1B.003), that has been geometrically corrected and rotated to a north-up UTM projection. The AST_L1T V3.1 is created from a single resampling of the corresponding ASTER L1A AST_L1A (https://doi.org/10.5067/ASTER/AST_L1A.003) product. Radiometric calibration coefficients Version 5 (RCC V5) are applied to this product to improve the degradation curve derived from vicarious and lunar calibrations. The bands available in the AST_L1T V3.1 depend on the bands in the AST_L1A and can include up to three Visible and Near Infrared (VNIR) bands, six Shortwave Infrared (SWIR) bands, and five Thermal Infrared (TIR) bands. The AST_L1T V3.1 dataset does not include the aft-looking VNIR band 3.\r\n\r\nThe 3.1 version uses a precision terrain correction process that incorporates GLS2000 digital elevation data with derived ground control points (GCPs) to achieve topographic accuracy for all daytime scenes where correlation statistics reach a minimum threshold. Alternate levels of correction are possible (systematic terrain, systematic, or precision) for scenes acquired at night or that otherwise represent a reduced quality ground image (e.g., cloud cover).\r\n\r\nFor daytime images, if the VNIR or SWIR telescope collected data and precision correction was attempted, each precision terrain corrected image will have an accompanying independent quality assessment. It will include the geometric correction available for distribution in both a text file and a single band browse image with the valid GCPs overlaid.\r\n\r\nThis multi-file product also includes georeferenced full resolution browse images. The number of browse images and the band combinations of the images depend on the bands available in the corresponding AST_L1A dataset.\r\n\r\nThe AST_L1T V3.1 data product is only available through NASA\u2019s Earthdata Search. The ASTER L1T V3.1 Order Instructions provide step-by-step directions for ordering this product.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "AST_L1T.031",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "NASA LP DAAC",
-            "title": "ASTER Level 1 Precision Terrain Corrected Registered At-Sensor Radiance V031",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.07.06/pg-BR1A0000-2021070601_023_001.1.TIR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Terra Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Level 1 Precision Terrain Corrected Registered At-Sensor Radiance (AST_L1T) Version 3.1 data contains calibrated at-sensor radiance, which corresponds with the ASTER Level 1B AST_L1B  (https://doi.org/10.5067/ASTER/AST_L1B.003), that has been geometrically corrected and rotated to a north-up UTM projection. The AST_L1T V3.1 is created from a single resampling of the corresponding ASTER L1A AST_L1A (https://doi.org/10.5067/ASTER/AST_L1A.003) product. Radiometric calibration coefficients Version 5 (RCC V5) are applied to this product to improve the degradation curve derived from vicarious and lunar calibrations. The bands available in the AST_L1T V3.1 depend on the bands in the AST_L1A and can include up to three Visible and Near Infrared (VNIR) bands, six Shortwave Infrared (SWIR) bands, and five Thermal Infrared (TIR) bands. The AST_L1T V3.1 dataset does not include the aft-looking VNIR band 3.\r\n\r\nThe 3.1 version uses a precision terrain correction process that incorporates GLS2000 digital elevation data with derived ground control points (GCPs) to achieve topographic accuracy for all daytime scenes where correlation statistics reach a minimum threshold. Alternate levels of correction are possible (systematic terrain, systematic, or precision) for scenes acquired at night or that otherwise represent a reduced quality ground image (e.g., cloud cover).\r\n\r\nFor daytime images, if the VNIR or SWIR telescope collected data and precision correction was attempted, each precision terrain corrected image will have an accompanying independent quality assessment. It will include the geometric correction available for distribution in both a text file and a single band browse image with the valid GCPs overlaid.\r\n\r\nThis multi-file product also includes georeferenced full resolution browse images. The number of browse images and the band combinations of the images depend on the bands available in the corresponding AST_L1A dataset.\r\n\r\nThe AST_L1T V3.1 data product is only available through NASA\u2019s Earthdata Search. The ASTER L1T V3.1 Order Instructions provide step-by-step directions for ordering this product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_L1T.031",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST_L1T.031",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_L1T.031",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/AST_L1T.031",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "http://asterweb.jpl.nasa.gov/",
-                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
+                    "downloadURL": "http://asterweb.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2052604735-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2052604735-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.07.06/pg-BR1A0000-2021070601_023_001.1.TIR.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.07.06/pg-BR1A0000-2021070601_023_001.1.TIR.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1400/AST_L1T_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1400/AST_L1T_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/647/AST__L1T_User_Guide_V3.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/647/AST__L1T_User_Guide_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1401/ASTER_L1T_Product_Specification_v1.pdf",
-                    "description": "The ASTER Level-1T Product Specification provides a description of the data file.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER Level-1T Product Specification provides a description of the data file.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1401/ASTER_L1T_Product_Specification_v1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1335/AST_L1T_Quick_Reference_Guide_V2.pdf",
-                    "description": "ASTER L1T Quick Reference Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER L1T Quick Reference Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1335/AST_L1T_Quick_Reference_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1045/ASTER_L1T_Earthdata_Search_Order_Instructions.pdf",
-                    "description": "The ASTER L1T V3.1 Order Instructions provide step-by-step directions for downloading data.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER L1T V3.1 Order Instructions provide step-by-step directions for downloading data.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1045/ASTER_L1T_Earthdata_Search_Order_Instructions.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.07.06/pg-BR1A0000-2021070601_023_001.1.TIR.jpg",
+            "identifier": "C2052604735-LPDAAC_ECS",
+            "issued": "2021-07-07",
+            "keyword": [
+                "national geospatial data asset",
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/AST_L1T.031",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-07-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "AST_L1T.031",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-04T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER Level 1 Precision Terrain Corrected Registered At-Sensor Radiance V031"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-MIMI-4-INCA-CALIB-V1.0",
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
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Ion and Neutral Camera (INCA) obtains remote images of the global distribution of energetic ions for energies from 7 keV/nucleon to 8 MeV/nucleon, discriminated according to energy and mass species (oxygen and hydrogen). To obtain the images, INCA measures the arrival directions, energy and mass species of Energetic Neutral Atoms (ENA's) using the relatively new technique of ENA imaging. INCA also can be commanded to obtain very high sensitivity ion measurements, providing the angular, energy and species distributions of in-situ O and H ions. The Cassini Magnetospheric Imaging Instrument(MIMI) Imaging Neutral Camera (INCA) calibrated data set includes all image data collected from the MIMI Data Processing Unit during the Saturn tour. The original data has been decommutated, decoded, calibrated and further processed by software at the Applied Physics Laboratory (APL). The calibrated image data is provided in three forms: an averaged form where the original image N x N pixel images pixels intensity are averaged to a single value for one species and time-of-flight (TOF) combination, browse images which display rows and columns of images for one species and TOF combination, and movies which display averaged ENA image skymaps. Calibration of INCA data has been described fully in the Cassini/MIMI Data User Guide. This data set should be among the first used by a user of any of the MIMI INCA archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-mimi-4-inca-calib-v1.0_ujxw-d7hx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-MIMI-4-INCA-CALIB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-mimi-4-inca-calib-v1.0_ujxw-d7hx",
-            "description": "The Ion and Neutral Camera (INCA) obtains remote images of the global distribution of energetic ions for energies from 7 keV/nucleon to 8 MeV/nucleon, discriminated according to energy and mass species (oxygen and hydrogen). To obtain the images, INCA measures the arrival directions, energy and mass species of Energetic Neutral Atoms (ENA's) using the relatively new technique of ENA imaging. INCA also can be commanded to obtain very high sensitivity ion measurements, providing the angular, energy and species distributions of in-situ O and H ions. The Cassini Magnetospheric Imaging Instrument(MIMI) Imaging Neutral Camera (INCA) calibrated data set includes all image data collected from the MIMI Data Processing Unit during the Saturn tour. The original data has been decommutated, decoded, calibrated and further processed by software at the Applied Physics Laboratory (APL). The calibrated image data is provided in three forms: an averaged form where the original image N x N pixel images pixels intensity are averaged to a single value for one species and time-of-flight (TOF) combination, browse images which display rows and columns of images for one species and TOF combination, and movies which display averaged ENA image skymaps. Calibration of INCA data has been described fully in the Cassini/MIMI Data User Guide. This data set should be among the first used by a user of any of the MIMI INCA archive as it will lead one to information required to search for more detailed or highly specialized features in the original data.",
-            "title": "CASSINI S MIMI INCA SENSOR CALIBRATED DATA V1.0",
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
+            "title": "CASSINI S MIMI INCA SENSOR CALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F10/SSMI/DATA303",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wentz, Frank J, Kyle Hilburn and Deborah K Smith.2012. RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F10 NETCDF [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/DMSP-F10/SSMI/DATA303",
-            "issued": "2012-08-08",
-            "temporal": "1990-12-02T00:00:00Z/1997-11-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "oceans",
-                "precipitation",
-                "atmosphere",
-                "clouds",
-                "atmospheric water vapor",
-                "ocean winds",
-                "atmospheric winds",
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
-            "identifier": "C1979903058-GHRC_DAAC",
             "description": "The RSS SSM/I Ocean Product Grids Weekly Average from DMSP F10 netCDF dataset is part of the collection of Special Sensor Microwave/Imager (SSM/I) and Special Sensor Microwave Imager Sounder (SSMIS) data products produced as part of NASA's MEaSUREs Program. Remote Sensing Systems generates SSM/I and SSMIS binary data products using a unified, physically based algorithm to simultaneously retrieve ocean wind speed, water vapor, cloud water, and rain rate. The SSMIS data have been carefully intercalibrated to the brightness temperature level of the previous SSM/I and therefore extend this important time series of ocean winds, vapor, cloud and rain values. This algorithm is a product of 20 years of refinements, improvements, and verifications. The Global Hydrology Resource Center has reformatted the binary data into a netCDF data product for each temporal group for each satellite. The netCDF SSMI/SSMIS collection will be available for F10 for weekly averages.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F10 NETCDF V7",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F10%2FSSMI%2FDATA303",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSP-F10%2FSSMI%2FDATA303",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif10w",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rssmif10w",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/1995/f10_ssmi_19950107v7_wk_CW.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/1995/f10_ssmi_19950107v7_wk_CW.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/1995/f10_ssmi_19950107v7_wk_RR.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/1995/f10_ssmi_19950107v7_wk_RR.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/1995/f10_ssmi_19950107v7_wk_WV.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/1995/f10_ssmi_19950107v7_wk_WV.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/1995/f10_ssmi_19950107v7_wk_WS.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/1995/f10_ssmi_19950107v7_wk_WS.png",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/Hilburn_V7_Poster_AMS_SatMet_2010_Annapolis.pdf",
-                    "description": "Description of Remote Sensing Systems Version-7 Geophysical Retrievals",
                     "@type": "dcat:Distribution",
+                    "description": "Description of Remote Sensing Systems Version-7 Geophysical Retrievals",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ssmi_netcdf/Hilburn_V7_Poster_AMS_SatMet_2010_Annapolis.pdf",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f10/weekly/",
-                    "description": "OPeNDAP server dataset access",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP server dataset access",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/opendap/ssmi/f10/weekly/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ssmi/f10/weekly/browse/",
+            "identifier": "C1979903058-GHRC_DAAC",
+            "issued": "2012-08-08",
+            "keyword": [
+                "oceans",
+                "precipitation",
+                "atmosphere",
+                "clouds",
+                "atmospheric water vapor",
+                "ocean winds",
+                "atmospheric winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSP-F10/SSMI/DATA303",
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
+            "temporal": "1990-12-02T00:00:00Z/1997-11-15T23:59:59Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS SSM/I OCEAN PRODUCT GRIDS WEEKLY AVERAGE FROM DMSP F10 NETCDF V7"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/389/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-06-07",
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
-            "identifier": "DASHLINK_389",
             "description": "execute plans and schedules that achieve stated goals while simultaneously minimizing the cost of logistics management and maximizing resource productivity. This goal is a challenge in space flight environments where just-in-time logistics management can\u2019t be supported and large scale planning and scheduling requires collaborations and negotiations that aross many divisions and departments. Although there have been many systems proposed and/or developed that address one or more of these concerns, a key element missing in these systems is the\r\ntight coupling that is necessary between maintenance, logistics, and operations. This close relationship is particularly important in space operations where changes to scheduled missions and/or the logistics chain can greatly impact overall operations. Based on previous work on combined maintenance and operations planning/scheduling for Marine\r\nAviation, we propose a software-based infrastructure that coordinates planning, scheduling, and execution across multiple departments and disciplines.",
-            "title": "Tracking Logistical Constraints Across Missions and Organizations: A Multipurpose Information Infrastructure",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/SMC-IT_2006_CMMD.pdf",
-                    "description": "SMC-IT_2006_CMMD.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SMC-IT_2006_CMMD.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/SMC-IT_2006_CMMD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "SMC-IT_2006_CMMD.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Orosz_et_al._-_2006_-_Tracking_Logistical_Constraints_Across_Missions_and_Organizations_A_Multipurpose_Information_Infrastructure_2.pdf",
-                    "description": "Orosz et al. - 2006 - Tracking Logistical Constraints Across Missions and Organizations A Multipurpose Information Infrastructure.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Orosz et al. - 2006 - Tracking Logistical Constraints Across Missions and Organizations A Multipurpose Information Infrastructure.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Orosz_et_al._-_2006_-_Tracking_Logistical_Constraints_Across_Missions_and_Organizations_A_Multipurpose_Information_Infrastructure_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Orosz et al. - 2006 - Tracking Logistical Constraints Across Missions and Organizations A Multipurpose Information Infrastructure.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_389",
+            "issued": "2011-06-07",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/389/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Tracking Logistical Constraints Across Missions and Organizations: A Multipurpose Information Infrastructure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/CERES/ES8-FM3_L2.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-09-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AQUA/CERES/ES8-FM3_L2.004.",
-            "issued": "2017-08-18",
-            "temporal": "2002-06-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-10",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KORY, DR. PRIESTLEY",
                 "hasEmail": "mailto:kory.j.priestly@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1419931580-LARC_ASDC",
             "description": "CER_ES8_Aqua-FM3_Edition4 is the Clouds and the Earth's Radiant Energy System (CERES) Earth Radiation Budget Experiment (ERBE)-like Instantaneous Top-of-the-Atmosphere (TOA) Estimates Aqua Flight Model 3 (FM3) Edition 4 data product, which was collected using the CERES-FM3 instrument on the Aqua platform. Data collection for this product is ongoing.\r\n\r\nThe ERBE-like Footprint TOA Fluxes (ES-8) product contains 24 hours of instantaneous CERES data for a single scanner instrument, FM3 on the Aqua spacecraft. The ES-8 contains filtered radiances recorded every 0.01-second for the total (TOT), shortwave (SW), and window (WN) channels and the unfiltered SW, longwave (LW), and WN radiances. The SW and LW radiances at spacecraft altitude are converted to TOA fluxes with a scene identification algorithm and Angular Distribution Models (ADMs) which are \"like\" those used for the ERBE. The TOA fluxes, scene identification, and angular geometry are included on the ES-8.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful ERBE mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES ERBE-like Instantaneous TOA Estimates Aqua FM3 Edition4",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FES8-FM3_L2.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FCERES%2FES8-FM3_L2.004",
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
-                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/ES8-FM3_L2.004",
-                    "description": "DOI data set landing page for CER_ES8_Aqua-FM3_Edition4",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ES8_Aqua-FM3_Edition4",
+                    "downloadURL": "https://doi.org/10.5067/AQUA/CERES/ES8-FM3_L2.004",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1419931580-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ES8_Aqua-FM3_Edition4 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ES8_Aqua-FM3_Edition4 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1419931580-LARC_ASDC",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/CERES",
-                    "description": "NASA Earthdata Forum - CERES",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - CERES",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/CERES",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
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
-                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Signs of Change in the Tropics\u00a0-\u00a0New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring...",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Signs of Change in the Tropics\u00a0-\u00a0New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring...",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/DelicateBalance/balance2.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
-                    "description": "NASA Earth Observatory Article: Aqua CERES First Light: Image of the Day\u00a0-\u00a0The Clouds and the Earth's Radiant Energy System (CERES) instrument is one of six on board the Aqua satellite.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Aqua CERES First Light: Image of the Day\u00a0-\u00a0The Clouds and the Earth's Radiant Energy System (CERES) instrument is one of six on board the Aqua satellite.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
-                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day\u00a0-\u00a0Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day\u00a0-\u00a0Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
-                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day\u00a0- These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day\u00a0- These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
-                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction\u00a0-\u00a0Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction\u00a0-\u00a0Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
-                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog\u00a0-\u00a0Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog\u00a0-\u00a0Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
-                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation\u00a0-\u00a0These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation\u00a0-\u00a0These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/global-maps/CERES_NETFLUX_M",
-                    "description": "NASA Earth Observatory Article: Net Radiation\u00a0-\u00a0The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Net Radiation\u00a0-\u00a0The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
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
-                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet\u00a0-\u00a0Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that...",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet\u00a0-\u00a0Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that...",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/AM1/terra_animations.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
-                    "description": "NASA Earth Observatory Article: The Water Cycle\u00a0-\u00a0MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Water Cycle\u00a0-\u00a0MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2984/tropical-cloud-systems-and-ceres",
-                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day\u00a0-\u00a0CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day\u00a0-\u00a0CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ES8_R7V1.pdf",
-                    "description": "DPC-ES-8 R7V1 Data Products Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "DPC-ES-8 R7V1 Data Products Catalog",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ES8_R7V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES8/Aqua-FM3_Edition4/",
-                    "description": "ASDC Direct Data Download for CER_ES8_Aqua-FM3_Edition4",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ES8_Aqua-FM3_Edition4",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES8/Aqua-FM3_Edition4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES8/Aqua-FM3_Edition4/contents.html",
-                    "description": "OPeNDAP data access for CER_ES8_Aqua-FM3_Edition4",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ES8_Aqua-FM3_Edition4",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES8/Aqua-FM3_Edition4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1419931580-LARC_ASDC",
+            "issued": "2017-08-18",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/CERES/ES8-FM3_L2.004",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-10-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2002-06-18T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES ERBE-like Instantaneous TOA Estimates Aqua FM3 Edition4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/454/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-08-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
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
-            "identifier": "DASHLINK_454",
             "description": "##Eligibility \r\nStudents with accepted papers at CIDU 2011\r\n##Application deadline\r\nSeptember 12, 2011",
-            "title": "Student travel application for CIDU 2011",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.d",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/cidu11_travel_application.docx",
-                    "description": "Student travel award application",
                     "@type": "dcat:Distribution",
+                    "description": "Student travel award application",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/cidu11_travel_application.docx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.d",
                     "title": "cidu11_travel_application.docx"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_454",
+            "issued": "2011-08-30",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/454/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Student travel application for CIDU 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA211",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GLAS/ICESat L2 Global Land Surface Altimetry Data (HDF5) V034. Version 034. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ICESAT/GLAS/DATA211.",
-            "issued": "2003-02-20",
-            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-10-11",
-            "keyword": [
-                "sea ice",
-                "topography",
-                "cryosphere",
-                "earth science",
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
-            "identifier": "C2153551318-NSIDC_CPRD",
             "description": "GLAH06 is used in conjunction with GLAH05 to create the Level-2 altimetry products. Level-2 altimetry data provide surface elevations for ice sheets (GLAH12), sea ice (GLAH13), land (GLAH14), and oceans (GLAH15). Data also include the laser footprint geolocation and reflectance, as well as geodetic, instrument, and atmospheric corrections for range measurements. The Level-2 elevation products, are regional products archived at 14 orbits per granule, starting and stopping at the same demarcation (\u00b1 50\u00b0 latitude) as GLAH05 and GLAH06. Each regional product is processed with algorithms specific to that surface type. Surface type masks define which data are written to each of the products. If any data within a given record fall within a specific mask, the entire record is written to the product. Masks can overlap: for example, non-land data in the sea ice region may be written to the sea ice and ocean products. This means that an algorithm may write the same data to more than one Level-2 product. In this case, different algorithms calculate the elevations in their respective products. The surface type masks are versioned and archived at NSIDC, so users can tell which data to expect in each product.  Each data granule has an associated browse product.",
-            "title": "GLAS/ICESat L2 Global Land Surface Altimetry Data (HDF5) V034",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA211",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA211",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLAH14+V034",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLAH14+V034",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA211",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA211",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA211",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA211",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2153551318-NSIDC_CPRD",
+            "issued": "2003-02-20",
+            "keyword": [
+                "sea ice",
+                "topography",
+                "cryosphere",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA211",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-10-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -86.0 180.0 86.0",
+            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLAS/ICESat L2 Global Land Surface Altimetry Data (HDF5) V034"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MPFR-M-RVRCAM-2-EDR-V1.0",
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
-                "mars pathfinder",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Mars Pathfinder bounced down and rolled to a stop on the surface \nof Mars on July 4, 1997.  After a slight delay in deployment due \nto airbags draped over one of the lander's petals, the Rover rolled \ndown onto the surface of Mars at 5:37am, July 6, 1997 (UTC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mpfr-m-rvrcam-2-edr-v1.0_ukcs-a6h5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars pathfinder",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MPFR-M-RVRCAM-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mpfr-m-rvrcam-2-edr-v1.0_ukcs-a6h5",
-            "description": "Mars Pathfinder bounced down and rolled to a stop on the surface \nof Mars on July 4, 1997.  After a slight delay in deployment due \nto airbags draped over one of the lander's petals, the Rover rolled \ndown onto the surface of Mars at 5:37am, July 6, 1997 (UTC).",
-            "title": "MARS PATHFINDER ROVER MARS ROVER CAMERA\n                                      2 EDR VERSION 1.0",
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
+            "title": "MARS PATHFINDER ROVER MARS ROVER CAMERA\n                                      2 EDR VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-3-ESC1-V1.0",
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
+            "description": "This data set contains CODMAC\nlevel 3 science data acquired by the DFMS and RTOF ROSINA sensors\nbetween 2014-11-19 and 2015-03-10 during the Escort phase 1 of\nthe Rosetta mission to comet 67P/CG. COPS data do not need on-\nground calibration and are included in the level 2 dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-3-esc1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-3-ESC1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-3-esc1-v1.0",
-            "description": "This data set contains CODMAC\nlevel 3 science data acquired by the DFMS and RTOF ROSINA sensors\nbetween 2014-11-19 and 2015-03-10 during the Escort phase 1 of\nthe Rosetta mission to comet 67P/CG. COPS data do not need on-\nground calibration and are included in the level 2 dataset.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 3 ESC1 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 3 ESC1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0571-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-09T22:50:30.000 to 2015-02-10T05:11:37.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0571-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0571-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0571-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-09T22:50:30.000 to 2015-02-10T05:11:37.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0571 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0571 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-C-ITS-2-NAV-9P-ENCOUNTER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw comet 9P/Tempel 1 and calibration images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the impactor spacecraft as well as for scientific investigations. These data were collected from 6 May to 4 July 2005.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-c-its-2-nav-9p-encounter-v1.0_ukem-m48c",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "deep impact",
                 "9p/tempel 1 (1867 g1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-C-ITS-2-NAV-9P-ENCOUNTER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-c-its-2-nav-9p-encounter-v1.0_ukem-m48c",
-            "description": "This data set contains raw comet 9P/Tempel 1 and calibration images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the impactor spacecraft as well as for scientific investigations. These data were collected from 6 May to 4 July 2005.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - RAW ITS NAV IMAGES V1.0",
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
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - RAW ITS NAV IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4GQ6VP4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Drought Total Economic Loss Risk Deciles. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H4GQ6VP4. https://doi.org/10.7927/H4GQ6VP4.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4VX0DFT",
-                "https://doi.org/10.7927/H4R49NQV",
-                "https://doi.org/10.7927/H4MG7MDV"
-            ],
-            "keyword": [
-                "natural hazards",
-                "earth science",
-                "socioeconomics",
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
-            "identifier": "C179001772-SEDAC",
-            "description": "The Global Drought Total Economic Loss Risk Deciles is a 2.5 minute grid of global drought total economic loss risks. A process of spatially allocating Gross Domestic Product (GDP) based upon the Sachs et al. (2003) methodology is utilized.  First the proportional contributions of subnational Units to their respective national GDP are determined using sources of various origins. The contribution rates are then applied to published World Bank Development Indicators to determine a GDP value for the subnational Unit. Once the national GDP is spatially stratified into the smallest administrative Units available, GDP values for grid cells are derived using Gridded Population of the World, Version 3 (GPWv3) data of population distributions. A per capita contribution value is determined within each subnational Unit, and this value is multiplied by the population per grid cell. Once a GDP value has been determined on a per grid cell basis, then the regionally variable loss rate as derived from the historical records of EM-DAT is used to determine the total economic loss risks posed to a grid cell by drought hazards. The final surface does not present absolute values of total economic loss, but rather a relative decile (1-10 with increasing risk) ranking of grid cells based upon the calculated economic loss risks. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Drought Total Economic Loss Risk Deciles",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Drought Total Economic Loss Risk Deciles is a 2.5 minute grid of global drought total economic loss risks. A process of spatially allocating Gross Domestic Product (GDP) based upon the Sachs et al. (2003) methodology is utilized.  First the proportional contributions of subnational Units to their respective national GDP are determined using sources of various origins. The contribution rates are then applied to published World Bank Development Indicators to determine a GDP value for the subnational Unit. Once the national GDP is spatially stratified into the smallest administrative Units available, GDP values for grid cells are derived using Gridded Population of the World, Version 3 (GPWv3) data of population distributions. A per capita contribution value is determined within each subnational Unit, and this value is multiplied by the population per grid cell. Once a GDP value has been determined on a per grid cell basis, then the regionally variable loss rate as derived from the historical records of EM-DAT is used to determine the total economic loss risks posed to a grid cell by drought hazards. The final surface does not present absolute values of total economic loss, but rather a relative decile (1-10 with increasing risk) ranking of grid cells based upon the calculated economic loss risks. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4GQ6VP4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4GQ6VP4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-drought-total-economic-loss-risk-deciles/drought-total-economic-loss-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-drought-total-economic-loss-risk-deciles/drought-total-economic-loss-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-total-economic-loss-risk-deciles/maps",
+            "identifier": "C179001772-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "natural hazards",
+                "earth science",
+                "socioeconomics",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4GQ6VP4",
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
+                "https://doi.org/10.7927/H4VX0DFT",
+                "https://doi.org/10.7927/H4R49NQV",
+                "https://doi.org/10.7927/H4MG7MDV"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 86.0",
+            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "NDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Drought Total Economic Loss Risk Deciles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-EXT1-67PCHURYUMOV-M25-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the ROSETTA EXTENSION 1 phase of the Rosetta mission at the comet 67P, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-ext1-67pchuryumov-m25-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "dark",
@@ -1473882,140 +1473884,116 @@
                 "vega",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-EXT1-67PCHURYUMOV-M25-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-ext1-67pchuryumov-m25-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the ROSETTA EXTENSION 1 phase of the Rosetta mission at the comet 67P, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000.",
-            "title": "ROSETTA-ORBITER ROSETTA EXTENSION 1 OSINAC 2 EDR MTP025 V1.0",
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
+            "title": "ROSETTA-ORBITER ROSETTA EXTENSION 1 OSINAC 2 EDR MTP025 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-3/CAMERA/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Pueschel, Rudolf F.2001. CAMEX-3 CLOUD AND AEROSOL PARTICLE CHARACTERIZATION VIDEO [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-3/CAMERA/DATA201",
-            "issued": "2001-04-06",
-            "temporal": "1998-08-10T15:19:01Z/1998-09-02T23:37:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "aerosols",
-                "clouds",
-                "earth science",
-                "precipitation",
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
-            "identifier": "C1995554198-GHRC_DAAC",
             "description": "CAPAC is a series of three instruments: the Forward Scattering Spectrometer Probe model 300 (FSSP-300), the Two Dimensional Optical Array Probes [Cloud and Precipitation Probes (2D-P)] and the CAPAC video. These instruments flew during CAMEX-3 upon the NASA DC-8 mounted on the left wing. Cloud and aerosol particles were exposed to laser light to measure particle size from 0.3 micrometer to 6.4 millimeter, and both size and shape between 40 micrometer and 6.4 millimeter particle diameter as function of particle size.  The size distributions thus determined were integrated to yield particle surface area, and ice and liquid water contents in clouds and precipitation. CAPAC videos are a visual record of the particles and hydrometeors passing through the instrument housing. The purpose of the CAMEX-3 mission was to study hurricanes over land and ocean in the U.S. Gulf of Mexico, Caribbean, and Western Atlantic Ocean in coordination with multiple aircraft and research-quality radar, lightning, radiosonde and rain gauge sites.  For further information and to obtain this data, please contact GHRC at support-ghrc@earthdata.nasa.gov",
-            "title": "CAMEX-3 CLOUD AND AEROSOL PARTICLE CHARACTERIZATION VIDEO V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FCAMERA%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-3%2FCAMERA%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/CAMEX-3/CAMERA/DATA201",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "http://dx.doi.org/10.5067/CAMEX-3/CAMERA/DATA201",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex3/dc8capac/dc8capac_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex3/dc8capac/dc8capac_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/CAMEX3",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/CAMEX3",
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
+            "identifier": "C1995554198-GHRC_DAAC",
+            "issued": "2001-04-06",
+            "keyword": [
+                "aerosols",
+                "clouds",
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-3/CAMERA/DATA201",
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
             "spatial": "-105.0 10.0 -50.0 50.0",
+            "temporal": "1998-08-10T15:19:01Z/1998-09-02T23:37:00Z",
             "theme": [
                 "CAMEX-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-3 CLOUD AND AEROSOL PARTICLE CHARACTERIZATION VIDEO V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/wfpc2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/hubble/main/index.html"
-            ],
-            "keyword": [
-                "wide field planetary camera 2",
-                "3d model",
-                "camera",
-                "hubble"
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
-            "identifier": "NASA-421",
             "description": "Polygons: 152 Vertices: 224",
-            "title": "NASA 3D Models: Wide Field Planetary Camera 2",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1474023,183 +1474001,186 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-421",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wide field planetary camera 2",
+                "3d model",
+                "camera",
+                "hubble"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/wfpc2",
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
+                "http://www.nasa.gov/mission_pages/hubble/main/index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Wide Field Planetary Camera 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-MIRO-2-EAR2-EARTH2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the second Earth swing-by phase of the Rosetta mission by the MIRO instrument. It also contains data taken during the immediately preceding 6th Payload Checkout.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-miro-2-ear2-earth2-v1.0_ukix-nfam",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "calibration",
                 "earth",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-MIRO-2-EAR2-EARTH2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-miro-2-ear2-earth2-v1.0_ukix-nfam",
-            "description": "This data set contains Spectroscopic, Continuum and Engineering data, in the form of table files, taken during the second Earth swing-by phase of the Rosetta mission by the MIRO instrument. It also contains data taken during the immediately preceding 6th Payload Checkout.",
-            "title": "ROSETTA-ORBITER EARTH MIRO 2 EAR2 EARTH2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH MIRO 2 EAR2 EARTH2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/206/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Deniz Gencaga",
+                "hasEmail": "mailto:dgencaga@gmail.com"
+            },
+            "description": "We present a novel and general methodology for modeling time-varying vector autoregressive processes which are widely used in many areas such as modeling of chemical processes, mobile communication channels and biomedical signals. In the literature, most work utilize multivariate Gaussian models for the mentioned applications, mainly due to the lack of efficient analytical tools for modeling with non-Gaussian distributions. In this paper, we propose a particle filtering approach which can model non-Gaussian autoregressive processes having cross-correlations among them. Moreover, time-varying parameters of the process can be modeled as the most general case by using this sequential Bayesian estimation method. Simulation results justify the performance of the proposed technique, which potentially can model also Gaussian processes as a sub-case.",
+            "identifier": "DASHLINK_206",
             "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "dashlink",
                 "ames",
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Deniz Gencaga",
-                "hasEmail": "mailto:dgencaga@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/206/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_206",
-            "description": "We present a novel and general methodology for modeling time-varying vector autoregressive processes which are widely used in many areas such as modeling of chemical processes, mobile communication channels and biomedical signals. In the literature, most work utilize multivariate Gaussian models for the mentioned applications, mainly due to the lack of efficient analytical tools for modeling with non-Gaussian distributions. In this paper, we propose a particle filtering approach which can model non-Gaussian autoregressive processes having cross-correlations among them. Moreover, time-varying parameters of the process can be modeled as the most general case by using this sequential Bayesian estimation method. Simulation results justify the performance of the proposed technique, which potentially can model also Gaussian processes as a sub-case.",
-            "title": "Modeling non-Gaussian time-varying vector autoregressive process",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Modeling non-Gaussian time-varying vector autoregressive process"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OETP-5-LORESELECTRONS-V1.0",
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
+            "description": "This file gives the Ne, Te and Vs measurements derived by fitting the radial probe voltampere curves taken whenever PVO was within the ionosphere (ie., between the inbound and outbound ionopause crossings). Data from essentially every orbit in 1979 and 1980 included ionosphere transits. After the summer of 1980, however, periapsis could no longer be maintained at low altitudes, and it rose slowly. After April 1981 periapsis was above the altitude of the dayside ionopause, so the spacecraft encountered the ionosphere only in the terminator regions and on the nightside where the ionosphere extends to much higher altitudes. Dayside measurements again became available early in 1992 when periapsis returned to low enough altitudes. The PVO Entry period of between July and October 1992 provided only nightside periapsis data. During the intervening period (1981-91), only nightside UADS measurements in the high altitude (downstream) ionosphere were available. Note that High Resolution Ne data from the 1981-91 interval provide measurements in the dayside magnetosheath and in the solar wind, but these data have limited accuracy because of spacecraft photoelectron contributions. See [BRACEETAL1988] for further details on the interpretation of High Resolution measurements made outside the ionosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oetp-5-loreselectrons-v1.0_ukkn-bcwd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OETP-5-LORESELECTRONS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oetp-5-loreselectrons-v1.0_ukkn-bcwd",
-            "description": "This file gives the Ne, Te and Vs measurements derived by fitting the radial probe voltampere curves taken whenever PVO was within the ionosphere (ie., between the inbound and outbound ionopause crossings). Data from essentially every orbit in 1979 and 1980 included ionosphere transits. After the summer of 1980, however, periapsis could no longer be maintained at low altitudes, and it rose slowly. After April 1981 periapsis was above the altitude of the dayside ionopause, so the spacecraft encountered the ionosphere only in the terminator regions and on the nightside where the ionosphere extends to much higher altitudes. Dayside measurements again became available early in 1992 when periapsis returned to low enough altitudes. The PVO Entry period of between July and October 1992 provided only nightside periapsis data. During the intervening period (1981-91), only nightside UADS measurements in the high altitude (downstream) ionosphere were available. Note that High Resolution Ne data from the 1981-91 interval provide measurements in the dayside magnetosheath and in the solar wind, but these data have limited accuracy because of spacecraft photoelectron contributions. See [BRACEETAL1988] for further details on the interpretation of High Resolution measurements made outside the ionosphere.",
-            "title": "PVO VENUS ELECT TEMP PROBE DERVD ELECT DENS LOW RES VER 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PVO VENUS ELECT TEMP PROBE DERVD ELECT DENS LOW RES VER 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-RSS-1-EDR-V1.0",
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
-                "mars exploration rover"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains raw radio science data and supporting media calibration acquired during the Mars Exploration Rover surface operations. The radio observations were carried out using the Earth-based receiving stations of the NASA Deep Space Network (DSN), providing measurements of the range-rate (Doppler) between Earth and MER1 and with the Mars Odyssey orbiter, providing measurements of the range-rate (Doppler) between MER1 and the Odyssey orbiter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-rss-1-edr-v1.0_ukmz-aiak",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-RSS-1-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-rss-1-edr-v1.0_ukmz-aiak",
-            "description": "This archive contains raw radio science data and supporting media calibration acquired during the Mars Exploration Rover surface operations. The radio observations were carried out using the Earth-based receiving stations of the NASA Deep Space Network (DSN), providing measurements of the range-rate (Doppler) between Earth and MER1 and with the Mars Odyssey orbiter, providing measurements of the range-rate (Doppler) between MER1 and the Odyssey orbiter.",
-            "title": "MARS EXPLORATION ROVER 1 RADIO SCIENCE SUBSYSTEM EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARS EXPLORATION ROVER 1 RADIO SCIENCE SUBSYSTEM EDR V1.0"
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
-                "m3"
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
-            "identifier": "NASA-555",
             "description": "M3",
-            "title": "PDS Chandrayaan-1 Moon Mineralogy Mapper (M3) Release 1",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1474207,60 +1474188,57 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-555",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "m3"
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
+            "title": "PDS Chandrayaan-1 Moon Mineralogy Mapper (M3) Release 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/L4CD2D15VU2G",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lauren M. Zamora, Nikolaus Evangeliou, Christine D. Groot Zwaaftink, Ralph A. Kahn. 2022-06-24. OCFLEXPART. Version 1. FLEXPART organic carbon aerosol L4 global daily 1 x 1 degrees. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/L4CD2D15VU2G. https://disc.gsfc.nasa.gov/datacollection/OCFLEXPART_1.html. Digital Science Data.",
-            "issued": "2022-05-24",
-            "temporal": "2008-01-01T00:00:00Z/2015-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-24",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lauren Zamora",
                 "hasEmail": "mailto:lauren.m.zamora@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2364413057-GES_DISC",
-            "description": "This is a global simulation of organic carbon (OC) aerosol concentrations and daily deposition (wet+dry) from the FLEX-ible PARTicle (FLEXPART) Lagrangian particle dispersion model version 10.4. The FLEXPART model code are open source and freely available.",
-            "series-name": "OCFLEXPART",
-            "graphic-preview-description": "The figure shows a sample daily concentration of organic carbon from biomass burning.",
             "creator": "Lauren M. Zamora, Nikolaus Evangeliou, Christine D. Groot Zwaaftink, Ralph A. Kahn",
-            "title": "FLEXPART organic carbon aerosol L4 global daily 1 x 1 degrees V1 (OCFLEXPART)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCFLEXPART_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This is a global simulation of organic carbon (OC) aerosol concentrations and daily deposition (wet+dry) from the FLEX-ible PARTicle (FLEXPART) Lagrangian particle dispersion model version 10.4. The FLEXPART model code are open source and freely available.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL4CD2D15VU2G",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL4CD2D15VU2G",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCFLEXPART_1.png",
-                    "description": "The figure shows a sample daily concentration of organic carbon from biomass burning.",
                     "@type": "dcat:Distribution",
+                    "description": "The figure shows a sample daily concentration of organic carbon from biomass burning.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCFLEXPART_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
@@ -1474270,264 +1474248,265 @@
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/FLEXPART/OCFLEXPART.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/FLEXPART/OCFLEXPART.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/FLEXPART/OCFLEXPART.1/doc/README.OCFLEXPART_1.pdf",
-                    "description": "README document for the FLEXPART organic carbon aerosol L4 global daily 1 x 1 degrees V1 (OCFLEXPART), available at the GES DISC",
                     "@type": "dcat:Distribution",
+                    "description": "README document for the FLEXPART organic carbon aerosol L4 global daily 1 x 1 degrees V1 (OCFLEXPART), available at the GES DISC",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/FLEXPART/OCFLEXPART.1/doc/README.OCFLEXPART_1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "The figure shows a sample daily concentration of organic carbon from biomass burning.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCFLEXPART_1.png",
+            "identifier": "C2364413057-GES_DISC",
+            "issued": "2022-05-24",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/L4CD2D15VU2G",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "series-name": "OCFLEXPART",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2008-01-01T00:00:00Z/2015-12-31T23:59:59.999Z",
             "theme": [
                 "ESDIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FLEXPART organic carbon aerosol L4 global daily 1 x 1 degrees V1 (OCFLEXPART)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSUERP_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSUERP_001.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-30",
-            "keyword": [
-                "geodetics",
-                "gravity/gravitational field",
-                "tectonics",
-                "earth science",
-                "solid earth"
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
-            "identifier": "C1427046559-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System Ultra-Rapid Earth Rotation Product (ERP) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure.  Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce GNSS Earth Rotation products. The IGS Analysis Center Coordinator (ACC) uses these individual AC solutions to generate the official IGS ultra-rapid combined ERP products.\u00a0The ultra-rapid ERP combination is a sub-daily solution, released four times per day, at 03:00, 09:00, 15:00, and 21:00 UTC (prior to GPS week 1267 they were released twice daily). IGS ultra-rapid ERP files are to be used with the IGS ultra-rapid orbit solution files. All ERP solution files utilize the IGS ERP format.",
-            "title": "Global Navigation Satellite System (GNSS) Ultra-Rapid Earth Rotation Product from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSUERP_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSUERP_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "ftp://cddis.nasa.gov/gnss/products",
-                    "description": "URL for retrieval of GNSS derived products through ftp",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS derived products through ftp",
+                    "downloadURL": "ftp://cddis.nasa.gov/gnss/products",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_product_holdings.html",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_product_holdings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSUERP_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSUERP_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1427046559-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics",
+                "earth science",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSUERP_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) Ultra-Rapid Earth Rotation Product from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D89.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D89. Version 001. VIIRS/NPP BRDF/Albedo NBAR at Solar Noon DNB Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D89.001. https://doi.org/10.5067/VIIRS/VNP43D89.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "earth science"
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
-            "identifier": "C1607364966-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Nadir BRDF-Adjusted Reflectance (NBAR) for DNB (VNP43D89) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D80 through VNP43D89 are the NBAR products of the VNP43D BRDF/Albedo product suite. NBAR values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) included in the VNP43MA4 (https://doi.org/10.5067/VIIRS/VNP43MA4.001) product. In addition to the bands included in VNP43MA4, this product suite includes NBAR values for the VIIRS Day/Night Band (DNB). The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon. Details regarding methodology are available on the VNP43MA4 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D89 is the NBAR for VIIRS DNB (0.7 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D89",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo NBAR at Solar Noon DNB Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Nadir BRDF-Adjusted Reflectance (NBAR) for DNB (VNP43D89) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D80 through VNP43D89 are the NBAR products of the VNP43D BRDF/Albedo product suite. NBAR values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) included in the VNP43MA4 (https://doi.org/10.5067/VIIRS/VNP43MA4.001) product. In addition to the bands included in VNP43MA4, this product suite includes NBAR values for the VIIRS Day/Night Band (DNB). The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon. Details regarding methodology are available on the VNP43MA4 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D89 is the NBAR for VIIRS DNB (0.7 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D89.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D89.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D89.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D89.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D89.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D89.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607364966-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607364966-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D89.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D89.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D89",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D89",
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
+            "identifier": "C1607364966-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D89.001",
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
+            "series-name": "VNP43D89",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo NBAR at Solar Noon DNB Daily L3 Global 30ArcSec CMG V001"
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
-                "grs",
-                "themis",
-                "pds",
-                "spice"
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
-            "identifier": "NASA-683",
             "description": "GRS, THEMIS, SPICE",
-            "title": "PDS Odyssey Data Release 16",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1474535,131 +1474514,166 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-683",
+            "issued": "2018-06-25",
+            "keyword": [
+                "grs",
+                "themis",
+                "pds",
+                "spice"
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
+            "title": "PDS Odyssey Data Release 16"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-3-TELRDR-V1.0",
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
+            "description": "Data taken by the sensors of the Rover Environmental Monitoring Station (REMS) aboard the  Mars Science Laboratory, in electrical and thermal units.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-3-telrdr-v1.0_ukwn-e33h",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-3-TELRDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-3-telrdr-v1.0_ukwn-e33h",
-            "description": "Data taken by the sensors of the Rover Environmental Monitoring Station (REMS) aboard the  Mars Science Laboratory, in electrical and thermal units.",
-            "title": "MSL MARS ROVER ENV MONITORING STATION \n                                      3 TELRDR V1.0",
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
+            "title": "MSL MARS ROVER ENV MONITORING STATION \n                                      3 TELRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0021-V1.0",
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
-                "sun",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-03-28T00:29:04.500 to 2006-03-28T02:38:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0021-v1.0_ukyp-qaj4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "sun",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0021-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0021-v1.0_ukyp-qaj4",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-03-28T00:29:04.500 to 2006-03-28T02:38:57.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0021 V1.0",
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
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0021 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_pancam_sci_derived_iof&version=1.0",
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
+            "description": "This bundle contains derived IOF data from the Panoramic Cameras (Pancam) on Mars Exploration Rover 2 (Spirit). These data were produced by the science team.",
+            "identifier": "urn:nasa:pds:mer2_pancam_sci_derived_iof",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_pancam_sci_derived_iof&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer2_pancam_sci_derived_iof",
-            "description": "This bundle contains derived IOF data from the Panoramic Cameras (Pancam) on Mars Exploration Rover 2 (Spirit). These data were produced by the science team.",
-            "title": "MER2 Pancam Science Derived IOF Data Bundle",
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
+            "title": "MER2 Pancam Science Derived IOF Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/um5r-gqim",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "DLD-1 and MOLT-4 cell lines were cultured in a rotating cell culture system to simulate microgravity and mRNA expression profile in comparison to Static controls. Cells were grown in 10mL rotating vessels in a Rotary Cell Culture System (RCCS) and in 60mm Petri dishes (test control respectively). Two replicates of test (Microgravity) and control (static) each from DLD-1 and MOLT-4 were analyzed by microarray. Simulated microgravity affected the solid tumor cell line DLD-1 markedly which showed a higher percentage of dysregulated genes compared to the hematological tumor cell line MOLT-4. Microgravity affects the cell cycle of DLD-1 cells and disturbs expression of cell cycle regulatory gene networks. Multiple microRNA host genes were dysregulated and significantly mir-22 tumor suppressor microRNA is highly upregulated in DLD-1.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-125",
+                    "mediaType": "text/html",
+                    "title": "mRNA expression profile in DLD-1 and MOLT-4 cancer cell lines cultured under Microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-125_um5r-gqim",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "growth protocol",
                 "data transformation",
@@ -1474672,284 +1474686,271 @@
                 "rna extraction",
                 "data collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/um5r-gqim",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-125_um5r-gqim",
-            "description": "DLD-1 and MOLT-4 cell lines were cultured in a rotating cell culture system to simulate microgravity and mRNA expression profile in comparison to Static controls. Cells were grown in 10mL rotating vessels in a Rotary Cell Culture System (RCCS) and in 60mm Petri dishes (test control respectively). Two replicates of test (Microgravity) and control (static) each from DLD-1 and MOLT-4 were analyzed by microarray. Simulated microgravity affected the solid tumor cell line DLD-1 markedly which showed a higher percentage of dysregulated genes compared to the hematological tumor cell line MOLT-4. Microgravity affects the cell cycle of DLD-1 cells and disturbs expression of cell cycle regulatory gene networks. Multiple microRNA host genes were dysregulated and significantly mir-22 tumor suppressor microRNA is highly upregulated in DLD-1.",
-            "title": "mRNA expression profile in DLD-1 and MOLT-4 cancer cell lines cultured under Microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-125",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "mRNA expression profile in DLD-1 and MOLT-4 cancer cell lines cultured under Microgravity"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "mRNA expression profile in DLD-1 and MOLT-4 cancer cell lines cultured under Microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-SUMM-AVERAGE-15MIN-V1.0",
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
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-summ-average-15min-v1.0_um8r-cn9r",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-SUMM-AVERAGE-15MIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-summ-average-15min-v1.0_um8r-cn9r",
-            "description": "NULL",
-            "title": "VG2 JUP LECP CALIBRATED RESAMPLED SCAN\n                                      AVERAGED 15MIN V1.1",
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
+            "title": "VG2 JUP LECP CALIBRATED RESAMPLED SCAN\n                                      AVERAGED 15MIN V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/11/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ole Mengshoel",
                 "hasEmail": "mailto:ole.j.mengshoel@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_11",
             "description": "Electrical power systems play a critical role in spacecraft and aircraft. This paper discusses our development of a diagnostic capability for an electrical power system testbed, ADAPT, using probabilistic techniques. In the context of ADAPT, we present two challenges, regarding modelling and real-time performance, often encountered in real-world diagnostic applications. To meet the modelling challenge, we discuss our novel high-level specification language which supports auto-generation of Bayesian networks. To meet the real-time challenge, we compile Bayesian networks into arithmetic circuits.  Arithmetic circuits typically have small footprints and are optimized for the real-time avionics systems found in spacecraft and aircraft. Using our approach, we present how Bayesian networks with over 400 nodes are auto-generated and then compiled into arithmetic circuits. Using real-world data from ADAPT as well as simulated data, we obtain average inference times smaller than one millisecond when computing diagnostic queries using arithmetic circuits that model our real-world electrical power system.\r\n\r\nReference:\r\n\r\n O. J. Mengshoel, A. Darwiche, K. Cascio, M. Chavira, S. Poll, and S. Uckun, \u201cDiagnosing Faults in Electrical Power Systems of Spacecraft and Aircraft\u201d, In Proc. of the Twentieth Innovative Applications of Artificial Intelligence, Conference (IAAI-08), Chicago, IL, 2008.\r\n\r\nBibTex Reference:  \r\n\r\n @inproceedings{mengshoel08diagnosing,\r\n  author    = {Mengshoel, O. J. and Darwiche, A. and Cascio, K. and Chavira, M. and Poll, S. and Uckun, S.},\r\n  title     = {Diagnosing Faults in Electrical Power Systems of Spacecraft and Aircraft},\r\n  booktitle     = {Proceedings of the Twentieth Innovative Applications of Artificial Intelligence\r\n                      Conference (IAAI-08)},\r\n  pages = {1699--1705},\r\n  address = {Chicago, IL},\r\n  year      = {2008}\r\n}",
-            "title": "Probabilistic Fault Diagnosis in Electrical Power Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/IAAI2008.pdf",
-                    "description": "Diagnosing Faults in Electrical Power Systems of Spacecraft and Aircraft",
                     "@type": "dcat:Distribution",
+                    "description": "Diagnosing Faults in Electrical Power Systems of Spacecraft and Aircraft",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/IAAI2008.pdf",
+                    "mediaType": "application/pdf",
                     "title": "IAAI2008.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_11",
+            "issued": "2010-09-09",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/11/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Probabilistic Fault Diagnosis in Electrical Power Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A17L-L-TG-2-TRAVERSE-GRAVITY-V1.0",
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
-                "apollo 17"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains a table of readings from the Traverse Gravimeter Experiment performed during the Apollo 17 mission.  The gravimeter, which recorded relative measurements of the local gravitational field at the lunar surface, was manually run by the astronauts near the Lunar Module landing site.  The data table includes 23 valid gravity values, with calibrations and corrections, that were obtained from 12 to 14 December 1972.  The absolute value for the Lunar Module site was estimated to be 162,694.6 milligal with an uncertainty of 5 milligal. Supporting documentation includes the Apollo 17 Traverse Gravimeter Experiment Final Report.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a17l-l-tg-2-traverse-gravity-v1.0_umbt-3pi9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "apollo 17"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A17L-L-TG-2-TRAVERSE-GRAVITY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a17l-l-tg-2-traverse-gravity-v1.0_umbt-3pi9",
-            "description": "This data set contains a table of readings from the Traverse Gravimeter Experiment performed during the Apollo 17 mission.  The gravimeter, which recorded relative measurements of the local gravitational field at the lunar surface, was manually run by the astronauts near the Lunar Module landing site.  The data table includes 23 valid gravity values, with calibrations and corrections, that were obtained from 12 to 14 December 1972.  The absolute value for the Lunar Module site was estimated to be 162,694.6 milligal with an uncertainty of 5 milligal. Supporting documentation includes the Apollo 17 Traverse Gravimeter Experiment Final Report.",
-            "title": "APOLLO 17 TRAVERSE GRAVIMETER\n      DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "APOLLO 17 TRAVERSE GRAVIMETER\n      DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1085-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-07T10:16:35.000 to 2015-10-07T17:30:01.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1085-v1.0_umd2-nvh5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1085-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1085-v1.0_umd2-nvh5",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-07T10:16:35.000 to 2015-10-07T17:30:01.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1085 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1085 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-IRON-COUNTS_V1.0",
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
+            "description": "A global map of gamma ray                counting rates binned on twenty-degree quasi-equal-area                 pixels is provided. The map was determined from a time series           of net counting rates for the 7.6 MeV gamma ray peak produced by        neutron capture with Fe within Ceres' regolith. The data were           acquired by Dawn's Gamma Ray and Neutron Detector (GRaND) while         in low altitude mapping orbit, about 385 km from Ceres' surface         (about 0.8 body radii altitude). Prior to mapping, the time             series counting data were subjected to corrections for variations       in the flux of galactic cosmic rays and measurement geometry,           as described by PRETTYMANETAL2017.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-iron-counts_v1.0_umeb-mq5g",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "1 ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-IRON-COUNTS_V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-iron-counts_v1.0_umeb-mq5g",
-            "description": "A global map of gamma ray                counting rates binned on twenty-degree quasi-equal-area                 pixels is provided. The map was determined from a time series           of net counting rates for the 7.6 MeV gamma ray peak produced by        neutron capture with Fe within Ceres' regolith. The data were           acquired by Dawn's Gamma Ray and Neutron Detector (GRaND) while         in low altitude mapping orbit, about 385 km from Ceres' surface         (about 0.8 body radii altitude). Prior to mapping, the time             series counting data were subjected to corrections for variations       in the flux of galactic cosmic rays and measurement geometry,           as described by PRETTYMANETAL2017.",
-            "title": "DAWN GRAND MAP CERES IRON               \n                                      7.6MEV GAMMA COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN GRAND MAP CERES IRON               \n                                      7.6MEV GAMMA COUNTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/UMFN22VHGGMH",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge DMS L0 Raw Imagery, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/UMFN22VHGGMH.",
-            "issued": "2009-10-16",
-            "temporal": "2009-10-16T00:00:00Z/2018-04-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-19",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Roseanne Dominguez",
                 "hasEmail": "mailto:Roseanne.Dominguez@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386206948-NSIDCV0",
             "description": "This data set contains Level-0 imagery taken from the Digital Mapping System (DMS) over Antarctica and Greenland. The data were collected as part of Operation IceBridge funded aircraft survey campaigns.",
-            "title": "IceBridge DMS L0 Raw Imagery, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUMFN22VHGGMH",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUMFN22VHGGMH",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IODMS0_DMSraw_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IODMS0_DMSraw_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/UMFN22VHGGMH",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/UMFN22VHGGMH",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/UMFN22VHGGMH",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/UMFN22VHGGMH",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206948-NSIDCV0",
+            "issued": "2009-10-16",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/UMFN22VHGGMH",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2009-10-16T00:00:00Z/2018-04-19T23:59:59.999Z",
             "theme": [
                 "2009_AN_NASA",
                 "2010_AN_NASA",
@@ -1474971,162 +1474972,175 @@
                 "2018_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge DMS L0 Raw Imagery, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/LMOS/Ground_Milwaukee_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/LMOS/Ground_Milwaukee_Data_1. https://asdc.larc.nasa.gov/project/SEAC4RS.",
-            "issued": "2020-09-08",
-            "temporal": "2017-05-10T00:00:00Z/2017-06-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-02",
-            "keyword": [
-                "atmospheric chemistry",
-                "air quality",
-                "earth science",
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
-            "identifier": "C1966368550-LARC_ASDC",
             "description": "LMOS_Ground_Milwaukee_Data_1 is the Lake Michigan Ozone Study (LMOS) Milwaukee ground site data collected during the LMOS field campaign. This product is a result of a joint effort across multiple agencies, including NASA, NOAA, the EPA, Electric Power Research Institute (EPRI), National Science Foundation (NSF), Lake Michigan Air Directors Consortium (LADCO) and its member states, and several research groups at universities. Data collection is complete.\r\rElevated spring and summertime ozone levels remain a challenge along the coast of Lake Michigan, with a number of monitors exceeding the 2015 National Ambient Air Quality Standards (NAAQS) for ozone. The production of ozone over Lake Michigan, combined with onshore daytime \u201clake breeze\u201d airflow is believed to increase ozone concentrations at locations within a few kilometers off shore. This observed lake-shore gradient motivated the Lake Michigan Ozone Study (LMOS). Conducted from May through June 2017, the goal of LMOS was to better understand ozone formation and transport around Lake Michigan; in particular, why ozone concentrations are generally highest along the lakeshore and drop off sharply inland and why ozone concentrations peak in rural areas far from major emission sources. LMOS was a collaborative, multi-agency field study that provided extensive observational air quality and meteorology datasets through a combination of airborne, ship, mobile laboratories, and fixed ground-based observational platforms. Chemical transport models (CTMs) and meteorological forecast tools assisted in planning for day-to-day measurement strategies. The long term goals of the LMOS field study were to improve modeled ozone forecasts for this region, better understand ozone formation and transport around Lake Michigan, provide a better understanding of the lakeshore gradient in ozone concentrations (which could influence how the Environmental Protection Agency (EPA) addresses future regional ozone issues), and provide improved knowledge of how emissions influence ozone formation in the region.",
-            "title": "LMOS Milwaukee Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLMOS%2FGround_Milwaukee_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLMOS%2FGround_Milwaukee_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LMOS",
-                    "description": "ASDC Data and Information for LMOS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for LMOS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LMOS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/LMOS_FAQ_rev_jun5.pdf",
-                    "description": "Lake Michigan Ozone Study (LMOS 2017) FAQ",
                     "@type": "dcat:Distribution",
+                    "description": "Lake Michigan Ozone Study (LMOS 2017) FAQ",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/LMOS_FAQ_rev_jun5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/Great_Lakes_Ozone_Study_White_Paper_Draft_v6.pdf",
-                    "description": "White Paper: Lake Michigan Ozone Study 2017 (LMOS 2017)",
                     "@type": "dcat:Distribution",
+                    "description": "White Paper: Lake Michigan Ozone Study 2017 (LMOS 2017)",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/docs/Great_Lakes_Ozone_Study_White_Paper_Draft_v6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/",
-                    "description": "LMOS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/lmos/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/LMOS/Ground_Milwaukee_Data_1",
-                    "description": "DOI data set landing page for LMOS_Ground_Milwaukee_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for LMOS_Ground_Milwaukee_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/LMOS/Ground_Milwaukee_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1966368550-LARC_ASDC",
-                    "description": "Earthdata Search for LMOS_Ground_Milwaukee_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LMOS_Ground_Milwaukee_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1966368550-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LMOS/Ground_Milwaukee_Data_1/",
-                    "description": "ASDC Direct Data Download for LMOS_Ground_Milwaukee_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LMOS_Ground_Milwaukee_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LMOS/Ground_Milwaukee_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1966368550-LARC_ASDC",
+            "issued": "2020-09-08",
+            "keyword": [
+                "atmospheric chemistry",
+                "air quality",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/LMOS/Ground_Milwaukee_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-11-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-90.0 40.0 -85.0 45.0",
+            "temporal": "2017-05-10T00:00:00Z/2017-06-15T23:59:59Z",
             "theme": [
                 "LMOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LMOS Milwaukee Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-GIA-2-AST1-STEINSFLYBY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The report provides the results from GIADA experiment during theRosetta Steins Flyby. Asteroid Steins was the first dedicated scientific target of the Rosetta mission. Unfortunately the three subsystem of GIADA were not able to study Steins, so GIADA during asteroid flyby was in a non-nominal operational configuration, i.e.only the impact sensor operational and the cover closed. Therefore, during Steins fly-by we have only checked the status of GIADA instrument. Scientific operations targeting the asteroid started on 1 Sept. 2008 and ended on 10 Sept. 2008 and the Closest approach was on 5 Sept. 2008 at 18:38:20 UTC. Actually GIADA was in operation only the 5th Sept. 2008 just for 15 minutes. It also contains documentation which describes the GIADA experiment. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-gia-2-ast1-steinsflyby-v1.0_umgw-jp9e",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2867 steins",
                 "international rosetta mission",
                 "unknown"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-GIA-2-AST1-STEINSFLYBY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-gia-2-ast1-steinsflyby-v1.0_umgw-jp9e",
-            "description": "The report provides the results from GIADA experiment during theRosetta Steins Flyby. Asteroid Steins was the first dedicated scientific target of the Rosetta mission. Unfortunately the three subsystem of GIADA were not able to study Steins, so GIADA during asteroid flyby was in a non-nominal operational configuration, i.e.only the impact sensor operational and the cover closed. Therefore, during Steins fly-by we have only checked the status of GIADA instrument. Scientific operations targeting the asteroid started on 1 Sept. 2008 and ended on 10 Sept. 2008 and the Closest approach was on 5 Sept. 2008 at 18:38:20 UTC. Actually GIADA was in operation only the 5th Sept. 2008 just for 15 minutes. It also contains documentation which describes the GIADA experiment. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
-            "title": "ROSETTA-ORBITER STEINS GIADA 2 AST1 STEINSFLYBY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER STEINS GIADA 2 AST1 STEINSFLYBY V1.0"
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
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2009.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY09 NASA Budget Estimates",
+                    "downloadURL": "http://www.nasa.gov/pdf/210019main_NASA_FY09_Budget_Estimates.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FY09 NASA Budget Estimates"
+                }
+            ],
+            "identifier": "OCIO-Fitara-78",
             "issued": "2008-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "finance",
                 "financial",
@@ -1475135,47 +1475149,35 @@
                 "budget",
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
-            "identifier": "OCIO-Fitara-78",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2009.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2009: NASA Budget Estimates",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/210019main_NASA_FY09_Budget_Estimates.pdf",
-                    "description": "FY09 NASA Budget Estimates",
-                    "@type": "dcat:Distribution",
-                    "title": "FY09 NASA Budget Estimates"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2009: NASA Budget Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IRRDR-CLEANED-EXT4-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-irrdr-cleaned-ext4-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "sky",
                 "sun",
@@ -1475187,742 +1475189,754 @@
                 "comet",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IRRDR-CLEANED-EXT4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-irrdr-cleaned-ext4-v1.0",
-            "description": "The Mars Express SPICAM level 1A IR data set contains clean measurements from the infrared SPICAM spectrometer collected during the nominal MARS phases",
-            "title": "MEX EXT4 SPICAM MARS CLEANED IR RDR V1.0",
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
+            "title": "MEX EXT4 SPICAM MARS CLEANED IR RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0052",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0052.",
-            "issued": "2000-03-17",
-            "temporal": "1987-06-01T00:00:00Z/1992-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "earth science",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "altitude"
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
-            "identifier": "C1000001036-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.This data set contains sounding measurements taken in Funchal, Madeiras during June, 1987-1992. Six files contain 00Z data and five files contain 12Z data.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) INMG Funchal Sounding Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0052",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0052",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001036-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_SFC_FUNCHAL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_SFC_FUNCHAL_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001036-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sfc_func_read.c",
-                    "description": "Read Software - Standard C Library Call for FIRE ASTEX_SFC_FUNC_read.c - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software - Standard C Library Call for FIRE ASTEX_SFC_FUNC_read.c - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_sfc_func_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_sfc_dataset.pdf",
-                    "description": "FIRE ASTEX Surface Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Surface Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_sfc_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sfc_funchal_part2.ps",
-                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Readme - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_sfc_funchal_part2.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0052",
-                    "description": "DOI data set landing page for FIRE_AX_SFC_FUNCHAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_SFC_FUNCHAL_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0052",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_SFC_FUNCHAL/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_SFC_FUNCHAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_SFC_FUNCHAL_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_SFC_FUNCHAL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_SFC_FUNCHAL/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_SFC_FUNCHAL_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_SFC_FUNCHAL_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_SFC_FUNCHAL/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001036-LARC_ASDC",
+            "issued": "2000-03-17",
+            "keyword": [
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0052",
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
             "spatial": "32.66 -16.92",
+            "temporal": "1987-06-01T00:00:00Z/1992-06-30T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) INMG Funchal Sounding Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0489-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-14T06:44:15.000 to 2014-12-14T12:55:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0489-v1.0_umpk-a995",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0489-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0489-v1.0_umpk-a995",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-14T06:44:15.000 to 2014-12-14T12:55:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0489 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0489 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC1-3-RDR-CERES-IMAGES-V1.0",
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
-                "dawn mission to vesta and ceres",
-                "1 ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract                                                                   ========                                                                   This dataset contains calibrated Framing Camera 1 (FC1) images sometimes called level-1b or reduced data. It includes images from the Dawn Ceres  eXtended Mission 1 Orbit 3 (XMO3, aka Ceres Extended GRaND - CXG) phase  on 2017-02-19 and the Ceres eXtended Mission Orbit 4 (XMO4, aka Ceres    Extended Opposition - CXO) phase on 2017-04-29. In addition, there are   images from eXtended Mission 2 (XM2), orbits XMO6 (C2I - intermediate),  and XMO7 (C2E - elliptical) as well as some checkout and end-of-mission  star calibration images. FC1 is one of two identical units flying        on the Dawn spacecraft. It was designated as the backup system to be     used only in the event of a failure of the primary system, FC2. Prior to the Ceres extended mission, FC1 had only been used for in-flight         calibration and to periodically exercise its various mechanisms (door,   filter wheel, etc.). This is the only science dataset generated by FC1.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc1-3-rdr-ceres-images-v1.0_umpv-jrct",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "1 ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-FC1-3-RDR-CERES-IMAGES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-fc1-3-rdr-ceres-images-v1.0_umpv-jrct",
-            "description": "Abstract                                                                   ========                                                                   This dataset contains calibrated Framing Camera 1 (FC1) images sometimes called level-1b or reduced data. It includes images from the Dawn Ceres  eXtended Mission 1 Orbit 3 (XMO3, aka Ceres Extended GRaND - CXG) phase  on 2017-02-19 and the Ceres eXtended Mission Orbit 4 (XMO4, aka Ceres    Extended Opposition - CXO) phase on 2017-04-29. In addition, there are   images from eXtended Mission 2 (XM2), orbits XMO6 (C2I - intermediate),  and XMO7 (C2E - elliptical) as well as some checkout and end-of-mission  star calibration images. FC1 is one of two identical units flying        on the Dawn spacecraft. It was designated as the backup system to be     used only in the event of a failure of the primary system, FC2. Prior to the Ceres extended mission, FC1 had only been used for in-flight         calibration and to periodically exercise its various mechanisms (door,   filter wheel, etc.). This is the only science dataset generated by FC1.",
-            "title": "DAWN FC1 CALIBRATED CERES IMAGES V1.0",
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
+            "title": "DAWN FC1 CALIBRATED CERES IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-MAG-4-SUMM-U1COORDS-48SEC-V1.0",
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
-                "uranus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes data from the Low Field Magnetometer (LFM) in the during the Uranus encounter. The encounter data (1986-01-24T07:00:00  -> 1986-01-25T04:00:00) have been averaged from the 9.6 second averages to a 48 second resampled rate and are provided in the Uranus Longitude (U1) coordinate system. Magnetometer data in the solar wind are given in Heliographic coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-mag-4-summ-u1coords-48sec-v1.0_umq4-46in",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "uranus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-MAG-4-SUMM-U1COORDS-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-mag-4-summ-u1coords-48sec-v1.0_umq4-46in",
-            "description": "This data set includes data from the Low Field Magnetometer (LFM) in the during the Uranus encounter. The encounter data (1986-01-24T07:00:00  -> 1986-01-25T04:00:00) have been averaged from the 9.6 second averages to a 48 second resampled rate and are provided in the Uranus Longitude (U1) coordinate system. Magnetometer data in the solar wind are given in Heliographic coordinates.",
-            "title": "VG2 URA MAG RESAMPLED SUMMARY U1\n                                      COORDINATES 48SEC V1.0",
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
+            "title": "VG2 URA MAG RESAMPLED SUMMARY U1\n                                      COORDINATES 48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/CARBON_TRANSPORT_MS_RIVER/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/CARBON_TRANSPORT_MS_RIVER/DATA001.",
-            "issued": "2001-05-14",
-            "temporal": "2001-05-14T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "salinity/density",
-                "earth science",
-                "ocean chemistry",
-                "ocean optics",
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
-            "identifier": "C1633360175-OB_DAAC",
             "description": "Measurements made near the Mississippi River outflow region in the Gulf of Mexico between 2001 and 2003.",
-            "title": "Carbon transport in the Mississippi River",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCARBON_TRANSPORT_MS_RIVER%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FCARBON_TRANSPORT_MS_RIVER%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Carbon_Transport_MS_River/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Carbon_Transport_MS_River/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360175-OB_DAAC",
+            "issued": "2001-05-14",
+            "keyword": [
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/CARBON_TRANSPORT_MS_RIVER/DATA001",
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
+            "temporal": "2001-05-14T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon transport in the Mississippi River"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/266/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-11-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT POLL",
                 "hasEmail": "mailto:scott.d.poll@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_266",
             "description": "Synthetic Track Competition Data",
-            "title": "DXC'09 Synthetic Track Competition Data",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-gzip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DXC09_Synthetic_CompetitionData_1.1.tar.gz",
-                    "description": "Synthetic Track Competition Data",
                     "@type": "dcat:Distribution",
+                    "description": "Synthetic Track Competition Data",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/DXC09_Synthetic_CompetitionData_1.1.tar.gz",
+                    "mediaType": "application/x-gzip",
                     "title": "DXC09_Synthetic_CompetitionData_1.1.tar.gz"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_266",
+            "issued": "2010-11-22",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/266/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "DXC'09 Synthetic Track Competition Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0012",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0012.",
-            "issued": "1999-11-01",
-            "temporal": "1992-06-01T00:00:00Z/1992-07-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-05",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LAURENCE EYMARD",
                 "hasEmail": "mailto:laurence.eymard@cetp.ipsl.fr"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000981-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution clouddata.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.These files are calculations of the daily solar irradiance at the surface, based on observations by the METEOSAT. The file naming convention is: esqDDMMYYx.fis where DDMMYY is the dateThese files are: I2 pixels, 376 pixels/row, 326 rows. Each pixel has a spatial resolution of 0.04 degrees.The header of each file claims there are two channels, although the provided documentation states that there is only one channel per file.The units are: flux [tenths of Joule/cm^2]",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) Centre Meteorologie Spatiale (CMS) Daily Solar Irradiance Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0012",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0012",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000981-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_CMS_SOLAR_DY_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_CMS_SOLAR_DY_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000981-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_ax_cms_read.c",
-                    "description": "CMS Read program to interpret CMS binary raster data files - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "CMS Read program to interpret CMS binary raster data files - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_ax_cms_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fire_ax_cms",
-                    "description": "Makefile.fci2 Release: 1.1 Date: 3/22/94",
                     "@type": "dcat:Distribution",
+                    "description": "Makefile.fci2 Release: 1.1 Date: 3/22/94",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/Makefile.fire_ax_cms",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_cms_solar_dy_info1.txt",
-                    "description": "CMS Statement on satellite-based series of images as part of ASTEX Readme",
                     "@type": "dcat:Distribution",
+                    "description": "CMS Statement on satellite-based series of images as part of ASTEX Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_cms_solar_dy_info1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_cms_solar_dy.txt",
-                    "description": "Readme Information about the FIRE ASTEX CMS sample read software and data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the FIRE ASTEX CMS sample read software and data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_cms_solar_dy.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0012",
-                    "description": "DOI data set landing page for FIRE_AX_CMS_SOLAR_DY_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_CMS_SOLAR_DY_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0012",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_cms_dataset.pdf",
-                    "description": "FIRE ASTEX Centre de Meteorologie Spatiale (CMS) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX Centre de Meteorologie Spatiale (CMS) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_cms_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_CMS_SOLAR_DY/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_CMS_SOLAR_DY_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_CMS_SOLAR_DY_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_CMS_SOLAR_DY/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_CMS_SOLAR_DY/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_CMS_SOLAR_DY_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_CMS_SOLAR_DY_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_CMS_SOLAR_DY/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000981-LARC_ASDC",
+            "issued": "1999-11-01",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0012",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>27.01 -29.99 27.01 -14.99 40.01 -14.99 40.01 -29.99 27.01 -29.99</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-01T00:00:00Z/1992-07-02T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) Centre Meteorologie Spatiale (CMS) Daily Solar Irradiance Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2003-10-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0007.",
-            "issued": "2003-11-17",
-            "temporal": "2001-01-01T00:00:00Z/2002-02-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-07",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C1000000144-LARC_ASDC",
             "description": "The NARSTO_SOS_SC_UPSTATE_PM25_COMPOSITION data were collected during July 2001 and January of 2002 to elucidate the seasonal variability of the aerosols. Samples were collected at a rural location in South Carolina, beginning and ending at midnight in order to associate each sampling event with a calendar day. In all, 40 samples per month were collected (including blanks).The purpose of the study was to determine experimentally the concentration and chemical composition of fine particulate matter (PM2.5, particles with a diameter less than 2.5 um) in South Carolina. The collection of PM2.5 samples on Teflon filters was carried out using a cyclone-based system. Ion chromatography analysis for anions and cations was performed, as well as x-ray fluorescence (XRF) analysis for crustal metals. PM2.5 samples on quartz filters were also collected in order to determine the organic and elemental carbon (EC/OC) particle concentration.The average concentration for PM2.5 during July of 2001 was 20.85 mg/m3. The major components of the aerosol were organic compounds (38.5%) and sulfates (34.7%). During January of 2002, the average concentration for PM2.5 was 9.4 mg/m3. Again, the major components of the aerosol were organic compounds (64.1%) and sulfates (21.9%).NARSTO (formerly North American Research Strategy for Tropospheric Ozone) is a public/private partnership, whose membership spans government, the utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission is to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are available.",
-            "title": "NARSTO_SOS_SC_UPSTATE PM2.5 Composition Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0007",
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
-                    "downloadURL": "https://www.narsto.org/",
-                    "description": "NARSTO Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "NARSTO Project Home Page",
+                    "downloadURL": "https://www.narsto.org/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000144-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_SOS_SC_UPSTATE_PM25_COMPOSITION_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_SOS_SC_UPSTATE_PM25_COMPOSITION_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000144-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0007",
-                    "description": "DOI data set landing page for NARSTO_SOS_SC_UPSTATE_PM25_COMPOSITION_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_SOS_SC_UPSTATE_PM25_COMPOSITION_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0007",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_sos_sc_upstate_pm25_composition.pdf",
-                    "description": "Guide for NARSTO_SOS_SC_UPSTATE PM2.5 Composition Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO_SOS_SC_UPSTATE PM2.5 Composition Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_sos_sc_upstate_pm25_composition.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/SOS_SC_UPSTATE_PM25_COMPOSITION_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_SOS_SC_UPSTATE_PM25_COMPOSITION_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_SOS_SC_UPSTATE_PM25_COMPOSITION_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/SOS_SC_UPSTATE_PM25_COMPOSITION_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000144-LARC_ASDC",
+            "issued": "2003-11-17",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0007",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "34.58 -82.81",
+            "temporal": "2001-01-01T00:00:00Z/2002-02-01T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO_SOS_SC_UPSTATE PM2.5 Composition Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1320-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-07T22:35:20.000 to 2016-01-08T02:24:01.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1320-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1320-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1320-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-07T22:35:20.000 to 2016-01-08T02:24:01.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1320 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1320 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/un2z-2f5z",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Our study aims to comprehensively understand effects induced by the space environment on mammals. To achieve this aim we analyze the male mice housed under environments as the artificial gravity and the microgravity (space environment) in Japanese Experiment Module JEM) of the International Space Station (ISS) on orbit for 35 days. After recovered these mice on the ground transcriptome analysis by next-generation sequencing technology is performed about spleen to examine alteration of gene expression in the space.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-288",
+                    "mediaType": "text/html",
+                    "title": "Transcriptome analysis of murine spleen in space"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-288_un2z-2f5z",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "mouse habitation",
                 "nucleic acid sequencing",
@@ -1475934,546 +1475948,512 @@
                 "data transformation",
                 "library construction",
                 "animal husbandry",
-                "nucleic acid extraction"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "nasa_genelab_GLDS-288_un2z-2f5z",
-            "description": "Our study aims to comprehensively understand effects induced by the space environment on mammals. To achieve this aim we analyze the male mice housed under environments as the artificial gravity and the microgravity (space environment) in Japanese Experiment Module JEM) of the International Space Station (ISS) on orbit for 35 days. After recovered these mice on the ground transcriptome analysis by next-generation sequencing technology is performed about spleen to examine alteration of gene expression in the space.",
-            "title": "Transcriptome analysis of murine spleen in space",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-288",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcriptome analysis of murine spleen in space"
-                }
+                "nucleic acid extraction"
             ],
+            "landingPage": "https://data.nasa.gov/d/un2z-2f5z",
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
+            "title": "Transcriptome analysis of murine spleen in space"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/561",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wrigley, R.C., M.A. Spanner, and R.E. Slye. 2000. BOREAS Level-2 MAS Surface Reflectance and Temperature Images in BSQ Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/561",
-            "issued": "2023-11-22",
-            "temporal": "1994-07-21T00:00:00Z/1994-08-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-07",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric radiation"
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
-            "identifier": "C2813525557-ORNL_CLOUD",
             "description": "MAS images, along with other remotely sensed data, were collected to provide spatially extensive information over the primary study areas. This information includes biophysical parameter maps such as surface reflectance and temperature. Collection of the MAS images occurred over the study areas during the 1994 field campaigns.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Level-2 MAS Surface Reflectance and Temperature Images in BSQ Format",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F561",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F561",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/mas_lv2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/mas_lv2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/MAS_L2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/MAS_L2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/561",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/561",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/MAS_L2.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/MAS_L2.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/MAS_L2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/MAS_L2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/MAS_L2.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/MAS_L2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/mas_level_2_inv.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/mas_level_2_inv.dat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/mas_lv2.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/mas_lv2.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/mas_lv2/comp/README",
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
+            "identifier": "C2813525557-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/561",
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
             "spatial": "-106.32 53.42 -97.23 56.25",
+            "temporal": "1994-07-21T00:00:00Z/1994-08-08T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Level-2 MAS Surface Reflectance and Temperature Images in BSQ Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-ESC1-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V3.0 data set supersedes the previous V2.0 data set with improved documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-esc1-v3.0_un3u-j8qm",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-ESC1-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-esc1-v3.0_un3u-j8qm",
-            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V3.0 data set supersedes the previous V2.0 data set with improved documentation.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 ESC1 V3.0",
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
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 ESC1 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0298-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-16T17:05:04.000 to 2014-09-16T23:25:10.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0298-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0298-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0298-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-16T17:05:04.000 to 2014-09-16T23:25:10.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0298 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0298 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MODBMSS.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Terra Atmosphere BELMANIP Subsetting Product. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MODBMSS.061. https://doi.org/10.5067/MODIS/MODBMSS.061.",
-            "issued": "2017-10-01",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-10",
-            "keyword": [
-                "spectral/engineering",
-                "ngda",
-                "visible wavelengths",
-                "national geospatial data asset",
-                "earth science",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASAD ULLAH",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1444771617-LAADS",
-            "description": "The MODIS/Terra Atmosphere BELMANIP subsetting Product (MODBMSS) consists of MODIS Atmosphere and Ancillary Products subsets that are generated over the Bench-mark Land Multisite Analysis and Intercomparison of Products (BELMANIP) sites. The BELMANIP sites is a network of sites, distributed globally and consist of existing networks such as Earth Observing System (EOS) Core Sites, Bigfoot, Validation of Land European Remote sensing Instruments (VALERI), a global network of micrometeorological flux measurement (FLUXNET), the aerosol robotic network (AERONET) and a set of additional sites.The process of generating cutouts for these sites involves locating and identifying a subset of sites taken from global BELMANIP sites that are within the spatial coverage of a 5 minute Level 2 MODIS granule and extracting 0.5 x 0.5 degree cutouts. The MODBMSS data set consists of subsets for approximately 445 sites around the globe. There is one file per site with 55 Science Data Sets (SDS) such as at-aperture radiances for 36 discrete MODIS bands, Cloud Mask, and Water Vapor, etc.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Terra Atmosphere BELMANIP Subsetting Product",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra Atmosphere BELMANIP subsetting Product (MODBMSS) consists of MODIS Atmosphere and Ancillary Products subsets that are generated over the Bench-mark Land Multisite Analysis and Intercomparison of Products (BELMANIP) sites. The BELMANIP sites is a network of sites, distributed globally and consist of existing networks such as Earth Observing System (EOS) Core Sites, Bigfoot, Validation of Land European Remote sensing Instruments (VALERI), a global network of micrometeorological flux measurement (FLUXNET), the aerosol robotic network (AERONET) and a set of additional sites.The process of generating cutouts for these sites involves locating and identifying a subset of sites taken from global BELMANIP sites that are within the spatial coverage of a 5 minute Level 2 MODIS granule and extracting 0.5 x 0.5 degree cutouts. The MODBMSS data set consists of subsets for approximately 445 sites around the globe. There is one file per site with 55 Science Data Sets (SDS) such as at-aperture radiances for 36 discrete MODIS bands, Cloud Mask, and Water Vapor, etc.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMODBMSS.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMODBMSS.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MODBMSS.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MODBMSS.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MODBMSS--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MODBMSS--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MODBMSS/",
-                    "description": "Direct access to MODBMSS C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MODBMSS C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MODBMSS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MODBMSS/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MODBMSS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1444771617-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "spectral/engineering",
+                "ngda",
+                "visible wavelengths",
+                "national geospatial data asset",
+                "earth science",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MODBMSS.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Atmosphere BELMANIP Subsetting Product"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-4-VIRS-DDR-V1.0",
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
-                "messenger"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS derived observations, also known as DDRs. The MASCS VIRS experiment is a fixed concave grating spectrograph with a beam splitter that simultaneously disperses the spectrum onto two photodiode arrays. There are two VIRS DDR data products, one for each array, which result in coverage of the wavelength ranges of the visible (VIS) and near infrared (NIR).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-4-virs-ddr-v1.0_un7e-49t3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mercury",
+                "messenger"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-4-VIRS-DDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-4-virs-ddr-v1.0_un7e-49t3",
-            "description": "Abstract ======== This data set consists of the MESSENGER MASCS VIRS derived observations, also known as DDRs. The MASCS VIRS experiment is a fixed concave grating spectrograph with a beam splitter that simultaneously disperses the spectrum onto two photodiode arrays. There are two VIRS DDR data products, one for each array, which result in coverage of the wavelength ranges of the visible (VIS) and near infrared (NIR).",
-            "title": "MESSENGER E/V/H MASCS 4 VIRS DERIVED DATA V1.0",
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
+            "title": "MESSENGER E/V/H MASCS 4 VIRS DERIVED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-IR-VESTA-SPECTRA-V2.0",
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
-                "dawn mission to vesta and ceres",
-                "4 vesta"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the raw           infrared channel digital numbers (DN) contained in the telemetry         packages taken by the Dawn VIR spectrometer for all Vesta encounter      mission phaes. The data in this version of the data set include          minor updates to the data files and labels. The data cover the time      period between 2011-05-03 and 2012-07-18.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-ir-vesta-spectra-v2.0_un7q-dmwk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-VIR-2-EDR-IR-VESTA-SPECTRA-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-vir-2-edr-ir-vesta-spectra-v2.0_un7q-dmwk",
-            "description": "This data set contains the raw           infrared channel digital numbers (DN) contained in the telemetry         packages taken by the Dawn VIR spectrometer for all Vesta encounter      mission phaes. The data in this version of the data set include          minor updates to the data files and labels. The data cover the time      period between 2011-05-03 and 2012-07-18.",
-            "title": "DAWN VIR RAW (EDR) VESTA INFRARED SPECTRA V2.0",
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
+            "title": "DAWN VIR RAW (EDR) VESTA INFRARED SPECTRA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAMEX-4/RADIOMETER/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Knupp, Kevin  and Justin  Walters.2002. CAMEX-4 MIPS MICROWAVE PROFILING RADIOMETER [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CAMEX-4/RADIOMETER/DATA301",
-            "issued": "2002-08-28",
-            "temporal": "2001-08-15T14:22:32Z/2001-09-12T13:19:54Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "atmosphere",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science",
-                "precipitation",
-                "atmospheric radiation",
-                "atmospheric temperature"
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
-            "identifier": "C1979100507-GHRC_DAAC",
             "description": "The University of Alabama in Huntsville (UAH) Mobile Integrated Profiling System (MIPS) is a mobile atmospheric profiling system. It includes a 915 MHz Doppler profiler, lidar ceilometer, 12 channel microwave profiling radiometer, Doppler Sodar, Radio Acoustic Sounding System (RASS), Field Mills, and surface observing station. The 12 channel microwave profiling radiometer provides profiles of temperature, water vapor and liquid water and integrated values of water vapor and liquid water from the surface to 10km every ~ 15 minutes. Cloud base temperature is also measured.",
-            "title": "CAMEX-4 MIPS MICROWAVE PROFILING RADIOMETER V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FRADIOMETER%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAMEX-4%2FRADIOMETER%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4gmipmpr",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=c4gmipmpr",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4gmipmpr/c4gmipmpr_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/camex4/c4gmipmpr/c4gmipmpr_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1979100507-GHRC_DAAC",
+            "issued": "2002-08-28",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science",
+                "precipitation",
+                "atmospheric radiation",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAMEX-4/RADIOMETER/DATA301",
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
             "spatial": "-81.7 24.6 -81.5 24.8",
+            "temporal": "2001-08-15T14:22:32Z/2001-09-12T13:19:54Z",
             "theme": [
                 "CAMEX-4",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMEX-4 MIPS MICROWAVE PROFILING RADIOMETER V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-PRL-67P-M09-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-prl-67p-m09-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-5-PRL-67P-M09-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-5-prl-67p-m09-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 5 PRL-MTP009 DDR-GEO V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 5 PRL-MTP009 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PRISM/CORAL/L2/RBEN/V1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC. https://doi.org/10.5067/PRISM/CORAL/L2/RBEN/V1.",
-            "issued": "2016-06-20",
-            "temporal": "2016-06-20T00:00:00Z/2017-05-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-28",
-            "keyword": [
-                "ocean optics",
-                "ocean chemistry",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:webadmin@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1653653611-OB_DAAC",
             "description": "Flight line benthic cover measurements from the Portable Remote Imaging Spectrometer (PRISM) instrument aboard the Tempus Applied Solutions Gulfstream-IV (G-IV) aircraft, taken as part of the NASA COral Reef Airborne Laboratory (CORAL) Earth Venture Suborbital-2 (EVS-2) mission designed to provide an extensive, uniform picture of coral reef composition. The CORAL mission surveyed parts of the reefs surrounding the Mariana Islands, Palau, portions of the Great Barrier Reef, the main Hawaiian Islands, and the Florida Keys.",
-            "title": "Portable Remote Imaging Spectrometer (PRISM) COral Reef Airborne Laboratory (CORAL) Regional Benthic Cover Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRISM%2FCORAL%2FL2%2FRBEN%2FV1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRISM%2FCORAL%2FL2%2FRBEN%2FV1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1476483,486 +1476463,478 @@
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1653653611-OB_DAAC",
+            "issued": "2016-06-20",
+            "keyword": [
+                "ocean optics",
+                "ocean chemistry",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/PRISM/CORAL/L2/RBEN/V1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-05-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-06-20T00:00:00Z/2017-05-28T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Portable Remote Imaging Spectrometer (PRISM) COral Reef Airborne Laboratory (CORAL) Regional Benthic Cover Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/EOR3XUV9POHR",
             "citation": "William E. Shenk. 2024-10-25. GVHRRATS6IMIR. Version 001. GVHRR/ATS-6 Black and White Infrared Images on Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/EOR3XUV9POHR. https://disc.gsfc.nasa.gov/datacollection/GVHRRATS6IMIR_001.html. Digital Science Data.",
-            "issued": "2019-03-08",
-            "temporal": "1974-06-07T00:00:00Z/1974-08-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-08",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "William E. Shenk",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C3275628922-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "GVHRRATS6IMIR is the Geosynchronous Very High Resolution Radiometer (GVHRR) Black and White Infrared Images on 70mm Film data product from the sixth Applications Technology Satellite (ATS-6). This set of IR imagery (10.5 to 12.5 micrometer, with an 11 km footprint at the sub-satellite point) was originally produced on commercial image-generation equipment from digital tapes and was made available on 70-mm film, from which they were later scanned to digital TIFF image files. Each TIFF scan contains 2 or 3 pictures, and there are several hundred scans from an original 70 mm film roll which are combined into a ZIP file. Each picture contains a title at the bottom of the image and a gray scale on the right boundary that represents brightness temperatures. The title contains the satellite identification, receiving station, spectral band, picture number, picture type, pixel scale, sector number, and date.\n\nThe ATS-6 satellite was in a geosynchronous orbit parked at 95W viewing the hemisphere below the satellite. The GVHRR experiment returned data from launch until August 15, 1974 when it became inoperable, The PI was William E. Shenk from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00092 (old ID 74-039A-08B).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GVHRRATS6IMIR",
-            "creator": "William E. Shenk",
-            "title": "GVHRR/ATS-6 Black and White Infrared Images on Film V001 (GVHRRATS6IMIR) at GES DISC",
-            "graphic-preview-description": "Typical GVHRR/ATS-6 infrared film image.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GVHRRATS6IMIR_001.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEOR3XUV9POHR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEOR3XUV9POHR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GVHRRATS6IMIR_001.png",
-                    "description": "Typical GVHRR/ATS-6 infrared film image.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical GVHRR/ATS-6 infrared film image.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GVHRRATS6IMIR_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GVHRRATS6IMIR_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GVHRRATS6IMIR_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/GVHRRATS6IMIR.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/GVHRRATS6IMIR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GVHRRATS6IMIR",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GVHRRATS6IMIR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/GVHRRATS6IMIR.001/doc/README.GVHRRATS6IM.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/GVHRRATS6IMIR.001/doc/README.GVHRRATS6IM.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/ATS6/ATS6_Inventory.xlsx",
-                    "description": "ATS-6 Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "ATS-6 Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/ATS6/ATS6_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Typical GVHRR/ATS-6 infrared film image.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GVHRRATS6IMIR_001.png",
+            "identifier": "C3275628922-GES_DISC",
+            "issued": "2019-03-08",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/EOR3XUV9POHR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GVHRRATS6IMIR",
             "spatial": "175.0 -90.0 -5.0 90.0",
+            "temporal": "1974-06-07T00:00:00Z/1974-08-15T23:59:59.999Z",
             "theme": [
                 "EOSDIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GVHRR/ATS-6 Black and White Infrared Images on Film V001 (GVHRRATS6IMIR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA-MODIS/CERES/SYN1DEG-MHOUR_L3.004A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-09-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA-MODIS/CERES/SYN1DEG-MHOUR_L3.004A.",
-            "issued": "2017-09-12",
-            "temporal": "2000-03-01T00:00:00Z/2002-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-13",
-            "keyword": [
-                "national geospatial data asset",
-                "atmospheric pressure",
-                "clouds",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "earth science",
-                "atmosphere",
-                "ngda",
-                "vegetation",
-                "biosphere",
-                "atmospheric water vapor",
-                "aerosols"
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
-            "identifier": "C1419910528-LARC_ASDC",
             "description": "CER_SYN1deg-MHour_Terra-MODIS_Edition4A is the Clouds and the Earth's Radiant Energy System (CERES) and geostationary (GEO)-Enhanced Top-of-Atmosphere (TOA), Within-Atmosphere and Surface Fluxes, Clouds and Aerosols Monthly-Averaged 1-Hourly Terra Edition4A data product. Data was collected using the CERES Imaging Radiometers on the Geostationary Satellites platform and CERES Flight Model 1 (FM1), FM2, CERES Scanner, and Moderate-Resolution Imaging Spectroradiometer (MODIS) on the Terra platform. Data collection for this product is complete.\r\n\r\nThe CERES Synoptic (SYN) 1 degree (SYN1deg) products provide CERES-observed temporally interpolated TOA radiative fluxes and coincident MODIS-derived cloud and aerosol properties and include geostationary-derived cloud properties and broadband fluxes that have been carefully normalized with CERES fluxes in order to maintain the CERES calibration. They also contain computed initial TOA, in-atmosphere, and surface fluxes and computed fluxes that have been adjusted or constrained to the CERES-observed TOA fluxes. The computed fluxes are produced using the Langley Fu-Liou radiative transfer model. Computations use MODIS and geostationary satellite cloud properties along with atmospheric profiles provided by the Global Modeling and Assimilation Office (GMAO). The adjustments to clouds and atmospheric properties are also provided. The computations are made for all-sky, clear-sky, pristine (clear-sky without aerosols), and all-sky without aerosol conditions. This product provides parameters on a monthly-averaged one-hourly temporal resolution and 1\u00b0-regional spatial scales. Fluxes are provided for clear-sky and all-sky conditions in the longwave (LW), shortwave (SW), and window (WN) regions.\r\n\r\nThe CERES SYN1deg products use 1-hourly radiances and cloud property data from geostationary (GEO) imagers to more accurately model variability between CERES observations. To use GEO data to enhance diurnal sampling, several steps are involved. First, GEO radiances are cross-calibrated with the MODIS imager using only data that is coincident in time and ray-matched in angle. Next, the GEO cloud retrievals are inferred from the calibrated GEO radiances. The GEO radiances are converted from narrowband to broadband using empirical regressions and then to broadband GEO TOA fluxes using Angular Distribution Models (ADMs) and directional models. To ensure GEO and CERES TOA fluxes are consistent, a normalization technique is used. Instantaneous matched gridded fluxes from CERES and GEO are regressed against one another over a month from 5\u00b0x5 \u00b0 latitude-longitude regions. The regression relation is then applied to all GEO fluxes to remove biases that depend upon cloud amount, solar and view zenith angles, and regional dependencies. The regional means are determined for 1\u00b0 equal-angle grid boxes calculated by first interpolating each parameter for any missing times of the CERES/GEO observations to produce a complete 1-hourly time series for the month. Monthly means are calculated using the combination of observed and interpolated parameters from all days containing at least one CERES observation.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. Th",
-            "title": "CERES and GEO-Enhanced TOA, Within-Atmosphere and Surface Fluxes, Clouds and Aerosols Monthly-Averaged 1-Hourly Terra Edition4A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA-MODIS%2FCERES%2FSYN1DEG-MHOUR_L3.004A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA-MODIS%2FCERES%2FSYN1DEG-MHOUR_L3.004A",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CERES",
-                    "description": "ASDC Data and Information for CERES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CERES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CERES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA-MODIS/CERES/SYN1DEG-MHOUR_L3.004A",
-                    "description": "DOI data set landing page for CER_SYN1deg-MHour_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SYN1deg-MHour_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://doi.org/10.5067/TERRA-MODIS/CERES/SYN1DEG-MHOUR_L3.004A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/TISAavg_SampleRead_SYN1deg_R5-922.zip",
-                    "description": "Read Software Package - SYN1deg - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - SYN1deg - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/TISAavg_SampleRead_SYN1deg_R5-922.zip",
+                    "mediaType": "application/zip",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf",
-                    "description": "CERES SYN1deg Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES SYN1deg Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_syn1deg.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS.pdf",
-                    "description": "Quality Summary: CERES_SYN1deg_Ed4A (10/3/2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_SYN1deg_Ed4A (10/3/2017)",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SYN1deg_Ed4A_DQS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1419910528-LARC_ASDC",
-                    "description": "Earthdata Search for CER_SYN1deg-MHour_Terra-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_SYN1deg-MHour_Terra-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1419910528-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/CERES",
-                    "description": "NASA Earthdata Forum - CERES",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - CERES",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/CERES",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
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
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
-                    "description": "NASA Earth Observatory Article: Aqua CERES First Light: Image of the Day\u00a0-\u00a0The Clouds and the Earth's Radiant Energy System (CERES) instrument is one of six on board the Aqua satellite.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Aqua CERES First Light: Image of the Day\u00a0-\u00a0The Clouds and the Earth's Radiant Energy System (CERES) instrument is one of six on board the Aqua satellite.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
-                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day\u00a0-\u00a0Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day\u00a0-\u00a0Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
-                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day\u00a0- These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day\u00a0- These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
-                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction\u00a0-\u00a0Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction\u00a0-\u00a0Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
-                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog\u00a0-\u00a0Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog\u00a0-\u00a0Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
-                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation\u00a0-\u00a0These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation\u00a0-\u00a0These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/global-maps/CERES_NETFLUX_M",
-                    "description": "NASA Earth Observatory Article: Net Radiation\u00a0-\u00a0The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Net Radiation\u00a0-\u00a0The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
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
-                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet\u00a0-\u00a0Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that...",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet\u00a0-\u00a0Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that...",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/AM1/terra_animations.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.\u00a0",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
-                    "description": "NASA Earth Observatory Article: The Water Cycle\u00a0-\u00a0MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Water Cycle\u00a0-\u00a0MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2984/tropical-cloud-systems-and-ceres",
-                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day\u00a0-\u00a0CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day\u00a0-\u00a0CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#Terra",
-                    "description": "CERES Overview of Terra",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of Terra",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#Terra",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SYNI_R5V1.pdf",
-                    "description": "CERES Data Products Catalog R5V1 11/22/2013 Synoptic Radiative Fluxes and Clouds Intermediate (SYNI)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R5V1 11/22/2013 Synoptic Radiative Fluxes and Clouds Intermediate (SYNI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_SYNI_R5V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/JTECHA_2590.pdf",
-                    "description": "Angular Distribution Models for Top-of-Atmosphere Radiative Flux Estimation from the Clouds and the Earth\u2019s Radiant Energy System Instrument on the Terra Satellite. Part II: Validation",
                     "@type": "dcat:Distribution",
+                    "description": "Angular Distribution Models for Top-of-Atmosphere Radiative Flux Estimation from the Clouds and the Earth\u2019s Radiant Energy System Instrument on the Terra Satellite. Part II: Validation",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/JTECHA_2590.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/region_mean_attach_C.pdf",
-                    "description": "CERES/Terra Regional Mean TOA Flux Uncertainties",
                     "@type": "dcat:Distribution",
+                    "description": "CERES/Terra Regional Mean TOA Flux Uncertainties",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/region_mean_attach_C.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's documented anomalies"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/#syn1deg-level-3",
-                    "description": "CERES Data Page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/#syn1deg-level-3",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
@@ -1476972,62 +1476944,69 @@
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SYN1deg-MHour/Terra-MODIS_Edition4A/",
-                    "description": "ASDC Direct Data Download for CER_SYN1deg-MHour_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SYN1deg-MHour_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SYN1deg-MHour/Terra-MODIS_Edition4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SYN1deg-MHour/Terra-MODIS_Edition4A/contents.html",
-                    "description": "OPeNDAP data access for CER_SYN1deg-MHour_Terra-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SYN1deg-MHour_Terra-MODIS_Edition4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SYN1deg-MHour/Terra-MODIS_Edition4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1419910528-LARC_ASDC",
+            "issued": "2017-09-12",
+            "keyword": [
+                "national geospatial data asset",
+                "atmospheric pressure",
+                "clouds",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "earth science",
+                "atmosphere",
+                "ngda",
+                "vegetation",
+                "biosphere",
+                "atmospheric water vapor",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA-MODIS/CERES/SYN1DEG-MHOUR_L3.004A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-03-01T00:00:00Z/2002-06-30T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES and GEO-Enhanced TOA, Within-Atmosphere and Surface Fluxes, Clouds and Aerosols Monthly-Averaged 1-Hourly Terra Edition4A"
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
-                "appel",
-                "sharing",
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
-            "identifier": "NASA-862__23",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1477035,118 +1477014,115 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__23",
+            "issued": "2018-06-25",
+            "keyword": [
+                "appel",
+                "sharing",
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
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206746-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Permafrost monitoring and prediction in Southern Carpathians, Romania, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1986-01-01",
-            "temporal": "1986-01-01T00:00:00Z/1994-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1994-12-31",
-            "keyword": [
-                "earth science",
-                "frozen ground",
-                "land surface",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Petru Urdea",
                 "hasEmail": "mailto:aardelean@mail.dnttm.ro"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206746-NSIDCV0",
             "description": "This study monitored the summer temperatures (July and August)  of the springs at the base of the rock glaciers' fronts and talus cones of Fagaras and Retezat Mountains. These water measurements have been made since 1986. BTS  (bottom temperature of snow) measurements were made in the same areas during  the second and third weeks of February since 1992.  Data are presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Permafrost monitoring and prediction in Southern Carpathians, Romania, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD30_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD30_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD30/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD30/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD30/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD30/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206746-NSIDCV0",
+            "issued": "1986-01-01",
+            "keyword": [
+                "earth science",
+                "frozen ground",
+                "land surface",
+                "cryosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206746-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1994-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "22.717 45.283 25.05 45.683",
+            "temporal": "1986-01-01T00:00:00Z/1994-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Permafrost monitoring and prediction in Southern Carpathians, Romania, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Y7QUDGMD2HUG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Junjie Liu and Kevin Bowman. 2020-09-28. CMSFluxFossilFuelPrior. Version 3. Carbon Monitoring System Carbon Flux FossilFuel Prior L4 V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Y7QUDGMD2HUG. https://disc.gsfc.nasa.gov/datacollection/CMSFluxFossilFuelPrior_3.html. Digital Science Data.",
-            "issued": "2017-04-26",
-            "temporal": "2010-01-01T00:00:00Z/2022-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-08-18",
-            "keyword": [
-                "ocean chemistry",
-                "oceans",
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Bowman",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C3005726524-GES_DISC",
-            "description": "This dataset provides the Prior for the Fossil Fuel Carbon Flux.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMSFluxFossilFuelPrior",
             "creator": "Junjie Liu and Kevin Bowman",
-            "title": "Carbon Monitoring System Carbon Flux FossilFuel Prior L4 V3 (CMSFluxFossilFuelPrior)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxFossilFuelPrior_3.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This dataset provides the Prior for the Fossil Fuel Carbon Flux.\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY7QUDGMD2HUG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FY7QUDGMD2HUG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1477156,233 +1477132,271 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxFossilFuelPrior_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMSFluxFossilFuelPrior_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFossilFuelPrior.3/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMSFluxFossilFuelPrior.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxFossilFuelPrior.3/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CMS/CMSFluxFossilFuelPrior.3/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/README.CMS_Flux_V3.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/README.CMS_Flux_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://carbon.nasa.gov/",
-                    "description": "The NASA Carbon Monitoring System (CMS) page.",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA Carbon Monitoring System (CMS) page.",
+                    "downloadURL": "https://carbon.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSFluxFossilFuelPrior",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMSFluxFossilFuelPrior",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMSFluxFossilFuelPrior_3.png",
+            "identifier": "C3005726524-GES_DISC",
+            "issued": "2017-04-26",
+            "keyword": [
+                "ocean chemistry",
+                "oceans",
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Y7QUDGMD2HUG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-08-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CMSFluxFossilFuelPrior",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-01-01T00:00:00Z/2022-12-31T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Carbon Monitoring System Carbon Flux FossilFuel Prior L4 V3 (CMSFluxFossilFuelPrior)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/np6p-qe61",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University, CUNY Institute for Demographic Research - CIDR - City University of New York, International Food Policy Research Institute - IFPRI, The World Bank, and Centro Internacional de Agricultura Tropical - CIAT. 2021-02-24. Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extent Polygons, Revision 02. Version 1.02. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/np6p-qe61. https://doi.org/10.7927/np6p-qe61.",
-            "issued": "2021-02-24",
-            "temporal": "1995-07-01T00:00:00Z/1995-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-24",
-            "references": [
-                "https://doi.org/10.7927/H4VT1Q1H",
-                "https://doi.org/10.7927/H4CR5R8J",
-                "https://doi.org/10.7927/H44B2Z74",
-                "https://doi.org/10.7927/H40K26HS",
-                "https://doi.org/10.7927/H4R20Z93",
-                "https://doi.org/10.7927/H4M906KR",
-                "https://doi.org/10.7927/H4GH9FVG",
-                "https://doi.org/10.7927/H48050JH",
-                "https://doi.org/10.7927/H4BC3WG1",
-                "https://doi.org/10.7927/xnyy-4s75"
-            ],
-            "keyword": [
-                "boundaries",
-                "human dimensions",
-                "earth science"
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
-            "identifier": "C2210244511-SEDAC",
-            "description": "The Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extent Polygons, Revision 02 is an update to Revision 01, which included new settlements and represented the first time that SEDAC released polygons (in Esri shapefile format) with the settlement name (or name of the largest city in the case of multi-city agglomerations). The shapefile consists of polygons defined by the extent of the nighttime lights and approximated urban extents (circles) based on buffered settlement points. Revision 01 also included new urban extents identified from multiple sources and corrected georeferencing for some settlements (see separate documentation for Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Settlement Points, Revision 01 for the data and methods). Revision 01 was produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with CUNY Institute for Demographic Research (CIDR). Revision 02 was produced by CIESIN.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University, CUNY Institute for Demographic Research - CIDR - City University of New York, International Food Policy Research Institute - IFPRI, The World Bank, and Centro Internacional de Agricultura Tropical - CIAT",
-            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extent Polygons, Revision 02",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-urban-ext-polygons-rev02/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extent Polygons, Revision 02 is an update to Revision 01, which included new settlements and represented the first time that SEDAC released polygons (in Esri shapefile format) with the settlement name (or name of the largest city in the case of multi-city agglomerations). The shapefile consists of polygons defined by the extent of the nighttime lights and approximated urban extents (circles) based on buffered settlement points. Revision 01 also included new urban extents identified from multiple sources and corrected georeferencing for some settlements (see separate documentation for Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Settlement Points, Revision 01 for the data and methods). Revision 01 was produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with CUNY Institute for Demographic Research (CIDR). Revision 02 was produced by CIESIN.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fnp6p-qe61",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fnp6p-qe61",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-urban-ext-polygons-rev02/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-urban-ext-polygons-rev02/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-ext-polygons-rev02/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-ext-polygons-rev02/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-ext-polygons-rev02/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-ext-polygons-rev02/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-ext-polygons-rev02",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-ext-polygons-rev02",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-urban-ext-polygons-rev02/sedac-logo.jpg",
+            "identifier": "C2210244511-SEDAC",
+            "issued": "2021-02-24",
+            "keyword": [
+                "boundaries",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/np6p-qe61",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-24",
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
+                "https://doi.org/10.7927/H4GH9FVG",
+                "https://doi.org/10.7927/H48050JH",
+                "https://doi.org/10.7927/H4BC3WG1",
+                "https://doi.org/10.7927/xnyy-4s75"
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
+            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extent Polygons, Revision 02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M17-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m17-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M17-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m17-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP017 RDR-INFLDSTR V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP017 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCC10-V1.0",
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
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Solar Corona Characterization Experiment (SCC10) Raw Data Archive is a time-ordered collection of radio science raw data acquired from October 5 to November 14, 2012, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-scc10-v1.0_unsm-imb2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCC10-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-scc10-v1.0_unsm-imb2",
-            "description": "The Cassini Radio Science Solar Corona Characterization Experiment (SCC10) Raw Data Archive is a time-ordered collection of radio science raw data acquired from October 5 to November 14, 2012, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SCC10 V1.0",
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
+            "title": "CASSINI RSS RAW DATA SET - SCC10 V1.0"
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
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2011.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY11 NASA Budget Overview",
+                    "downloadURL": "http://www.nasa.gov/pdf/420990main_FY_201_%20Budget_Overview_1_Feb_2010.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NASA FY11 Budget Overview"
+                }
+            ],
+            "identifier": "OCIO-Fitara-72",
             "issued": "2010-02-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "financial",
                 "strategic",
@@ -1477391,1031 +1477405,991 @@
                 "budget",
                 "finance"
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
-            "identifier": "OCIO-Fitara-72",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2011.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2011: NASA Budget Overview",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/420990main_FY_201_%20Budget_Overview_1_Feb_2010.pdf",
-                    "description": "FY11 NASA Budget Overview",
-                    "@type": "dcat:Distribution",
-                    "title": "NASA FY11 Budget Overview"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2011: NASA Budget Overview"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/6MLZSLRBL67U",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Greenland Annual Accumulation along the EGIG Line, 1959\u20132004, from Airborne Radar and Neutron Probe Densities, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/6MLZSLRBL67U.",
-            "issued": "1959-10-01",
-            "temporal": "1959-10-01T00:00:00Z/2004-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-09-30",
-            "keyword": [
-                "cryosphere",
-                "earth science",
-                "snow/ice"
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
-            "identifier": "C1436304012-NSIDCV0",
             "description": "This data set reports mean annual snow accumulation rates in meters water equivalent (m\u00b7w.e.) from 1959 to 2004 along a 250 km segment of the Exp\u00e9ditions Glaciologiques Internationales au Groenland (EGIG) line. Accumulation rates are derived from Airborne SAR/Interferometric Radar Altimeter System (ASIRAS) data and high resolution neutron-probe (NP) density profiles.",
-            "title": "Greenland Annual Accumulation along the EGIG Line, 1959\u20132004, from Airborne Radar and Neutron Probe Densities, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6MLZSLRBL67U",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F6MLZSLRBL67U",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0644_EGIG_line_v01",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0644_EGIG_line_v01",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0644_EGIG_line_v01",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0644_EGIG_line_v01",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6MLZSLRBL67U",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/6MLZSLRBL67U",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/6MLZSLRBL67U",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/6MLZSLRBL67U",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1436304012-NSIDCV0",
+            "issued": "1959-10-01",
+            "keyword": [
+                "cryosphere",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/6MLZSLRBL67U",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-42.838297 70.585609 -36.232431 71.207715",
+            "temporal": "1959-10-01T00:00:00Z/2004-09-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Greenland Annual Accumulation along the EGIG Line, 1959\u20132004, from Airborne Radar and Neutron Probe Densities, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/837/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-09-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER HEEG",
                 "hasEmail": "mailto:jennifer.heeg@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_837",
             "description": "Images for RSW configuration.",
-            "title": "images_RSW",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDatatable_unsteady_10Hz.png",
-                    "description": "RSW_expDatatable_unsteady_10Hz.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expDatatable_unsteady_10Hz.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDatatable_unsteady_10Hz.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expDatatable_unsteady_10Hz.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDataplots_unsteady_20Hz.png",
-                    "description": "RSW_expDataplots_unsteady_20Hz.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expDataplots_unsteady_20Hz.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDataplots_unsteady_20Hz.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expDataplots_unsteady_20Hz.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDatatable_unsteady_20Hz.png",
-                    "description": "RSW_expDatatable_unsteady_20Hz.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expDatatable_unsteady_20Hz.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDatatable_unsteady_20Hz.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expDatatable_unsteady_20Hz.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDataplots_unsteady_10Hz.png",
-                    "description": "RSW_expDataplots_unsteady_10Hz.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expDataplots_unsteady_10Hz.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDataplots_unsteady_10Hz.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expDataplots_unsteady_10Hz.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDatatable_steady_aoa4.png",
-                    "description": "RSW_expDatatable_steady_aoa4.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expDatatable_steady_aoa4.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDatatable_steady_aoa4.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expDatatable_steady_aoa4.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDatatable_steady_aoa2.png",
-                    "description": "RSW_expDatatable_steady_aoa2.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expDatatable_steady_aoa2.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expDatatable_steady_aoa2.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expDatatable_steady_aoa2.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expTabpts_Unsteady.png",
-                    "description": "RSW_expTabpts_Unsteady.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expTabpts_Unsteady.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expTabpts_Unsteady.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expTabpts_Unsteady.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expTabpts_Steady.png",
-                    "description": "RSW_expTabpts_Steady.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expTabpts_Steady.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expTabpts_Steady.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expTabpts_Steady.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expdata_FRFexamples.png",
-                    "description": "RSW_expdata_FRFexamples.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_expdata_FRFexamples.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_expdata_FRFexamples.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_expdata_FRFexamples.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_spanstations.png",
-                    "description": "RSW_spanstations.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_spanstations.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_spanstations.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_spanstations.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_grids.png",
-                    "description": "Table_RSW_grids.png",
                     "@type": "dcat:Distribution",
+                    "description": "Table_RSW_grids.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_grids.png",
+                    "mediaType": "image/x-png",
                     "title": "Table_RSW_grids.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_analysis_teams.png",
-                    "description": "Table_RSW_analysis_teams.png",
                     "@type": "dcat:Distribution",
+                    "description": "Table_RSW_analysis_teams.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_analysis_teams.png",
+                    "mediaType": "image/x-png",
                     "title": "Table_RSW_analysis_teams.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_analysis_teams_small.png",
-                    "description": "Table_RSW_analysis_teams_small.png",
                     "@type": "dcat:Distribution",
+                    "description": "Table_RSW_analysis_teams_small.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_analysis_teams_small.png",
+                    "mediaType": "image/x-png",
                     "title": "Table_RSW_analysis_teams_small.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_analysis_cases.png",
-                    "description": "Table_RSW_analysis_cases.png",
                     "@type": "dcat:Distribution",
+                    "description": "Table_RSW_analysis_cases.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_analysis_cases.png",
+                    "mediaType": "image/x-png",
                     "title": "Table_RSW_analysis_cases.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_Exp_SepFlow_Table.png",
-                    "description": "RSW_Exp_SepFlow_Table.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_Exp_SepFlow_Table.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_Exp_SepFlow_Table.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_Exp_SepFlow_Table.png"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_FlowSolvers.gif",
-                    "description": "Table_RSW_FlowSolvers.gif",
                     "@type": "dcat:Distribution",
+                    "description": "Table_RSW_FlowSolvers.gif",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Table_RSW_FlowSolvers.gif",
+                    "mediaType": "image/gif",
                     "title": "Table_RSW_FlowSolvers.gif"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_PressureTransducerLocations.png",
-                    "description": "RSW_PressureTransducerLocations.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_PressureTransducerLocations.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_PressureTransducerLocations.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_PressureTransducerLocations.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_Summary_Information_2.png",
-                    "description": "RSW Summary Information.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW Summary Information.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_Summary_Information_2.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW Summary Information.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_AnalysisParameters.png",
-                    "description": "RSW_AnalysisParameters.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_AnalysisParameters.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_AnalysisParameters.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_AnalysisParameters.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_ReferenceQuantities_2.png",
-                    "description": "RSW_ReferenceQuantities.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_ReferenceQuantities.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_ReferenceQuantities_2.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_ReferenceQuantities.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Photo_RSW_splitterplate1.jpg",
-                    "description": "Photo_RSW_splitterplate1.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Photo_RSW_splitterplate1.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Photo_RSW_splitterplate1.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Photo_RSW_splitterplate1.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Photo_RSW_splitterplate2.jpg",
-                    "description": "Photo_RSW_splitterplate2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Photo_RSW_splitterplate2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Photo_RSW_splitterplate2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Photo_RSW_splitterplate2.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_cartoon_JH.png",
-                    "description": "RSW_cartoon_JH.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_cartoon_JH.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_cartoon_JH.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_cartoon_JH.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_cartoon_JH.jpg",
-                    "description": "RSW_cartoon_JH.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_cartoon_JH.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_cartoon_JH.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_cartoon_JH.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_planform_cartoon.jpg",
-                    "description": "RSW_planform_cartoon.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_planform_cartoon.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_planform_cartoon.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_planform_cartoon.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_airfoil.png",
-                    "description": "RSW_airfoil.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_airfoil.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_airfoil.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_airfoil.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_grids.png",
-                    "description": "RSW_grids.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_grids.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_grids.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_grids.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_solution_methods.png",
-                    "description": "RSW_solution_methods.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_solution_methods.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_solution_methods.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_solution_methods.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_teams.png",
-                    "description": "RSW_analysis_teams.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_analysis_teams.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_teams.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_analysis_teams.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_image_2.png",
-                    "description": "RSW_analysis_image.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_analysis_image.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_analysis_image_2.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_analysis_image.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_GridResolution.jpg",
-                    "description": "RSW_steady_aoa2_U_S2_GridResolution.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_U_S2_GridResolution.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_GridResolution.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_steady_aoa2_U_S2_GridResolution.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/CM_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
-                    "description": "CM_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "CM_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/CM_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "CM_all_aoa_2_SteadyremoveOutliers_notitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/CD_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
-                    "description": "CD_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "CD_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/CD_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "CD_all_aoa_2_SteadyremoveOutliers_notitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/CL_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
-                    "description": "CL_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "CL_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/CL_all_aoa_2_SteadyremoveOutliers_notitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "CL_all_aoa_2_SteadyremoveOutliers_notitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station2.jpg",
-                    "description": "ShockLoc_withExp_station2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockLoc_withExp_station2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockLoc_withExp_station2.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station2_zoomC_Legend.jpg",
-                    "description": "ShockLoc_withExp_station2_zoomC_Legend.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockLoc_withExp_station2_zoomC_Legend.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station2_zoomC_Legend.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockLoc_withExp_station2_zoomC_Legend.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station4.jpg",
-                    "description": "ShockLoc_withExp_station4.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockLoc_withExp_station4.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station4.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockLoc_withExp_station4.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station3.jpg",
-                    "description": "ShockLoc_withExp_station3.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockLoc_withExp_station3.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station3.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockLoc_withExp_station3.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockStrength_withExp_station1.jpg",
-                    "description": "ShockStrength_withExp_station1.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockStrength_withExp_station1.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockStrength_withExp_station1.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockStrength_withExp_station1.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station1.jpg",
-                    "description": "ShockLoc_withExp_station1.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockLoc_withExp_station1.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station1.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockLoc_withExp_station1.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockStrength_withExp_station2.jpg",
-                    "description": "ShockStrength_withExp_station2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockStrength_withExp_station2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockStrength_withExp_station2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockStrength_withExp_station2.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Slope_lowersurface.png",
-                    "description": "Slope_lowersurface.png",
                     "@type": "dcat:Distribution",
+                    "description": "Slope_lowersurface.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Slope_lowersurface.png",
+                    "mediaType": "image/x-png",
                     "title": "Slope_lowersurface.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Slope_uppersurface.png",
-                    "description": "Slope_uppersurface.png",
                     "@type": "dcat:Distribution",
+                    "description": "Slope_uppersurface.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Slope_uppersurface.png",
+                    "mediaType": "image/x-png",
                     "title": "Slope_uppersurface.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockStrength_withExp_station4.jpg",
-                    "description": "ShockStrength_withExp_station4.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockStrength_withExp_station4.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockStrength_withExp_station4.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockStrength_withExp_station4.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AOA_variation_Exp_Upper_station2.png",
-                    "description": "AOA_variation_Exp_Upper_station2.png",
                     "@type": "dcat:Distribution",
+                    "description": "AOA_variation_Exp_Upper_station2.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AOA_variation_Exp_Upper_station2.png",
+                    "mediaType": "image/x-png",
                     "title": "AOA_variation_Exp_Upper_station2.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AOA_variation_Exp_Lower_station2.png",
-                    "description": "AOA_variation_Exp_Lower_station2.png",
                     "@type": "dcat:Distribution",
+                    "description": "AOA_variation_Exp_Lower_station2.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AOA_variation_Exp_Lower_station2.png",
+                    "mediaType": "image/x-png",
                     "title": "AOA_variation_Exp_Lower_station2.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Time_Convergence_CL_RSW_10Hz_noTitle.jpg",
-                    "description": "Time_Convergence_CL_RSW_10Hz_noTitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Time_Convergence_CL_RSW_10Hz_noTitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Time_Convergence_CL_RSW_10Hz_noTitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Time_Convergence_CL_RSW_10Hz_noTitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Grid_Convergence_CL_logNRSW_noTitle.jpg",
-                    "description": "Grid_Convergence_CL_logNRSW_noTitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Grid_Convergence_CL_logNRSW_noTitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Grid_Convergence_CL_logNRSW_noTitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Grid_Convergence_CL_logNRSW_noTitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Grid_Convergence_CL_RSW_noTitle.jpg",
-                    "description": "Grid_Convergence_CL_RSW_noTitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Grid_Convergence_CL_RSW_noTitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Grid_Convergence_CL_RSW_noTitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Grid_Convergence_CL_RSW_noTitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/GridPoints_RSW_noTitle.jpg",
-                    "description": "GridPoints_RSW_noTitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "GridPoints_RSW_noTitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/GridPoints_RSW_noTitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "GridPoints_RSW_noTitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_key_steady_aoa2.jpg",
-                    "description": "RSW_key_steady_aoa2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_key_steady_aoa2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_key_steady_aoa2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_key_steady_aoa2.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_Solver.jpg",
-                    "description": "RSW_steady_aoa2_U_S2_Solver.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_U_S2_Solver.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_Solver.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_steady_aoa2_U_S2_Solver.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_TurbulenceModel.jpg",
-                    "description": "RSW_steady_aoa2_U_S2_TurbulenceModel.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_U_S2_TurbulenceModel.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_TurbulenceModel.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_steady_aoa2_U_S2_TurbulenceModel.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_L_S1_analyst.png",
-                    "description": "RSW_steady_aoa2_L_S1_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_L_S1_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_L_S1_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_L_S1_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_L_S2_analyst.png",
-                    "description": "RSW_steady_aoa2_L_S2_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_L_S2_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_L_S2_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_L_S2_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_L_S3_analyst.png",
-                    "description": "RSW_steady_aoa2_L_S3_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_L_S3_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_L_S3_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_L_S3_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_L_S4_analyst.png",
-                    "description": "RSW_steady_aoa2_L_S4_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_L_S4_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_L_S4_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_L_S4_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S1_analyst.png",
-                    "description": "RSW_steady_aoa2_U_S1_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_U_S1_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S1_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_U_S1_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_analyst.png",
-                    "description": "RSW_steady_aoa2_U_S2_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_U_S2_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_U_S2_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S3_analyst.png",
-                    "description": "RSW_steady_aoa2_U_S3_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_U_S3_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S3_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_U_S3_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S4_analyst.png",
-                    "description": "RSW_steady_aoa2_U_S4_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_U_S4_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S4_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_U_S4_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_L_S1_analyst.png",
-                    "description": "RSW_steady_aoa4_L_S1_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_L_S1_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_L_S1_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_L_S1_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_L_S2_analyst.png",
-                    "description": "RSW_steady_aoa4_L_S2_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_L_S2_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_L_S2_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_L_S2_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_L_S3_analyst.png",
-                    "description": "RSW_steady_aoa4_L_S3_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_L_S3_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_L_S3_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_L_S3_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_L_S4_analyst.png",
-                    "description": "RSW_steady_aoa4_L_S4_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_L_S4_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_L_S4_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_L_S4_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S1_analyst.png",
-                    "description": "RSW_steady_aoa4_U_S1_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_U_S1_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S1_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_U_S1_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S2_analyst.png",
-                    "description": "RSW_steady_aoa4_U_S2_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_U_S2_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S2_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_U_S2_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S3_analyst.png",
-                    "description": "RSW_steady_aoa4_U_S3_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_U_S3_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S3_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_U_S3_analyst.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S4_analyst.png",
-                    "description": "RSW_steady_aoa4_U_S4_analyst.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_U_S4_analyst.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S4_analyst.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_U_S4_analyst.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_key_steady_aoa4.jpg",
-                    "description": "RSW_key_steady_aoa4.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_key_steady_aoa4.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_key_steady_aoa4.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_key_steady_aoa4.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_key_unsteady_f10.jpg",
-                    "description": "RSW_key_unsteady_f10.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_key_unsteady_f10.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_key_unsteady_f10.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_key_unsteady_f10.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_key_unsteady_f20.jpg",
-                    "description": "RSW_key_unsteady_f20.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_key_unsteady_f20.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_key_unsteady_f20.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_key_unsteady_f20.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_M_S1_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_L_M_S1_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_L_M_S1_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_M_S1_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_L_M_S1_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_M_S2_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_L_M_S2_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_L_M_S2_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_M_S2_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_L_M_S2_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_M_S3_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_L_M_S3_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_L_M_S3_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_M_S3_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_L_M_S3_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_M_S4_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_L_M_S4_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_L_M_S4_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_M_S4_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_L_M_S4_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_P_S1_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_L_P_S1_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_L_P_S1_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_P_S1_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_L_P_S1_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_P_S2_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_L_P_S2_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_L_P_S2_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_P_S2_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_L_P_S2_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_P_S3_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_L_P_S3_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_L_P_S3_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_P_S3_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_L_P_S3_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_P_S4_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_L_P_S4_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_L_P_S4_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_L_P_S4_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_L_P_S4_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S1_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_U_M_S1_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_M_S1_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S1_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_U_M_S1_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S2_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_U_M_S2_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_M_S2_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S2_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_U_M_S2_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S3_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_U_M_S3_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_M_S3_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S3_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_U_M_S3_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S4_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_U_M_S4_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_M_S4_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S4_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_U_M_S4_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_P_S1_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_U_P_S1_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_P_S1_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_P_S1_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_U_P_S1_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_P_S2_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_U_P_S2_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_P_S2_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_P_S2_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_U_P_S2_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_P_S3_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_U_P_S3_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_P_S3_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_P_S3_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_U_P_S3_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_P_S4_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f10_U_P_S4_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_P_S4_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_P_S4_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f10_U_P_S4_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_M_S1_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_L_M_S1_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_L_M_S1_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_M_S1_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_L_M_S1_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_M_S2_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_L_M_S2_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_L_M_S2_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_M_S2_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_L_M_S2_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_M_S3_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_L_M_S3_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_L_M_S3_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_M_S3_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_L_M_S3_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_M_S4_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_L_M_S4_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_L_M_S4_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_M_S4_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_L_M_S4_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_P_S1_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_L_P_S1_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_L_P_S1_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_P_S1_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_L_P_S1_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_P_S2_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_L_P_S2_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_L_P_S2_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_P_S2_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_L_P_S2_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_P_S3_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_L_P_S3_analyst.jpg",
                     "@type": "dcat:Distribution",
-                    "title": "RSW_unsteady_aoa2_f20_L_P_S3_analyst.jpg"
-                },
-                {
+                    "description": "RSW_unsteady_aoa2_f20_L_P_S3_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_P_S3_analyst.jpg",
                     "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_P_S4_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_L_P_S4_analyst.jpg",
+                    "title": "RSW_unsteady_aoa2_f20_L_P_S3_analyst.jpg"
+                },
+                {
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_L_P_S4_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_L_P_S4_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_L_P_S4_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S1_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_U_M_S1_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_M_S1_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S1_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_U_M_S1_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S2_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_U_M_S2_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_M_S2_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S2_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_U_M_S2_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S3_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_U_M_S3_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_M_S3_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S3_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_U_M_S3_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S4_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_U_M_S4_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_M_S4_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S4_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_U_M_S4_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_P_S1_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_U_P_S1_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_P_S1_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_P_S1_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_U_P_S1_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_P_S2_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_U_P_S2_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_P_S2_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_P_S2_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_U_P_S2_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_P_S3_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_U_P_S3_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_P_S3_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_P_S3_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_U_P_S3_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_P_S4_analyst.jpg",
-                    "description": "RSW_unsteady_aoa2_f20_U_P_S4_analyst.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_P_S4_analyst.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_P_S4_analyst.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_unsteady_aoa2_f20_U_P_S4_analyst.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Convergence_CL_RSW_noTitle.jpg",
-                    "description": "Convergence_CL_RSW_noTitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Convergence_CL_RSW_noTitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Convergence_CL_RSW_noTitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Convergence_CL_RSW_noTitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_instrumentation.jpeg",
-                    "description": "RSW_instrumentation.jpeg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_instrumentation.jpeg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_instrumentation.jpeg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_instrumentation.jpeg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_instrumentation.jpg",
-                    "description": "RSW_instrumentation.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_instrumentation.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_instrumentation.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_instrumentation.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_schematic.jpg",
-                    "description": "RSW_schematic.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_schematic.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_schematic.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "RSW_schematic.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_GridResolution.png",
-                    "description": "RSW_steady_aoa2_U_S2_GridResolution.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa2_U_S2_GridResolution.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa2_U_S2_GridResolution.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa2_U_S2_GridResolution.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S2_Solver.png",
-                    "description": "RSW_steady_aoa4_U_S2_Solver.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_steady_aoa4_U_S2_Solver.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_steady_aoa4_U_S2_Solver.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_steady_aoa4_U_S2_Solver.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S2_Solver.png",
-                    "description": "RSW_unsteady_aoa2_f10_U_M_S2_Solver.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f10_U_M_S2_Solver.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f10_U_M_S2_Solver.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_unsteady_aoa2_f10_U_M_S2_Solver.png"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S2_Solver.png",
-                    "description": "RSW_unsteady_aoa2_f20_U_M_S2_Solver.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_unsteady_aoa2_f20_U_M_S2_Solver.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_unsteady_aoa2_f20_U_M_S2_Solver.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_unsteady_aoa2_f20_U_M_S2_Solver.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Steady_Xitionstrip_station2.jpg",
-                    "description": "Steady_Xitionstrip_station2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Steady_Xitionstrip_station2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Steady_Xitionstrip_station2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Steady_Xitionstrip_station2.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/TimeHistories_fwdstation.png",
-                    "description": "TimeHistories_fwdstation.png",
                     "@type": "dcat:Distribution",
+                    "description": "TimeHistories_fwdstation.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/TimeHistories_fwdstation.png",
+                    "mediaType": "image/x-png",
                     "title": "TimeHistories_fwdstation.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Timehistories_shocklocation.jpg",
-                    "description": "Timehistories_shocklocation.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Timehistories_shocklocation.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Timehistories_shocklocation.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Timehistories_shocklocation.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_onsplitterplate_cartoon_2.png",
-                    "description": "RSW_onsplitterplate_cartoon.png",
                     "@type": "dcat:Distribution",
+                    "description": "RSW_onsplitterplate_cartoon.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_onsplitterplate_cartoon_2.png",
+                    "mediaType": "image/x-png",
                     "title": "RSW_onsplitterplate_cartoon.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Time_Convergence_CL_RSW_20Hz_noTitle.jpg",
-                    "description": "Time_Convergence_CL_RSW_20Hz_noTitle.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Time_Convergence_CL_RSW_20Hz_noTitle.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Time_Convergence_CL_RSW_20Hz_noTitle.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "Time_Convergence_CL_RSW_20Hz_noTitle.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockStrength_withExp_station3.jpg",
-                    "description": "ShockStrength_withExp_station3.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockStrength_withExp_station3.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockStrength_withExp_station3.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockStrength_withExp_station3.jpg"
                 },
                 {
-                    "mediaType": "image/x-png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station2_zoomC_Legend.png",
-                    "description": "ShockLoc_withExp_station2_zoomC_Legend.png",
                     "@type": "dcat:Distribution",
+                    "description": "ShockLoc_withExp_station2_zoomC_Legend.png",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station2_zoomC_Legend.png",
+                    "mediaType": "image/x-png",
                     "title": "ShockLoc_withExp_station2_zoomC_Legend.png"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station2_zoomC_Legend_v2.jpg",
-                    "description": "ShockLoc_withExp_station2_zoomC_Legend_v2.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "ShockLoc_withExp_station2_zoomC_Legend_v2.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/ShockLoc_withExp_station2_zoomC_Legend_v2.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "ShockLoc_withExp_station2_zoomC_Legend_v2.jpg"
                 },
                 {
-                    "mediaType": "image/pjpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/image1.jpg",
-                    "description": "image1.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "image1.jpg",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/image1.jpg",
+                    "mediaType": "image/pjpeg",
                     "title": "image1.jpg"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_837",
+            "issued": "2013-09-23",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/837/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "images_RSW"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "MAM04S0",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350972-GES_DISC.html",
             "citation": "MODIS Science Team. 2006-10-01. MAM04S0. Version 002. MODIS/Aqua Aerosol 5-Min L2 Swath Subset 10km along MLS. Greenbelt, MD, USA. MAM04S0. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/MAM04S0_002.html. Digital Science Data.",
-            "issued": "2004-08-08",
-            "temporal": "2004-08-08T00:00:00Z/2008-01-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-01-11",
-            "keyword": [
-                "ngda",
-                "aerosols",
-                "atmosphere",
-                "national geospatial data asset",
-                "earth science",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "MODIS Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1236350972-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This is the MODIS/Aqua subset along MLS field of view track. The goal of the subset is to select and return MODIS data that are within +-100 km across the MLS track. I.e. the resultant MODIS subset swath is sought to be about 200 km cross-track. However, the original MYD04_L2 has 10-km pixels. Thus, MAM04S0 cross-track width is 21 pixels, and the resultant cross-track swath width is about 200 km. Along-track, all MODIS pixels from the original product are preserved.\n      \nIn the stardard product, the MODIS level-2 atmospheric aerosol product provides retrieved ambient aerosol optical properties (e.g., optical thickness and size distribution), mass concentration, look-up table derived reflected and transmitted fluxes, as well as quality assurance and other ancillary parameters, globally over ocean and near globally over land.\n      \n      \n(The shortname for this product is MAM04S0).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MAM04S0",
-            "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Aerosol 5-Min L2 Swath Subset 10km along MLS V002 (MAM04S0) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAM04S0_002.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1478424,146 +1478398,195 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAM04S0_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MAM04S0_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAM/MAM04S0.002/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://atrain.gesdisc.eosdis.nasa.gov/data/MAM/MAM04S0.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.nascom.nasa.gov",
-                    "description": "View standard full-sized MODIS data availability.",
                     "@type": "dcat:Distribution",
+                    "description": "View standard full-sized MODIS data availability.",
+                    "downloadURL": "https://ladsweb.nascom.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis.gsfc.nasa.gov/",
-                    "description": "MODIS Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Science Team",
+                    "downloadURL": "https://modis.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mcst.gsfc.nasa.gov/",
-                    "description": "MODIS Characterization Support Team (MCST)",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Characterization Support Team (MCST)",
+                    "downloadURL": "https://mcst.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.cloudsat.cira.colostate.edu/",
-                    "description": "CloudSat Data Processing Center",
                     "@type": "dcat:Distribution",
+                    "description": "CloudSat Data Processing Center",
+                    "downloadURL": "http://www.cloudsat.cira.colostate.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/data-issues/aerosol",
-                    "description": "Quality Assurance for the original product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance for the original product.",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/data-issues/aerosol",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MAM04S0_002.png",
+            "identifier": "C1236350972-GES_DISC",
+            "issue-identification": "MAM04S0",
+            "issued": "2004-08-08",
+            "keyword": [
+                "ngda",
+                "aerosols",
+                "atmosphere",
+                "national geospatial data asset",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1236350972-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-01-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "MAM04S0",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-08-08T00:00:00Z/2008-01-11T23:59:59.999Z",
             "theme": [
                 "ATDD",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Aerosol 5-Min L2 Swath Subset 10km along MLS V002 (MAM04S0) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5TD9V75",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Snowfall and Snow Depth for Canada 1943-1982, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5TD9V75.",
-            "issued": "1943-01-01",
-            "temporal": "1943-01-01T00:00:00Z/1982-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1982-12-31",
-            "keyword": [
-                "snow/ice",
-                "terrestrial hydrosphere",
-                "precipitation",
-                "earth science",
-                "cryosphere",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Walsh",
                 "hasEmail": "mailto:walsh@wx.atmos.uiuc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206481-NSIDCV0",
             "description": "Data include monthly snowfall and end-of-month snow depth for 140 stations across Canada. Stations that maintained at least 20 years of data were chosen. The original data are from Atmospheric Environment Service Canadian Climate Centre and from NOAA's National Climatic Data Center. Data are divided into eight files by region or province: British Columbia (17 stations), Yukon and Northwest Territories (33 stations), Alberta (12 stations), Saskatchewan (115 stations), Manitoba (10 stations), Ontario (19 stations), Quebec (20 stations) and Atlantic Provinces (14 stations). Each data record contains a variable indicator to identify data as snow on the ground on the last day of the month (centimeters) or total snowfall for the month (millimeters). A list of stations, with latitude and longitude to hundredths of a degree, is included in documentation for this data set.",
-            "title": "Snowfall and Snow Depth for Canada 1943-1982, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5TD9V75",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5TD9V75",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G00922_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G00922_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5TD9V75",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5TD9V75",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5TD9V75",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5TD9V75",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206481-NSIDCV0",
+            "issued": "1943-01-01",
+            "keyword": [
+                "snow/ice",
+                "terrestrial hydrosphere",
+                "precipitation",
+                "earth science",
+                "cryosphere",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5TD9V75",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1982-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-142.0 45.0 -55.0 75.0",
+            "temporal": "1943-01-01T00:00:00Z/1982-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Snowfall and Snow Depth for Canada 1943-1982, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10926",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John Vallerga",
+                "hasEmail": "mailto:jvv@ssl.berkeley.edu"
+            },
+            "description": "N/A",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://techport.nasa.gov/xml-api/10926",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "TECHPORT_10926",
             "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
+            "keyword": [
+                "project",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10926",
             "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Science Mission Directorate"
+            },
             "references": [
                 "http://techport.nasa.gov/home",
                 "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
@@ -1478574,44 +1478597,40 @@
                 "http://techport.nasa.gov/fetchFile?objectId=6560",
                 "http://techport.nasa.gov/fetchFile?objectId=3448"
             ],
-            "keyword": [
-                "project",
-                "active"
+            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
+            "title": "High performance cross-strip micro-channel plate detector systems for spaceflight experiments Project"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "John Vallerga",
-                "hasEmail": "mailto:jvv@ssl.berkeley.edu"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
+                "fn": "GREG STENSAAS",
+                "hasEmail": "mailto:stensaas@usgs.gov"
             },
-            "identifier": "TECHPORT_10926",
-            "description": "N/A",
-            "title": "High performance cross-strip micro-channel plate detector systems for spaceflight experiments Project",
-            "programCode": [
-                "026:000"
-            ],
+            "description": "On the background of these requirements for sensor calibration, intercalibration and product validation, the subgroup on Calibration and Validation of the Committee on Earth Observing System (CEOS) formulated the following recommendation during the plenary session held in China at the end of 2004, with the goal of setting-up and operating an internet based system to provide sensor data, protocols and guidelines for these purposes:\n\nBackground:\n\nReference Datasets are required to support the understanding of climate change and quality assure operational services by Earth Observing satellites. The data from different sensors and the resulting synergistic data products require a high level of accuracy that can only be obtained through continuous traceable calibration and validation activities.\nRequirement:\n\nInitiate an activity to document a reference methodology to predict Top of Atmosphere (TOA) radiance for which currently flying and planned wide swath sensors can be intercompared, i.e. define a standard for traceability. Also create and maintain a fully accessible web page containing, on an instrument basis, links to all instrument characteristics needed for intercomparisons as specified above, ideally in a common format. In addition, create and maintain a database (e.g. SADE) of instrument data for specific vicarious calibration sites, including site characteristics, in a common format. Each agency is responsible for providing data for their instruments in this common format. Recommendation : The required activities described above should be supported for an implementation period of two years and a maintenance period over two subsequent years. The CEOS should encourage a member agency to accept the lead role in supporting this activity. CEOS should request all member agencies to support this activity by providing appropriate information and data in a timely manner.\n\nInstrumented Sites:\nLa Crau, France is one of eight instrumented sites that are CEOS Reference Test Sites. The CEOS instrumented sites are provisionally being called LANDNET. These instrumented sites are primarily used for field campaigns to obtain radiometric gain, and these sites can serve as a focus for international efforts, facilitating traceability and inter-comparison to evaluate biases of in-flight and future instruments in a harmonized manner.\u00a0 In the longer-term it is anticipated that these sites will all be fully automated and provide surface and atmospheric measurements to the WWW in an autonomous manner reducing some of the cost of a manned campaign, at present three can operate in this manner.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "http://techport.nasa.gov/xml-api/10926",
-                    "mediaType": "application/xml"
-                }
-            ]
+                    "description": "Committee on Earth Observation Satellites (CEOS) Working Group on Calibration and Validation (WGCV) Test Sites.",
+                    "downloadURL": "http://calvalportal.ceos.org/web/guest/home",
+                    "mediaType": "text/html",
+                    "title": "The dataset's project home page"
                 },
                 {
-            "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566843-USGS_LTA.html",
-            "bureauCode": [
-                "026:00"
+                    "@type": "dcat:Distribution",
+                    "description": "Collection-specific granule Open Search Descriptor Document",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/opensearch/granules/descriptor_document.xml?collectionConceptId=C1220566843-USGS_LTA",
+                    "mediaType": "application/opensearchdescription+xml",
+                    "title": "Retrieve the OpenSearch Get Capabilities document"
+                }
             ],
-            "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
+            "identifier": "C1220566843-USGS_LTA",
             "issued": "1972-08-16",
-            "temporal": "1972-08-16T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-27",
             "keyword": [
                 "sensor characteristics",
                 "surface thermal properties",
@@ -1478623,569 +1478642,564 @@
                 "national geospatial data asset",
                 "land use/land cover"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GREG STENSAAS",
-                "hasEmail": "mailto:stensaas@usgs.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220566843-USGS_LTA",
-            "description": "On the background of these requirements for sensor calibration, intercalibration and product validation, the subgroup on Calibration and Validation of the Committee on Earth Observing System (CEOS) formulated the following recommendation during the plenary session held in China at the end of 2004, with the goal of setting-up and operating an internet based system to provide sensor data, protocols and guidelines for these purposes:\n\nBackground:\n\nReference Datasets are required to support the understanding of climate change and quality assure operational services by Earth Observing satellites. The data from different sensors and the resulting synergistic data products require a high level of accuracy that can only be obtained through continuous traceable calibration and validation activities.\nRequirement:\n\nInitiate an activity to document a reference methodology to predict Top of Atmosphere (TOA) radiance for which currently flying and planned wide swath sensors can be intercompared, i.e. define a standard for traceability. Also create and maintain a fully accessible web page containing, on an instrument basis, links to all instrument characteristics needed for intercomparisons as specified above, ideally in a common format. In addition, create and maintain a database (e.g. SADE) of instrument data for specific vicarious calibration sites, including site characteristics, in a common format. Each agency is responsible for providing data for their instruments in this common format. Recommendation : The required activities described above should be supported for an implementation period of two years and a maintenance period over two subsequent years. The CEOS should encourage a member agency to accept the lead role in supporting this activity. CEOS should request all member agencies to support this activity by providing appropriate information and data in a timely manner.\n\nInstrumented Sites:\nLa Crau, France is one of eight instrumented sites that are CEOS Reference Test Sites. The CEOS instrumented sites are provisionally being called LANDNET. These instrumented sites are primarily used for field campaigns to obtain radiometric gain, and these sites can serve as a focus for international efforts, facilitating traceability and inter-comparison to evaluate biases of in-flight and future instruments in a harmonized manner.\u00a0 In the longer-term it is anticipated that these sites will all be fully automated and provide surface and atmospheric measurements to the WWW in an autonomous manner reducing some of the cost of a manned campaign, at present three can operate in this manner.",
-            "title": "CEOS Cal Val Test Site - La Crau, France - Instrumented Site",
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566843-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-27",
             "programCode": [
                 "026:001"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://calvalportal.ceos.org/web/guest/home",
-                    "description": "Committee on Earth Observation Satellites (CEOS) Working Group on Calibration and Validation (WGCV) Test Sites.",
-                    "@type": "dcat:Distribution",
-                    "title": "The dataset's project home page"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOI/USGS/EROS"
             },
-                {
-                    "mediaType": "application/opensearchdescription+xml",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/opensearch/granules/descriptor_document.xml?collectionConceptId=C1220566843-USGS_LTA",
-                    "description": "Collection-specific granule Open Search Descriptor Document",
-                    "@type": "dcat:Distribution",
-                    "title": "Retrieve the OpenSearch Get Capabilities document"
-                }
-            ],
             "spatial": "1.92 41.86 6.49 45.63",
+            "temporal": "1972-08-16T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CEOS Cal Val Test Site - La Crau, France - Instrumented Site"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD04_3K.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Terra Aerosol 5-Min L2 Swath 3km. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MOD04_3K.061. https://doi.org/10.5067/MODIS/MOD04_3K.061.",
-            "issued": "2017-01-01",
-            "temporal": "2000-02-24T00:05:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "atmospheric radiation",
-                "aerosols",
-                "national geospatial data asset",
-                "atmosphere",
-                "ngda",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASAD ULLAH",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1443420430-LAADS",
-            "description": "The new Collection 6.1 (C61) MODIS/Terra Aerosol 5 Min L2 Swath 3km (MOD04_3K) product is an improved version based on algorithm changes in Dark Target (DT) Aerosol retrieval over urban areas and uncertainty estimates for Deep Blue (DB) Aerosol retrievals.\r\n\r\nThe MODIS level-2 atmospheric aerosol product provides retrieved ambient aerosol optical properties, quality assurance, and other parameters, globally over ocean and land. In Collection 5, and earlier collections, there was only one aerosol product (MOD04_L2) at 10km (at nadir) spatial resolution. Starting from C6, the Dark Target (DT) Aerosol algorithm team provided a new 3 km spatial resolution product (MOD04_3k) intended for the air quality community.\r\n\r\nThe MOD04_3K product is based on the same algorithm and Look up Tables as the standard Dark Target aerosol product. Because of finer resolution, subtle differences are made in selecting pixels for retrieval and in determining QA. The only differences between the existing 10km algorithm and the new 3km algorithm are: 1) the size of the pixel-arrays defining each retrieval box ( 6x6 retrieval boxes of 36 pixels at 0.5km resolution for 3km algorithm as oppose to 20x20 retrieval boxes of 400 pixels at 0.5km resolution for 10km product); 2) the minimum percentage of \"good\" pixels required for a retrieval (a minimum of 5 pixels over ocean and 6 pixels over land instead of a minimum of 10 pixels over ocean or 12 pixels over land for 10km product retrieval); 3) the 10km algorithm attemptes a \"poor quality\" retrieval while 3km algorithm does not. Everything else is the same between two products.\r\n\r\nFor more information on C6.1 changes and updates, visit the MODIS Atmosphere website at:\r\nhttps://modis-atmosphere.gsfc.nasa.gov/documentation/collection-61",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Terra Aerosol 5-Min L2 Swath 3km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The new Collection 6.1 (C61) MODIS/Terra Aerosol 5 Min L2 Swath 3km (MOD04_3K) product is an improved version based on algorithm changes in Dark Target (DT) Aerosol retrieval over urban areas and uncertainty estimates for Deep Blue (DB) Aerosol retrievals.\r\n\r\nThe MODIS level-2 atmospheric aerosol product provides retrieved ambient aerosol optical properties, quality assurance, and other parameters, globally over ocean and land. In Collection 5, and earlier collections, there was only one aerosol product (MOD04_L2) at 10km (at nadir) spatial resolution. Starting from C6, the Dark Target (DT) Aerosol algorithm team provided a new 3 km spatial resolution product (MOD04_3k) intended for the air quality community.\r\n\r\nThe MOD04_3K product is based on the same algorithm and Look up Tables as the standard Dark Target aerosol product. Because of finer resolution, subtle differences are made in selecting pixels for retrieval and in determining QA. The only differences between the existing 10km algorithm and the new 3km algorithm are: 1) the size of the pixel-arrays defining each retrieval box ( 6x6 retrieval boxes of 36 pixels at 0.5km resolution for 3km algorithm as oppose to 20x20 retrieval boxes of 400 pixels at 0.5km resolution for 10km product); 2) the minimum percentage of \"good\" pixels required for a retrieval (a minimum of 5 pixels over ocean and 6 pixels over land instead of a minimum of 10 pixels over ocean or 12 pixels over land for 10km product retrieval); 3) the 10km algorithm attemptes a \"poor quality\" retrieval while 3km algorithm does not. Everything else is the same between two products.\r\n\r\nFor more information on C6.1 changes and updates, visit the MODIS Atmosphere website at:\r\nhttps://modis-atmosphere.gsfc.nasa.gov/documentation/collection-61",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD04_3K.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD04_3K.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD04_3K.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD04_3K.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/modis_deep_blue_c61_changes2.pdf",
-                    "description": "The MODIS deep blue aerosol version 6 to 6.1 change document",
                     "@type": "dcat:Distribution",
+                    "description": "The MODIS deep blue aerosol version 6 to 6.1 change document",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/modis_deep_blue_c61_changes2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/C061_Aerosol_Dark_Target_v2.pdf",
-                    "description": "The dark target 6.1 update document.",
                     "@type": "dcat:Distribution",
+                    "description": "The dark target 6.1 update document.",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/C061_Aerosol_Dark_Target_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/ATBD_MOD04_C005_rev2_0.pdf",
-                    "description": "Aerosol product ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "Aerosol product ATBD",
+                    "downloadURL": "https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/ATBD_MOD04_C005_rev2_0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MOD04_3K--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MOD04_3K--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD04_3K/",
-                    "description": "Direct access to MOD04_3K C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MOD04_3K C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD04_3K/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MOD04_3K/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MOD04_3K/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1443420430-LAADS",
+            "issued": "2017-01-01",
+            "keyword": [
+                "atmospheric radiation",
+                "aerosols",
+                "national geospatial data asset",
+                "atmosphere",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD04_3K.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:05:00Z/2025-01-20T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Aerosol 5-Min L2 Swath 3km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRII-2-9P-CRUISE-V1.0",
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
-                "deep impact",
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains raw spectra for science calibrations acquired by the Deep Impact High Resolution Instrument Infrared Spectrometer during the cruise phase of the mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hrii-2-9p-cruise-v1.0_unzz-kitu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "deep impact",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRII-2-9P-CRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hrii-2-9p-cruise-v1.0_unzz-kitu",
-            "description": "This data set contains raw spectra for science calibrations acquired by the Deep Impact High Resolution Instrument Infrared Spectrometer during the cruise phase of the mission.",
-            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW HRII CALIB DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW HRII CALIB DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/754",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ito, A., and J.E. Penner. 2004. SAFARI 2000 1-Degree Estimates of Burned Biomass, Area, and Emissions, 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/754",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-01T00:00:00Z/2000-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "aerosols",
-                "national geospatial data asset",
-                "ngda",
-                "biosphere",
-                "earth science",
-                "soils",
-                "ecological dynamics",
-                "atmosphere",
-                "ecosystems",
-                "environmental impacts",
-                "human dimensions",
-                "land surface",
-                "vegetation",
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
-            "identifier": "C2789029387-ORNL_CLOUD",
             "description": "A new method is used to generate spatial estimates of monthly averaged biomass burned area and spatial and temporal estimates of trace gas and aerosol emissions from open fires in southern Africa. Global burned area data for the year 2000 (GBA2000) supplemented with the Along Track Scanning Radiometer (ATSR) fire count data are employed to quantify the area burned at 1-km resolution by using a fractional vegetation cover map derived from satellite observations.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 1-Degree Estimates of Burned Biomass, Area, and Emissions, 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F754",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F754",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/regional/one_deg_biomass/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/regional/one_deg_biomass/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/one_degree_biomass.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/one_degree_biomass.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/754",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/754",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/regional/one_deg_biomass/comp/one_degree_biomass_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/regional/one_deg_biomass/comp/one_degree_biomass_readme.pdf",
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
+            "identifier": "C2789029387-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "aerosols",
+                "national geospatial data asset",
+                "ngda",
+                "biosphere",
+                "earth science",
+                "soils",
+                "ecological dynamics",
+                "atmosphere",
+                "ecosystems",
+                "environmental impacts",
+                "human dimensions",
+                "land surface",
+                "vegetation",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/754",
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
             "spatial": "-18.0 -36.0 56.0 0.0",
+            "temporal": "2000-08-01T00:00:00Z/2000-09-30T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 1-Degree Estimates of Burned Biomass, Area, and Emissions, 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-THREEMICRON-V1.0",
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
+            "description": "This dataset includes the infrared spectrophotometry asteroid data reported in the following papers: [LEBOFSKY1980]; [FEIERBERGETAL1985]; [LEBOFSKYETAL1990]; and [JONESETAL1990]",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-threemicron-v1.0_up36-8npe",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-THREEMICRON-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-threemicron-v1.0_up36-8npe",
-            "description": "This dataset includes the infrared spectrophotometry asteroid data reported in the following papers: [LEBOFSKY1980]; [FEIERBERGETAL1985]; [LEBOFSKYETAL1990]; and [JONESETAL1990]",
-            "title": "ASTEROID 3-MICRON SURVEY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID 3-MICRON SURVEY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/424",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Aber, J.D., and M.E. Martin. 1999. Visible and Near-Infrared Leaf Reflectance Spectra, 1992-1993 (ACCP). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/424",
-            "issued": "2023-10-02",
-            "temporal": "1992-06-18T00:00:00Z/1993-05-27T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
-            "keyword": [
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
-            "identifier": "C2776851335-ORNL_CLOUD",
             "description": "Visible/NIR reflectance spectra data for both fresh and dry leaf samples were collected to determine the relationship of foliar chemical concentrations with reflectance.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Visible and Near-Infrared Leaf Reflectance Spectra, 1992-1993 (ACCP)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/accp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F424",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F424",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/accp/leafspec/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/accp/leafspec/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ACCP/guides/leafspec.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ACCP/guides/leafspec.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/424",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/424",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/accp/leafspec/comp/leafspec.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/accp/leafspec/comp/leafspec.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/accp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/accp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/accp_logo_square.png",
+            "identifier": "C2776851335-ORNL_CLOUD",
+            "issued": "2023-10-02",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/424",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-122.05 37.4 -68.74 45.22",
+            "temporal": "1992-06-18T00:00:00Z/1993-05-27T23:59:59Z",
             "theme": [
                 "ACCP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Visible and Near-Infrared Leaf Reflectance Spectra, 1992-1993 (ACCP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/WZVJ68EXNLK7",
             "citation": "Nadia Smith. 2019-01-15. SNDRAQIL2CPS. Version 2.1. Sounder SIPS: AQUA AIRS IR-only Level 2 CLIMCAPS: retrieved atmospheric state V2.1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/WZVJ68EXNLK7. https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL2CPS_2.1.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-01",
-            "references": [
-                "https://doi.org/10.1029/2022EA002701",
-                "https://doi.org/10.1029/2023EA002913",
-                "https://doi.org/10.1029/2022EA002725",
-                "https://doi.org/10.3390/rs15030547",
-                "https://doi.org/10.1029/2022GL101830",
-                "https://doi.org/DOI  10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "clouds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric radiation",
-                "land surface",
-                "oceans",
-                "atmospheric chemistry",
-                "earth science",
-                "surface thermal properties",
-                "air quality",
-                "altitude",
-                "precipitation",
-                "ocean temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Nadia Smith",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2790952275-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the AIRS (Atmospheric Infrared Sounder). The AIRS instrument is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. The AIRS CLIMCAPS Retrieval Product consists of retrieved estimates of cloud and surface properties, plus profiles of retrieved temperature, water vapor, ozone, carbon monoxide and methane. The temperature profile vertical resolution is 100 levels total between 1100 mb and 0.1 mb, while moisture profile is reported at atmospheric layers between 1100 mb and 300 mb. The horizontal resolution is 50 km.\n\nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere\nprofiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n\nAn AIRS level 2 granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRAQIL2CPS",
-            "creator": "Nadia Smith",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
-            "title": "Sounder SIPS: AQUA AIRS IR-only Level 2 CLIMCAPS: retrieved atmospheric state V2.1 (SNDRAQIL2CPS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL2CPS_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWZVJ68EXNLK7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWZVJ68EXNLK7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL2CPS_2.1.png",
-                    "description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL2CPS_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL2CPS_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIL2CPS_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level2/SNDRAQIL2CPS.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level2/SNDRAQIL2CPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level2/SNDRAQIL2CPS.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level2/SNDRAQIL2CPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIL2CPS+2.1",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIL2CPS+2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.1.README.pdf",
-                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.1.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
-                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS CPS",
                     "@type": "dcat:Distribution",
+                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS CPS",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V1.ATBD.pdf",
-                    "description": "CLIMCAPS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V1.ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.Test.Report.pdf",
-                    "description": "Product quality assessment guide",
                     "@type": "dcat:Distribution",
+                    "description": "Product quality assessment guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.Test.Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/data/guides-docs/climcaps-science/",
-                    "description": "CLIMCAPS Science Application Guide (Digital version)",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS Science Application Guide (Digital version)",
+                    "downloadURL": "https://airs.jpl.nasa.gov/data/guides-docs/climcaps-science/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS_V2_L2_science_guides.pdf",
-                    "description": "CLIMCAPS Science Application Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS Science Application Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS_V2_L2_science_guides.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIL2CPS_2.1.png",
+            "identifier": "C2790952275-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "clouds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere",
+                "atmospheric radiation",
+                "land surface",
+                "oceans",
+                "atmospheric chemistry",
+                "earth science",
+                "surface thermal properties",
+                "air quality",
+                "altitude",
+                "precipitation",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/WZVJ68EXNLK7",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/10.1029/2022EA002701",
+                "https://doi.org/10.1029/2023EA002913",
+                "https://doi.org/10.1029/2022EA002725",
+                "https://doi.org/10.3390/rs15030547",
+                "https://doi.org/10.1029/2022GL101830",
+                "https://doi.org/DOI  10.3390/rs11101227",
+                "https://doi.org/10.1109/TGRS.2012.2220369",
+                "https://doi.org/10.1016/S0022-4073(97)00169-6",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRAQIL2CPS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: AQUA AIRS IR-only Level 2 CLIMCAPS: retrieved atmospheric state V2.1 (SNDRAQIL2CPS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/up6a-38gf",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Analysis of effect of hindlimb suspension and reloading on C57Bl/6 mouse soleus muscle. Experimental groups examined: -Control mice 14 days -Hindlimb suspension for 7 days -Hindlimb suspension for 7 days and subsequent reloading for 1 day -Hindlimb suspension for 7 days and subsequent reloading for 7 days",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-228",
+                    "mediaType": "text/html",
+                    "title": "Hindlimb suspension and reloading study"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-228_up6a-38gf",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "normalization data transformation",
                 "hindlimb unloading",
@@ -1479195,232 +1479209,194 @@
                 "labeling",
                 "data collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/up6a-38gf",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-228_up6a-38gf",
-            "description": "Analysis of effect of hindlimb suspension and reloading on C57Bl/6 mouse soleus muscle. Experimental groups examined: -Control mice 14 days -Hindlimb suspension for 7 days -Hindlimb suspension for 7 days and subsequent reloading for 1 day -Hindlimb suspension for 7 days and subsequent reloading for 7 days",
-            "title": "Hindlimb suspension and reloading study",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-228",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Hindlimb suspension and reloading study"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Hindlimb suspension and reloading study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ROX6G419O13W",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Grayscale Swath Data L1, TIFF V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ROX6G419O13W.",
-            "issued": "1970-05-09",
-            "temporal": "1970-04-18T00:00:00Z/1975-11-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1975-03-17",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere"
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
-            "identifier": "C1703458270-NSIDC_ECS",
             "description": "This data set consists of daily, global grayscale TIFF images derived from radiative temperatures measured in the 6.7 \u00b5m window (6.5 \u00b5m - 7.0 \u00b5m). These data were detected by the Temperature-Humidity Infrared Radiometer (THIR) on board the Nimbus 4, Nimbus 5, and Nimbus 6 satellites, respectively, during 1970-1971, 1973-1975, and 1975. The Nimbus satellites used the THIR 6.7 \u00b5m window to map the water vapor distribution in the upper troposphere and stratosphere. Note: This data set is not georeferenced and there are some gaps in temporal coverage because of missing data.",
-            "title": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Grayscale Swath Data L1, TIFF V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FROX6G419O13W",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FROX6G419O13W",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR67-1T.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIR67-1T.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703458270-NSIDC_ECS&q=NmTHIR67-1T&m=-59.43570100523044%21-4.1220703125%211%211%210%210%2C2&tl=1568750791%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703458270-NSIDC_ECS&q=NmTHIR67-1T&m=-59.43570100523044%21-4.1220703125%211%211%210%210%2C2&tl=1568750791%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR67-1T/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIR67-1T/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ROX6G419O13W",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ROX6G419O13W",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ROX6G419O13W",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ROX6G419O13W",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1703458270-NSIDC_ECS",
+            "issued": "1970-05-09",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ROX6G419O13W",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1975-03-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1970-04-18T00:00:00Z/1975-11-11T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus Temperature-Humidity Infrared Radiometer 6.7 \u00b5m Grayscale Swath Data L1, TIFF V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0408-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-04T20:57:05.000 to 2014-11-04T23:24:48.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0408-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0408-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0408-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-04T20:57:05.000 to 2014-11-04T23:24:48.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0408 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0408 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-3-RADCAL-RDR-V1.0",
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
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-3-radcal-rdr-v1.0_upa2-hmfz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-3-RADCAL-RDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-3-radcal-rdr-v1.0_upa2-hmfz",
-            "description": "NULL",
-            "title": "MER 2 MARS PANCAM RADIOMETRICALLY\n                                      CALIBRATED RDR V1.0",
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
+            "title": "MER 2 MARS PANCAM RADIOMETRICALLY\n                                      CALIBRATED RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-03-30",
-            "temporal": "2021-03-30T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "ephemeris",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "location",
-                "iss",
-                "international",
-                "coords",
-                "coordinates"
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
-            "identifier": "nasa-iss-data_2021-03-30",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-03-30",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1479543,359 +1479519,361 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-03-30",
+            "issued": "2021-03-30",
+            "keyword": [
+                "ephemeris",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "location",
+                "iss",
+                "international",
+                "coords",
+                "coordinates"
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
+            "temporal": "2021-03-30T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-03-30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VCO-V-IR1-3-SEDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The VCO IR1 SEDR data set contains products of geometry information calculated by SPICE toolkit using SPICE kernels VCO-V-SPICE-6-V1.0, associated with images acquired by the IR1 instrument onboard the Venus Climate Orbiter (VCO, also known as PLANET-C and AKATSUKI) spacecraft. The data files are provided in FITS format with several HDUs as IMAGE extension, and it also contains metadata to the header of the HDUs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vco-v-ir1-3-sedr-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "venus climate orbiter",
                 "earth",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VCO-V-IR1-3-SEDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vco-v-ir1-3-sedr-v1.0",
-            "description": "The VCO IR1 SEDR data set contains products of geometry information calculated by SPICE toolkit using SPICE kernels VCO-V-SPICE-6-V1.0, associated with images acquired by the IR1 instrument onboard the Venus Climate Orbiter (VCO, also known as PLANET-C and AKATSUKI) spacecraft. The data files are provided in FITS format with several HDUs as IMAGE extension, and it also contains metadata to the header of the HDUs.",
-            "title": "VENUS CLIMATE ORBITER IR1 GEOMETRY\n                                      INFORMATION V1.0",
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
+            "title": "VENUS CLIMATE ORBITER IR1 GEOMETRY\n                                      INFORMATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/27A0P5M6LZBI",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lagrangian Snow Distributions for Sea-Ice Applications, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/27A0P5M6LZBI.",
-            "issued": "1980-08-01",
-            "temporal": "1980-08-01T00:00:00Z/2021-07-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-31",
-            "keyword": [
-                "snow/ice",
-                "cryosphere",
-                "sea ice",
-                "earth science",
-                "oceans"
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
-            "identifier": "C1977853902-NSIDCV0",
             "description": "This data set provides daily estimates of snow depth and snow density for snow-on-sea-ice in the Arctic Ocean over a 41-year period using a Lagrangian snow-evolution model forced with NASA\u2019s Modern Era Retrospective-Analysis for Research Applications Version 2 (MERRA-2) and the European Centre for Medium Range Weather Forecasts (ECMWF) Reanalysis, generation 5 (ERA5).",
-            "title": "Lagrangian Snow Distributions for Sea-Ice Applications, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F27A0P5M6LZBI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F27A0P5M6LZBI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0758_lagrangian_snow_distributions_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0758_lagrangian_snow_distributions_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/27A0P5M6LZBI",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/27A0P5M6LZBI",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/27A0P5M6LZBI",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/27A0P5M6LZBI",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1977853902-NSIDCV0",
+            "issued": "1980-08-01",
+            "keyword": [
+                "snow/ice",
+                "cryosphere",
+                "sea ice",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/27A0P5M6LZBI",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "1980-08-01T00:00:00Z/2021-07-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lagrangian Snow Distributions for Sea-Ice Applications, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ESDAB-L2C11",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs/OSWV. 2022-09-28. MEaSUREs Ocean Surface Wind Vectors. Version 1.1.  MetOp-B ASCAT ESDR Level 2 Ancillary Ocean Surface Fields Version 1.1. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ESDAB-L2C11.",
-            "issued": "2022-04-27",
-            "temporal": "2013-08-01T00:00:00Z/2022-05-31T01:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-08",
-            "keyword": [
-                "ocean circulation",
-                "precipitation",
-                "ocean winds",
-                "ocean temperature",
-                "oceans",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere",
-                "altitude"
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
-            "identifier": "C2706510710-POCLOUD",
-            "description": "This dataset contains model output interpolated in space and time to observations from the MetOp-B ASCAT (ASCAT-B) instrument (a satellite-based scatterometer), representing the first science quality release of these data (post-provisional after v1.0) funded under the MEaAUREs program. These auxiliary fields are included to complement the scatterometer observations. Model variables include: i) ocean surface wind fields from ERA-5 short-term forecast (removed from the analyses times to reduce impacts from assimilated scatterometer retrievals at the beginning of the forecast); ii) estimations of precipitation from the GPM IMERG product; iii) estimation of the surface currents from the GlobCurrent project. The modeled fields are provided on a non-uniform grid within the sampled locations of the ASCAT-B Level 2 product, and at a nominal 12.5 km pixel resolution. Each file corresponds to a specific orbital revolution number, which begins at the southernmost point of the ascending orbit.\r\n<br><br>\r\nThe dataset represents the first science quality release of this product with funding from the MEaSUREs (Making Earth System Data Records for Use in Research Environments) program. Version 1.1 provides a set of updates and improvements from version 1.0, including: 1) cleaned up ancillary data points in between the left/right swaths for improved collocation with available satellite data, 2) improved variable metadata, 3) removed the GlobCurrent stokes drift variables, and 4) provided data source metadata including DOIs for the ERA-5, IMERGE, and GlobCurrent data sources. The primary purpose of this Version 1.1 release is for science evaluation by the NASA International Ocean Vector Winds Science Team (IOVWST).",
-            "release-place": "PO.DAAC",
-            "series-name": "MEaSUREs Ocean Surface Wind Vectors",
-            "graphic-preview-description": "Thumbnail",
             "creator": "MEaSUREs/OSWV",
-            "title": "MetOp-B ASCAT ESDR Level 2 Ancillary Ocean Surface Fields Version 1.1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ASCATB_ESDR_MODELED_L2_AUX_V1.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains model output interpolated in space and time to observations from the MetOp-B ASCAT (ASCAT-B) instrument (a satellite-based scatterometer), representing the first science quality release of these data (post-provisional after v1.0) funded under the MEaAUREs program. These auxiliary fields are included to complement the scatterometer observations. Model variables include: i) ocean surface wind fields from ERA-5 short-term forecast (removed from the analyses times to reduce impacts from assimilated scatterometer retrievals at the beginning of the forecast); ii) estimations of precipitation from the GPM IMERG product; iii) estimation of the surface currents from the GlobCurrent project. The modeled fields are provided on a non-uniform grid within the sampled locations of the ASCAT-B Level 2 product, and at a nominal 12.5 km pixel resolution. Each file corresponds to a specific orbital revolution number, which begins at the southernmost point of the ascending orbit.\r\n<br><br>\r\nThe dataset represents the first science quality release of this product with funding from the MEaSUREs (Making Earth System Data Records for Use in Research Environments) program. Version 1.1 provides a set of updates and improvements from version 1.0, including: 1) cleaned up ancillary data points in between the left/right swaths for improved collocation with available satellite data, 2) improved variable metadata, 3) removed the GlobCurrent stokes drift variables, and 4) provided data source metadata including DOIs for the ERA-5, IMERGE, and GlobCurrent data sources. The primary purpose of this Version 1.1 release is for science evaluation by the NASA International Ocean Vector Winds Science Team (IOVWST).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FESDAB-L2C11",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FESDAB-L2C11",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ASCATB_ESDR_MODELED_L2_AUX_V1.1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ASCATB_ESDR_MODELED_L2_AUX_V1.1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2706510710-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2706510710-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2706510710-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2706510710-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ASCATB_ESDR_MODELED_L2_AUX_V1.1.jpg",
+            "identifier": "C2706510710-POCLOUD",
+            "issued": "2022-04-27",
+            "keyword": [
+                "ocean circulation",
+                "precipitation",
+                "ocean winds",
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/ESDAB-L2C11",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "PO.DAAC",
+            "series-name": "MEaSUREs Ocean Surface Wind Vectors",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2013-08-01T00:00:00Z/2022-05-31T01:00:00Z",
             "theme": [
                 "MEaSUREs/OSWV",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MetOp-B ASCAT ESDR Level 2 Ancillary Ocean Surface Fields Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0450-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-22T03:34:50.000 to 2014-11-22T13:25:27.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0450-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0450-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0450-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-22T03:34:50.000 to 2014-11-22T13:25:27.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0450 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0450 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-SUMM-L1COORDS-48SEC-V1.1",
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
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-summ-l1coords-48sec-v1.1_upjv-4ynx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-SUMM-L1COORDS-48SEC-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-summ-l1coords-48sec-v1.1_upjv-4ynx",
-            "description": "not applicable",
-            "title": "VG2 SAT MAG RESAMPLED KRONOGRAPHIC (L1) COORDS 48.0SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT MAG RESAMPLED KRONOGRAPHIC (L1) COORDS 48.0SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0347-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-10T04:52:05.000 to 2014-10-10T15:25:36.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0347-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0347-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0347-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-10T04:52:05.000 to 2014-10-10T15:25:36.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0347 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0347 V1.0"
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
-                "flow",
-                "incompressible",
-                "models",
-                "turbulence",
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
-            "identifier": "NASA-844__19",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1479903,351 +1479881,349 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-844__19",
+            "issued": "2018-06-25",
+            "keyword": [
+                "flow",
+                "incompressible",
+                "models",
+                "turbulence",
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
+            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H40Z716C",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2017-05-26. U.S. Census Grids (Summary File 1), 2010. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/ 10.7927/H40Z716C. https://doi.org/10.7927/H40Z716C.",
-            "issued": "2017-05-26",
-            "temporal": "2010-01-01T00:00:00Z/2010-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-26",
-            "references": [
-                "https://doi.org/10.7927/H4B85623",
-                "https://doi.org/10.7927/H4TB14TN",
-                "https://doi.org/10.7927/H4MP517W"
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
-            "identifier": "C1426173834-SEDAC",
-            "description": "The U.S. Census Grids (Summary File 1), 2010 data set contains grids of demographic and socioeconomic data from the year 2010 in ASCII and GeoTIFF formats. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 2010 TIGER/Line Files and census variables (population, households, and housing variables).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "U.S. Census Grids (Summary File 1), 2010",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The U.S. Census Grids (Summary File 1), 2010 data set contains grids of demographic and socioeconomic data from the year 2010 in ASCII and GeoTIFF formats. The grids have a resolution of 30 arc-seconds (0.0083 decimal degrees), or approximately 1 square km. The gridded variables are based on census block geography from Census 2010 TIGER/Line Files and census variables (population, households, and housing variables).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=+10.7927%2FH40Z716C",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=+10.7927%2FH40Z716C",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file1-2010/usgrid-summary-file1-2010-amind-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file1-2010/usgrid-summary-file1-2010-amind-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2010/maps",
+            "identifier": "C1426173834-SEDAC",
+            "issued": "2017-05-26",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H40Z716C",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-05-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4B85623",
+                "https://doi.org/10.7927/H4TB14TN",
+                "https://doi.org/10.7927/H4MP517W"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 17.0 -65.0 72.0",
+            "temporal": "2010-01-01T00:00:00Z/2010-12-31T00:00:00Z",
             "theme": [
                 "USCG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. Census Grids (Summary File 1), 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3387-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-09-03T05:26:25.000 to 2012-09-03T08:05:09.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3387-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3387-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3387-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-09-03T05:26:25.000 to 2012-09-03T08:05:09.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3387 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3387 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC%2FOSIWAC-5-67P-SHAPE-V1.0",
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
+            "description": "This data set collects shape models and their associated coordinate systems for the Rosetta target 67P/1969 R1 (Churyumov- Gersimenko).  These were produced by the mission teams based on data obtained at the comet.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-osiwac-5-67p-shape-v1.0_uppt-6qpd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC%2FOSIWAC-5-67P-SHAPE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-osiwac-5-67p-shape-v1.0_uppt-6qpd",
-            "description": "This data set collects shape models and their associated coordinate systems for the Rosetta target 67P/1969 R1 (Churyumov- Gersimenko).  These were produced by the mission teams based on data obtained at the comet.",
-            "title": "ROSETTA OSIRIS SHAPE MODELS OF COMET 67P/C-G",
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
+            "title": "ROSETTA OSIRIS SHAPE MODELS OF COMET 67P/C-G"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V7.0",
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
+            "description": "Groundbased radar detections of asteroids, collected from the published literature by S. J. Ostro.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v7.0_upqr-5tzc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V7.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v7.0_upqr-5tzc",
-            "description": "Groundbased radar detections of asteroids, collected from the published literature by S. J. Ostro.",
-            "title": "ASTEROID RADAR V7.0",
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
+            "title": "ASTEROID RADAR V7.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.insitu.calibrated&version=21.0",
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
-                "maven"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The insitu.calibrated level 2 science.data bundle contains selected fully  calibrated (L2) data from the Particles and Fields package and NGIMS, together  with ephemeris information. These data are in physical units and are  averaged/sampled at a uniform cadence. In situ instrument data is derived  directly from Level 2 data. Ephemeris information is derived using SPICE  libraries and kernels provided by MAVEN/NAV team and Lockheed-Martin.",
+            "identifier": "urn:nasa:pds:maven.insitu.calibrated_upra-2882",
+            "issued": "2021-05-21",
+            "keyword": [
+                "maven"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amaven.insitu.calibrated&version=21.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:maven.insitu.calibrated_upra-2882",
-            "description": "The insitu.calibrated level 2 science.data bundle contains selected fully  calibrated (L2) data from the Particles and Fields package and NGIMS, together  with ephemeris information. These data are in physical units and are  averaged/sampled at a uniform cadence. In situ instrument data is derived  directly from Level 2 data. Ephemeris information is derived using SPICE  libraries and kernels provided by MAVEN/NAV team and Lockheed-Martin.",
-            "title": "MAVEN Insitu Key Parameters Data Bundle",
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
+            "title": "MAVEN Insitu Key Parameters Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/AMSRE/AQUA/GPROFCLIM/2A/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_2AGPROFAQUAAMSRE_CLIM. Version 07. GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 5 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/AMSRE/AQUA/GPROFCLIM/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFAQUAAMSRE_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2002-06-01T00:00:00Z/2011-10-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "precipitation",
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264133950-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07. \n\nThe 'CLIM'  products differ from their 'regular' counterparts (without the 'CLIM' in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the 'CLIM' output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\n\nThe 2AGPROF (also known as, GPM GPROF (Level 2)) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors: \n+ TMI (TRMM)\n+ GMI, (GPM)\n+ SSMI (DMSP F11, F13, F14, F15); SSMIS (DMSP F16, F17, F18, F19)\n+ AMSR2 (Aqua)\n+ MHS (NOAA 18,19) \n+ MHS (METOP A,B)\n+ ATMS (NPP)\n+ SAPHIR (MT1)\n\n\nThis provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are near-realtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. The NRT product uses GANAL forecast fields. Standard products use the GANAL analysis product, while the climate product uses ECMWF reanalysis in order to allow for consistent data records with earlier missions. These earlier data may be archived separately. The main strength of the product is the large sampling provided. \n\nThe GPM radiometer algorithms are Bayesian-type algorithms. These algorithms search an a-priori database of potential rain profiles and retrieve a weighted average of these entries based upon the proximity of the observed brightness temperature (Tb) to the simulated Tb corresponding to each rain profile. By using the same a-priori database of rain profiles, with appropriate simulated Tb for each constellation sensor, the Bayesian method is completely parametric and thus well suited for GPM's constellation approach. The a-priori information will be supplied by the combined algorithm supplied by GPM's core satellite as soon after launch as feasible. Databases for V0 of the algorithm had to be constructed from various sources as described in the ATBD. The solution provides a mean rain rate as well as the vertical structure of cloud and precipitation hydrometeors and their uncertainty.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_2AGPROFAQUAAMSRE_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 5 km V07 (GPM_2AGPROFAQUAAMSRE_CLIM) at GES DISC",
-            "graphic-preview-description": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 5 km (GPM_2AGPROFAQUAAMSRE_CLIM)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFAQUAAMSRE_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSRE%2FAQUA%2FGPROFCLIM%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FAMSRE%2FAQUA%2FGPROFCLIM%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFAQUAAMSRE_CLIM_07.png",
-                    "description": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 5 km (GPM_2AGPROFAQUAAMSRE_CLIM)",
                     "@type": "dcat:Distribution",
+                    "description": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 5 km (GPM_2AGPROFAQUAAMSRE_CLIM)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFAQUAAMSRE_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFAQUAAMSRE_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFAQUAAMSRE_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFAQUAAMSRE_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFAQUAAMSRE_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFAQUAAMSRE_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFAQUAAMSRE_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFAQUAAMSRE_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFAQUAAMSRE_CLIM_07",
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
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/doc/README.GPM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/doc/README.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
@@ -1480257,288 +1480233,290 @@
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
-                    "downloadURL": "https://aqua.nasa.gov/amsr-e",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://aqua.nasa.gov/amsr-e",
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
+            "graphic-preview-description": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 5 km (GPM_2AGPROFAQUAAMSRE_CLIM)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFAQUAAMSRE_CLIM_07.png",
+            "identifier": "C2264133950-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "precipitation",
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/AMSRE/AQUA/GPROFCLIM/2A/07",
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
+            "series-name": "GPM_2AGPROFAQUAAMSRE_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-06-01T00:00:00Z/2011-10-04T23:59:59.999Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM AMSR-E on Aqua (GPROF) Climate-based Radiometer Precipitation Profiling L2 1.5 hours 5 km V07 (GPM_2AGPROFAQUAAMSRE_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/DBVUO4KQHXTK",
             "citation": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin. Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin. 2020-07-30. GPCPMON. Version 3.1. GPCP Version 3.1 Satellite-Gauge (SG) Combined Precipitation Data Set. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA GES DISC. https://doi.org/10.5067/DBVUO4KQHXTK. https://disc.gsfc.nasa.gov/datacollection/GPCPMON_3.1.html. Digital Science Data.",
-            "issued": "2020-07-30",
-            "temporal": "1983-01-01T00:00:00Z/2019-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-30",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GEORGE HUFFMAN",
                 "hasEmail": "mailto:George.J.Huffman@nasa.gov"
             },
+            "creator": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1921115203-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Global Precipitation Climatology Project (GPCP) is the precipitation component of an internationally coordinated set of (mainly) satellite-based global products dealing with the Earth's water and energy cycles, under the auspices of the Global Water and Energy Experiment (GEWEX) Data and Assessment Panel (GDAP) of the World Climate Research Program.  As the follow on to the GPCP Version 2.X products, GPCP Version 3 (GPCP V3.1) seeks to continue the long, homogeneous precipitation record using modern merging techniques and input data sets.  The GPCPV3 suite currently consists the 0.5-degree monthly.  Additional products are planned, namely a 0.5\u00b0 daily product for the entire record from 1983 to the (delayed) present and a 0.1\u00b0 3-hourly product from 1998 to the (delayed) present. All GPCPV3 products will be internally consistent.  The monthly product spans 1983 - 2019. Inputs consist of the GPROF SSMI/SSMIS orbit files that are used to calibrate the PERSIANN-CDR IR-based precipitation in the span 60\u00b0N-S.  Outside of 58\u00b0N-S, TOVS/AIRS estimates, calibrated by the IR estimates and the GPCC gauge analyses are used.  This satellite-only estimate is then merged with GPCC gauge analyses over land to compute the final product. In addition to the final precipitation field, ancillary precipitation and error estimates are provided.",
-            "editor": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GPCPMON",
-            "creator": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "GPCP Precipitation Level 3 Monthly 0.5-Degree V3.1 (GPCPMON) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCPMON",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDBVUO4KQHXTK",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDBVUO4KQHXTK",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPCPMON_V31.png",
-                    "description": "A sample map for sat_gauge_precip",
                     "@type": "dcat:Distribution",
+                    "description": "A sample map for sat_gauge_precip",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GPCPMON_V31.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPCPMON_3.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPCPMON_3.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.3.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.3.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPCPMON_3.1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPCPMON_3.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCPMON",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCPMON",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GPCP/GPCPMON.3.1/",
-                    "description": "Access to the data via OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access to the data via OPeNDAP protocol",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GPCP/GPCPMON.3.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.3.1/doc/README.GPCPV3.1_Monthly.pdf",
-                    "description": "README document",
                     "@type": "dcat:Distribution",
+                    "description": "README document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.3.1/doc/README.GPCPV3.1_Monthly.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.1_Monthly.pdf",
-                    "description": "GPCP_ATBD_V3.1_Monthly.pdf\n",
                     "@type": "dcat:Distribution",
+                    "description": "GPCP_ATBD_V3.1_Monthly.pdf\n",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.1_Monthly.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc%3AC00979",
-                    "description": "More information about the GPCP project",
                     "@type": "dcat:Distribution",
+                    "description": "More information about the GPCP project",
+                    "downloadURL": "https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc%3AC00979",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.V3.1.pdf",
-                    "description": "GPCP V3.1 Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "GPCP V3.1 Release Notes",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/Release_Notes.V3.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 }
             ],
+            "editor": "Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin",
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GPCPMON",
+            "identifier": "C1921115203-GES_DISC",
+            "issued": "2020-07-30",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/DBVUO4KQHXTK",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-07-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "GPCPMON",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1983-01-01T00:00:00Z/2019-12-31T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPCP Precipitation Level 3 Monthly 0.5-Degree V3.1 (GPCPMON) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/123/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-10",
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
-            "identifier": "DASHLINK_123",
             "description": "The code in the stableGP package implements Gaussian process calculations using efficient and numerically stable algorithms. Description of the algorithms is in the paper \"Stable and Efficient Gaussian Process Calculations\" by L. Foster, A. Waagen, N. Aijaz, M. Hurley, A. Luis, J. Rinsky, C. Satyavolu, M. Way, P. Gazis, and A. Srivastava accepted in the Journal of Machine Learning Research, February, 2009.\r\n\r\nThe easiest way to get started using the code is to download and unzip the zip file, start Matlab (7.0 or higher), move to the appropriate folder and type either \"demo_bootstrap\" or \"demo_history\" to run one of the demonstration files.\r\n\r\nCode in the zip file is based on the code used in the text Gaussian Processes or Machine Learning by Rasmussen and Williams (www.gaussianprocess.org/gpml/).  So that the demonstrations are self contained and do not require that the user download additional code the zip file contains a few functions that are copied directly from Rasmussen and Williams' code.",
-            "title": "stableGP",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/stableGP.pdf",
-                    "description": "stableGP.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "stableGP.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/stableGP.pdf",
+                    "mediaType": "application/pdf",
                     "title": "stableGP.pdf"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/stableGP.zip",
-                    "description": "stableGP.zip",
                     "@type": "dcat:Distribution",
+                    "description": "stableGP.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/stableGP.zip",
+                    "mediaType": "application/zip",
                     "title": "stableGP.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_123",
+            "issued": "2010-09-10",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/123/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "stableGP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-HVM-PA-4-SUMM-MERGED-1HR-V1.0",
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
-                "jupiter",
-                "pioneer 11"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains data merged from\nmultiple instruments from the Jupiter close encounter. Pioneer 11 plasma\n(PA) and magnetic field (HVM) data from 1974-11-03T00:00:00 to\n1975-01-01T00:00:00. The data include 1 hour averages.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-hvm-pa-4-summ-merged-1hr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "pioneer 11"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-HVM-PA-4-SUMM-MERGED-1HR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-hvm-pa-4-summ-merged-1hr-v1.0",
-            "description": "This dataset contains data merged from\nmultiple instruments from the Jupiter close encounter. Pioneer 11 plasma\n(PA) and magnetic field (HVM) data from 1974-11-03T00:00:00 to\n1975-01-01T00:00:00. The data include 1 hour averages.",
-            "title": "P11 J HVM PA 4-SUMM-MERGED 1HR V1.0",
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
+            "title": "P11 J HVM PA 4-SUMM-MERGED 1HR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA313",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gille, John and Gray, Lesley J.. 2013-08-19. H3ZFCT. Version 007. HIRDLS/Aura Level 3 Temperature 1deg Lat Zonal Fourier Coefficients V007. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/HIRDLS/DATA313. https://disc.gsfc.nasa.gov/datacollection/H3ZFCT_007.html. Digital Science Data.",
-            "issued": "2013-05-06",
-            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-05-06",
-            "keyword": [
-                "earth science",
-                "atmospheric temperature",
-                "atmosphere"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JOHN GILLE",
                 "hasEmail": "mailto:gille@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1251101041-GES_DISC",
-            "description": "The \"HIRDLS/Aura Level 3 Temperature Zonal Fourier Coefficients\" version 7 data product (H3ZFCT) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 1000 to 0.0042 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "H3ZFCT",
             "creator": "Gille, John and Gray, Lesley J.",
-            "title": "HIRDLS/Aura Level 3 Temperature 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFCT_007.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The \"HIRDLS/Aura Level 3 Temperature Zonal Fourier Coefficients\" version 7 data product (H3ZFCT) contains the entire mission (~3 years) of HIRDLS data expressed as zonal Fourier coefficients in 1 degree latitude bands from -64 to 80 degrees at 121 pressure levels. The coefficients are computed from the HIRDLS Level 2 profiles with a Kalman filter approach using both forward and backward passes in time. Expressed as the mean and up to 7 sine and cosine coefficients (4 waves for ascending and descending, 7 waves for combined), these coefficients may be used to compute values at any longitude. The data are provided on a pressure grid with 24 levels per decade, corresponding to about 1 km vertical resolution. The useful vertical range of the data is 1000 to 0.0042 hPa. The precision values are given by the root-mean square of the differences between the estimated fields and the input data.\n\nThe data are stored in the version 5 Hierarchical Data Format for the Earth Observing System (HDF-EOS5), which is an extension of the HDF5 format. Each file contains a zonal object with data for the entire mission with separate data fields for ascending (daytime), descending (nighttime), and combined orbit node.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA313",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FHIRDLS%2FDATA313",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1480548,862 +1480526,857 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFCT_007.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/H3ZFCT_007.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFCT.007/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_HIRDLS_Level3/H3ZFCT.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFCT.007/HIRDLS-Aura_L3ZFCT_v07-00-20-c01_2005d022-2008d077.he5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_HIRDLS_Level3/H3ZFCT.007/HIRDLS-Aura_L3ZFCT_v07-00-20-c01_2005d022-2008d077.he5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFCT_007",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=H3ZFCT_007",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.5_Product_Quality/HIRDLS-DQD_V7.pdf",
-                    "description": "README and Data Quality document",
                     "@type": "dcat:Distribution",
+                    "description": "README and Data Quality document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.5_Product_Quality/HIRDLS-DQD_V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.6_Product_Application/All_HIRDLS_Papers_26June2013.pdf",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/HIRDLS/3.3_Product_Documentation/3.3.6_Product_Application/All_HIRDLS_Papers_26June2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/H3ZFCT_007.png",
+            "identifier": "C1251101041-GES_DISC",
+            "issued": "2013-05-06",
+            "keyword": [
+                "earth science",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/HIRDLS/DATA313",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-05-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "H3ZFCT",
             "spatial": "-180.0 -64.0 180.0 80.0",
+            "temporal": "2005-01-22T00:00:00Z/2008-03-17T23:59:59.999Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HIRDLS/Aura Level 3 Temperature 1deg Lat Zonal Fourier Coefficients V007 (H3ZFCT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/POLARIS_Model_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/POLARIS_Model_Data_1.",
-            "issued": "1997-04-09",
-            "temporal": "1997-01-06T00:00:00Z/1997-09-26T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-05-13",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
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
-            "identifier": "C2712777352-LARC_ASDC",
             "description": "POLARIS_Model_Data is the model data collected during the Photochemistry of Ozone Loss in the Arctic Region in Summer (POLARIS) campaign. Data collection for this product is complete.\r\n\r\nThe POLARIS mission was a joint effort of NASA and NOAA that occurred in 1997 and was designed to expand on the photochemical and transport processes that cause the summer polar decreases in the stratospheric ozone. The POLARIS campaign had the overarching goal of better understanding the change of stratospheric ozone levels from very high concentrations in the spring to very low concentrations in the autumn. The NASA ER-2 high-altitude aircraft was the primary platform deployed along with balloons, satellites, and ground-sites. The POLARIS campaign was based in Fairbanks, Alaska with some flights being conducted from California and Hawaii. Flights were conducted between the summer solstice and fall equinox at mid- to high latitudes. The data collected included meteorological variables; long-lived tracers in reference to summertime transport questions; select species with reactive nitrogen (NOy), halogen (Cly), and hydrogen (HOx) reservoirs; and aerosols. More specifically, the ER-2 utilized various techniques/instruments including Laser Absorption, Gas Chromatography, Non-dispersive IR, UV Photometry, Catalysis, and IR Absorption. These techniques/instruments were used to collect data including N2O, CH4, CH3CCl3, CO2, O3, H2O, and NOy. Ground stations were responsible for collecting SO2 and O3, while balloons recorded pressure, temperature, wind speed, and wind directions. Satellites partnered with these platforms collected meteorological data and Lidar imagery. The observations were used to constrain stratospheric computer models to evaluate ozone changes due to chemistry and transport.",
-            "title": "POLARIS Model Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FPOLARIS_Model_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FPOLARIS_Model_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/polaris",
-                    "description": "ESPO Home Page for POLARIS",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for POLARIS",
+                    "downloadURL": "https://espo.nasa.gov/polaris",
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
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/1999JD900832",
-                    "description": "Preface [to special section on Photochemistry of Ozone Loss in the Arctic Region in Summer (POLARIS)]",
                     "@type": "dcat:Distribution",
+                    "description": "Preface [to special section on Photochemistry of Ozone Loss in the Arctic Region in Summer (POLARIS)]",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/1999JD900832",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/POLARIS/Model_Data_1/",
-                    "description": "ASDC Direct Data Download for POLARIS_Model_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for POLARIS_Model_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/POLARIS/Model_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2712777352-LARC_ASDC",
-                    "description": "Earthdata Search for POLARIS_Model_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for POLARIS_Model_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2712777352-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/POLARIS_Model_Data_1",
-                    "description": "DOI for POLARIS_Model_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for POLARIS_Model_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/POLARIS_Model_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2712777352-LARC_ASDC",
+            "issued": "1997-04-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/POLARIS_Model_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1997-05-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-3.37 -171.0 -3.37 152.075 90.0 152.075 90.0 -171.0 -3.37 -171.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-01-06T00:00:00Z/1997-09-26T00:00:00Z",
             "theme": [
                 "POLARIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "POLARIS Model Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Joshua Fisher, Martha Anderson. 2019-08-01. ECOSTRESS Evapotranspiration dis-ALEXI USDA Daily L3 Global 30 m V001. Archived by National Aeronautics and Space Administration, U.S. Government,  NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001. https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2018-07-30",
-            "temporal": "2018-07-30T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-29",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
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
-            "identifier": "C1534730413-LPDAAC_ECS",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data over the conterminous United States (CONUS) as well as key biomes and agricultural zones around the world and selected [FLUXNET](http://fluxnet.fluxdata.org/about/) validation sites. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe United States Department of Agriculture (USDA) ECO3ETALEXIU Version 1 data product provides estimates of daily evapotranspiration (ET) using the ECOSTRESS Level 2 (L2) land surface temperature and emissivity (LST&E) product, along with ancillary meteorological data and remotely sensed vegetation cover information. The ECO3ETALEXIU data product is derived using a physics-based surface energy balance (SEB) algorithm, the Atmosphere Land Exchange Inverse (ALEXI) Disaggregation algorithm (disALEXI). Described in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/332/ECO3ETALEXIU_ATBD_V1.pdf), disALEXI is based on spatial disaggregation of regional-scale fluxes from the ALEXI SEB model. Many approaches exist for mapping ET spatially; however, SEB methods are favored for remote sensing retrievals based on land-surface temperature. ALEXI was initially developed for managed landscapes. Applications include crop water use, crop phenology monitoring, and drought early warning or water stress detection. The output ET is generated on a UTM grid at a spatial resolution of 30 meters.\r\n\r\nThe ECO3ETALEXIU Version 1 data product contains layers of daily ET, ET uncertainty, and associated quality flags. A low-resolution browse is also available showing daily ET as a stretched image with a color ramp in JPEG format.",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Joshua Fisher, Martha Anderson",
-            "title": "ECOSTRESS Evapotranspiration dis-ALEXI USDA Daily L3 Global 30m V001",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.07.25/ECOSTRESS_L3_ET_ALEXI_USDA_00731_008_20180822T201811_0503_03.mead.1.jpg?_ga=2.229793116.1575605641.1565613093-1371303444.1563801461",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data over the conterminous United States (CONUS) as well as key biomes and agricultural zones around the world and selected [FLUXNET](http://fluxnet.fluxdata.org/about/) validation sites. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe United States Department of Agriculture (USDA) ECO3ETALEXIU Version 1 data product provides estimates of daily evapotranspiration (ET) using the ECOSTRESS Level 2 (L2) land surface temperature and emissivity (LST&E) product, along with ancillary meteorological data and remotely sensed vegetation cover information. The ECO3ETALEXIU data product is derived using a physics-based surface energy balance (SEB) algorithm, the Atmosphere Land Exchange Inverse (ALEXI) Disaggregation algorithm (disALEXI). Described in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/332/ECO3ETALEXIU_ATBD_V1.pdf), disALEXI is based on spatial disaggregation of regional-scale fluxes from the ALEXI SEB model. Many approaches exist for mapping ET spatially; however, SEB methods are favored for remote sensing retrievals based on land-surface temperature. ALEXI was initially developed for managed landscapes. Applications include crop water use, crop phenology monitoring, and drought early warning or water stress detection. The output ET is generated on a UTM grid at a spatial resolution of 30 meters.\r\n\r\nThe ECO3ETALEXIU Version 1 data product contains layers of daily ET, ET uncertainty, and associated quality flags. A low-resolution browse is also available showing daily ET as a stretched image with a color ramp in JPEG format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO3ETALEXIU.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO3ETALEXIU.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534730413-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534730413-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO3ETALEXIU.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO3ETALEXIU.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/331/ECO3ETALEXIU_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/331/ECO3ETALEXIU_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/332/ECO3ETALEXIU_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/332/ECO3ETALEXIU_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001",
-                    "description": "Digital Object Identifier",
                     "@type": "dcat:Distribution",
+                    "description": "Digital Object Identifier",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/333/ECO3ETALEXIU_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECO3ETALEXIU product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECO3ETALEXIU product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/333/ECO3ETALEXIU_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/227/ECO_Earthdata_Search_Quick_Guide.pdf",
-                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/227/ECO_Earthdata_Search_Quick_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.07.25/ECOSTRESS_L3_ET_ALEXI_USDA_00731_008_20180822T201811_0503_03.mead.1.jpg?_ga=2.229793116.1575605641.1565613093-1371303444.1563801461",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.07.25/ECOSTRESS_L3_ET_ALEXI_USDA_00731_008_20180822T201811_0503_03.mead.1.jpg?_ga=2.229793116.1575605641.1565613093-1371303444.1563801461",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.07.25/ECOSTRESS_L3_ET_ALEXI_USDA_00731_008_20180822T201811_0503_03.mead.1.jpg?_ga=2.229793116.1575605641.1565613093-1371303444.1563801461",
+            "identifier": "C1534730413-LPDAAC_ECS",
+            "issued": "2018-07-30",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXIU.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-07-30T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Evapotranspiration dis-ALEXI USDA Daily L3 Global 30m V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3708-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-03-07T00:23:12 to 2015-03-09T13:59:26.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3708-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3708-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3708-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-03-07T00:23:12 to 2015-03-09T13:59:26.000.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3708 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3708 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/13677",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-10-01",
-            "temporal": "2012-10-01T00:00:00Z/2014-09-01T00:00:00Z",
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
-                "johnson space center",
-                "active",
-                "element"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Gaddis",
                 "hasEmail": "mailto:stephen.w.gaddis@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_13677",
             "description": "&lt;p&gt;During 2014, the &lt;em&gt;Extreme Terrain Mobility &lt;/em&gt;project element is developing five technologies:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Exoskeleton Development for ISS Evaluation&lt;/li&gt;&lt;li&gt;Extreme Terrain Mobility Testbed&lt;/li&gt;&lt;li&gt;Low Gravity Testbed using Tethered Stewart Platform&lt;/li&gt;&lt;li&gt;Prototype Crater Access Robot&lt;/li&gt;&lt;li&gt;Advanced Mobility Navigation Software&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;&lt;strong&gt;Exoskeleton Development for ISS Evaluation&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;During FY12, HRS and GCD developed the X1 exoskeleton with the ultimate intent of augmenting crew endurance/strength in future missions.&amp;nbsp; Offshoots of the technology involved lightweight exercise devices for ISS and strength measurement by using the torque sensing in the X1&amp;rsquo;s joints.&amp;nbsp; The objective for exoskeleton development in FY14 is to build prototype exoskeleton ankles and deliver them to the JSC space and life sciences organization for evaluation as exercise devices and to design a single-joint knee dynamometer, based on X1 technologies, capable of measuring crew strength.&amp;nbsp;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Extreme Terrain Mobility Testbed&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The objective of FY14 work is to present mature systems that are ready to be carried forward by a Science Mission Directorate Principal Investigator (PI) willing to propose a system with greater mobility than exists on current Mars rovers.&amp;nbsp; HRS has recently identified a potential national need with the National Science Foundation (NSF) that requires no-emission vehicles, such as NASA rovers, on the Arctic, Antarctic, Alaska and polar coastal areas.&amp;nbsp; We have an opportunity to deploy NASA Space Technologies to these areas. Minimal success requires disseminating results to potential SMD PIs and potential partners within the NSF polar program.&amp;nbsp; Early in fiscal year 2014, the HRS extreme terrain mobility group will prepare an Analysis of Alternatives study of a 170 kg rover for the Advance Exploration System (AES) Resource Prospector (RP).&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Low Gravity Testbed using Tethered Stewart Platform&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;This task creates a 6-DOF testbed for evaluating microgravity and low-gravity proximity and contact operations, e.g. in the vicinity of a Near Earth Asteroid (NEA). This is accomplished using an &amp;quot;inverted Stewart platform&amp;quot;, where the vehicle under test is suspended by six computer-controlled cable winches so that it can be maneuvered in all 6 Degrees-of-Freedom.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Prototype Crater Access Robot&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;This task will develop and demonstrate a &amp;ldquo;mother-daughter&amp;rdquo; approach to exploring craters using tethered robots.&amp;nbsp; The small robots will be tethered to the larger robot with winches on both ends so that the &amp;ldquo;mother&amp;rdquo; can recover the &amp;ldquo;daughter&amp;rdquo; even in the event of failure of the small robot.&amp;nbsp; In normal operation, the daughter robot will pay out the tether to move further away, and spool it back in to return.&amp;nbsp; In FY13, this task demonstrated deployment of the daughter robot with an internal winch on a tether. The daughter robot is designed to move on steep slopes, up to vertical, to carry and point close-up instruments, and to collect samples.&amp;nbsp; In FY14, this task will design and build a tether that provides power from the mother robot to the daughter robot and provides for communications between them.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Advanced Mobility Navigation Software&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;The Advanced Navigation Software task is developing approaches for dealing with the significant challenges of autonomous planetary surface navigation, including descent on rough and steep terrain, exploring lava tubes, navigating long distances without co",
-            "title": "Human Robotic Systems (HRS): Extreme Terrain Mobility Element",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/13677",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_13677",
+            "issued": "2012-10-01",
+            "keyword": [
+                "johnson space center",
+                "active",
+                "element"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/13677",
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
+            "temporal": "2012-10-01T00:00:00Z/2014-09-01T00:00:00Z",
+            "title": "Human Robotic Systems (HRS): Extreme Terrain Mobility Element"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0380-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-23T03:48:31.000 to 2014-10-23T14:45:48.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0380-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0380-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0380-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-23T03:48:31.000 to 2014-10-23T14:45:48.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0380 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0380 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3230-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-02-03T00:12:00.000 to 2012-02-03T02:54:05.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3230-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3230-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3230-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-02-03T00:12:00.000 to 2012-02-03T02:54:05.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3230 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3230 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1966",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, R.O. Green, and B. Cairns. 2022. MASTER: HyspIRI Airborne Campaign, California, Fall 2013. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1966",
-            "issued": "2023-07-08",
-            "temporal": "2013-09-13T17:23:51Z/2013-12-05T21:22:39Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "surface radiative properties",
-                "visible wavelengths",
-                "earth science",
-                "land surface",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "surface thermal properties"
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
-            "identifier": "C2731688788-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The raw data were collected as part of the Hyperspectral Infrared Imager (HyspIRI) mission's preparatory airborne campaign during 11 flights aboard a NASA ER-2 aircraft over California and Nevada, U.S., from 2013-09-13 to 2013-12-05. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 1 acquired on 13 September 2013 over the Rim Fire scar at Yosemite National Park, California, U.S. Source: MASTERL1B_1364500_01_20130913_1723_1729_V03.jpg",
-            "title": "MASTER: HyspIRI Airborne Campaign, California, Fall 2013",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Fall_2013_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1966",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1966",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_HyspIRI_Fall_2013/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_HyspIRI_Fall_2013/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Fall_2013.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Fall_2013.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1966",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1966",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_HyspIRI_Fall_2013/comp/MASTER_HyspIRI_Fall_2013.pdf",
-                    "description": "MASTER: HyspIRI Airborne Campaign, California, Fall 2013: MASTER_HyspIRI_Fall_2013.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: HyspIRI Airborne Campaign, California, Fall 2013: MASTER_HyspIRI_Fall_2013.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_HyspIRI_Fall_2013/comp/MASTER_HyspIRI_Fall_2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Fall_2013_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 1 acquired on 13 September 2013 over the Rim Fire scar at Yosemite National Park, California, U.S. Source: MASTERL1B_1364500_01_20130913_1723_1729_V03.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 1 acquired on 13 September 2013 over the Rim Fire scar at Yosemite National Park, California, U.S. Source: MASTERL1B_1364500_01_20130913_1723_1729_V03.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Fall_2013_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 1 acquired on 13 September 2013 over the Rim Fire scar at Yosemite National Park, California, U.S. Source: MASTERL1B_1364500_01_20130913_1723_1729_V03.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Fall_2013_Fig1.jpg",
+            "identifier": "C2731688788-ORNL_CLOUD",
+            "issued": "2023-07-08",
+            "keyword": [
+                "surface radiative properties",
+                "visible wavelengths",
+                "earth science",
+                "land surface",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1966",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-123.75 31.95 -112.5 40.98",
+            "temporal": "2013-09-13T17:23:51Z/2013-12-05T21:22:39Z",
             "theme": [
                 "MASTER",
                 "HyspIRI Airborne",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: HyspIRI Airborne Campaign, California, Fall 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/AERDT_L2_VIIRS_SNPP.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2023-09-21. VIIRS/SNPP Dark Target Aerosol L2 6-Min Swath 6 km. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/AERDT_L2_VIIRS_SNPP.002. https://doi.org/10.5067/VIIRS/AERDT_L2_VIIRS_SNPP.002.",
-            "issued": "2023-08-01",
-            "temporal": "2012-03-01T00:36:00Z/2024-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sips.support@ssec.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2771506686-LAADS",
-            "description": "The VIIRS/SNPP Dark Target Aerosol L2 6-Min Swath 6 km product provides satellite-derived measurements of Aerosol Optical Thickness (AOT) and their properties over land and ocean, and spectral AOT and their size parameters over oceans every 6 minutes, globally.  The Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS) incarnation of the dark target (DT) aerosol product is based on the same DT algorithm that was developed and used to derive products from the Terra and Aqua mission&#8217;s MODIS instruments.  Two separate and distinct DT algorithms exist.  One helps retrieve aerosol information over ocean (dark in visible and longer wavelengths), while the second aids retrievals over vegetated/dark-soiled land (dark in the visible).\r\n\r\nThis orbit-level product (Short-name: AERDT_L2_VIIRS_SNPP) has an at-nadir resolution of 6 km x 6 km, and progressively increases away from nadir given the sensor's scanning geometry and Earth's curvature. Viewed differently, this product's resolution accommodates 8 x 8 native VIIRS moderate-resolution (M-band) pixels that nominally have ~750 m horizontal pixel size. Hence, the Level-2 Dark Target Aerosol Optical Thickness data product incorporates 64 (750 m) pixels over a 6-minute acquisition. Version 2.0 constitutes the latest collection of the L2 Dark Target Aerosol product and contains improvements over its previous collection (v1.1).\r\n\r\nFor more information consult LAADS product description page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDT_L2_VIIRS_SNPP\r\n\r\nOr, Dark Target aerosol team Page at: \r\nhttps://darktarget.gsfc.nasa.gov/",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/SNPP Dark Target Aerosol L2 6-Min Swath 6 km V2",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/SNPP Dark Target Aerosol L2 6-Min Swath 6 km product provides satellite-derived measurements of Aerosol Optical Thickness (AOT) and their properties over land and ocean, and spectral AOT and their size parameters over oceans every 6 minutes, globally.  The Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS) incarnation of the dark target (DT) aerosol product is based on the same DT algorithm that was developed and used to derive products from the Terra and Aqua mission&#8217;s MODIS instruments.  Two separate and distinct DT algorithms exist.  One helps retrieve aerosol information over ocean (dark in visible and longer wavelengths), while the second aids retrievals over vegetated/dark-soiled land (dark in the visible).\r\n\r\nThis orbit-level product (Short-name: AERDT_L2_VIIRS_SNPP) has an at-nadir resolution of 6 km x 6 km, and progressively increases away from nadir given the sensor's scanning geometry and Earth's curvature. Viewed differently, this product's resolution accommodates 8 x 8 native VIIRS moderate-resolution (M-band) pixels that nominally have ~750 m horizontal pixel size. Hence, the Level-2 Dark Target Aerosol Optical Thickness data product incorporates 64 (750 m) pixels over a 6-minute acquisition. Version 2.0 constitutes the latest collection of the L2 Dark Target Aerosol product and contains improvements over its previous collection (v1.1).\r\n\r\nFor more information consult LAADS product description page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDT_L2_VIIRS_SNPP\r\n\r\nOr, Dark Target aerosol team Page at: \r\nhttps://darktarget.gsfc.nasa.gov/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FAERDT_L2_VIIRS_SNPP.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FAERDT_L2_VIIRS_SNPP.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://darktarget.gsfc.nasa.gov/pubs",
-                    "description": "Data product documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data product documentation",
+                    "downloadURL": "https://darktarget.gsfc.nasa.gov/pubs",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/AERDT_L2_VIIRS_SNPP--5200",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/AERDT_L2_VIIRS_SNPP--5200",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5200/AERDT_L2_VIIRS_SNPP/",
-                    "description": "Direct link to Collection's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct link to Collection's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5200/AERDT_L2_VIIRS_SNPP/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/DT_Aerosol_UG_MODIS_VIIRS_March_2023.pdf",
-                    "description": "A pdf version User's Guide for MODIS and VIIRS dark target products.",
                     "@type": "dcat:Distribution",
+                    "description": "A pdf version User's Guide for MODIS and VIIRS dark target products.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/DT_Aerosol_UG_MODIS_VIIRS_March_2023.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://darktarget.gsfc.nasa.gov/atbd/overview",
-                    "description": "An Agorithm Theoretical Basis Document (ATBD) for MODIS and VIIRS dark target products.",
                     "@type": "dcat:Distribution",
+                    "description": "An Agorithm Theoretical Basis Document (ATBD) for MODIS and VIIRS dark target products.",
+                    "downloadURL": "https://darktarget.gsfc.nasa.gov/atbd/overview",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "identifier": "C2771506686-LAADS",
+            "issued": "2023-08-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/AERDT_L2_VIIRS_SNPP.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-03-01T00:36:00Z/2024-09-30T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/SNPP Dark Target Aerosol L2 6-Min Swath 6 km V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D35.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang\r\n. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand3 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D35.061. https://doi.org/10.5067/MODIS/MCD43D35.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
-                "earth science",
-                "national geospatial data asset",
-                "ngda"
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
-            "identifier": "C2540270757-LPCLOUD",
-            "description": "The MCD43D35 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) QA ValidObs Band 3 dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. MCD43D35 provides MODIS band 3 valid observation quality information for the MCD43D products. \r\n\r\nMCD43D35 contains the valid observation quality layer representing each of the 16 days of the retrieval period for MODIS band 3.  \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand3 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D35 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) QA ValidObs Band 3 dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. MCD43D35 provides MODIS band 3 valid observation quality information for the MCD43D products. \r\n\r\nMCD43D35 contains the valid observation quality layer representing each of the 16 days of the retrieval period for MODIS band 3.  \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D35.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D35.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D35.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D35.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540270757-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540270757-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D35.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D35.061",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/terra_aqua_modis/v006",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/terra_aqua_modis/v006",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/97/MCD43_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/97/MCD43_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D35",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D35",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 4 has been achieved for all MODIS BRDF/Albedo products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 4 has been achieved for all MODIS BRDF/Albedo products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43",
-                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D35.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D35.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540270757-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D35.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra+Aqua BRDF/Albedo QA ValidobsBand3 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AMSR-E/AE_SID.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/Aqua Daily L3 6.25 km Sea Ice Drift Polar Grids V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/AMSR-E/AE_SID.001.",
-            "issued": "2011-05-30",
-            "temporal": "2011-05-30T00:00:00Z/2011-10-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-10-03",
-            "keyword": [
-                "sea ice",
-                "oceans",
-                "earth science",
-                "microwave",
-                "spectral/engineering"
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
-            "identifier": "C186290274-NSIDC_ECS",
             "description": "This product provides 6.25 km sea ice drift grids for the Northern and Southern Hemispheres.",
-            "title": "AMSR-E/Aqua Daily L3 6.25 km Sea Ice Drift Polar Grids V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAE_SID.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAE_SID.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_SID.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AE_SID.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C186290274-NSIDC_ECS&m=-63.984375%212.25%211%211%210%210%2C2&q=AE_SID",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C186290274-NSIDC_ECS&m=-63.984375%212.25%211%211%210%210%2C2&q=AE_SID",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AE_SID/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AE_SID/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_SID.001",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_SID.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_SID.001",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AE_SID.001",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C186290274-NSIDC_ECS",
+            "issued": "2011-05-30",
+            "keyword": [
+                "sea ice",
+                "oceans",
+                "earth science",
+                "microwave",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/AMSR-E/AE_SID.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-10-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -39.23",
+            "temporal": "2011-05-30T00:00:00Z/2011-10-03T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua Daily L3 6.25 km Sea Ice Drift Polar Grids V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2013",
             "citation": "Pepijn Veefkind. 2012-03-09. OMDOAO3G. Version 003. OMI/Aura Ozone (O3) DOAS Total Column Daily L2 Global Gridded 0.25 degree x 0.25 degree V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA2013. https://disc.gsfc.nasa.gov/datacollection/OMDOAO3G_003.html. Digital Science Data.",
-            "issued": "2004-10-01",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-03-09",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JENNIFER WEI",
                 "hasEmail": "mailto:jennifer.c.wei@nasa.gov"
             },
+            "creator": "Pepijn Veefkind",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1266136103-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This Level-2G daily global gridded product OMDOAO3G is based on the pixel level OMI Level-2 DOAO3 product OMDOAO3.  This Level-2G global total column ozone product is derived from OMDOAO3 which is based on the Differential Absorption Spectroscopy (DOAS) fitting technique that essentially uses the OMI visible radiance values between 331.1 and 336.1 nm. In addition to the total ozone column this product also contains some auxiliary derived and ancillary input parameters, e.g. ozone slant column density, ozone ghost column density, etc. The short name for this Level-2 OMI ozone product is OMDOAO3G and the lead algorithm scientist for this product and for OMDOAO3 (the data source of OMDOAO3G) is Dr. Pepijn Veefkind from KNMI.\n\nThe OMDOAO3G product files are stored in the version 5 Hierarchical Data Format (HDF-EOS5). Each daily file contains data from the day lit portion of the orbits (approximately 14 orbits) and is roughly 80 MB in size.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMDOAO3G",
-            "creator": "Pepijn Veefkind",
-            "title": "OMI/Aura Ozone (O3) DOAS Total Column Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMDOAO3G) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMDOAO3G_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2013",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2013",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1481413,73 +1481386,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMDOAO3G_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMDOAO3G_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level2G/OMDOAO3G.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/Aura_OMI_Level2G/OMDOAO3G.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMDOAO3G_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMDOAO3G_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2G/OMDOAO3G.003/doc/OMDOAO3G_OSIPS_README_V003.doc",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2G/OMDOAO3G.003/doc/OMDOAO3G_OSIPS_README_V003.doc",
+                    "mediaType": "application/msword",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/README.OMI_DUG.pdf",
-                    "description": "OMI User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "OMI User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/README.OMI_DUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMDOAO3G_FileSpec_V003.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/OMDOAO3G_FileSpec_V003.pdf",
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
-                    "downloadURL": "http://projects.knmi.nl/omi/research/news/newsWrap.php?language=only_enhttps%3A%2F%2Fwww.knmi.nl%2FomitimeFrame%3Dlatesthttps%3A%2F%2Fwww.knmi.nl%2Fomichoise%3Dpage",
-                    "description": "OMI KNMI Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OMI KNMI Home Page",
+                    "downloadURL": "http://projects.knmi.nl/omi/research/news/newsWrap.php?language=only_enhttps%3A%2F%2Fwww.knmi.nl%2FomitimeFrame%3Dlatesthttps%3A%2F%2Fwww.knmi.nl%2Fomichoise%3Dpage",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-02.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-02.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level2G/OMDOAO3G.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level2G/OMDOAO3G.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
@@ -1481489,330 +1481462,330 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMDOAO3G_003.png",
+            "identifier": "C1266136103-GES_DISC",
+            "issued": "2004-10-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2013",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-03-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1109/TGRS.2006.869987",
+                "https://doi.org/10.1109/TGRS.2006.872935",
+                "https://doi.org/10.1117/12.627013"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMDOAO3G",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Ozone (O3) DOAS Total Column Daily L2 Global Gridded 0.25 degree x 0.25 degree V3 (OMDOAO3G) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1342-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-14T21:02:05.000 to 2016-01-15T00:47:52.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1342-v1.0_uqjk-kb9k",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1342-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1342-v1.0_uqjk-kb9k",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-14T21:02:05.000 to 2016-01-15T00:47:52.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1342 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1342 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-PFES-3-RDR-SPECTRUM-V1.0",
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
-                "geologic remote sensing field experiment",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Portable Field Emission Spectrometer (PFES) data were acquired on July 15 and 17, 1989. A total of 31 measurements were collected for GRSFE. Of these measurements, 13 were calibrations and 18 were of representative surfaces. The data were collected primarily to support the calibration of the TIMS data and to assist in interpreting spectral mixing in the mid-infrared. Sites were selected for calibration that covered a range of emissivities. On July 15, PFES data were collected at Kelso Dunes and the Cima Volcanic Field as part of the Calibration Team effort. Daedalus and SIRIS data were collected over the same sites. For the PFES data, the Kelso Dunes Bright Target site represented the silica-rich endmember and the Cima basalt tephra Dark Target site represented the more silica-poor endmember. On July 17, PFES data were collected at two of the modelling sites at Lunar Lake (the playa and the cobble sites). Several spectra were also collected at the playa surface next to the Lunar Lake thermistor site.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-pfes-3-rdr-spectrum-v1.0_uqna-q2b5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "geologic remote sensing field experiment",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-PFES-3-RDR-SPECTRUM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-pfes-3-rdr-spectrum-v1.0_uqna-q2b5",
-            "description": "Portable Field Emission Spectrometer (PFES) data were acquired on July 15 and 17, 1989. A total of 31 measurements were collected for GRSFE. Of these measurements, 13 were calibrations and 18 were of representative surfaces. The data were collected primarily to support the calibration of the TIMS data and to assist in interpreting spectral mixing in the mid-infrared. Sites were selected for calibration that covered a range of emissivities. On July 15, PFES data were collected at Kelso Dunes and the Cima Volcanic Field as part of the Calibration Team effort. Daedalus and SIRIS data were collected over the same sites. For the PFES data, the Kelso Dunes Bright Target site represented the silica-rich endmember and the Cima basalt tephra Dark Target site represented the more silica-poor endmember. On July 17, PFES data were collected at two of the modelling sites at Lunar Lake (the playa and the cobble sites). Several spectra were also collected at the playa surface next to the Lunar Lake thermistor site.",
-            "title": "FIELD EXP EARTH PFES CALIBRATED RDR SPECTRUM V1.0",
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
+            "title": "FIELD EXP EARTH PFES CALIBRATED RDR SPECTRUM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD10_L2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS/Aqua Snow Cover 5-Min L2 Swath 500m V061. Version 61. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD10_L2.061.",
-            "issued": "2002-07-04",
-            "temporal": "2002-07-04T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-20",
-            "keyword": [
-                "national geospatial data asset",
-                "cryosphere",
-                "earth science",
-                "ngda",
-                "snow/ice"
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
-            "identifier": "C1646610101-NSIDC_ECS",
             "description": "This global Level-2 (L2) data set provides daily snow cover detected using Normalized Difference Snow Index (NDSI) and a series of screens designed to alleviate errors and flag uncertain snow cover detections. The NDSI is derived from radiance data acquired by the Moderate Resolution Imaging Spectroradiometer (MODIS) on board the Aqua satellite: DOI:10.5067/MODIS/MYD02HKM.061 and DOI:10.5067/MODIS/MYD021KM.061. Each data granule contains 5 minutes of swath data observed at a resolution of 500 m.\n\nThe terms \"Version 61\" and \"Collection 6.1\" are used interchangeably in reference to this release of MODIS data.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "MODIS/Aqua Snow Cover 5-Min L2 Swath 500m V061",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-206,-86,159,83&l=MODIS_Aqua_NDSI_Snow_Cover,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD10_L2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD10_L2.061",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOSA/MYD10_L2.061",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOSA/MYD10_L2.061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MYD10_L2+V061",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MYD10_L2+V061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/MYD10_L2/versions/61/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/MYD10_L2/versions/61/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-206%2C-86%2C159%2C83&l=MODIS_Aqua_NDSI_Snow_Cover%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-206%2C-86%2C159%2C83&l=MODIS_Aqua_NDSI_Snow_Cover%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10_L2.061",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10_L2.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10_L2.061",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10_L2.061",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-206,-86,159,83&l=MODIS_Aqua_NDSI_Snow_Cover,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C1646610101-NSIDC_ECS",
+            "issued": "2002-07-04",
+            "keyword": [
+                "national geospatial data asset",
+                "cryosphere",
+                "earth science",
+                "ngda",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD10_L2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Snow Cover 5-Min L2 Swath 500m V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-D-GDDS-5-DUST-V4.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains the data from the Galileo dust detector system (GDDS) from start of mission through the end of mission. Included are the dust impact data, noise data, laboratory calibration data, and location and orientation of the spacecraft and instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-d-gdds-5-dust-v4.1_uqnn-vvsc",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dust",
                 "calibration",
                 "galileo"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-D-GDDS-5-DUST-V4.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-d-gdds-5-dust-v4.1_uqnn-vvsc",
-            "description": "This data set contains the data from the Galileo dust detector system (GDDS) from start of mission through the end of mission. Included are the dust impact data, noise data, laboratory calibration data, and location and orientation of the spacecraft and instrument.",
-            "title": "GALILEO DUST DETECTION SYSTEM V4.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO DUST DETECTION SYSTEM V4.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0355-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-13T03:34:50.000 to 2014-10-13T15:16:06.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0355-v1.0_uqqz-uaj4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0355-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0355-v1.0_uqqz-uaj4",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-13T03:34:50.000 to 2014-10-13T15:16:06.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0355 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0355 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1323",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Walker, D.A., and M.K. Raynolds. 2018. Circumpolar Arctic Vegetation, Geobotanical, Physiographic Maps, 1982-2003. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1323",
-            "issued": "2018-12-31",
-            "temporal": "1982-06-01T00:00:00Z/2010-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "ecosystems",
-                "vegetation",
-                "topography",
-                "land surface",
-                "landscape",
-                "earth science",
-                "biosphere",
-                "atmospheric temperature",
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
-            "identifier": "C2170968604-ORNL_CLOUD",
             "description": "This data set provides the spatial distributions of vegetation types, geobotanical characteristics, and physiographic features for the circumpolar Arctic tundra biome for the period 1982-2003. Specific attributes include dominant vegetation, bioclimate subzones, floristic subprovinces, landscape types, lake coverage, Arctic treeline, elevation, and substrate chemistry data. Vegetation indices, trends, and biomass estimate products for the circumpolar Arctic through 2010 are also provided.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Circumpolar Arctic Vegetation, Geobotanical, Physiographic Maps, 1982-2003",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Arctic_Vegetation_Maps_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1323",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1323",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Arctic_Vegetation_Maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Arctic_Vegetation_Maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Vegetation_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Vegetation_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1323",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1323",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -1481834,76 +1481807,75 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Vegetation_Maps_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Arctic_Vegetation_Maps_Fig1.png",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1323",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1323",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Arctic_Vegetation_Maps_Fig1.png",
+            "identifier": "C2170968604-ORNL_CLOUD",
+            "issued": "2018-12-31",
+            "keyword": [
+                "ecosystems",
+                "vegetation",
+                "topography",
+                "land surface",
+                "landscape",
+                "earth science",
+                "biosphere",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1323",
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
             "spatial": "-180.0 55.8 180.0 90.0",
+            "temporal": "1982-06-01T00:00:00Z/2010-09-30T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Circumpolar Arctic Vegetation, Geobotanical, Physiographic Maps, 1982-2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.lpi.usra.edu/resources/apollo/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1967-01-01/1972-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.lpi.usra.edu/resources/apollopanoramas/",
-                "http://www.lpi.usra.edu/resources/cla/",
-                "http://www.lpi.usra.edu/resources/lunarorbiter/",
-                "http://www.lpi.usra.edu/resources/lunar_orbiter/",
-                "http://www.lpi.usra.edu/resources/ranger/",
-                "http://planetarynames.wr.usgs.gov/"
-            ],
-            "keyword": [
-                "modeling",
-                "space science",
-                "imagery",
-                "mapping",
-                "circulation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Schenk",
                 "hasEmail": "mailto:rpif@lpi.usra.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000019__3",
             "description": "The Apollo Image Atlas is a comprehensive collection of Apollo-Saturn mission photography. Included are almost 25,000 lunar images, both from orbit and from the moon's surface, as well as photographs of the earth, astronauts and mission hardware.",
-            "title": "Apollo Image Atlas",
-            "programCode": [
-                "026:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1481911,1045 +1481883,1084 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "NASA-0000019__3",
+            "issued": "2018-06-25",
+            "keyword": [
+                "modeling",
+                "space science",
+                "imagery",
+                "mapping",
+                "circulation"
+            ],
+            "landingPage": "http://www.lpi.usra.edu/resources/apollo/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.lpi.usra.edu/resources/apollopanoramas/",
+                "http://www.lpi.usra.edu/resources/cla/",
+                "http://www.lpi.usra.edu/resources/lunarorbiter/",
+                "http://www.lpi.usra.edu/resources/lunar_orbiter/",
+                "http://www.lpi.usra.edu/resources/ranger/",
+                "http://planetarynames.wr.usgs.gov/"
+            ],
             "spatial": "Lunar",
-            "accrualPeriodicity": "irregular",
+            "temporal": "1967-01-01/1972-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Apollo Image Atlas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-3-NAV-9P-ENCOUNTER-V1.1",
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
-                "9p/tempel 1 (1867 g1)",
-                "deep impact"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated images of comet 9P/Tempel 1 acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation of the flyby spacecraft as well as for scientific investigations. These data were collected from 15 May to 4 July 2005. In this version (1.1) of the data set, the modified Julian date values, found in the PDS data labels of version 1.0, were replaced with full Julian dates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-3-nav-9p-encounter-v1.1_uqsf-tqpm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "9p/tempel 1 (1867 g1)",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-3-NAV-9P-ENCOUNTER-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-3-nav-9p-encounter-v1.1_uqsf-tqpm",
-            "description": "This data set contains calibrated images of comet 9P/Tempel 1 acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the encounter phase of the mission. These observations were used for optical and autonomous navigation of the flyby spacecraft as well as for scientific investigations. These data were collected from 15 May to 4 July 2005. In this version (1.1) of the data set, the modified Julian date values, found in the PDS data labels of version 1.0, were replaced with full Julian dates.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED MRI NAV IMGS V1.1",
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
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED MRI NAV IMGS V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MKJG22GUOD34",
             "citation": "Dan Goldberg at George Washington University. 2024-03-15. HAQ_TROPOMI_NO2_CONUS_M_L3. Version 2.4. HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Monthly Level 3 0.01 x 0.01 Degree Gridded Data V2.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MKJG22GUOD34. https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_CONUS_M_L3_2.4.html. Digital Science Data.",
-            "issued": "2024-01-26",
-            "temporal": "2018-05-01T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
-            "references": [
-                "https://doi.org/10.1029/2020EF001665"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Xiaohua Pan",
                 "hasEmail": "mailto:xiaohua.pan@nasa.gov"
             },
+            "creator": "Dan Goldberg at George Washington University",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2839237275-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product provides level 3 monthly averages of tropospheric Nitrogen dioxide (NO2) vertical column density derived from the level 2 Tropospheric Monitoring Instrument (TROPOMI) across the Continental United States oversampled to a spatial resolution of 0.01\u02da x 0.01\u02da (~1 km2) using a consistent algorithm from the European Space Agency (ESA) version 2.4 that can be used for trend analysis of air pollution. The dataset record began in May 2018 and continues to the present. \n\nThis L3 product was developed by the George Washington University Air, Climate and Health Laboratory as part of the NASA Health Air Quality Applied Science Team (HAQAST) using Level 2 version 2.4 TROPOMI NO2 files from the ESA. The TROPOMI instrument on Sentinel-5 Precursor acquires tropospheric NO2 column contents from low Earth orbit (~824 km above ground level) once per day globally at approximately 13:30 local time.\n\nNO2 is an air pollutant that adversely affects the human respiratory system and leads to premature mortality. NO2 is also an important precursor for ozone and fine particulates, which also have severe health impacts. In urban areas, the majority of NO2 originates from anthropogenic NOx (=NO+NO2; most NOx is emitted as NO, which rapidly cycles to NO2) emissions during high-temperature fossil fuel combustion. Tropospheric NO2 vertical column contents are qualitatively representative of near-surface NO2 concentrations and NOx emissions in urban/polluted locations.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HAQ_TROPOMI_NO2_CONUS_M_L3",
-            "creator": "Dan Goldberg at George Washington University",
-            "graphic-preview-description": "Sample image: The level 3 TROPOMI Tropospheric vertical column NO2 density for January 2023",
-            "title": "HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Monthly Level 3 0.01 x 0.01 Degree Gridded Data V2.4 (HAQ_TROPOMI_NO2_CONUS_M_L3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMKJG22GUOD34",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMKJG22GUOD34",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4.png",
-                    "description": "Sample image: The level 3 TROPOMI Tropospheric vertical column NO2 density for January 2023",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image: The level 3 TROPOMI Tropospheric vertical column NO2 density for January 2023",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4/doc/README_TROPOMI_Level3_TropNO2_DG_20240222.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4/doc/README_TROPOMI_Level3_TropNO2_DG_20240222.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_CONUS_M_L3_2.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_CONUS_M_L3_2.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQ_TROPOMI_NO2_CONUS_M_L3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQ_TROPOMI_NO2_CONUS_M_L3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4/contents.html",
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
+            "graphic-preview-description": "Sample image: The level 3 TROPOMI Tropospheric vertical column NO2 density for January 2023",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_CONUS_M_L3.2.4.png",
+            "identifier": "C2839237275-GES_DISC",
+            "issued": "2024-01-26",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/MKJG22GUOD34",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-29",
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
+            "series-name": "HAQ_TROPOMI_NO2_CONUS_M_L3",
             "spatial": "-124.75 24.5 -66.76 49.49",
+            "temporal": "2018-05-01T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "HAQAST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) CONUS Monthly Level 3 0.01 x 0.01 Degree Gridded Data V2.4 (HAQ_TROPOMI_NO2_CONUS_M_L3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0071-2-IRTF-MIR-TMPL1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Mid-IR images of Comet 9P/Tempel 1 were obtained at the NASA IRTF during the period from July 2-18, 2005 UT. These observations were taken as part of a campaign designed to support the science objectives of the Deep Impact spacecraft around the time of its encounter with Tempel 1. This data set contains all raw images, including those required for reduction and photometric calibration of the comet observations.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0071-2-irtf-mir-tmpl1-v1.0_uqtx-p8g8",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "68 leto",
                 "support archives",
                 "9p/tempel 1 (1867 g1)",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0071-2-IRTF-MIR-TMPL1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0071-2-irtf-mir-tmpl1-v1.0_uqtx-p8g8",
-            "description": "Mid-IR images of Comet 9P/Tempel 1 were obtained at the NASA IRTF during the period from July 2-18, 2005 UT. These observations were taken as part of a campaign designed to support the science objectives of the Deep Impact spacecraft around the time of its encounter with Tempel 1. This data set contains all raw images, including those required for reduction and photometric calibration of the comet observations.",
-            "title": "IRTF MID-IR IMAGING OF COMET 9P-TEMPEL 1 V1.0",
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
+            "title": "IRTF MID-IR IMAGING OF COMET 9P-TEMPEL 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M05-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-07-02 to 2014-08-01.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m05-v1.0_uqtx-usy5",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M05-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m05-v1.0_uqtx-usy5",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Wide Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-07-02 to 2014-08-01.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 005 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 3 RDR MTP 005 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-RVM1-MAG-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 3 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the RVM1 (Rendez-vous Manoeuvre 1) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-rvm1-mag-v1.0_uqtz-iema",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-RVM1-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-rvm1-mag-v1.0_uqtz-iema",
-            "description": "This archive contains level 3 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the RVM1 (Rendez-vous Manoeuvre 1) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 3 RVM1 MAG\n                            V1.0",
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
+            "title": "ROSETTA-LANDER CAL ROMAP 3 RVM1 MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-EXT1-67P-V3.0",
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
+            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA COMET EXTENSION 1 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes data sets with a lower version number. The updates include a new calibration algorithm and modified documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-ext1-67p-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-EXT1-67P-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-ext1-67p-v3.0",
-            "description": "This data set contains Spectroscopic and Continuum, level 3 data, in the form of table files, taken during the ROSETTA COMET EXTENSION 1 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.  It supercedes data sets with a lower version number. The updates include a new calibration algorithm and modified documentation.",
-            "title": "ROSETTA-ORBITER 67P MIRO 3 EXT1 V3.0",
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
+            "title": "ROSETTA-ORBITER 67P MIRO 3 EXT1 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL3DCOD.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2018), Terra/MISR Level 3, Cloud Top Height-Optical Depth Product covering a day, version 1, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/TERRA/MISR/MIL3DCOD.001",
-            "issued": "2018-08-06",
-            "temporal": "2000-03-01T00:00:00Z/2022-05-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-26",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Roger Marchand",
                 "hasEmail": "mailto:rojmarch@u.washington.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1644916756-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. This file contains the public MISR Level 3 Cloud Top Height-Optical Depth Product covering a day.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Cloud Top Height-Optical Depth Product covering a day V001",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL3DCOD.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL3DCOD.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C1644916756-LARC",
+            "issued": "2018-08-06",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL3DCOD.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-03-01T00:00:00Z/2022-05-03T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Cloud Top Height-Optical Depth Product covering a day V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-IMS-3-RDR-HIS-GRIGG-SKJELL-V1.0",
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
-                "giotto extended mission",
-                "26p/grigg-skjellerup 1 (1922 k1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set lists counts as a function of either angular position or energy level. The data were obtained from the Ion Mass Spectrometer (IMS) High Intensity Spectrometer (HIS) instrument flown aboard the GIOTTO spacecraft during its extended mission to fly by comet 26P/Grigg-Skjellerup. These data have not been formally reviewed by PDS.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-ims-3-rdr-his-grigg-skjell-v1.0_uqwc-9yd9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "giotto extended mission",
+                "26p/grigg-skjellerup 1 (1922 k1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-IMS-3-RDR-HIS-GRIGG-SKJELL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-ims-3-rdr-his-grigg-skjell-v1.0_uqwc-9yd9",
-            "description": "This data set lists counts as a function of either angular position or energy level. The data were obtained from the Ion Mass Spectrometer (IMS) High Intensity Spectrometer (HIS) instrument flown aboard the GIOTTO spacecraft during its extended mission to fly by comet 26P/Grigg-Skjellerup. These data have not been formally reviewed by PDS.",
-            "title": "IMS HIGH INTENSITY SPECTROMETER V1.0",
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
+            "title": "IMS HIGH INTENSITY SPECTROMETER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1739",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hasbrouck, T., T.J. Brinkman, G. Stout, K. Kielland, and E. Trochim. 2019. ABoVE: Environmental Conditions During Fall Moose Hunting Seasons, Alaska, 2000-2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1739",
-            "issued": "2020-02-06",
-            "temporal": "2000-01-01T00:00:00Z/2016-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "animal commodities",
-                "biospheric indicators",
-                "national geospatial data asset",
-                "agriculture",
-                "surface water",
-                "ngda",
-                "terrestrial hydrosphere",
-                "biological classification",
-                "atmospheric temperature",
-                "atmosphere",
-                "animals/vertebrates",
-                "animal science",
-                "climate indicators",
-                "human settlements",
-                "vegetation",
-                "human dimensions",
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
-            "identifier": "C2143402663-ORNL_CLOUD",
             "description": "This dataset provides daily and annual air temperature, river water level, and leaf drop dates coincident with the moose (Alces alces) hunting season (September) for the area surrounding the rural communities of Nulato, Koyukuk, Kaltag, Galena, Ruby, Huslia, and Hughes in interior Alaska, USA, over the period 2000-2016. The main objective of the study was to assess how the environmental conditions impacted the success of hunters who rely on moose as a subsistence resource.",
-            "graphic-preview-description": "Map of study area communities. GMUs are Game Management Units and GMU21D is highlighted. From Hasbrouck et al., 2019, in process.",
-            "title": "ABoVE: Environmental Conditions During Fall Moose Hunting Seasons, Alaska, 2000-2016",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Effect_Environment_Moose_fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1739",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1739",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Effect_Environment_Moose/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Effect_Environment_Moose/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Effect_Environment_Moose.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Effect_Environment_Moose.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1739",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1739",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Effect_Environment_Moose/comp/Effect_Environment_Moose.pdf",
-                    "description": "ABoVE: Leaf Drop, Water Levels and Temperature During Moose Hunting Season, 2000-2016: Effect_Environment_Moose.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Leaf Drop, Water Levels and Temperature During Moose Hunting Season, 2000-2016: Effect_Environment_Moose.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Effect_Environment_Moose/comp/Effect_Environment_Moose.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Effect_Environment_Moose_fig1.png",
-                    "description": "Map of study area communities. GMUs are Game Management Units and GMU21D is highlighted. From Hasbrouck et al., 2019, in process.",
                     "@type": "dcat:Distribution",
+                    "description": "Map of study area communities. GMUs are Game Management Units and GMU21D is highlighted. From Hasbrouck et al., 2019, in process.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Effect_Environment_Moose_fig1.png",
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
+            "graphic-preview-description": "Map of study area communities. GMUs are Game Management Units and GMU21D is highlighted. From Hasbrouck et al., 2019, in process.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Effect_Environment_Moose_fig1.png",
+            "identifier": "C2143402663-ORNL_CLOUD",
+            "issued": "2020-02-06",
+            "keyword": [
+                "biosphere",
+                "animal commodities",
+                "biospheric indicators",
+                "national geospatial data asset",
+                "agriculture",
+                "surface water",
+                "ngda",
+                "terrestrial hydrosphere",
+                "biological classification",
+                "atmospheric temperature",
+                "atmosphere",
+                "animals/vertebrates",
+                "animal science",
+                "climate indicators",
+                "human settlements",
+                "vegetation",
+                "human dimensions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1739",
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
             "spatial": "-158.53 64.55 -156.66 64.93",
+            "temporal": "2000-01-01T00:00:00Z/2016-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Environmental Conditions During Fall Moose Hunting Seasons, Alaska, 2000-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/SWYV7CLJV8AX",
             "citation": "NOAA NESDIS. 2022-08-22. VISSRGOES1IMVIS. Version 001. VISSR/GOES-1 Visible Imagery on 70mm Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/SWYV7CLJV8AX. https://disc.gsfc.nasa.gov/datacollection/VISSRGOES1IMVIS_001.html. Digital Science Data.",
-            "issued": "2018-03-16",
-            "temporal": "1976-01-27T00:00:00Z/1976-10-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-16",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NOAA NESDIS",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2386972514-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "VISSRGOES1IMVIS is the Visible Infrared Spin-Scan Radiometer (VISSR) Visible Imagery on 70mm Film data product from the first Geostationary Operational Environmental Satellite (GOES-1). This set of visible imagery (0.55 to 0.70 micrometer) was originally produced on commercial image-generation equipment from digital tapes and was made available on 70-mm film, from which they were later scanned to digital TIFF image files. Each TIFF scan contains 2 or 3 pictures, and there are several hundred scans from an original 70 mm film roll which are combined into a ZIP file. Each picture contains a title on the top boundary and a 33-level gray scale on the right boundary that represents brightness temperatures. It may have a combination of the following options: 1) contrast enhancement, 2) image sectorization, and 3) 1/16-size imagery. The maximum effective size covers 500 sq km, represented by 4000 by 3904 pixels. Each element has a maximum resolution of 3.7 km. The title contains the satellite identification, picture number, picture type, coordinate numbers of the top left pixel relative to the visible sensor, start time of sectorized image, and pixel scaling and sector size identification.\n\nThe GOES-1 satellite was parked over the equator at longitude 115W on Dec 18, 1975 viewing the hemisphere below the satellite. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00247 (old ID 75-100A-01B).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "VISSRGOES1IMVIS",
-            "creator": "NOAA NESDIS",
-            "title": "VISSR/GOES-1 Visible Imagery on 70mm Film V001 (VISSRGOES1IMVIS) at GES DISC",
-            "graphic-preview-description": "Typical GOES-1 VISSR visible 70mm film image.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES1IMVIS_001.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWYV7CLJV8AX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWYV7CLJV8AX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES1IMVIS_001.png",
-                    "description": "Typical GOES-1 VISSR visible 70mm film image.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical GOES-1 VISSR visible 70mm film image.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES1IMVIS_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRGOES1IMVIS_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRGOES1IMVIS_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES1IMVIS.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES1IMVIS.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRGOES1IMVIS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRGOES1IMVIS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES1IMVIS.001/doc/README.VISSRSMSGOESIM.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES1IMVIS.001/doc/README.VISSRSMSGOESIM.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/GOES_SMS_Users_Guide.pdf",
-                    "description": "The GOES/SMS User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "The GOES/SMS User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/GOES_SMS_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/VISSR_data_processing_plan.pdf",
-                    "description": "VISSR Data Processing Plan for SMS/GOES Satellites",
                     "@type": "dcat:Distribution",
+                    "description": "VISSR Data Processing Plan for SMS/GOES Satellites",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/VISSR_data_processing_plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Typical GOES-1 VISSR visible 70mm film image.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES1IMVIS_001.png",
+            "identifier": "C2386972514-GES_DISC",
+            "issued": "2018-03-16",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWYV7CLJV8AX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "VISSRGOES1IMVIS",
             "spatial": "155.0 -90.0 -25.0 90.0",
+            "temporal": "1976-01-27T00:00:00Z/1976-10-28T23:59:59.999Z",
             "theme": [
                 "GOES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VISSR/GOES-1 Visible Imagery on 70mm Film V001 (VISSRGOES1IMVIS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCIES-2-RVM1-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains EDITED RAW DATA of the Rosetta RPCIES instrument taken during the Rendezvous Manoeuvre 1 (RVM1). Included are the data taken between 29 Nov 2010 and 30 Nov 2010.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcies-2-rvm1-v1.0_uqxn-6pxx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar wind",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCIES-2-RVM1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcies-2-rvm1-v1.0_uqxn-6pxx",
-            "description": "This dataset contains EDITED RAW DATA of the Rosetta RPCIES instrument taken during the Rendezvous Manoeuvre 1 (RVM1). Included are the data taken between 29 Nov 2010 and 30 Nov 2010.",
-            "title": "ROSETTA-ORBITER SOLAR WIND RPCIES 2 RVM1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER SOLAR WIND RPCIES 2 RVM1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-NORMAL-OPS-V1.0",
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
-                "phoenix"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains normal data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-normal-ops-v1.0_uqyg-wna4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-NORMAL-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-normal-ops-v1.0_uqyg-wna4",
-            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains normal data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA \n                                     5 NORMAL OPS V1.0",
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
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA \n                                     5 NORMAL OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/ICEPOP/D3R/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chandrasekar, V. .2019. GPM Ground Validation Dual-frequency Dual-polarized Doppler Radar (D3R) ICE POP [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/ICEPOP/D3R/DATA101",
-            "issued": "2019-09-21",
-            "temporal": "2017-11-01T01:45:31Z/2018-03-17T18:46:16Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
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
-            "identifier": "C1983445363-GHRC_DAAC",
             "description": "The GPM Ground Validation Dual-frequency Dual-polarized Doppler Radar (D3R) ICE POP dataset includes reflectivity, differential reflectivity, copolar correlation coefficient, differential propagation phase, radial velocity, and spectrum width data collected by the Dual-frequency Dual-polarized Doppler Radar (D3R) during the International Collaborative Experiments for Pyeongchang 2018 Olympic and Paralympic Winter Games (ICE-POP) field campaign in South Korea. The two major objectives of ICE-POP were to study severe winter weather events in regions of complex terrain and improve the short-term forecasting of such events. These data contributed to Global Precipitation Measurement mission Ground Validation (GPM GV) campaign efforts to improve satellite estimates of orographic winter precipitation. The D3R was developed by a government-industry-academic consortium with funding from NASA's GPM Project. It operates at the ku (13.91 GHz \u00b1 25 MHz) and ka (35.56 GHz \u00b1 25 MHz) frequencies covering a fixed range from 450 m to 39.75 km. The D3R dataset files are available from November 1, 2017 through March 17, 2018 in netCDF-4 format.",
-            "title": "GPM Ground Validation Dual-frequency Dual-polarized Doppler Radar (D3R) ICE POP V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FICEPOP%2FD3R%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FICEPOP%2FD3R%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmd3ricepop",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmd3ricepop",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pmm.nasa.gov/ice-pop",
-                    "description": "PMM ICE-POP Field Campaign webpage",
                     "@type": "dcat:Distribution",
+                    "description": "PMM ICE-POP Field Campaign webpage",
+                    "downloadURL": "https://pmm.nasa.gov/ice-pop",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20180003615.pdf",
-                    "description": "NASA Participation in the International Collaborative Experiments for Pyeongchang 2018 Olympic and Paralympic Winter Games (ICE-POP 2018)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Participation in the International Collaborative Experiments for Pyeongchang 2018 Olympic and Paralympic Winter Games (ICE-POP 2018)",
+                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20180003615.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160013407.pdf",
-                    "description": "ICE-POP and the NASA Global Precipitation Measurement (GPM) Mission",
                     "@type": "dcat:Distribution",
+                    "description": "ICE-POP and the NASA Global Precipitation Measurement (GPM) Mission",
+                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160013407.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/public/pub/fieldCampaigns/gpmValidation/icepop/D3R/doc/gpmd3ricepop_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/public/pub/fieldCampaigns/gpmValidation/icepop/D3R/doc/gpmd3ricepop_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/icepop/D3R/doc/D3R_ICEPOP_dataset.docx",
-                    "description": "D3R ICE POP Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "D3R ICE POP Documentation",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/icepop/D3R/doc/D3R_ICEPOP_dataset.docx",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/IGARSS.2010.5649440",
-                    "description": "Scientific and engineering overview of the NASA Dual-Frequency DualPolarized Doppler Radar (D3R) system for GPM Ground Validation",
                     "@type": "dcat:Distribution",
+                    "description": "Scientific and engineering overview of the NASA Dual-Frequency DualPolarized Doppler Radar (D3R) system for GPM Ground Validation",
+                    "downloadURL": "https://doi.org/10.1109/IGARSS.2010.5649440",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/IGARSS.2010.5653929",
-                    "description": "Realization of the NASA Dual-Frequency Dual-Polarized Doppler Radar (D3R)",
                     "@type": "dcat:Distribution",
+                    "description": "Realization of the NASA Dual-Frequency Dual-Polarized Doppler Radar (D3R)",
+                    "downloadURL": "https://doi.org/10.1109/IGARSS.2010.5653929",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ieeexplore.ieee.org/abstract/document/7909473",
-                    "description": "Calibration Procedures for Global Precipitation-Measurement Ground-Validation Radars",
                     "@type": "dcat:Distribution",
+                    "description": "Calibration Procedures for Global Precipitation-Measurement Ground-Validation Radars",
+                    "downloadURL": "https://ieeexplore.ieee.org/abstract/document/7909473",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-14-00097.1",
-                    "description": "A semi-supervised robust hydrometeor classification method for dual-polarization radar applications",
                     "@type": "dcat:Distribution",
+                    "description": "A semi-supervised robust hydrometeor classification method for dual-polarization radar applications",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-14-00097.1",
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
+            "identifier": "C1983445363-GHRC_DAAC",
+            "issued": "2019-09-21",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/ICEPOP/D3R/DATA101",
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
             "spatial": "128.36 37.3181 129.078 38.0367",
+            "temporal": "2017-11-01T01:45:31Z/2018-03-17T18:46:16Z",
             "theme": [
                 "ICE POP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Dual-frequency Dual-polarized Doppler Radar (D3R) ICE POP V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YCLD_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Component Global Cloud Product covering a year's products;See ProductionDateTime for Published date.",
-            "issued": "2005-11-28",
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
-            "identifier": "C84942920-LARC",
             "description": "This file contains the public MISR Level 3 Component Global Cloud Product covering a year",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Component Global Cloud Product covering a year V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YCLD_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3YCLD_L3.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C84942920-LARC",
+            "issued": "2005-11-28",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3YCLD_L3.002",
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
+            "title": "MISR Level 3 Component Global Cloud Product covering a year V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-ESC3-MTP021-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the COMET ESCORT 3 MTP021 Phase from 23 Sep. 2015, 06:02:17 to 20 Oct. 2015, 23:02:19 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-esc3-mtp021-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "zeta cas",
                 "international rosetta mission",
                 "alpha lyr",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-ESC3-MTP021-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-esc3-mtp021-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the COMET ESCORT 3 MTP021 Phase from 23 Sep. 2015, 06:02:17 to 20 Oct. 2015, 23:02:19 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 COMET ESCORT 3 MTP021 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 COMET ESCORT 3 MTP021 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/ACTIVATE_Model_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-11-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/ACTIVATE_Model_Data_1.",
-            "issued": "2021-10-28",
-            "temporal": "2020-02-14T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-15",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "aerosols",
-                "earth science",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Armin Sorooshian",
                 "hasEmail": "mailto:armin@email.arizona.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2163554174-LARC_ASDC",
             "description": "ACTIVATE_Model_Data is the MERRA-2 variables sampled along the HU-25 flight tracks during the ACTIVATE project. ACTIVATE is a 5-year NASA Earth-Venture Sub-Orbital field campaign, with a target completion of December 2023. Data collection is still ongoing. \r\n\r\nMarine boundary layer clouds play a critical role in Earth\u2019s energy balance and water cycle. These clouds cover more than 45% of the ocean surface and exert a net cooling effect. The Aerosol Cloud meTeorology Interactions oVer the western Atlantic Experiment (ACTIVATE) project is a five-year project (January 2019-December 2023) that will provide important globally-relevant data about changes in marine boundary layer cloud systems, atmospheric aerosols and multiple feedbacks that warm or cool the climate. ACTIVATE studies the atmosphere over the western North Atlantic and samples its broad range of aerosol, cloud and meteorological conditions using two aircraft, the UC-12 King Air and HU-25 Falcon. The UC-12 King Air will primarily be used for remote sensing measurements while the HU-25 Falcon will contain a comprehensive instrument payload for detailed in-situ measurements of aerosol, cloud properties, and atmospheric state. A few trace gas measurements will also be onboard the HU-25 Falcon for the measurements of pollution traces, which will contribute to airmass classification analysis. A total of 150 coordinated flights over the western North Atlantic are planned through 6 deployments from 2020-2022. The ACTIVATE science observing strategy intensively targets the shallow cumulus cloud regime and aims to collect sufficient statistics over a broad range of aerosol and weather conditions which enables robust characterization of aerosol-cloud-meteorology interactions. This strategy is implemented by two nominal flight patterns: Statistical Survey and Process Study. The statistical survey pattern involves close coordination between the remote sensing and in-situ aircraft to conduct near coincident sampling at and below cloud base as well as above and within cloud top. The process study pattern involves extensive vertical profiling to characterize the target cloud and surrounding aerosol and meteorological conditions.",
-            "title": "ACTIVATE Supplementary Model Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
```

