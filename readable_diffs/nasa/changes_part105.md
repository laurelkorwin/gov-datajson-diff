# Change History for nasa.json (Part 105)

### Changes from 31606f9 to dd2190f (Part 94/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-111_jkwe-5qwa",
-            "description": "Microgravity exposure as well as chronic muscle disuse are two of the main causes of physiological adaptive skeletal muscle atrophy in humans and murine animals in physiological condition. The aim of this study was to investigate at both morphological and global gene expression level skeletal muscle adaptation to microgravity in mouse soleus and extensor digitorum longus (EDL). Adult male mice C57BL/N6 were flown aboard the BION-M1 biosatellite for 30 days on orbit (BF) or housed in a replicate flight habitat on Earth (BG) as reference flight control. In this study we investigated for the first time gene expression adaptation to 30 days of microgravity exposure in mouse soleus and EDL highlighting potential new targets for improvement of countermeasures able to ameliorate or even prevent microgravity-induced atrophy in future spaceflights. Overall Design: C57BL/N6 mice were randomly divided in 3 groups: Bion Flown (BF) mice flown aboard the Bion M1 biosatellite in microgravity environment for 30 days; Bion Ground (BG) mice housed in the same habitat of flown animals but exposed to earth gravity; and Flight Control (FC) mice housed in a standard animal facility.",
-            "title": "Global gene expression analysis highlights microgravity sensitive key genes in soleus and EDL of 30 days space flown mice",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-111",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Global gene expression analysis highlights microgravity sensitive key genes in soleus and EDL of 30 days space flown mice"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Global gene expression analysis highlights microgravity sensitive key genes in soleus and EDL of 30 days space flown mice"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/910/",
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
-            "identifier": "DASHLINK_910",
             "description": "Ballscrew jam fault datasets (diagnostic and prognostic)",
-            "title": "2010_09_05 Lab",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_05_2.zip",
-                    "description": "2010_09_05.zip",
                     "@type": "dcat:Distribution",
+                    "description": "2010_09_05.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_05_2.zip",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "2010_09_05.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_910",
+            "issued": "2014-07-02",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/910/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "2010_09_05 Lab"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://aeronet.gsfc.nasa.gov/cgi-bin/combined_data_access_new",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://aeronet.gsfc.nasa.gov/new_web/data_usage.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "description": "The aerosol optical depth processing includes the spectral de-convolution algorithm (SDA) described in O'Neill et al. (2003). This algorithm yields fine (sub-micron) and coarse (super-micron) aerosol optical depths at a standard wavelength of 500 nm (from which FMF*, the fraction of fine mode to total aerosol optical depth can be computed).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/AOT_Level2_All_Points.tar.gz",
+                    "mediaType": "application/x-tar"
+                }
             ],
+            "identifier": "NASA-0000008",
+            "issued": "2018-06-25",
             "keyword": [
                 "precipitable water",
                 "satellite",
@@ -983659,151 +983668,117 @@
                 "earth science",
                 "clouds"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brent Holben",
-                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
-            },
+            "landingPage": "http://aeronet.gsfc.nasa.gov/cgi-bin/combined_data_access_new",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000008",
-            "description": "The aerosol optical depth processing includes the spectral de-convolution algorithm (SDA) described in O'Neill et al. (2003). This algorithm yields fine (sub-micron) and coarse (super-micron) aerosol optical depths at a standard wavelength of 500 nm (from which FMF*, the fraction of fine mode to total aerosol optical depth can be computed).",
-            "title": "AERONET Level 2.0 AOD",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/AOT_Level2_All_Points.tar.gz",
-                    "mediaType": "application/x-tar"
-                }
+            "references": [
+                "http://aeronet.gsfc.nasa.gov/new_web/data_usage.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "AERONET Level 2.0 AOD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-3-CR5-V1.0",
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
-                "calibration",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 5 mission phase, which took place between 2009-12-14 and 2010-06-06, and includes Payload Checkout #12.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-3-cr5-v1.0_jm3f-7qps",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-ALICE-3-CR5-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-alice-3-cr5-v1.0_jm3f-7qps",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Cruise 5 mission phase, which took place between 2009-12-14 and 2010-06-06, and includes Payload Checkout #12.",
-            "title": "ROSETTA-ORBITER CAL ALICE 3 CR5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL ALICE 3 CR5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCICA-2-EAR1-RAW-V1.0",
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
-                "earth",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RAW DATA from the RPCICA instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcica-2-ear1-raw-v1.0_jm6n-k6qq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCICA-2-EAR1-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcica-2-ear1-raw-v1.0_jm6n-k6qq",
-            "description": "This dataset contains RAW DATA from the RPCICA instrument.",
-            "title": "ROSETTA-ORBITER EARTH RPCICA 2 EAR1 UNCALIBRATED V1.0",
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
+            "title": "ROSETTA-ORBITER EARTH RPCICA 2 EAR1 UNCALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-kb39wni",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2021-07-05. S5P_L1B_RA_BD7_HiR. Version 2. Sentinel-5P TROPOMI L1B Radiance product band 7 (SWIR detector) 5.5km x 7km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-kb39wni. https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD7_HiR_2.html. Digital Science Data.",
-            "issued": "2014-12-09",
-            "temporal": "2021-07-01T19:06:28Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-09",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "earth science",
-                "platform characteristics",
-                "spectral/engineering",
-                "sensor characteristics"
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
-            "identifier": "C2086595497-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L1B_RA_BD7_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L1B_RA_BD7_HiR",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Radiance product band 7 (SWIR detector) L1B 5.5km x 7km V2 (S5P_L1B_RA_BD7_HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_RA_BD7_HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L1B_RA_BD7_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm).\nTROPOMI Level-1B (L1B) product is generated by the Koninklijk Nederlands Meteoroligisch Instituut (KNMI) TROPOMI L01B processor from Level-0 input data and auxiliary data products with the netCDF-4 enhanced model. It provides users with radiance, irradiance, calibration and engineering products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-kb39wni",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-kb39wni",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -983813,993 +983788,1000 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD7_HiR_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L1B_RA_BD7_HiR_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD7_HiR.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD7_HiR.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD7_HiR.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level1B/S5P_L1B_RA_BD7_HiR.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-Level-1B-ATBD",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-Level-1B-ATBD",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3119978/Sentinel-5P-Level-01B-input-output-data-specification",
-                    "description": "Data Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Specification Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3119978/Sentinel-5P-Level-01B-input-output-data-specification",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_RA_BD7_HiR_2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L1B_RA_BD7_HiR_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Level-1b-Product-Readme-File",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Level-1b-Product-Readme-File",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/web/sentinel/missions/sentinel-5p",
-                    "description": "ESA Copernicus Sentinal 5P Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ESA Copernicus Sentinal 5P Home Page",
+                    "downloadURL": "https://sentinel.esa.int/web/sentinel/missions/sentinel-5p",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/glossary?title=Sentinel-5P",
-                    "description": "S5P TROPOMI Data Collection Summary",
                     "@type": "dcat:Distribution",
+                    "description": "S5P TROPOMI Data Collection Summary",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/glossary?title=Sentinel-5P",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L1B_RA_BD7_HiR_1.png",
+            "identifier": "C2086595497-GES_DISC",
+            "issued": "2014-12-09",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science",
+                "platform characteristics",
+                "spectral/engineering",
+                "sensor characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5270/S5P-kb39wni",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-12-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "S5P_L1B_RA_BD7_HiR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-07-01T19:06:28Z/2023-02-28T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Radiance product band 7 (SWIR detector) L1B 5.5km x 7km V2 (S5P_L1B_RA_BD7_HiR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-08-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_TraceGas_AircraftInSitu_DC8_Data_1.",
-            "issued": "1997-10-07",
-            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-11-12",
-            "keyword": [
-                "ocean chemistry",
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "earth science",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Donald Blake",
                 "hasEmail": "mailto:drblake@uci.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2662395889-LARC_ASDC",
             "description": "SONEX_TraceGas_AircraftInSitu_DC8_Data_1 is the in-situ trace gas data collected onboard the DC-8 aircraft during the SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) suborbital campaign. Data was collected from a variety of in-situ instrumentation, including the Whole Air Sampler (WAS), ATHOS, FASTOZ, University of Rhode Island Chemistry Instrument, chemiluminescence, DACOM, LICOR, PANAK, CIMS and SAGA. Data collection for this product is complete.\r\n\r\nThe SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) was an international, multi-organizational mission that took place in October-November 1997. NASA was the US sponsor of SONEX that partnered with POLINAT-2 (Pollution from Aircraft Emissions in the North Atlantic Flight Corridor) funded by the German DLR (Deutsches Zentrum f\u00fcr Luft- und Raumfahrt) or German Aerospace Agency. NASA flew the DC-8 aircraft out of NASA/Ames Research Center. DLR operated an instrumented Falcon 20 aircraft. The staging locations for NAFC sampling were primarily Bangor, Maine (US), and Shannon, Ireland. Subsonic aircraft emissions impact several aspects of atmospheric composition: nitrogen oxides (NOx), CO, and hydrocarbons from emissions can perturb upper tropospheric/lower stratospheric (UT/LS) ozone; water vapor, soot, and sulfur oxides (SOx) emitted by aircraft may perturb clouds and aerosols, changing UT/LS radiative forcing and global temperature.\r\nIn SONEX and POLINAT, flights were conducted in the vicinity of the North Atlantic Flight Coordinator (NAFC) to observe the impact of aircraft emissions on NOx and ozone (O3). The DC-8 aircraft payload (Singh et al., 1999) primarily measured in-situ CO, CO2, hydrocarbons/halocarbons, O3, aerosols (Dibb et al., 2000), OH/HO2, water vapor, nitric acid (Talbot et al., 1999), photolysis rates, temperature, pressure, winds, NOx, and NOy.\r\nThree sampling approaches were implemented during SONEX. First, special meteorological (Fuelberg et al., 2000) were developed to allow targeted sampling for air parcels affected by aircraft emissions and various meteorological events, e.g., convection, lightning (Jeker et al., 2000), stratospheric intrusions (Cho et al., 2000). Second, because the NAFC had not been extensively sampled in the past, it was important for SONEX to characterize the climatology of trace species like CN (Wang et al., 2000), NOx and NOy (Koike et al., 2000). Third, tracers (Simpson et al., 2000; Thompson et al., 1999) and model sensitivity studies (Meijer et al., 2000) were employed for Air Mass Identification. This sampling strategy answered the following questions: Where and when are air masses found with the greatest aircraft influence? When and where was stratospheric air sampled? SONEX showed a substantial impact of aircraft emissions on UT/LS NOx and CN in the vicinity of fresh aircraft emissions. However, during October-November 1997 over the NAFC, UT/LS NOx was dominated by surface emissions redistributed by convection and augmented by lightning.",
-            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) DC-8 In-Situ Trace Gas Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_TraceGas_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_TraceGas_AircraftInSitu_DC8_Data_1",
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
-                    "downloadURL": "https://doi.org/10.1029/1999GL900588",
-                    "description": "SONEX airborne mission and coordinated POLINAT-2 activity: Overview and accomplishments",
                     "@type": "dcat:Distribution",
+                    "description": "SONEX airborne mission and coordinated POLINAT-2 activity: Overview and accomplishments",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900588",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900424",
-                    "description": "Composition and distribution of aerosols over the North Atlantic during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX)",
                     "@type": "dcat:Distribution",
+                    "description": "Composition and distribution of aerosols over the North Atlantic during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX)",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900424",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL900589",
-                    "description": "Reactive nitrogen budget during the NASA SONEX Mission",
                     "@type": "dcat:Distribution",
+                    "description": "Reactive nitrogen budget during the NASA SONEX Mission",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900589",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900917",
-                    "description": "A meteorological overview of the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX) period",
                     "@type": "dcat:Distribution",
+                    "description": "A meteorological overview of the Subsonic Assessment Ozone and Nitrogen Oxide Experiment (SONEX) period",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900917",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901053",
-                    "description": "Measurements of nitrogen oxides at the tropopause: Attribution to convection and correlation with lightning",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of nitrogen oxides at the tropopause: Attribution to convection and correlation with lightning",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901053",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900430",
-                    "description": "Observations of convective and dynamical instabilities in tropopause folds and their contribution to stratosphere-troposphere exchange",
                     "@type": "dcat:Distribution",
+                    "description": "Observations of convective and dynamical instabilities in tropopause folds and their contribution to stratosphere-troposphere exchange",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900430",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL010930",
-                    "description": "Evidence of convection as a major source of condensation nuclei in the northern midlatitude upper troposphere",
                     "@type": "dcat:Distribution",
+                    "description": "Evidence of convection as a major source of condensation nuclei in the northern midlatitude upper troposphere",
+                    "downloadURL": "https://doi.org/10.1029/1999GL010930",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901013",
-                    "description": "Impact of aircraft emissions on reactive nitrogen over the North Atlantic Flight Corridor region",
                     "@type": "dcat:Distribution",
+                    "description": "Impact of aircraft emissions on reactive nitrogen over the North Atlantic Flight Corridor region",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901013",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD900750",
-                    "description": "Nonmethane hydrocarbon measurements in the North Atlantic Flight Corridor during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment",
                     "@type": "dcat:Distribution",
+                    "description": "Nonmethane hydrocarbon measurements in the North Atlantic Flight Corridor during the Subsonic Assessment Ozone and Nitrogen Oxide Experiment",
+                    "downloadURL": "https://doi.org/10.1029/1999JD900750",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL900581",
-                    "description": "Perspectives on NO, NOy, and fine aerosol sources and variability during SONEX",
                     "@type": "dcat:Distribution",
+                    "description": "Perspectives on NO, NOy, and fine aerosol sources and variability during SONEX",
+                    "downloadURL": "https://doi.org/10.1029/1999GL900581",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999JD901052",
-                    "description": "Model calculations of the impact of NOx from air traffic, lightning, and surface emissions, compared with measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Model calculations of the impact of NOx from air traffic, lightning, and surface emissions, compared with measurements",
+                    "downloadURL": "https://doi.org/10.1029/1999JD901052",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/content/Ames_Format_Overview",
-                    "description": "Ames File Format Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Ames File Format Overview",
+                    "downloadURL": "https://espo.nasa.gov/content/Ames_Format_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2662395889-LARC_ASDC",
-                    "description": "Earthdata Search client for SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2662395889-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI for SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/TraceGas_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/TraceGas_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2662395889-LARC_ASDC",
+            "issued": "1997-10-07",
+            "keyword": [
+                "ocean chemistry",
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_TraceGas_AircraftInSitu_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1997-11-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.89 -180.0 19.89 148.167 69.127 148.167 69.127 -180.0 19.89 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
             "theme": [
                 "SONEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) DC-8 In-Situ Trace Gas Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PTKXKSE28XYN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Aquarius L3 Gridded 1-Degree Daily Soil Moisture V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/PTKXKSE28XYN.",
-            "issued": "2011-08-25",
-            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-06-07",
-            "keyword": [
-                "land surface",
-                "soils",
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
-            "identifier": "C1529467467-NSIDC_ECS",
             "description": "This data set contains Level-3 gridded daily global soil moisture estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "Aquarius L3 Gridded 1-Degree Daily Soil Moisture V005",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?p=geographic&l=BlueMarble_NextGeneration,Aquarius_Soil_Moisture_Daily,Coastlines&t=2011-08-25",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPTKXKSE28XYN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPTKXKSE28XYN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AQUARIUS/AQ3_DYSM.005/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AQUARIUS/AQ3_DYSM.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_DYSM",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_DYSM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AQ3_DYSM/versions/5/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AQ3_DYSM/versions/5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AQUARIUS/AQ3_DYSM.005/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AQUARIUS/AQ3_DYSM.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_DYSM",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_DYSM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AQ3_DYSM/versions/5/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AQ3_DYSM/versions/5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?p=geographic&l=BlueMarble_NextGeneration%2CAquarius_Soil_Moisture_Daily%2CCoastlines&t=2011-08-25",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?p=geographic&l=BlueMarble_NextGeneration%2CAquarius_Soil_Moisture_Daily%2CCoastlines&t=2011-08-25",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PTKXKSE28XYN",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/PTKXKSE28XYN",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PTKXKSE28XYN",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/PTKXKSE28XYN",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?p=geographic&l=BlueMarble_NextGeneration,Aquarius_Soil_Moisture_Daily,Coastlines&t=2011-08-25",
+            "identifier": "C1529467467-NSIDC_ECS",
+            "issued": "2011-08-25",
+            "keyword": [
+                "land surface",
+                "soils",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/PTKXKSE28XYN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T00:00:00Z/2015-06-07T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius L3 Gridded 1-Degree Daily Soil Moisture V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ZXTJ28TQR1TR",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2T3NVMST. Version 5.12.4. MERRA-2 tavg3_3d_mst_Nv: 3d,3-Hourly,Time-Averaged,Model-Level,Assimilation,Moist Processes Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ZXTJ28TQR1TR. https://disc.gsfc.nasa.gov/datacollection/M2T3NVMST_5.12.4.html. Digital Science Data.",
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
-                "precipitation",
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812927-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2T3NVMST (or tavg3_3d_mst_Nv) is a 3-dimensional 3-hourly time averaged data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilated moist processes diagnostics at 72 model layers, such as convective rainwater source, large scale rainwater source, evap subl of convective precipitation, and evap subl of non convective precipitation.  The data field is available every three hour starting from  01:30 UTC, e.g.: 01:30, 04:30, \u2026 , 22:30 UTC. Section 4.2 of the MERRA-2 File Specification document provides pressure values nominal for a 1000 hPa surface pressure and refers to the top edge of the layer. The lev=1 is for the top layer, and lev=72 is for the bottom (or surface) model layer. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2T3NVMST",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2T3NVMST variable",
-            "title": "MERRA-2 tavg3_3d_mst_Nv: 3d,3-Hourly,Time-Averaged,Model-Level,Assimilation,Moist Processes Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NVMST) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NVMST_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZXTJ28TQR1TR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FZXTJ28TQR1TR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NVMST_5.12.4.png",
-                    "description": "M2T3NVMST variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2T3NVMST variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NVMST_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T3NVMST_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T3NVMST_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NVMST.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NVMST.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T3NVMST",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T3NVMST",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2T3NVMST.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/dods/M2T3NVMST.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T3NVMST.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T3NVMST.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T3NVMST.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T3NVMST.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NVMST.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T3NVMST.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2T3NVMST variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T3NVMST_5.12.4.png",
+            "identifier": "C1276812927-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/ZXTJ28TQR1TR",
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
+            "series-name": "M2T3NVMST",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavg3_3d_mst_Nv: 3d,3-Hourly,Time-Averaged,Model-Level,Assimilation,Moist Processes Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T3NVMST) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-0-ACCEL_DATA-V1.0",
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
-                "mars global surveyor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "All level zero accelerometer data are packaged by periapsis number for each aerobraking orbit. Each orbit is identified by a folder with name Pyyyy where 'yyyy' is the four digit periapsis number. Level 0 z-axis accelerometer data are provided every 0.1 seconds during an interval of time that generally assures that the initial and final data points are taken at least 200 km above the surface of Mars. Additional data, required to reduce accelerometer counts to acceleration on the spacecraft, are provided at lower sampling rates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-0-accel_data-v1.0_jmbe-6etx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-0-ACCEL_DATA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-0-accel_data-v1.0_jmbe-6etx",
-            "description": "All level zero accelerometer data are packaged by periapsis number for each aerobraking orbit. Each orbit is identified by a folder with name Pyyyy where 'yyyy' is the four digit periapsis number. Level 0 z-axis accelerometer data are provided every 0.1 seconds during an interval of time that generally assures that the initial and final data points are taken at least 200 km above the surface of Mars. Additional data, required to reduce accelerometer counts to acceleration on the spacecraft, are provided at lower sampling rates.",
-            "title": "MGS ACCELEROMETER RAW DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS ACCELEROMETER RAW DATA RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GSACB044M4PK",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High Mountain Asia 8-meter DEMs Derived from Along-track Optical Imagery V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/GSACB044M4PK.",
-            "issued": "2002-01-28",
-            "temporal": "2002-01-28T00:00:00Z/2016-11-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-11-17",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "topography"
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
-            "identifier": "C1442092309-NSIDC_ECS",
             "description": "This data set contains 8-meter Digital Elevation Models (DEMs) of high mountain Asia glacier and snow regions generated from very-high-resolution commercial stereoscopic satellite imagery.",
-            "title": "High Mountain Asia 8-meter DEMs Derived from Along-track Optical Imagery V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGSACB044M4PK",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGSACB044M4PK",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DEM8m_AT.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DEM8m_AT.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1442092309-NSIDC_ECS&m=15.561309814453127%2189.3507080078125%213%211%210%210%2C2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1442092309-NSIDC_ECS&m=15.561309814453127%2189.3507080078125%213%211%210%210%2C2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DEM8m_AT/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DEM8m_AT/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DEM8m_AT.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/HMA/HMA_DEM8m_AT.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1442092309-NSIDC_ECS&m=15.561309814453127%2189.3507080078125%213%211%210%210%2C2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1442092309-NSIDC_ECS&m=15.561309814453127%2189.3507080078125%213%211%210%210%2C2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DEM8m_AT/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/HMA_DEM8m_AT/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GSACB044M4PK",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/GSACB044M4PK",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GSACB044M4PK",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/GSACB044M4PK",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1442092309-NSIDC_ECS",
+            "issued": "2002-01-28",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/GSACB044M4PK",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-11-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "67.0 26.0 103.0 46.0",
+            "temporal": "2002-01-28T00:00:00Z/2016-11-24T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High Mountain Asia 8-meter DEMs Derived from Along-track Optical Imagery V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/701",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Batjes, N.H. 2003. LBA Regional Derived Soil Properties, 0.5-Deg (ISRIC-WISE). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/701",
-            "issued": "2023-10-03",
-            "temporal": "1950-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-07",
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
-            "identifier": "C2777329835-ORNL_CLOUD",
             "description": "The data set consists of a subset of the ISRIC-WISE global data set of derived soil properties for the study area of the Large Scale Biosphere-Atmosphere Experiment in Amazonia (LBA) in South America (i.e., longitude 85 to 30 degrees W, latitude 25 degrees S to 10 degrees N). More information about LBA and links to other LBA project sites can be found at http://www.daac.ornl.gov/LBA/misc_amazon.html.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA Regional Derived Soil Properties, 0.5-Deg (ISRIC-WISE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/701_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F701",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F701",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/lba_isric_wise/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/lba_isric_wise/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_isric.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_isric.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/701",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/701",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/lba_isric_wise/comp/ISRIC-WISE_README_LBA.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/lba_isric_wise/comp/ISRIC-WISE_README_LBA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/701_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/701_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=701",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=701",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/701_1_fit.png",
+            "identifier": "C2777329835-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/701",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-85.0 -25.0 -30.0 10.0",
+            "temporal": "1950-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA Regional Derived Soil Properties, 0.5-Deg (ISRIC-WISE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1816",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jones, C., M. Simard, Y. Lou, and T. Oliver. 2021. Pre-Delta-X: L1 UAVSAR Single Look Complex and Interferograms, MRD, LA, USA, 2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1816",
-            "issued": "2021-07-23",
-            "temporal": "2016-10-16T14:08:00Z/2016-10-17T21:55:23Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "oceans",
-                "biosphere",
-                "coastal processes",
-                "earth science",
-                "ecosystems",
-                "geomorphic landforms/processes",
-                "topography",
-                "terrestrial hydrosphere",
-                "surface water",
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
-            "identifier": "C2025125085-ORNL_CLOUD",
             "description": "This Level 1 (L1) dataset includes single look complex (SLC) stack products and co-registered interferograms in the HH (horizontal transmit and horizontal receive) polarization for the Atchafalaya Basin, in Southern Louisiana, USA, within the Mississippi River Delta (MRD) floodplain. The data were collected in October 2016 by Uninhabited Aerial Vehicle Synthetic Aperture Radar (UAVSAR), a polarimetric L-band synthetic aperture radar flown on the NASA Gulfstream-III aircraft as part of the Pre-Delta-X campaign. A single study region, flight line \"gulfco_12011\", was sampled six times at approximately 30-minute intervals to monitor changing water levels. The SLC stack product is a standard UAVSAR product delivered by the UAVSAR processing team. The L1 interferograms were generated from the SLC stacks.",
-            "graphic-preview-description": "Region sampled by UAVSAR on flight line \"gulfco_12011\" on October 16, 2016, in coastal Louisiana. This flight line was sampled six times at approximately 30-minute intervals.",
-            "title": "Pre-Delta-X: L1 UAVSAR Single Look Complex and Interferograms, MRD, LA, USA, 2016",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_SLC_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1816",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1816",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/deltax/PreDeltaX_UAVSAR_SLC/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/deltax/PreDeltaX_UAVSAR_SLC/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_SLC.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_SLC.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1816",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1816",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/PreDeltaX_UAVSAR_SLC/comp/PreDeltaX_UAVSAR_SLC.pdf",
-                    "description": "Pre-Delta-X: L1 UAVSAR Single Look Complex and Interferograms, MRD, LA, USA, 2016: PreDeltaX_UAVSAR_SLC.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Pre-Delta-X: L1 UAVSAR Single Look Complex and Interferograms, MRD, LA, USA, 2016: PreDeltaX_UAVSAR_SLC.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/PreDeltaX_UAVSAR_SLC/comp/PreDeltaX_UAVSAR_SLC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_SLC_Fig1.jpg",
-                    "description": "Region sampled by UAVSAR on flight line \"gulfco_12011\" on October 16, 2016, in coastal Louisiana. This flight line was sampled six times at approximately 30-minute intervals.",
                     "@type": "dcat:Distribution",
+                    "description": "Region sampled by UAVSAR on flight line \"gulfco_12011\" on October 16, 2016, in coastal Louisiana. This flight line was sampled six times at approximately 30-minute intervals.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_SLC_Fig1.jpg",
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
+            "graphic-preview-description": "Region sampled by UAVSAR on flight line \"gulfco_12011\" on October 16, 2016, in coastal Louisiana. This flight line was sampled six times at approximately 30-minute intervals.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/PreDeltaX_UAVSAR_SLC_Fig1.jpg",
+            "identifier": "C2025125085-ORNL_CLOUD",
+            "issued": "2021-07-23",
+            "keyword": [
+                "oceans",
+                "biosphere",
+                "coastal processes",
+                "earth science",
+                "ecosystems",
+                "geomorphic landforms/processes",
+                "topography",
+                "terrestrial hydrosphere",
+                "surface water",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1816",
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
             "spatial": "-91.62 29.36 -91.06 29.76",
+            "temporal": "2016-10-16T14:08:00Z/2016-10-17T21:55:23Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-Delta-X: L1 UAVSAR Single Look Complex and Interferograms, MRD, LA, USA, 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-ALTITUDE-V1.0",
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
-                "mars global surveyor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-altitude-v1.0_jmf4-bmez",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-ALTITUDE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-altitude-v1.0_jmf4-bmez",
-            "description": "not applicable",
-            "title": "MGS ALTITUDE DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MGS ALTITUDE DATA RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1234-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-04T01:50:40.000 to 2015-12-04T07:06:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1234-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1234-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1234-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-04T01:50:40.000 to 2015-12-04T07:06:57.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1234 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1234 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-RSS-5-GRAVITY-V1.0",
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
-                "lunar prospector",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The gravitational signature of the Moon was determined from velocity perturbations of the Lunar Prospector (LP) spacecraft as measured from the Doppler shift of the S-band radio tracking signal. LP was tracked by NASA's Deep Space Network (DSN) at Goldstone, California, Canberra, Australia, and Madrid, Spain. The tracking data were used to determine the LP orbit about the Moon, as well as the lunar gravity field [KONOPLIVETAL1998].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-rss-5-gravity-v1.0_jmix-vt56",
+            "issued": "2018-06-26",
+            "keyword": [
+                "lunar prospector",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-RSS-5-GRAVITY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-rss-5-gravity-v1.0_jmix-vt56",
-            "description": "The gravitational signature of the Moon was determined from velocity perturbations of the Lunar Prospector (LP) spacecraft as measured from the Doppler shift of the S-band radio tracking signal. LP was tracked by NASA's Deep Space Network (DSN) at Goldstone, California, Canberra, Australia, and Madrid, Spain. The tracking data were used to determine the LP orbit about the Moon, as well as the lunar gravity field [KONOPLIVETAL1998].",
-            "title": "LP LUNAR GRAVITY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LP LUNAR GRAVITY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jmjm-zwey",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "space science",
-                "wise",
-                "nen",
-                "geography"
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
-            "identifier": "NASA-0000038__39",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -984807,178 +984789,208 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__39",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "wise",
+                "nen",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jmjm-zwey",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1324-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-09T05:00:20.000 to 2016-01-09T09:24:55.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1324-v1.0_jms8-t8b7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1324-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1324-v1.0_jms8-t8b7",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-09T05:00:20.000 to 2016-01-09T09:24:55.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1324 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1324 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1223",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yang, X., W.M. Post, P.E. Thornton, and A.K. Jain. 2014. Global Gridded Soil Phosphorus Distribution Maps at 0.5-degree Resolution. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1223",
-            "issued": "2022-02-12",
-            "temporal": "1850-01-01T00:00:00Z/1850-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
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
-            "identifier": "C2216863372-ORNL_CLOUD",
             "description": "This data set provides estimates of different forms of naturally occurring soil phosphorus (P) including labile inorganic P, organic P, occluded P, secondary mineral P, apatite P, and total P on a global scale at 0.5-degree resolution. The data were assembled from chronosequence information and global spatial databases to develop a map of total soil P and the distribution among mineral bound, labile, organic, occluded, and secondary P forms in soils. Uncertainty was calculated for the different forms. The data set has no explicit temporal component -- data were nominally for the pre-industrial period ca. 1850.The estimated global spatial variation and distribution of different soil P forms presented in this study will be useful for global biogeochemistry models that include P as a limiting element in biological production by providing initial estimates of the available soil P for plant uptake and microbial utilization (Yang et al., 2013).There is one netCDF data file (.nc) with this data set.",
-            "graphic-preview-description": "Map of total global soil Phosphorus distribution.",
-            "title": "Global Gridded Soil Phosphorus Distribution Maps at 0.5-degree Resolution",
-            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/global_P_total.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1223",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1223",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_soil/Global_Phosphorus_Dist_Map/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_soil/Global_Phosphorus_Dist_Map/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Global_Phosphorus_Dist_Map.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/Global_Phosphorus_Dist_Map.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1223",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1223",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_Phosphorus_Dist_Map/comp/Global_Phosphorus_Dist_Map.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/Global_Phosphorus_Dist_Map/comp/Global_Phosphorus_Dist_Map.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/global_P_total.png",
-                    "description": "Map of total global soil Phosphorus distribution.",
                     "@type": "dcat:Distribution",
+                    "description": "Map of total global soil Phosphorus distribution.",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/global_P_total.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Map of total global soil Phosphorus distribution.",
+            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/global_P_total.png",
+            "identifier": "C2216863372-ORNL_CLOUD",
+            "issued": "2022-02-12",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1223",
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
+            "temporal": "1850-01-01T00:00:00Z/1850-12-31T23:59:59Z",
             "theme": [
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Gridded Soil Phosphorus Distribution Maps at 0.5-degree Resolution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1307-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-02T19:23:15.000 to 2016-01-02T21:15:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1307-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1307-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1307-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-02T19:23:15.000 to 2016-01-02T21:15:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1307 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1307 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/nasa/CrisisMappingToolkit",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CMT Team",
+                "hasEmail": "mailto:arc-sra-team@mail.nasa.gov"
+            },
+            "description": "The Crisis Mapping Toolkit (CMT) is a collection of tools for processing geospatial data (images, satellite data, etc.) into cartographic products that improve understanding of large-scale crises, such as natural disasters. The cartographic products produced by CMT include flood inundation maps, maps of damaged or destroyed structures, forest fire maps, population density estimates, etc. CMT is designed to rapidly process large-scale data using Google Earth Engine and other geospatial data systems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://github.com/nasa/CrisisMappingToolkit/archive/master.zip",
+                    "mediaType": "application/x-zip"
+                }
+            ],
+            "identifier": "OCIO-Fitara-116",
             "issued": "2015-07-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "geospatial data systems",
                 "code ti",
@@ -984988,75 +985000,41 @@
                 "cmt",
                 "map"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CMT Team",
-                "hasEmail": "mailto:arc-sra-team@mail.nasa.gov"
-            },
+            "landingPage": "https://github.com/nasa/CrisisMappingToolkit",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Ames Research Center"
             },
-            "identifier": "OCIO-Fitara-116",
-            "description": "The Crisis Mapping Toolkit (CMT) is a collection of tools for processing geospatial data (images, satellite data, etc.) into cartographic products that improve understanding of large-scale crises, such as natural disasters. The cartographic products produced by CMT include flood inundation maps, maps of damaged or destroyed structures, forest fire maps, population density estimates, etc. CMT is designed to rapidly process large-scale data using Google Earth Engine and other geospatial data systems.",
-            "title": "ARC Code TI: Crisis Mapping Toolkit",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://github.com/nasa/CrisisMappingToolkit/archive/master.zip",
-                    "mediaType": "application/x-zip"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "ARC Code TI: Crisis Mapping Toolkit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/DMSPF18/SSMIS/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chris Kidd. PRECIP_SSMIS_F18. Version 1. NASA MEASURES Precipitation Ensemble based on SSMIS DMSP F18 NASA PPS L1C V05 Tbs. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/DMSPF18/SSMIS/DATA201. https://measures.gsfc.nasa.gov/datacollection/PRECIP_SSMIS_F18_1.html. Digital Science Data.",
-            "issued": "2021-06-10",
-            "temporal": "2010-03-08T00:32:18Z/2021-01-01T00:56:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-10",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "precipitation"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Kidd",
                 "hasEmail": "mailto:chris.kidd@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2368311020-GES_DISC",
-            "description": "The data presented in this level 2 orbital product are rain rate estimates expressed as mm/hour determined from brightness temperatures (Tbs) obtained from the Special Sensor Microwave Imager Sounder (SSMIS) flown on the US Defense Meteorological Satellite Program (DMSP) F18 mission. Most of the products generated in this data set are based upon the algorithms developed for the 3rd Algorithm Intercomparison Project (AIP-3) of the Global Precipitation Climatology Project (GPCP).  Details of these 15 algorithms and development of a quality score which is a measure of confidence in the estimate, along with processing and algorithmic flags, can be found in the Algorithm Theoretical Basis Document  (ATBD).  The data in this product cover the period from 2010 to 2020 with one file per orbit.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "PRECIP_SSMIS_F18",
             "creator": "Chris Kidd",
-            "title": "NASA MEASURES Precipitation Ensemble based on SSMIS DMSP F18 NASA PPS L1C V05 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMIS_F18) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PRECIP_SSMIS_F18.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The data presented in this level 2 orbital product are rain rate estimates expressed as mm/hour determined from brightness temperatures (Tbs) obtained from the Special Sensor Microwave Imager Sounder (SSMIS) flown on the US Defense Meteorological Satellite Program (DMSP) F18 mission. Most of the products generated in this data set are based upon the algorithms developed for the 3rd Algorithm Intercomparison Project (AIP-3) of the Global Precipitation Climatology Project (GPCP).  Details of these 15 algorithms and development of a quality score which is a measure of confidence in the estimate, along with processing and algorithmic flags, can be found in the Algorithm Theoretical Basis Document  (ATBD).  The data in this product cover the period from 2010 to 2020 with one file per orbit.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSPF18%2FSSMIS%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FDMSPF18%2FSSMIS%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -985096,179 +985074,183 @@
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Precipitation/PRECIP_SSMIS_F18.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Precipitation/PRECIP_SSMIS_F18.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/PRECIP_SSMIS_F18.png",
+            "identifier": "C2368311020-GES_DISC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/DMSPF18/SSMIS/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-06-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "PRECIP_SSMIS_F18",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2010-03-08T00:32:18Z/2021-01-01T00:56:00Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NASA MEASURES Precipitation Ensemble based on SSMIS DMSP F18 NASA PPS L1C V05 Tbs 1-orbit L2 Swath 12x12km V1 (PRECIP_SSMIS_F18) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PRESW-RMJ10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I. . 2021-02-10. Northeast Weddell Sea Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/PRESW-RMJ10. Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I. 2021. Northeast Weddell Sea Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. PO.DAAC, CA, USA. Dataset accessed[YYYY-MM-DD] at https://doi.org/10.5067/PRESW-RMJ10.",
-            "issued": "2021-01-20",
-            "temporal": "2011-09-13T00:00:00Z/2012-11-15T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-11-14",
-            "references": [
-                "https://doi.org/10.1029/2019gl083074",
-                "https://doi.org/10.1029/2018JC014438",
-                "https://doi.org/10.17125/gov2018.ch13",
-                "https://doi.org/10.1038/s41467-018-02983-w",
-                "https://doi.org/10.1175/jtech-d-17-0076.1",
-                "https://doi.org/810.1175/JPO-D-15-0087.1"
-            ],
-            "keyword": [
-                "ocean circulation",
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
-                "earth science",
-                "ocean heat budget"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dimitris Menemenlis",
                 "hasEmail": "mailto:menemenlis@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2006849345-POCLOUD",
-            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Northeast Weddell Sea region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.",
-            "title": "Northeast Weddell Sea Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_ROAM_MIZ_v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the Northeast Weddell Sea region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-RMJ10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-RMJ10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/SWOT",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/SWOT",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/MEaSUREs-SSH",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/MEaSUREs-SSH",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/PRESW-RMJ10",
-                    "description": "Access the dataset landing page for the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page for the collection",
+                    "downloadURL": "https://doi.org/10.5067/PRESW-RMJ10",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/common/sw/generic_nc_readers",
-                    "description": "Generic netCDF read software provided in IDL, MATLAB, Python, and R",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "Generic netCDF read software provided in IDL, MATLAB, Python, and R",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/common/sw/generic_nc_readers",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_ROAM_MIZ_v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_ROAM_MIZ_v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2006849345-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2006849345-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2006849345-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2006849345-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/Pre-SWOT_LLC4320/preswot_llc4320_user_guide.pdf",
-                    "description": "PRE-SWOT NUMERICAL SIMULATION VERSION 1 USER GUIDE",
                     "@type": "dcat:Distribution",
+                    "description": "PRE-SWOT NUMERICAL SIMULATION VERSION 1 USER GUIDE",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/Pre-SWOT_LLC4320/preswot_llc4320_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/Pre-SWOT_LLC4320/README",
-                    "description": "Readme File",
                     "@type": "dcat:Distribution",
+                    "description": "Readme File",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/Pre-SWOT_LLC4320/README",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_ROAM_MIZ_v1.0.jpg",
+            "identifier": "C2006849345-POCLOUD",
+            "issued": "2021-01-20",
+            "keyword": [
+                "ocean circulation",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean heat budget"
+            ],
+            "landingPage": "https://doi.org/10.5067/PRESW-RMJ10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-11-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2019gl083074",
+                "https://doi.org/10.1029/2018JC014438",
+                "https://doi.org/10.17125/gov2018.ch13",
+                "https://doi.org/10.1038/s41467-018-02983-w",
+                "https://doi.org/10.1175/jtech-d-17-0076.1",
+                "https://doi.org/810.1175/JPO-D-15-0087.1"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "1.197917 -63.57185 5.177083 -59.5867",
+            "temporal": "2011-09-13T00:00:00Z/2012-11-15T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Northeast Weddell Sea Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jmwg-es6s",
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
-                "nen",
-                "space science",
-                "wise"
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
-            "identifier": "NASA-0000038__50",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -985276,21 +985258,48 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__50",
+            "issued": "2018-06-25",
+            "keyword": [
+                "geography",
+                "nen",
+                "space science",
+                "wise"
+            ],
+            "landingPage": "https://data.nasa.gov/d/jmwg-es6s",
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
-            "landingPage": "http://aeronet.gsfc.nasa.gov/cgi-bin/combined_data_access_new",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://aeronet.gsfc.nasa.gov/new_web/data_usage.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "description": "The aerosol optical depth processing includes the spectral de-convolution algorithm (SDA) described in O'Neill et al. (2003). This algorithm yields fine (sub-micron) and coarse (super-micron) aerosol optical depths at a standard wavelength of 500 nm (from which FMF*, the fraction of fine mode to total aerosol optical depth can be computed).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/SDA/SDA_Level2_Monthly.tar.gz",
+                    "mediaType": "application/x-tar"
+                }
             ],
+            "identifier": "NASA-0000010__2",
+            "issued": "2018-06-25",
             "keyword": [
                 "clouds",
                 "precipitable water",
@@ -985300,170 +985309,139 @@
                 "satellite",
                 "radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brent Holben",
-                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
-            },
+            "landingPage": "http://aeronet.gsfc.nasa.gov/cgi-bin/combined_data_access_new",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000010__2",
-            "description": "The aerosol optical depth processing includes the spectral de-convolution algorithm (SDA) described in O'Neill et al. (2003). This algorithm yields fine (sub-micron) and coarse (super-micron) aerosol optical depths at a standard wavelength of 500 nm (from which FMF*, the fraction of fine mode to total aerosol optical depth can be computed).",
-            "title": "AERONET Level 2.0 SDA",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aeronet.gsfc.nasa.gov/data_push/SDA/SDA_Level2_Monthly.tar.gz",
-                    "mediaType": "application/x-tar"
-                }
+            "references": [
+                "http://aeronet.gsfc.nasa.gov/new_web/data_usage.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "AERONET Level 2.0 SDA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/LMER-TIES/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/LMER-TIES/DATA001.",
-            "issued": "1993-07-03",
-            "temporal": "1993-07-03T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean optics",
-                "ocean chemistry",
-                "salinity/density",
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
-            "identifier": "C1633360440-OB_DAAC",
             "description": "Measurements taken under the Chesapeake Bay Land Margin Ecosystem Research (LMER): Trophic Interactions in Estuarine Systems (TIES) between 1993 and 2001.",
-            "title": "Land Margin Ecosystem Research (LMER): Trophic Interactions in Estuarine Systems (TIES)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLMER-TIES%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLMER-TIES%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/LMER-TIES/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/LMER-TIES/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360440-OB_DAAC",
+            "issued": "1993-07-03",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "salinity/density",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/LMER-TIES/DATA001",
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
+            "temporal": "1993-07-03T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Land Margin Ecosystem Research (LMER): Trophic Interactions in Estuarine Systems (TIES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M22-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 4 mission phase, covering the period  from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m22-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M22-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m22-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 4 mission phase, covering the period  from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP022 RDR-INFLDSTR V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP022 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3562",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Santee, M., Livesey, N., Read, W., and Fuller, R.. 2021-04-29. ML3DZCH3CL. Version 005. MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Zonal and Similar Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3562. https://disc.gsfc.nasa.gov/datacollection/ML3DZCH3CL_005.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
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
-            "identifier": "C2042566434-GES_DISC",
-            "description": "ML3DZCH3CL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for methyl chloride (CH3Cl) derived from radiances measured by the 640 GHz radiometer. The data version is 5.1. Data coverage is from August 2, 2005 to current. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is between 147 and 4.64 hPa, and the vertical resolution ranges between 4-6 km in the lower stratosphere and 8-10 km above 14 hPa. Users of the ML3DZCH3CL data product should read chapter 4 and section 3.3 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DZCH3CL",
             "creator": "Santee, M., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZCH3CL) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZCH3CL_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DZCH3CL is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for methyl chloride (CH3Cl) derived from radiances measured by the 640 GHz radiometer. The data version is 5.1. Data coverage is from August 2, 2005 to current. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is between 147 and 4.64 hPa, and the vertical resolution ranges between 4-6 km in the lower stratosphere and 8-10 km above 14 hPa. Users of the ML3DZCH3CL data product should read chapter 4 and section 3.3 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3562",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3562",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -985473,127 +985451,158 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZCH3CL_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZCH3CL_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZCH3CL.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZCH3CL.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZCH3CL.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZCH3CL.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZCH3CL_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZCH3CL_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZCH3CL_005.png",
+            "identifier": "C2042566434-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3562",
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
+            "series-name": "ML3DZCH3CL",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Methyl Chloride (CH3Cl) Mixing Ratio on Zonal and Similar Grids V005 (ML3DZCH3CL) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0978-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-21T21:32:20.000 to 2015-08-22T04:37:11.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0978-v1.0_jn72-unt3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0978-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0978-v1.0_jn72-unt3",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-21T21:32:20.000 to 2015-08-22T04:37:11.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0978 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0978 V1.0"
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
+            "description": "CDA, CIRS, ISS, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20091014.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-698",
+            "issued": "2018-06-25",
             "keyword": [
                 "iss",
                 "vims",
@@ -985606,906 +985615,873 @@
                 "cirs",
                 "cda"
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
-            "identifier": "NASA-698",
-            "description": "CDA, CIRS, ISS, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
-            "title": "PDS Cassini Data Release 19",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20091014.shtml",
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
+            "title": "PDS Cassini Data Release 19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROMAP-3-FSS-MAG-V1.0",
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
+            "description": "This archive contains preliminary calibrated data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the FSS (First Science Sequence) phase. It also contains documentation which describes the ROMAP experiment. The primary target is the comet 67P/Churyumov-Gerasimenko. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-romap-3-fss-mag-v1.0_jnbv-7fqp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-ROMAP-3-FSS-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-romap-3-fss-mag-v1.0_jnbv-7fqp",
-            "description": "This archive contains preliminary calibrated data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the FSS (First Science Sequence) phase. It also contains documentation which describes the ROMAP experiment. The primary target is the comet 67P/Churyumov-Gerasimenko. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P ROMAP 3 FSS MAG\n                            V1.0",
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
+            "title": "ROSETTA-LANDER 67P ROMAP 3 FSS MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chen, R.H., R.J. Michaelides, J. Chen, A.C. Chen, L.K. Clayton, K. Bakian-Dogaheh, L. Huang, E. Jafarov, L. Liu, M. Moghaddam, A.D. Parsekian, T.D. Sullivan, A. Tabatabaeenejad, E. Wig, H.A. Zebker, and Y. Zhao. 2022. ABoVE: Active Layer Thickness from Airborne L- and P- band SAR, Alaska, 2017, Ver. 3. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2004",
-            "issued": "2022-08-31",
-            "temporal": "2017-06-19T00:00:00Z/2017-09-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "earth science",
-                "soils",
-                "land surface",
-                "terrestrial hydrosphere indicators",
-                "frozen ground",
-                "cryosphere",
-                "climate indicators"
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
-            "identifier": "C2432584227-ORNL_CLOUD",
             "description": "This dataset provides estimates of seasonal subsidence, active layer thickness (ALT), the vertical soil moisture profile, and uncertainties at a 30 m resolution for 51 sites across the ABoVE domain, including 39 sites in Alaska and 12 sites in Northwest Canada. The ALT and soil moisture profile retrievals simultaneously use L- and P-band synthetic aperture radar (SAR) data acquired by the NASA/JPL Uninhabited Aerial Vehicle Synthetic Aperture Radar (UAVSAR) instruments during the 2017 Arctic Boreal Vulnerability Experiment (ABoVE) airborne campaign. The data are provided in NetCDF Version 4 format along with a python script for estimating soil volumetric water content from data.",
-            "graphic-preview-description": "Sites of the Permafrost Dynamics Observatory Project product.",
-            "title": "ABoVE: Active Layer Thickness from Airborne L- and P- band SAR, Alaska, 2017, Ver. 3",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ReSALT_InSAR_PolSAR_V3_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2004",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_ReSALT_InSAR_PolSAR_V3/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_ReSALT_InSAR_PolSAR_V3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ReSALT_InSAR_PolSAR_V3.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ReSALT_InSAR_PolSAR_V3.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2004",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2004",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_ReSALT_InSAR_PolSAR_V3/comp/ABoVE_ReSALT_InSAR_PolSAR_V3.pdf",
-                    "description": "ABoVE: Active Layer Thickness from Airborne L- and P- band SAR, Alaska, 2017, Ver. 3: ABoVE_ReSALT_InSAR_PolSAR_V3.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Active Layer Thickness from Airborne L- and P- band SAR, Alaska, 2017, Ver. 3: ABoVE_ReSALT_InSAR_PolSAR_V3.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_ReSALT_InSAR_PolSAR_V3/comp/ABoVE_ReSALT_InSAR_PolSAR_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ReSALT_InSAR_PolSAR_V3_Fig1.png",
-                    "description": "Sites of the Permafrost Dynamics Observatory Project product.",
                     "@type": "dcat:Distribution",
+                    "description": "Sites of the Permafrost Dynamics Observatory Project product.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ReSALT_InSAR_PolSAR_V3_Fig1.png",
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
+            "graphic-preview-description": "Sites of the Permafrost Dynamics Observatory Project product.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ReSALT_InSAR_PolSAR_V3_Fig1.png",
+            "identifier": "C2432584227-ORNL_CLOUD",
+            "issued": "2022-08-31",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface",
+                "terrestrial hydrosphere indicators",
+                "frozen ground",
+                "cryosphere",
+                "climate indicators"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2004",
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
             "spatial": "-166.73 57.83 -110.42 71.52",
+            "temporal": "2017-06-19T00:00:00Z/2017-09-16T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Active Layer Thickness from Airborne L- and P- band SAR, Alaska, 2017, Ver. 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-ROUGHNESS-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-roughness-ops-v1.0_jnec-77cg",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-ROUGHNESS-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-roughness-ops-v1.0_jnec-77cg",
-            "description": "NULL",
-            "title": "MER 1 MARS PANORAMIC CAMERA SURFACE\n                                     ROUGH RDR OPS V1.0",
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
+            "title": "MER 1 MARS PANORAMIC CAMERA SURFACE\n                                     ROUGH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3333-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-01T10:53:26.000 to 2012-07-01T14:15:32.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3333-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3333-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3333-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-01T10:53:26.000 to 2012-07-01T14:15:32.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3333 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3333 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VF7QO90IHZ99",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Near-Real-Time SSM/I-SSMIS EASE-Grid Daily Global Ice Concentration and Snow Extent V004. Version 4. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/VF7QO90IHZ99.",
-            "issued": "2009-08-17",
-            "temporal": "2009-08-17T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "keyword": [
-                "cryosphere",
-                "sea ice",
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
-            "identifier": "C1450086509-NSIDC_ECS",
             "description": "The Near-real-time Ice and Snow Extent (NISE) data set provides daily, global maps of sea ice concentrations and snow extent. These data are not suitable for time series, anomalies, or trends analyses. They are meant to provide a best estimate of current ice and snow conditions based on information and algorithms available at the time the data are acquired. Near-real-time products are not intended for operational use in assessing sea ice conditions for navigation. \n\nThis NISE Version 4 product contains DMSP-F17, SSMIS-derived sea ice concentrations and snow extents derived from the Special Sensor Microwave Imager/Sounder (SSMIS) aboard the Defense Meteorological Satellite Program (DMSP) F17 satellite. For DMSP-F16, SSMIS-derived data, see <a href=\"https://doi.org/10.5067/JAQDJKPX0S60\"> NISE Version 3</a>. For DMSP-F18, SSMIS-derived data, see <a href=\"https://dx.doi.org/10.5067/3KB2JPLFPK3R\">NISE Version 5</a>. For the older, DMSP-F13, Special Sensor Microwave Imager (SSMI) derived data, see <a href=\"https://doi.org/10.5067/4FSODMDM1WEJ\">NISE Version 2</a>.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "Near-Real-Time SSM/I-SSMIS EASE-Grid Daily Global Ice Concentration and Snow Extent V004",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-7689170,-3826010,5790597,2418912&p=arctic&l=SSMIS_Sea_Ice_Concentration_Snow_Extent(disabled=3-4-5-6;),Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVF7QO90IHZ99",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVF7QO90IHZ99",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/OTHR/NISE.004/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/OTHR/NISE.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NISE+V004",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NISE+V004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NISE/versions/4/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NISE/versions/4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-7689170%2C-3826010%2C5790597%2C2418912&p=arctic&l=SSMIS_Sea_Ice_Concentration_Snow_Extent%28disabled%3D3-4-5-6%3B%29%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-7689170%2C-3826010%2C5790597%2C2418912&p=arctic&l=SSMIS_Sea_Ice_Concentration_Snow_Extent%28disabled%3D3-4-5-6%3B%29%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VF7QO90IHZ99",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/VF7QO90IHZ99",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VF7QO90IHZ99",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VF7QO90IHZ99",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-7689170,-3826010,5790597,2418912&p=arctic&l=SSMIS_Sea_Ice_Concentration_Snow_Extent(disabled=3-4-5-6;),Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C1450086509-NSIDC_ECS",
+            "issued": "2009-08-17",
+            "keyword": [
+                "cryosphere",
+                "sea ice",
+                "earth science",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/VF7QO90IHZ99",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2009-08-17T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Near-Real-Time SSM/I-SSMIS EASE-Grid Daily Global Ice Concentration and Snow Extent V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/MOCE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/MOCE/DATA001.",
-            "issued": "1992-08-28",
-            "temporal": "1992-08-08T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean optics",
-                "ocean chemistry",
-                "ocean temperature",
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
-            "identifier": "C1633360487-OB_DAAC",
             "description": "Measurements taken under the Marine Optical Characterization Experiment between 1992 and 1999 off the US and Mexican Pacific coasts and central Pacific Ocean.",
-            "title": "Marine Optical Characterization Experiment (MOCE)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMOCE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMOCE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MOCE/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MOCE/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360487-OB_DAAC",
+            "issued": "1992-08-28",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "ocean temperature",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/MOCE/DATA001",
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
+            "temporal": "1992-08-08T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Marine Optical Characterization Experiment (MOCE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/NAAMES_Radiation_AircraftInSitu_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-03-23. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/NAAMES_Radiation_AircraftInSitu_Data_1.",
-            "issued": "2021-03-01",
-            "temporal": "2015-11-04T00:00:00Z/2017-09-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-11",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Behrenfeld",
                 "hasEmail": "mailto:behrenfm@science.oregonstate.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2031004453-LARC_ASDC",
             "description": "NAAMES_Radiation_AircraftInSitu_Data is the North Atlantic Aerosols and Marine Ecosystems Study (NAAMES) in-situ radiation data collected onboard the C-130 aircraft during the NAAMES campaign. NAAMES was a NASA funded Earth-Venture Suborbital (EVS) mission with 4 deployments occurring from 2015-2018. Data collection is complete.\r\n\r\nThe NASA North Atlantic Aerosols and Marine Ecosystems Study (NAAMES) project was the first NASA Earth Venture \u2013 Suborbital mission focused on studying the coupled ocean ecosystem and atmosphere. NAAMES utilizes a combination of ship-based, airborne, autonomous sensor, and remote sensing measurements that directly link ocean ecosystem processes, emissions of ocean-generated aerosols and precursor gases, and subsequent atmospheric evolution and processing. Four deployments coincide with the seasonal cycle of phytoplankton in the North Atlantic Ocean: the Winter Transition (November 5 \u2013 December 2, 2015), the Bloom Climax (May 11 \u2013 June 5, 2016), the Deceleration Phase (August 30 \u2013 September 24, 2017), and the Acceleration Phase (March 20 \u2013 April 13, 2018). Ship-based measurements were conducted from the Woods Hole Oceanographic Institution Research Vessel Atlantis in the middle of the North Atlantic Ocean, while airborne measurements were conducted on a NASA Wallops Flight Facility C-130 Hercules that was based at St. John's International Airport, Newfoundland, Canada. Data products in the ASDC archive focus on the NAAMES atmospheric aerosol, cloud, and trace gas data from the ship and aircraft, as well as related satellite and model data subsets. While a few ocean-remote sensing data products (e.g., from the high-spectral resolution lidar) are also included in the ASDC archive, most ocean data products reside in a companion archive at SeaBass.",
-            "title": "NAAMES C-130 Aircraft In-Situ Radiation Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FNAAMES_Radiation_AircraftInSitu_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FNAAMES_Radiation_AircraftInSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/NAAMES",
-                    "description": "ASDC Data and Information for NAAMES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for NAAMES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/NAAMES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://naames.larc.nasa.gov/",
-                    "description": "NAAMES project home page",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES project home page",
+                    "downloadURL": "https://naames.larc.nasa.gov/",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/naames/naames-project-documents.html",
-                    "description": "ASDC NAAMES Project Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC NAAMES Project Documentation Page",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/naames/naames-project-documents.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/naames",
-                    "description": "NAAMES SeaBASS Data",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES SeaBASS Data",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/naames",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.frontiersin.org/articles/10.3389/fmars.2019.00122/full",
-                    "description": "NAAMES Science Motive and Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES Science Motive and Mission Overview",
+                    "downloadURL": "https://www.frontiersin.org/articles/10.3389/fmars.2019.00122/full",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/fromthefield/category/naames/",
-                    "description": "NASA Earth Observatory NAAMES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory NAAMES Posts",
+                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/fromthefield/category/naames/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/naames/",
-                    "description": "NASA Earth Expeditions NAAMES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions NAAMES Posts",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/naames/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/five-year-nasa-study-to-look-at-the-immense-influence-of-petite-plankton",
-                    "description": "NASA.gov Article \u201cFive-Year NASA Study to Look at the Immense Influence of Petite Plankton\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cFive-Year NASA Study to Look at the Immense Influence of Petite Plankton\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/five-year-nasa-study-to-look-at-the-immense-influence-of-petite-plankton",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/all-in-the-naames-of-ocean-ecosystems-and-climate",
-                    "description": "NASA.gov Article \u201cAll in the NAAMES of Ocean Ecosystems and Climate\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cAll in the NAAMES of Ocean Ecosystems and Climate\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/all-in-the-naames-of-ocean-ecosystems-and-climate",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/naames-returns-to-air-and-sea-to-study-plankton-s-annual-cycle",
-                    "description": "NASA.gov Article \u201cNAAMES Returns to Air and Sea to Study Plankton\u2019s Annual Cycle\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cNAAMES Returns to Air and Sea to Study Plankton\u2019s Annual Cycle\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/naames-returns-to-air-and-sea-to-study-plankton-s-annual-cycle",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/outreach-materials#name-exploring-the-connection-between-plankton-and-clouds-naames-storymap",
-                    "description": "ASDC StoryMap \u201cExploring the Connection Between Plankton and Clouds \u2013 NAAMES\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC StoryMap \u201cExploring the Connection Between Plankton and Clouds \u2013 NAAMES\u201d",
+                    "downloadURL": "https://asdc.larc.nasa.gov/outreach-materials#name-exploring-the-connection-between-plankton-and-clouds-naames-storymap",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/a-look-into-the-north-atlantic-aerosols-and-marine-ecosystems-study-naames",
-                    "description": "ASDC Microarticle \u201cA Look into the North Atlantic Aerosols and Marine Ecosystems Study (NAAMES)\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Microarticle \u201cA Look into the North Atlantic Aerosols and Marine Ecosystems Study (NAAMES)\u201d",
+                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/a-look-into-the-north-atlantic-aerosols-and-marine-ecosystems-study-naames",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/observing-sea-to-air-aerosol-gas-fluxes-under-extreme-weather-conditions",
-                    "description": "ASDC Microarticle \u201cObserving Sea-to-Air Aerosol Gas Fluxes Under Extreme Weather Conditions\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Microarticle \u201cObserving Sea-to-Air Aerosol Gas Fluxes Under Extreme Weather Conditions\u201d",
+                    "downloadURL": "https://asdc.larc.nasa.gov/micro-article/observing-sea-to-air-aerosol-gas-fluxes-under-extreme-weather-conditions",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/NAAMES_Radiation_AircraftInSitu_Data_1",
-                    "description": "DOI Data Set Landing Page for NAAMES_Radiation_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for NAAMES_Radiation_AircraftInSitu_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/NAAMES_Radiation_AircraftInSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2031004453-LARC_ASDC",
-                    "description": "Earthdata Search for NAAMES_Radiation_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NAAMES_Radiation_AircraftInSitu_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2031004453-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/NAAMES/2015",
-                    "description": "NAAMES Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/NAAMES/2015",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.frontiersin.org/research-topics/8451/unraveling-mechanisms-underlying-annual-plankton-blooms-in-the-north-atlantic-and-their-implications",
-                    "description": "Frontiers E-Book: Unraveling Mechanisms Underlying Annual Plankton Blooms in the North Atlantic and their Implications for Biogenic Aerosol Properties and Cloud Formation",
                     "@type": "dcat:Distribution",
+                    "description": "Frontiers E-Book: Unraveling Mechanisms Underlying Annual Plankton Blooms in the North Atlantic and their Implications for Biogenic Aerosol Properties and Cloud Formation",
+                    "downloadURL": "https://www.frontiersin.org/research-topics/8451/unraveling-mechanisms-underlying-annual-plankton-blooms-in-the-north-atlantic-and-their-implications",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NAAMES/Radiation_AircraftInSitu_Data_1/",
-                    "description": "ASDC Direct Data Download for NAAMES_Radiation_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NAAMES_Radiation_AircraftInSitu_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NAAMES/Radiation_AircraftInSitu_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/NAAMES/Radiation_AircraftInSitu_Data_1/contents.html",
-                    "description": "OPeNDAP data access for NAAMES_Radiation_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for NAAMES_Radiation_AircraftInSitu_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/NAAMES/Radiation_AircraftInSitu_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2031004453-LARC_ASDC",
+            "issued": "2021-03-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/NAAMES_Radiation_AircraftInSitu_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.0 -80.0 30.0 -30.0 65.0 -30.0 65.0 -80.0 30.0 -80.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-11-04T00:00:00Z/2017-09-20T23:59:59.999Z",
             "theme": [
                 "NAAMES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NAAMES C-130 Aircraft In-Situ Radiation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1848",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Haynes, K.D., I.T. Baker, and A.S. Denning. 2021. SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1848",
-            "issued": "2024-05-01",
-            "temporal": "2000-01-01T00:00:00Z/2018-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-02",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "earth science",
-                "soils",
-                "land surface",
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
-            "identifier": "C2345882961-ORNL_CLOUD",
             "description": "This dataset provides global monthly output predicted by the Simple Biosphere Model, Version 4.2 (SiB4), at a 0.5-degree spatial resolution covering the time period 2000 through 2018. SiB4 is a mechanistic land surface model that integrates heterogeneous land cover, environmentally responsive phenology, dynamic carbon allocation, and cascading carbon pools from live biomass to surface litter to soil organic matter. Monthly output includes carbon, carbonyl sulfide (COS), and energy fluxes; solar-induced fluorescence (SIF); carbon pools; soil moisture and temperatures in the top three layers; total column soil water and plant available water; and environmental potentials used to scale photosynthesis. The SiB4 output is per plant functional type (PFT) within each 0.5-degree grid cell. SiB4 partitions variable output to 15 PFTs in each grid cell that are indexed by the \"npft\" dimension (01-15) in each data file. The PFT three-character abbreviations (\"pft_names\" variable) are listed in the same order as the \"npft\" dimension. To combine the PFT-specific output into grid cell totals, users must compute the area-weighted mean across the vector of PFT-specific values for each cell. Fractional areal coverages are given in the \"pft_area\" variable for each cell.",
-            "graphic-preview-description": "Overview of the Simple Biosphere Model (SiB4) that estimates carbon fluxes among the atmosphere, vegetation, and soils. Input information is shown in yellow boxes. This dataset includes a selection of the output variables (blue boxes). Source: Haynes et al. (2020)",
-            "title": "SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/SiB4_Global_HalfDegree_Monthly_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1848",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1848",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/SiB4_Global_HalfDegree_Monthly/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/SiB4_Global_HalfDegree_Monthly/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SiB4_Global_HalfDegree_Monthly.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SiB4_Global_HalfDegree_Monthly.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1848",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1848",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SiB4_Global_HalfDegree_Monthly/comp/SiB4_assessment.pdf",
-                    "description": "SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018: SiB4_assessment.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018: SiB4_assessment.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SiB4_Global_HalfDegree_Monthly/comp/SiB4_assessment.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SiB4_Global_HalfDegree_Monthly/comp/SiB4_Global_HalfDegree_Monthly.pdf",
-                    "description": "SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018: SiB4_Global_HalfDegree_Monthly.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018: SiB4_Global_HalfDegree_Monthly.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SiB4_Global_HalfDegree_Monthly/comp/SiB4_Global_HalfDegree_Monthly.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SiB4_Global_HalfDegree_Monthly/comp/SiB4_v2.tgz",
-                    "description": "SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018: SiB4_v2.tgz",
                     "@type": "dcat:Distribution",
+                    "description": "SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018: SiB4_v2.tgz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/SiB4_Global_HalfDegree_Monthly/comp/SiB4_v2.tgz",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SiB4_Global_HalfDegree_Monthly_Fig1.png",
-                    "description": "Overview of the Simple Biosphere Model (SiB4) that estimates carbon fluxes among the atmosphere, vegetation, and soils. Input information is shown in yellow boxes. This dataset includes a selection of the output variables (blue boxes). Source: Haynes et al. (2020)",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of the Simple Biosphere Model (SiB4) that estimates carbon fluxes among the atmosphere, vegetation, and soils. Input information is shown in yellow boxes. This dataset includes a selection of the output variables (blue boxes). Source: Haynes et al. (2020)",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/SiB4_Global_HalfDegree_Monthly_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Overview of the Simple Biosphere Model (SiB4) that estimates carbon fluxes among the atmosphere, vegetation, and soils. Input information is shown in yellow boxes. This dataset includes a selection of the output variables (blue boxes). Source: Haynes et al. (2020)",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/SiB4_Global_HalfDegree_Monthly_Fig1.png",
+            "identifier": "C2345882961-ORNL_CLOUD",
+            "issued": "2024-05-01",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science",
+                "soils",
+                "land surface",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1848",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-01-01T00:00:00Z/2018-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SiB4 Modeled Global 0.5-Degree Monthly Carbon Fluxes and Pools, 2000-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-5-WILD2-SHAPE-MODEL-V1.0",
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
-                "stardust",
-                "81p/wild 2 (1978 a2)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Basic tri-axial ellipsoid shape model of comet 81P/Wild 2, as derived from Navcam images obtained around the time of closest approach to the comet.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-5-wild2-shape-model-v1.0_jnnf-db7n",
+            "issued": "2018-06-26",
+            "keyword": [
+                "stardust",
+                "81p/wild 2 (1978 a2)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-5-WILD2-SHAPE-MODEL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-5-wild2-shape-model-v1.0_jnnf-db7n",
-            "description": "Basic tri-axial ellipsoid shape model of comet 81P/Wild 2, as derived from Navcam images obtained around the time of closest approach to the comet.",
-            "title": "TRI-AXIAL ELLIPSOID MODEL OF COMET WILD 2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TRI-AXIAL ELLIPSOID MODEL OF COMET WILD 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H41N7Z2Z",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN. 1994-12-31. Georeferenced Population Datasets of Mexico (GEO-MEX): Raster Based GIS Coverage of Mexican Population. Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H41N7Z2Z. https://doi.org/10.7927/H41N7Z2Z.",
-            "issued": "1994-12-31",
-            "temporal": "1990-01-01T00:00:00Z/1990-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1994-12-31",
-            "references": [
-                "https://doi.org/10.7927/H45D8PS8",
-                "https://doi.org/10.7927/H4S46PV7",
-                "https://doi.org/10.7927/H4959FH0",
-                "https://doi.org/10.7927/H4WW7FKN"
-            ],
-            "keyword": [
-                "boundaries",
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
-            "identifier": "C179001922-SEDAC",
-            "description": "The Raster Based GIS Coverage of Mexican Population is a gridded coverage (1 x 1 km) of Mexican population. The data were converted from vector into raster. The population figures were derived based on available point data (the population of known localities - 30,000 in all). Cell values were derived using a weighted moving average function (Burrough, 1986), and then calculated based on known population by state. The result from this conversion is a coverage whose population data is based on square grid cells rather than a series of vectors. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the Instituto Nacional de Estadistica Geografia e Informatica (INEGI).",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN",
-            "title": "Georeferenced Population Datasets of Mexico (GEO-MEX): Raster Based GIS Coverage of Mexican Population",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/geo-mex/geo-mex-mexico-raster-based-population-gis/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Raster Based GIS Coverage of Mexican Population is a gridded coverage (1 x 1 km) of Mexican population. The data were converted from vector into raster. The population figures were derived based on available point data (the population of known localities - 30,000 in all). Cell values were derived using a weighted moving average function (Burrough, 1986), and then calculated based on known population by state. The result from this conversion is a coverage whose population data is based on square grid cells rather than a series of vectors. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the Instituto Nacional de Estadistica Geografia e Informatica (INEGI).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH41N7Z2Z",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH41N7Z2Z",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/geo-mex/geo-mex-mexico-raster-based-population-gis/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/geo-mex/geo-mex-mexico-raster-based-population-gis/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-raster-based-population-gis/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-raster-based-population-gis/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-raster-based-population-gis/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-raster-based-population-gis/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-raster-based-population-gis",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/geo-mex-mexico-raster-based-population-gis",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/geo-mex/geo-mex-mexico-raster-based-population-gis/sedac-logo.jpg",
+            "identifier": "C179001922-SEDAC",
+            "issued": "1994-12-31",
+            "keyword": [
+                "boundaries",
+                "earth science",
+                "human dimensions",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H41N7Z2Z",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1994-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H45D8PS8",
+                "https://doi.org/10.7927/H4S46PV7",
+                "https://doi.org/10.7927/H4959FH0",
+                "https://doi.org/10.7927/H4WW7FKN"
+            ],
+            "release-place": "Saginaw, MI",
             "spatial": "-117.0 14.0 -86.0 33.0",
+            "temporal": "1990-01-01T00:00:00Z/1990-12-31T00:00:00Z",
             "theme": [
                 "GEO-MEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Georeferenced Population Datasets of Mexico (GEO-MEX): Raster Based GIS Coverage of Mexican Population"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/888/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-01-07",
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
-            "identifier": "DASHLINK_888",
             "description": "Model-based prognostics approaches use domain knowledge about a system and its failure modes through the use of physics-based models. Model-based prognosis is generally divided into two sequential problems: a joint state-parameter estimation problem, in which, using the model, the health of a system or component is determined based on the observations; and a prediction problem, in which, using the model, the state-parameter distribution is simulated forward in time to compute end of life and remaining useful life. The first problem is typically solved through the use of a state observer, or filter. The choice of filter depends on the assumptions that may be made about the system, and on the desired algorithm performance. In this paper, we review three separate filters for the solution to the first problem: the Daum filter, an exact nonlinear filter; the unscented Kalman filter, which approximates nonlinearities through the use of a deterministic sampling method known as the unscented transform; and the particle filter, which approximates the state distribution using a finite set of discrete, weighted samples, called particles. Using a centrifugal pump as a case study, we conduct a number of simulation-based experiments investigating the performance of the different algorithms as applied to prognostics.",
-            "title": "A Comparison of Filter-based Approaches for Model-based Prognostics",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/vnd.openxmlformats-officedocument.presentationml.pre",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/DaigleEtAl-ComparisonFilterBasedPrognostics-Aero2011.pptx",
-                    "description": "DaigleEtAl-ComparisonFilterBasedPrognostics-Aero2011.pptx",
                     "@type": "dcat:Distribution",
+                    "description": "DaigleEtAl-ComparisonFilterBasedPrognostics-Aero2011.pptx",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/DaigleEtAl-ComparisonFilterBasedPrognostics-Aero2011.pptx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.presentationml.pre",
                     "title": "DaigleEtAl-ComparisonFilterBasedPrognostics-Aero2011.pptx"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_888",
+            "issued": "2014-01-07",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/888/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Comparison of Filter-based Approaches for Model-based Prognostics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-02-22",
-            "temporal": "2021-02-22T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "topo",
-                "trajectory",
-                "station",
-                "space",
-                "location",
-                "iss",
-                "international",
-                "ephemeris",
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
-            "identifier": "nasa-iss-data_2021-02-22",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-02-22",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -986628,279 +986604,304 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-02-22",
+            "issued": "2021-02-22",
+            "keyword": [
+                "topo",
+                "trajectory",
+                "station",
+                "space",
+                "location",
+                "iss",
+                "international",
+                "ephemeris",
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
+            "temporal": "2021-02-22T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-02-22"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agaskell.dione.shape-model&version=1.0",
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
-                "saturn iv (dione)",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The shape model of Dione derived by      Robert Gaskell from Cassini images.  The model is provided in the      implicitly connected quadrilateral (ICQ) format.  This version of the  model was prepared on July 23, 2012.  Vertex-facet versions of the     models are also provided.",
+            "identifier": "urn:nasa:pds:gaskell.dione.shape-model",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn iv (dione)",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agaskell.dione.shape-model&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gaskell.dione.shape-model",
-            "description": "The shape model of Dione derived by      Robert Gaskell from Cassini images.  The model is provided in the      implicitly connected quadrilateral (ICQ) format.  This version of the  model was prepared on July 23, 2012.  Vertex-facet versions of the     models are also provided.",
-            "title": "GASKELL DIONE SHAPE MODEL",
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
+            "title": "GASKELL DIONE SHAPE MODEL"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/MRR/DATA202",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Barros, Ana P.2017. GPM Ground Validation Duke Micro Rain Radar (MRR) IPHEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/MRR/DATA202",
-            "issued": "2017-06-26",
-            "temporal": "2014-05-01T00:00:00Z/2014-06-15T23:59:55Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
-                "spectral/engineering",
-                "atmosphere",
-                "earth science",
-                "precipitation",
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
-            "identifier": "C1979626644-GHRC_DAAC",
             "description": "The GPM Ground Validation Duke Micro Rain Radar (MRR) IPHEx dataset was gathered during the Global Precipitation Measurement (GPM) Ground Validation Integrated Precipitation and Hydrology Experiment (IPHEx) in North Carolina from May 1, 2014 through June 15, 2014. The dataset contains measured and derived data from three MRR instruments placed in separate locations within the study region. The MRR is a Biral/Metek 24 GHz (K-band) vertically oriented Frequency Modulated Continuous Wave (FM-CW) radar that measures signal backscatter from which Doppler spectra, radar reflectivity, Doppler velocity, drop size distribution, rain rate, liquid water content, and path integrated attenuation are derived.  Data files are available in ASCII data format.",
-            "title": "GPM Ground Validation Duke Micro Rain Radar (MRR) IPHEx V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FMRR%2FDATA202",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FMRR%2FDATA202",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmrrdukeiphx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmrrdukeiphx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.7924/G8CC0XMR",
-                    "description": "NASA GPM-Ground Validation: Integrated Precipitation and Hydrology Experiment 2014 Science Plan",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GPM-Ground Validation: Integrated Precipitation and Hydrology Experiment 2014 Science Plan",
+                    "downloadURL": "http://dx.doi.org/10.7924/G8CC0XMR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://wallops-prf.gsfc.nasa.gov/Field_Campaigns/IPHEx/index.html",
-                    "description": "Integrated Precipitation Hydrology Experiment (IPHEx)",
                     "@type": "dcat:Distribution",
+                    "description": "Integrated Precipitation Hydrology Experiment (IPHEx)",
+                    "downloadURL": "https://wallops-prf.gsfc.nasa.gov/Field_Campaigns/IPHEx/index.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IPHEX/DATA101",
-                    "description": "IPHEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IPHEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/mrr_Duke/doc/gpmmrrdukeiphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/mrr_Duke/doc/gpmmrrdukeiphx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://journals.ametsoc.org/doi/pdf/10.1175/JAM2316.1",
-                    "description": "Profiles of Raindrop Size Distributions as Retrieved by Microrain Radars",
                     "@type": "dcat:Distribution",
+                    "description": "Profiles of Raindrop Size Distributions as Retrieved by Microrain Radars",
+                    "downloadURL": "http://journals.ametsoc.org/doi/pdf/10.1175/JAM2316.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1029/2010GL046018",
-                    "description": "Aliasing in Micro Rain Radar data due to strong vertical winds",
                     "@type": "dcat:Distribution",
+                    "description": "Aliasing in Micro Rain Radar data due to strong vertical winds",
+                    "downloadURL": "http://dx.doi.org/10.1029/2010GL046018",
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
+            "identifier": "C1979626644-GHRC_DAAC",
+            "issued": "2017-06-26",
+            "keyword": [
+                "spectral/engineering",
+                "atmosphere",
+                "earth science",
+                "precipitation",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/MRR/DATA202",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-83.0743 35.5843 -82.5814 35.8894",
+            "temporal": "2014-05-01T00:00:00Z/2014-06-15T23:59:55Z",
             "theme": [
                 "IPHEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Duke Micro Rain Radar (MRR) IPHEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0037-5-SHAPE153591-V1.0",
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
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "We present the three-dimensional shapes  and rotation states of the three components of near-Earth asteroid     (153591) 2001 SN263 based on radar images and optical lightcurves      (Becker et al., 2015. 2001 SN263 was observed in 2003 using the        12.6-cm radar at Arecibo Observatory. Optical lightcurves were         obtained at several observatories and used to further constrain the    shape modeling.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0037-5-shape153591-v1.0_jnxk-222s",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0037-5-SHAPE153591-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0037-5-shape153591-v1.0_jnxk-222s",
-            "description": "We present the three-dimensional shapes  and rotation states of the three components of near-Earth asteroid     (153591) 2001 SN263 based on radar images and optical lightcurves      (Becker et al., 2015. 2001 SN263 was observed in 2003 using the        12.6-cm radar at Arecibo Observatory. Optical lightcurves were         obtained at several observatories and used to further constrain the    shape modeling.",
-            "title": "SHAPE MODEL OF ASTEROID (153591) 2001   \n        SN263 V1.0",
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
+            "title": "SHAPE MODEL OF ASTEROID (153591) 2001   \n        SN263 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8DJW56PKY133",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge BGM-3 Gravimeter L2 Geolocated Free Air Anomalies V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/8DJW56PKY133.",
-            "issued": "2009-01-08",
-            "temporal": "2009-01-08T00:00:00Z/2011-12-21T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-12-21",
-            "keyword": [
-                "earth science",
-                "gravity/gravitational field",
-                "solid earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Donald Blankenship",
                 "hasEmail": "mailto:blank@ig.utexas.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1000000341-NSIDC_ECS",
             "description": "This data set contains free air anomaly measurements taken over Antarctica using the BGM-3 Gravimeter. The data were collected by scientists working on the Investigating the Cryospheric Evolution of the Central Antarctic Plate (ICECAP) project funded by the National Science Foundation (NSF) and the Natural Environment Research Council (NERC) with additional support from NASA Operation IceBridge.",
-            "title": "IceBridge BGM-3 Gravimeter L2 Geolocated Free Air Anomalies V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8DJW56PKY133",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8DJW56PKY133",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGBGM2.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGBGM2.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000341-NSIDC_ECS&m=-61.86041224173192%21150.57254359681028%210%212%210%210%2C2&tl=1513803253%214%21%21&q=IGBGM2",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000341-NSIDC_ECS&m=-61.86041224173192%21150.57254359681028%210%212%210%210%2C2&tl=1513803253%214%21%21&q=IGBGM2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/icebridge/portal",
-                    "description": "Tool to visualize, search, and download IceBridge data.",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to visualize, search, and download IceBridge data.",
+                    "downloadURL": "https://nsidc.org/icebridge/portal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGBGM2/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGBGM2/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8DJW56PKY133",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/8DJW56PKY133",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/8DJW56PKY133",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/8DJW56PKY133",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000341-NSIDC_ECS",
+            "issued": "2009-01-08",
+            "keyword": [
+                "earth science",
+                "gravity/gravitational field",
+                "solid earth"
+            ],
+            "landingPage": "https://doi.org/10.5067/8DJW56PKY133",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-12-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2009-01-08T00:00:00Z/2011-12-21T23:59:59.999Z",
             "theme": [
                 "2008_AN_UTIG",
                 "2009_AN_UTIG",
@@ -986908,304 +986909,279 @@
                 "2011_AN_UTIG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge BGM-3 Gravimeter L2 Geolocated Free Air Anomalies V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-3-RDR-ELS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains calibrated Mars Express ASPERA-3 Electron Spectrometer (ELS) data from launch (June 2, 2003) to the end of the nominal mission (through December 2005). These data are provided in units of Differential Number Flux (DNF): cnts/(cm**2-sr-sec-eV)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-3-rdr-els-v1.0_jp2u-2qhi",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "solar wind",
                 "mars express",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-3-RDR-ELS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-3-rdr-els-v1.0_jp2u-2qhi",
-            "description": "This data set contains calibrated Mars Express ASPERA-3 Electron Spectrometer (ELS) data from launch (June 2, 2003) to the end of the nominal mission (through December 2005). These data are provided in units of Differential Number Flux (DNF): cnts/(cm**2-sr-sec-eV)",
-            "title": "MARS EXPRESS ASPERA-3 CAL RDR ELECTRON SPECTROMETER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARS EXPRESS ASPERA-3 CAL RDR ELECTRON SPECTROMETER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-MRI-3%2F4-EPOXI-MARS-V2.0",
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
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains calibrated 750-nm filter images of Mars acquired by the Deep Impact Medium Resolution Visible CCD (MRI) for the EPOCh project during the second cruise phase of the EPOXI mission. One set of observations was acquired on 20-21 November 2009 to characterize Mars as an analog for extrasolar planets. The observing period lasted approximately 24 hours, and one MRI image was taken simultaneously with the first north/south scan of the HRI IR spectrometer at half-hour intervals to provide context for the spectral scans. Version 2.0 includes the application of a horizontal destriping process, new absolute calibration constants for filters, and revised electronic crosstalk calibration files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-mri-3-4-epoxi-mars-v2.0_jp5a-94wr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-M-MRI-3%2F4-EPOXI-MARS-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-m-mri-3-4-epoxi-mars-v2.0_jp5a-94wr",
-            "description": "This dataset contains calibrated 750-nm filter images of Mars acquired by the Deep Impact Medium Resolution Visible CCD (MRI) for the EPOCh project during the second cruise phase of the EPOXI mission. One set of observations was acquired on 20-21 November 2009 to characterize Mars as an analog for extrasolar planets. The observing period lasted approximately 24 hours, and one MRI image was taken simultaneously with the first north/south scan of the HRI IR spectrometer at half-hour intervals to provide context for the spectral scans. Version 2.0 includes the application of a horizontal destriping process, new absolute calibration constants for filters, and revised electronic crosstalk calibration files.",
-            "title": "EPOXI MARS OBS - MRI CALIBRATED IMAGES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI MARS OBS - MRI CALIBRATED IMAGES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0925-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-28T10:40:10.000 to 2015-07-28T17:29:29.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0925-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0925-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0925-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-28T10:40:10.000 to 2015-07-28T17:29:29.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0925 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0925 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ESROGSS/AERDB_L2_ABI_G17.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2024-12-27. GOES-17 ABI Dark Target Aerosol 10-Min L2 Full Disk 10 km. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/ESROGSS/AERDB_L2_ABI_G17.001. https://doi.org/10.5067/ESROGSS/AERDB_L2_ABI_G17.001.",
-            "issued": "2023-08-22",
-            "temporal": "2019-05-01T00:00:00Z/2020-05-01T04:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-01",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C3352437433-LAADS",
-            "description": "The ABI G17 Deep Blue Aerosol 10-Min L2 Full Disk product, short-name AERDB_L2_ABI_G17 is produced every 30 minutes and contains full-disk observation data. The L2 data products comprise 10 x 10 native GEO pixels. Each spectral band with 0.5 km or 2 km resolution is downscaled or upscaled to a nominal ~1 km horizontal pixel size in the production process. To distinguish them from native instrument pixels, these 10 x 10 aggregated pixels are also called retrieval pixels. Therefore, the L2 products\u2019 image dimensions are roughly 10 km x 10 km at the sub-satellite point and are larger away from that point because of the combined effects of the sensor\u2019s scanning geometry and Earth\u2019s curvature. This first release of these products spans from May 2019 through April 2020 with a potential to generate additional temporal coverage in the future. \n\nThe Level-2 (L2) Advanced Baseline Imager (ABI) Geostationary Operational Environmental Satellite-17 (GOES-17) Deep Blue Aerosol Full-Disk dataset is part of a 12-product suite produced by an Earth Science Research from Operational Geostationary Satellite Systems (ESROGSS)-funded project. The 12 products in this project include nine derived from three Geostationary Earth Observation (GEO) instruments and three from merged data from GEO and Low-Earth Orbit (LEO) instruments.\n\nThe AERDB_L2_ABI_G17 product, in netCDF4 format, contains 51 Science Data Set (SDS) layers. \n\nFor more information consult LAADS product description page at:\n\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDB_L2_ABI_G17\n\nOr, Deep Blue aerosol project webpage at: \nhttps://earth.gsfc.nasa.gov/climate/data/deep-blue",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "GOES17 ABI Deep Blue Aerosol L2",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ABI G17 Deep Blue Aerosol 10-Min L2 Full Disk product, short-name AERDB_L2_ABI_G17 is produced every 30 minutes and contains full-disk observation data. The L2 data products comprise 10 x 10 native GEO pixels. Each spectral band with 0.5 km or 2 km resolution is downscaled or upscaled to a nominal ~1 km horizontal pixel size in the production process. To distinguish them from native instrument pixels, these 10 x 10 aggregated pixels are also called retrieval pixels. Therefore, the L2 products\u2019 image dimensions are roughly 10 km x 10 km at the sub-satellite point and are larger away from that point because of the combined effects of the sensor\u2019s scanning geometry and Earth\u2019s curvature. This first release of these products spans from May 2019 through April 2020 with a potential to generate additional temporal coverage in the future. \n\nThe Level-2 (L2) Advanced Baseline Imager (ABI) Geostationary Operational Environmental Satellite-17 (GOES-17) Deep Blue Aerosol Full-Disk dataset is part of a 12-product suite produced by an Earth Science Research from Operational Geostationary Satellite Systems (ESROGSS)-funded project. The 12 products in this project include nine derived from three Geostationary Earth Observation (GEO) instruments and three from merged data from GEO and Low-Earth Orbit (LEO) instruments.\n\nThe AERDB_L2_ABI_G17 product, in netCDF4 format, contains 51 Science Data Set (SDS) layers. \n\nFor more information consult LAADS product description page at:\n\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDB_L2_ABI_G17\n\nOr, Deep Blue aerosol project webpage at: \nhttps://earth.gsfc.nasa.gov/climate/data/deep-blue",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FESROGSS%2FAERDB_L2_ABI_G17.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FESROGSS%2FAERDB_L2_ABI_G17.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earth-dev.gsfc.nasa.gov/climate/data/deep-blue/documentation",
-                    "description": "Data product documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data product documentation",
+                    "downloadURL": "https://earth-dev.gsfc.nasa.gov/climate/data/deep-blue/documentation",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/AERDB_L2_ABI_G17--5019",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/AERDB_L2_ABI_G17--5019",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/Document%20Archive/Science%20Data%20Product%20Documentation/GEO_Deep-Blue_Aerosol_UG_v1.0.pdf",
-                    "description": "A pdf version User's Guide for dark target products.",
                     "@type": "dcat:Distribution",
+                    "description": "A pdf version User's Guide for dark target products.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/Document%20Archive/Science%20Data%20Product%20Documentation/GEO_Deep-Blue_Aerosol_UG_v1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C3352437433-LAADS",
+            "issued": "2023-08-22",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ESROGSS/AERDB_L2_ABI_G17.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-05-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-05-01T00:00:00Z/2020-05-01T04:59:00Z",
             "theme": [
                 "GOES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOES17 ABI Deep Blue Aerosol L2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1172-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-11T04:58:40.000 to 2015-11-11T07:59:48.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1172-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1172-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1172-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-11T04:58:40.000 to 2015-11-11T07:59:48.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1172 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1172 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-ION-MOM-96.0SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 2 ENCOUNTER. RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IS SOME REGIONS. DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY. THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY. THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983). DATA FORMAT: COLUMNS 1-5 ARE TIME (YEAR, DAY, HOUR, MIN, SEC) AND COLUMN 6 IS THE MOMENT DENSITY IN CM-3. EACH ROW HAS FORMAT (I5,I4,2I3,I4,F8.3). ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN LAZARUS AND MCNUTT (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-ion-mom-96.0sec_jpbt-q6jz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "saturn",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PLS-5-ION-MOM-96.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pls-5-ion-mom-96.0sec_jpbt-q6jz",
-            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 2 ENCOUNTER. RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IS SOME REGIONS. DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY. THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY. THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983). DATA FORMAT: COLUMNS 1-5 ARE TIME (YEAR, DAY, HOUR, MIN, SEC) AND COLUMN 6 IS THE MOMENT DENSITY IN CM-3. EACH ROW HAS FORMAT (I5,I4,2I3,I4,F8.3). ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN LAZARUS AND MCNUTT (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
-            "title": "VOYAGER 2 SATURN PLASMA DERIVED ION MOMENTS 96 SEC",
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
+            "title": "VOYAGER 2 SATURN PLASMA DERIVED ION MOMENTS 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-02-15",
-            "temporal": "2022-02-15T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "iss",
-                "coordinates",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "location",
-                "international",
-                "ephemeris",
-                "coords"
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
-            "identifier": "nasa-iss-data_2022-02-15_jpc4-khud",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2022-02-15",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -987328,537 +987304,570 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2022-02-15_jpc4-khud",
+            "issued": "2022-02-15",
+            "keyword": [
+                "iss",
+                "coordinates",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "location",
+                "international",
+                "ephemeris",
+                "coords"
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
+            "temporal": "2022-02-15T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2022-02-15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1356-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-20T05:00:45.000 to 2016-01-20T07:00:10.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1356-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1356-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1356-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-20T05:00:45.000 to 2016-01-20T07:00:10.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1356 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1356 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXI.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Kerry Cawse-Nicholson. 2021-06-04. ECO3ETALEXI.001. ECOSTRESS Evapotranspiration dis-ALEXI Daily L3 CONUS 70 m V001. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXI.001. https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXI.001. The DOI landing page provides citations in APA and Chicago formats..",
-            "issued": "2018-07-15",
-            "temporal": "2018-07-15T00:00:00Z/2023-03-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-06",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor"
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
-            "identifier": "C1639530522-LPDAAC_ECS",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data over the conterminous United States (CONUS) as well as key biomes and agricultural zones around the world and selected FLUXNET (http://fluxnet.fluxdata.org/about/) validation sites. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe NASA Jet Propulsion Laboratory (JPL) ECO3ETALEXI Version 1 data product provides estimates of daily evapotranspiration (ET) using the ECOSTRESS Level 2 (L2) land surface temperature and emissivity (LST&E) product, along with ancillary meteorological data and remotely sensed vegetation cover information. The ECO3ETALEXI data product is derived using a physics-based surface energy balance (SEB) algorithm, the Atmosphere Land Exchange Inverse (ALEXI) Disaggregation algorithm (DisALEXI). Described in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1000/ECO3ETALEXI_ATBD_V1.pdf), DisALEXI is based on spatial disaggregation of regional-scale fluxes from the ALEXI SEB model. There are many approaches for spatially mapping ET; however, SEB methods are favored for remote sensing retrievals based on land-surface temperature. ALEXI was initially developed for managed landscapes and has now been evaluated in comparison with micrometeorological flux tower observations over crop, forest, grassland, wetland, and semiarid desert sites. Applications include crop water use, crop phenology monitoring, and drought early warning or water stress detection. ECO3ETALEXI is available for CONUS at 70-meter (m) pixel resolution.\r\n\r\nThe ECO3ETALEXI Version 1 data product contains layers of daily ET, ET uncertainty, and associated quality flags. A low-resolution browse is also available showing daily ET as a stretched image with a color ramp in JPEG format.",
-            "series-name": "ECO3ETALEXI.001",
-            "graphic-preview-description": "Browse for Earthdata Search",
             "creator": "Simon Hook, Kerry Cawse-Nicholson",
-            "title": "ECOSTRESS Evapotranspiration dis-ALEXI Daily L3 CONUS 70 m V001",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.10.25/ECOSTRESS_L3_ET_ALEXI_12977_012_20201019T204204_0601_01.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data over the conterminous United States (CONUS) as well as key biomes and agricultural zones around the world and selected FLUXNET (http://fluxnet.fluxdata.org/about/) validation sites. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe NASA Jet Propulsion Laboratory (JPL) ECO3ETALEXI Version 1 data product provides estimates of daily evapotranspiration (ET) using the ECOSTRESS Level 2 (L2) land surface temperature and emissivity (LST&E) product, along with ancillary meteorological data and remotely sensed vegetation cover information. The ECO3ETALEXI data product is derived using a physics-based surface energy balance (SEB) algorithm, the Atmosphere Land Exchange Inverse (ALEXI) Disaggregation algorithm (DisALEXI). Described in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/1000/ECO3ETALEXI_ATBD_V1.pdf), DisALEXI is based on spatial disaggregation of regional-scale fluxes from the ALEXI SEB model. There are many approaches for spatially mapping ET; however, SEB methods are favored for remote sensing retrievals based on land-surface temperature. ALEXI was initially developed for managed landscapes and has now been evaluated in comparison with micrometeorological flux tower observations over crop, forest, grassland, wetland, and semiarid desert sites. Applications include crop water use, crop phenology monitoring, and drought early warning or water stress detection. ECO3ETALEXI is available for CONUS at 70-meter (m) pixel resolution.\r\n\r\nThe ECO3ETALEXI Version 1 data product contains layers of daily ET, ET uncertainty, and associated quality flags. A low-resolution browse is also available showing daily ET as a stretched image with a color ramp in JPEG format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO3ETALEXI.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO3ETALEXI.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1639530522-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1639530522-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO3ETALEXI.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO3ETALEXI.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXI.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXI.001",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/999/ECO3ETALEXI_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/999/ECO3ETALEXI_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1000/ECO3ETALEXI_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1000/ECO3ETALEXI_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.10.25/ECOSTRESS_L3_ET_ALEXI_12977_012_20201019T204204_0601_01.1.jpg",
-                    "description": "Browse for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.10.25/ECOSTRESS_L3_ET_ALEXI_12977_012_20201019T204204_0601_01.1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
+            "graphic-preview-description": "Browse for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.10.25/ECOSTRESS_L3_ET_ALEXI_12977_012_20201019T204204_0601_01.1.jpg",
+            "identifier": "C1639530522-LPDAAC_ECS",
+            "issued": "2018-07-15",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO3ETALEXI.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "series-name": "ECO3ETALEXI.001",
             "spatial": "-127.0 23.0 -65.0 52.0",
+            "temporal": "2018-07-15T00:00:00Z/2023-03-13T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Evapotranspiration dis-ALEXI Daily L3 CONUS 70 m V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ROS-E%2FM%2FA%2FC-SPICE-6-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "SPICE deals with ancillary data needed to support the planning for, and analysis of, science instrument data. As well as software (the SPICE toolkit) and documentation, SPICE provides data files, called kernels, that contain ancillary information which has been created in such a way as to allow easy access and correct usage by the space science and engineering communities.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ros-e-m-a-c-spice-6-v1.0_jpdu-cva9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ROS-E%2FM%2FA%2FC-SPICE-6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ros-e-m-a-c-spice-6-v1.0_jpdu-cva9",
-            "description": "SPICE deals with ancillary data needed to support the planning for, and analysis of, science instrument data. As well as software (the SPICE toolkit) and documentation, SPICE provides data files, called kernels, that contain ancillary information which has been created in such a way as to allow easy access and correct usage by the space science and engineering communities.",
-            "title": "ROSETTA SPICE KERNELS V1.0",
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
+            "title": "ROSETTA SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0038",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2002-09-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0038.",
-            "issued": "2003-11-28",
-            "temporal": "2000-08-05T00:00:00Z/2000-09-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "earth science",
-                "aerosols",
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
-            "identifier": "C1000000102-LARC_ASDC",
             "description": "The NARSTO_EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR measurement data consist of absolute absorbance areas for organonitrates, sulfate, aliphatic carbon and carbonyl compounds for size segregated particulate matter collected using a Herring Low Pressure Impactor (LPI). These data were collected during August and September 2000 at the Houston PM Supersite locations (LaPorte, HRM3, and Aldine) during the Texas Air Quality Study 2000 (TexAQS).The Houston Supersite is one of several Supersites that was established in urban areas within the United States by the U.S. Environmental Protection Agency (EPA) to better understand the measurement, sources, and health effects of suspended particulate matter (PM). The overall goals were to characterize the composition and identify the sources of particulate matter in Southeastern Texas, to develop and test new methods for characterizing fine particulate matter, and to collect data on the physical and chemical characterization of fine particulate matter that can be used to support exposure and health effects studies.NARSTO (formerly North American Research Strategy for Tropospheric Ozone) is a public/private partnership, whose membership spans government, the utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission is to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are available.",
-            "title": "NARSTO EPA_SS_HOUSTON TEXAQS2000 Particulate Matter FTIR Composition",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0038",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0038",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000102-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000102-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0038",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0038",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_houston_texaqs2000_pm_ftir.pdf",
-                    "description": "Guide for NARSTO EPA_SS_HOUSTON TEXAQS2000 Particulate Matter FTIR Composition",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_HOUSTON TEXAQS2000 Particulate Matter FTIR Composition",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_houston_texaqs2000_pm_ftir.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_HOUSTON_TEXAQS2000_PM_FTIR_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000102-LARC_ASDC",
+            "issued": "2003-11-28",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0038",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>29.0 -96.0 29.0 -93.0 30.5 -93.0 30.5 -96.0 29.0 -96.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-08-05T00:00:00Z/2000-09-13T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA_SS_HOUSTON TEXAQS2000 Particulate Matter FTIR Composition"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-07-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1.",
-            "issued": "2021-06-10",
-            "temporal": "2011-06-30T00:00:00Z/2011-08-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-20",
-            "keyword": [
-                "air quality",
-                "atmosphere",
-                "aerosols",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "earth science",
-                "altitude"
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
-            "identifier": "C2358952642-LARC_ASDC",
             "description": "DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data contains data collected at ancillary ground sites during the Maryland (Baltimore-Washington) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Maryland deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P3-B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Maryland Deployment Analysis and Ancillary Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
-                    "description": "DOI for DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2358952642-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2358952642-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Ground_Analysis_Ancillary_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Ground_Analysis_Ancillary_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2358952642-LARC_ASDC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "aerosols",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "earth science",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Analysis_Ancillary_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.0 -109.0 30.0 70.0 45.0 70.0 45.0 -109.0 30.0 -109.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2011-06-30T00:00:00Z/2011-08-02T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Maryland Deployment Analysis and Ancillary Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRII-2-EPOXI-CALIBRATIONS-V2.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains raw calibration spectra acquired by the High Resolution Infrared Spectrometer (HRII) from 04 October 2007 through 07 February 2011 during the EPOCh, 103P/Hartley 2 Encounter, and cruise phases of the EPOXI mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hrii-2-epoxi-calibrations-v2.0_jpf6-cst4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "epoxi",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRII-2-EPOXI-CALIBRATIONS-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hrii-2-epoxi-calibrations-v2.0_jpf6-cst4",
-            "description": "This dataset contains raw calibration spectra acquired by the High Resolution Infrared Spectrometer (HRII) from 04 October 2007 through 07 February 2011 during the EPOCh, 103P/Hartley 2 Encounter, and cruise phases of the EPOXI mission.",
-            "title": "EPOXI INFLIGHT CALIBRATIONS - HRII RAW SPECTRA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI INFLIGHT CALIBRATIONS - HRII RAW SPECTRA V2.0"
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
+            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090309.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-601",
+            "issued": "2018-06-25",
             "keyword": [
                 "crism",
                 "hirise",
@@ -987870,42 +987879,47 @@
                 "ctx",
                 "marci"
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
-            "identifier": "NASA-601",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 8",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090309.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 8"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/jpgc-pf6n",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Microgravity effect on C. elegans gene expression was analysed by whole genome microarray. The worms were cultivated under microgravity for 8 days in the Japanese Module of the International Space Station. The samples of this study were divided three experimental groups: 1. microgravity for 8 days 2. artificial 1G control for 8 days on orbit 3. ground 1G control for 8 days This study was repeated with three biological and two technical replicates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-41",
+                    "mediaType": "text/html",
+                    "title": "Microgravity effect on C. elegans N2/VC (CERISE 8days)"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-41_jpgc-pf6n",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse27338-5",
                 "image_aquisition",
@@ -987923,739 +987937,701 @@
                 "p-gse27338-4",
                 "nucleic_acid_extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/jpgc-pf6n",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-41_jpgc-pf6n",
-            "description": "Microgravity effect on C. elegans gene expression was analysed by whole genome microarray. The worms were cultivated under microgravity for 8 days in the Japanese Module of the International Space Station. The samples of this study were divided three experimental groups: 1. microgravity for 8 days 2. artificial 1G control for 8 days on orbit 3. ground 1G control for 8 days This study was repeated with three biological and two technical replicates.",
-            "title": "Microgravity effect on C. elegans N2/VC (CERISE 8days)",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-41",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microgravity effect on C. elegans N2/VC (CERISE 8days)"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microgravity effect on C. elegans N2/VC (CERISE 8days)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/841",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Pilewskie, P. 2006. SAFARI 2000 Solar Spectral Flux Radiometer Data, Southern Africa, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/841",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-17T00:00:00Z/2000-09-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C2788411266-ORNL_CLOUD",
             "description": "The Solar Spectral Flux Radiometer (SSFR) was deployed on the University of Washington CV-580 during the dry season component of the Southern African Regional Science Initiative, August 1 - September 20, 2000. The SSFR made simultaneous measurements of both downwelling and upwelling net solar spectral irradiance at varying flight levels.  Data have been provided for twenty flights in netcdf format for the period August 17 - September 16, 2000.For a complete detailed guide to the extensive measurements obtained aboard the UW Convair-580 aircraft in support of SAFARI 2000, see the UW Technical Report for the SAFARI 2000 Project.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Solar Spectral Flux Radiometer Data, Southern Africa, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F841",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F841",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/SSFR_irradiance/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/SSFR_irradiance/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/S2K_SSFR_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/S2K_SSFR_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/841",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/841",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/SSFR_irradiance/comp/SAFARI-MASTER.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/SSFR_irradiance/comp/SAFARI-MASTER.pdf",
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
+            "identifier": "C2788411266-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/841",
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
             "spatial": "5.0 -35.0 60.0 5.0",
+            "temporal": "2000-08-17T00:00:00Z/2000-09-16T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Solar Spectral Flux Radiometer Data, Southern Africa, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1738",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Anchang, J.Y., L. Prihodko, A.T. Kaptue, C.W. Ross, W. Ji, S.S. Kumar, B. Lind, M.A. Sarr, A.A. Diouf, and N.P. Hanan. 2020. Woody and Herbaceous Vegetation Change across the Savannas of West Africa, 1982-2013. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1738",
-            "issued": "2020-05-07",
-            "temporal": "1982-01-01T00:00:00Z/2013-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "vegetation",
-                "precipitation",
-                "human dimensions",
-                "habitat conversion/fragmentation",
-                "ecosystems",
-                "ecological dynamics",
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2764722720-ORNL_CLOUD",
             "description": "The WAVeTrends dataset is a 0.05 degree (5.55 km) vegetation change product, spanning the West African Sudano-Sahel region. It provides pixel-wise information on concurrent woody and herbaceous vegetation trends over a 32-year period (1982-2013). Change in woody vegetation was derived using long-term rain use efficiency (RUE) sensitivity, i.e., the per-pixel comparison of the difference of mean RUE between the first and last decades of the 32-year time series. Herbaceous vegetation change was defined by short-term RUE sensitivity, i.e., comparing the slope of the RUE relationship (productivity vs. precipitation) between both decades using per-pixel Analysis of Covariance (ANCOVA). Categorical vegetation change was then determined for each pixel using the direction of the change and a significance level of p<0.05. The use of RUE (the amount of biomass produced per unit of precipitation) for vegetation trend analysis in savanna regions relies on the assumption that rainfall is a significant positive driver of net production in drylands. Testing of this long-term productivity-rainfall relationship revealed that the assumption was not always met, therefore, validity flags are included for each pixel location.",
-            "graphic-preview-description": "Concurrent woody and herbaceous vegetation changes between the 1982-1991 and 2004-2013 decades of the Sudano-Sahel region of Africa. (A) Map of vegetation change categories. (B) Chart showing the conceptual position and the relative abundance of each category in a 2-D space (Anchang et al. 2019).",
-            "title": "Woody and Herbaceous Vegetation Change across the Savannas of West Africa, 1982-2013",
-            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/WAVeTrends_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1738",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1738",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/WAVeTrends/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/WAVeTrends/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/WAVeTrends.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/WAVeTrends.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1738",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1738",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/WAVeTrends/comp/WAVeTrends.pdf",
-                    "description": "West African Vegetation Trends (WAVeTrends): WAVeTrends.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "West African Vegetation Trends (WAVeTrends): WAVeTrends.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/WAVeTrends/comp/WAVeTrends.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/WAVeTrends/comp/WAVeTrends_classify.pdf",
-                    "description": "West African Vegetation Trends (WAVeTrends): WAVeTrends_classify.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "West African Vegetation Trends (WAVeTrends): WAVeTrends_classify.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/WAVeTrends/comp/WAVeTrends_classify.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/WAVeTrends_Fig1.png",
-                    "description": "Concurrent woody and herbaceous vegetation changes between the 1982-1991 and 2004-2013 decades of the Sudano-Sahel region of Africa. (A) Map of vegetation change categories. (B) Chart showing the conceptual position and the relative abundance of each category in a 2-D space (Anchang et al. 2019).",
                     "@type": "dcat:Distribution",
+                    "description": "Concurrent woody and herbaceous vegetation changes between the 1982-1991 and 2004-2013 decades of the Sudano-Sahel region of Africa. (A) Map of vegetation change categories. (B) Chart showing the conceptual position and the relative abundance of each category in a 2-D space (Anchang et al. 2019).",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/WAVeTrends_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Concurrent woody and herbaceous vegetation changes between the 1982-1991 and 2004-2013 decades of the Sudano-Sahel region of Africa. (A) Map of vegetation change categories. (B) Chart showing the conceptual position and the relative abundance of each category in a 2-D space (Anchang et al. 2019).",
+            "graphic-preview-file": "https://daac.ornl.gov/VEGETATION/guides/WAVeTrends_Fig1.png",
+            "identifier": "C2764722720-ORNL_CLOUD",
+            "issued": "2020-05-07",
+            "keyword": [
+                "vegetation",
+                "precipitation",
+                "human dimensions",
+                "habitat conversion/fragmentation",
+                "ecosystems",
+                "ecological dynamics",
+                "earth science",
+                "biosphere",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1738",
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
             "spatial": "-17.14 9.96 15.31 17.41",
+            "temporal": "1982-01-01T00:00:00Z/2013-12-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Woody and Herbaceous Vegetation Change across the Savannas of West Africa, 1982-2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-SESAME-3-FSS-V1.0",
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
+            "description": "This archive contains calibrated data (CODMAC level 3) from the SESAME instrument onboard ROSETTA Lander, acquired during the FSS phase. It also contains documentation which describes the SESAME experiment. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-sesame-3-fss-v1.0_jphr-8qhy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-SESAME-3-FSS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-sesame-3-fss-v1.0_jphr-8qhy",
-            "description": "This archive contains calibrated data (CODMAC level 3) from the SESAME instrument onboard ROSETTA Lander, acquired during the FSS phase. It also contains documentation which describes the SESAME experiment. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P SESAME 3 FSS\n                            V1.0",
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
+            "title": "ROSETTA-LANDER 67P SESAME 3 FSS\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1204",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schuh, A.E., T. Lauvaux, S.M. Ogle, K.J. Davis, A.S. Denning, N.L. Miles, S.J. Richardson, and M. Uliasz. 2014. NACP MCI: CO2 Flux from Inversion Modeling, Upper Midwest Region, USA, 2007. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1204",
-            "issued": "2022-11-21",
-            "temporal": "2007-01-01T00:00:00Z/2007-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C2539908010-ORNL_CLOUD",
             "description": "This data set provides estimates of Net Ecosystem Exchange (NEE) flux for the U.S. Upper Midwest at 0.5-degree resolution for the year 2007. Estimates were produced by two atmospheric CO2 inversion systems (top-down), referenced as the continental Colorado State University (CSU) inversion and the mesoscale Pennsylvania State University (PSU) inversion. This modeling work was performed in support of the North American Carbon Program (NACP) Mid-Continent Intensive (MCI) experimental campaign in the U.S. Upper Midwest designed to evaluate innovative methods for CO2 flux inversion and data assimilation. The experiment was performed over a relatively flat, heavily managed agricultural landscape which features a high density of atmospheric CO2 observation measurements. Among the CO2 observations used by the inversion systems were results from a network of instrumented tall towers in the region. The NEE estimates were produced for comparison with CO2 fluxes derived from bottom-up inventory estimates.There are five data files with this data set. The NEE estimates are provided in two NetCDF files, one for each inversion system. Boundary CO2 inflow data used by each inversion system are provided in three comma-separated-format files (.csv).",
-            "graphic-preview-description": "Browse Image",
-            "title": "NACP MCI: CO2 Flux from Inversion Modeling, Upper Midwest Region, USA, 2007",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/nacp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1204",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1204",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_MCI_CO2_Inversions/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/NACP_MCI_CO2_Inversions/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_MCI_CO2_Inversions.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/NACP_MCI_CO2_Inversions.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1204",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1204",
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
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_CO2_Inversions/comp/NACP_MCI_Boundary_Shapefile.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_CO2_Inversions/comp/NACP_MCI_Boundary_Shapefile.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_CO2_Inversions/comp/NACP_MCI_CO2_Inversions.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_CO2_Inversions/comp/NACP_MCI_CO2_Inversions.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_CO2_Inversions/comp/NACP_MCI_US_County_Boundaries_Shapefile.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_CO2_Inversions/comp/NACP_MCI_US_County_Boundaries_Shapefile.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_CO2_Inversions/comp/NACP_MCI_US_County_Names.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/NACP_MCI_CO2_Inversions/comp/NACP_MCI_US_County_Names.csv",
+                    "mediaType": "text/csv",
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
+            "identifier": "C2539908010-ORNL_CLOUD",
+            "issued": "2022-11-21",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1204",
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
             "spatial": "-105.0 36.0 -81.0 50.0",
+            "temporal": "2007-01-01T00:00:00Z/2007-12-31T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP MCI: CO2 Flux from Inversion Modeling, Upper Midwest Region, USA, 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-3-EDR-EROS%2FORBIT-V1.0",
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
-                "eros",
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The GRS Level 2 data products in this archive include daily time series of spectra collected by the instrument along with selected spacecraft engineering and instrument configuration and orbital ephemerides. Supporting documentation includes as to the specifics of how these data were generated. Selected ephemerides and engineering parameters are averaged for the composite set of information.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-3-edr-eros-orbit-v1.0_jpnh-4ue4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-3-EDR-EROS%2FORBIT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-3-edr-eros-orbit-v1.0_jpnh-4ue4",
-            "description": "The GRS Level 2 data products in this archive include daily time series of spectra collected by the instrument along with selected spacecraft engineering and instrument configuration and orbital ephemerides. Supporting documentation includes as to the specifics of how these data were generated. Selected ephemerides and engineering parameters are averaged for the composite set of information.",
-            "title": "NEAR GRS SPECTRA FOR EROS/ORBIT",
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
+            "title": "NEAR GRS SPECTRA FOR EROS/ORBIT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DAL_L3.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 Global Albedo product for a day;See ProductionDateTime for Published date.",
-            "issued": "2004-11-04",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C61095953-LARC",
             "description": "MISR Level 3 Component Global Albedo publicly available product covering a day to be used starting with MISR Release V3.2.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Component Global Albedo product covering a day V006",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DAL_L3.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL3DAL_L3.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C61095953-LARC",
+            "issued": "2004-11-04",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL3DAL_L3.006",
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
+            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Component Global Albedo product covering a day V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V18.0",
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
+            "description": "This data set is intended to include all published groundbased asteroid radar detections. The file is based on the collection of asteroid radar detections established by Steven J. Ostro and currently maintained by Lance A.M. Benner. The file includes disc-integrated radar properties extracted from the published papers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v18.0_jpqj-ujh4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V18.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v18.0_jpqj-ujh4",
-            "description": "This data set is intended to include all published groundbased asteroid radar detections. The file is based on the collection of asteroid radar detections established by Steven J. Ostro and currently maintained by Lance A.M. Benner. The file includes disc-integrated radar properties extracted from the published papers.",
-            "title": "ASTEROID RADAR V18.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID RADAR V18.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1373",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Raich, J.W., and O.J. Valverde-Barrantes. 2017. Soil CO2 Flux, Moisture, Temperature, and Litterfall, La Selva, Costa Rica, 2003-2010. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1373",
-            "issued": "2017-03-16",
-            "temporal": "2003-10-01T00:00:00Z/2010-02-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "atmosphere",
-                "earth science",
-                "biosphere",
-                "vegetation",
-                "soils",
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
-            "identifier": "C2216864144-ORNL_CLOUD",
             "description": "This data set provides measurements of soil carbon dioxide (CO2) emission rates, soil moisture, relative humidity (RH), temperature, and litterfall from six types of tree plantations at the La Selva Biological Station, Costa Rica. Soil CO2 flux and related measurements were made 1) hourly during 2-day diel field campaigns and 2) as single daytime measurements during multiple survey campaigns, over the period 2004-2010. All measurements were made at the same sites to compare hourly, monthly, and inter-annual variations. Most of the emissions data represent a single soil CO2 flux measurement, with three to five measurements per plot. Litterfall was collected monthly from 2003-2009 and was sorted into fractions prior to drying.",
-            "graphic-preview-description": "The LaSelva Biological Preserve, Costa Rica.",
-            "title": "Soil CO2 Flux, Moisture, Temperature, and Litterfall, La Selva, Costa Rica, 2003-2010",
-            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/SOIL_CO2_Flux_Costa_Rica_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1373",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1373",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/global_soil/SOIL_CO2_Flux_Costa_Rica/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/global_soil/SOIL_CO2_Flux_Costa_Rica/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/SOIL_CO2_Flux_Costa_Rica.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/SOIL_CO2_Flux_Costa_Rica.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1373",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1373",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/SOIL_CO2_Flux_Costa_Rica/comp/SOIL_CO2_Flux_Costa_Rica.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_soil/SOIL_CO2_Flux_Costa_Rica/comp/SOIL_CO2_Flux_Costa_Rica.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/SOIL_CO2_Flux_Costa_Rica_Fig1.png",
-                    "description": "The LaSelva Biological Preserve, Costa Rica.",
                     "@type": "dcat:Distribution",
+                    "description": "The LaSelva Biological Preserve, Costa Rica.",
+                    "downloadURL": "https://daac.ornl.gov/SOILS/guides/SOIL_CO2_Flux_Costa_Rica_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "The LaSelva Biological Preserve, Costa Rica.",
+            "graphic-preview-file": "https://daac.ornl.gov/SOILS/guides/SOIL_CO2_Flux_Costa_Rica_Fig1.png",
+            "identifier": "C2216864144-ORNL_CLOUD",
+            "issued": "2017-03-16",
+            "keyword": [
+                "land surface",
+                "atmosphere",
+                "earth science",
+                "biosphere",
+                "vegetation",
+                "soils",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1373",
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
             "spatial": "-84.05 10.43 -84.04 10.44",
+            "temporal": "2003-10-01T00:00:00Z/2010-02-25T23:59:59Z",
             "theme": [
                 "Soil",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil CO2 Flux, Moisture, Temperature, and Litterfall, La Selva, Costa Rica, 2003-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/EXRAD/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Gerald M and Lin  Tian.2016. GPM GROUND VALIDATION ER-2 X-BAND RADAR (EXRAD) IPHEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/EXRAD/DATA101",
-            "issued": "2016-10-18",
-            "temporal": "2014-05-03T17:57:45Z/2014-06-12T23:28:34Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
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
-            "identifier": "C1979141020-GHRC_DAAC",
             "description": "The GPM Ground Validation ER-2 X-band Radar (EXRAD) IPHEx dataset was collected in support of the Global Precipitation Measurement (GPM) mission Ground Validation Integrated Precipitation and Hydrology Experiment (IPHEx) field campaign in North Carolina, with an intense study period occurring from May 1, 2014 through June 15, 2014. The goal of IPHEx was to evaluate the accuracy of satellite precipitation measurements and use the collected data for hydrology models in the region. EXRAD is a single-frequency X-band Doppler radar that measures reflectivity and Doppler velocity. The science instruments, including the EXRAD, onboard the NASA ER-2 aircraft acted as a proxy for GPM satellite instruments. This dataset is available in netCDF-3 file format.",
-            "title": "GPM GROUND VALIDATION ER-2 X-BAND RADAR (EXRAD) IPHEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FEXRAD%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FEXRAD%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmexradiphx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmexradiphx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IPHEX/DATA101",
-                    "description": "IPHEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/IPHEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://science.gsfc.nasa.gov/sci/content/uploadFiles/scihi_atmos_ppt/2013_4_highlights.pdf",
-                    "description": "First Flights of ER-2 X-band Radar",
                     "@type": "dcat:Distribution",
+                    "description": "First Flights of ER-2 X-band Radar",
+                    "downloadURL": "http://science.gsfc.nasa.gov/sci/content/uploadFiles/scihi_atmos_ppt/2013_4_highlights.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://har.gsfc.nasa.gov/index.php?section=14",
-                    "description": "EXRAD Description and Sample Measurements from the Nadir Beam",
                     "@type": "dcat:Distribution",
+                    "description": "EXRAD Description and Sample Measurements from the Nadir Beam",
+                    "downloadURL": "http://har.gsfc.nasa.gov/index.php?section=14",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/EXRAD/doc/gpmexradiphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/EXRAD/doc/gpmexradiphx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(1997)014%3C0203:COSEIO%3E2.0.CO;2",
-                    "description": "Correction of Sampling Errors in Ocean Surface Cross-Sectional Estimates from Nadir-Looking Weather Radar",
                     "@type": "dcat:Distribution",
+                    "description": "Correction of Sampling Errors in Ocean Surface Cross-Sectional Estimates from Nadir-Looking Weather Radar",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(1997)014%3C0203:COSEIO%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2080:TPRRPA%3E2.0.CO;2",
-                    "description": "TRMM Precipitation Radar Reflectivity Profiles as Compared with High-Resolution Airborne and Ground-Based Radar Measurements",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Precipitation Radar Reflectivity Profiles as Compared with High-Resolution Airborne and Ground-Based Radar Measurements",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2080:TPRRPA%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7924/G8CC0XMR",
-                    "description": "NASA GPM-Ground Validation: Integrated Precipitation and Hydrology Experiment 2014 Science Plan",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GPM-Ground Validation: Integrated Precipitation and Hydrology Experiment 2014 Science Plan",
+                    "downloadURL": "https://doi.org/10.7924/G8CC0XMR",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
-                    "description": "IPHEx Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
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
+            "identifier": "C1979141020-GHRC_DAAC",
+            "issued": "2016-10-18",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/EXRAD/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-86.5619 26.7991 -71.9384 36.5498",
+            "temporal": "2014-05-03T17:57:45Z/2014-06-12T23:28:34Z",
             "theme": [
                 "IPHEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION ER-2 X-BAND RADAR (EXRAD) IPHEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1261530244-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Spencer R., Christy J.R.. 1996-01-01. MSULST. Version 001. MSU Ch 4 Daily Lower Stratosphere Temps with Limb93 Correction L3 1 day 2.5 degree x 2.5 degree V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/MSULST_001.html.",
-            "issued": "1979-01-01",
-            "temporal": "1979-01-01T00:00:00Z/1994-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1994-12-31",
-            "keyword": [
-                "atmospheric temperature",
-                "spectral/engineering",
-                "microwave",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1261530244-GES_DISC",
-            "description": "The Microwave Sounding Unit (MSU) Lower Stratosphere Deep Layer Mean Temperature product (MSULST) provides gridded lower stratospheric temperatures for each day derived from MSU instruments on several different platforms. The temperatures are derived from MSU channel 4 using the method of Spencer and Christy (1990) with the LIMB 93 limb correction based on latitude, longitude,  month, and scan angle. The MSU instruments measure the thermal emission of radiation by molecular oxygen at four frequencies near 60 GHz.  North (south) of 66.7N (S) the footprint data are assigned to grid boxes in a weighted method depending on footprint latitude.  Horizontal averaging is used\nto fill some of the empty grid boxes.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MSULST",
             "creator": "Spencer R., Christy J.R.",
-            "title": "MSU Ch 4 Daily Lower Stratosphere Temps with Limb93 Correction L3 1 day 2.5 degree x 2.5 degree V001 (MSULST) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MSULST_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Microwave Sounding Unit (MSU) Lower Stratosphere Deep Layer Mean Temperature product (MSULST) provides gridded lower stratospheric temperatures for each day derived from MSU instruments on several different platforms. The temperatures are derived from MSU channel 4 using the method of Spencer and Christy (1990) with the LIMB 93 limb correction based on latitude, longitude,  month, and scan angle. The MSU instruments measure the thermal emission of radiation by molecular oxygen at four frequencies near 60 GHz.  North (south) of 66.7N (S) the footprint data are assigned to grid boxes in a weighted method depending on footprint latitude.  Horizontal averaging is used\nto fill some of the empty grid boxes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -988664,84 +988640,86 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MSULST_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MSULST_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/msu/MSULST.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/msu/MSULST.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/opendap/lim93/MSULST.001/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/opendap/lim93/MSULST.001/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://disc1.gsfc.nasa.gov/data/msu/MSULST.001/doc/README.lim93.pdf",
-                    "description": "Microwave Sounding Unit (MSU) Limb93 Documentation.",
                     "@type": "dcat:Distribution",
+                    "description": "Microwave Sounding Unit (MSU) Limb93 Documentation.",
+                    "downloadURL": "https://disc1.gsfc.nasa.gov/data/msu/MSULST.001/doc/README.lim93.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MSU/GES_DISC_MSU_Data_Guide.pdf",
-                    "description": "This is an MSU legacy data guide.  Some information may be obsolete.",
                     "@type": "dcat:Distribution",
+                    "description": "This is an MSU legacy data guide.  Some information may be obsolete.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MSU/GES_DISC_MSU_Data_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MSULST_001.png",
+            "identifier": "C1261530244-GES_DISC",
+            "issued": "1979-01-01",
+            "keyword": [
+                "atmospheric temperature",
+                "spectral/engineering",
+                "microwave",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1261530244-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1994-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "MSULST",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1979-01-01T00:00:00Z/1994-12-31T23:59:59.999Z",
             "theme": [
                 "TOVS Pathfinder",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MSU Ch 4 Daily Lower Stratosphere Temps with Limb93 Correction L3 1 day 2.5 degree x 2.5 degree V001 (MSULST) at GES DISC"
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
-                "turbulence",
-                "flow",
-                "cases",
-                "models",
-                "incompressible"
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
-            "identifier": "NASA-845__10",
             "description": "This grouping contains more recent incompressible-flow cases.",
-            "title": "Collaborative Testing of Turbulence Models: More Recent Incompressible Flow Cases",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -988749,455 +988727,489 @@
                     "mediaType": "application/x-gzip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-845__10",
+            "issued": "2018-06-25",
+            "keyword": [
+                "turbulence",
+                "flow",
+                "cases",
+                "models",
+                "incompressible"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-02 to 2014-09-16.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m07-v1.0_jpys-kaku",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m07-v1.0_jpys-kaku",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the prelanding phase of the Rosetta mission at the comet 67P,\ncovering the period from 2014-09-02 to 2014-09-16.",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 2 EDR MTP 007 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSINAC 2 EDR MTP 007 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1162-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-07T08:18:10.000 to 2015-11-07T12:29:07.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1162-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1162-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1162-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-07T08:18:10.000 to 2015-11-07T12:29:07.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1162 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1162 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP03T_L3.109",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MOPITT/MOP03T_L3.109. https://asdc.larc.nasa.gov/project/MOPITT.",
-            "issued": "2020-12-23",
-            "temporal": "2018-03-25T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-23",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "air quality",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Helen Worden",
                 "hasEmail": "mailto:hmw@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2103888965-LARC",
             "description": "MOP03T_109 is the Measurements Of Pollution In The Troposphere (MOPITT) Beta CO gridded daily means (Thermal Infrared Radiances) version 109 product. It is an unvalidated beta product subject to recalibration, contains daily mean gridded versions of the daily Level 2 CO profile and total column retrievals. The averaging kernels associated with each retrieval are also gridded and included in the Level 3 files. Version 109 products are beta versions for version 9 products, they are unvalidated beta products subject to recalibration. Data collection for this version is ongoing. \r\rFor a description of the file contents, refer to the File Spec Document. The MOPITT Level 2 Data Quality Statement contains additional information about the quality and the limitations of the retrievals. [From the MOPITT version 3 Level 3 Data Quality Summary] MOPITT was successfully launched into sun-synchronous polar orbit aboard Terra, NASA's first Earth Observing System spacecraft on December 18, 1999. The MOPITT instrument was constructed by a consortium of Canadian companies and funded by the Space Science Division of the Canadian Space Agency.",
-            "graphic-preview-description": "NASA Worldview",
-            "title": "MOPITT Beta CO gridded daily means (Thermal Infrared Radiances) V109",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP03T_L3.109",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP03T_L3.109",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mopitt.physics.utoronto.ca/",
-                    "description": "University of Toronto MOPITT Overview",
                     "@type": "dcat:Distribution",
+                    "description": "University of Toronto MOPITT Overview",
+                    "downloadURL": "https://mopitt.physics.utoronto.ca/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/mopitt",
-                    "description": "U.S. MOPITT project home page",
                     "@type": "dcat:Distribution",
+                    "description": "U.S. MOPITT project home page",
+                    "downloadURL": "https://www2.acom.ucar.edu/mopitt",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.atmosp.physics.utoronto.ca/MOPITT/home.html",
-                    "description": "Canadian MOPITT project home page",
                     "@type": "dcat:Distribution",
+                    "description": "Canadian MOPITT project home page",
+                    "downloadURL": "https://www.atmosp.physics.utoronto.ca/MOPITT/home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/48",
-                    "description": "NASA EOS ATB Documents: MOPITT",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MOPITT",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/48",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/guide/ASDC_MOPITT_Overview_2015.pdf",
-                    "description": "Overview of MOPITT Data at the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MOPITT Data at the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/guide/ASDC_MOPITT_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://terra.nasa.gov/",
-                    "description": "Terra Instrument home page",
                     "@type": "dcat:Distribution",
+                    "description": "Terra Instrument home page",
+                    "downloadURL": "https://terra.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/mopitt_quality_statements.html",
-                    "description": "ASDC List of MOPITT Quality Statements",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MOPITT Quality Statements",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/mopitt_quality_statements.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MOPITT",
-                    "description": "ASDC Data and Information for MOPITT",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MOPITT",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MOPITT",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/on-the-trail-of-global-pollution-drift",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: On The Trail of Global Pollution Drift",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: On The Trail of Global Pollution Drift",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/on-the-trail-of-global-pollution-drift",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/",
-                    "description": "Goddard Earth Sciences Data and Information Services Center (GES DISC): Giovanni - Interactive Visualization and Analysis software",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard Earth Sciences Data and Information Services Center (GES DISC): Giovanni - Interactive Visualization and Analysis software",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/10775/bushfires-raging-in-southeast-australia",
-                    "description": "NASA Earth Observatory Article: Bushfires Raging in Southeast Australia : Natural Hazards\u00a0- Data taken by the Measurements Of Pollution In The Troposphere (MOPITT) instrument aboard NASA's Terra satellite have been combined for 6 days from January 15-20, 2003",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Bushfires Raging in Southeast Australia : Natural Hazards\u00a0- Data taken by the Measurements Of Pollution In The Troposphere (MOPITT) instrument aboard NASA's Terra satellite have been combined for 6 days from January 15-20, 2003",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/10775/bushfires-raging-in-southeast-australia",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/13721/carbon-monoxide-from-tropical-fires",
-                    "description": "NASA Earth Observatory Article: Carbon Monoxide from Tropical Fires : Natural Hazards\u00a0-\u00a0The Terra MOPITT sensor observed large plumes of carbon monoxide produced by biomass burning in South America and Africa in early August 2004.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Carbon Monoxide from Tropical Fires : Natural Hazards\u00a0-\u00a0The Terra MOPITT sensor observed large plumes of carbon monoxide produced by biomass burning in South America and Africa in early August 2004.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/13721/carbon-monoxide-from-tropical-fires",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/19011/fires-and-thick-smoke-over-south-america",
-                    "description": "NASA Earth Observatory Article: Fires and Thick Smoke over South America : Natural Hazards\u00a0-\u00a0Places where MOPITT could not collect enough data to make an estimate of carbon monoxide (probably due to clouds) are gray.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Fires and Thick Smoke over South America : Natural Hazards\u00a0-\u00a0Places where MOPITT could not collect enough data to make an estimate of carbon monoxide (probably due to clouds) are gray.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/19011/fires-and-thick-smoke-over-south-america",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/533/mopitt-first-light-image",
-                    "description": "NASA Earth Observatory Article: MOPITT First Light Image : Image of the Day\u00a0-\u00a0MOPITT measures radiances in several channels to determine the amount of carbon monoxide (CO) and methane in the atmosphere.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT First Light Image : Image of the Day\u00a0-\u00a0MOPITT measures radiances in several channels to determine the amount of carbon monoxide (CO) and methane in the atmosphere.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/533/mopitt-first-light-image",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/852/mopitt-views-carbon-monoxide-concentration",
-                    "description": "NASA Earth Observatory Article: MOPITT Views Carbon Monoxide Concentration, there were widespread wildfires across Montana and Idaho.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT Views Carbon Monoxide Concentration, there were widespread wildfires across Montana and Idaho.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/852/mopitt-views-carbon-monoxide-concentration",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/559/mopitt-views-north-america",
-                    "description": "NASA Earth Observatory Article: MOPITT Views North America : Image of the Day\u00a0-\u00a0Measurement of Pollution in the Troposphere, MOPITT, measures two important pollutants in the Earth's atmosphere\u2014carbon monoxide (CO) and methane.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: MOPITT Views North America : Image of the Day\u00a0-\u00a0Measurement of Pollution in the Troposphere, MOPITT, measures two important pollutants in the Earth's atmosphere\u2014carbon monoxide (CO) and methane.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/559/mopitt-views-north-america",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/nature-s-contribution",
-                    "description": "NASA Earthdata Article: Nature's contribution: Researchers investigate how much wildfires contribute to pollution, and how far this pollution can travel - By Jane Beitler",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Article: Nature's contribution: Researchers investigate how much wildfires contribute to pollution, and how far this pollution can travel - By Jane Beitler",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/nature-s-contribution",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MOPITT",
-                    "description": "NASA Earthdata Forum - MOPITT Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - MOPITT Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MOPITT",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/longstanding-carbon-monoxide-measuring-instrument-mopitt-celebrated/",
-                    "description": "NASA Langley Article: Fourteen Years of Carbon Monoxide from MOPITT, which has truly unlocked a pathway for groundbreaking studies of air pollution transport and atmospheric chemical processes.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Langley Article: Fourteen Years of Carbon Monoxide from MOPITT, which has truly unlocked a pathway for groundbreaking studies of air pollution transport and atmospheric chemical processes.",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/longstanding-carbon-monoxide-measuring-instrument-mopitt-celebrated/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/",
-                    "description": "NASA Worldview",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Worldview",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
-                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
                     "@type": "dcat:Distribution",
+                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
+                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hdfeos.org/zoo/",
-                    "description": "Examples on how to access and visualize various NASA HDF/HDF-EOS files using Python (pyhdf/h5py), NCL, MATLAB\u00ae, and IDL\u00ae, NCL, MATLAB\u00ae, and IDL\u00ae",
                     "@type": "dcat:Distribution",
+                    "description": "Examples on how to access and visualize various NASA HDF/HDF-EOS files using Python (pyhdf/h5py), NCL, MATLAB\u00ae, and IDL\u00ae, NCL, MATLAB\u00ae, and IDL\u00ae",
+                    "downloadURL": "https://hdfeos.org/zoo/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2103888965-LARC",
-                    "description": "Earthdata Search for MOP03T_109 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MOP03T_109 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2103888965-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP03T_L3.109",
-                    "description": "DOI data set landing page for MOP03T_109",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MOP03T_109",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP03T_L3.109",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "graphic-preview-description": "NASA Worldview",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/",
+            "identifier": "C2103888965-LARC",
+            "issued": "2020-12-23",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP03T_L3.109",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-12-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-03-25T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "MOPITT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MOPITT Beta CO gridded daily means (Thermal Infrared Radiances) V109"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/568/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
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
-            "identifier": "DASHLINK_568",
             "description": "These slides were presented at the AePW, April 21-22, 2012. Additional presentations can be found on each of the associated analysis webpages.  Separate pages contain the RSW, BSCW and HIRENASD analysts' presentations.   \r\n\r\nUpdated May 15, 2012 JH",
-            "title": "Workshop Presentations: Overviews",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Agenda_only.pdf",
-                    "description": "Final Agenda (Heeg)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Agenda (Heeg)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Agenda_only.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Agenda_only.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Welcome_and_Overview_v3.pdf",
-                    "description": "Welcome and Overview (Heeg)",
                     "@type": "dcat:Distribution",
+                    "description": "Welcome and Overview (Heeg)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_Welcome_and_Overview_v3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AePW_Welcome_and_Overview_v3.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_OVERVIEW_FINAL.pdf",
-                    "description": "RSW Overview (Perry)",
                     "@type": "dcat:Distribution",
+                    "description": "RSW Overview (Perry)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_OVERVIEW_FINAL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "RSW OVERVIEW FINAL.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_DataMethods_v2.pdf",
-                    "description": "Experimental Data Analysis (Heeg)",
                     "@type": "dcat:Distribution",
+                    "description": "Experimental Data Analysis (Heeg)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AePW_DataMethods_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "AePW_DataMethods_v2.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_ComparisonPlots.pdf",
-                    "description": "RSW Comparison Plots (Schuster)",
                     "@type": "dcat:Distribution",
+                    "description": "RSW Comparison Plots (Schuster)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_ComparisonPlots.pdf",
+                    "mediaType": "application/pdf",
                     "title": "RSW_ComparisonPlots.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/BSCW_Overview_AePW1.pdf",
-                    "description": "BSCW Overview (Scott)",
                     "@type": "dcat:Distribution",
+                    "description": "BSCW Overview (Scott)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/BSCW_Overview_AePW1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "BSCW_Overview_AePW1.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/BSCW_ComparisonPlots_v3.pdf",
-                    "description": "BSCW Comparison Plots",
                     "@type": "dcat:Distribution",
+                    "description": "BSCW Comparison Plots",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/BSCW_ComparisonPlots_v3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "BSCW_ComparisonPlots_v3.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Hirenasd_Boucke.pdf",
-                    "description": "HIRENASD Overview (Boucke)",
                     "@type": "dcat:Distribution",
+                    "description": "HIRENASD Overview (Boucke)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Hirenasd_Boucke.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Hirenasd_Boucke.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_ComparisonPlots_v3.pdf",
-                    "description": "HIRENASD Comparison Plots (Heeg)",
                     "@type": "dcat:Distribution",
+                    "description": "HIRENASD Comparison Plots (Heeg)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/HIRENASD_ComparisonPlots_v3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "HIRENASD_ComparisonPlots_v3.pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/StructuralDynamics_AEPW1_v4.pdf",
-                    "description": "Structural Dynamics HIRENASD (Wieseman)",
                     "@type": "dcat:Distribution",
+                    "description": "Structural Dynamics HIRENASD (Wieseman)",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/StructuralDynamics_AEPW1_v4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "StructuralDynamics_AEPW1_v4.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_568",
+            "issued": "2012-04-29",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/568/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Workshop Presentations: Overviews"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC2-MTP016-V2.0",
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
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT 2 MTP016 phase, which occurred from 2015-05-06 to 2015-06-03 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc2-mtp016-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC2-MTP016-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc2-mtp016-v2.0",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT 2 MTP016 phase, which occurred from 2015-05-06 to 2015-06-03 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 2 MTP016 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 2 MTP016 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985660-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "Sentinel-1B Dual-pol ground projected medium resolution images",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1327985660-ASF",
             "issued": "2016-08-20",
-            "temporal": "2016-04-25T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
             "keyword": [
                 "earth science",
                 "terrestrial hydrosphere",
@@ -989224,278 +989236,280 @@
                 "erosion/sedimentation",
                 "surface water"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985660-ASF.html",
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
-            "identifier": "C1327985660-ASF",
-            "description": "Sentinel-1B Dual-pol ground projected medium resolution images",
-            "title": "SENTINEL-1B_DUAL_POL_GRD_MEDIUM_RES",
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
+            "title": "SENTINEL-1B_DUAL_POL_GRD_MEDIUM_RES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA1002",
             "citation": "Jarnot, R. and Perun, V.. 2015-02-19. ML1RADD. Version 004. MLS/Aura L1 Radiances from Digital Autocorrelators V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA1002. https://disc.gsfc.nasa.gov/datacollection/ML1RADD_004.html. Digital Science Data.",
-            "issued": "2014-10-21",
-            "temporal": "2004-08-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-10-21",
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATHANIEL LIVESEY",
                 "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
             },
+            "creator": "Jarnot, R. and Perun, V.",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1265737438-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "ML1RADD is the EOS Aura Microwave Limb Sounder (MLS) product containing the level 1 radiances from the digital autocorrelators. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), and files contain a full days worth of data (15 orbits). Users of the ML1RADD data product should read the 'A Short Guide to the Use and Interpretation of v4.2x Level 1 Data' document for additional information.\n\nThe data are stored in the version 5 Hierarchical Data Format, or HDF-5. Each file contains radiances and ancillary information written as HDF-5 dataset objects (n-dimensional arrays), along with file attributes and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML1RADD",
-            "creator": "Jarnot, R. and Perun, V.",
-            "title": "MLS/Aura L1 Radiances from Digital Autocorrelators V004 (ML1RADD) at GES DISC",
-            "graphic-preview-description": "Aura MLS logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADD_004.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA1002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA1002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADD_004.jpeg",
-                    "description": "Aura MLS logo",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADD_004.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML1RADD_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML1RADD_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level1/ML1RADD.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level1/ML1RADD.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML1RADD_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML1RADD_004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/Level_1_ReadMe_v4.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/Level_1_ReadMe_v4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
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
+            "graphic-preview-description": "Aura MLS logo",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADD_004.jpeg",
+            "identifier": "C1265737438-GES_DISC",
+            "issued": "2014-10-21",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA1002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-10-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML1RADD",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura L1 Radiances from Digital Autocorrelators V004 (ML1RADD) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-2-JUPITER-V1.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-2-jupiter-v1.0_jq89-g5aw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-2-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-2-jupiter-v1.0_jq89-g5aw",
-            "description": "This data set contains Raw data taken by the New Horizons Solar Wind Around Pluto instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS SWAP JUPITER ENCOUNTER V1.0",
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
+            "title": "NEW HORIZONS SWAP JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/46IY83E4HHJU",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SASS Twice-Daily SIR-Enhanced EASE-Grid 2.0 Radar Backscatter V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/46IY83E4HHJU.",
-            "issued": "1978-07-07",
-            "temporal": "1978-07-07T00:00:00Z/1978-10-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1978-10-10",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C3065845408-NSIDC_ECS",
             "description": "This product contains twice-daily radar backscatter data collected at 14.6 GHz for horizontal-horizontal and vertical-vertical receive radar channels from the SeaSat-A satellite scatterometer (SASS) sensor. Data are available on the Northern Hemisphere, Southern Hemisphere, and Temperate EASE-Grid 2.0 projections as either 25 km or 3.125 km resolution grids. The data set uses the drop-in-the bucket gridding (GRD) and Scatterometer Image Reconstruction (SIR) algorithms to process the individual swath-based data into twice-daily morning and evening images. The GRD algorithm produces SAR images (high-resolution) on a 25 km grid and the SIR algorithm produces slice and footprint images (both lower-resolution) on a 3.125 km grid, provided at 8-,16-, 32-day imaging intervals. The data coverage is global from 7 July 1978 through 10 Oct 1978.",
-            "title": "SASS Twice-Daily SIR-Enhanced EASE-Grid 2.0 Radar Backscatter V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F46IY83E4HHJU",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F46IY83E4HHJU",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/OTHR/NSIDC-0787.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/OTHR/NSIDC-0787.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0787+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0787+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0787/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0787/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/46IY83E4HHJU",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/46IY83E4HHJU",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/46IY83E4HHJU",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/46IY83E4HHJU",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3065845408-NSIDC_ECS",
+            "issued": "1978-07-07",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/46IY83E4HHJU",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1978-10-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-07-07T00:00:00Z/1978-10-10T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASS Twice-Daily SIR-Enhanced EASE-Grid 2.0 Radar Backscatter V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition43/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "Press kit for ISS mission Expedition 43 from 11/2014-06/2015. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Press Kit PDF",
+                    "downloadURL": "http://www.nasa.gov/sites/default/files/atoms/files/np-2015-03-011-jsc-expedition-43-summary.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "ISS 43 Press Kit"
+                }
+            ],
+            "identifier": "OCIO-Fitara-53",
             "issued": "2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "schedule",
                 "43",
@@ -989508,119 +989522,107 @@
                 "crew",
                 "expedition"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition43/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "JSC"
             },
-            "identifier": "OCIO-Fitara-53",
-            "description": "Press kit for ISS mission Expedition 43 from 11/2014-06/2015. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
-            "title": "ISS Expedition 43 Press Kit",
-            "programCode": [
-                "026:037"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/sites/default/files/atoms/files/np-2015-03-011-jsc-expedition-43-summary.pdf",
-                    "description": "Press Kit PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS 43 Press Kit"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ISS Expedition 43 Press Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-3-FGM-CAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the Juno FGM calibrated orbital observations. The FGM sensor block uses two miniature ring-core fluxgate sensors to measure the magnetic field in three components of the vector field. There are multiple FGM data products to accomodate different coordinate systems.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-3-fgm-cal-v1.0_jqdd-9nf3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "solar system",
                 "earth",
                 "jupiter",
                 "juno"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-3-FGM-CAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-3-fgm-cal-v1.0_jqdd-9nf3",
-            "description": "Abstract ======== This data set consists of the Juno FGM calibrated orbital observations. The FGM sensor block uses two miniature ring-core fluxgate sensors to measure the magnetic field in three components of the vector field. There are multiple FGM data products to accomodate different coordinate systems.",
-            "title": "JUNO J FLUXGATE MAGNETOMETER\nCALIBRATED DATA V1.0",
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
+            "title": "JUNO J FLUXGATE MAGNETOMETER\nCALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-CHEMCAM-RMI-5-RDR-V1.0",
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
-                "mars science laboratory",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The MSL ChemCam RMI RDR data set consists of radiometrically and geometrically calibrated images acquired by the ChemCam Remote Micro-Imager on the Mars Science Laboratory rover.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-chemcam-rmi-5-rdr-v1.0_jqe7-98k3",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-CHEMCAM-RMI-5-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-chemcam-rmi-5-rdr-v1.0_jqe7-98k3",
-            "description": "The MSL ChemCam RMI RDR data set consists of radiometrically and geometrically calibrated images acquired by the ChemCam Remote Micro-Imager on the Mars Science Laboratory rover.",
-            "title": "MSL MARS CHEMCAM REMOTE MICRO-IMAGER CAMERA 5 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL MARS CHEMCAM REMOTE MICRO-IMAGER CAMERA 5 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FJ%2FM-ALICE-3-MARS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Mars swing-by phase of the Rosetta mission, which occurred 2006-07-29 to 2007-05-28. Data include the calibration observations of payload checkout (PC) 4, observations of Mars, and observations of Jupiter and the Io plasma torus.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-j-m-alice-3-mars-v1.0_jqec-jvau",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "calibration",
@@ -989628,1409 +989630,1388 @@
                 "mars",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FJ%2FM-ALICE-3-MARS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-j-m-alice-3-mars-v1.0_jqec-jvau",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Mars swing-by phase of the Rosetta mission, which occurred 2006-07-29 to 2007-05-28. Data include the calibration observations of payload checkout (PC) 4, observations of Mars, and observations of Jupiter and the Io plasma torus.",
-            "title": "ROSETTA-ORBITER CAL/JUPITER/MARS ALICE 3 MARS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL/JUPITER/MARS ALICE 3 MARS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PWS-2-REFDR-GSAFULL-V1.0",
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
-                "galileo",
-                "gaspra"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes full resolution electric and magnetic wave spectra obtained during a ~ 2-hour period of contiguous observations near the closest approach to Gaspra and a number of non-contiguous spectra taken prior and subsequent to closest approach.  In addition waveform survey data (uncalibrated) and all instrument housekeeping data are included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pws-2-refdr-gsafull-v1.0_jqex-42zh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "gaspra"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PWS-2-REFDR-GSAFULL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pws-2-refdr-gsafull-v1.0_jqex-42zh",
-            "description": "This data set includes full resolution electric and magnetic wave spectra obtained during a ~ 2-hour period of contiguous observations near the closest approach to Gaspra and a number of non-contiguous spectra taken prior and subsequent to closest approach.  In addition waveform survey data (uncalibrated) and all instrument housekeeping data are included.",
-            "title": "GO A PWS REFORMATTED GASPRA SPECTRUM ANALYZER FULL V1.0",
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
+            "title": "GO A PWS REFORMATTED GASPRA SPECTRUM ANALYZER FULL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SARGASSUM_GOM/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SARGASSUM_GOM/DATA001.",
-            "issued": "2017-07-20",
-            "temporal": "2017-07-20T19:25:00Z/2023-04-17T00:00:00Z",
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
-            "identifier": "C1633360637-OB_DAAC",
             "description": "Measurements made under the Linking habitat to recruitment: evaluating the importance of pelagic Sargassum to fisheries management in the Gulf of Mexico, in the Northern Gulf of Mexico. Collaboration with USF and USM.",
-            "title": "Importance of pelagic Sargassum to fisheries management in the Northern Gulf of Mexico",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSARGASSUM_GOM%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSARGASSUM_GOM%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Sargassum_GOM/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Sargassum_GOM/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360637-OB_DAAC",
+            "issued": "2017-07-20",
+            "keyword": [
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SARGASSUM_GOM/DATA001",
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
+            "temporal": "2017-07-20T19:25:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Importance of pelagic Sargassum to fisheries management in the Northern Gulf of Mexico"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR1-RAW-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "2010-07-30 SBN:T.Barnes Updated and DATA_SET_DESCThis dataset contains EDITED RAW DATA of the first Earth Flyby (EAR1). Included are the data of the very Flyby from March 1 until March 7 and the data of the Passive Checkout (PC0) at March 29. (Version 3.0 is the first version archived.)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear1-raw-v3.0_jqgu-6pb7",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "unknown",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR1-RAW-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear1-raw-v3.0_jqgu-6pb7",
-            "description": "2010-07-30 SBN:T.Barnes Updated and DATA_SET_DESCThis dataset contains EDITED RAW DATA of the first Earth Flyby (EAR1). Included are the data of the very Flyby from March 1 until March 7 and the data of the Passive Checkout (PC0) at March 29. (Version 3.0 is the first version archived.)",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR1 RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR1 RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-SW-MISCHA-3-RDR-CRUISE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "On Dec 15, 1984, the Vega spacecraft was launched to first flyby Venus at which time landers were released and then continue to a flyby of Halley. The magnetic field experiments MISCHA carried four fluxgate sensors, with three sensors mounted on a boom at the end of the solar panels and the fourth sensor mounted one meter closer. During the cruise phase, the TRASSA-1 mode of the instrument (1 vector/2.5 min) was used. The sensors were switched to the TRASSA-2 mode (1 vector/min) during the flyby which started roughly two days before the encounter. From 3 h before closest approach (CA) until 1 hour after CA, the HS-mode 1 vector/6s) and the DT-mode (1 vector/100ms) was used [DELVAETAL1991].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-sw-mischa-3-rdr-cruise-v1.0_jqmi-uy8a",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "halley",
                 "vega 1",
                 "1p/halley 1 (1682 q1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-SW-MISCHA-3-RDR-CRUISE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-sw-mischa-3-rdr-cruise-v1.0_jqmi-uy8a",
-            "description": "On Dec 15, 1984, the Vega spacecraft was launched to first flyby Venus at which time landers were released and then continue to a flyby of Halley. The magnetic field experiments MISCHA carried four fluxgate sensors, with three sensors mounted on a boom at the end of the solar panels and the fourth sensor mounted one meter closer. During the cruise phase, the TRASSA-1 mode of the instrument (1 vector/2.5 min) was used. The sensors were switched to the TRASSA-2 mode (1 vector/min) during the flyby which started roughly two days before the encounter. From 3 h before closest approach (CA) until 1 hour after CA, the HS-mode 1 vector/6s) and the DT-mode (1 vector/100ms) was used [DELVAETAL1991].",
-            "title": "VEGA1 CRUISE MAGNETOMETER DATA",
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
+            "title": "VEGA1 CRUISE MAGNETOMETER DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-ESC1-CALIB2-V1.0",
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
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 1\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains instrument outputs in\nvolts and amperes, calibrated and corrected for instrument offsets. This\nversion reorganizes the data into fewer files with longer time series\nand sorted by type of measurement. The version number starts over from\nV1.0 due to a change in naming convention.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-esc1-calib2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-3-ESC1-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-3-esc1-calib2-v1.0",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 1\nmission phase where the primary target was the comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1). It contains instrument outputs in\nvolts and amperes, calibrated and corrected for instrument offsets. This\nversion reorganizes the data into fewer files with longer time series\nand sorted by type of measurement. The version number starts over from\nV1.0 due to a change in naming convention.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 3\nESC1 CALIB2 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RPCLAP 3\nESC1 CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/AST14DMO.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. 2007-02-26. AST14DMO.003. ASTER On-Demand L3 DEM and Orthorectified Images, GeoTIF Format. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ASTER/AST14DMO.003. https://doi.org/10.5067/ASTER/AST14DMO.003. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2007-02-26",
-            "temporal": "2000-03-06T00:30:05Z/2024-12-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-28",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "infrared wavelengths",
-                "national geospatial data asset",
-                "ngda",
-                "spectral/engineering",
-                "topography",
-                "visible wavelengths"
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
-            "identifier": "C1299783651-LPDAAC_ECS",
-            "description": "The ASTER Digital Elevation Model and Orthorectified Registered Radiance at the Sensor (AST14DMO) product (https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf) form a multi-file product. The product contains both a Digital Elevation Model (DEM) and up to 15 orthorectified images representing Visible and Near Infrared (VNIR), Shortwave Infrared (SWIR), and Thermal Infrared (TIR) data layers for each available ASTER scene, if acquired. The spatial resolution is 15 m (VNIR), 30 m (SWIR), and 90 m (TIR) with a temporal coverage of 2000 to present.\r\n\r\nFor more information, see the links below:\r\n\r\n(AST14DEM) (https://doi.org/10.5067/ASTER/AST14DEM.003)\r\n(AST14OTH) (https://doi.org/10.5067/ASTER/AST14OTH.003)\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\nAs of January 2021, the LP DAAC has implemented version 3.0 of the Sensor Information Laboratory Corporation ASTER DEM/Ortho (SILCAST) software, which is used to generate the Level 2 on-demand ASTER Orthorectified and Digital Elevation Model (DEM) products (AST14). The updated software provides digital elevation extraction and orthorectification from ASTER L1B input data without needing to enter ground control points or depending on external global DEMs at 30-arc-second resolution (GTOPO30). It utilizes the ephemeris and attitude data derived from both the ASTER instrument and the Terra spacecraft platform. The outputs are geoid height-corrected and waterbodies are automatically detected in this version. Users will notice differences between AST14DEM, AST14DMO, and AST14OTH products ordered before January 2021 (generated with SILCAST V1) and those generated with the updated version of the production software (version 3.0). Differences may include slight elevation changes over different surface types, including waterbodies. Differences have also been observed over cloudy portions of ASTER scenes. Additional information on SILCAST version 3.0 can be found on the SILCAST website (http://www.silc.co.jp/en/products.html).\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "AST14DMO.003",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER Orthorectified Digital Elevation Model (DEM) V003",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_029_047.1.VNIR.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ASTER Digital Elevation Model and Orthorectified Registered Radiance at the Sensor (AST14DMO) product (https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf) form a multi-file product. The product contains both a Digital Elevation Model (DEM) and up to 15 orthorectified images representing Visible and Near Infrared (VNIR), Shortwave Infrared (SWIR), and Thermal Infrared (TIR) data layers for each available ASTER scene, if acquired. The spatial resolution is 15 m (VNIR), 30 m (SWIR), and 90 m (TIR) with a temporal coverage of 2000 to present.\r\n\r\nFor more information, see the links below:\r\n\r\n(AST14DEM) (https://doi.org/10.5067/ASTER/AST14DEM.003)\r\n(AST14OTH) (https://doi.org/10.5067/ASTER/AST14OTH.003)\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\nAs of January 2021, the LP DAAC has implemented version 3.0 of the Sensor Information Laboratory Corporation ASTER DEM/Ortho (SILCAST) software, which is used to generate the Level 2 on-demand ASTER Orthorectified and Digital Elevation Model (DEM) products (AST14). The updated software provides digital elevation extraction and orthorectification from ASTER L1B input data without needing to enter ground control points or depending on external global DEMs at 30-arc-second resolution (GTOPO30). It utilizes the ephemeris and attitude data derived from both the ASTER instrument and the Terra spacecraft platform. The outputs are geoid height-corrected and waterbodies are automatically detected in this version. Users will notice differences between AST14DEM, AST14DMO, and AST14OTH products ordered before January 2021 (generated with SILCAST V1) and those generated with the updated version of the production software (version 3.0). Differences may include slight elevation changes over different surface types, including waterbodies. Differences have also been observed over cloudy portions of ASTER scenes. Additional information on SILCAST version 3.0 can be found on the SILCAST website (http://www.silc.co.jp/en/products.html).\r\n\r\nStarting June 23, 2021, radiometric calibration coefficient Version 5 (RCC V5) will be applied to newly observed ASTER data and archived ASTER data products. Details regarding RCC V5 are described in the following journal article.\r\n\r\nTsuchida, S., Yamamoto, H., Kouyama, T., Obata, K., Sakuma, F., Tachikawa, T., Kamei, A., Arai, K., Czapla-Myers, J.S., Biggar, S.F., and Thome, K.J., 2020, Radiometric Degradation Curves for the ASTER VNIR Processing Using Vicarious and Lunar Calibrations: Remote Sensing, v. 12, no. 3, at https://doi.org/10.3390/rs12030427.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST14DMO.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FAST14DMO.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asterweb.jpl.nasa.gov/",
-                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER home page is maintained through NASA's Jet Propulsion Laboratory and documents various aspects of the ASTER mission.",
+                    "downloadURL": "https://asterweb.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/AST14DMO.003",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/AST14DMO.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1299783651-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1299783651-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/81/AST14_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/81/AST14_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/69/AST_L1_User_Guide_V3.pdf",
-                    "description": "ASTER Level-1 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Level-1 User Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/69/AST_L1_User_Guide_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/80/AST14_User_Guide_V3.pdf",
-                    "description": "ASTER Higher-Level Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Higher-Level Product User Guide",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/80/AST14_User_Guide_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf",
-                    "description": "ASTER Order Instructions",
                     "@type": "dcat:Distribution",
+                    "description": "ASTER Order Instructions",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/996/ASTER_Earthdata_Search_Order_Instructions.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_029_047.1.VNIR.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_029_047.1.VNIR.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1010/ASTER_User_Handbook_v3.pdf",
-                    "description": "The ASTER User Handbook provides in depth information on ASTER data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ASTER User Handbook provides in depth information on ASTER data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1010/ASTER_User_Handbook_v3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2021.06.16/pg-BR1A0000-2021061601_029_047.1.VNIR.jpg",
+            "identifier": "C1299783651-LPDAAC_ECS",
+            "issued": "2007-02-26",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "infrared wavelengths",
+                "national geospatial data asset",
+                "ngda",
+                "spectral/engineering",
+                "topography",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/AST14DMO.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "AST14DMO.003",
             "spatial": "-180.0 -83.0 180.0 83.0",
+            "temporal": "2000-03-06T00:30:05Z/2024-12-16T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER Orthorectified Digital Elevation Model (DEM) V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD13A4N.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-02-07. MODIS/Terra Vegetation Indices Daily Rolling-8-Day L3 Global 500m SIN Grid NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD13A4N.NRT.061.",
-            "issued": "2021-02-07",
-            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "ngda",
-                "surface radiative properties",
-                "earth science",
-                "vegetation",
-                "land surface",
-                "biosphere",
-                "national geospatial data asset"
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
-            "identifier": "C2007657679-LANCEMODIS",
-            "description": "The MODIS level-3 Vegetation Indices Daily Rolling-8-Day Near Real Time (NRT), MOD13A4N data are provided everyday at 500-meter spatial resolution as a gridded level-3 product in the Sinusoidal projection. Vegetation indices are used for global monitoring of vegetation conditions and are used in products displaying land cover and land cover changes. These data may be used as input for modeling global biogeochemical and hydrologic processes and global and regional climate. These data also may be used for characterizing land surface biophysical properties and processes including primary production and land cover conversion.\r\n\r\nNote: This is a near real-time product only. Standard historical data and imagery for MOD13Q4N (250m) and MOD13A4N (500m) are not available. Users can either use the NDVI standard products from LAADS web (https://ladsweb.modaps.eosdis.nasa.gov/search/) or access the science quality MxD09[A1/Q1] data and create the NDVI product of their own.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Terra Vegetation Indices Daily Rolling-8-Day L3 Global 500m SIN Grid NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS level-3 Vegetation Indices Daily Rolling-8-Day Near Real Time (NRT), MOD13A4N data are provided everyday at 500-meter spatial resolution as a gridded level-3 product in the Sinusoidal projection. Vegetation indices are used for global monitoring of vegetation conditions and are used in products displaying land cover and land cover changes. These data may be used as input for modeling global biogeochemical and hydrologic processes and global and regional climate. These data also may be used for characterizing land surface biophysical properties and processes including primary production and land cover conversion.\r\n\r\nNote: This is a near real-time product only. Standard historical data and imagery for MOD13Q4N (250m) and MOD13A4N (500m) are not available. Users can either use the NDVI standard products from LAADS web (https://ladsweb.modaps.eosdis.nasa.gov/search/) or access the science quality MxD09[A1/Q1] data and create the NDVI product of their own.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD13A4N.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD13A4N.NRT.061",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD13A4N/",
-                    "description": "Direct access to the download site and directory hosting the MOD13A4N 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD13A4N 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD13A4N/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C2007657679-LANCEMODIS",
+            "issued": "2021-02-07",
+            "keyword": [
+                "ngda",
+                "surface radiative properties",
+                "earth science",
+                "vegetation",
+                "land surface",
+                "biosphere",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD13A4N.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -81.0 180.0 81.0",
+            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "CWIC",
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Vegetation Indices Daily Rolling-8-Day L3 Global 500m SIN Grid NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4JW8BSC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2007-12-31. National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 2 (PLACE II). Version 2.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4JW8BSC. https://doi.org/10.7927/H4JW8BSC.",
-            "issued": "2007-12-31",
-            "temporal": "1990-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4PN93H3",
-                "https://doi.org/10.7927/H4F769GP"
-            ],
-            "keyword": [
-                "human dimensions",
-                "boundaries",
-                "topography",
-                "land surface",
-                "population",
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
-            "identifier": "C179001708-SEDAC",
-            "description": "The National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 2 (PLACE II) data set contains estimates of national-level aggregations of territorial extent and population size by biome, climate zone, coastal proximity zone, elevation zone, and population density zone, a compendium of nearly 300 variables for 228 countries. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 2 (PLACE II)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 2 (PLACE II) data set contains estimates of national-level aggregations of territorial extent and population size by biome, climate zone, coastal proximity zone, elevation zone, and population density zone, a compendium of nearly 300 variables for 228 countries. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4JW8BSC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4JW8BSC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nagdc/nagdc-population-landscape-climate-estimates-v2/global-population-density-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nagdc/nagdc-population-landscape-climate-estimates-v2/global-population-density-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/nagdc-population-landscape-climate-estimates-v2/maps",
+            "identifier": "C179001708-SEDAC",
+            "issued": "2007-12-31",
+            "keyword": [
+                "human dimensions",
+                "boundaries",
+                "topography",
+                "land surface",
+                "population",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4JW8BSC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4PN93H3",
+                "https://doi.org/10.7927/H4F769GP"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1990-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "NAGDC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Aggregates of Geospatial Data Collection: Population, Landscape, And Climate Estimates, Version 2 (PLACE II)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/FPSU0V1MWUB6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs BedMachine Antarctica V003. Version 3. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/FPSU0V1MWUB6.",
-            "issued": "1970-01-01",
-            "temporal": "1970-01-01T00:00:00Z/2019-10-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "topography",
-                "land surface",
-                "glaciers/ice sheets",
-                "bathymetry/seafloor topography",
-                "earth science",
-                "cryospheric indicators",
-                "cryosphere",
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
-            "identifier": "C2509060594-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, contains a bed topography/bathymetry map of Antarctica based on mass conservation, streamline diffusion, and other methods. The data set also includes ice thickness, surface elevation, an ice/ocean/land mask, ice thickness estimation errors, and a map showing where each method was utilized.",
-            "title": "MEaSUREs BedMachine Antarctica V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFPSU0V1MWUB6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFPSU0V1MWUB6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0756.003/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0756.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0756+V003",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0756+V003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0756/versions/3/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0756/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FPSU0V1MWUB6",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/FPSU0V1MWUB6",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FPSU0V1MWUB6",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/FPSU0V1MWUB6",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2509060594-NSIDC_ECS",
+            "issued": "1970-01-01",
+            "keyword": [
+                "oceans",
+                "topography",
+                "land surface",
+                "glaciers/ice sheets",
+                "bathymetry/seafloor topography",
+                "earth science",
+                "cryospheric indicators",
+                "cryosphere",
+                "climate indicators"
+            ],
+            "landingPage": "https://doi.org/10.5067/FPSU0V1MWUB6",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "1970-01-01T00:00:00Z/2019-10-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs BedMachine Antarctica V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/612/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-08-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
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
-            "identifier": "DASHLINK_612",
             "description": "Results for the DXC'11 Industrial Track, Diagnostic Problem I (no entries for DP II).",
-            "title": "DXC'11 Results",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC11_DPI_ScenarioResults20110915.zip",
-                    "description": "Scenario Output for Each Diagnostic Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "Scenario Output for Each Diagnostic Algorithm",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC11_DPI_ScenarioResults20110915.zip",
+                    "mediaType": "application/zip",
                     "title": "DXC11_DPI_ScenarioResults20110915.zip"
                 },
                 {
-                    "mediaType": "text/plain",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC11_DPI_EvaluatorResults20111003.txt",
-                    "description": "Evaluator Results for Diagnostic Problem I",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluator Results for Diagnostic Problem I",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC11_DPI_EvaluatorResults20111003.txt",
+                    "mediaType": "text/plain",
                     "title": "DXC11_DPI_EvaluatorResults20111003.txt"
                 },
                 {
-                    "mediaType": "application/unknown",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC11_DPI_ResultsSummary20110915.pdf",
-                    "description": "Results Summary for Diagnostic Problem I",
                     "@type": "dcat:Distribution",
+                    "description": "Results Summary for Diagnostic Problem I",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/DXC11_DPI_ResultsSummary20110915.pdf",
+                    "mediaType": "application/unknown",
                     "title": "DXC11_DPI_ResultsSummary20110915.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_612",
+            "issued": "2012-08-29",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/612/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "DXC'11 Results"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1051",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hamilton, S.K., S.J. Sippel, and J.M. Melack. 2011. LBA-ECO LC-07 Monthly Inundated Areas, Amazon, Orinoco and Pantanal Basins: 1978-1987. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1051",
-            "issued": "2023-10-03",
-            "temporal": "1978-12-01T00:00:00Z/1987-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-09",
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
-                "surface water",
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
-            "identifier": "C2779739356-ORNL_CLOUD",
             "description": "This data set reports the monthly record of inundated area, in square km, for six floodplain and open water regions in South America. The following floodplains were analyzed: (1) mainstem Amazon River floodplain in Brazil; (2) Llanos de Mojos (Beni and Mamore rivers) in Bolivia; (3) Bananal Island (Araguaia River) in Brazil; (4) Roraima savannas (Branco and Rupununi rivers) in Brazil and Guyana; (5) Llanos del Orinoco (Apure and Meta rivers) in Venezuela and Colombia; and (6) Pantanal wetland (Paraguay River) in Brazil. Flooded area was estimated at monthly intervals from December 1978 through August 1987 for the Amazon mainstem region and from January 1979 through August 1987 for the other five regions. Inundated area was determined from SMMR (Scanning Multichannel Microwave Radiometer) passive microwave data. Area estimates include permanent open water as well as land subject to seasonal inundation. This data set contains five data files: two comma-delimited (.csv) ASCII data files providing the monthly inundation area values for six floodplain and open water regions in South America; a compressed (.zip) file providing seventeen ESRI Shape files for the region bounding polygons; and two .csv files providing information about the region bounding polygons and latitude/longitude verticies.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-07 Monthly Inundated Areas, Amazon, Orinoco and Pantanal Basins: 1978-1987",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1051",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1051",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC07_SMMR_Inundated_Area/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC07_SMMR_Inundated_Area/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC07_SMMR_Inundated_Area.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC07_SMMR_Inundated_Area.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1051",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1051",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_SMMR_Inundated_Area/comp/LC07_SMMR_Inundated_Area.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_SMMR_Inundated_Area/comp/LC07_SMMR_Inundated_Area.pdf",
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
+            "identifier": "C2779739356-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "surface water",
+                "land use/land cover",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1051",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-80.0 -21.0 -35.0 10.0",
+            "temporal": "1978-12-01T00:00:00Z/1987-08-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-07 Monthly Inundated Areas, Amazon, Orinoco and Pantanal Basins: 1978-1987"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-MAG-4-SUMM-L1COORDS-9.60SEC-V1.0",
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
+            "description": "This data set includes calibrated magnetic field data acquired by the Voyager 1 Low Field Magnetometer (LFM) during the Saturn encounter. Coverage begins in the solar wind inbound to Saturn and continues past the last outbound bowshock crossing. The data are in Kronographic (L1) coordinates and have been averaged from the 1.92 second summary rate to a 9.6 second sample rate. All magnetic field measurements are given in nanoTesla (nT). The magnetic field data are calibrated (see the calibration description included in the Voyager 1 Magnetometer instrument catalog file for details).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-mag-4-summ-l1coords-9.60sec-v1.0_jqsn-z4b6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-MAG-4-SUMM-L1COORDS-9.60SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-mag-4-summ-l1coords-9.60sec-v1.0_jqsn-z4b6",
-            "description": "This data set includes calibrated magnetic field data acquired by the Voyager 1 Low Field Magnetometer (LFM) during the Saturn encounter. Coverage begins in the solar wind inbound to Saturn and continues past the last outbound bowshock crossing. The data are in Kronographic (L1) coordinates and have been averaged from the 1.92 second summary rate to a 9.6 second sample rate. All magnetic field measurements are given in nanoTesla (nT). The magnetic field data are calibrated (see the calibration description included in the Voyager 1 Magnetometer instrument catalog file for details).",
-            "title": "VG1 SAT MAG RESAMPLED KRONOGRAPHIC (L1)\n                                      COORDS 9.6SEC V1.0",
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
+            "title": "VG1 SAT MAG RESAMPLED KRONOGRAPHIC (L1)\n                                      COORDS 9.6SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MB-4-SUMSPEC-SCI-V1.0",
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
+            "description": "This archive contains Mars Exploration Rover Moessbauer Summed Spectra Reduced Data Record (RDR) products and ancillary files. Each product has a detached PDS label that describes the file structure and instrument parameters used for that image. The products archived on this volume were generated by the Moessbauer instrument team from Moessbauer EDR (Experiment Data Record) products. Supporting documentation and label files conform to the Planetary Data System (PDS) Standards, Version 3.6, Jet Propulsion Laboratory (JPL) document number D-7669.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mb-4-sumspec-sci-v1.0_jqsx-eshi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MB-4-SUMSPEC-SCI-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mb-4-sumspec-sci-v1.0_jqsx-eshi",
-            "description": "This archive contains Mars Exploration Rover Moessbauer Summed Spectra Reduced Data Record (RDR) products and ancillary files. Each product has a detached PDS label that describes the file structure and instrument parameters used for that image. The products archived on this volume were generated by the Moessbauer instrument team from Moessbauer EDR (Experiment Data Record) products. Supporting documentation and label files conform to the Planetary Data System (PDS) Standards, Version 3.6, Jet Propulsion Laboratory (JPL) document number D-7669.",
-            "title": "MER 1 MOESSBAUER 4 SUMMED SPECTRA RDR SCIENCE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MOESSBAUER 4 SUMMED SPECTRA RDR SCIENCE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP03IMG_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2021-12-31. VIIRS/NPP Imagery Resolution Terrain-Corrected Geolocation L1 6-Min Swath 375m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VNP03IMG_NRT.002. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt.",
-            "issued": "2021-12-15",
-            "temporal": "2021-12-15T00:00:00Z/2024-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "spectral/engineering",
-                "sensor characteristics",
-                "visible wavelengths",
-                "earth science",
-                "platform characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Guoqing \"Gary\" Lin",
                 "hasEmail": "mailto:guoqing.lin-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2185522599-LANCEMODIS",
-            "description": "The VIIRS/NPP Imagery Resolution Terrain-Corrected Geolocation 6-Min L1 Swath 375m Near Real Time (NRT) product, short-name VNP03IMG includes the geolocation fields that are calculated for each VIIRS imagery resolution band (I-band) Line of sight (LOS) for all orbits at the nominal resolution of 375 m. The locations and ancillary information correspond to the intersection of the centers of each Field of View (FOV) from 32 detectors in an ideal I-band on the Earth's surface. A digital terrain model is used to model the Earth's surface. The main inputs are the spacecraft attitude and orbit ephemeris data, the instrument telemetry and the digital elevation model. The geolocation fields contained within the VNP03IMG Geolocation files include geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, satellite zenith and azimuth angles, and a land/water mask for each 375m sample. Additional information is included in the header to enable the calculation of the approximate location of the center of the detectors for any of the VIIRS bands. This product is used as input by a large number of subsequent VIIRS Imagery Resolution products, particularly those produced by the Land team.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/NPP Imagery Resolution Terrain-Corrected Geolocation 6-Min L1 Swath 375m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NPP Imagery Resolution Terrain-Corrected Geolocation 6-Min L1 Swath 375m Near Real Time (NRT) product, short-name VNP03IMG includes the geolocation fields that are calculated for each VIIRS imagery resolution band (I-band) Line of sight (LOS) for all orbits at the nominal resolution of 375 m. The locations and ancillary information correspond to the intersection of the centers of each Field of View (FOV) from 32 detectors in an ideal I-band on the Earth's surface. A digital terrain model is used to model the Earth's surface. The main inputs are the spacecraft attitude and orbit ephemeris data, the instrument telemetry and the digital elevation model. The geolocation fields contained within the VNP03IMG Geolocation files include geodetic latitude, longitude, surface height above the geoid, solar zenith and azimuth angles, satellite zenith and azimuth angles, and a land/water mask for each 375m sample. Additional information is included in the header to enable the calculation of the approximate location of the center of the detectors for any of the VIIRS bands. This product is used as input by a large number of subsequent VIIRS Imagery Resolution products, particularly those produced by the Land team.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP03IMG_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP03IMG_NRT.002",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP03IMG_NRT",
-                    "description": "Direct access to the download site and directory hosting the VNP03IMG_NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the VNP03IMG_NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP03IMG_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2185522599-LANCEMODIS",
+            "issued": "2021-12-15",
+            "keyword": [
+                "spectral/engineering",
+                "sensor characteristics",
+                "visible wavelengths",
+                "earth science",
+                "platform characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP03IMG_NRT.002",
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
+            "temporal": "2021-12-15T00:00:00Z/2024-09-30T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Imagery Resolution Terrain-Corrected Geolocation 6-Min L1 Swath 375m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1051-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-23T09:47:45.000 to 2015-09-23T17:32:52.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1051-v1.0_jqut-6kd8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1051-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1051-v1.0_jqut-6kd8",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-23T09:47:45.000 to 2015-09-23T17:32:52.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1051 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1051 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-09-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_jValue_AircraftInSitu_DC8_Data_1.",
-            "issued": "2021-03-19",
-            "temporal": "2013-08-02T00:00:00Z/2013-09-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
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
-            "identifier": "C2119341667-LARC_ASDC",
             "description": "SEAC4RS_jValue_AircraftInSitu_DC8_Data are in-situ photolysis rate (j value) data collected onboard the DC8 aircraft during the Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEA4CRS) airborne field study. Data collection for this product is complete.\r\n\r\nStudies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEAC4RS) airborne field study was conducted in August and September of 2013. The field operation was based in Houston, Texas. The primary SEAC4RS science objectives are: to determine how pollutant emissions are redistributed via deep convection throughout the troposphere; to determine the evolution of gases and aerosols in deep convective outflow and the implications for UT/LS chemistry; to identify the influences and feedbacks of aerosol particles from anthropogenic pollution and biomass burning on meteorology and climate through changes in the atmospheric heat budget (i.e., semi-direct effect) or through microphysical changes in clouds (i.e., indirect effects); and lastly, to serve as a calibration and validation test bed for future satellite instruments and missions.\r\n\r\nThe airborne observational data were collected from three aircraft platforms: the NASA DC-8, ER-2, and SPEC LearJet. Both the NASA DC-8 and ER-2 aircraft were instrumented for comprehensive in-situ and remote sensing measurements of the trace gas, aerosol properties, and cloud properties. In addition, radiative fluxes and meteorological parameters were also recorded. The NASA DC-8 was mostly responsible for tropospheric sampling, while the NASA ER-2 was operating in the lower stratospheric regime. The SPEC LearJet was dedicated to in-situ cloud characterizations. To accomplish the science objectives, the flight plans were designed to investigate the influence of biomass burning and pollution, their temporal evolution, and ultimately, impacts on meteorological processes which can, in turn, feedback on regional air quality. With respect to meteorological feedbacks, the opportunity to examine the impact of polluting aerosols on cloud properties and dynamics was of particular interest.",
-            "title": "SEAC4RS DC-8 Aircraft In-Situ Photolysis Rate Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI data set landing page for SEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for SEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341667-LARC_ASDC",
-                    "description": "Earthdata Search for SEAC4RS_jValue_AircraftInSitu_DC8_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SEAC4RS_jValue_AircraftInSitu_DC8_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341667-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/jValue_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/jValue_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2119341667-LARC_ASDC",
+            "issued": "2021-03-19",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_jValue_AircraftInSitu_DC8_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.0 -127.0 19.0 -80.0 51.0 -80.0 51.0 -127.0 19.0 -127.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-08-02T00:00:00Z/2013-09-24T23:59:59.999Z",
             "theme": [
                 "SEAC4RS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEAC4RS DC-8 Aircraft In-Situ Photolysis Rate Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43A4.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MCD43A4.061. MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF Adjusted Ref Daily L3 Global - 500m V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43A4.061. https://doi.org/10.5067/MODIS/MCD43A4.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "ngda",
-                "land surface",
-                "national geospatial data asset",
-                "surface radiative properties",
-                "earth science"
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
-            "identifier": "C2218719731-LPCLOUD",
-            "description": "The Moderate Resolution Imaging Spectroradiometer (MODIS) MCD43A4 Version 6.1 Nadir Bidirectional Reflectance Distribution Function (BRDF)-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua MODIS data at 500 meter (m) resolution. The view angle effects are removed from the directional reflectances, resulting in a stable and consistent NBAR product. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name.\r\n\r\nThe MCD43A4 provides NBAR and quality layers for MODIS bands 1 through 7.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "MCD43A4.061",
-            "graphic-preview-description": "Browse image for Earthdata Search.",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global - 500m V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2357569327-LPCLOUD?h=500&w=500",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Moderate Resolution Imaging Spectroradiometer (MODIS) MCD43A4 Version 6.1 Nadir Bidirectional Reflectance Distribution Function (BRDF)-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua MODIS data at 500 meter (m) resolution. The view angle effects are removed from the directional reflectances, resulting in a stable and consistent NBAR product. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name.\r\n\r\nThe MCD43A4 provides NBAR and quality layers for MODIS bands 1 through 7.\r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43A4.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43A4.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43A4.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43A4.061",
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
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43A4.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43A4.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2218719731-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2218719731-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD43A4.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD43A4.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/97/MCD43_ATBD.pdf",
-                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/97/MCD43_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43A4",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD43A4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43A4",
-                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43A4",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
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
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aquaTerra&ver=C6",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aquaTerra&ver=C6",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2357569327-LPCLOUD?h=500&w=500",
-                    "description": "Browse image for Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2357569327-LPCLOUD?h=500&w=500",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search.",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2357569327-LPCLOUD?h=500&w=500",
+            "identifier": "C2218719731-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "ngda",
+                "land surface",
+                "national geospatial data asset",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43A4.061",
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
+            "series-name": "MCD43A4.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global - 500m V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR7-V1.0",
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
-                "titan",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 28, 30, March 25, 26 2007 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr7-v1.0_jqwh-bqji",
+            "issued": "2018-06-26",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR7-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr7-v1.0_jqwh-bqji",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 28, 30, March 25, 26 2007 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
-            "title": "CASSINI RSS RAW DATA SET - TIGR7 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TIGR7 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-3-PLUTO-V1.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-3-pluto-v1.0_jqxn-9thj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-3-PLUTO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-3-pluto-v1.0_jqxn-9thj",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      CALIBRATED V1.0",
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
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/3YZYV93X5E28",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx17 Boise State University Raw Terrestrial Laser Scanner (TLS) Point Cloud V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/3YZYV93X5E28.",
-            "issued": "2016-09-26",
-            "temporal": "2016-09-26T00:00:00Z/2017-02-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-02-25",
-            "keyword": [
-                "earth science",
-                "lidar",
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
-            "identifier": "C1591634974-NSIDC_ECS",
             "description": "This data set contains raw, unprocessed terrestrial laser scanner (TLS) point cloud data collected as part of the 2017 SnowEx campaign in Grand Mesa, Colorado. Data were collected in the fall (September 2016) and winter (February 2017). Multiple scans were conducted at each site and registered together using common targets. Each point contains X, Y, and Z coordinates (Easting, Northing, and Elevation), as well as intensity (i).",
-            "title": "SnowEx17 Boise State University Raw Terrestrial Laser Scanner (TLS) Point Cloud V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3YZYV93X5E28",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3YZYV93X5E28",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_TLS_PC_BSU_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_TLS_PC_BSU_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1591634974-NSIDC_ECS&m=32.150390625%21-110.126953125%214%211%210%210%2C2&tl=1534286678%214%21%21&q=SNEX17_TLS_PC_BSU_Raw&ok=SNEX17_TLS_PC_BSU_Raw",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1591634974-NSIDC_ECS&m=32.150390625%21-110.126953125%214%211%210%210%2C2&tl=1534286678%214%21%21&q=SNEX17_TLS_PC_BSU_Raw&ok=SNEX17_TLS_PC_BSU_Raw",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_TLS_PC_BSU_Raw/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_TLS_PC_BSU_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_TLS_PC_BSU_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX17_TLS_PC_BSU_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1591634974-NSIDC_ECS&m=32.150390625%21-110.126953125%214%211%210%210%2C2&tl=1534286678%214%21%21&q=SNEX17_TLS_PC_BSU_Raw&ok=SNEX17_TLS_PC_BSU_Raw",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1591634974-NSIDC_ECS&m=32.150390625%21-110.126953125%214%211%210%210%2C2&tl=1534286678%214%21%21&q=SNEX17_TLS_PC_BSU_Raw&ok=SNEX17_TLS_PC_BSU_Raw",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_TLS_PC_BSU_Raw/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX17_TLS_PC_BSU_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3YZYV93X5E28",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/3YZYV93X5E28",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/3YZYV93X5E28",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/3YZYV93X5E28",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1591634974-NSIDC_ECS",
+            "issued": "2016-09-26",
+            "keyword": [
+                "earth science",
+                "lidar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/3YZYV93X5E28",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-02-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.146 39.0 -108.025 39.041",
+            "temporal": "2016-09-26T00:00:00Z/2017-02-25T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx17 Boise State University Raw Terrestrial Laser Scanner (TLS) Point Cloud V001"
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
-                "nasaview",
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
-            "identifier": "NASA-588",
             "description": "Nasaview (3.6.0)",
-            "title": "PDS Software Release Nasaview (3.6.0)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -991038,375 +991019,370 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-588",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nasaview",
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
+            "title": "PDS Software Release Nasaview (3.6.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1370-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-25T16:23:40.000 to 2016-01-25T18:41:48.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1370-v1.0_jr54-2nck",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1370-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1370-v1.0_jr54-2nck",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-25T16:23:40.000 to 2016-01-25T18:41:48.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1370 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1370 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEASURES/MULTIPLE/WIND_CLIMATOLOGY/DATA302",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Mears, Carl A., Deborah K Smith, Kyle Hilburn and Lucrezia Ricciardulli.2016. RSS MONTHLY 1-DEG MERGED WIND CLIMATOLOGY NETCDF V7R01 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/MEASURES/MULTIPLE/WIND_CLIMATOLOGY/DATA302",
-            "issued": "2016-04-25",
-            "temporal": "1988-01-01T00:00:00Z/2022-05-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-24",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean winds",
-                "atmosphere",
-                "atmospheric winds"
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
-            "identifier": "C1996546295-GHRC_DAAC",
             "description": "The Remote Sensing Systems (RSS) Monthly 1-degree Merged Wind Climatology netCDF dataset V7R01 provides global gridded wind speed data over ocean areas. This dataset contains a 12-month climatology using January 1, 1988 to March 31, 2016 data, monthly anomaly maps, a trend map with associated global and tropical wind speed time series, and a time-latitude plot. The wind climatology dataset is a merged ocean product constructed using the version-7 (V7) passive microwave geophysical ocean products made publicly available by Remote Sensing Systems (www.remss.com). Ocean wind measurements used to create this dataset were acquired from the following satellite microwave radiometers: SSM/I F08 through F15, SSMIS F16 and F17, AMSR-E, AMSR-2, and WindSat. The radiometers used to construct this dataset were inter-calibrated at the brightness temperature level, while the V7 ocean products were produced using a consistent processing methodology across sensors.",
-            "graphic-preview-description": "N/A",
-            "title": "RSS MONTHLY 1-DEG MERGED WIND CLIMATOLOGY NETCDF V7R01",
-            "graphic-preview-file": "http://images.remss.com/cdr/climate_data_record_browse.html?product%3Dwind",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FMULTIPLE%2FWIND_CLIMATOLOGY%2FDATA302",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FMULTIPLE%2FWIND_CLIMATOLOGY%2FDATA302",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rss1windnv7r01",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=rss1windnv7r01",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/wind_climatology/doc/rss1windnv7r01_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/wind_climatology/doc/rss1windnv7r01_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/missions/amsre",
-                    "description": "AMSR2 / AMSRE",
                     "@type": "dcat:Distribution",
+                    "description": "AMSR2 / AMSRE",
+                    "downloadURL": "http://www.remss.com/missions/amsre",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/measurements/wind/wspd-1-deg-product",
-                    "description": "Merged Wind Speed 1-deg Monthly Climate Product Information",
                     "@type": "dcat:Distribution",
+                    "description": "Merged Wind Speed 1-deg Monthly Climate Product Information",
+                    "downloadURL": "http://www.remss.com/measurements/wind/wspd-1-deg-product",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://images.remss.com/papers/rsspubs/Wentz_JClim_2015_TMI_17yr_ESDR.pdf",
-                    "description": "A 17-Yr Climate Record of Environmental Parameters Derived from the Tropical Rainfall Measuring Mission (TRMM) Microwave Image",
                     "@type": "dcat:Distribution",
+                    "description": "A 17-Yr Climate Record of Environmental Parameters Derived from the Tropical Rainfall Measuring Mission (TRMM) Microwave Image",
+                    "downloadURL": "http://images.remss.com/papers/rsspubs/Wentz_JClim_2015_TMI_17yr_ESDR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://images.remss.com/cdr/climate_data_record_browse.html?product%3Dwind",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "http://images.remss.com/cdr/climate_data_record_browse.html?product%3Dwind",
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
+            "graphic-preview-file": "http://images.remss.com/cdr/climate_data_record_browse.html?product%3Dwind",
+            "identifier": "C1996546295-GHRC_DAAC",
+            "issued": "2016-04-25",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean winds",
+                "atmosphere",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/MULTIPLE/WIND_CLIMATOLOGY/DATA302",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1988-01-01T00:00:00Z/2022-05-30T00:00:00Z",
             "theme": [
                 "DISCOVER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RSS MONTHLY 1-DEG MERGED WIND CLIMATOLOGY NETCDF V7R01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-RSS-1-CEGR-V1.0",
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
-                "1 ceres",
-                "dawn mission to vesta and ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains archival raw, partially processed, and              ancillary/supporting gravity science data acquired during the Dawn         mission while the spacecraft was in orbit around the asteroid Ceres.       The radio observations were carried out using the Dawn spacecraft and      Earth-based receiving stations of the NASA Deep Space Network (DSN).       The data set was designed primarily to support generation of               high-resolution gravity field models for Ceres. Of most interest are       likely to be the Orbit Data Files in the ODF directory, which provided     the raw input to gravity investigations, as well as the ionospheric and    tropospheric media calibration files in the ION and TRO directories,       respectively.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-rss-1-cegr-v1.0_jr6m-qvqa",
+            "issued": "2018-06-26",
+            "keyword": [
+                "1 ceres",
+                "dawn mission to vesta and ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-RSS-1-CEGR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-rss-1-cegr-v1.0_jr6m-qvqa",
-            "description": "This data set contains archival raw, partially processed, and              ancillary/supporting gravity science data acquired during the Dawn         mission while the spacecraft was in orbit around the asteroid Ceres.       The radio observations were carried out using the Dawn spacecraft and      Earth-based receiving stations of the NASA Deep Space Network (DSN).       The data set was designed primarily to support generation of               high-resolution gravity field models for Ceres. Of most interest are       likely to be the Orbit Data Files in the ODF directory, which provided     the raw input to gravity investigations, as well as the ionospheric and    tropospheric media calibration files in the ION and TRO directories,       respectively.",
-            "title": "DAWN CERES RAW GRAVITY SCIENCE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN CERES RAW GRAVITY SCIENCE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VJPF383IL5E1",
             "citation": "Kevin W. Bowman. 2022-04-04. TRPSYL2COCRSFS. Version 1. TROPESS CrIS-SNPP L2 Carbon Monoxide for Forward Stream, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/VJPF383IL5E1. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2COCRSFS_1.html. Digital Science Data.",
-            "issued": "2022-04-01",
-            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1029/2006JD007663",
-                "https://doi.org/10.1029/2007JD008803",
-                "https://doi.org/10.5194/amt-9-2567-2016",
-                "https://doi.org/10.1016/j.rse.2020.112275",
-                "https://doi.org/10.5194/acp-13-837-2013"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2247040120-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Carbon Monoxide for Forward Stream, Summary Product contains the vertical distribution of the retrieved atmospheric state of carbon monoxide (CO),  and formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is global for the time period from 2021-02-01 to 2021-05-21, when the CrIS-SNPP processing was discontinued. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 14 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2COCRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP CO (Forward Stream, Summary Product) at 383 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Carbon Monoxide for Forward Stream, Summary Product V1 (TRPSYL2COCRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2COCRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVJPF383IL5E1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVJPF383IL5E1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2COCRSFS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP CO (Forward Stream, Summary Product) at 383 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP CO (Forward Stream, Summary Product) at 383 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2COCRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2COCRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2COCRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2COCRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2COCRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2COCRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2COCRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Summary/TRPSYL2COCRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Summary/TRPSYL2COCRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2COCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2COCRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CO_L2_Product_Quick_Start_User_Guide_Summary_only.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CO_L2_Product_Quick_Start_User_Guide_Summary_only.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP CO (Forward Stream, Summary Product) at 383 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2COCRSFS_Sample.png",
+            "identifier": "C2247040120-GES_DISC",
+            "issued": "2022-04-01",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/VJPF383IL5E1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.1029/2006JD007663",
+                "https://doi.org/10.1029/2007JD008803",
+                "https://doi.org/10.5194/amt-9-2567-2016",
+                "https://doi.org/10.1016/j.rse.2020.112275",
+                "https://doi.org/10.5194/acp-13-837-2013"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSYL2COCRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Carbon Monoxide for Forward Stream, Summary Product V1 (TRPSYL2COCRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1383",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Steiner, N., K.C. McDonald, and C.E. Miller. 2018. CARVE: Daily Thaw State of Boreal and Arctic Alaska from AMSR-E and SSM/I, 2003-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1383",
-            "issued": "2018-11-02",
-            "temporal": "2003-01-01T00:00:00Z/2014-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "snow/ice",
-                "earth science",
-                "terrestrial hydrosphere",
-                "climate indicators",
-                "cryosphere",
-                "cryospheric indicators"
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
-            "identifier": "C2236282870-ORNL_CLOUD",
             "description": "This data set provides daily 10 km resolution maps of the Alaskan and Arctic Boreal land surface state as either frozen, melting, or thawed. These data are generated from passive microwave radiometer observations made from 2003 through 2014 by the Advanced Microwave Scanning Radiometer (AMSR-E) and the Special Sensor Microwave Imager (SSM/I). Data products overlap with science data collections carried out during the Carbon in Arctic Reservoirs Vulnerability Experiment (CARVE).",
-            "graphic-preview-description": "Browse Image",
-            "title": "CARVE: Daily Thaw State of Boreal and Arctic Alaska from AMSR-E and SSM/I, 2003-2014",
-            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/CARVE_Land_Thaw_State_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1383",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1383",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/carve/CARVE_Land_Thaw_State/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/carve/CARVE_Land_Thaw_State/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_Land_Thaw_State.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_Land_Thaw_State.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1383",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1383",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
@@ -991512,640 +991488,666 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_Land_Thaw_State_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_Land_Thaw_State_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://carve.ornl.gov",
-                    "description": "CARVE campaign site",
                     "@type": "dcat:Distribution",
+                    "description": "CARVE campaign site",
+                    "downloadURL": "https://carve.ornl.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1383/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1383/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/CARVE_Land_Thaw_State_Fig1.png",
+            "identifier": "C2236282870-ORNL_CLOUD",
+            "issued": "2018-11-02",
+            "keyword": [
+                "snow/ice",
+                "earth science",
+                "terrestrial hydrosphere",
+                "climate indicators",
+                "cryosphere",
+                "cryospheric indicators"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1383",
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
             "spatial": "-180.0 46.99 -106.95 74.4",
+            "temporal": "2003-01-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: Daily Thaw State of Boreal and Arctic Alaska from AMSR-E and SSM/I, 2003-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP02GDC_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2022-01-27. NPP/VIIRS Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VNP02GDC_NRT.002. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt.",
-            "issued": "2022-01-01",
-            "temporal": "2022-01-01T00:00:00Z/2024-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "visible wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Guoqing \"Gary\" Lin",
                 "hasEmail": "mailto:guoqing.lin-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2208829372-LANCEMODIS",
-            "description": "The NPP/VIIRS Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m  Near Real Time (NRT) product, short-name VNP02GDC, contains unaggregated, calibrated TOA radiances for those VIIRS sub-pixel samples that are aggregated along-scan during post-calibration ground processing. In other words, this file contains the calibrated M1- M5, M7 and M13 dual gain band data from the nadir and near-nadir zones that would otherwise be discarded following post-calibration aggregation/Earth View Radiometric Calibration Unit.\r\n\r\nThe VIIRS Level-1 and Level-2 swath products are generated from the processing of 6 minutes of VIIRS data acquired during the NPP satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 micron to 11.45 micron. There are also 7 dual-gain VIIRS bands. The dual gain moderate resolution bands (M1 to M5, M7 and M13) have 6304 samples and the other moderate resolution bands have 3200.\r\n\r\nFor additional information, see the Algorithm Theoretical Basis Document (ATBD) for the L1B product (https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/NASARevisedJPSSVIIRSRadCalATBD2014.pdf). The document describes how VIIRS operates in space and provides the equations implemented by the L1B software to generate the MODIS Level-1 intermediate products. It is a summary document the presents the formulae and error budges used to transform VIIRS digital counts to radiance and reflectance.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "NPP/VIIRS Moderate-Resolution Dual Gain Bands Calibrated Radiance 6 Min L1B Swath 750m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The NPP/VIIRS Moderate-Resolution Dual Gain Bands Calibrated Radiance 6-Min L1B Swath 750m  Near Real Time (NRT) product, short-name VNP02GDC, contains unaggregated, calibrated TOA radiances for those VIIRS sub-pixel samples that are aggregated along-scan during post-calibration ground processing. In other words, this file contains the calibrated M1- M5, M7 and M13 dual gain band data from the nadir and near-nadir zones that would otherwise be discarded following post-calibration aggregation/Earth View Radiometric Calibration Unit.\r\n\r\nThe VIIRS Level-1 and Level-2 swath products are generated from the processing of 6 minutes of VIIRS data acquired during the NPP satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 micron to 11.45 micron. There are also 7 dual-gain VIIRS bands. The dual gain moderate resolution bands (M1 to M5, M7 and M13) have 6304 samples and the other moderate resolution bands have 3200.\r\n\r\nFor additional information, see the Algorithm Theoretical Basis Document (ATBD) for the L1B product (https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/NASARevisedJPSSVIIRSRadCalATBD2014.pdf). The document describes how VIIRS operates in space and provides the equations implemented by the L1B software to generate the MODIS Level-1 intermediate products. It is a summary document the presents the formulae and error budges used to transform VIIRS digital counts to radiance and reflectance.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP02GDC_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP02GDC_NRT.002",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP02GDC_NRT",
-                    "description": "Direct access to the download site and directory hosting the VNP02GDC_NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the VNP02GDC_NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP02GDC_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2208829372-LANCEMODIS",
+            "issued": "2022-01-01",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP02GDC_NRT.002",
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
+            "temporal": "2022-01-01T00:00:00Z/2024-09-30T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP/VIIRS Moderate-Resolution Dual Gain Bands Calibrated Radiance 6 Min L1B Swath 750m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-2%2F3-EDR%2FRDR-NPI-EXT3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Mars Express ASPERA-3 Neutral Particle Imager (NPI) data for the third mission extension (January 1, 2010 - Dec. 31, 2012). These data are provided in units of count rate (counts/second).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-2-3-edr-rdr-npi-ext3-v1.0_jraw-4fns",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "solar wind",
                 "mars express"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-2%2F3-EDR%2FRDR-NPI-EXT3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-2-3-edr-rdr-npi-ext3-v1.0_jraw-4fns",
-            "description": "This data set contains Mars Express ASPERA-3 Neutral Particle Imager (NPI) data for the third mission extension (January 1, 2010 - Dec. 31, 2012). These data are provided in units of count rate (counts/second).",
-            "title": "MARS EXPRESS ASPERA-3 RAW-CAL NTRL PARTICLE IMAGER EXT3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARS EXPRESS ASPERA-3 RAW-CAL NTRL PARTICLE IMAGER EXT3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/111ANV0FK5CY",
             "citation": "Chris Barnet. 2019-12-15. SNDRJ1IML3CDCCP. Version 2. Sounder SIPS: JPSS-1 CrIS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/111ANV0FK5CY. https://disc.gsfc.nasa.gov/datacollection/SNDRJ1IML3CDCCP_2.html. Digital Science Data.",
-            "issued": "2018-02-17",
-            "temporal": "2018-02-17T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-30",
-            "references": [
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "surface thermal properties",
-                "surface radiative properties",
-                "precipitation",
-                "ocean temperature",
-                "oceans",
-                "atmosphere",
-                "land surface",
-                "earth science",
-                "altitude",
-                "atmospheric chemistry",
-                "air quality",
-                "atmospheric temperature",
-                "clouds",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Chris Barnet",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1692982094-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "WARNING: To users of the derived product \u201cco_mmr_midtrop\u201d (carbon monoxide mass mixing ratio to dry air [kg/kg] at ~500 hPa). This variable has a significant bias due to a conversion error: the molecular weight of carbon dioxide (CO2, 44.01 g/mol) was used instead of carbon monoxide (CO, 28.01 g/mol). To correct, simply multiply \u201cco_mmr_midtrop\u201d by 28.01/44.01. Alternatively, derive a profile of mass mixing ratio from scratch using the retrieved column density values (\u201cmol_lay/co_mol_lay\u201d) in the Level 2 files. For further questions or concerns please contact the Sounder SIPS at: sounder.sips@jpl.nasa.gov\n\nThe CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite). The CrIS/ATMS instruments used for this product are on board the NOAA-20 platform, also known as JPSS-1. The CrIS instrument is a Fourier transform spectrometer with a total of 2211 FSR (Full Spectral Resolution) infrared sounding channels covering the longwave (645-1095 cm-1), midwave (1210-1750 cm-1), and shortwave (2100-2550 cm-1) spectral regions. The ATMS instrument  is a cross-track scanner with 22 channels in spectral bands from 23 GHz through 183 GHz.\n \nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n \nThis daily one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products with QC values of 0 (best), 1 (good), and 2 (don't use) which are provided for each variable. Comprehensive QC accepts a retrieval if the profile is good to the surface and ensures consistent analysis across all levels and variables.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRJ1IML3CDCCP",
-            "creator": "Chris Barnet",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 daily surface skin temperature (K).",
-            "title": "Sounder SIPS: JPSS-1 CrIS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS V2 (SNDRJ1IML3CDCCP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1IML3CDCCP_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F111ANV0FK5CY",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F111ANV0FK5CY",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1IML3CDCCP_2.png",
-                    "description": "Sample plot of CrIS/ATMS Level 3 daily surface skin temperature (K).",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS Level 3 daily surface skin temperature (K).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1IML3CDCCP_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ1IML3CDCCP_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ1IML3CDCCP_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS1_Sounder_Level3/SNDRJ1IML3CDCCP.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS1_Sounder_Level3/SNDRJ1IML3CDCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS1_Sounder_Level3/SNDRJ1IML3CDCCP.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS1_Sounder_Level3/SNDRJ1IML3CDCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ1IML3CDCCP+2",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ1IML3CDCCP+2",
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
+            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 daily surface skin temperature (K).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1IML3CDCCP_2.png",
+            "identifier": "C1692982094-GES_DISC",
+            "issued": "2018-02-17",
+            "keyword": [
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "surface thermal properties",
+                "surface radiative properties",
+                "precipitation",
+                "ocean temperature",
+                "oceans",
+                "atmosphere",
+                "land surface",
+                "earth science",
+                "altitude",
+                "atmospheric chemistry",
+                "air quality",
+                "atmospheric temperature",
+                "clouds",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/111ANV0FK5CY",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-30",
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
+                "https://doi.org/10.1016/S0022-4073(97)00169-6",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRJ1IML3CDCCP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-02-17T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: JPSS-1 CrIS Level 3 Comprehensive Quality Control Gridded Daily CLIMCAPS V2 (SNDRJ1IML3CDCCP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C184964548-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, LaRC.",
-            "issued": "2006-04-04",
-            "temporal": "2001-12-10T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-05",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Chu",
                 "hasEmail": "mailto:William.P.Chu@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "identifier": "C184964548-LARC",
             "description": "Level 1B pixel group transmission profiles for a single solar event",
-            "title": "SAGE III Meteor-3M L1B Solar Event Transmission Data (HDF-EOS) V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C184964548-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C184964548-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C184964548-LARC",
+            "issued": "2006-04-04",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C184964548-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-11-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2001-12-10T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAGE III Meteor-3M L1B Solar Event Transmission Data (HDF-EOS) V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0732-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-26T07:57:45.000 to 2015-04-26T12:54:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0732-v1.0_jrc5-mdxq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0732-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0732-v1.0_jrc5-mdxq",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-26T07:57:45.000 to 2015-04-26T12:54:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0732 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0732 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2143",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, A. Gillespie, and S.L. Ustin. 2022. MASTER: Airborne Science, western US, August, 2001, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2143",
-            "issued": "2023-02-23",
-            "temporal": "2001-08-22T17:46:29Z/2001-08-31T20:46:11Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "visible wavelengths"
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
-            "identifier": "C2731788929-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during 11 flights aboard a DOE B-200 aircraft over California, Nevada, Oregon, and Washington, U.S., on 2001-08-22 to 2001-08-31. This deployment was coordinated by the U.S. Department of Energy's Remote Sensing Laboratory (RSL) located at Nellis Air Force Base near Las Vegas, Nevada. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 20-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 4 acquired on 25 August 2001 over Soo's Creek west of Kent, Washington, U.S. Source: MASTERL1B_0100503_04_20010825_1800_1802_V01.jpg",
-            "title": "MASTER: Airborne Science, western US, August, 2001, V2",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2001_V2_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2143",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2143",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_August_2001_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_August_2001_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2001_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2001_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2143",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2143",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_August_2001_V2/comp/MASTER_RSL_August_2001_V2.pdf",
-                    "description": "MASTER: Airborne Science, western US, August, 2001, V2: MASTER_RSL_August_2001_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, western US, August, 2001, V2: MASTER_RSL_August_2001_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_August_2001_V2/comp/MASTER_RSL_August_2001_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2001_V2_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 4 acquired on 25 August 2001 over Soo's Creek west of Kent, Washington, U.S. Source: MASTERL1B_0100503_04_20010825_1800_1802_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 4 acquired on 25 August 2001 over Soo's Creek west of Kent, Washington, U.S. Source: MASTERL1B_0100503_04_20010825_1800_1802_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2001_V2_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 4 acquired on 25 August 2001 over Soo's Creek west of Kent, Washington, U.S. Source: MASTERL1B_0100503_04_20010825_1800_1802_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2001_V2_Fig1.jpg",
+            "identifier": "C2731788929-ORNL_CLOUD",
+            "issued": "2023-02-23",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2143",
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
             "spatial": "-122.43 36.01 -114.26 47.65",
+            "temporal": "2001-08-22T17:46:29Z/2001-08-31T20:46:11Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, western US, August, 2001, V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-FL-3-CAL-V1.0",
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
+            "description": "Calibrated flash mode spectra from the Near Infrared Spectrometer 1 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-fl-3-cal-v1.0_jrgy-nkr4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "lunar crater observation and sensing satellite",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-X-NSP2-FL-3-CAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-x-nsp2-fl-3-cal-v1.0_jrgy-nkr4",
-            "description": "Calibrated flash mode spectra from the Near Infrared Spectrometer 1 (NSP2) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER FLASH 3 CAL V1.0",
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
+            "title": "LCROSS SUN 2ND NEAR IR SPECTROMETER FLASH 3 CAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4NK3BZJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "World Economic Forum - WEF - Global Leaders for Tomorrow Environment Task Force, Yale Center for Environmental Law and Policy - YCELP - Yale University, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2000-12-31. 2000 Pilot Environmental Sustainability Index (ESI). Version 2000.00. New Haven, CT. Archived by National Aeronautics and Space Administration, U.S. Government, Yale Center for Environmental Law and Policy (YCELP)/Yale University. https://doi.org/10.7927/H4NK3BZJ. https://doi.org/10.7927/H4NK3BZJ.",
-            "issued": "2000-12-31",
-            "temporal": "1978-01-01T00:00:00Z/1999-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4X34VDM",
-                "https://doi.org/10.7927/H4SB43P8",
-                "https://doi.org/10.7927/H40V89R6"
-            ],
-            "keyword": [
-                "sustainability",
-                "earth science",
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
-            "identifier": "C179001887-SEDAC",
-            "description": "The 2000 Pilot Environmental Sustainability Index (ESI) is an exploratory effort to construct an index that measures the ability of a nation's economy to achieve sustainable development, with the long term goal of finding a single indicator for environmental sustainability analagous to that of the Gross Domestic Product (GDP). The index covering 56 countries is a composite measure of the current status of a nation's environmental systems, pressures on those systems, human vulnerability to environmental change, national capacity to respond, and contributions to global environmental stewardship. The index was unveiled at the World Economic Forum's annual meeting, January 2000, Davos, Switzerland. The 2000 Pilot ESI is the result of collaboration among the World Economic Forum (WEF), Yale Center for Environmental Law and Policy (YCELP), and the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "New Haven, CT",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "World Economic Forum - WEF - Global Leaders for Tomorrow Environment Task Force, Yale Center for Environmental Law and Policy - YCELP - Yale University, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "2000 Pilot Environmental Sustainability Index (ESI)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/esi/esi-pilot-environmental-sustainability-index-2000/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 2000 Pilot Environmental Sustainability Index (ESI) is an exploratory effort to construct an index that measures the ability of a nation's economy to achieve sustainable development, with the long term goal of finding a single indicator for environmental sustainability analagous to that of the Gross Domestic Product (GDP). The index covering 56 countries is a composite measure of the current status of a nation's environmental systems, pressures on those systems, human vulnerability to environmental change, national capacity to respond, and contributions to global environmental stewardship. The index was unveiled at the World Economic Forum's annual meeting, January 2000, Davos, Switzerland. The 2000 Pilot ESI is the result of collaboration among the World Economic Forum (WEF), Yale Center for Environmental Law and Policy (YCELP), and the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4NK3BZJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4NK3BZJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/esi/esi-pilot-environmental-sustainability-index-2000/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/esi/esi-pilot-environmental-sustainability-index-2000/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-pilot-environmental-sustainability-index-2000/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-pilot-environmental-sustainability-index-2000/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-pilot-environmental-sustainability-index-2000",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-pilot-environmental-sustainability-index-2000",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/esi/esi-pilot-environmental-sustainability-index-2000/sedac-logo.jpg",
+            "identifier": "C179001887-SEDAC",
+            "issued": "2000-12-31",
+            "keyword": [
+                "sustainability",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4NK3BZJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2000-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4X34VDM",
+                "https://doi.org/10.7927/H4SB43P8",
+                "https://doi.org/10.7927/H40V89R6"
+            ],
+            "release-place": "New Haven, CT",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "1978-01-01T00:00:00Z/1999-12-31T00:00:00Z",
             "theme": [
                 "ESI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2000 Pilot Environmental Sustainability Index (ESI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_tt_bundle&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The original PHX TT dataset was submitted in 2009",
+            "identifier": "urn:nasa:pds:phx_tt_bundle_jrii-srjj",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "phoenix telltale tt mars",
                 "phoenix",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_tt_bundle&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:phx_tt_bundle_jrii-srjj",
-            "description": "The original PHX TT dataset was submitted in 2009",
-            "title": "Phoenix TELLTALE Bundle",
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
+            "title": "Phoenix TELLTALE Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-5-MODRDR-V1.0",
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
+            "description": "Data taken by the sensors of the Rover Environmental Monitoring Station (REMS) aboard the  Mars Science Laboratory, in physical units, with corrections and modeling.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-5-modrdr-v1.0_jrjv-2wgu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-REMS-5-MODRDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-rems-5-modrdr-v1.0_jrjv-2wgu",
-            "description": "Data taken by the sensors of the Rover Environmental Monitoring Station (REMS) aboard the  Mars Science Laboratory, in physical units, with corrections and modeling.",
-            "title": "MSL MARS ROVER ENV MONITORING STATION \n                                      5 MODRDR V1.0",
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
+            "title": "MSL MARS ROVER ENV MONITORING STATION \n                                      5 MODRDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-SHAPE-MODELS-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Optical shape models of 9 planetary moons and asteroids, derived from spacecraft imaging by P. Thomas",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-shape-models-v2.0_jrmd-3rq8",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mathilde",
                 "phobos",
@@ -992158,172 +992160,179 @@
                 "hyperion",
                 "gaspra"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-SHAPE-MODELS-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-shape-models-v2.0_jrmd-3rq8",
-            "description": "Optical shape models of 9 planetary moons and asteroids, derived from spacecraft imaging by P. Thomas",
-            "title": "SMALL BODY SHAPE MODELS V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SMALL BODY SHAPE MODELS V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H46H4FBC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seirup, L., and G. Yetman. 2006-05-31. U.S. Census Grids (Summary File 1), 2000: Metropolitan Statistical Areas. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H46H4FBC. https://doi.org/10.7927/H46H4FBC.",
-            "issued": "2006-05-31",
-            "temporal": "2000-04-01T00:00:00Z/2000-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2006-05-31",
-            "references": [
-                "https://doi.org/10.7927/H4PK0D3B"
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
-            "identifier": "C179001955-SEDAC",
-            "description": "U.S. Census Grids (Summary File 1), 2000: Metropolitan Statistical Areas contain grids of demographic and socioeconomic data from the year 2000 U.S. census in ASCII and geotiff formats for 50 metropolitan statistical areas with at least one million in population. The grids have a resolution of 7.5 arc-seconds (0.002075 decimal degrees), or approximately 250 square meters. The gridded variables are based on census block geography from Census 2000 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Seirup, L., and G. Yetman",
-            "title": "U.S. Census Grids (Summary File 1), 2000: Metropolitan Statistical Areas",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "U.S. Census Grids (Summary File 1), 2000: Metropolitan Statistical Areas contain grids of demographic and socioeconomic data from the year 2000 U.S. census in ASCII and geotiff formats for 50 metropolitan statistical areas with at least one million in population. The grids have a resolution of 7.5 arc-seconds (0.002075 decimal degrees), or approximately 250 square meters. The gridded variables are based on census block geography from Census 2000 TIGER/Line Files and census variables (population, households, and housing variables). This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH46H4FBC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH46H4FBC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file1-2000-msa/nyc-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/usgrid/usgrid-summary-file1-2000-msa/nyc-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/usgrid-summary-file1-2000-msa/maps",
+            "identifier": "C179001955-SEDAC",
+            "issued": "2006-05-31",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H46H4FBC",
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
+                "https://doi.org/10.7927/H4PK0D3B"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-124.0 17.0 -65.0 47.0",
+            "temporal": "2000-04-01T00:00:00Z/2000-04-01T00:00:00Z",
             "theme": [
                 "USCG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. Census Grids (Summary File 1), 2000: Metropolitan Statistical Areas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MB-2-EDR-OPS-V1.0",
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
+            "description": "This archive contains Mars Exploration Rover Operations (Ops) Moessbauer Experiment Data Record (EDR) products and ancillary files. Each EDR product has a detached PDS label that describes the file structure and instrument parameters used for that image. The Moessbauer Operations EDR products archived on this volume are the original products used during mission operations by the Mars Exploration Rover project. Supporting documentation and label files conform to the Planetary Data System (PDS) Standards, Version 3.6, Jet Propulsion Laboratory (JPL) document number D-7669.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mb-2-edr-ops-v1.0_jrqy-9awj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MB-2-EDR-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mb-2-edr-ops-v1.0_jrqy-9awj",
-            "description": "This archive contains Mars Exploration Rover Operations (Ops) Moessbauer Experiment Data Record (EDR) products and ancillary files. Each EDR product has a detached PDS label that describes the file structure and instrument parameters used for that image. The Moessbauer Operations EDR products archived on this volume are the original products used during mission operations by the Mars Exploration Rover project. Supporting documentation and label files conform to the Planetary Data System (PDS) Standards, Version 3.6, Jet Propulsion Laboratory (JPL) document number D-7669.",
-            "title": "MER 1 MARS MOESSBAUER SPECTROMETER EDR OPS VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS MOESSBAUER SPECTROMETER EDR OPS VERSION 1.0"
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
+            "description": "CIRS, HRD, ISS, RPWS, RSS, SPICE, UVIS, VIMS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090709.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-699",
+            "issued": "2018-06-25",
             "keyword": [
                 "rpws",
                 "vims",
@@ -992336,292 +992345,285 @@
                 "radar",
                 "iss"
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
-            "identifier": "NASA-699",
-            "description": "CIRS, HRD, ISS, RPWS, RSS, SPICE, UVIS, VIMS",
-            "title": "PDS Cassini Data Release 18",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090709.shtml",
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
+            "title": "PDS Cassini Data Release 18"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0537-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-15T11:48:35.000 to 2015-01-15T23:17:21.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0537-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0537-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0537-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-15T11:48:35.000 to 2015-01-15T23:17:21.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0537 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0537 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/709",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "King, M.D., C. Gatebe, and S.E. Platnick. 2000. SAFARI 2000 Cloud Absorption Radiometer BRDF, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/709",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-15T00:00:00Z/2000-09-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "atmospheric radiation",
-                "earth science",
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
-            "identifier": "C2788376147-ORNL_CLOUD",
             "description": "The Cloud Absorption Radiometer (CAR) is an airborne multi-wavelength scanning radiometer that can perform several functions including determining the single scattering albedo of clouds at selected wavelengths in the visible and near-infrared; measuring the angular distribution of scattered radiation; measuring bidirectional reflectance of various surface types; and acquiring imagery of cloud and Earth surface features.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Cloud Absorption Radiometer BRDF, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F709",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F709",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/CAR_BRDF/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/CAR_BRDF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_car_brdf.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_car_brdf.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/709",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/709",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/CAR_BRDF/comp/car_brdf_cv580_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/CAR_BRDF/comp/car_brdf_cv580_doc.pdf",
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
+            "identifier": "C2788376147-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "atmospheric radiation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/709",
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
             "spatial": "5.0 -35.0 60.0 5.0",
+            "temporal": "2000-08-15T00:00:00Z/2000-09-16T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Cloud Absorption Radiometer BRDF, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-EXT2-MTP030-V1.0",
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
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the EXTENSION 2 MTP030 phase, which occurred from 2016-06-01 to 2016-06-29",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-ext2-mtp030-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-EXT2-MTP030-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-ext2-mtp030-v1.0",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the EXTENSION 2 MTP030 phase, which occurred from 2016-06-01 to 2016-06-29",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 2 EXTENSION 2 MTP030 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P VIRTIS 2 EXTENSION 2 MTP030 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-3-FGM-CAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the Juno FGM calibrated orbital observations. The FGM sensor block uses two miniature ring-core fluxgate sensors to measure the magnetic field in three components of the vector field. There are multiple FGM data products to accomodate different coordinate systems.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-3-fgm-cal-v1.0_jryb-svak",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "solar system",
                 "juno",
                 "jupiter",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-J-3-FGM-CAL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-j-3-fgm-cal-v1.0_jryb-svak",
-            "description": "Abstract ======== This data set consists of the Juno FGM calibrated orbital observations. The FGM sensor block uses two miniature ring-core fluxgate sensors to measure the magnetic field in three components of the vector field. There are multiple FGM data products to accomodate different coordinate systems.",
-            "title": "JUNO J FLUXGATE MAGNETOMETER\nCALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "JUNO J FLUXGATE MAGNETOMETER\nCALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567905-USGS_LTA.html",
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
-            "identifier": "C1220567905-USGS_LTA",
             "description": "The surface reflectance CDR is generated from specialized software called Landsat Ecosystem Disturbance Adaptive Processing System (LEDAPS). LEDAPS was originally developed through a National Aeronautics and Space Administration (NASA) Making Earth System Data Records for Use in Research Environments (MEaSUREs)grant by NASA Goddard Space Flight Center (GSFC) and the University of Maryland (Masek et al., 2006). The software applies Moderate Resolution Imaging spectroradiometer (MODIS) atmospheric correction routines to Level-1 Landsat Thematic Mapper (TM) or Enhanced Thematic Mapper Plus (ETM+)data.  Water,vapor, ozone, geopotential height, aerosol optical thickness,and digital elevation are input with Landsat data to the Second Simulation of a Satellite Signal in the Solar Spectrum (6S) radiative transfer models to generate top of atmosphere (TOA)reflectance, surface reflectance, brightness temperature, and masks for clouds, cloud shadows, adjacent clouds, land, and water.  The result is delivered as the Landsat surface reflectance CDR.",
-            "title": "Land Surface Reflectance - GLS2000",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Data set searching and ordering capabilities are available through EarthExplorer at the above URL.  Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Data set searching and ordering capabilities are available through EarthExplorer at the above URL.  Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1220567905-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "surface radiative properties",
+                "topography",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567905-USGS_LTA.html",
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
+            "title": "Land Surface Reflectance - GLS2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acompil.ast.radar.shape-models&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains radar-based shape models for small solar system bodies,\nprepared by various authors.",
+            "identifier": "urn:nasa:pds:compil.ast.radar.shape-models",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "1998 ky26",
                 "(1620) geographos",
@@ -992634,36 +992636,48 @@
                 "(6489) golevka",
                 "none"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Acompil.ast.radar.shape-models&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:compil.ast.radar.shape-models",
-            "description": "This data set contains radar-based shape models for small solar system bodies,\nprepared by various authors.",
-            "title": "Small Bodies Radar Shape Models V1.0",
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
+            "title": "Small Bodies Radar Shape Models V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/js2x-b7sc",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We report the findings of an animal experiment onboard STS-135 investigating the molecular aspects of the impact of spaceflight on retinal biology by performing differential gene expression profiling between mice flown onboard STS-135 and their ground control counterparts.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-87",
+                    "mediaType": "text/html",
+                    "title": "Spaceflight effects on the mouse retina: Histological gene expression and epigenetic changes after flight on STS-135"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-87_js2x-b7sc",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "normalization data transformation",
                 "spaceflight",
@@ -992675,1174 +992689,1132 @@
                 "radiation dosimetry",
                 "absorbed radiation dose"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/js2x-b7sc",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-87_js2x-b7sc",
-            "description": "We report the findings of an animal experiment onboard STS-135 investigating the molecular aspects of the impact of spaceflight on retinal biology by performing differential gene expression profiling between mice flown onboard STS-135 and their ground control counterparts.",
-            "title": "Spaceflight effects on the mouse retina: Histological gene expression and epigenetic changes after flight on STS-135",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-87",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Spaceflight effects on the mouse retina: Histological gene expression and epigenetic changes after flight on STS-135"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Spaceflight effects on the mouse retina: Histological gene expression and epigenetic changes after flight on STS-135"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M03-V1.0",
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
+            "description": "This data set contains images acquired between 2014-05-07 and 2014-06-04 by\nthe OSIRIS Wide Angle Camera during the prelanding phase of the Rosetta\nmission at the comet 67P",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m03-v1.0_js2y-n589",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M03-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m03-v1.0_js2y-n589",
-            "description": "This data set contains images acquired between 2014-05-07 and 2014-06-04 by\nthe OSIRIS Wide Angle Camera during the prelanding phase of the Rosetta\nmission at the comet 67P",
-            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER COMET PRELANDING OSIWAC 2 EDR data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/C98E2L0ZTWO4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX08 In Situ Soil Moisture Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/C98E2L0ZTWO4.",
-            "issued": "2008-09-29",
-            "temporal": "2008-09-29T00:00:00Z/2008-10-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-10-13",
-            "keyword": [
-                "soils",
-                "land surface",
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
-            "identifier": "C1000001423-NSIDC_ECS",
             "description": "This data set includes several parameters that were obtained from field surveys as part of the Soil Moisture Active Passive Validation Experiment 2008 (SMAPVEX08).",
-            "title": "SMAPVEX08 In Situ Soil Moisture Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC98E2L0ZTWO4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FC98E2L0ZTWO4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV08SM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV08SM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV08SM/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV08SM/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV08SM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV08SM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV08SM/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV08SM/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/C98E2L0ZTWO4",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/C98E2L0ZTWO4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/C98E2L0ZTWO4",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/C98E2L0ZTWO4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001423-NSIDC_ECS",
+            "issued": "2008-09-29",
+            "keyword": [
+                "soils",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/C98E2L0ZTWO4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-10-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-76.25 38.93 -75.55 39.09",
+            "temporal": "2008-09-29T00:00:00Z/2008-10-13T23:59:59.999Z",
             "theme": [
                 "SMAPVEX08",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX08 In Situ Soil Moisture Data V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TRMM/CERES/BDS-PFM_L1B.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1998-07-08. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TRMM/CERES/BDS-PFM_L1B.001.",
-            "issued": "2014-01-23",
-            "temporal": "1997-12-08T00:00:00Z/2000-04-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-29",
-            "keyword": [
-                "sensor characteristics",
-                "atmosphere",
-                "atmospheric radiation",
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering",
-                "infrared wavelengths"
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
-            "identifier": "C4254871-LARC_ASDC",
             "description": "CER_BDS_TRMM-PFM_Edition1 is the Clouds and the Earth's Radiant Energy System (CERES) BiDirectional Scans (BDS) Tropical Rainfall Measuring Mission (TRMM) Edition 1 data product. Data collection for this product is complete. \r\n\r\nCER_BDS_TRMM-PFM_Edition1 data are CERES geolocated and calibrated Top-of-Atmosphere (TOA) filtered radiances and other instrument data. Each CERES BDS data product contains twenty-four hours of Level-1B data for each CERES scanner instrument mounted on each spacecraft. The BDS includes samples taken in normal and short Earth scan elevation profiles in both fixed and rotating azimuth scan modes (including space, internal calibration, and solar calibration views). BDS contains Level-0 raw (unconverted) science and instrument data as well as the geolocated converted science and instrument data. Further, BDS contains additional data not found in the Level-0 input file, including converted satellite position and velocity data, celestial data, converted digital status data, and parameters used in the radiance count conversion equations. \r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the TRMM. Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Bidirectional Scans TRMM Edition1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMM%2FCERES%2FBDS-PFM_L1B.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMM%2FCERES%2FBDS-PFM_L1B.001",
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
-                    "downloadURL": "https://doi.org/10.5067/TRMM/CERES/BDS-PFM_L1B.001",
-                    "description": "DOI data set landing page for CER_BDS_TRMM-PFM_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_BDS_TRMM-PFM_Edition1",
+                    "downloadURL": "https://doi.org/10.5067/TRMM/CERES/BDS-PFM_L1B.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C4254871-LARC_ASDC",
-                    "description": "Earthdata Search for CER_BDS_TRMM-PFM_Edition1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_BDS_TRMM-PFM_Edition1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C4254871-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_BDS_R6V1.pdf",
-                    "description": "CERES Data Products Catalog R6V16/20/2014 Bidirectional Scans (BDS)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R6V16/20/2014 Bidirectional Scans (BDS)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_BDS_R6V1.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/BDS_CG_R3V4.pdf",
-                    "description": "CERES Data Management System BiDirectional Scans (BDS) Collection Document - Release 3 Version 4",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Management System BiDirectional Scans (BDS) Collection Document - Release 3 Version 4",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/BDS_CG_R3V4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_bds.pdf",
-                    "description": "CERES Bidirectional Scans (BDS) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Bidirectional Scans (BDS) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_bds.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_BDS_TRMM-PFM_Edition1.pdf",
-                    "description": "Quality Summary: CERES BDS (BiDirectional Scan) TRMM-PFM Edition 1",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES BDS (BiDirectional Scan) TRMM-PFM Edition 1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_BDS_TRMM-PFM_Edition1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_bds_SampleRead_R5-890.txt",
-                    "description": "Readme Information on the CERES BDS Data Sets",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information on the CERES BDS Data Sets",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_bds_SampleRead_R5-890.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/instrument_SampleRead_BDS_R5-890.zip",
-                    "description": "Read Software Package - CERES BDS_Terra-FM1 - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - CERES BDS_Terra-FM1 - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/instrument_SampleRead_BDS_R5-890.zip",
+                    "mediaType": "application/zip",
                     "title": "View this dataset's science data product software documentation"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/BDS/TRMM-PFM_Edition1/",
-                    "description": "ASDC Direct Data Download for CER_BDS_TRMM-PFM_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_BDS_TRMM-PFM_Edition1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/BDS/TRMM-PFM_Edition1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/BDS/TRMM-PFM_Edition1/contents.html",
-                    "description": "OPeNDAP data access for CER_BDS_TRMM-PFM_Edition1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_BDS_TRMM-PFM_Edition1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/BDS/TRMM-PFM_Edition1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C4254871-LARC_ASDC",
+            "issued": "2014-01-23",
+            "keyword": [
+                "sensor characteristics",
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/TRMM/CERES/BDS-PFM_L1B.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-09-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-55.0 -180.0 -55.0 180.0 55.0 180.0 55.0 -180.0 -55.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-12-08T00:00:00Z/2000-04-02T23:59:59.999Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Bidirectional Scans TRMM Edition1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1129",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Davidson, E.A., C.J.R. de Carvalho, A.M. Figueira, F.Y. Ishida, J.P.H.B. Ometto, G.B. Nardoto, R.T. Saba, S.N. Hayashi, E.C. Leal, I.C.G. Vieira and L.A. Martinelli. 2012. LBA-ECO ND-30 Nutrient Analysis and Gas Fluxes, Forest Chronosequences, Para, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1129",
-            "issued": "2023-10-03",
-            "temporal": "2000-10-01T00:00:00Z/2005-01-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "vegetation",
-                "solid earth",
-                "soils",
-                "land surface",
-                "atmosphere",
-                "geochemistry",
-                "atmospheric chemistry",
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
-            "identifier": "C2780955938-ORNL_CLOUD",
             "description": "This data set provides fine litterfall mass and nutrient concentrations from samples collected at chronosequences established at Sao Francisco do Para and Capitao Poco, Para, Brazil. Nitrogen (N) and phosphorus (P) concentrations were determined for litterfall samples from the Sao Francisco do Para, and N, P, potassium (K), calcium (Ca), and magnesium (Mg) concentrations are reported for samples from the Capitao Poco. In addition, carbon (C), N, delta C13, and delta N15 values were determined for leaves from the dominant species of the forests at Sao Francisco do Para; soil physical and chemical characteristics were determined for a subset of the chronosequence plots at the two study sites; and soil trace gas fluxes were determined from the Sao Francisco do Para site. All samples were collected between March 2001-February 2005. Trace gas fluxes were measured 10 times between October 2000 and June 2002 with 5 sample periods in dry season and 5 in wet season months. There are five comma-delimited data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-30 Nutrient Analysis and Gas Fluxes, Forest Chronosequences, Para, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1129",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1129",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND30_Litter_Para/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND30_Litter_Para/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND30_Litter_Para.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND30_Litter_Para.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1129",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1129",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND30_Litter_Para/comp/ND30_Litter_Para.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND30_Litter_Para/comp/ND30_Litter_Para.pdf",
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
+            "identifier": "C2780955938-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "vegetation",
+                "solid earth",
+                "soils",
+                "land surface",
+                "atmosphere",
+                "geochemistry",
+                "atmospheric chemistry",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1129",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-47.78 -15.93 -47.37 -1.27",
+            "temporal": "2000-10-01T00:00:00Z/2005-01-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-30 Nutrient Analysis and Gas Fluxes, Forest Chronosequences, Para, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/16",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chalfant, M. P., and R. Frouin. 1994. Atmospheric Profiles: TOVS - NOAA (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/16",
-            "issued": "2024-05-04",
-            "temporal": "1987-01-01T00:00:00Z/1987-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric temperature",
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
-            "identifier": "C2979926833-ORNL_CLOUD",
             "description": "TOVS data received by FIFE",
-            "graphic-preview-description": "Browse Image",
-            "title": "Atmospheric Profiles: TOVS - NOAA (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F16",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F16",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_atmos_noaa_tov/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_atmos_noaa_tov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/TOVS_atmos_prof.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/TOVS_atmos_prof.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/16",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/16",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_noaa_tov/comp/noaa_tov.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_noaa_tov/comp/noaa_tov.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_noaa_tov/comp/noaa_tov.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_noaa_tov/comp/noaa_tov.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_noaa_tov/comp/TOVS_atmos_prof.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_noaa_tov/comp/TOVS_atmos_prof.pdf",
+                    "mediaType": "application/pdf",
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
+            "identifier": "C2979926833-ORNL_CLOUD",
+            "issued": "2024-05-04",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "clouds",
+                "atmospheric pressure",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/16",
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
             "spatial": "-102.0 37.0 -95.0 40.0",
+            "temporal": "1987-01-01T00:00:00Z/1987-12-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Atmospheric Profiles: TOVS - NOAA (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/783/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Miryam Strautkalns",
                 "hasEmail": "mailto:miryam.strautkalns@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_783",
             "description": "This paper demonstrates how to apply prognostics to power MOSFETs (metal oxide field effect transistor). The methodology uses thermal cycling to age devices and Gaussian process regression to perform prognostics. The approach is validated with experiments on 100V power MOSFETs. The failure mechanism for the stress conditions is determined to be die-attachment degradation. Change in ON-state resistance is used as a precursor of failure due to its dependence on junction temperature. The experimental data is augmented with a finite element analysis simulation that is based on a two-transistor model. The simulation assists in the interpretation of the degradation phenomena and SOA (safe operation area) change.",
-            "title": "Prognostics of Power MOSFET",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_ISPSD_MOSFET.pdf",
-                    "description": "2011_ISPSD_MOSFET.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2011_ISPSD_MOSFET.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_ISPSD_MOSFET.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2011_ISPSD_MOSFET.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_783",
+            "issued": "2013-06-19",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/783/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Prognostics of Power MOSFET"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-EXT1-V2.0",
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
+            "description": "This data set contains CODMAC level 2 science data acquired by the COPS, DFMS and RTOF ROSINA sensors between 2016-01-13 and 2016-04-05 during the Extension phase 1 of the Rosetta mission at the comet 67P/CG. V2.0 : Some missing DFMS PDS files were added and corrupted files have been removed.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-ext1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-EXT1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-ext1-v2.0",
-            "description": "This data set contains CODMAC level 2 science data acquired by the COPS, DFMS and RTOF ROSINA sensors between 2016-01-13 and 2016-04-05 during the Extension phase 1 of the Rosetta mission at the comet 67P/CG. V2.0 : Some missing DFMS PDS files were added and corrupted files have been removed.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 2\n                                      EXT1 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 2\n                                      EXT1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0958-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-12T21:31:30.000 to 2015-08-13T05:22:25.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0958-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0958-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0958-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-12T21:31:30.000 to 2015-08-13T05:22:25.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0958 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0958 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/620",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kittel, T.G.F., N.A. Rosenbloom, C. Kaufman, J.A. Royle, C. Daly, H.H. Fisher, W.P. Gibson, S. Aulenbach, R. McKeown, D.S. Schimel, and VEMAP 2 Participants. 2001. VEMAP 2: U.S. Daily Climate, 1895-1993 . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/620",
-            "issued": "2024-04-22",
-            "temporal": "1895-01-01T00:00:00Z/1993-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-23",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "precipitation",
-                "earth science",
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
-            "identifier": "C2946956305-ORNL_CLOUD",
             "description": "VEMAP Phase 2 has developed a data set of ~100-year gridded monthly and daily time series of climate for the conterminous United States that includes realistic interannual variability.  This data set has been used to compare time-dependent ecological responses of biogeochemical and coupled biogeochemical-biogeographical models to historical time series and projected scenarios of climate, atmospheric CO2, and N-Deposition, and N-Deposition",
-            "graphic-preview-description": "Browse Image",
-            "title": "VEMAP 2: U.S. Daily Climate, 1895-1993",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/620_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F620",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F620",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-2_TCLIMATE_daily/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-2_TCLIMATE_daily/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/Vemap-2_DailyClimate.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/Vemap-2_DailyClimate.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/620",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/620",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_daily/comp/Phase_2_User_Guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_daily/comp/Phase_2_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_daily/comp/README_CLIMATE.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_daily/comp/README_CLIMATE.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_daily/comp/Vemap-2_DailyClimate.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-2_TCLIMATE_daily/comp/Vemap-2_DailyClimate.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/620_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/620_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/620/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/620/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/620_1_fit.png",
+            "identifier": "C2946956305-ORNL_CLOUD",
+            "issued": "2024-04-22",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/620",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-124.5 25.0 -67.0 49.0",
+            "temporal": "1895-01-01T00:00:00Z/1993-12-31T23:59:59Z",
             "theme": [
                 "VEMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VEMAP 2: U.S. Daily Climate, 1895-1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/261",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hardy, J.P., and R.E. Davis. 1998. BOREAS HYD-03 Snow Temperature Profiles. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/261",
-            "issued": "2023-11-22",
-            "temporal": "1994-02-05T00:00:00Z/1994-04-27T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "snow/ice",
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
-            "identifier": "C2807624725-ORNL_CLOUD",
             "description": "This is a snow temperature table for HYD03. The snow temperature is given for various snow heights at various sites.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS HYD-03 Snow Temperature Profiles",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F261",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F261",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h03sntmd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h03sntmd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD03_Snow_Meas.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD03_Snow_Meas.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/261",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/261",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03sntmd/comp/h03sntmd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03sntmd/comp/h03sntmd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03sntmd/comp/HYD03_Snow_Meas.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03sntmd/comp/HYD03_Snow_Meas.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03sntmd/comp/HYD03_Snow_Meas.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03sntmd/comp/HYD03_Snow_Meas.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03sntmd/comp/HYD03_Snow_Meas.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h03sntmd/comp/HYD03_Snow_Meas.txt",
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
+            "identifier": "C2807624725-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/261",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-105.27 53.56 -97.82 55.93",
+            "temporal": "1994-02-05T00:00:00Z/1994-04-27T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS HYD-03 Snow Temperature Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPC/1C/07",
             "citation": "Wesley Berg. 2022-05-09. GPM_1CMETOPCMHS. GPM MHS on METOP-C Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/MHS/METOPC/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CMETOPCMHS_07.html. Digital Science Data.",
-            "issued": "2022-05-01",
-            "temporal": "2018-11-16T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "precipitation",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264133127-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. \n\n1CAMSR2 contains common calibrated brightness temperature from the AMSR2 passive microwave instrument flown on the GCOMW1 satellite. This products contains 6 swaths. Swath 1 has channels 10.65V 10.65H. Swath 2 has channels 18.7V 18.7H. Swath 3 has channels 23.8V 23.8H. Swath 4 has channels 36.5V 36.5H. Swath S5 has 2 high frequency A-Scan channels (89V 89H). Swath S6 has 2 high frequency B-Scan channels (89V 89H). Data for all six swaths is observed in the same revolution of the instrument. High frequency A and high frequency B data are observed in separate feedhorns. All 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_1CMETOPCMHS",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from METOPB (GPM_1CMETOPBMHS)",
-            "title": "GPM MHS on METOP-C Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CMETOPCMHS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CMETOPCMHS.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPC%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FMETOPC%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CMETOPCMHS.png",
-                    "description": "Common Calibrated Brightness Temperature from METOPB (GPM_1CMETOPBMHS)",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from METOPB (GPM_1CMETOPBMHS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CMETOPCMHS.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CMETOPCMHS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CMETOPCMHS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CMETOPCMHS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CMETOPCMHS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CMETOPCMHS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CMETOPCMHS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CMETOPCMHS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CMETOPCMHS_07",
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
@@ -993852,156 +993824,165 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/V07_L1C_Release_Notes.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/V07_L1C_Release_Notes.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://www.eumetsat.int/mhs",
-                    "description": "Instrument Description from EUMETSAT",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from EUMETSAT",
+                    "downloadURL": "https://www.eumetsat.int/mhs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/mhs.php",
-                    "description": "Instrument Description from NOAA",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from NOAA",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/mhs.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from METOPB (GPM_1CMETOPBMHS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CMETOPCMHS.png",
+            "identifier": "C2264133127-GES_DISC",
+            "issued": "2022-05-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "precipitation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/MHS/METOPC/1C/07",
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
+            "references": [
+                "https://doi.org/10.1175/JTECH-D-16-0100.1",
+                "https://doi.org/10.3390/rs10081306"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_1CMETOPCMHS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-11-16T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM MHS on METOP-C Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CMETOPCMHS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-TES-3-TSDR-V1.0",
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
+            "description": "The TES-TSDR data product contains the raw and calibrated thermal IR radiance spectra, the visual and thermal bolometric radiance measurements, and several atmospheric and surface properties derived from this data. Also included are the parameters that describe each observations, some downlinked diagnostic information, and the pointing and positional information derived from the project's SPICE kernels.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-tes-3-tsdr-v1.0_jscs-vtza",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-TES-3-TSDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-tes-3-tsdr-v1.0_jscs-vtza",
-            "description": "The TES-TSDR data product contains the raw and calibrated thermal IR radiance spectra, the visual and thermal bolometric radiance measurements, and several atmospheric and surface properties derived from this data. Also included are the parameters that describe each observations, some downlinked diagnostic information, and the pointing and positional information derived from the project's SPICE kernels.",
-            "title": "MGS MARS TES SCIENCE DATA RECORD V1.0",
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
+            "title": "MGS MARS TES SCIENCE DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3299-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-15T12:00:00.500 to 2012-05-27T08:17:11.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3299-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3299-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3299-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-15T12:00:00.500 to 2012-05-27T08:17:11.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3299 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3299 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://data.giss.nasa.gov/stormtracks/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "knowledge sharing",
-                "space science",
-                "geography",
-                "safety",
-                "planetary science",
-                "lessons learned"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Schenk",
                 "hasEmail": "mailto:schenk@lpi.usra.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000026",
+            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
             "description": "This web page leads to a database of images and information about the 150 major impact craters on Callisto and is updated semi-regularly based on continuing analysis of Voyager images.",
-            "title": "Callisto Crater Database",
-            "programCode": [
-                "026:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -994009,83 +993990,81 @@
                     "mediaType": "text/tab-separated-values"
                 }
             ],
+            "identifier": "NASA-0000026",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge sharing",
+                "space science",
+                "geography",
+                "safety",
+                "planetary science",
+                "lessons learned"
+            ],
+            "landingPage": "http://data.giss.nasa.gov/stormtracks/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "spatial": "Callisto",
-            "describedBy": "http://www.lpi.usra.edu/resources/gc/gcreadme.html",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Callisto Crater Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_tega_derived&version=1.1",
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
-                "phoenix",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Phoenix Thermal Evolved Gas Analyzer Derived Differential Scanning Calorimetry Dataset produced by Brad Sutter, MDAP 2014",
+            "identifier": "urn:nasa:pds:phx_tega_derived",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aphx_tega_derived&version=1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:phx_tega_derived",
-            "description": "Phoenix Thermal Evolved Gas Analyzer Derived Differential Scanning Calorimetry Dataset produced by Brad Sutter, MDAP 2014",
-            "title": "Phoenix Thermal Evolved Gas Analyzer Derived Scanning Calorimetry Dataset",
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
+            "title": "Phoenix Thermal Evolved Gas Analyzer Derived Scanning Calorimetry Dataset"
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
-            "identifier": "NASA-862__35",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -994093,46 +994072,44 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__35",
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
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/sts",
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
-                "shuttle",
-                "3d model",
-                "vehicles",
-                "space shuttle",
-                "spacecraft"
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
-            "identifier": "NASA-401",
             "description": "Polygons: 2476  Vertices: 1353",
-            "title": "NASA 3D Models: Shuttle Model 1",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -994140,478 +994117,513 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-401",
+            "issued": "2018-06-25",
+            "keyword": [
+                "shuttle",
+                "3d model",
+                "vehicles",
+                "space shuttle",
+                "spacecraft"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/sts",
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
+            "title": "NASA 3D Models: Shuttle Model 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/298",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wrigley, R.C. 1998. BOREAS RSS-12 Airborne Tracking Sunphotometer Measurements (C-130). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/298",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-25T00:00:00Z/1994-09-09T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-07",
-            "keyword": [
-                "aerosols",
-                "atmosphere",
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
-            "identifier": "C2813389538-ORNL_CLOUD",
             "description": "Contains measurements from the airborne auto tracking sun photometers on board the NASA Ames C-130 aircraft, operated by RSS12 (Wrigley).",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-12 Airborne Tracking Sunphotometer Measurements (C-130)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F298",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F298",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/sunphair/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/sunphair/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS12_Air_Sunphoto.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS12_Air_Sunphoto.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/298",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/298",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/RSS12_Air_Sunphoto.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/RSS12_Air_Sunphoto.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/RSS12_Air_Sunphoto.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/RSS12_Air_Sunphoto.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/RSS12_Air_Sunphoto.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/RSS12_Air_Sunphoto.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/rss12_c130_sun_photo_ref.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/rss12_c130_sun_photo_ref.dat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/rss12_sun_photo_ref.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/rss12_sun_photo_ref.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/sunphair.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/sunphair/comp/sunphair.def",
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
+            "identifier": "C2813389538-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/298",
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
             "spatial": "-106.75 52.94 -97.38 56.33",
+            "temporal": "1994-05-25T00:00:00Z/1994-09-09T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-12 Airborne Tracking Sunphotometer Measurements (C-130)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_DAILY_Q_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service (IGS). 1992. Daily 30-Second QZSS broadcast ephemeris data [online]. Available from the NASA Crustal Dynamics Data Information System DAAC, Greenbelt, MD, USA at: https://doi.org/10.5067/GNSS/gnss_daily_q_001, Accessed [[enter user data access date]]",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "geodetics",
-                "gravity/gravitational field",
-                "tectonics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-cddis@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDDIS"
-            },
-            "identifier": "C1416457581-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS)  Quasi-Zenith Satellite System (QZSS) Broadcast Ephemeris Data (daily files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLONASS. Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The daily QZSS broadcast ephemeris files contain one day of QZSS broadcast navigation data in RINEX format from a global permanent network of ground-based receivers, one file per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) QZSS Broadcast Ephemeris Data (daily files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_DAILY_Q_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_DAILY_Q_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/daily",
-                    "description": "URL for retrieval of GNSS daily data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS daily data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/daily",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
-                    "description": "URL for more information about GNSS daily QZSS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS daily QZSS broadcast navigation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_DAILY_Q_001",
-                    "description": "URL for more information about GNSS daily QZSS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS daily QZSS broadcast navigation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_DAILY_Q_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1416457581-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_DAILY_Q_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) QZSS Broadcast Ephemeris Data (daily files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625684-GES_DISC.html",
             "citation": "Goddard Laboratory for Atmospheres at NASA/GSFC. 1995-01-01. TOVSBDND. Version 01. TOVS LMD DAILY GRIDS from NOAA-12 V01. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOVSBDND_01.html. Digital Science Data.",
-            "issued": "1991-06-29",
-            "temporal": "1991-06-29T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1995-07-05",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmosphere",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
+            "creator": "Goddard Laboratory for Atmospheres at NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1274625684-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Level 3 parameters from HIRS/2 and MSU radiances using the Improved Initialization Inversion (3I) classification retrieval scheme by the Laboratoire de  Meteorologie Dynamique (Ecole Polytechnique) averaged over 1 day and mapped on to a 1x1 degree grid. This data was run as part of the NASA TOVS Pathfinder project and designated as Path-B. This dataset contains data from the NOAA-12 satellite.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TOVSBDND",
-            "creator": "Goddard Laboratory for Atmospheres at NASA/GSFC",
-            "title": "TOVS LMD DAILY GRIDS from NOAA-12 V01 (TOVSBDND) at GES DISC",
-            "graphic-preview-description": "TOVSBDND image",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSBDND_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSBDND_01.png",
-                    "description": "TOVSBDND image",
                     "@type": "dcat:Distribution",
+                    "description": "TOVSBDND image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSBDND_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSBDND_01.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOVSBDND_01.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSBDND/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSBDND/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSBDND+001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOVSBDND+001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSBDND/doc/README.TOVSPathB.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc1.gesdisc.eosdis.nasa.gov/data/tovs/TOVSBDND/doc/README.TOVSPathB.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "TOVSBDND image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOVSBDND_01.png",
+            "identifier": "C1274625684-GES_DISC",
+            "issued": "1991-06-29",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1274625684-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1995-07-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TOVSBDND",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1991-06-29T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOVS LMD DAILY GRIDS from NOAA-12 V01 (TOVSBDND) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/W66HUFU4KYRQ",
             "citation": "NOAA NESDIS. 2022-08-22. VISSRGOES3IMIR. Version 001. VISSR/GOES-3 Infrared Imagery on 70mm Film V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/W66HUFU4KYRQ. https://disc.gsfc.nasa.gov/datacollection/VISSRGOES3IMIR_001.html. Digital Science Data.",
-            "issued": "2018-03-21",
-            "temporal": "1979-05-02T00:00:00Z/1979-06-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-21",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NOAA NESDIS",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2387041635-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "VISSRGOES3IMIR is the Visible Infrared Spin-Scan Radiometer (VISSR) Infrared Imagery on 70mm Film data product from the third Geostationary Operational Environmental Satellite (GOES-3). This set of IR imagery (10.5 to 12.5 micrometer) was originally produced on commercial image-generation equipment from digital tapes and was made available on 70-mm film, from which they were later scanned to digital TIFF image files. Each TIFF scan contains 2 or 3 pictures, and there are several hundred scans from an original 70 mm film roll which are combined into a ZIP file. Each picture contains a title on the top boundary and a 33-level gray scale on the right boundary that represents brightness temperatures. It may have a combination of the following options: 1) contrast enhancement, 2) image sectorization, and 3) 1/16-size imagery. The maximum effective size covers 500 sq km, represented by 4000 by 3904 pixels. Each element has a maximum resolution of 3.7 km. The title contains the satellite identification, picture number, picture type, coordinate numbers of the top left pixel relative to the visible sensor, start time of sectorized image, and pixel scaling and sector size identification.\n\nThe GOES-3 satellite was parked over the equator at longitude 135W from 1978 through 1981 viewing the hemisphere below the satellite. The VISSR experiment was operated by the NOAA National Environmental Satellite Data and Information Service (NESDIS), as well as scientists from NASA Goddard Space Flight Center.\n\nThis product was previously available from the NSSDC with the identifier ESAD-00105 (old ID 75-100A-01C).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "VISSRGOES3IMIR",
-            "creator": "NOAA NESDIS",
-            "title": "VISSR/GOES-3 Infrared Imagery on 70mm Film V001 (VISSRGOES3IMIR) at GES DISC",
-            "graphic-preview-description": "Typical GOES-3 VISSR visible 70mm film image.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES3IMIR_001.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW66HUFU4KYRQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW66HUFU4KYRQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES3IMIR_001.png",
-                    "description": "Typical GOES-3 VISSR visible 70mm film image.",
                     "@type": "dcat:Distribution",
+                    "description": "Typical GOES-3 VISSR visible 70mm film image.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES3IMIR_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRGOES3IMIR_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/VISSRGOES3IMIR_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES3IMIR.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES3IMIR.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRGOES3IMIR",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=VISSRGOES3IMIR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES3IMIR.001/doc/README.VISSRSMSGOESIM.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GOES/VISSRGOES3IMIR.001/doc/README.VISSRSMSGOESIM.001.pdf",
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
+            "graphic-preview-description": "Typical GOES-3 VISSR visible 70mm film image.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/VISSRGOES3IMIR_001.png",
+            "identifier": "C2387041635-GES_DISC",
+            "issued": "2018-03-21",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/W66HUFU4KYRQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "VISSRGOES3IMIR",
             "spatial": "135.0 -90.0 -45.0 90.0",
+            "temporal": "1979-05-02T00:00:00Z/1979-06-07T23:59:59.999Z",
             "theme": [
                 "GOES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VISSR/GOES-3 Infrared Imagery on 70mm Film V001 (VISSRGOES3IMIR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-2-ESC2-67P-V1.0",
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
+            "description": "This data set contains Spectroscopic, Continuum, and Engineering level 2 data, in the form of table files, taken during the COMET ESCORT 2 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-2-esc2-67p-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-2-ESC2-67P-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-2-esc2-67p-v1.0",
-            "description": "This data set contains Spectroscopic, Continuum, and Engineering level 2 data, in the form of table files, taken during the COMET ESCORT 2 phase of the Rosetta mission to comet 67P/CHURYUMOV-GERASIMENKO by the MIRO instrument.",
-            "title": "ROSETTA-ORBITER 67P MIRO 2 ESC2 67P V1.0",
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
+            "title": "ROSETTA-ORBITER 67P MIRO 2 ESC2 67P V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-APD-POLARIMETRY-V3.0",
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
+            "description": "The Asteroid Polarimetric Database (APD) is compiled by Dmitrij Lupishko of Kharkov University. This database tabulates the original data comprising degree of polarization as a function of phase angle of the asteroid, and additional parameters where available. This data set, together with 'polar.tab' containing the TRIAD polarimetry, includes most if not all existing asteroid polarimetry data published by 1998. The APD is an ongoing compilation and this data set will be updated yearly.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-apd-polarimetry-v3.0_jsse-n6zn",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-APD-POLARIMETRY-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-apd-polarimetry-v3.0_jsse-n6zn",
-            "description": "The Asteroid Polarimetric Database (APD) is compiled by Dmitrij Lupishko of Kharkov University. This database tabulates the original data comprising degree of polarization as a function of phase angle of the asteroid, and additional parameters where available. This data set, together with 'polar.tab' containing the TRIAD polarimetry, includes most if not all existing asteroid polarimetry data published by 1998. The APD is an ongoing compilation and this data set will be updated yearly.",
-            "title": "ASTEROID POLARIMETRIC DATABASE V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID POLARIMETRIC DATABASE V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1808440897-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "ALOS AVNIR-2 OBS ORI",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1808440897-ASF",
             "issued": "2020-06-04",
-            "temporal": "2006-01-23T00:00:00Z/2011-05-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-24",
             "keyword": [
                 "earth science",
                 "topography",
@@ -994621,199 +994633,163 @@
                 "geomorphic landforms/processes",
                 "visible wavelengths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1808440897-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-24",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1808440897-ASF",
-            "description": "ALOS AVNIR-2 OBS ORI",
-            "title": "ALOS_AVNIR_OBS_ORI",
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
+            "temporal": "2006-01-23T00:00:00Z/2011-05-23T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ALOS_AVNIR_OBS_ORI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D07.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Parameter1 Band3 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D07.061. https://doi.org/10.5067/MODIS/MCD43D07.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "surface radiative properties",
-                "earth science",
-                "land surface",
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
-            "identifier": "C2539207575-LPCLOUD",
-            "description": "The MCD43D07 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameter dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. Each of the three model parameters (isotropic, volumetric, and geometric) for each of the MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands included in MCD43C1 (https://doi.org/10.5067/MODIS/MCD43C1.061) are stored in a separate file as MCD43D01 through MCD43D30. \r\n\r\nMCD43D07 is the BRDF isotropic parameter for MODIS band 3. The isotropic parameter, in conjunction with the volumetric and geometric parameters, is used to derive the BRDF/Albedo values for MODIS band 3. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
```

