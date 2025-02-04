# Change History for nasa.json (Part 118)

### Changes from 31606f9 to dd2190f (Part 107/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                     "title": "Access this dataset's users feedback page"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S4G/MFOV_SF_ZG_1/",
-                    "description": "ASDC Direct Data Download for ERBE_S4G_MFOV_SF_ZG_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ERBE_S4G_MFOV_SF_ZG_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S4G/MFOV_SF_ZG_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000772-LARC_ASDC",
+            "issued": "1999-06-14",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ERBE/S4G_MFOV_SF_ZG_L3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-01-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1984-11-05T00:00:00Z/1990-02-28T23:59:59.999Z",
             "theme": [
                 "ERBE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Earth Radiation Budget Experiment (ERBE) Nonscanner S-4G MediumField of View (MFOV) Shape Factor (SF) Zonal and Global Averages"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC1-MTP010-V2.0",
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
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT  1 MTP010 phase, which occurred from 2014-11-22 to 2014-12-20 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc1-mtp010-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC1-MTP010-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc1-mtp010-v2.0",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT  1 MTP010 phase, which occurred from 2014-11-22 to 2014-12-20 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 1 MTP010 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 1 MTP010 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0816-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-29T09:28:00.000 to 2015-05-29T11:34:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0816-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0816-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0816-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-29T09:28:00.000 to 2015-05-29T11:34:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0816 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0816 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PLS-5-RDR-IONLMODE-48SEC-V1.0",
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
-                "neptune"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set gives the best available values for ion densities, temperatures, and velocities near Neptune derived from data obtained by the Voyager 2 plasma experiment.  All parameters are obtained by fitting the observed spectra (current as a function of energy) with Maxwellian plasma distributions, using a non-linear least squares fitting routine to find the plasma parameters which, when coupled with the full instrument response, best simulate the data. The PLS instrument measures energy/charge, so composition is not uniquely determined but can be deduced in some cases by the separation of the observed current peaks in energy (assuming the plasma is co-moving).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pls-5-rdr-ionlmode-48sec-v1.0_n6qy-hq9b",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "neptune"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PLS-5-RDR-IONLMODE-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pls-5-rdr-ionlmode-48sec-v1.0_n6qy-hq9b",
-            "description": "This data set gives the best available values for ion densities, temperatures, and velocities near Neptune derived from data obtained by the Voyager 2 plasma experiment.  All parameters are obtained by fitting the observed spectra (current as a function of energy) with Maxwellian plasma distributions, using a non-linear least squares fitting routine to find the plasma parameters which, when coupled with the full instrument response, best simulate the data. The PLS instrument measures energy/charge, so composition is not uniquely determined but can be deduced in some cases by the separation of the observed current peaks in energy (assuming the plasma is co-moving).",
-            "title": "VG2 NEP PLS DERIVED RDR ION OUTBND MAGSHTH L-MODE 48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 NEP PLS DERIVED RDR ION OUTBND MAGSHTH L-MODE 48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000015-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "2008-10-05",
-            "temporal": "2008-10-05T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C1000000015-CDDIS",
             "description": "Precise satellite orbits derived from analysis of Global Navigation Satellite System (GNSS) data. Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce precise orbits identifying the position and velocity of the GNSS satellites. The orbits derived from real-time data streams are used for comparison purposes.",
-            "title": "CDDIS_GNSS_products_orbit_realtime",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1121836,25 +1121819,53 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000015-CDDIS",
+            "issued": "2008-10-05",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000015-CDDIS.html",
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
+            "temporal": "2008-10-05T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_GNSS_products_orbit_realtime"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the first full catalog of LAT sources, based on the first eleven months of survey data. For a full explanation about the catalog and its construction see the LAT 1-year Catalog Paper.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://heasarc.gsfc.nasa.gov/cgi-bin/W3Browse/w3query.pl?&tablehead=name%3Dheasarc%5Ffermilpsc%26description%3DFermi+LAT+Point+Source+Catalog%26url%3Dhttp%3A%2F%2Fheasarc%2Egsfc%2Enasa%2Egov%2FW3Browse%2Ffermi%2Ffermilpsc%2Ehtml%26archive%3DY%26radius%3D10%26mission%3DFERMI%26priority%3D5&mission=FERMI&Action=More+Options&Action=Parameter+Search&ConeAdd=1",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000221__1",
             "issued": "2018-06-25",
-            "temporal": "2008-08-01/2009-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "acd",
                 "high-energy",
@@ -1121872,575 +1121883,566 @@
                 "bursts",
                 "balloon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000221__1",
-            "description": "The Fermi Gamma-ray Space Telescope (Fermi) Large Area Telescope (LAT) is a successor to EGRET, with greatly improved sensitivity, resolution, and energy range. This web page presents the first full catalog of LAT sources, based on the first eleven months of survey data. For a full explanation about the catalog and its construction see the LAT 1-year Catalog Paper.",
-            "title": "LAT 1-year Point Source Catalog",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://heasarc.gsfc.nasa.gov/cgi-bin/W3Browse/w3query.pl?&tablehead=name%3Dheasarc%5Ffermilpsc%26description%3DFermi+LAT+Point+Source+Catalog%26url%3Dhttp%3A%2F%2Fheasarc%2Egsfc%2Enasa%2Egov%2FW3Browse%2Ffermi%2Ffermilpsc%2Ehtml%26archive%3DY%26radius%3D10%26mission%3DFERMI%26priority%3D5&mission=FERMI&Action=More+Options&Action=Parameter+Search&ConeAdd=1",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-01/2009-07-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT 1-year Point Source Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-07-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Aldino_Data_1.",
-            "issued": "2021-06-10",
-            "temporal": "2011-06-17T00:00:00Z/2011-08-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-20",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
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
-            "identifier": "C2359074792-LARC_ASDC",
             "description": "DISCOVERAQ_Maryland_Ground_Aldino_Data contains data collected at the Aldino ground site during the Maryland (Baltimore-Washington) deployment of NASA's DISCOVER-AQ field study. This data product contains data for only the Maryland deployment and data collection is complete.\r\n\r\nUnderstanding the factors that contribute to near surface pollution is difficult using only satellite-based observations. The incorporation of surface-level measurements from aircraft and ground-based platforms provides the crucial information necessary to validate and expand upon the use of satellites in understanding near surface pollution. Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) was a four-year campaign conducted in collaboration between NASA Langley Research Center, NASA Goddard Space Flight Center, NASA Ames Research Center, and multiple universities to improve the use of satellites to monitor air quality for public health and environmental benefit. Through targeted airborne and ground-based observations, DISCOVER-AQ enabled more effective use of current and future satellites to diagnose ground level conditions influencing air quality.\r\n\r\nDISCOVER-AQ employed two NASA aircraft, the P-3B and King Air, with the P-3B completing in-situ spiral profiling of the atmosphere (aerosol properties, meteorological variables, and trace gas species). The King Air conducted both passive and active remote sensing of the atmospheric column extending below the aircraft to the surface. Data from an existing network of surface air quality monitors, AERONET sun photometers, Pandora UV/vis spectrometers and model simulations were also collected. Further, DISCOVER-AQ employed many surface monitoring sites, with measurements being made on the ground, in conjunction with the aircraft. The B200 and P-3B conducted flights in Baltimore-Washington, D.C. in 2011, Houston, TX in 2013, San Joaquin Valley, CA in 2013, and Denver, CO in 2014. These regions were targeted due to being in violation of the National Ambient Air Quality Standards (NAAQS).\r\n\r\nThe first objective of DISCOVER-AQ was to determine and investigate correlations between surface measurements and satellite column observations for the trace gases ozone (O3), nitrogen dioxide (NO2), and formaldehyde (CH2O) to understand how satellite column observations can diagnose surface conditions. DISCOVER-AQ also had the objective of using surface-level measurements to understand how satellites measure diurnal variability and to understand what factors control diurnal variability. Lastly, DISCOVER-AQ aimed to explore horizontal scales of variability, such as regions with steep gradients and urban plumes.",
-            "title": "DISCOVER-AQ Maryland Deployment Aldino Ground Site Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Ground_Aldino_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FDISCOVERAQ_Maryland_Ground_Aldino_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
-                    "description": "DOI for DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2359074792-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2359074792-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Ground_Aldino_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/Maryland_Ground_Aldino_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2359074792-LARC_ASDC",
+            "issued": "2021-06-10",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_Maryland_Ground_Aldino_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.0 -85.0 30.0 -70.0 45.0 -70.0 45.0 -85.0 30.0 -85.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2011-06-17T00:00:00Z/2011-08-02T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ Maryland Deployment Aldino Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA209",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GLAS/ICESat L2 Global Antarctic and Greenland Ice Sheet Altimetry Data (HDF5) V034. Version 034. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ICESAT/GLAS/DATA209.",
-            "issued": "2003-02-20",
-            "temporal": "2003-02-20T00:00:00Z/2009-10-11T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-10-11",
-            "keyword": [
-                "earth science",
-                "sea ice",
-                "glaciers/ice sheets",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2153549818-NSIDC_CPRD",
             "description": "GLAH06 is used in conjunction with GLAH05 to create the Level-2 altimetry products. Level-2 altimetry data provide surface elevations for ice sheets (GLAH12), sea ice (GLAH13), land (GLAH14), and oceans (GLAH15). Data also include the laser footprint geolocation and reflectance, as well as geodetic, instrument, and atmospheric corrections for range measurements. The Level-2 elevation products, are regional products archived at 14 orbits per granule, starting and stopping at the same demarcation (\u00b1 50\u00b0 latitude) as GLAH05 and GLAH06. Each regional product is processed with algorithms specific to that surface type. Surface type masks define which data are written to each of the products. If any data within a given record fall within a specific mask, the entire record is written to the product. Masks can overlap: for example, non-land data in the sea ice region may be written to the sea ice and ocean products. This means that an algorithm may write the same data to more than one Level-2 product. In this case, different algorithms calculate the elevations in their respective products. The surface type masks are versioned and archived at NSIDC, so users can tell which data to expect in each product.  Each data granule has an associated browse product.",
-            "title": "GLAS/ICESat L2 Global Antarctic and Greenland Ice Sheet Altimetry Data (HDF5) V034",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA209",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FICESAT%2FGLAS%2FDATA209",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLAH12+V034",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLAH12+V034",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA209",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA209",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA209",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ICESAT/GLAS/DATA209",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2153549818-NSIDC_CPRD",
+            "issued": "2003-02-20",
+            "keyword": [
+                "earth science",
+                "sea ice",
+                "glaciers/ice sheets",
+                "terrestrial hydrosphere",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ICESAT/GLAS/DATA209",
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
+            "title": "GLAS/ICESat L2 Global Antarctic and Greenland Ice Sheet Altimetry Data (HDF5) V034"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/MBON/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/MBON/DATA001.",
-            "issued": "2015-07-27",
-            "temporal": "2015-07-27T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "oceans",
-                "ocean temperature",
-                "earth science",
-                "salinity/density",
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
-            "identifier": "C1719969316-OB_DAAC",
             "description": "The Marine Biodiversity Observation Network (MBON) is a growing global initiative composed of regional networks of scientists, resource managers, and end-users working to integrate data from existing long-term programs to improve our understanding of changes and connections between marine biodiversity and ecosystem functions.",
-            "title": "Marine Biodiversity Observation Network (MBON)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMBON%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMBON%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MBON/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MBON/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1719969316-OB_DAAC",
+            "issued": "2015-07-27",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "ocean temperature",
+                "earth science",
+                "salinity/density",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/MBON/DATA001",
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
+            "temporal": "2015-07-27T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Marine Biodiversity Observation Network (MBON)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-RVM1-RENDEZMANOEUVRE1-V1.0",
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
+            "description": "Payload Checkout 13 (PC13) was the final Cruise Phase Checkout of several payload checkouts performed with the Rosetta Payload. Since PC13 was scheduled as the final Cruise Phase Checkout, a number of additional payload operations were also executed to close out pending and essential requirements, and/or configure instruments for the upcoming Deep Space Hibernation Phase. Given the importance of this final checkout all Rosetta payload, except Osiris, took part in this scenario The Payload Checkout 13 ran for 9 consecutive days starting on the 1st December 2010 until the 9th December 2010. An RSI passive checkout was also completed on 14th December 2010. The Scenario was covered by dedicated NNO and DSN. During PC13 GIADA performs only a  passive test (GD01) similar to the previous Passive Payload Checkouts. This passive test (GD01), which includes standard procedures and full functional verification, was executed by switching on Main and Redundant I/Fs in sequence and executing similar procedures for the two cases. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-rvm1-rendezmanoeuvre1-v1.0_n6vm-cd48",
+            "issued": "2021-05-21",
+            "keyword": [
+                "checkout",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-RVM1-RENDEZMANOEUVRE1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-rvm1-rendezmanoeuvre1-v1.0_n6vm-cd48",
-            "description": "Payload Checkout 13 (PC13) was the final Cruise Phase Checkout of several payload checkouts performed with the Rosetta Payload. Since PC13 was scheduled as the final Cruise Phase Checkout, a number of additional payload operations were also executed to close out pending and essential requirements, and/or configure instruments for the upcoming Deep Space Hibernation Phase. Given the importance of this final checkout all Rosetta payload, except Osiris, took part in this scenario The Payload Checkout 13 ran for 9 consecutive days starting on the 1st December 2010 until the 9th December 2010. An RSI passive checkout was also completed on 14th December 2010. The Scenario was covered by dedicated NNO and DSN. During PC13 GIADA performs only a  passive test (GD01) similar to the previous Passive Payload Checkouts. This passive test (GD01), which includes standard procedures and full functional verification, was executed by switching on Main and Redundant I/Fs in sequence and executing similar procedures for the two cases. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
-            "title": "ROSETTA-ORBITER CHECK GIADA 2 RVM1 RENDEZMANOEUVRE1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK GIADA 2 RVM1 RENDEZMANOEUVRE1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-PRL-MTP008-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the PRELANDING MTP008 phase, which occurred from 2014-09-23 to 2014-10-24",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-prl-mtp008-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-PRL-MTP008-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-prl-mtp008-v1.0",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the PRELANDING MTP008 phase, which occurred from 2014-09-23 to 2014-10-24",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 2 PRELANDING MTP008 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 2 PRELANDING MTP008 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0849-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-19T03:44:00.000 to 2015-06-19T11:14:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0849-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0849-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0849-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-19T03:44:00.000 to 2015-06-19T11:14:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0849 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0849 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/283",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fitzsimmons, M. 1998. BOREAS Prince Albert National Park Forest Cover Data in Vector Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/283",
-            "issued": "2024-03-24",
-            "temporal": "1978-01-01T00:00:00Z/1994-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-25",
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
-            "identifier": "C2846961321-ORNL_CLOUD",
             "description": "Detailed canopy, understory, and ground cover, height, density, and condition information for PANP in the western part of the BOREAS SSA in vector form.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Prince Albert National Park Forest Cover Data in Vector Format",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F283",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F283",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/panpfcov/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/panpfcov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/PANP_For_Cov.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/PANP_For_Cov.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/283",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/283",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/0_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/0_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/panpfcov_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/panpfcov_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/panp_comp_readme",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/panp_comp_readme",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/PANP_For_Cov.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/PANP_For_Cov.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/PANP_For_Cov.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/PANP_For_Cov.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/PANP_For_Cov.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/panpfcov/comp/PANP_For_Cov.txt",
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
+            "identifier": "C2846961321-ORNL_CLOUD",
+            "issued": "2024-03-24",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/283",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-106.8 53.56 -105.99 54.33",
+            "temporal": "1978-01-01T00:00:00Z/1994-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Prince Albert National Park Forest Cover Data in Vector Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Asmallbodiesoccultations&version=1.0",
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
-                "none"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set is intended to include all reported timings of observed asteroid,\nplanet, and planetary satellite occultation events as well as occultation axes\nderived from those timings by David W. Dunham and David Herald. This version is\ncomplete through the end of 2016.",
+            "identifier": "urn:nasa:pds:smallbodiesoccultations_n727-a33h",
+            "issued": "2018-06-26",
+            "keyword": [
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Asmallbodiesoccultations&version=1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:smallbodiesoccultations_n727-a33h",
-            "description": "This data set is intended to include all reported timings of observed asteroid,\nplanet, and planetary satellite occultation events as well as occultation axes\nderived from those timings by David W. Dunham and David Herald. This version is\ncomplete through the end of 2016.",
-            "title": "Asteroid Occultations V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "Asteroid Occultations V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT2-MTP030-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 2 MTP030 Phase from 01 Jun. 2016, 06:04:21 to 28 Jun. 2016, 23:17:54 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext2-mtp030-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "alpha lyr",
@@ -1122448,236 +1122450,246 @@
                 "zeta cas",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-EXT2-MTP030-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-ext2-mtp030-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the ROSETTA EXTENSION 2 MTP030 Phase from 01 Jun. 2016, 06:04:21 to 28 Jun. 2016, 23:17:54 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 2 MTP030 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 ROSETTA EXTENSION 2 MTP030 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MPF-M-RSS-1%2F5-RADIOTRACK-V1.0",
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
-                "mars pathfinder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Mars Pathfinder (MPF) Radio Science (RS) data archive contains both raw radio tracking data collected during the surface lifetime of the MPF Lander and results derived from those data. Results include rotation rate, rotation axis, and (jointly with Viking Lander data) the change in rotation rate for Mars. For more information on the investigations see [FOLKNERETAL1997A].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mpf-m-rss-1-5-radiotrack-v1.0_n73t-uk2x",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars pathfinder"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MPF-M-RSS-1%2F5-RADIOTRACK-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mpf-m-rss-1-5-radiotrack-v1.0_n73t-uk2x",
-            "description": "The Mars Pathfinder (MPF) Radio Science (RS) data archive contains both raw radio tracking data collected during the surface lifetime of the MPF Lander and results derived from those data. Results include rotation rate, rotation axis, and (jointly with Viking Lander data) the change in rotation rate for Mars. For more information on the investigations see [FOLKNERETAL1997A].",
-            "title": "MARS PATHFINDER RADIO TRACKING",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARS PATHFINDER RADIO TRACKING"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-3-CR4A-CALIB2-V1.0",
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
+            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the CRUISE 4-1\nmission phase where the primary target was the SOLAR WIND. It contains\ninstrument outputs in volts and amperes, calibrated and corrected for\ninstrument offsets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-3-cr4a-calib2-v1.0_n73u-xjhu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-3-CR4A-CALIB2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-3-cr4a-calib2-v1.0_n73u-xjhu",
-            "description": "This data set contains\nCALIBRATED data from Rosetta RPC-LAP, acquired during the CRUISE 4-1\nmission phase where the primary target was the SOLAR WIND. It contains\ninstrument outputs in volts and amperes, calibrated and corrected for\ninstrument offsets.",
-            "title": "ROSETTA-ORBITER SW RPCLAP 3\nCR4A CALIB2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SW RPCLAP 3\nCR4A CALIB2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_UWEC-Auto_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-11-05. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_UWEC-Auto_Data_1.",
-            "issued": "2020-09-08",
-            "temporal": "2017-06-02T00:00:00Z/2017-06-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-19",
-            "keyword": [
-                "air quality",
-                "atmospheric chemistry",
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
-            "identifier": "C1966380374-LARC_ASDC",
             "description": "LMOS_TraceGas_SurfaceMobile_UWEC-Auto_Data_1 is the Lake Michigan Ozone Study (LMOS) trace gas surface mobile data collected onboard the University of Wisconsin-Eau Claire (UWEC) surface mobile platform during the LMOS field campaign. This product is a result of a joint effort across multiple agencies, including NASA, NOAA, the EPA, Electric Power Research Institute (EPRI), National Science Foundation (NSF), Lake Michigan Air Directors Consortium (LADCO) and its member states, and several research groups at universities. Data collection for this product is complete.\r\n\r\nElevated spring and summertime ozone levels remain a challenge along the coast of Lake Michigan, with a number of monitors recording levels/amounts exceeding the 2015 National Ambient Air Quality Standards (NAAQS) for ozone. The production of ozone over Lake Michigan, combined with onshore daytime \u201clake breeze\u201d airflow is believed to increase ozone concentrations at locations within a few kilometers off shore. This observed lake-shore gradient motivated the Lake Michigan Ozone Study (LMOS). Conducted from May through June 2017, the goal of LMOS was to better understand ozone formation and transport around Lake Michigan; in particular, why ozone concentrations are generally highest along the lakeshore and drop off sharply inland and why ozone concentrations peak in rural areas far from major emission sources. LMOS was a collaborative, multi-agency field study that provided extensive observational air quality and meteorology datasets through a combination of airborne, ship, mobile laboratories, and fixed ground-based observational platforms. Chemical transport models (CTMs) and meteorological forecast tools assisted in planning for day-to-day measurement strategies. The long term goals of the LMOS field study were to improve modeled ozone forecasts for this region, better understand ozone formation and transport around Lake Michigan, provide a better understanding of the lakeshore gradient in ozone concentrations (which could influence how the Environmental Protection Agency (EPA) addresses future regional ozone issues), and provide improved knowledge of how emissions influence ozone formation in the region.",
-            "title": "LMOS Surface Mobile University of Wisconsin-Eau Claire Ozone Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLMOS%2FTraceGas_SurfaceMobile_UWEC-Auto_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FLMOS%2FTraceGas_SurfaceMobile_UWEC-Auto_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_UWEC-Auto_Data_1",
-                    "description": "DOI data set landing page for LMOS_TraceGas_SurfaceMobile_UWEC-Auto_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for LMOS_TraceGas_SurfaceMobile_UWEC-Auto_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_UWEC-Auto_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.ladco.org/wp-content/uploads/Research/LMOS2017/LMOS_LADCO_report_revision_apr2019_final.pdf",
-                    "description": "LMOS Lake Michigan Air Directors Consortium Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Lake Michigan Air Directors Consortium Mission Overview",
+                    "downloadURL": "https://www.ladco.org/wp-content/uploads/Research/LMOS2017/LMOS_LADCO_report_revision_apr2019_final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-aids-study-of-lake-michigan-high-ozone-events",
-                    "description": "LMOS Nasa.gov \u201cNASA Aids Study of Lake Michigan High-Ozone Events\u201d Article",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Nasa.gov \u201cNASA Aids Study of Lake Michigan High-Ozone Events\u201d Article",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-aids-study-of-lake-michigan-high-ozone-events",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LMOS/2017",
-                    "description": "LMOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/LMOS/2017",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1966380374-LARC_ASDC",
-                    "description": "Earthdata Search for LMOS_TraceGas_SurfaceMobile_UWEC-Auto_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LMOS_TraceGas_SurfaceMobile_UWEC-Auto_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1966380374-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LMOS/pdocuments",
-                    "description": "LMOS Support Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "LMOS Support Documentation",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LMOS/pdocuments",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LMOS/TraceGas_SurfaceMobile_UWEC-Auto_Data_1/",
-                    "description": "ASDC Direct Data Download for LMOS_TraceGas_SurfaceMobile_UWEC-Auto_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LMOS_TraceGas_SurfaceMobile_UWEC-Auto_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LMOS/TraceGas_SurfaceMobile_UWEC-Auto_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1966380374-LARC_ASDC",
+            "issued": "2020-09-08",
+            "keyword": [
+                "air quality",
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/LMOS/TraceGas_SurfaceMobile_UWEC-Auto_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>40.0 -90.0 40.0 -85.0 45.0 -85.0 45.0 -90.0 40.0 -90.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2017-06-02T00:00:00Z/2017-06-17T23:59:59.999Z",
             "theme": [
                 "LMOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LMOS Surface Mobile University of Wisconsin-Eau Claire Ozone Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/n755-avyb",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Anita Harrell",
+                "hasEmail": "mailto:Anita.Harrell@nasa.gov"
+            },
+            "description": "Workforce Information Cubes for NASA, sourced from NASA's personnel/payroll system, gives data about who is working where and on what. Includes records for every civil service employee in NASA, snapshots of workforce composition as of certain dates, and data on personnel transactions, such as hires, losses and promotions. Updates occur every 2 weeks.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://wicn.nssc.nasa.gov/wicn_cubes.html",
+                    "mediaType": "image/jpg"
+                }
+            ],
+            "identifier": "NASA-0000116",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "aeronautics",
                 "disasters",
@@ -1122688,67 +1122700,32 @@
                 "biodiversity",
                 "deployment"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Anita Harrell",
-                "hasEmail": "mailto:Anita.Harrell@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/n755-avyb",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000116",
-            "description": "Workforce Information Cubes for NASA, sourced from NASA's personnel/payroll system, gives data about who is working where and on what. Includes records for every civil service employee in NASA, snapshots of workforce composition as of certain dates, and data on personnel transactions, such as hires, losses and promotions. Updates occur every 2 weeks.",
-            "title": "Workforce Information Cubes for NASA",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://wicn.nssc.nasa.gov/wicn_cubes.html",
-                    "mediaType": "image/jpg"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Workforce Information Cubes for NASA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1233768983-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AIRS Science Team/Moustafa Chahine. 2007-07-26. AIRVBQAP_NRT. Version 005. AIRS/Aqua L1B Near Real Time (NRT) Visible/Near Infrared (VIS/NIR) quality assurance subset V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/AIRVBQAP_NRT_005.html. Digital Science Data.",
-            "issued": "2024-07-03",
-            "temporal": "2015-12-15T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-07",
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
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
-            "identifier": "C1233768983-GES_DISC",
-            "description": "The AIRS Level 1B Near Real Time (NRT) product (AIRVBQAP_NRT_005) differs from the routine product (AIRVBQAP_005) in 2 ways to meet the three hour latency requirements of the Land Atmosphere NRT Capability Earth Observing System (LANCE): (1) The NRT granules are produced without previous or subsequent granules if those granules are not available within 5 minutes, (2) the predictive ephemeris/attitude data are used rather than the definitive ephemeris/attitude. The consequences of these differences are described in the AIRS Near Real Time (NRT) data products document. The Atmospheric Infrared Sounder (AIRS) Visible/Near Infrared (VIS/NIR) instrument in combination with the AIRS Infrared Spectrometer, the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB) constitute an innovative atmospheric sounding group aboard the Earth Observing System (EOS) Aqua platform in a near-polar Sun-synchronous orbit with a 1:30 AM/PM equator crossing time and an ~705 km altitude. The AIRS Visible/Near Infrared (VIS/NIR) Level 1B QA Subset contains Quality Assurance (QA) parameters that a may use of filter AIRS VIS/NIR Level 1B radiance data to create a subset of analysis. It includes \"state\" that user should check before using any VIS/NIR Level 1B data radiance and \"glintlat\", \"glintlon\", and \"sun_glint_distant\" that users can use to check for possibility of solar glint contamination. AIRS VIS/NIR Level 1B radiance data can be found in AIRVBRAD.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRVBQAP_NRT",
             "creator": "AIRS Science Team/Moustafa Chahine",
-            "title": "AIRS/Aqua L1B Near Real Time (NRT) Visible/Near Infrared (VIS/NIR) quality assurance subset V005 (AIRVBQAP_NRT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRVBQAP_NRT_005.gif",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The AIRS Level 1B Near Real Time (NRT) product (AIRVBQAP_NRT_005) differs from the routine product (AIRVBQAP_005) in 2 ways to meet the three hour latency requirements of the Land Atmosphere NRT Capability Earth Observing System (LANCE): (1) The NRT granules are produced without previous or subsequent granules if those granules are not available within 5 minutes, (2) the predictive ephemeris/attitude data are used rather than the definitive ephemeris/attitude. The consequences of these differences are described in the AIRS Near Real Time (NRT) data products document. The Atmospheric Infrared Sounder (AIRS) Visible/Near Infrared (VIS/NIR) instrument in combination with the AIRS Infrared Spectrometer, the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB) constitute an innovative atmospheric sounding group aboard the Earth Observing System (EOS) Aqua platform in a near-polar Sun-synchronous orbit with a 1:30 AM/PM equator crossing time and an ~705 km altitude. The AIRS Visible/Near Infrared (VIS/NIR) Level 1B QA Subset contains Quality Assurance (QA) parameters that a may use of filter AIRS VIS/NIR Level 1B radiance data to create a subset of analysis. It includes \"state\" that user should check before using any VIS/NIR Level 1B data radiance and \"glintlat\", \"glintlon\", and \"sun_glint_distant\" that users can use to check for possibility of solar glint contamination. AIRS VIS/NIR Level 1B radiance data can be found in AIRVBRAD.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1122757,73 +1122734,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRVBQAP_NRT_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRVBQAP_NRT_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRVBQAP_NRT.005/",
-                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS. User registration is required. Register for a username and password at https://urs.eosdis.nasa.gov/users/new",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_NRT/AIRVBQAP_NRT.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRVBQAP_NRT.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://discnrt1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_NRT/AIRVBQAP_NRT.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRVBQAP_NRT+005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRVBQAP_NRT+005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
-                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument, algorithms, and other AIRS related activities can be found.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument, algorithms, and other AIRS related activities can be found.",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRVBRAD.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRVBRAD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/nrt_memo_v6.pdf",
-                    "description": "Memo on NRT vs Standard Product",
                     "@type": "dcat:Distribution",
+                    "description": "Memo on NRT vs Standard Product",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/nrt_memo_v6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRVBQAP_NRT_005.html",
-                    "description": "AIRS AIRVBQAP_NRT information page",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS AIRVBQAP_NRT information page",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRVBQAP_NRT_005.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
@@ -1122833,577 +1122810,580 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRVBQAP_NRT_005.gif",
+            "identifier": "C1233768983-GES_DISC",
+            "issued": "2024-07-03",
+            "keyword": [
+                "infrared wavelengths",
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1233768983-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-08-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRVBQAP_NRT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-12-15T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "Aqua",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L1B Near Real Time (NRT) Visible/Near Infrared (VIS/NIR) quality assurance subset V005 (AIRVBQAP_NRT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHAAO-4BC21",
             "citation": "NOAA National Centers for Environmental Information. 2020-04-22. Daily L4 in situ and AVHRR OISST 0.25 degree. Version 2.1. Daily L4 Optimally Interpolated SST (OISST) In situ and AVHRR Analysis. National Centers for Environmental Information, Asheville, NC, USA. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHAAO-4BC21.",
-            "issued": "2020-04-01",
-            "temporal": "2016-01-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-04-01",
-            "references": [
-                "https://doi.org/10.1175/2007JCLI1824.1"
-            ],
-            "keyword": [
-                "ocean temperature",
-                "earth science",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036881712-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) global Level 4 sea surface temperature dataset is produced daily on a 0.25 degree grid at the NOAA National Centers for Environmental Information. This product uses optimal interpolation (OI) by interpolating and extrapolating SST observations from different sources, resulting in a smoothed complete field. The sources of data are satellite (AVHRR) and in situ platforms (i.e., ships, buoys, and Argo floats above 5m depth), and the specific datasets employed may change over time. In the regions with sea-ice concentration higher than 30%, freezing points of seawater are used to generate proxy SSTs.  A preliminary version of this dataset is produced in near-real time (1-day latency), and then replaced with a final version after 2 weeks. The v2.1 (Huang et al. 2021) is updated from the previous AVHRR_OI-NCEI-L4-GLOB-v2.0 data. Major improvements include: 1) In-situ ship and buoy data changed from the NCEP Traditional Alphanumeric Codes (TAC) to the NCEI merged TAC + Binary Universal Form for the Representation (BUFR) data, with large increases of buoy data included to correct satellite SST biases; 2) Addition of Argo float observed SST data as well, for further correction of satellite SST biases; 3) Satellite input from the METOP-A and NOAA-19 to METOP-A and METOP-B, removing degraded satellite data; 4) Revised ship-buoy SST corrections for improved accuracy; and 5) Revised sea-ice-concentration to SST conversion to remove warm biases in the Arctic region. These updates only apply to data after January 1st, 2016. The data pre 2016 are still the same as v2.0 except for metadata upgrades. NCEI has panned to update the entire dataset from 1982 to fix the In-Situ data ingest and bias correction which exist prior 2016.",
-            "release-place": "National Centers for Environmental Information, Asheville, NC, USA",
-            "series-name": "Daily L4 in situ and AVHRR OISST 0.25 degree",
             "creator": "NOAA National Centers for Environmental Information",
-            "title": "GHRSST Level 4 AVHRR_OI Global Blended Sea Surface Temperature Analysis (GDS2) from NCEI",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR_OI-NCEI-L4-GLOB-v2.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) global Level 4 sea surface temperature dataset is produced daily on a 0.25 degree grid at the NOAA National Centers for Environmental Information. This product uses optimal interpolation (OI) by interpolating and extrapolating SST observations from different sources, resulting in a smoothed complete field. The sources of data are satellite (AVHRR) and in situ platforms (i.e., ships, buoys, and Argo floats above 5m depth), and the specific datasets employed may change over time. In the regions with sea-ice concentration higher than 30%, freezing points of seawater are used to generate proxy SSTs.  A preliminary version of this dataset is produced in near-real time (1-day latency), and then replaced with a final version after 2 weeks. The v2.1 (Huang et al. 2021) is updated from the previous AVHRR_OI-NCEI-L4-GLOB-v2.0 data. Major improvements include: 1) In-situ ship and buoy data changed from the NCEP Traditional Alphanumeric Codes (TAC) to the NCEI merged TAC + Binary Universal Form for the Representation (BUFR) data, with large increases of buoy data included to correct satellite SST biases; 2) Addition of Argo float observed SST data as well, for further correction of satellite SST biases; 3) Satellite input from the METOP-A and NOAA-19 to METOP-A and METOP-B, removing degraded satellite data; 4) Revised ship-buoy SST corrections for improved accuracy; and 5) Revised sea-ice-concentration to SST conversion to remove warm biases in the Arctic region. These updates only apply to data after January 1st, 2016. The data pre 2016 are still the same as v2.0 except for metadata upgrades. NCEI has panned to update the entire dataset from 1982 to fix the In-Situ data ingest and bias correction which exist prior 2016.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHAAO-4BC21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHAAO-4BC21",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "GHRSST Project Information",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project Information",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/NCEI_AVHRR-OI_SST_ATBD.pdf",
-                    "description": "Daily 1/4 Degree Optimum Interpolation Sea Surface Temperature (OISST)- ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "Daily 1/4 Degree Optimum Interpolation Sea Surface Temperature (OISST)- ATBD",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/NCEI_AVHRR-OI_SST_ATBD.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://doi.org/10.5194/essd-8-165-2016",
-                    "description": "A long-term record of blended satellite and in situ sea-surface temperature for climate monitoring, modeling and environmental studies, Earth Syst. Sci. Data, 8, 165-176, 2016",
                     "@type": "dcat:Distribution",
+                    "description": "A long-term record of blended satellite and in situ sea-surface temperature for climate monitoring, modeling and environmental studies, Earth Syst. Sci. Data, 8, 165-176, 2016",
+                    "downloadURL": "https://doi.org/10.5194/essd-8-165-2016",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR_OI-NCEI-L4-GLOB-v2.1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR_OI-NCEI-L4-GLOB-v2.1.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036881712-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036881712-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036881712-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036881712-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR_OI-NCEI-L4-GLOB-v2.1.jpg",
+            "identifier": "C2036881712-POCLOUD",
+            "issued": "2020-04-01",
+            "keyword": [
+                "ocean temperature",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHAAO-4BC21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1175/2007JCLI1824.1"
+            ],
+            "release-place": "National Centers for Environmental Information, Asheville, NC, USA",
+            "series-name": "Daily L4 in situ and AVHRR OISST 0.25 degree",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-01-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 4 AVHRR_OI Global Blended Sea Surface Temperature Analysis (GDS2) from NCEI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0423-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-12T03:05:00.000 to 2014-11-12T07:04:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0423-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0423-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0423-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-12T03:05:00.000 to 2014-11-12T07:04:59.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0423 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0423 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD17A2HGF.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Steve Running, Maosheng Zhao. 2021-03-15. MODIS/Terra Gross Primary Productivity Gap-Filled 8-Day L4 Global 500m SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD17A2HGF.061. https://doi.org/10.5067/MODIS/MOD17A2HGF.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-03-15",
-            "temporal": "2000-01-01T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-15",
-            "keyword": [
-                "earth science",
-                "national geospatial data asset",
-                "ngda",
-                "biosphere",
-                "ecological dynamics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Steve Running",
                 "hasEmail": "mailto:swr@ntsg.umt.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2565791029-LPCLOUD",
-            "description": "The Terra Moderate Resolution Imaging Spectroradiometer (MODIS) MOD17A2HGF Version 6.1 Gross Primary Productivity (GPP) product is a cumulative 8-day composite of values with 500 meter (m) pixel size based on the radiation use efficiency concept that can be potentially used as inputs to data models to calculate terrestrial energy, carbon, water cycle processes, and biogeochemistry of vegetation. The data product includes information about GPP and Net Photosynthesis (PSN). The PSN band values are the GPP less the Maintenance Respiration (MR). The data product also contains a PSN Quality Control (QC) layer. The quality layer contains quality information for both the GPP and the PSN.\n\nThe MOD17A2HGF will be generated at the end of each year when the entire yearly 8-day MOD15A2H (https://doi.org/10.5067/modis/mod15a2h.061) is available. Hence, the gap-filled MOD17A2HGF is the improved MOD17, which has cleaned the poor-quality inputs from 8-day Leaf Area Index and Fraction of Photosynthetically Active Radiation  (FPAR/LAI) based on the Quality Control (QC) label for every pixel. If any LAI/FPAR pixel did not meet the quality screening criteria, its value is determined through linear interpolation. However, users cannot get MOD17A2HGF in near-real time because it will be generated only at the end of a given year.\n\nStage 3 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) validation has been achieved for MOD17 products.\n\nImprovements/Changes from Previous Versions\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\n* The product uses Climatology LAI/FPAR as back up to the operational LAI/FPAR.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Steve Running, Maosheng Zhao",
-            "title": "MODIS/Terra Gross Primary Productivity Gap-Filled 8-Day L4 Global 500m SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2600672346-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Terra Moderate Resolution Imaging Spectroradiometer (MODIS) MOD17A2HGF Version 6.1 Gross Primary Productivity (GPP) product is a cumulative 8-day composite of values with 500 meter (m) pixel size based on the radiation use efficiency concept that can be potentially used as inputs to data models to calculate terrestrial energy, carbon, water cycle processes, and biogeochemistry of vegetation. The data product includes information about GPP and Net Photosynthesis (PSN). The PSN band values are the GPP less the Maintenance Respiration (MR). The data product also contains a PSN Quality Control (QC) layer. The quality layer contains quality information for both the GPP and the PSN.\n\nThe MOD17A2HGF will be generated at the end of each year when the entire yearly 8-day MOD15A2H (https://doi.org/10.5067/modis/mod15a2h.061) is available. Hence, the gap-filled MOD17A2HGF is the improved MOD17, which has cleaned the poor-quality inputs from 8-day Leaf Area Index and Fraction of Photosynthetically Active Radiation  (FPAR/LAI) based on the Quality Control (QC) label for every pixel. If any LAI/FPAR pixel did not meet the quality screening criteria, its value is determined through linear interpolation. However, users cannot get MOD17A2HGF in near-real time because it will be generated only at the end of a given year.\n\nStage 3 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) validation has been achieved for MOD17 products.\n\nImprovements/Changes from Previous Versions\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\n* The product uses Climatology LAI/FPAR as back up to the operational LAI/FPAR.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD17A2HGF.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD17A2HGF.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD17A2HGF.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD17A2HGF.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565791029-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565791029-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD17A2HGF.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD17A2HGF.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/972/MOD17_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/95/MOD17_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/95/MOD17_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MOD17A2HGF",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MOD17A2HGF",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for the MODIS Gross and Net Primary Productivity data products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the MODIS Gross and Net Primary Productivity data products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD17",
-                    "description": "Further details regarding MODIS land product validation for the MOD17 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MOD17 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD17",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOLT/MOD17A2HGF.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOLT/MOD17A2HGF.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2600672346-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2600672346-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2600672346-LPCLOUD?h=85&w=85",
+            "identifier": "C2565791029-LPCLOUD",
+            "issued": "2021-03-15",
+            "keyword": [
+                "earth science",
+                "national geospatial data asset",
+                "ngda",
+                "biosphere",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD17A2HGF.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-01-01T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Gross Primary Productivity Gap-Filled 8-Day L4 Global 500m SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/gr2e-dh86",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Frolking, S., T. Milliman, R. Mahtta, A. Paget, D. G. Long, and K. C. Seto. 2022-09-29. Global Monthly and Seasonal Urban and Land Backscatter Time Series, 1993-2020. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/gr2e-dh86. https://doi.org/10.7927/gr2e-dh86.",
-            "issued": "2022-09-30",
-            "temporal": "1993-01-01T00:00:00Z/2020-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-30",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
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
-            "identifier": "C2492953186-SEDAC",
-            "description": "The Global Monthly and Seasonal Urban and Land Backscatter Time Series, 1993-2020, is a multi-sensor, multi-decadal, data set of global microwave backscatter, for 1993 to 2020. It assembles data from C-band sensors onboard the European Remote Sensing Satellites (ERS-1 and ERS-2) covering 1993-2000, Advanced Scatterometer (ASCAT) onboard EUMETSAT satellites for 2007-2020, and the Ku-band sensor onboard the QuikSCAT satellite for 1999-2009, onto a common spatial grid (0.05 degree latitude /longitude resolution) and time step (both monthly and seasonal). Data are provided for all land (except high latitudes and islands), and for urban grid cells, based on a specific masking that removes grid cells with > 50% open water or < 20% built land. The all-land data allows users to choose and evaluate other urban masks. There is an offset between C-band and Ku-band backscatter from both vegetated and urban surfaces that is not spatially constant. There is a strong linear correlation (overall R-squared value = 0.69) between 2015 ASCAT urban backscatter and a continental-scale gridded product of building volume, across 8,450 urban grid cells (0.05 degree resolution) from large cities in Europe, China, and the United States.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Frolking, S., T. Milliman, R. Mahtta, A. Paget, D. G. Long, and K. C. Seto",
-            "title": "Global Monthly and Seasonal Urban and Land Backscatter Time Series, 1993-2020",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/urbanspatial/urbanspatial-urban-land-backscatter-time-series-1993-2020/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Monthly and Seasonal Urban and Land Backscatter Time Series, 1993-2020, is a multi-sensor, multi-decadal, data set of global microwave backscatter, for 1993 to 2020. It assembles data from C-band sensors onboard the European Remote Sensing Satellites (ERS-1 and ERS-2) covering 1993-2000, Advanced Scatterometer (ASCAT) onboard EUMETSAT satellites for 2007-2020, and the Ku-band sensor onboard the QuikSCAT satellite for 1999-2009, onto a common spatial grid (0.05 degree latitude /longitude resolution) and time step (both monthly and seasonal). Data are provided for all land (except high latitudes and islands), and for urban grid cells, based on a specific masking that removes grid cells with > 50% open water or < 20% built land. The all-land data allows users to choose and evaluate other urban masks. There is an offset between C-band and Ku-band backscatter from both vegetated and urban surfaces that is not spatially constant. There is a strong linear correlation (overall R-squared value = 0.69) between 2015 ASCAT urban backscatter and a continental-scale gridded product of building volume, across 8,450 urban grid cells (0.05 degree resolution) from large cities in Europe, China, and the United States.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fgr2e-dh86",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fgr2e-dh86",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/urbanspatial/urbanspatial-urban-land-backscatter-time-series-1993-2020/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/urbanspatial/urbanspatial-urban-land-backscatter-time-series-1993-2020/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/urbanspatial-urban-land-backscatter-time-series-1993-2020/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/urbanspatial-urban-land-backscatter-time-series-1993-2020/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/urbanspatial-urban-land-backscatter-time-series-1993-2020/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/urbanspatial-urban-land-backscatter-time-series-1993-2020/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/urbanspatial-urban-land-backscatter-time-series-1993-2020",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/urbanspatial-urban-land-backscatter-time-series-1993-2020",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/urbanspatial/urbanspatial-urban-land-backscatter-time-series-1993-2020/sedac-logo.jpg",
+            "identifier": "C2492953186-SEDAC",
+            "issued": "2022-09-30",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/gr2e-dh86",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1993-01-01T00:00:00Z/2020-12-31T00:00:00Z",
             "theme": [
                 "USPAT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Monthly and Seasonal Urban and Land Backscatter Time Series, 1993-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3321-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-04T05:45:02.000 to 2012-08-04T08:15:01.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3321-v1.0_n7cn-impj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3321-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3321-v1.0_n7cn-impj",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-08-04T05:45:02.000 to 2012-08-04T08:15:01.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3321 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3321 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SASSIE-JETSSP2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Drushka, Kyla. 2023-05-08. SASSIE Arctic Field Campaign Jet Surface Salinity Profiler Data Fall 2022. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, SASSIE Project Data Manager, Frederick Bingham. https://doi.org/10.5067/SASSIE-JETSSP2. https://doi.org/10.5067/SASSIE-JETSSP2.",
-            "issued": "2022-09-10",
-            "temporal": "2022-09-10T23:00:00Z/2022-09-26T20:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-26",
-            "references": [
-                "https://doi.org/10.5670/oceanog.2019.215"
-            ],
-            "keyword": [
-                "atmospheric pressure",
-                "atmospheric winds",
-                "earth science",
-                "salinity/density",
-                "atmospheric temperature",
-                "atmosphere",
-                "oceans",
-                "ocean temperature"
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
-            "identifier": "C2624096959-POCLOUD",
-            "description": "The Salinity and Stratification at the Sea Ice Edge (SASSIE) project is a NASA experiment that aims to understand how salinity anomalies in the upper ocean generated by melting sea ice affect sea surface temperature (SST), stratification, and subsequent sea-ice growth. SASSIE involved a field campaign that sampled the transition from summer melt to autumn ice advance in the Beaufort Sea during August-October 2022, making intensive in situ and remote sensing observations within ~200 km of the sea ice edge. This dataset contains near-surface air pressure, temperature, and winds, as well as ocean temperature and salinity measurements collected using a Jet Surface Salinity Profiler (Jet-SSP). The Jet-SSP is a remotely operated kayak containing various instrumentation. It moved along various horizontal trajectories each deployment, traveling up to 5 kts as it collected data. Data are available in NetCDF format.",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Drushka, Kyla",
-            "title": "SASSIE Arctic Field Campaign Jet Surface Salinity Profiler Data Fall 2022 Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_JET_SSP_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Salinity and Stratification at the Sea Ice Edge (SASSIE) project is a NASA experiment that aims to understand how salinity anomalies in the upper ocean generated by melting sea ice affect sea surface temperature (SST), stratification, and subsequent sea-ice growth. SASSIE involved a field campaign that sampled the transition from summer melt to autumn ice advance in the Beaufort Sea during August-October 2022, making intensive in situ and remote sensing observations within ~200 km of the sea ice edge. This dataset contains near-surface air pressure, temperature, and winds, as well as ocean temperature and salinity measurements collected using a Jet Surface Salinity Profiler (Jet-SSP). The Jet-SSP is a remotely operated kayak containing various instrumentation. It moved along various horizontal trajectories each deployment, traveling up to 5 kts as it collected data. Data are available in NetCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSASSIE-JETSSP2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSASSIE-JETSSP2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://salinity.oceansciences.org/sassie.htm",
-                    "description": "SASSIE Project Website",
                     "@type": "dcat:Distribution",
+                    "description": "SASSIE Project Website",
+                    "downloadURL": "https://salinity.oceansciences.org/sassie.htm",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/sassie",
-                    "description": "Field Campaign and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/sassie",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://salinity.oceansciences.org/docs/SASSIE_overview.pdf",
-                    "description": "SASSIE Overview Document",
                     "@type": "dcat:Distribution",
+                    "description": "SASSIE Overview Document",
+                    "downloadURL": "https://salinity.oceansciences.org/docs/SASSIE_overview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2624096959-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2624096959-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2624096959-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2624096959-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_JET_SSP_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_JET_SSP_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SASSIE-JETSSP2",
-                    "description": "Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Landing Page",
+                    "downloadURL": "https://doi.org/10.5067/SASSIE-JETSSP2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_JET_SSP_V1.jpg",
+            "identifier": "C2624096959-POCLOUD",
+            "issued": "2022-09-10",
+            "keyword": [
+                "atmospheric pressure",
+                "atmospheric winds",
+                "earth science",
+                "salinity/density",
+                "atmospheric temperature",
+                "atmosphere",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SASSIE-JETSSP2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.5670/oceanog.2019.215"
+            ],
             "spatial": "-151.0 72.0 -144.0 73.5",
+            "temporal": "2022-09-10T23:00:00Z/2022-09-26T20:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASSIE Arctic Field Campaign Jet Surface Salinity Profiler Data Fall 2022 Version 1"
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
-                "validation",
-                "tool",
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
-            "identifier": "NASA-783",
             "description": "PDS Validation Tool (2.0.1) and Product Tools (2.0.1)",
-            "title": "PDS Software Release Validation Tool (2.0.1) and Product Tools (2.0.1)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1123411,216 +1123391,262 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-783",
+            "issued": "2018-06-25",
+            "keyword": [
+                "validation",
+                "tool",
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
+            "title": "PDS Software Release Validation Tool (2.0.1) and Product Tools (2.0.1)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_SNPP.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2019-03-01. VIIRS/Suomi-NPP Cloud Mask 6-Min Swath 750 m. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_SNPP.001. https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_SNPP.001.",
-            "issued": "2019-02-15",
-            "temporal": "2012-03-01T00:00:00Z/2024-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths",
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sips.support@ssec.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS"
-            },
-            "identifier": "C1562021084-LAADS",
-            "description": "The VIIRS/Suomi-NPP Cloud Mask 6-Min Swath 750m product is a Level-2 product generated at 750-m (at nadir) spatial resolutions. The algorithm employs a series of visible and infrared threshold and consistency tests to specify confidence that an unobstructed view of the Earth's surface has been observed. An indication of shadows affecting the scene is also provided. Radiometrically-accurate radiances are required, thus holes in the Cloud Mask will appear wherever the input radiances are incomplete or of poor quality assurance.\r\n\r\nFor more information consult Product Page at: \r\nhttps://cimss.ssec.wisc.edu/MVCM/",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/Suomi-NPP Cloud Mask 6-Min Swath 750 m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/Suomi-NPP Cloud Mask 6-Min Swath 750m product is a Level-2 product generated at 750-m (at nadir) spatial resolutions. The algorithm employs a series of visible and infrared threshold and consistency tests to specify confidence that an unobstructed view of the Earth's surface has been observed. An indication of shadows affecting the scene is also provided. Radiometrically-accurate radiances are required, thus holes in the Cloud Mask will appear wherever the input radiances are incomplete or of poor quality assurance.\r\n\r\nFor more information consult Product Page at: \r\nhttps://cimss.ssec.wisc.edu/MVCM/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FCLDMSK_L2_VIIRS_SNPP.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FCLDMSK_L2_VIIRS_SNPP.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_SNPP.001",
-                    "description": "Data product's landing page",
                     "@type": "dcat:Distribution",
+                    "description": "Data product's landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_SNPP.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/CLDMSK_L2_VIIRS_SNPP--5110",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/CLDMSK_L2_VIIRS_SNPP--5110",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5110/CLDMSK_L2_VIIRS_SNPP/contents.html",
-                    "description": "Direct access to CLDMSK_L2_VIIRS_SNPP OPeNDAP data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to CLDMSK_L2_VIIRS_SNPP OPeNDAP data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5110/CLDMSK_L2_VIIRS_SNPP/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/MODIS_VIIRS_Cloud-Mask_UG_Feb_2019.pdf",
-                    "description": "Product User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Product User's Guide",
+                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/MODIS_VIIRS_Cloud-Mask_UG_Feb_2019.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C1562021084-LAADS",
+            "issued": "2019-02-15",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths",
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/CLDMSK_L2_VIIRS_SNPP.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/HBSL/BISB/MODAPS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-03-01T00:00:00Z/2024-09-30T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/Suomi-NPP Cloud Mask 6-Min Swath 750 m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_mb_raw&version=1.0",
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
-                "mars exploration rover"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains raw data from the Moessbauer Spectrometer (MB) on Mars Exploration Rover 2 (Spirit).",
+            "identifier": "urn:nasa:pds:mer2_mb_raw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer2_mb_raw&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer2_mb_raw",
-            "description": "This bundle contains raw data from the Moessbauer Spectrometer (MB) on Mars Exploration Rover 2 (Spirit).",
-            "title": "MER2 MB Raw Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER2 MB Raw Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/941/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2016-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
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
-            "identifier": "DASHLINK_941",
             "description": "Particle filters (PF) have been established as the de facto state of the art\r\nin failure prognosis. They combine advantages of the rigors of Bayesian estimation\r\nto nonlinear prediction while also providing uncertainty estimates with a given solution. Within the context of particle filters, this paper introduces several novel methods for uncertainty representations and uncertainty management. The prediction uncertainty is modeled via a rescaled Epanechnikov kernel and is assisted with resampling techniques and regularization algorithms. Uncertainty management is accomplished through parametric adjustments in a feedback correction loop of the state model and its noise distributions. The correction loop provides the mechanism to incorporate information that can improve solution accuracy and reduce uncertainty bounds. In addition, this approach results in reduction in computational burden. The scheme is illustrated with real vibration feature data from a fatigue-driven fault in a critical aircraft component.",
-            "title": "Advances in Uncertainty Representation and Management for Particle Filtering Applied to Prognostics",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_ICES_PF.pdf",
-                    "description": "chapter",
                     "@type": "dcat:Distribution",
+                    "description": "chapter",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_ICES_PF.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2009_ICES_PF.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_941",
+            "issued": "2016-01-14",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/941/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Advances in Uncertainty Representation and Management for Particle Filtering Applied to Prognostics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-48.0SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data that have been resampled at a 48.0 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979A Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-48.0sec_n7t3-6pdt",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-48.0SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-48.0sec_n7t3-6pdt",
-            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data that have been resampled at a 48.0 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979A Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
-            "title": "VOYAGER 2 JUPITER MAGNETOMETER RESAMPLED DATA 48.0 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 2 JUPITER MAGNETOMETER RESAMPLED DATA 48.0 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "http://techport.nasa.gov/view/18913",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Douglas Rohn",
+                "hasEmail": "mailto:douglas.a.rohn@nasa.gov"
+            },
+            "description": "&lt;p&gt;The Convergent Aeronautics Solutions (CAS) Project uses short-duration activities to establish early-stage concept and technology feasibility for high-potential solutions. Internal teams propose ideas for overcoming key barriers associated with large-scale aeronautics problems associated with ARMD&amp;rsquo;s six strategic thrusts. The teams will conduct initial feasibility studies, perform experiments, try out new ideas, identify failures, and try again. At the end of the cycle, a review determines whether the developed solutions have met their goals, established initial feasibility, and identified potential for future aviation impact. During these reviews, the most promising capabilities will be considered for continued development further by other ARMD programs or by direct transfer to the aviation community. In the dynamic environment of new ideas, ARMD also gains significant value from the knowledge gained in activities that do not proceed.&lt;/p&gt;&lt;p&gt;In order to enable new capabilities in commercial aviation, the CAS Project&amp;rsquo;s focus is on merging traditional aeronautics disciplines with advancements driven by the non-aeronautics world.&amp;nbsp; The Project will draw on external collaborators to supplement in-house NASA expertise in technologies and disciplines that broadly support advancements in all ARMD strategic thrusts.&lt;/p&gt;",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://techport.nasa.gov/xml-api/18913",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "TECHPORT_18913",
             "issued": "2015-01-01",
-            "@type": "dcat:Dataset",
+            "keyword": [
+                "cas",
+                "active",
+                "project",
+                "nasa headquarters"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/18913",
             "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Aeronautics Research Mission Directorate"
+            },
             "references": [
                 "http://techport.nasa.gov/home",
                 "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
@@ -1123631,214 +1123657,202 @@
                 "http://techport.nasa.gov/fetchFile?objectId=6560",
                 "http://techport.nasa.gov/fetchFile?objectId=3448"
             ],
-            "keyword": [
-                "cas",
-                "active",
-                "project",
-                "nasa headquarters"
+            "title": "Convergent Aeronautics Solutions Project"
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
-                "fn": "Douglas Rohn",
-                "hasEmail": "mailto:douglas.a.rohn@nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Aeronautics Research Mission Directorate"
+                "fn": "Indir Jaganjac",
+                "hasEmail": "mailto:ijaganjac@yahoo.com"
             },
-            "identifier": "TECHPORT_18913",
-            "description": "&lt;p&gt;The Convergent Aeronautics Solutions (CAS) Project uses short-duration activities to establish early-stage concept and technology feasibility for high-potential solutions. Internal teams propose ideas for overcoming key barriers associated with large-scale aeronautics problems associated with ARMD&amp;rsquo;s six strategic thrusts. The teams will conduct initial feasibility studies, perform experiments, try out new ideas, identify failures, and try again. At the end of the cycle, a review determines whether the developed solutions have met their goals, established initial feasibility, and identified potential for future aviation impact. During these reviews, the most promising capabilities will be considered for continued development further by other ARMD programs or by direct transfer to the aviation community. In the dynamic environment of new ideas, ARMD also gains significant value from the knowledge gained in activities that do not proceed.&lt;/p&gt;&lt;p&gt;In order to enable new capabilities in commercial aviation, the CAS Project&amp;rsquo;s focus is on merging traditional aeronautics disciplines with advancements driven by the non-aeronautics world.&amp;nbsp; The Project will draw on external collaborators to supplement in-house NASA expertise in technologies and disciplines that broadly support advancements in all ARMD strategic thrusts.&lt;/p&gt;",
-            "title": "Convergent Aeronautics Solutions Project",
-            "programCode": [
-                "026:000"
-            ],
+            "description": "Blind source separation in Simulink using STFT and inverse STFT\r\n(Signal processing blockset).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "http://techport.nasa.gov/xml-api/18913",
-                    "mediaType": "application/xml"
+                    "description": "blind_source_separation.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/blind_source_separation.zip",
+                    "mediaType": "application/zip",
+                    "title": "blind_source_separation.zip"
                 }
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/129/",
-            "bureauCode": [
-                "026:00"
             ],
+            "identifier": "DASHLINK_129",
             "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ames",
                 "nasa",
                 "dashlink"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Indir Jaganjac",
-                "hasEmail": "mailto:ijaganjac@yahoo.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/129/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_129",
-            "description": "Blind source separation in Simulink using STFT and inverse STFT\r\n(Signal processing blockset).",
-            "title": "Blind Source Separation",
-            "programCode": [
-                "026:029"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/blind_source_separation.zip",
-                    "description": "blind_source_separation.zip",
-                    "@type": "dcat:Distribution",
-                    "title": "blind_source_separation.zip"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Blind Source Separation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D71.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D71. Version 001. VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D71.001. https://doi.org/10.5067/VIIRS/VNP43D71.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "surface radiative properties",
-                "land surface",
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
-            "identifier": "C1607343154-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo white-sky albedo for band M5 (VNP43D71) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D71 is the WSA for VIIRS band M5 (0.672 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D71",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo white-sky albedo for band M5 (VNP43D71) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D71 is the WSA for VIIRS band M5 (0.672 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D71.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D71.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D71.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D71.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D71.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D71.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607343154-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607343154-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D71.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D71.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D71",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D71",
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
+            "identifier": "C1607343154-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "surface radiative properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D71.001",
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
+            "series-name": "VNP43D71",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo WSA at Solar Noon Band M5 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/n7ww-782w",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "We examined molecular responses using transcriptome profiling in isolated left ventricular murine cardiomyocytes to 90 cGy 1 GeV proton (1H) and 15 cGy 1 GeV/nucleon (n) iron (56Fe) particles 1 3 7 14 and 28 days after exposure. Unsupervised clustering analysis of gene expression segregated samples according to the radiation (IR) response and time after exposure with 56Fe-IR showing the greatest level of gene modulation. 1H-IR exposures showed little differential transcript modulation. Network analysis categorized the major differentially expressed genes into cell cycle oxidative responses and transcriptional regulation functional groups. Transcriptional networks identified key nodes regulating expression. Individual transcription factors were inferred to be active at 1 3 7 14 and 28 days after exposure. Validation of the signal transduction network by protein analysis showed that particle IR clearly regulates a long lived signaling mechanism for p38 MAPK signaling and NFATc4 activation. Electrophoresis mobility shift assays supported the role of additional key transcription factors GATA-4 STAT-3 and NF-kB as regulators of the response at specific time points. These data suggest that the molecular response to 56Fe-IR is unique and shows long-lasting gene expression in cardiomyocytes up to 28 days after exposure. Additionally proteins involved in signal transduction and transcriptional activation via DNA binding play a role in the response to high charge (Z) and energy (E) particles (HZE). Our study may have implications for NASA  s efforts to develop heart disease risk estimates for astronauts safety via identification of specific HZE-IR molecular markers and for patients receiving conventional and particle radiotherapy. Transcriptome profiling in isolated left ventricular murine cardiomyocytes to 90 cGy 1 GeV proton (1H) and 15 cGy 1 GeV/nucleon (n) iron (56Fe) particles 1 3 7 14 and 28 days after exposure.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-109",
+                    "mediaType": "text/html",
+                    "title": "Delayed Cardiomyocyte Response to Total Body Particle Radiation Exposure - Identification of Regulatory Gene Network [iron]"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-109_n7ww-782w",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse68875-5",
                 "rna extraction",
@@ -1123856,977 +1123870,977 @@
                 "p-gse68875-6",
                 "radiation dosage"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/n7ww-782w",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-109_n7ww-782w",
-            "description": "We examined molecular responses using transcriptome profiling in isolated left ventricular murine cardiomyocytes to 90 cGy 1 GeV proton (1H) and 15 cGy 1 GeV/nucleon (n) iron (56Fe) particles 1 3 7 14 and 28 days after exposure. Unsupervised clustering analysis of gene expression segregated samples according to the radiation (IR) response and time after exposure with 56Fe-IR showing the greatest level of gene modulation. 1H-IR exposures showed little differential transcript modulation. Network analysis categorized the major differentially expressed genes into cell cycle oxidative responses and transcriptional regulation functional groups. Transcriptional networks identified key nodes regulating expression. Individual transcription factors were inferred to be active at 1 3 7 14 and 28 days after exposure. Validation of the signal transduction network by protein analysis showed that particle IR clearly regulates a long lived signaling mechanism for p38 MAPK signaling and NFATc4 activation. Electrophoresis mobility shift assays supported the role of additional key transcription factors GATA-4 STAT-3 and NF-kB as regulators of the response at specific time points. These data suggest that the molecular response to 56Fe-IR is unique and shows long-lasting gene expression in cardiomyocytes up to 28 days after exposure. Additionally proteins involved in signal transduction and transcriptional activation via DNA binding play a role in the response to high charge (Z) and energy (E) particles (HZE). Our study may have implications for NASA  s efforts to develop heart disease risk estimates for astronauts safety via identification of specific HZE-IR molecular markers and for patients receiving conventional and particle radiotherapy. Transcriptome profiling in isolated left ventricular murine cardiomyocytes to 90 cGy 1 GeV proton (1H) and 15 cGy 1 GeV/nucleon (n) iron (56Fe) particles 1 3 7 14 and 28 days after exposure.",
-            "title": "Delayed Cardiomyocyte Response to Total Body Particle Radiation Exposure - Identification of Regulatory Gene Network [iron]",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-109",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Delayed Cardiomyocyte Response to Total Body Particle Radiation Exposure - Identification of Regulatory Gene Network [iron]"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Delayed Cardiomyocyte Response to Total Body Particle Radiation Exposure - Identification of Regulatory Gene Network [iron]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/96ltniikJ7vd",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CanSISE Observation-Based Ensemble of Northern Hemisphere Terrestrial Snow Water Equivalent, Version 2. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/96ltniikJ7vd.",
-            "issued": "1981-01-01",
-            "temporal": "1981-01-01T00:00:00Z/2010-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2010-12-31",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "earth science",
-                "snow/ice",
-                "ngda",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lawrence Mudryk",
                 "hasEmail": "mailto:Lawrence.mudryk@canada.ca"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386256679-NSIDCV0",
             "description": "This data set is a daily gridded terrestrial snow water equivalent (SWE) dataset based on five component SWE products:\n<ul>\n<li><a href=\"http://www.globsnow.info\">GlobSnow combined SWE product (passive microwave/ground-based weather station, version 2)</a></li>\n<li><a href=\"http://apps.ecmwf.int/datasets/.\">ERA-Interim/Land reanalysis SWE product</a></li>\n<li><a href=\"http://gmao.gsfc.nasa.gov/pubs/docs/Reichle541.pdf\">MERRA reanalysis SWE product </a></li>\n<li>Crocus SWE data set: output from the Crocus snowpack model, driven by ERA-Interim meteorology (<a href=\"http://dx.doi.org/10.1175/JHM-D-12-012.1\">Brun et al. 2013</a>)</li>\n<li>GLDAS SWE product (version 2) (<a href=\"http://dx.doi.org/10.1175/BAMS-85-3-381\">Rodell et al. 2004</a>; <a href=\"http://dx.doi.org/10.5067/0JNJQ8ZDZRBA\">Rodell and Beaudoing 2013</a>)</li>\n</ul>",
-            "title": "CanSISE Observation-Based Ensemble of Northern Hemisphere Terrestrial Snow Water Equivalent, Version 2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F96ltniikJ7vd",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F96ltniikJ7vd",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0668_swe_ensemble_v2",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0668_swe_ensemble_v2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0668_swe_ensemble_v2",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0668_swe_ensemble_v2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/96ltniikJ7vd",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/96ltniikJ7vd",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/96ltniikJ7vd",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/96ltniikJ7vd",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386256679-NSIDCV0",
+            "issued": "1981-01-01",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "earth science",
+                "snow/ice",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/96ltniikJ7vd",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2010-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "1981-01-01T00:00:00Z/2010-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CanSISE Observation-Based Ensemble of Northern Hemisphere Terrestrial Snow Water Equivalent, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/424/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-07-05",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Santanu Das",
                 "hasEmail": "mailto:Santanu.Das-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_424",
             "description": "For the purposes of this paper, the National\r\nAirspace System (NAS) encompasses the operations of all\r\naircraft which are subject to air traffic control procedures.\r\nThe NAS is a highly complex dynamic system that is\r\nsensitive to aeronautical decision-making and risk management\r\nskills. In order to ensure a healthy system with safe\r\nflights a systematic approach to anomaly detection is very\r\nimportant when evaluating a given set of circumstances\r\nand for determination of the best possible course of action.\r\nGiven the fact that the NAS is a vast and loosely integrated\r\nnetwork of systems, it requires improved safety assurance\r\ncapabilities to maintain an extremely low accident rate\r\nunder increasingly dense operating conditions. Data mining\r\nbased tools and techniques are required to support and aid\r\noperators\u2019 (such as pilots, management, or policy makers)\r\noverall decision-making capacity. Within the NAS, the\r\nability to analyze fleetwide aircraft data autonomously is\r\nstill considered a significantly challenging task. For our\r\npurposes a fleet is defined as a group of aircraft sharing\r\ngenerally compatible parameter lists. Here, in this effort,\r\nwe aim at developing a system level analysis scheme. In this\r\npaper we address the capability for detection of fleetwide\r\nanomalies as they occur, which itself is an important\r\ninitiative toward the safety of the real-world flight operations.\r\nThe flight data recorders archive millions of data\r\npoints with valuable information on flights everyday. The\r\noperational parameters consist of both continuous and discrete\r\n(binary & categorical) data from several critical subsystems\r\nand numerous complex procedures. In this paper,\r\nwe discuss a system level anomaly detection approach based\r\non the theory of kernel learning to detect potential safety\r\nanomalies in a very large data base of commercial aircraft.\r\nWe also demonstrate that the proposed approach uncovers\r\nsome operationally significant events due to environmental,\r\nmechanical, and human factors issues in high dimensional,\r\nmultivariate Flight Operations Quality Assurance (FOQA)\r\ndata. We present the results of our detection algorithms on\r\nreal FOQA data from a regional carrier.",
-            "title": "Fleet Level Anomaly Detection of Aviation Safety Data",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/10696.pdf",
-                    "description": "Fleet Level Anomaly Detection of Aviation Safety Data",
                     "@type": "dcat:Distribution",
+                    "description": "Fleet Level Anomaly Detection of Aviation Safety Data",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/10696.pdf",
+                    "mediaType": "application/pdf",
                     "title": "10696.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_424",
+            "issued": "2011-07-05",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/424/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Fleet Level Anomaly Detection of Aviation Safety Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/n7zh-gwzv",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "library construction",
-                "nucleic acid sequencing",
-                "time",
-                "nucleic acid extraction",
-                "treatment protocol"
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
-            "identifier": "nasa_genelab_GLDS-319_n7zh-gwzv",
             "description": "Physical inactivity decreases the mechanical load on the skeleton which when prolonged leads to losses of muscle strength and bone mass in humans and most mammalian species. Hibernating mammals show no loss in bone mass and less muscle atrophy than would be anticipated over such a prolonged period of physical inactivity. This suggests that diverse hibernating mammals have evolved natural mechanisms that reduce muscle atrophy and conserve bone mass.",
-            "title": "Muscle atrophy osteoporosis prevention in hibernating mammals",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-319",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-319",
+                    "mediaType": "text/html",
                     "title": "Muscle atrophy osteoporosis prevention in hibernating mammals"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-319_n7zh-gwzv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "library construction",
+                "nucleic acid sequencing",
+                "time",
+                "nucleic acid extraction",
+                "treatment protocol"
+            ],
+            "landingPage": "https://data.nasa.gov/d/n7zh-gwzv",
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
+            "title": "Muscle atrophy osteoporosis prevention in hibernating mammals"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-07-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21.",
-            "issued": "2021-04-01",
-            "temporal": "2020-07-01T00:00:00Z/2022-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-09",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHARLES TREPTE",
                 "hasEmail": "mailto:charles.r.trepte@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2059838686-LARC_ASDC",
             "description": "CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) Lidar Level 3 Tropospheric Aerosol Profiles, All Sky Data, Standard Version 4-21 data product. This data product was collected using the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP) instrument. Data collection for this product is complete.\r\n\r\n\r\nThe CALIPSO lidar level 3 aerosol data product reports monthly mean profiles of aerosol optical properties on a uniform spatial grid. It is intended to be a tropospheric product and so data are only reported below altitudes of 12 km. All level 3 parameters are derived from the version 4.21 CALIOP level 2 aerosol profile product and have been quality screened prior to averaging. The primary quantities reported are vertical profiles of aerosol extinction coefficient at 532 nm and its vertical integral, the aerosol optical depth (AOD). Aerosol type and spatial distribution information are also included. Averaged profile data is reported for all aerosols, regardless of type, and for mineral dust aerosol only. Classification of dust is based on the aerosol type flags in the level 2 profile product. To keep level 3 file sizes manageable, there are four different types of level 3 files produced, depending on the sky condition and the temporal coverage of the data prior to averaging.\r\n\r\nDescription of the Four Sky Conditions (Day, Night):\r\n1) All Sky: All level 2 columns are averaged, regardless of cloud occurrence,\r\n2) Cloud-Free: Only cloud-free level 2 columns are averaged,\r\n3) Cloudy-Sky, Transparent: Only level 2 columns containing transparent clouds are averaged, and\r\n4) Cloud-Sky, Opaque: Only level 2 columns containing opaque clouds are averaged\r\n\r\nCALIPSO was launched on April 28, 2006, and continues to collect data necessary to study the impact of clouds and aerosols on the Earth's radiation budget and climate. It flies in the international A-Train constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments: CALIOP, Imaging Infrared Radiometer (IIR), and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES (Centre national d'\u00e9tudes spatiales).",
-            "title": "CALIPSO Lidar Level 3 Tropospheric Aerosol Profiles, All Sky Data, Standard V4-21",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCALIOP%2FCALIPSO%2FCAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
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
-                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/",
-                    "description": "NASA Mission Page for CALIPSO",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Mission Page for CALIPSO",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.92",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.92",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x92.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
-                    "description": "DOI data set landing page for CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21",
+                    "downloadURL": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2059838686-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2059838686-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
-                    "description": "CALIPSO User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO User's Guide",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L3_Tropospheric_APro_AllSky-Standard-V4-21/",
-                    "description": "ASDC Direct Data Download for CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/LID_L3_Tropospheric_APro_AllSky-Standard-V4-21/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L3_Tropospheric_APro_AllSky-Standard-V4-21/contents.html",
-                    "description": "OPeNDAP data access for CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/LID_L3_Tropospheric_APro_AllSky-Standard-V4-21/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2059838686-LARC_ASDC",
+            "issued": "2021-04-01",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L3_Tropospheric_APro_AllSky-Standard-V4-21_V4-21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2020-07-01T00:00:00Z/2022-01-01T23:59:59.999Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Lidar Level 3 Tropospheric Aerosol Profiles, All Sky Data, Standard V4-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/774/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
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
-            "identifier": "DASHLINK_774",
             "description": "With the advent of the next generation of aerospace systems equipped with fly-by-wire controls, electro- mechanical actuators (EMA) are quickly becoming components critical to safety of aerospace vehicles. Being relatively new to the field, however, EMA lack the knowledge base compared to what is accumulated for the more traditional actuator types, especially when it comes to fault detection and prognosis. Scarcity of health monitoring data from fielded systems and prohibitive costs of carrying out real flight tests create the need to build high-fidelity system models and design affordable yet realistic experimental setups. The objective of this work is to build an EMA test stand that, unlike current laboratory stands typically weighing in excess of one metric ton, is portable enough to be easily placed aboard a wide variety of aircraft. This stand, named the FLEA (for Flyable Electro- mechanical Actuator test stand), allows testing EMA fault detection and prognosis technologies in flight environment, thus substantially increasing their technology readiness level \u2013 all without the expense of dedicated flights, as the stand is designed to function as a non-intrusive secondary payload. No aircraft modifications are required and data can be collected during any available flight opportunity: pilot currency flights, ferry flights, or flights dedicated to other experiments. The stand is currently equipped with a prototype version of NASA Ames developed prognostic health management system with models aimed at detecting and tracking several fault types. At this point the team has completed test flights of the stand on US Air Force C-17 aircraft and US Army UH-60 helicopters and more experiments, both laboratory and airborne, are planned for the coming months.",
-            "title": "Airborne Electro-Mechanical Actuator Test Stand for Development of Prognostic Health Management Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_PHM_EMA.pdf",
-                    "description": "2010_PHM_EMA.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2010_PHM_EMA.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2010_PHM_EMA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2010_PHM_EMA.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_774",
+            "issued": "2013-06-19",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/774/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Airborne Electro-Mechanical Actuator Test Stand for Development of Prognostic Health Management Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/1AMEDB6VJ1NZ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs Greenland 6 and 12 day Ice Sheet Velocity Mosaics from SAR V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/1AMEDB6VJ1NZ.",
-            "issued": "2015-01-01",
-            "temporal": "2015-01-01T00:00:00Z/2024-04-24T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-24",
-            "keyword": [
-                "snow/ice",
-                "cryosphere",
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
-            "identifier": "C2439350316-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) Program, contains 6 and 12 day surface velocity estimates for the Greenland Ice Sheet and periphery. Velocities are derived from images acquired by the European Space Agency (ESA) Copernicus Sentinel-1A and Sentinel-1B satellites.\n\nSee <a href=\"http://nsidc.org/grimp\">Greenland Ice Mapping Project (GrIMP)</a> for related data sets.",
-            "title": "MEaSUREs Greenland 6 and 12 day Ice Sheet Velocity Mosaics from SAR V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1AMEDB6VJ1NZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1AMEDB6VJ1NZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0766.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0766.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0766/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0766/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0766+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0766+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0766.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0766.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0766/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0766/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0766+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0766+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0766.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0766.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0766/versions/2/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0766/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0766+V002",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NSIDC-0766+V002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1AMEDB6VJ1NZ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/1AMEDB6VJ1NZ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1AMEDB6VJ1NZ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/1AMEDB6VJ1NZ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2439350316-NSIDC_ECS",
+            "issued": "2015-01-01",
+            "keyword": [
+                "snow/ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/1AMEDB6VJ1NZ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-90.9 58.5 8.32 83.0",
+            "temporal": "2015-01-01T00:00:00Z/2024-04-24T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs Greenland 6 and 12 day Ice Sheet Velocity Mosaics from SAR V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/680",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Defries, R.S., M.C. Hansen, J.R.G. Townshend, and R.A. Sohlberg. 2003. LBA Regional Land Cover from AVHRR, 8-km, 1984 (DeFries et al.). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/680",
-            "issued": "2023-10-03",
-            "temporal": "1984-01-01T00:00:00Z/1984-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "ecosystems",
-                "land use/land cover",
-                "vegetation",
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
-            "identifier": "C2777326444-ORNL_CLOUD",
             "description": "This data set is a subset of an 8-km global land cover product (DeFries et al. 1998). This subset was created for the study area of the Large Scale Biosphere-Atmosphere Experiment in Amazonia (LBA) in South America (i.e., latitude 10 N to 25 S, longitude 30 to 85 W). The data are in ASCII GRID file format.To develop improved methodologies for global land cover classifications as well as to provide global land cover products for immediate use in global change research, researchers at the Laboratory for Global Remote Sensing Studies at the University of Maryland employed the NASA/NOAA Pathfinder AVHRR Land (PAL) data set with a spatial resolution of 8 km. The PAL data set has a length of record of 14 years (1981-1994), providing the ability to test the stability of classification algorithms. Furthermore, the data set includes red, infrared, and thermal bands in addition to the Normalized Difference Vegetation Index (NDVI). Inclusion of these additional bands improves discrimination between cover types. The project's aim was to develop and validate global land cover data sets and to develop advanced methodologies for more realistically describing the vegetative land surface based on satellite data.The global land cover product (Defries et al. 1998) was derived by testing several metrics that describe the temporal dynamics of vegetation over an annual cycle. These metrics were applied to 1984 PAL data at 8-km resolution to derive a global land cover classification product using a decision tree classifier. The final product contains 13 land cover classes. The original 8-km global land cover product is available for download from the University of Maryland's Global Land Cover Facility (GLCF) Web site (http://glcf.umiacs.umd.edu/data/landcover/index.shtml). Additional information and references on this data set can be found at the GLCF Web site, as well as at the LGRSS Web site (http://www.geog.umd.edu/LGRSS/intro.html). More information can be found at ftp://daac.ornl.gov/data/lba/land_use_land_cover_change/comp/land_cover_data_8km/glcf8km_readme.pdf.LBA was a cooperative international research initiative led by Brazil. NASA was a lead sponsor for several experiments. LBA was designed to create the new knowledge needed to understand the climatological, ecological, biogeochemical, and hydrological functioning of Amazonia; the impact of land use change on these functions; and the interactions between Amazonia and the Earth system. More information about LBA can be found at http://www.daac.ornl.gov/LBA/misc_amazon.html.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA Regional Land Cover from AVHRR, 8-km, 1984 (DeFries et al.)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/680_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F680",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F680",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/land_cover_data_8km/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/land_cover_data_8km/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_glcf8km.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_glcf8km.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/680",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/680",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/land_cover_data_8km/comp//glcf8km_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/land_cover_data_8km/comp//glcf8km_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/680_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/680_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=680",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=680",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/680_1_fit.png",
+            "identifier": "C2777326444-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "ecosystems",
+                "land use/land cover",
+                "vegetation",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/680",
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
+            "temporal": "1984-01-01T00:00:00Z/1984-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA Regional Land Cover from AVHRR, 8-km, 1984 (DeFries et al.)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M24-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 4 mission phase, covering the period  from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m24-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M24-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m24-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 4 mission phase, covering the period  from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP024 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP024 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP09GA.001",
             "citation": "Eric Vermote, Belen Franch, Martin Claverie\r\n. 2017-03-24. VNP09GA. Version 001. VIIRS/NPP Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V001\r\n. Sioux Falls, SD, USA\r\n. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC\r\n. https://doi.org/10.5067/VIIRS/VNP09GA.001. https://doi.org/10.5067/VIIRS/VNP09GA.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2017-02-15",
-            "temporal": "2012-01-19T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-27",
-            "keyword": [
-                "surface radiative properties",
-                "earth science",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "data-presentation-form": "Digital Science Data",
-            "identifier": "C1373412034-LPDAAC_ECS",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "description": "The Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) daily surface reflectance (VNP09GA) Version 1 product provides an estimate of land surface reflectance from the Suomi National Polar-Orbiting Partnership (Suomi NPP) VIIRS sensor. Data are provided for three imagery bands (I1-I3) at nominal 500 meter resolution (~ 463 meter) and nine moderate resolution bands (M1-M5, M7, M8, M10, M11) at nominal 1 kilometer (~926 meter) resolution. The 500 meter and 1 kilometer datasets are derived through resampling the native 375 meter and 750 meter VIIRS resolutions, respectively, in the Level 2 input product. These bands are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. \r\n\r\nThe inputs to the surface reflectance algorithm are top-of-atmosphere reflectance for the VIIRS visible bands, the VIIRS cloud mask and aerosol product, aerosol optical thickness and atmospheric data obtained from the NOAA National Centers for Environmental Prediction (NCEP) reanalysis system. Along with the twelve reflectance bands are reflectance band quality, sensor azimuth angle, solar azimuth angle, sensor zenith angle, solar zenith angle, and observations layers. The reflectance layers from the VNP09GA data product are used as input data for many of the VIIRS land products.",
-            "release-place": "Sioux Falls, SD, USA",
-            "series-name": "VNP09GA",
             "creator": "Eric Vermote, Belen Franch, Martin Claverie",
-            "title": "VIIRS/NPP Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP09GA.A2019182.h19v04.001.2019183070609.1.jpg?_ga=2.79669204.116070394.1561987039-1109527761.1561753117",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) daily surface reflectance (VNP09GA) Version 1 product provides an estimate of land surface reflectance from the Suomi National Polar-Orbiting Partnership (Suomi NPP) VIIRS sensor. Data are provided for three imagery bands (I1-I3) at nominal 500 meter resolution (~ 463 meter) and nine moderate resolution bands (M1-M5, M7, M8, M10, M11) at nominal 1 kilometer (~926 meter) resolution. The 500 meter and 1 kilometer datasets are derived through resampling the native 375 meter and 750 meter VIIRS resolutions, respectively, in the Level 2 input product. These bands are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. \r\n\r\nThe inputs to the surface reflectance algorithm are top-of-atmosphere reflectance for the VIIRS visible bands, the VIIRS cloud mask and aerosol product, aerosol optical thickness and atmospheric data obtained from the NOAA National Centers for Environmental Prediction (NCEP) reanalysis system. Along with the twelve reflectance bands are reflectance band quality, sensor azimuth angle, solar azimuth angle, sensor zenith angle, solar zenith angle, and observations layers. The reflectance layers from the VNP09GA data product are used as input data for many of the VIIRS land products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP09GA.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP09GA.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP09GA.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP09GA.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP09GA.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP09GA.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1373412034-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1373412034-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP09GA.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP09GA.001/contents.html",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP09GA.A2019182.h19v04.001.2019183070609.1.jpg?_ga=2.79669204.116070394.1561987039-1109527761.1561753117",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP09GA.A2019182.h19v04.001.2019183070609.1.jpg?_ga=2.79669204.116070394.1561987039-1109527761.1561753117",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
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
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP09GA.A2019182.h19v04.001.2019183070609.1.jpg?_ga=2.79669204.116070394.1561987039-1109527761.1561753117",
+            "identifier": "C1373412034-LPDAAC_ECS",
+            "issued": "2017-02-15",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP09GA.001",
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
+            "series-name": "VNP09GA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Surface Reflectance Daily L2G Global 1km and 500m SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-2-CR4A-EDITED2-V1.0",
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
-                "solar wind"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the CRUISE 4-1 mission phase\nwhere the primary target was the SOLAR WIND. It contains uncalibrated\nraw data, i.e. the digital output of the instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-2-cr4a-edited2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "solar wind"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCLAP-2-CR4A-EDITED2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpclap-2-cr4a-edited2-v1.0",
-            "description": "This data set contains EDITED\ndata from Rosetta RPC-LAP, acquired during the CRUISE 4-1 mission phase\nwhere the primary target was the SOLAR WIND. It contains uncalibrated\nraw data, i.e. the digital output of the instrument.",
-            "title": "ROSETTA-ORBITER SW RPCLAP 2\nCR4A EDITED2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SW RPCLAP 2\nCR4A EDITED2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/PLUVIO/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A, Ali  Tokay and Patrick N Gatlin.2017. GPM Ground Validation Pluvio Precipitation Gauges OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/PLUVIO/DATA301",
-            "issued": "2017-05-19",
-            "temporal": "2015-10-31T23:55:00Z/2016-01-31T23:54:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "precipitation",
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
-            "identifier": "C1979684276-GHRC_DAAC",
             "description": "The GPM Ground Validation Pluvio Precipitation Gauges OLYMPEX dataset contains one-minute precipitation rate and precipitation accumulation measurements, as well as start and end times of precipitation events, that were collected during the Olympic Mountain Experiment (OLYMPEX) field campaign on the Olympic Peninsula in the Pacific Northwest of the United States. A Pluvio 400 weighing bucket gauge created by OTT Hydromet in Kempten, Germany was used to collect data at three different sites: Neilton Point (apu04),  Wynoochee Trailer (apu10), and Upper Quinault Enchanted Valley (apu30). Data were collected from October 31, 2015 through January 31, 2016, but exact dates vary by site. Data files are available in ASCII-tsv format.",
-            "title": "GPM Ground Validation Pluvio Precipitation Gauges OLYMPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FPLUVIO%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FPLUVIO%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmplolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmplolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.wmo.int/pages/prog/www/IMOP/publications/IOM-96_TECO-2008/P2(18)_Nemeth_Germany.pdf",
-                    "description": "OTT Pluvio\u00b2: Weighing Precipitation Gauge and Advances in Precipitation Measurement Technology",
                     "@type": "dcat:Distribution",
+                    "description": "OTT Pluvio\u00b2: Weighing Precipitation Gauge and Advances in Precipitation Measurement Technology",
+                    "downloadURL": "http://www.wmo.int/pages/prog/www/IMOP/publications/IOM-96_TECO-2008/P2(18)_Nemeth_Germany.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pubs.usgs.gov/fs/fs07703/fs07703.pdf",
-                    "description": "Evaluation of OTT PLUVIO Precipitation Gage versus Belfort Universal Precipitation Gage 5-780\u2013Supplemental Data, January 15 through July 16, 2002",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation of OTT PLUVIO Precipitation Gage versus Belfort Universal Precipitation Gage 5-780\u2013Supplemental Data, January 15 through July 16, 2002",
+                    "downloadURL": "https://pubs.usgs.gov/fs/fs07703/fs07703.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
-                    "description": "OLYMPEX Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://olympex.atmos.washington.edu/",
-                    "description": "University of Washington OLYMPEX Web Site",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington OLYMPEX Web Site",
+                    "downloadURL": "http://olympex.atmos.washington.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/pluvio/doc/gpmplolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/pluvio/doc/gpmplolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/pluvio/doc/readme_pluvio_olympex-2.pdf",
-                    "description": "Pluvio Weighing Bucket Gauge data processing during Olympic Mountain Experiment (OLYMPEx)",
                     "@type": "dcat:Distribution",
+                    "description": "Pluvio Weighing Bucket Gauge data processing during Olympic Mountain Experiment (OLYMPEx)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/disdrometers_and_gauges/pluvio/doc/readme_pluvio_olympex-2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "downloadURL": "https://pmm.nasa.gov/olympex",
-                    "description": "OLYMPEX Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX Home Page",
+                    "downloadURL": "https://pmm.nasa.gov/olympex",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1979684276-GHRC_DAAC",
+            "issued": "2017-05-19",
+            "keyword": [
+                "precipitation",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/PLUVIO/DATA301",
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
             "spatial": "-123.867 47.3898 -123.581 47.68",
+            "temporal": "2015-10-31T23:55:00Z/2016-01-31T23:54:00Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Pluvio Precipitation Gauges OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-DID-3-RDR-GRIGG-SKJELL-V1.0",
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
-                "giotto extended mission",
-                "26p/grigg-skjellerup 1 (1922 k1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains the results obtained from the Dust Impact Detection System (DIDSY) flown aboard the GIOTTO spacecraft during its extended mission to Comet P/Grigg-Skjellerup in 1992. The measurements and analysis of the three impacts detected during close approach are contained in text files. Calibration tables for the sensors are included in this dataset. These data have not been reviewed or formally archived with the PDS.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-did-3-rdr-grigg-skjell-v1.0_n8dq-qx6d",
+            "issued": "2018-06-26",
+            "keyword": [
+                "giotto extended mission",
+                "26p/grigg-skjellerup 1 (1922 k1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-DID-3-RDR-GRIGG-SKJELL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-did-3-rdr-grigg-skjell-v1.0_n8dq-qx6d",
-            "description": "This dataset contains the results obtained from the Dust Impact Detection System (DIDSY) flown aboard the GIOTTO spacecraft during its extended mission to Comet P/Grigg-Skjellerup in 1992. The measurements and analysis of the three impacts detected during close approach are contained in text files. Calibration tables for the sensors are included in this dataset. These data have not been reviewed or formally archived with the PDS.",
-            "title": "GIOTTO EXTENDED MISSION DUST IMPACT DETECTOR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GIOTTO EXTENDED MISSION DUST IMPACT DETECTOR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/n8du-kijv",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "In prospective human exploration of outer space the need to maintain a species over several generations under changed gravity conditions may arise. This paper reports the analysis of the third generation of fruit fly Drosophila melanogaster obtained during the 44.5-day space flight (Foton-M4 satellite 2014 Russia) followed by the fourth generation on Earth and the fifth generation under conditions of a 12-day space flight (2014 in the Russian Segment of the ISS). The obtained results show that it is possible to obtain the third-fifth generations of a complex multicellular Earth organism under changed gravity conditions (in the cycle weightlessness - Earth - weightlessness) which preserves fertility and normal development. However there were a number of changes in the expression levels and content of cytoskeletal proteins that are the key components of the spindle apparatus and the contractile ring of cells.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-96",
+                    "mediaType": "text/html",
+                    "title": "The development of Drosophila melanogaster during space flight"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-96_n8du-kijv",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid extraction",
                 "growth protocol",
@@ -1124835,969 +1124849,931 @@
                 "nucleic acid sequencing",
                 "sequence analysis data transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/n8du-kijv",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-96_n8du-kijv",
-            "description": "In prospective human exploration of outer space the need to maintain a species over several generations under changed gravity conditions may arise. This paper reports the analysis of the third generation of fruit fly Drosophila melanogaster obtained during the 44.5-day space flight (Foton-M4 satellite 2014 Russia) followed by the fourth generation on Earth and the fifth generation under conditions of a 12-day space flight (2014 in the Russian Segment of the ISS). The obtained results show that it is possible to obtain the third-fifth generations of a complex multicellular Earth organism under changed gravity conditions (in the cycle weightlessness - Earth - weightlessness) which preserves fertility and normal development. However there were a number of changes in the expression levels and content of cytoskeletal proteins that are the key components of the spindle apparatus and the contractile ring of cells.",
-            "title": "The development of Drosophila melanogaster during space flight",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-96",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "The development of Drosophila melanogaster during space flight"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "The development of Drosophila melanogaster during space flight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOESRPLT/CRS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Gerald M.2019. GOES-R PLT Cloud Radar System (CRS) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GOESRPLT/CRS/DATA101",
-            "issued": "2019-05-13",
-            "temporal": "2017-04-11T16:29:39Z/2017-05-17T07:35:23Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
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
-            "identifier": "C1995568976-GHRC_DAAC",
             "description": "The GOES-R PLT Field Campaign Cloud Radar System (CRS) dataset provides high-resolution profiles of reflectivity and Doppler velocity at aircraft nadir along the flight track. The CRS was flown aboard a NASA ER-2 high-altitude aircraft during the GOES-R Post Launch Test (PLT) field campaign. The GOES-R PLT field campaign took place from March 21 to May 17, 2017 in support of post-launch product validation of the Advanced Baseline Image (ABI) and the Geostationary Lightning Mapper (GLM) aboard the GOES-R, now GOES-16, satellite. The CRS data files are available in netCDF-3 format with browse imagery available in PNG format.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GOES-R PLT Cloud Radar System (CRS) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/CRS/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FCRS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FCRS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltcrs",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltcrs",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/CRS/browse/GOESR_CRS_20170411_162940-170000.png",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/CRS/browse/GOESR_CRS_20170411_162940-170000.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://har.gsfc.nasa.gov/index.php?section=28",
-                    "description": "High Altitude Radar: Cloud Radar System (CRS)",
                     "@type": "dcat:Distribution",
+                    "description": "High Altitude Radar: Cloud Radar System (CRS)",
+                    "downloadURL": "https://har.gsfc.nasa.gov/index.php?section=28",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/CRS/doc/goesrpltcrs_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/CRS/doc/goesrpltcrs_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1002/2016JD025269",
-                    "description": "Using a multiwavelength suite of microwave instruments to investigate the microphysical structure of deep convective cores",
                     "@type": "dcat:Distribution",
+                    "description": "Using a multiwavelength suite of microwave instruments to investigate the microphysical structure of deep convective cores",
+                    "downloadURL": "https://doi.org/10.1002/2016JD025269",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JAM2250.1",
-                    "description": "Ice Cloud Retrievals and Analysis with the Compact Scanning Submillimeter Imaging Radiometer and the Cloud Radar System during CRYSTAL FACE",
                     "@type": "dcat:Distribution",
+                    "description": "Ice Cloud Retrievals and Analysis with the Compact Scanning Submillimeter Imaging Radiometer and the Cloud Radar System during CRYSTAL FACE",
+                    "downloadURL": "https://doi.org/10.1175/JAM2250.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0426(2004)021%3C1378:AGCRSO%3E2.0.CO;2",
-                    "description": "A 94-GHz Cloud Radar System on a NASA High-Altitude ER-2 Aircraft",
                     "@type": "dcat:Distribution",
+                    "description": "A 94-GHz Cloud Radar System on a NASA High-Altitude ER-2 Aircraft",
+                    "downloadURL": "https://doi.org/10.1175/1520-0426(2004)021%3C1378:AGCRSO%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH1722.1",
-                    "description": "Measurements of Ocean Surface Backscattering Using an Airborne 94-GHz Cloud Radar\u2014Implication for Calibration of Airborne and Spaceborne W-Band Radars",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of Ocean Surface Backscattering Using an Airborne 94-GHz Cloud Radar\u2014Implication for Calibration of Airborne and Spaceborne W-Band Radars",
+                    "downloadURL": "https://doi.org/10.1175/JTECH1722.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2003JD004030",
-                    "description": "Combined lidar-radar remote sensing: Initial results from CRYSTAL-FACE",
                     "@type": "dcat:Distribution",
+                    "description": "Combined lidar-radar remote sensing: Initial results from CRYSTAL-FACE",
+                    "downloadURL": "https://doi.org/10.1029/2003JD004030",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2004JD005605",
-                    "description": "Cirrus cloud optical, microphysical, and radiative properties observed during the CRYSTAL-FACE experiment: A lidar-radar retrieval system",
                     "@type": "dcat:Distribution",
+                    "description": "Cirrus cloud optical, microphysical, and radiative properties observed during the CRYSTAL-FACE experiment: A lidar-radar retrieval system",
+                    "downloadURL": "https://doi.org/10.1029/2004JD005605",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2005JD005969",
-                    "description": "Retrieving optically thick ice cloud microphysical properties by using airborne dual-wavelength radar measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Retrieving optically thick ice cloud microphysical properties by using airborne dual-wavelength radar measurements",
+                    "downloadURL": "https://doi.org/10.1029/2005JD005969",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/goes-r-post-launch-test-plt",
-                    "description": "GOES-R Post Launch Test (PLT) Field Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "GOES-R Post Launch Test (PLT) Field Campaign",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/goes-r-post-launch-test-plt",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/CRS/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/CRS/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/CRS/browse/",
+            "identifier": "C1995568976-GHRC_DAAC",
+            "issued": "2019-05-13",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOESRPLT/CRS/DATA101",
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
             "spatial": "-117.184 26.4488 -72.2019 43.5725",
+            "temporal": "2017-04-11T16:29:39Z/2017-05-17T07:35:23Z",
             "theme": [
                 "GOES-R PLT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOES-R PLT Cloud Radar System (CRS) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC3-MTP018-V1.0",
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
+            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 18 period of the ESCORT 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc3-mtp018-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC3-MTP018-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc3-mtp018-v1.0",
-            "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 18 period of the ESCORT 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 3\n    MTP018 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 3\n    MTP018 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-5-ANAGLYPH-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-5-anaglyph-ops-v1.0_n8gb-jmcm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-5-ANAGLYPH-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-5-anaglyph-ops-v1.0_n8gb-jmcm",
-            "description": "NULL",
-            "title": "MER 2 MARS NAVIGATION CAMERA\n                                      ANAGLYPH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS NAVIGATION CAMERA\n                                      ANAGLYPH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1066-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-29T10:16:35.000 to 2015-09-29T17:30:30.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1066-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1066-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1066-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-29T10:16:35.000 to 2015-09-29T17:30:30.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1066 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1066 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0348-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-10T15:42:30.000 to 2014-10-10T23:10:13.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0348-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0348-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0348-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-10T15:42:30.000 to 2014-10-10T23:10:13.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0348 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0348 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-ION-MAGSHEATH-96S-V1.0",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Voyager 1 plasma fit data from Saturn's magnetosphere. The fit parameters assume a convected isotropic proton Maxwellian distribution. Use of fit parameters is recommended as these are normally more accurate.  Since only the first 72 or last 72 energy/charge channels are telemetered to Earth from each M-mode spectra, derived parameters change significantly only every other set of spectra so the effective time resolution is 96 second.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ion-magsheath-96s-v1.0_n8it-hq5x",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUMM-ION-MAGSHEATH-96S-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-summ-ion-magsheath-96s-v1.0_n8it-hq5x",
-            "description": "This data set contains Voyager 1 plasma fit data from Saturn's magnetosphere. The fit parameters assume a convected isotropic proton Maxwellian distribution. Use of fit parameters is recommended as these are normally more accurate.  Since only the first 72 or last 72 energy/charge channels are telemetered to Earth from each M-mode spectra, derived parameters change significantly only every other set of spectra so the effective time resolution is 96 second.",
-            "title": "VG1 SAT PLS DERIVED ION MAGNETOSHEATH\n                                      96SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 SAT PLS DERIVED ION MAGNETOSHEATH\n                                      96SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-LSPN-N-NDR-HALLEY-V1.0",
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
-                "international halley watch",
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Large-Scale Phenomena Network has been organized into a set of digitized images and those left in the original analog state for reasons of quality, time coverage, or submission problems. These latter 1771 pieces of data are held in an archive both at Goddard Space Flight Center and with the Small Bodies Node of the Planetary Data System. (In the latter case, contact specifically the Comet Sub-Node of the PDS at the Laboratory for Atmospheric and Space Physics associated with the University of Colorado Boulder, for more assistance). Some of these analog images are presented in 'The International Halley Watch Atlas of Large-Scale Phenomena' (Brandt, John C., Niedner, Malcolm B. Jr., Rahe, Jurgen, 1992). The data cover a time range from 1984 December 22 through 1987 April 26 through 23 of the IHW Chronological Data Archive Collection",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-lspn-n-ndr-halley-v1.0_n8iv-7b7z",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-LSPN-N-NDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-lspn-n-ndr-halley-v1.0_n8iv-7b7z",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Large-Scale Phenomena Network has been organized into a set of digitized images and those left in the original analog state for reasons of quality, time coverage, or submission problems. These latter 1771 pieces of data are held in an archive both at Goddard Space Flight Center and with the Small Bodies Node of the Planetary Data System. (In the latter case, contact specifically the Comet Sub-Node of the PDS at the Laboratory for Atmospheric and Space Physics associated with the University of Colorado Boulder, for more assistance). Some of these analog images are presented in 'The International Halley Watch Atlas of Large-Scale Phenomena' (Brandt, John C., Niedner, Malcolm B. Jr., Rahe, Jurgen, 1992). The data cover a time range from 1984 December 22 through 1987 April 26 through 23 of the IHW Chronological Data Archive Collection",
-            "title": "IHW COMET HALLEY LSPN NON-DIGITIZED IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY LSPN NON-DIGITIZED IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/QUZD7OEEVRFZ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX16 Iowa Manual ThetaProbe Soil Moisture V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/QUZD7OEEVRFZ.",
-            "issued": "2016-05-31",
-            "temporal": "2016-05-31T00:00:00Z/2016-08-05T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-08-05",
-            "keyword": [
-                "soils",
-                "agriculture",
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
-            "identifier": "C2011916760-NSIDC_ECS",
             "description": "These data consist of calibrated soil moisture sensor measurements recorded by manual sampling teams at the field sites of SMAPVEX16-Iowa during two intensive observation periods in June and August of 2016. The sites were located throughout an experiment domain of about 30 km by 40 km approximately 30 km north of Ames, Iowa.",
-            "title": "SMAPVEX16 Iowa Manual ThetaProbe Soil Moisture V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQUZD7OEEVRFZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQUZD7OEEVRFZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16I_TPSM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16I_TPSM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990800780-NSIDC_ECS&m=37.93418934207473%21-110.109375%214%211%210%210%2C2&tl=1594227826%214",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990800780-NSIDC_ECS&m=37.93418934207473%21-110.109375%214%211%210%210%2C2&tl=1594227826%214",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16I_TPSM/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16I_TPSM/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QUZD7OEEVRFZ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/QUZD7OEEVRFZ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QUZD7OEEVRFZ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/QUZD7OEEVRFZ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2011916760-NSIDC_ECS",
+            "issued": "2016-05-31",
+            "keyword": [
+                "soils",
+                "agriculture",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/QUZD7OEEVRFZ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-08-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-93.57 42.39 -93.19 42.64",
+            "temporal": "2016-05-31T00:00:00Z/2016-08-05T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX16 Iowa Manual ThetaProbe Soil Moisture V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-PEPSSI-3-JUPITER-V1.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-pepssi-3-jupiter-v1.0_n8u8-dkmd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-PEPSSI-3-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-pepssi-3-jupiter-v1.0_n8u8-dkmd",
-            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS PEPSSI JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS PEPSSI JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-ESC1-V1.0",
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
+            "description": "This data set contains science\ndata acquired by the COPS, DFMS and RTOF ROSINA sensors between\n2014-11-19 and 2015-03-11 during the Escort phase 1 of the Rosetta\nmission at the comet 67P/CG",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-esc1-v1.0_n8x7-57c5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-2-ESC1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-2-esc1-v1.0_n8x7-57c5",
-            "description": "This data set contains science\ndata acquired by the COPS, DFMS and RTOF ROSINA sensors between\n2014-11-19 and 2015-03-11 during the Escort phase 1 of the Rosetta\nmission at the comet 67P/CG",
-            "title": "ROSETTA-ORBITER 67P ROSINA 2 ESC1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 2 ESC1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4JW8BTT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Geddes, J.A., R.V. Martin, B.L. Boys, and A. van Donkelaar. 2017-05-19. Global 3-Year Running Mean Ground-Level Nitrogen Dioxide (NO2) Grids from GOME, SCIAMACHY and GOME-2. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4JW8BTT. https://doi.org/10.7927/H4JW8BTT.",
-            "issued": "2017-05-19",
-            "temporal": "1996-01-01T00:00:00Z/2012-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-19",
-            "references": [
-                "https://doi.org/10.7927/H48C9T68",
-                "https://doi.org/10.1289/ehp.1409567"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C1401421022-SEDAC",
-            "description": "The Global 3-Year Running Mean Ground-Level Nitrogen Dioxide (NO2) Grids from GOME, SCIAMACHY and GOME-2 represent a series of three-year running mean grids (1996-2012) of ground level NO2 that were derived from Global Ozone Monitoring Experiment (GOME), SCanning Imaging Absorption SpectroMeter for Atmospheric CHartographY (SCIAMACHY) and Global Ozone Monitoring Experiment-2 (GOME-2) satellite retrievals. For each satellite-derived NO2 source, the relationship between satellite observations of tropospheric NO2 column densities and the NO2 concentrations at ground level relevant to human exposure is simulated, using the Goddard Earth Observing System chemical transport model (GEOS-Chem) to produce a mean NO2 concentration raster grid. The grid cell resolution is six arc-minutes (0.1 degree, or approximately 10 km at the equator) covering the global land surface.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Geddes, J.A., R.V. Martin, B.L. Boys, and A. van Donkelaar",
-            "title": "Global 3-Year Running Mean Ground-Level Nitrogen Dioxide (NO2) Grids from GOME, SCIAMACHY and GOME-2",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global 3-Year Running Mean Ground-Level Nitrogen Dioxide (NO2) Grids from GOME, SCIAMACHY and GOME-2 represent a series of three-year running mean grids (1996-2012) of ground level NO2 that were derived from Global Ozone Monitoring Experiment (GOME), SCanning Imaging Absorption SpectroMeter for Atmospheric CHartographY (SCIAMACHY) and Global Ozone Monitoring Experiment-2 (GOME-2) satellite retrievals. For each satellite-derived NO2 source, the relationship between satellite observations of tropospheric NO2 column densities and the NO2 concentrations at ground level relevant to human exposure is simulated, using the Goddard Earth Observing System chemical transport model (GEOS-Chem) to produce a mean NO2 concentration raster grid. The grid cell resolution is six arc-minutes (0.1 degree, or approximately 10 km at the equator) covering the global land surface.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4JW8BTT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4JW8BTT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2-1996-1998-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdei/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2-1996-1998-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdei-global-3-year-running-mean-no2-gome-sciamachy-gome2/maps",
+            "identifier": "C1401421022-SEDAC",
+            "issued": "2017-05-19",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4JW8BTT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-05-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H48C9T68",
+                "https://doi.org/10.1289/ehp.1409567"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-01-01T00:00:00Z/2012-12-31T00:00:00Z",
             "theme": [
                 "SDEI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global 3-Year Running Mean Ground-Level Nitrogen Dioxide (NO2) Grids from GOME, SCIAMACHY and GOME-2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/203",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Gilmanov, T.G. 2015. NPP Grassland: Badkhyz, Turkmenistan, 1948-1982, R1 . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/203",
-            "issued": "2015-04-20",
-            "temporal": "1941-01-01T00:00:00Z/1982-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2751943389-ORNL_CLOUD",
             "description": "This data set provides two data files in text format (.txt). One file contains estimates of above-ground live phytomass for an ephemeral desert steppe located in the Badkhyz Nature Reserve in southern Turkmenistan. Monthly measurements of plant biomass were made by harvest during the growing season (January-May) from 1948 through 1963. Afterwards, an annual measurement of peak live biomass was made in May from 1964 through 1982, with gaps for years 1973-1976. The second file contains monthly and annual climate data recorded at the study site from 1941 through 1982. Above-ground net production (ANPP) for the Badkhyz site is the lowest among the eight Eurasian grassland sites, at 100 g/m2/yr. Below-ground NPP for Badkhyz (1,745 g/m2/yr) was conservatively estimated from a similar dry, semiarid continental steppe in Northern Kazakhstan (i.e., Shortandy). Revision Notes: Only the documentation for this data set has been modified. The data files have been checked for accuracy and are identical to those originally published in 1998.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Badkhyz, Turkmenistan, 1948-1982, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F203",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F203",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_BDK/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_BDK/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BDK.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_BDK.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/203",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/203",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_BDK/comp/NPP_BDK.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_BDK/comp/NPP_BDK.pdf",
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
+            "identifier": "C2751943389-ORNL_CLOUD",
+            "issued": "2015-04-20",
+            "keyword": [
+                "vegetation",
+                "ecological dynamics",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/203",
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
             "spatial": "35.68 62.0",
+            "temporal": "1941-01-01T00:00:00Z/1982-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Badkhyz, Turkmenistan, 1948-1982, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4Z60KZ9",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN. 1996-12-31. Archive of Census Related Products (ACRP): 1990 Summary Tape File (STF1B). Version 1.00. Saginaw, MI. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4Z60KZ9. https://doi.org/10.7927/H4Z60KZ9.",
-            "issued": "1996-12-31",
-            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-12-31",
-            "references": [
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
-            "identifier": "C179001897-SEDAC",
-            "description": "The 1990 Summary Tape File (STF1B) portion of the Archive of Census Related Products (ACRP) contains population and housing data, along with additional demographic data for the U.S. The population data includes age, race, sex, marital status, Hispanic origin, and household type, while the housing data encompasses tenure, number of Units, value, number of rooms per Unit, and the use of the Unit. The data are available by county, county subdivision, place within county, tract/block numbering area (bna), blockgroup, and block. This portion of the ACRP is produced by the Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Saginaw, MI",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN",
-            "title": "Archive of Census Related Products (ACRP): 1990 Summary Tape File (STF1B)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-summary-tape-file-stf1b-1990/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 1990 Summary Tape File (STF1B) portion of the Archive of Census Related Products (ACRP) contains population and housing data, along with additional demographic data for the U.S. The population data includes age, race, sex, marital status, Hispanic origin, and household type, while the housing data encompasses tenure, number of Units, value, number of rooms per Unit, and the use of the Unit. The data are available by county, county subdivision, place within county, tract/block numbering area (bna), blockgroup, and block. This portion of the ACRP is produced by the Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4Z60KZ9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4Z60KZ9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-summary-tape-file-stf1b-1990/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-summary-tape-file-stf1b-1990/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-summary-tape-file-stf1b-1990/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-summary-tape-file-stf1b-1990/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-summary-tape-file-stf1b-1990",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/acrp-summary-tape-file-stf1b-1990",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/acrp/acrp-summary-tape-file-stf1b-1990/sedac-logo.jpg",
+            "identifier": "C179001897-SEDAC",
+            "issued": "1996-12-31",
+            "keyword": [
+                "earth science",
+                "population",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4Z60KZ9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
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
+            "release-place": "Saginaw, MI",
             "spatial": "-180.0 18.0 -66.0 72.0",
+            "temporal": "1990-04-01T00:00:00Z/1990-04-01T00:00:00Z",
             "theme": [
                 "ACRP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Archive of Census Related Products (ACRP): 1990 Summary Tape File (STF1B)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINSUM-V1.0",
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
+            "description": "This data set includes a summary table of the characteristics of known binary near-Earth asteroids, compiled by Petr Pravec and Petr Scheirich. A list of references to the original observations is also included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binsum-v1.0_n96a-vrkx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINSUM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binsum-v1.0_n96a-vrkx",
-            "description": "This data set includes a summary table of the characteristics of known binary near-Earth asteroids, compiled by Petr Pravec and Petr Scheirich. A list of references to the original observations is also included.",
-            "title": "BINARY NEAS SUMMARY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BINARY NEAS SUMMARY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/164",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-10-01",
-            "temporal": "2012-10-01T00:00:00Z/2022-09-01T00:00:00Z",
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
-                "jet propulsion laboratory",
-                "active",
-                "jpl cif",
-                "program"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jonas Zmuidzinas",
                 "hasEmail": "mailto:jonas.zmuidzinas@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_164",
             "description": "&lt;p&gt;Funds are distributed to each NASA Center to support emerging technologies and creative initiatives that leverage Center talent and capabilities. NASA scientists and engineers will lead projects and partnerships among Centers and with other agencies, research laboratories, academia and private industry are encouraged.&lt;/p&gt;",
-            "title": "Center Innovation Fund: JPL CIF Program",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/164",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_164",
+            "issued": "2012-10-01",
+            "keyword": [
+                "jet propulsion laboratory",
+                "active",
+                "jpl cif",
+                "program"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/164",
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
+            "temporal": "2012-10-01T00:00:00Z/2022-09-01T00:00:00Z",
+            "title": "Center Innovation Fund: JPL CIF Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RMPCRNS60ICX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO Science Team/Michael Gunson, Annmarie Eldering. 2024-04-10. OCO3_L1B_Science. Version 11r. OCO-3 Level 1B calibrated, geolocated science spectra, Retrospective Processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RMPCRNS60ICX. https://disc.gsfc.nasa.gov/datacollection/OCO3_L1B_Science_10r.html. Digital Science Data.",
-            "issued": "2021-05-31",
-            "temporal": "2019-08-06T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-31",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:andrey.savtchenko@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2910091100-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO3_L1B_Science",
             "creator": "OCO Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-3 Level 1B calibrated, geolocated science spectra, Retrospective Processing V11r (OCO3_L1B_Science) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRMPCRNS60ICX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRMPCRNS60ICX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1125807,167 +1125783,203 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L1B_Science_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L1B_Science_11r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_DQ_Statement_v10.pdf",
-                    "description": "OCO-3 Data Quality Statement",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Data Quality Statement",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_DQ_Statement_v10.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L1B_Science",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L1B_Science",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L1B_Science.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L1B_Science.11r/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov3.jpl.nasa.gov/",
-                    "description": "OCO-3 Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Project Home Page",
+                    "downloadURL": "https://ocov3.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L1B_Science.11r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L1B_Science.11r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO_L1B_ATBD.pdf",
-                    "description": "Level  1B Algorithm Theoretical Basis (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "Level  1B Algorithm Theoretical Basis (ATBD)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO_L1B_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_OCO3_B10_DUG.pdf",
-                    "description": "USER'S GUIDE",
                     "@type": "dcat:Distribution",
+                    "description": "USER'S GUIDE",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_OCO3_B10_DUG.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L1b.V7.pdf",
-                    "description": "Level 1B Software Interface Specification containing description of all data objects in data files",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1B Software Interface Specification containing description of all data objects in data files",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L1b.V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://ocov3.jpl.nasa.gov/science/publications/",
-                    "description": "Publications from the Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "Publications from the Science Team",
+                    "downloadURL": "https://ocov3.jpl.nasa.gov/science/publications/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
-                    "description": "OCO Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "OCO Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-3+Known+Data+Issues",
-                    "description": "OCO-3 Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Data Gaps",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-3+Known+Data+Issues",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
+            "identifier": "C2910091100-GES_DISC",
+            "issued": "2021-05-31",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/RMPCRNS60ICX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO3_L1B_Science",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 1B calibrated, geolocated science spectra, Retrospective Processing V11r (OCO3_L1B_Science) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PWS-4-SA-48.0SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of 48-second calibrated, averaged wave electric field intensities from the Voyager 2 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Jovian magnetosphere. For each 48-second interval, a geometric average field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kilo- Hertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of averages is the beginning of the averating interval. Averages are stored in units of volt/meter. During data gaps where complete 48-second intervals are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. Additional information about this dataset and the instrument which produced it can be found elsewhere in this catalog. An overview of the data in this data set can be found in Gurnett et al. [1979] and a complete instrument description can be found in Scarf and Gurnett [1977].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pws-4-sa-48.0sec_n9ae-im9f",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "comet sl9/jupiter collision",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PWS-4-SA-48.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pws-4-sa-48.0sec_n9ae-im9f",
-            "description": "This data set consists of 48-second calibrated, averaged wave electric field intensities from the Voyager 2 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Jovian magnetosphere. For each 48-second interval, a geometric average field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kilo- Hertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of averages is the beginning of the averating interval. Averages are stored in units of volt/meter. During data gaps where complete 48-second intervals are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. Additional information about this dataset and the instrument which produced it can be found elsewhere in this catalog. An overview of the data in this data set can be found in Gurnett et al. [1979] and a complete instrument description can be found in Scarf and Gurnett [1977].",
-            "title": "VOYAGER 2 JUP PLASMA WAVE SPECTROMETER RESAMP SPEC 48.0SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 2 JUP PLASMA WAVE SPECTROMETER RESAMP SPEC 48.0SEC"
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
+                    "downloadURL": "http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p6v11/",
+                    "mediaType": "image/fits"
+                }
+            ],
+            "identifier": "NASA-0000213",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "photons",
                 "space science",
@@ -1125980,366 +1125992,356 @@
                 "pulsars",
                 "gbm"
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
-            "identifier": "NASA-0000213",
-            "description": "Fermi is a powerful space observatory that will open a wide window on the universe. Gamma rays are the highest-energy form of light, and the gamma-ray sky is spectacularly different from the one we perceive with our own eyes. With a huge leap in all key capabilities, Fermi data will enable scientists to answer persistent questions across a broad range of topics, including supermassive black-hole systems, pulsars, the origin of cosmic rays, and searches for signals of new physics.",
-            "title": "LAT Pass 6 (V11) Archived Weekly files",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p6v11/",
-                    "mediaType": "image/fits"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT Pass 6 (V11) Archived Weekly files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/365",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bessemoulin, P., and D. Puech. 1998. BOREAS TF-06 SSA-YA Surface Energy Flux and Meteorological Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/365",
-            "issued": "2023-11-22",
-            "temporal": "1994-07-19T00:00:00Z/1994-09-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "atmospheric radiation",
-                "soils",
-                "precipitation",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure",
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
-            "identifier": "C2808130804-ORNL_CLOUD",
             "description": "Contains meteorology data collected at the SSA-YA tower flux site by the TF6 group. These data were reported at 10 minute intervals. The flux and ancillary data collected at the SSA-YA tower flux site by the TF6 group.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-06 SSA-YA Surface Energy Flux and Meteorological Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F365",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F365",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf6fxmet/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf6fxmet/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF06_Flux_Met.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF06_Flux_Met.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/365",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/365",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf6fxmet/comp/TF06_Flux_Met.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf6fxmet/comp/TF06_Flux_Met.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf6fxmet/comp/TF06_Flux_Met.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf6fxmet/comp/TF06_Flux_Met.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf6fxmet/comp/TF06_Flux_Met.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf6fxmet/comp/TF06_Flux_Met.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf6fxmet/comp/tf6fxmet.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf6fxmet/comp/tf6fxmet.def",
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
+            "identifier": "C2808130804-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmospheric radiation",
+                "soils",
+                "precipitation",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/365",
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
             "spatial": "53.66 -105.32",
+            "temporal": "1994-07-19T00:00:00Z/1994-09-19T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-06 SSA-YA Surface Energy Flux and Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/FIRMS/VIIRS/VJ114IMGT_NRT.002",
             "citation": "LANCEMODIS. 2016-02-16. VIIRS 375m, I-Band  Active Fire Product NRT (Vector Data). Version 2. NASA GSFC LANCE. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/FIRMS/VIIRS/VJ114IMGT_NRT.002. https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/viirs-i-band-active-fire-data. Formats: TXT, SHP, KML, WMS (TXT and SHP files contain all the attributes).. This data set was provided by LANCE FIRMS operated by NASA/GSFC/ESDIS with funding provided by NASA/HQ.",
-            "issued": "2016-02-15",
-            "temporal": "2016-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-05",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2013.12.008",
-                "https://doi.org/10.1007/978-1-4419-6749-7_29"
-            ],
-            "keyword": [
-                "earth science",
-                "surface thermal properties",
-                "ecological dynamics",
-                "land surface",
-                "biosphere",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LANCEMODIS",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
+            "creator": "LANCEMODIS",
             "data-presentation-form": "Formats: TXT, SHP, KML, WMS (TXT and SHP files contain all the attributes).",
-            "identifier": "C1355615368-LANCEMODIS",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "Near real-time (NRT) NOAA-20 (formally JPSS-1) Visible Infrared Imaging Radiometer Suite (VIIRS) Active Fire detection product is based on the instrument's 375 m nominal resolution data. Compared to other coarser resolution (\u22651km) satellite fire detection products, the improved 375 m data provide greater response over fires of relatively small areas, as well as improved mapping of large fire perimeters. Consequently, the data are well suited for use in support of fire management (e.g., near real-time alert systems), as well as other science applications requiring improved fire mapping fidelity. The 375 m product complements the baseline Suomi NPP/VIIRS 750 m active fire detection and characterization data, which was originally designed to provide continuity to the existing 1 km Earth Observing System Moderate Resolution Imaging Spectroradiometer (EOS/MODIS) active fire data record. Due to frequent data saturation issues, the current 375 m fire product provides detection information only with no sub-pixel fire characterization.\r\n\r\nVJ114IMGTDL_NRT are available in the following formats: TXT, SHP, KML, WMS. These data are also provided through the LANCE FIRMS Fire Email Alerts. Please note only the TXT and SHP files contain all the attributes. For the HDF version see: VJ114IMG_NRT \r\n\r\nRecommended reading: VIIRS 375m Active Fire Algorithm User Guide (https://earthdata.nasa.gov/files/VIIRS_375m_Users_guide_Dec15_v2.pdf) (updated December 2015).",
-            "release-place": "NASA GSFC LANCE",
-            "creator": "LANCEMODIS",
-            "title": "VIIRS NOAA-20 (JPSS-1) 375m, I-Band Active Fire Product NRT (Vector Data)",
-            "graphic-preview-description": "FIRMS Web Services",
-            "graphic-preview-file": "https://firms.modaps.eosdis.nasa.gov/web-services/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFIRMS%2FVIIRS%2FVJ114IMGT_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFIRMS%2FVIIRS%2FVJ114IMGT_NRT.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/FIRMS/noaa-20-viirs-c2",
-                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
                     "@type": "dcat:Distribution",
+                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/FIRMS/noaa-20-viirs-c2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data",
-                    "description": "NASA LANCE Near Real Time Data Product Information",
                     "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time Data Product Information",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://firms.modaps.eosdis.nasa.gov/map/",
-                    "description": "FIRMS Fire Map",
                     "@type": "dcat:Distribution",
+                    "description": "FIRMS Fire Map",
+                    "downloadURL": "https://firms.modaps.eosdis.nasa.gov/map/",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://firms.modaps.eosdis.nasa.gov/alerts/",
-                    "description": "FIRMS Email Alerts",
                     "@type": "dcat:Distribution",
+                    "description": "FIRMS Email Alerts",
+                    "downloadURL": "https://firms.modaps.eosdis.nasa.gov/alerts/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://firms.modaps.eosdis.nasa.gov/web-services/",
-                    "description": "FIRMS Web Services",
                     "@type": "dcat:Distribution",
+                    "description": "FIRMS Web Services",
+                    "downloadURL": "https://firms.modaps.eosdis.nasa.gov/web-services/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "FIRMS Web Services",
+            "graphic-preview-file": "https://firms.modaps.eosdis.nasa.gov/web-services/",
+            "identifier": "C1355615368-LANCEMODIS",
+            "issued": "2016-02-15",
+            "keyword": [
+                "earth science",
+                "surface thermal properties",
+                "ecological dynamics",
+                "land surface",
+                "biosphere",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/FIRMS/VIIRS/VJ114IMGT_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-08-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.rse.2013.12.008",
+                "https://doi.org/10.1007/978-1-4419-6749-7_29"
+            ],
+            "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "2016-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "FIRMS",
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS NOAA-20 (JPSS-1) 375m, I-Band Active Fire Product NRT (Vector Data)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCMAG-3-AST2-CALIBRATED-V3.0",
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
-                "21 lutetia"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains CALIBRATED DATA of the LUTETIA flyby Phase from July 7 until July 13, 2010. The closest approach (CA) took place on July 10, 2010 at 15:45",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpcmag-3-ast2-calibrated-v3.0_n9i8-fr3n",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "21 lutetia"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCMAG-3-AST2-CALIBRATED-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpcmag-3-ast2-calibrated-v3.0_n9i8-fr3n",
-            "description": "This dataset contains CALIBRATED DATA of the LUTETIA flyby Phase from July 7 until July 13, 2010. The closest approach (CA) took place on July 10, 2010 at 15:45",
-            "title": "ROSETTA-ORBITER LUTETIA RPCMAG 3 AST2 CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER LUTETIA RPCMAG 3 AST2 CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M11-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m11-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67P-M11-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67p-m11-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2014-12-19T23:25:00.000 to 2015-01-13T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP011 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP011 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PRA-3-RDR-LOWBAND-6SEC-V1.0",
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
+            "description": "This data set (VG2-J-PRA-3-RDR-LOWBAND-6SEC-V1.0) contains data acquired by the Voyager-2 Planetary Radio Astronomy (PRA) instrument during the Jupiter encounter. The bounding time interval set for most Voyager 2 Jupiter PDS data sets is the Voyager project defined 'far encounter' mission phase boundary (1979-07-02 to 1979-08-03). Since, however, the PRA instrument is able to observe planetary phenomenon at much larger ranges than other fields and particles experiments, this boundary is artificial with respect to PRA.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pra-3-rdr-lowband-6sec-v1.0_n9kh-qmvi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-PRA-3-RDR-LOWBAND-6SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-pra-3-rdr-lowband-6sec-v1.0_n9kh-qmvi",
-            "description": "This data set (VG2-J-PRA-3-RDR-LOWBAND-6SEC-V1.0) contains data acquired by the Voyager-2 Planetary Radio Astronomy (PRA) instrument during the Jupiter encounter. The bounding time interval set for most Voyager 2 Jupiter PDS data sets is the Voyager project defined 'far encounter' mission phase boundary (1979-07-02 to 1979-08-03). Since, however, the PRA instrument is able to observe planetary phenomenon at much larger ranges than other fields and particles experiments, this boundary is artificial with respect to PRA.",
-            "title": "VG2 JUP PRA CALIBRATED HI-RES LOW FREQ.\n                                        REC. BAND DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 JUP PRA CALIBRATED HI-RES LOW FREQ.\n                                        REC. BAND DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-CALIB-V1.3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Observations of solar or stellar targets for the purpose of calibrating detector wavelength scale, photometric sensitivity and flat fields.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-calib-v1.3_n9m2-xd7b",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bestia",
                 "calypso",
@@ -1126373,68 +1126375,44 @@
                 "atlas",
                 "cassini-huygens"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-CALIB-V1.3",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-calib-v1.3_n9m2-xd7b",
-            "description": "Observations of solar or stellar targets for the purpose of calibrating detector wavelength scale, photometric sensitivity and flat fields.",
-            "title": "CASSINI ORBITER SATURN UVIS CALIBRATION DATA V1.3",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER SATURN UVIS CALIBRATION DATA V1.3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3536",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schwartz, M., Pumphrey, H., Livesey, N., Read, W., and Fuller, R.. 2021-04-29. ML3MBCO. Version 005. MLS/Aura Level 3 Monthly Binned Carbon Monoxide (CO) Mixing Ratio on Assorted Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3536. https://disc.gsfc.nasa.gov/datacollection/ML3MBCO_005.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
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
-            "identifier": "C2042567756-GES_DISC",
-            "description": "ML3MBCO is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for carbon monoxide (CO) derived from radiances measured by the 640 GHz radiometer. The data version is 5.1. Data coverage is from August 2005 to current. Spatial coverage is near-global (-82 to +82 degrees latitude), with a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is between 215 and 0.00464 hPa, and the vertical resolution is about 6 km. Users of the ML3MBCO data product should read chapter 4 and section 3.7 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains two grid objects (profile and column data), each with a set of data and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3MBCO",
             "creator": "Schwartz, M., Pumphrey, H., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Monthly Binned Carbon Monoxide (CO) Mixing Ratio on Assorted Grids V005 (ML3MBCO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBCO_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3MBCO is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for carbon monoxide (CO) derived from radiances measured by the 640 GHz radiometer. The data version is 5.1. Data coverage is from August 2005 to current. Spatial coverage is near-global (-82 to +82 degrees latitude), with a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is between 215 and 0.00464 hPa, and the vertical resolution is about 6 km. Users of the ML3MBCO data product should read chapter 4 and section 3.7 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains two grid objects (profile and column data), each with a set of data and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3536",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3536",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1126444,90 +1126422,121 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBCO_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBCO_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBCO.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBCO.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBCO.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBCO.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBCO_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBCO_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBCO_005.png",
+            "identifier": "C2042567756-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3536",
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
+            "series-name": "ML3MBCO",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Monthly Binned Carbon Monoxide (CO) Mixing Ratio on Assorted Grids V005 (ML3MBCO) at GES DISC"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20110601.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-538",
+            "issued": "2018-06-25",
             "keyword": [
                 "sharad",
                 "ctx",
@@ -1126539,268 +1126548,234 @@
                 "mcs",
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
-            "identifier": "NASA-538",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 17",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20110601.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 17"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/LIS/LDAR/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Blakeslee, Richard J., Monte  Bateman and Douglas M. Mach.1997. LIGHTNING DETECTION AND RANGING (LDAR) RAW DATA [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/LIS/LDAR/DATA101",
-            "issued": "1997-01-01",
-            "temporal": "1997-02-28T00:00:00Z/2008-06-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "weather events",
-                "atmospheric electricity",
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
-            "identifier": "C1979878937-GHRC_DAAC",
             "description": "Lightning Detection and Ranging (LDAR) Raw data consists of level 1 lightning data collected from February 25, 1997 through June 11, 2008. The LDR system is located at the Kennedy Space Center. The center latitude and longitude of the LDAR network is 28.5387 and -80.6428. All x, y, and z values represent distance (in meters) from this location. LDAR is a volumetric lightning mapping system providing near real-time location of lightning in support of Space Shuttle operations. These data are in ASCII format.",
-            "graphic-preview-description": "N/A",
-            "title": "LIGHTNING DETECTION AND RANGING (LDAR) RAW DATA V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ksc-ldar/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLDAR%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLDAR%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ldarraw",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ldarraw",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/ghrc/lis/ldarraw/ldarB_2008.019_v2_daily.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/ghrc/lis/ldarraw/ldarB_2008.019_v2_daily.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ksc-ldar/doc/ldar_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ksc-ldar/doc/ldar_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ksc-ldar/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/ksc-ldar/browse/",
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
-            "spatial": "-83.0 26.0 -78.0 31.0",
-            "theme": [
-                "LIS",
-                "geospatial"
+            "graphic-preview-description": "N/A",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/ksc-ldar/browse/",
+            "identifier": "C1979878937-GHRC_DAAC",
+            "issued": "1997-01-01",
+            "keyword": [
+                "weather events",
+                "atmospheric electricity",
+                "atmosphere",
+                "earth science"
             ],
+            "landingPage": "https://doi.org/10.5067/LIS/LDAR/DATA101",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD02SSH.061",
-            "bureauCode": [
-                "026:00"
             ],
-            "citation": "MCST Team. 2017-05-01. MODIS/Terra Level 1B Subsampled Calibrated Radiance 5Km. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MOD02SSH.061. https://doi.org/10.5067/MODIS/MOD02SSH.061.",
-            "issued": "2017-05-05",
-            "temporal": "2000-02-24T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "earth science",
-                "ngda",
-                "national geospatial data asset",
-                "infrared wavelengths",
-                "visible wavelengths",
-                "spectral/engineering"
+            "modified": "2022-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
+            "spatial": "-83.0 26.0 -78.0 31.0",
+            "temporal": "1997-02-28T00:00:00Z/2008-06-11T23:59:59Z",
+            "theme": [
+                "LIS",
+                "geospatial"
             ],
+            "title": "LIGHTNING DETECTION AND RANGING (LDAR) RAW DATA V1"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
+            ],
+            "citation": "MCST Team. 2017-05-01. MODIS/Terra Level 1B Subsampled Calibrated Radiance 5Km. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MOD02SSH.061. https://doi.org/10.5067/MODIS/MOD02SSH.061.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASAD ULLAH",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1461234451-LAADS",
-            "description": "The MODIS/Terra Level 1B Subsampled Calibrated Radiances 5km (MOD02SSH) is a subsample from the MODIS Level 1B 1-km data. Every fifth pixel is taken from the MOD021KM product and written out to MOD02SSH. The subsampling starts at the third frame, and at the third line. Here, \"frame\" and \"line\" are naming conventions for pixels along and across the scan, respectively. Since MOD02SSH is a subsampled Level 1B , many things from the Level 1B documentation apply as well. That is, the MOD02SSH data product contains calibrated and geolocated at-aperture radiances for 36 bands generated from MODIS Level 1A scans of raw radiance (MOD01). The radiance units are in W/(m^2 um sr). Additional data are provided including quality flags, error estimates and calibration data. Visible, shortwave infrared (SWIR), and Near Infrared (NIR) measurements are made during daytime only, while radiances for Thermal Infrared (TIR) are measured continuously. \n\nAs its parent, the MOD02SSH is in HDF-EOS format, and all metadata structures and names are preserved for better convenience. However, some relevant changes are made where appropriate (e.g., the dimension mappings are updated to reflect the new one-to-one correspondence between the data and geolocations). The latter is one of the most important differences: in the MOD02SSH, there is no offset between data and geolocation pixels. The spatial coverage is almost similar to that from MOD021KM (nominally it is 2330 by 2030 km, cross-track by along-track, respectively). The MOD02SSH is produced continuously, and thus the processing provides 2-day repeat observations of the Earth with a repeat orbit pattern every 16 days.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MCST Team",
-            "title": "MODIS/Terra Level 1B Subsampled Calibrated Radiance 5Km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra Level 1B Subsampled Calibrated Radiances 5km (MOD02SSH) is a subsample from the MODIS Level 1B 1-km data. Every fifth pixel is taken from the MOD021KM product and written out to MOD02SSH. The subsampling starts at the third frame, and at the third line. Here, \"frame\" and \"line\" are naming conventions for pixels along and across the scan, respectively. Since MOD02SSH is a subsampled Level 1B , many things from the Level 1B documentation apply as well. That is, the MOD02SSH data product contains calibrated and geolocated at-aperture radiances for 36 bands generated from MODIS Level 1A scans of raw radiance (MOD01). The radiance units are in W/(m^2 um sr). Additional data are provided including quality flags, error estimates and calibration data. Visible, shortwave infrared (SWIR), and Near Infrared (NIR) measurements are made during daytime only, while radiances for Thermal Infrared (TIR) are measured continuously. \n\nAs its parent, the MOD02SSH is in HDF-EOS format, and all metadata structures and names are preserved for better convenience. However, some relevant changes are made where appropriate (e.g., the dimension mappings are updated to reflect the new one-to-one correspondence between the data and geolocations). The latter is one of the most important differences: in the MOD02SSH, there is no offset between data and geolocation pixels. The spatial coverage is almost similar to that from MOD021KM (nominally it is 2330 by 2030 km, cross-track by along-track, respectively). The MOD02SSH is produced continuously, and thus the processing provides 2-day repeat observations of the Earth with a repeat orbit pattern every 16 days.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD02SSH.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD02SSH.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mcst.gsfc.nasa.gov/content/l1b-documents",
-                    "description": "Level 1B Product User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1B Product User's Guide",
+                    "downloadURL": "https://mcst.gsfc.nasa.gov/content/l1b-documents",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD02SSH.061",
-                    "description": "Product Landing Page.",
                     "@type": "dcat:Distribution",
+                    "description": "Product Landing Page.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD02SSH.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MOD02SSH--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MOD02SSH--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MOD02SSH/contents.html",
-                    "description": "Direct access to MOD02SSH C6.1 OPeNDAP directory.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MOD02SSH C6.1 OPeNDAP directory.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MOD02SSH/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD02SSH/",
-                    "description": "Direct access to MOD02SSH C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MOD02SSH C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MOD02SSH/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mcst.gsfc.nasa.gov/sites/default/files/file_attachments/MODIS_L1B_ATBD_ver4.pdf",
-                    "description": "MODIS Level 1B Product ATBD.",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Level 1B Product ATBD.",
+                    "downloadURL": "https://mcst.gsfc.nasa.gov/sites/default/files/file_attachments/MODIS_L1B_ATBD_ver4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "identifier": "C1461234451-LAADS",
+            "issued": "2017-05-05",
+            "keyword": [
+                "earth science",
+                "ngda",
+                "national geospatial data asset",
+                "infrared wavelengths",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD02SSH.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Level 1B Subsampled Calibrated Radiance 5Km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/JG4HI4467BUA",
             "citation": "William J. Blackwell, MIT Lincoln Laboratory. 2023-10-01. TROPICS03ANTTL1A. Version 1.0. TROPICS03\u00a0L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/JG4HI4467BUA. https://disc.gsfc.nasa.gov/datacollection/TROPICS03ANTTL1A_1.0.html. Digital Science Data.",
-            "issued": "2021-07-19",
-            "temporal": "2021-07-19T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "references": [
-                "https://doi.org/10.5067/CBM5W8T7HHL6"
-            ],
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristan Morgan",
                 "hasEmail": "mailto:kristan.l.morgan@nasa.gov"
             },
+            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C3171499152-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The \"Time-Resolved Observations of Precipitation structure and storm Intensity with a Constellation of Smallsats\" (TROPICS) mission has a goal of providing nearly all-weather observations of three-dimensional temperature and humidity, as well as cloud ice and precipitation horizontal structure, at high temporal resolution to conduct high-value science investigations of tropical cyclones.  The mission comprises a constellation of six identical Space Vehicles (SVs) conforming to the 3U form factor and hosting a passive microwave spectrometer payload.  This dataset is produced from the Pathfinder satellite, a single 3U small satellite, which has launched previous to the constellation, on a sun-synchronous orbital plane.\n\nEach SV hosts an identical high-performance spectrometer named the TROPICS Millimeter-wave Sounder (TMS) that will provide temperature profiles using seven channels near the 118.75-GHz oxygen absorption line, water vapor profiles using three channels near the 183-GHz water vapor absorption line, imagery in a single channel near 90 GHz for precipitation measurements (when combined with higher resolution water vapor channels), and a single channel near 205 GHz that is more sensitive to cloud-sized ice particles.\n\nEach TROPICS netCDF file contains a granule of data with 81 spots and approximately 2880 scans, where a granule is defined as an orbit's worth of data.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TROPICS03ANTTL1A",
-            "creator": "William J. Blackwell, MIT Lincoln Laboratory",
-            "title": "TROPICS03\u00a0L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS01ANTTL1A_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJG4HI4467BUA",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJG4HI4467BUA",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1126810,307 +1126785,346 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS03ANTTL1A_1.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TROPICS03ANTTL1A_1.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TROPICS_L1A/TROPICS03ANTTL1A.1.0/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TROPICS_L1A/TROPICS03ANTTL1A.1.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TROPICS_L1A/TROPICS03ANTTL1A.1.0/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TROPICS_L1A/TROPICS03ANTTL1A.1.0/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICS03ANTTL1A_1.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TROPICS03ANTTL1A_1.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TRPCS-ATBD-034_L1_Rad_V2.1.pdf",
-                    "description": "TROPICS L1 Radiance ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS L1 Radiance ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TRPCS-ATBD-034_L1_Rad_V2.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS_UserGuide_base_Sept2023.pdf",
-                    "description": "TROPICS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS User Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS_UserGuide_base_Sept2023.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropics.ll.mit.edu/CMS/tropics/Mission-Overview",
-                    "description": "TROPICS Mission Page",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS Mission Page",
+                    "downloadURL": "https://tropics.ll.mit.edu/CMS/tropics/Mission-Overview",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS-03_TROPICS-06_L1_Validated_Stage1_Release_README_Aug2024_v2.pdf",
-                    "description": "TROPICS L1 README",
                     "@type": "dcat:Distribution",
+                    "description": "TROPICS L1 README",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPICS/TROPICS-03_TROPICS-06_L1_Validated_Stage1_Release_README_Aug2024_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TROPICS01ANTTL1A_01.png",
+            "identifier": "C3171499152-GES_DISC",
+            "issued": "2021-07-19",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/JG4HI4467BUA",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5067/CBM5W8T7HHL6"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "TROPICS03ANTTL1A",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-07-19T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "TROPICS (EVI-3)",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPICS03\u00a0L1A Orbital Geolocated Native-Resolution Antenna Temperatures V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/308/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vlad Popescu",
+                "hasEmail": "mailto:vmpopescu@gmail.com"
+            },
+            "description": "This paper takes an empirical approach\r\nto identify operational factors at busy airports that\r\nmay predate go-around maneuvers. Using four years\r\nof data from San Francisco International Airport, we\r\nbegin our investigation with a statistical approach\r\nto investigate which features of airborne, ground\r\noperations (e.g., number of inbound aircraft, number\r\nof aircraft taxiing from gate, etc.) or weather are\r\nmost likely to fluctuate, relative to nominal operations,\r\nin the minutes immediately preceding a missed\r\napproach. We analyze these findings both in terms\r\nof their implication on current airport operations\r\nand discuss how the antecedent factors may affect\r\nNextGen. Finally, as a means to assist air traffic controllers,\r\nwe draw upon techniques from the machine\r\nlearning community to develop a preliminary alert\r\nsystem for go-around prediction.",
+            "identifier": "DASHLINK_308",
             "issued": "2011-02-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ames",
                 "nasa",
                 "dashlink"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vlad Popescu",
-                "hasEmail": "mailto:vmpopescu@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/308/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_308",
-            "description": "This paper takes an empirical approach\r\nto identify operational factors at busy airports that\r\nmay predate go-around maneuvers. Using four years\r\nof data from San Francisco International Airport, we\r\nbegin our investigation with a statistical approach\r\nto investigate which features of airborne, ground\r\noperations (e.g., number of inbound aircraft, number\r\nof aircraft taxiing from gate, etc.) or weather are\r\nmost likely to fluctuate, relative to nominal operations,\r\nin the minutes immediately preceding a missed\r\napproach. We analyze these findings both in terms\r\nof their implication on current airport operations\r\nand discuss how the antecedent factors may affect\r\nNextGen. Finally, as a means to assist air traffic controllers,\r\nwe draw upon techniques from the machine\r\nlearning community to develop a preliminary alert\r\nsystem for go-around prediction.",
-            "title": "On the Statistics and Predictability of Go-Arounds",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "On the Statistics and Predictability of Go-Arounds"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1398-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-04T20:48:20.000 to 2016-02-04T23:07:08.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1398-v1.0_n9vg-bz9e",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1398-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1398-v1.0_n9vg-bz9e",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-04T20:48:20.000 to 2016-02-04T23:07:08.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1398 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1398 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0522-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-04T23:55:20.000 to 2015-01-05T02:40:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0522-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0522-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0522-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-04T23:55:20.000 to 2015-01-05T02:40:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0522 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0522 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2146",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and R.O. Green. 2022. MASTER: HyspIRI Airborne Campaign, California, Early Spring 2013, V2. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2146",
-            "issued": "2023-02-23",
-            "temporal": "2013-03-26T17:28:59Z/2013-04-19T23:26:42Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "infrared wavelengths",
-                "surface radiative properties",
-                "surface thermal properties",
-                "visible wavelengths",
-                "land surface",
-                "earth science",
-                "spectral/engineering"
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
-            "identifier": "C2731793704-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected as part of the Hyperspectral Infrared Imager (HyspIRI) mission's preparatory airborne campaign during 6 flights aboard a NASA ER-2 aircraft over California and Nevada, U.S., from 2013-03-26 to 2013-04-19. An additional purpose of this campaign was an underpass of Landsat 8. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes the flight path, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single band images and an RGB composite image from flight track 1 acquired on 26 March 2013 over Mono Lake, California, U.S. Source: /MASTERL1B_1393500_01_20130326_1728_1733_V01.jpg",
-            "title": "MASTER: HyspIRI Airborne Campaign, California, Early Spring 2013, V2",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_EarlyS2013_V2_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2146",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2146",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_HyspIRI_EarlyS2013_V2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_HyspIRI_EarlyS2013_V2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_EarlyS2013_V2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_EarlyS2013_V2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2146",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2146",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_HyspIRI_EarlyS2013_V2/comp/MASTER_HyspIRI_EarlyS2013_V2.pdf",
-                    "description": "MASTER: HyspIRI Airborne Campaign, California, Early Spring 2013, V2: MASTER_HyspIRI_EarlyS2013_V2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: HyspIRI Airborne Campaign, California, Early Spring 2013, V2: MASTER_HyspIRI_EarlyS2013_V2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_HyspIRI_EarlyS2013_V2/comp/MASTER_HyspIRI_EarlyS2013_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_EarlyS2013_V2_Fig1.jpg",
-                    "description": "Single band images and an RGB composite image from flight track 1 acquired on 26 March 2013 over Mono Lake, California, U.S. Source: /MASTERL1B_1393500_01_20130326_1728_1733_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single band images and an RGB composite image from flight track 1 acquired on 26 March 2013 over Mono Lake, California, U.S. Source: /MASTERL1B_1393500_01_20130326_1728_1733_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_EarlyS2013_V2_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single band images and an RGB composite image from flight track 1 acquired on 26 March 2013 over Mono Lake, California, U.S. Source: /MASTERL1B_1393500_01_20130326_1728_1733_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_EarlyS2013_V2_Fig1.jpg",
+            "identifier": "C2731793704-ORNL_CLOUD",
+            "issued": "2023-02-23",
+            "keyword": [
+                "infrared wavelengths",
+                "surface radiative properties",
+                "surface thermal properties",
+                "visible wavelengths",
+                "land surface",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2146",
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
             "spatial": "-123.78 31.95 -112.5 40.98",
+            "temporal": "2013-03-26T17:28:59Z/2013-04-19T23:26:42Z",
             "theme": [
                 "MASTER",
                 "HyspIRI Airborne",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: HyspIRI Airborne Campaign, California, Early Spring 2013, V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/161/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Santanu Das",
+                "hasEmail": "mailto:Santanu.Das-1@nasa.gov"
+            },
+            "description": "Damage characterization through wave propagation and scattering is of considerable interest to many non-destructive evaluation techniques. For fiber-reinforced composites, complex waves can be generated during the tests due to the non-homogeneous and anisotropic nature of the material when compared to isotropic materials. Additional complexities are introduced due to the presence of the damage and thus results in difficulty to characterize these defects. The inability to detect damage in composite structures limits their use in practice. A major task of structural health monitoring is to identify and characterize the existing defects or defect evolution through the interactions between structural features and multidisciplinary physical phenomena. In a wave-based approach to addressing this problem, the presence of damage is characterized by the changes in the signature of the resultant wave that propagates through the structure. In order to measure and characterize the wave propagation, we use the response of the surface-mounted piezoelectric transducers as input to an advanced machine-learning based classifier known as a support vector machine.",
+            "identifier": "DASHLINK_161",
             "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "dashlink",
                 "nasa",
                 "ames"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Santanu Das",
-                "hasEmail": "mailto:Santanu.Das-1@nasa.gov"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/161/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_161",
-            "description": "Damage characterization through wave propagation and scattering is of considerable interest to many non-destructive evaluation techniques. For fiber-reinforced composites, complex waves can be generated during the tests due to the non-homogeneous and anisotropic nature of the material when compared to isotropic materials. Additional complexities are introduced due to the presence of the damage and thus results in difficulty to characterize these defects. The inability to detect damage in composite structures limits their use in practice. A major task of structural health monitoring is to identify and characterize the existing defects or defect evolution through the interactions between structural features and multidisciplinary physical phenomena. In a wave-based approach to addressing this problem, the presence of damage is characterized by the changes in the signature of the resultant wave that propagates through the structure. In order to measure and characterize the wave propagation, we use the response of the surface-mounted piezoelectric transducers as input to an advanced machine-learning based classifier known as a support vector machine.",
-            "title": "Classification of Damage Signatures in Composite Plates using On",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Classification of Damage Signatures in Composite Plates using On"
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
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2007.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY07 NASA Financial Report",
+                    "downloadURL": "http://www.nasa.gov/pdf/202960main_NASA_FY07_Financial_Report.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FY07 NASA Financial Report"
+                }
+            ],
+            "identifier": "OCIO-Fitara-84",
             "issued": "2006-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "plan",
                 "budget",
@@ -1127119,47 +1127133,35 @@
                 "performance",
                 "financial"
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
-            "identifier": "OCIO-Fitara-84",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2007.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2007: NASA Financial Report",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/202960main_NASA_FY07_Financial_Report.pdf",
-                    "description": "FY07 NASA Financial Report",
-                    "@type": "dcat:Distribution",
-                    "title": "FY07 NASA Financial Report"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2007: NASA Financial Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-STOOKE-SHAPE-MODELS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Optical shape models of 10 planetary moons and asteroids, derived from spacecraft imaging by Philip Stooke.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-stooke-shape-models-v1.0_na9s-m2bm",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "gaspra",
                 "epimetheus",
@@ -1127170,72 +1127172,45 @@
                 "n7 larissa",
                 "n8 proteus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-STOOKE-SHAPE-MODELS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-stooke-shape-models-v1.0_na9s-m2bm",
-            "description": "Optical shape models of 10 planetary moons and asteroids, derived from spacecraft imaging by Philip Stooke.",
-            "title": "STOOKE SMALL BODY SHAPE MODELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STOOKE SMALL BODY SHAPE MODELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/J99FI2U38YRN",
             "citation": "Anenberg, Susan C.. 2023-02-28. SFC_NITROGEN_DIOXIDE_CONC. Version 1. Nitrogen Dioxide Surface-Level Annual Average Concentrations V1. NASA Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/J99FI2U38YRN. https://disc.gsfc.nasa.gov/datacollection/SFC_NITROGEN_DIOXIDE_CONC_1.html. Digital Science Data.",
-            "issued": "2023-02-04",
-            "temporal": "1990-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-04",
-            "references": [
-                "https://doi.org/10.1016/s2542-5196(21)00255-2"
-            ],
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SUSAN ANENBERG",
                 "hasEmail": "mailto:sanenberg@gwu.edu"
             },
+            "creator": "Anenberg, Susan C.",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2622658960-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Nitrogen Dioxide Surface-Level Annual Average Concentrations Product (SFC_NITROGEN_DIOXIDE_CONC) contains estimated global NO2 surface values derived using a Land Use Regression (LUR) model (based on 5220 NO2 monitors in 58 countries and land use variables) for the years 2010-2012. NO2 column densities from the Ozone Monitoring Instrument and MERRA-2 scale the concentrations to other years between 1990 and 2020. This product is part of NASA's Health and Air Quality Applied Sciences Team (HAQAST) effort.\n\nThe data are global over land and span the latitude range between 60 south and 75 north, gridded at 0.0083 degree resolution (array size is 43080 x 16200). Data variables include surface NO2, as well as latitude and longitude values. The data are written to files using the new version 4 netCDF format. The average file size is about 150 Megabytes.",
-            "release-place": "NASA Goddard Space Flight Center",
-            "series-name": "SFC_NITROGEN_DIOXIDE_CONC",
-            "creator": "Anenberg, Susan C.",
-            "title": "Nitrogen Dioxide Surface-Level Annual Average Concentrations V1 (SFC_NITROGEN_DIOXIDE_CONC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SFC_NITROGEN_DIOXIDE_CONC_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ99FI2U38YRN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ99FI2U38YRN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1127245,325 +1127220,326 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SFC_NITROGEN_DIOXIDE_CONC_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SFC_NITROGEN_DIOXIDE_CONC_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/SFC_NITROGEN_DIOXIDE_CONC.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/SFC_NITROGEN_DIOXIDE_CONC.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SFC_NITROGEN_DIOXIDE_CONC_1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SFC_NITROGEN_DIOXIDE_CONC_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/HAQAST/SFC_NITROGEN_DIOXIDE_CONC.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/HAQAST/SFC_NITROGEN_DIOXIDE_CONC.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/SFC_NITROGEN_DIOXIDE_CONC.1/doc/README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/SFC_NITROGEN_DIOXIDE_CONC.1/doc/README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://haqast.org/",
-                    "description": "HAQAST Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "HAQAST Home Page",
+                    "downloadURL": "https://haqast.org/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://haqast.org/haqast-publications-2/",
-                    "description": "HAQAST Publications",
                     "@type": "dcat:Distribution",
+                    "description": "HAQAST Publications",
+                    "downloadURL": "https://haqast.org/haqast-publications-2/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SFC_NITROGEN_DIOXIDE_CONC_1.png",
+            "identifier": "C2622658960-GES_DISC",
+            "issued": "2023-02-04",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/J99FI2U38YRN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1016/s2542-5196(21)00255-2"
+            ],
+            "release-place": "NASA Goddard Space Flight Center",
+            "series-name": "SFC_NITROGEN_DIOXIDE_CONC",
             "spatial": "-180.0 -60.0 180.0 75.0",
+            "temporal": "1990-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
             "theme": [
                 "HAQAST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nitrogen Dioxide Surface-Level Annual Average Concentrations V1 (SFC_NITROGEN_DIOXIDE_CONC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/5WAIACLZODHP",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Coordinated Eastern Arctic Experiment (CEAREX) Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/5WAIACLZODHP.",
-            "issued": "1988-03-01",
-            "temporal": "1988-03-01T00:00:00Z/1989-05-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1989-05-31",
-            "keyword": [
-                "atmospheric water vapor",
-                "sea ice",
-                "salinity/density",
-                "oceans",
-                "ocean chemistry",
-                "ocean acoustics",
-                "ecosystems",
-                "earth science",
-                "biosphere",
-                "bathymetry/seafloor topography",
-                "atmospheric winds",
-                "atmospheric temperature",
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
-            "identifier": "C1386206955-NSIDCV0",
             "description": "CEAREX was a multi-platform field program conducted in the Norwegian Seas and Greenland north to Svalbard from September 1988 through May 1989. Canada, Denmark, France, Norway and the United States participated in the experiment.",
-            "title": "Coordinated Eastern Arctic Experiment (CEAREX) Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5WAIACLZODHP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5WAIACLZODHP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0020_cearex_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0020_cearex_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/5WAIACLZODHP",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/5WAIACLZODHP",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/5WAIACLZODHP",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/5WAIACLZODHP",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206955-NSIDCV0",
+            "issued": "1988-03-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "sea ice",
+                "salinity/density",
+                "oceans",
+                "ocean chemistry",
+                "ocean acoustics",
+                "ecosystems",
+                "earth science",
+                "biosphere",
+                "bathymetry/seafloor topography",
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/5WAIACLZODHP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1989-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-30.0 60.0 30.0 90.0",
+            "temporal": "1988-03-01T00:00:00Z/1989-05-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Coordinated Eastern Arctic Experiment (CEAREX) Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-SR%2FUR%2FNR-PPS-2%2F4-OCC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-sr-ur-nr-pps-2-4-occ-v1.0_naeu-x3m6",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "s rings",
                 "n rings",
                 "u rings"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-SR%2FUR%2FNR-PPS-2%2F4-OCC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-sr-ur-nr-pps-2-4-occ-v1.0_naeu-x3m6",
-            "description": "not applicable",
-            "title": "VG2 SR/UR/NR PPS EDITED/RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 SR/UR/NR PPS EDITED/RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/PY75YPQOMP6W",
             "citation": "NASA/GSFC. 2024-05-24. EOLE1. Version 001. Eole 1 Raw Temperature, Pressure, and Location Data Near 200 mbar. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/PY75YPQOMP6W. https://disc.gsfc.nasa.gov/datacollection/EOLE1_001.html. Digital Science Data.",
-            "issued": "2024-02-06",
-            "temporal": "1971-08-27T00:00:00Z/1972-07-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-06",
-            "keyword": [
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C3031691150-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "619"
-            },
             "description": "The Eole 1 Raw Temperature, Pressure and Location Data Near 200 mbar product was obtained from the experimenter and originally consisted of a BCD tape generated on a CDC 6600 computer, subsequently converted to ASCII characters. The data are arranged sequentially by orbit. Data from each orbit are contained in a single record and consist of a heading giving the orbit number, the number of balloons contacted, and a control number. Following the heading, the balloon number, date of observation, location, and ambient temperature and pressure are listed. A maximum of 25 balloon contacts may appear in a single record. Empty records with no balloon contacts have been omitted. These data were obtained from balloons near 200 mbar and are for the region between 30 deg S and 60 deg S. The upper level wind speed and direction can be generated from these data by comparing individual balloon locations obtained from successive orbits. Eole, also known as the Cooperative Application Satellite (CAS-A), was the the second French experimental relay and meteorological satellite and the first launched by NASA under a cooperative agreement with the Centre National d'Etudes Spatiales (CNES).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "EOLE1",
-            "creator": "NASA/GSFC",
-            "title": "Eole 1 Raw Temperature, Pressure and Location Data Near 200 mbar (EOLE1) at GES DISC",
-            "graphic-preview-description": "Eole satellite.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/EOLE1_Sample.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPY75YPQOMP6W",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPY75YPQOMP6W",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/EOLE1_Sample.jpg",
-                    "description": "Eole satellite.",
                     "@type": "dcat:Distribution",
+                    "description": "Eole satellite.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/EOLE1_Sample.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/EOLE1_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/EOLE1_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EOLE1_Level1/EOLE1.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EOLE1_Level1/EOLE1.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=EOLE1_001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=EOLE1_001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EOLE1_Level1/EOLE1.001/doc/README.EOLE1.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EOLE1_Level1/EOLE1.001/doc/README.EOLE1.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Eole/3.3_Product_Documentation/3.3.5_Product_Quality/DSC_0219.pdf",
-                    "description": "Dataset Catalog 0219 for Satellite to Satellite System Observations and Data Formats",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Catalog 0219 for Satellite to Satellite System Observations and Data Formats",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Eole/3.3_Product_Documentation/3.3.5_Product_Quality/DSC_0219.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Eole/EOLE1_Inventory.xlsx",
-                    "description": "EOLE Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "EOLE Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Eole/EOLE1_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Eole satellite.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/EOLE1_Sample.jpg",
+            "identifier": "C3031691150-GES_DISC",
+            "issued": "2024-02-06",
+            "keyword": [
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/PY75YPQOMP6W",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-02-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "619"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "EOLE1",
             "spatial": "-180.0 -60.0 180.0 -30.0",
+            "temporal": "1971-08-27T00:00:00Z/1972-07-04T23:59:59.999Z",
             "theme": [
                 "EOSDIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Eole 1 Raw Temperature, Pressure and Location Data Near 200 mbar (EOLE1) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-10-05",
-            "temporal": "2021-10-05T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "topo",
-                "coordinates",
-                "space",
-                "station",
-                "ephemeris",
-                "iss",
-                "trajectory",
-                "coords",
-                "location",
-                "international"
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
-            "identifier": "nasa-iss-data_2021-10-05_nami-kjmm",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-10-05",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1127686,271 +1127662,297 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-10-05_nami-kjmm",
+            "issued": "2021-10-05",
+            "keyword": [
+                "topo",
+                "coordinates",
+                "space",
+                "station",
+                "ephemeris",
+                "iss",
+                "trajectory",
+                "coords",
+                "location",
+                "international"
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
+            "temporal": "2021-10-05T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-10-05"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4348H83",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2005-12-31. Last of the Wild Project, Version 2, 2005 (LWP-2): Last of the Wild Dataset (Geographic). Version 2.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4348H83. https://doi.org/10.7927/H4348H83.",
-            "issued": "2005-12-31",
-            "temporal": "1995-01-01T00:00:00Z/2004-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4M61H5F",
-                "https://doi.org/10.7927/H4GF0RFQ",
-                "https://doi.org/10.7927/H4ZC80SS",
-                "https://doi.org/10.7927/H4BP00QC",
-                "https://doi.org/10.7927/H46W980H"
-            ],
-            "keyword": [
-                "biosphere",
-                "land surface",
-                "land use/land cover",
-                "ecosystems",
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
-            "identifier": "C179001812-SEDAC",
-            "description": "The Last of the Wild Dataset of the Last of the Wild Project, Version 2, 2005 (LWP-2)  is derived from the LWP-2 Human Footprint Dataset. The gridded data are classified according to their raster value (wild = 0-10; not wild >10). The ten largest polygons of more than 5 square kilometers within each biome by realm are selected and identified. The dataset in Clarke 1866 Geographic Coordinate System is produced by the Wildlife Conservation Society (WCS) and the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Last of the Wild Project, Version 2, 2005 (LWP-2): Last of the Wild Dataset (Geographic)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Last of the Wild Dataset of the Last of the Wild Project, Version 2, 2005 (LWP-2)  is derived from the LWP-2 Human Footprint Dataset. The gridded data are classified according to their raster value (wild = 0-10; not wild >10). The ten largest polygons of more than 5 square kilometers within each biome by realm are selected and identified. The dataset in Clarke 1866 Geographic Coordinate System is produced by the Wildlife Conservation Society (WCS) and the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4348H83",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4348H83",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v2/wildareas-v2-last-of-the-wild-geographic/ltw-world-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v2/wildareas-v2-last-of-the-wild-geographic/ltw-world-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v2-last-of-the-wild-geographic/maps",
+            "identifier": "C179001812-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "biosphere",
+                "land surface",
+                "land use/land cover",
+                "ecosystems",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4348H83",
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
+                "https://doi.org/10.7927/H4M61H5F",
+                "https://doi.org/10.7927/H4GF0RFQ",
+                "https://doi.org/10.7927/H4ZC80SS",
+                "https://doi.org/10.7927/H4BP00QC",
+                "https://doi.org/10.7927/H46W980H"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-01-01T00:00:00Z/2004-12-31T00:00:00Z",
             "theme": [
                 "LWP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Last of the Wild Project, Version 2, 2005 (LWP-2): Last of the Wild Dataset (Geographic)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0410-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-05T15:26:10.000 to 2014-11-05T19:39:27.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0410-v1.0_nanu-vtrt",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0410-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0410-v1.0_nanu-vtrt",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-05T15:26:10.000 to 2014-11-05T19:39:27.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0410 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0410 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-E-HRII-3%2F4-EPOXI-EARTH-V2.0",
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
-                "earth",
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains calibrated, 1.05- to 4.8-micron spectra of Earth acquired by the High Resolution Infrared Spectrometer (HRII) during the EPOCh and Cruise 2 phases of the EPOXI mission. Five sets of observations were acquired on 18-19 March, 28-29 May and 04-05 June 2008 and on 27-28 March and 04-05 October 2009 to characterize Earth as an analog for extrasolar planets. Each observing period lasted approximately 24 hours, and spectra were acquired twice every 2 hours. During the observing period in May 2008, the Moon transited across Earth as seen from the spacecraft. HRII spectra were not acquired during the first attempt of an Earth south polar observation on 27-28 September 2009 because fault protection turned that instrument off; the full sequence was successfully rerun on 04-05 October 2009. Version 2 corrects an error in the IR absolute calibration that previously inflated all spectra by a factor of 2.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-e-hrii-3-4-epoxi-earth-v2.0_napp-x5rx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "earth",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-E-HRII-3%2F4-EPOXI-EARTH-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-e-hrii-3-4-epoxi-earth-v2.0_napp-x5rx",
-            "description": "This dataset contains calibrated, 1.05- to 4.8-micron spectra of Earth acquired by the High Resolution Infrared Spectrometer (HRII) during the EPOCh and Cruise 2 phases of the EPOXI mission. Five sets of observations were acquired on 18-19 March, 28-29 May and 04-05 June 2008 and on 27-28 March and 04-05 October 2009 to characterize Earth as an analog for extrasolar planets. Each observing period lasted approximately 24 hours, and spectra were acquired twice every 2 hours. During the observing period in May 2008, the Moon transited across Earth as seen from the spacecraft. HRII spectra were not acquired during the first attempt of an Earth south polar observation on 27-28 September 2009 because fault protection turned that instrument off; the full sequence was successfully rerun on 04-05 October 2009. Version 2 corrects an error in the IR absolute calibration that previously inflated all spectra by a factor of 2.",
-            "title": "EPOXI EARTH OBS - HRII CALIBRATED SPECTRA V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI EARTH OBS - HRII CALIBRATED SPECTRA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M09-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m09-inf-refl-v1.0_natf-gjdy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M09-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m09-inf-refl-v1.0_natf-gjdy",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP009 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP009 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-2-ENGEDR-V1.0",
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
+            "description": "Raw, uncalibrated engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-2-engedr-v1.0_naud-4dvv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-TEGA-2-ENGEDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-tega-2-engedr-v1.0_naud-4dvv",
-            "description": "Raw, uncalibrated engineering, housekeeping and scientific data collected from the Thermal Evolved Gas Analyzer (TEGA) aboard the 2007 Mars Phoenix Lander.",
-            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 2 ENGEDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHX MARS THERMAL EVOLVED GAS ANALYZER 2 ENGEDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IUE-C-SWP-3-EDR-IUECDB-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains spectral observations of 37 comets obtained with the Short-wavelength prime (SWP) spectrograph on the International Ultraviolet Explorer (IUE) satellite. Both low dispersion data from 1150-1975 A and high dispersion data from 1145-1930A (with partial coverage from 1930-2198A) are included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iue-c-swp-3-edr-iuecdb-v1.0_navy-skk3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "19p/borrelly 1 (1904 y2)",
                 "27p/crommelin 1 (1928 w1)",
@@ -1127993,881 +1127995,881 @@
                 "10p/tempel 2 (1873 n1)",
                 "109p/swift-tuttle 1 (1862 o1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IUE-C-SWP-3-EDR-IUECDB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iue-c-swp-3-edr-iuecdb-v1.0_navy-skk3",
-            "description": "This data set contains spectral observations of 37 comets obtained with the Short-wavelength prime (SWP) spectrograph on the International Ultraviolet Explorer (IUE) satellite. Both low dispersion data from 1150-1975 A and high dispersion data from 1145-1930A (with partial coverage from 1930-2198A) are included.",
-            "title": "IUE SWP DATA OF COMETS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IUE SWP DATA OF COMETS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1431",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Henderson, J., J.B. Miller, T. Nehrkorn, R.Y-W. Chang, C. Sweeney, N. Steiner, S.C. Wofsy, and C.E. Miller. 2017. CARVE: L4 Gridded Footprints from WRF-STILT model, 2012-2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1431",
-            "issued": "2022-05-09",
-            "temporal": "2012-01-01T00:00:00Z/2016-04-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric winds",
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
-            "identifier": "C2236316518-ORNL_CLOUD",
             "description": "This data set provides Weather Research and Forecasting (WRF) Stochastic Time-Inverted Lagrangian Transport (STILT) Footprint data products for particle receptors located at positions along Carbon in Arctic Reservoirs Vulnerability Experiment (CARVE) flight paths (2012 - 2015) and various meteorological stations in Alaska and the Canadian Arctic. Each product consists of multiple NetCDF footprint files packaged as a TAR/GZIP file. These aircraft and station positions were treated as receptors in the WRF-STILT model in order to simulate the land surface influence on observed atmospheric constituents. The measurements included in this data set are crucial for understanding changes in Arctic carbon cycling and the potential threats posed by thawing of Arctic permafrost.",
-            "graphic-preview-description": "Surface contours (50% --- blue; 80% --- purple) for the average WRF-STILT influence functions (mid-afternoon averages 2012-2014)  show CO2 and CH4 measurements from the CARVE tower have a high sensitivity to the boreal forests and lowlands of interior Alaska. Cyan and red circles are shown for the footprints after filtering (from Karion et al., 2016).",
-            "title": "CARVE: L4 Gridded Footprints from WRF-STILT model, 2012-2016",
-            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/CARVE_L4_WRF-STILT_Footprint_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1431",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1431",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/carve/campaign/CARVE_L4_WRF-STILT_Footprint/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/carve/campaign/CARVE_L4_WRF-STILT_Footprint/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L4_WRF-STILT_Footprint.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L4_WRF-STILT_Footprint.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1431",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1431",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L4_WRF-STILT_Footprint/comp/CARVE_L4_WRF-STILT_Footprint.pdf",
-                    "description": "CARVE: L4 Gridded Footprints from WRF-STILT model, 2012-2016: CARVE_L4_WRF-STILT_Footprint.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "CARVE: L4 Gridded Footprints from WRF-STILT model, 2012-2016: CARVE_L4_WRF-STILT_Footprint.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L4_WRF-STILT_Footprint/comp/CARVE_L4_WRF-STILT_Footprint.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L4_WRF-STILT_Footprint/comp/carve_wrf-stilt_inventory.csv",
-                    "description": "CARVE: L4 Gridded Footprints from WRF-STILT model, 2012-2016: carve_wrf-stilt_inventory.csv",
                     "@type": "dcat:Distribution",
+                    "description": "CARVE: L4 Gridded Footprints from WRF-STILT model, 2012-2016: carve_wrf-stilt_inventory.csv",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L4_WRF-STILT_Footprint/comp/carve_wrf-stilt_inventory.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L4_WRF-STILT_Footprint_Fig1.jpg",
-                    "description": "Surface contours (50% --- blue; 80% --- purple) for the average WRF-STILT influence functions (mid-afternoon averages 2012-2014)  show CO2 and CH4 measurements from the CARVE tower have a high sensitivity to the boreal forests and lowlands of interior Alaska. Cyan and red circles are shown for the footprints after filtering (from Karion et al., 2016).",
                     "@type": "dcat:Distribution",
+                    "description": "Surface contours (50% --- blue; 80% --- purple) for the average WRF-STILT influence functions (mid-afternoon averages 2012-2014)  show CO2 and CH4 measurements from the CARVE tower have a high sensitivity to the boreal forests and lowlands of interior Alaska. Cyan and red circles are shown for the footprints after filtering (from Karion et al., 2016).",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L4_WRF-STILT_Footprint_Fig1.jpg",
+                    "mediaType": "image/jpeg",
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
                 }
             ],
+            "graphic-preview-description": "Surface contours (50% --- blue; 80% --- purple) for the average WRF-STILT influence functions (mid-afternoon averages 2012-2014)  show CO2 and CH4 measurements from the CARVE tower have a high sensitivity to the boreal forests and lowlands of interior Alaska. Cyan and red circles are shown for the footprints after filtering (from Karion et al., 2016).",
+            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/CARVE_L4_WRF-STILT_Footprint_Fig1.jpg",
+            "identifier": "C2236316518-ORNL_CLOUD",
+            "issued": "2022-05-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric winds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1431",
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
             "spatial": "-180.0 30.0 180.0 90.0",
+            "temporal": "2012-01-01T00:00:00Z/2016-04-28T23:59:59Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: L4 Gridded Footprints from WRF-STILT model, 2012-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-NIMS-3-TUBE-V1.0",
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
-                "galileo",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-nims-3-tube-v1.0_naxw-usqj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-NIMS-3-TUBE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-nims-3-tube-v1.0_naxw-usqj",
-            "description": "Unknown",
-            "title": "NIMS SPECTRAL IMAGE CUBES OF THE EARTH: E1 & E2 ENCOUNTERS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NIMS SPECTRAL IMAGE CUBES OF THE EARTH: E1 & E2 ENCOUNTERS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3COD.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3COD.006. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-03T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "air quality",
-                "atmospheric temperature",
-                "atmospheric chemistry"
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
-            "identifier": "C1629286378-LARC",
             "description": "TL3COD_6 is the Tropospheric Emission Spectrometer (TES)/Aura Level3 Carbon Monoxide Daily Gridded Version 6 data product. It consists of daily atmospheric temperature and VMR for the atmospheric species, carbon monoxide, which are provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. \r\rThe TES Science Data Processing L3 subsystem interpolated L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. The L3 standard data products are composed of L3 HDF-EOS grid data. A separate product file was produced for each different atmospheric species. TES obtained data in two basic observation modes: Limb or Nadir; Nadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing were the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey was not split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly.",
-            "title": "TES/Aura L3 Carbon Monoxide Daily Gridded V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3COD.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3COD.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L3daily.cgi",
-                    "description": "Report of TES Level 3 Daily Data Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 3 Daily Data Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L3daily.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_alg_req_prod.pdf",
-                    "description": "TES Level 3 Algorithms, Requirements & Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 Algorithms, Requirements & Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_alg_req_prod.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L3ReadSoftwareV1.txt",
-                    "description": "Basic IDL Tools for extracting information from TES L3 HDF Product files",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extracting information from TES L3 HDF Product files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L3ReadSoftwareV1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_3.pdf",
-                    "description": "TES Level 3 Versioning - Level 3 Global Survey Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 Versioning - Level 3 Global Survey Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/TES",
-                    "description": "NASA Earthdata Forum - TES Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - TES Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/TES",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L3_products.pdf",
-                    "description": "Aura-TES L3 Products: Quality Description",
                     "@type": "dcat:Distribution",
+                    "description": "Aura-TES L3 Products: Quality Description",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L3_products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L3ReadSoftwareV1.tar",
-                    "description": "TES Level 3 Read Software Package Version 1 - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 Read Software Package Version 1 - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L3ReadSoftwareV1.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Data_Users_Guide.pdf",
-                    "description": "TES Level 3 (L3) Data/Plot User\u2019s Guide Version 1.0 December 17, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 (L3) Data/Plot User\u2019s Guide Version 1.0 December 17, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Data_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/tes_project.pdf",
-                    "description": "TES Langley ASDC Project Guide",
                     "@type": "dcat:Distribution",
+                    "description": "TES Langley ASDC Project Guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/tes_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3COD.006",
-                    "description": "DOI data set landing page for TL3COD_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3COD_6",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3COD.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3COD.006/contents.html",
-                    "description": "OPeNDAP data access for TL3COD_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3COD_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3COD.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1629286378-LARC",
-                    "description": "Earthdata Search for TL3COD_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3COD_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1629286378-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3COD.006/",
-                    "description": "ASDC Direct Data Download for TL3COD_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL3COD_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3COD.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1629286378-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "air quality",
+                "atmospheric temperature",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3COD.006",
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
+            "temporal": "2004-09-03T00:00:00Z/2018-01-22T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 Carbon Monoxide Daily Gridded V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/68",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Deering, D. W., and E. Middleton. 1994. PARABOLA Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/68",
-            "issued": "2024-05-05",
-            "temporal": "1987-06-06T00:00:00Z/1989-08-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation",
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
-            "identifier": "C2980142552-ORNL_CLOUD",
             "description": "Sky & ground radiance values averaged to give equal intervals of viewing angles",
-            "graphic-preview-description": "Browse Image",
-            "title": "PARABOLA Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F68",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F68",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_parabola/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_parabola/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Parabola_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Parabola_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/68",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/68",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_parabola/comp/parabola.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_parabola/comp/parabola.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_parabola/comp/parabola.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_parabola/comp/parabola.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_parabola/comp/Parabola_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_parabola/comp/Parabola_Data.pdf",
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
+            "identifier": "C2980142552-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/68",
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
             "spatial": "-96.59 39.05 -96.5 39.1",
+            "temporal": "1987-06-06T00:00:00Z/1989-08-08T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PARABOLA Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-EXT3-SAMPLES-V1.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set\nincludes all data from the ROSETTA EXTENSION 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-ext3-samples-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-EXT3-SAMPLES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-ext3-samples-v1.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set\nincludes all data from the ROSETTA EXTENSION 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P MIDAS 3 EXT3 SAMPLES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIDAS 3 EXT3 SAMPLES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/796/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Farzad amirjavid",
+                "hasEmail": "mailto:farzad.amirjavid@gmail.com"
+            },
+            "description": "Resident of a smart home, who may be an old person or an Alzheimer patient needing permanent assistance, actuates the world by realizing activities, which are observed through the embedded sensors of smart home. Typically, this person may sometimes forget completion of the activities; may realize the activities of daily living incorrectly, and may enter to dangerous states. In order to provide automatic assistance for the smart home resident through the embedded electronically controllable actuators and make the smart home resident able to live independently at home we propose to calculate a possibilistic logical space for correct realization of activities, which may be represented in form of a multivariable problem. Regardless from the physical entity (modality and location) of the intelligence source and the quantity of individuals who perform the activities; per each possible goal or activity, we consider a unique source of intelligence (for example a social mind) who directs the order of fuzzy events that occur in the ambient environment, then the plan behind world actuations is modeled applying extensions of the fuzzy logic. The main key point that we deal with is the analysis of the observations in order to make inferences about possible simultaneous activities that may be planned and realized by one or more individuals; so that we can reason in the cases the parallel activities are interrupted.",
+            "identifier": "DASHLINK_796",
             "issued": "2013-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ames",
                 "dashlink",
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Farzad amirjavid",
-                "hasEmail": "mailto:farzad.amirjavid@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/796/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_796",
-            "description": "Resident of a smart home, who may be an old person or an Alzheimer patient needing permanent assistance, actuates the world by realizing activities, which are observed through the embedded sensors of smart home. Typically, this person may sometimes forget completion of the activities; may realize the activities of daily living incorrectly, and may enter to dangerous states. In order to provide automatic assistance for the smart home resident through the embedded electronically controllable actuators and make the smart home resident able to live independently at home we propose to calculate a possibilistic logical space for correct realization of activities, which may be represented in form of a multivariable problem. Regardless from the physical entity (modality and location) of the intelligence source and the quantity of individuals who perform the activities; per each possible goal or activity, we consider a unique source of intelligence (for example a social mind) who directs the order of fuzzy events that occur in the ambient environment, then the plan behind world actuations is modeled applying extensions of the fuzzy logic. The main key point that we deal with is the analysis of the observations in order to make inferences about possible simultaneous activities that may be planned and realized by one or more individuals; so that we can reason in the cases the parallel activities are interrupted.",
-            "title": "Data driven modeling of the simultaneous activities in ambient environments",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "Data driven modeling of the simultaneous activities in ambient environments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MJCEUOW1H6ON",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Aquarius L3 Gridded 1-Degree Monthly Soil Moisture V005. Version 5. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MJCEUOW1H6ON.",
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
-            "identifier": "C1529467525-NSIDC_ECS",
             "description": "This data set contains Level-3 gridded monthly global soil moisture estimates derived from the NASA Aquarius passive microwave radiometer on the Sat&eacute;lite de Aplicaciones Cient&iacute;ficas (SAC-D).",
-            "title": "Aquarius L3 Gridded 1-Degree Monthly Soil Moisture V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMJCEUOW1H6ON",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMJCEUOW1H6ON",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AQUARIUS/AQ3_MOSM.005/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AQUARIUS/AQ3_MOSM.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_MOSM",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_MOSM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AQ3_MOSM/versions/5/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AQ3_MOSM/versions/5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AQUARIUS/AQ3_MOSM.005/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AQUARIUS/AQ3_MOSM.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_MOSM",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AQ3_MOSM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AQ3_MOSM/versions/5/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AQ3_MOSM/versions/5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MJCEUOW1H6ON",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MJCEUOW1H6ON",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MJCEUOW1H6ON",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MJCEUOW1H6ON",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1529467525-NSIDC_ECS",
+            "issued": "2011-08-25",
+            "keyword": [
+                "land surface",
+                "soils",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MJCEUOW1H6ON",
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
+            "title": "Aquarius L3 Gridded 1-Degree Monthly Soil Moisture V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PWS-2-RDR-SA-4SEC-V1.0",
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
-                "neptune",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 2 Plasma Wave Receiver (PWS) spectrum analyzer obtained in the vicinity of the Neptunian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade.  The time associated with each set of intensities (16 channels) is the time of the beginning of the scan.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pws-2-rdr-sa-4sec-v1.0_nb3a-y29g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "neptune",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PWS-2-RDR-SA-4SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pws-2-rdr-sa-4sec-v1.0_nb3a-y29g",
-            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 2 Plasma Wave Receiver (PWS) spectrum analyzer obtained in the vicinity of the Neptunian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade.  The time associated with each set of intensities (16 channels) is the time of the beginning of the scan.",
-            "title": "VG2 NEP PWS EDITED RDR UNCALIB SPECTRUM ANALYZER 4SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 NEP PWS EDITED RDR UNCALIB SPECTRUM ANALYZER 4SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/338/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-04-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CAROL WIESEMAN",
                 "hasEmail": "mailto:carol.d.wieseman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_338",
             "description": "IGES files\r\nGrids\r\nValidation Data",
-            "title": "RSW - Rectangular Supercritical Wing",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/rswf_w_splitterplate_2.igs",
-                    "description": "IGES file",
                     "@type": "dcat:Distribution",
+                    "description": "IGES file",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/rswf_w_splitterplate_2.igs",
+                    "mediaType": "application/octet-stream",
                     "title": "rswf_w_splitterplate_2.igs"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_338",
+            "issued": "2011-04-01",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/338/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW - Rectangular Supercritical Wing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC4-67PCHURYUMOV-M22-V1.0",
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
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc4-67pchuryumov-m22-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC4-67PCHURYUMOV-M22-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc4-67pchuryumov-m22-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSINAC 3 RDR MTP022 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSINAC 3 RDR MTP022 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1771",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bourgeau-Chavez, L.L., S.E. Grelick, N.H.F. French, D. Tanzer, and E.S. Kane. 2022. ABoVE: Post-Fire and Unburned Vegetation Community and Field Data, NWT, Canada, 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1771",
-            "issued": "2022-06-24",
-            "temporal": "2015-07-13T00:00:00Z/2017-08-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "soils",
-                "natural hazards",
-                "land surface",
-                "human dimensions",
-                "frozen ground",
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
-            "identifier": "C2308231345-ORNL_CLOUD",
             "description": "This dataset provides vegetation community characteristics, soil moisture, and biophysical data collected in 2017 from 11 study sites in the ABoVE Study area. The 11 study areas contained 28 sites that were burned by wildfires in 2014 and 2015, and 10 unburned sites in the Northwest Territories (NWT), Canada. Burned sites included peatland and upland. These field data include assessment of burn severity, vegetation inventories, ground cover, diameter and height for trees and shrubs, seedling and sprouting cover, soil moisture, and depth of unfrozen soil. Plot sizes were 10 m x 10 m with smaller subplots for selected measurements. Similar data were collected for these sites in the years 2015-2019 and are available in related separate datasets. Field data are provided in CSV format. The dataset includes digital photographs (in JPEG format) of vegetation conditions at sampling sites.",
-            "graphic-preview-description": "Researchers collecting data on vegetation and biophysical characteristics at a study site in Northwest Territories of Canada that was burned by wildfires in 2014-2015.",
-            "title": "ABoVE: Post-Fire and Unburned Vegetation Community and Field Data, NWT, Canada, 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_NWT_2017_Field_Data_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1771",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1771",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_NWT_2017_Field_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_NWT_2017_Field_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_NWT_2017_Field_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_NWT_2017_Field_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1771",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1771",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_NWT_2017_Field_Data/comp/ABoVE_NWT_2017_Field_Data.pdf",
-                    "description": "ABoVE: Post-Fire and Unburned Vegetation Community and Field Data, NWT, Canada, 2017: ABoVE_NWT_2017_Field_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Post-Fire and Unburned Vegetation Community and Field Data, NWT, Canada, 2017: ABoVE_NWT_2017_Field_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_NWT_2017_Field_Data/comp/ABoVE_NWT_2017_Field_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_NWT_2017_Field_Data_Fig1.jpg",
-                    "description": "Researchers collecting data on vegetation and biophysical characteristics at a study site in Northwest Territories of Canada that was burned by wildfires in 2014-2015.",
                     "@type": "dcat:Distribution",
+                    "description": "Researchers collecting data on vegetation and biophysical characteristics at a study site in Northwest Territories of Canada that was burned by wildfires in 2014-2015.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_NWT_2017_Field_Data_Fig1.jpg",
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
+            "graphic-preview-description": "Researchers collecting data on vegetation and biophysical characteristics at a study site in Northwest Territories of Canada that was burned by wildfires in 2014-2015.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_NWT_2017_Field_Data_Fig1.jpg",
+            "identifier": "C2308231345-ORNL_CLOUD",
+            "issued": "2022-06-24",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "soils",
+                "natural hazards",
+                "land surface",
+                "human dimensions",
+                "frozen ground",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1771",
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
             "spatial": "-117.38 60.52 -111.37 62.58",
+            "temporal": "2015-07-13T00:00:00Z/2017-08-10T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Post-Fire and Unburned Vegetation Community and Field Data, NWT, Canada, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/860/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-12",
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
-            "identifier": "DASHLINK_860",
             "description": "NASA Ames Research Center\u2019s Sustainability Base is a new\r\n50,000 sq. ft. LEED Platinum office building. Plug loads\r\nare expected to account for a significant portion of the overall\r\nenergy consumption. This is because building design choices\r\nhave resulted in greatly reduced energy demand from Heating,\r\nVentilation, and Air Conditioning (HVAC) and lighting\r\nsystems, which are major contributors to energy consumption\r\nin traditional buildings. In anticipation of the importance of\r\nplug loads in Sustainability Base, a pilot study was conducted\r\nto collect data from a variety of plug loads. A number of cases\r\nof anomalous or unhealthy behavior were observed including\r\nschedule-based rule failures, time-to-standby errors, changed\r\nloads, and inter-channel anomalies. These issues prevent effective\r\nplug load management; therefore, they are important\r\nto promptly identify and correct. The Inductive Monitoring\r\nSystem (IMS) data mining algorithm was chosen to identify\r\nerrors. This paper details how an automated data analysis program\r\nwas created, tested and implemented using IMS. This\r\nprogram will be applied to Sustainability Base to maintain\r\neffective plug load management system performance, identify\r\nmalfunctioning equipment, and reduce building energy\r\nconsumption.",
-            "title": "Application of Inductive Monitoring System to Plug Load Anomaly Detection",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/phmc_12_103.pdf",
-                    "description": "phmc_12_103.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "phmc_12_103.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/phmc_12_103.pdf",
+                    "mediaType": "application/pdf",
                     "title": "phmc_12_103.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_860",
+            "issued": "2013-12-12",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/860/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Application of Inductive Monitoring System to Plug Load Anomaly Detection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-4-EAR2-EARTHSWINGBY2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the EARTH SWING-BY 2 mission phase, covering the period  from 2007-09-13T00:00:00.000 to 2008-01-27T23:59:59.000. The prime target is planet Earth. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-4-ear2-earthswingby2-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "jupiter",
@@ -1128875,302 +1128877,281 @@
                 "earth",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-4-EAR2-EARTHSWINGBY2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-4-ear2-earthswingby2-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the EARTH SWING-BY 2 mission phase, covering the period  from 2007-09-13T00:00:00.000 to 2008-01-27T23:59:59.000. The prime target is planet Earth. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER EARTH OSINAC 4 EAR2 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH OSINAC 4 EAR2 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYDCSR_8.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Aqua Clear Sky Radiance 8-Day Composite Daily L3 Global 25km Equal Area. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MYDCSR_8.061. https://doi.org/10.5067/MODIS/MYDCSR_8.061.",
-            "issued": "2017-10-01",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "ultraviolet wavelengths",
-                "ngda",
-                "national geospatial data asset"
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
-            "identifier": "C1444147198-LAADS",
-            "description": "The MODIS/Aqua Clear Sky Radiance 8-Day Composite Daily L3 Global 25km Equal Area (MYDCSR_8) product is created from composited MYDCSR_D files. Nine clear-sky radiance and reflectance statistics (bands 1-7 and 17-36, see description of the MYDCSR_G product for description of statistics) are produced for day and night separately, for every calendar day from the previous eight days (eight MYDCSR_D files). There must be valid clear-sky data from at least four of the eight days in order to generate a MYDCSR_8 output file. The statistics include observed minus calculated data from bands 20, 22-25, and 27-36 and numbers of land vs. water observations. The data is global in extent at 25-km resolution. MYDCSR_8 files are in  Hierarchical Data Format (HDF).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Clear Sky Radiance 8-Day Composite Daily L3 Global 25km Equal Area",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Clear Sky Radiance 8-Day Composite Daily L3 Global 25km Equal Area (MYDCSR_8) product is created from composited MYDCSR_D files. Nine clear-sky radiance and reflectance statistics (bands 1-7 and 17-36, see description of the MYDCSR_G product for description of statistics) are produced for day and night separately, for every calendar day from the previous eight days (eight MYDCSR_D files). There must be valid clear-sky data from at least four of the eight days in order to generate a MYDCSR_8 output file. The statistics include observed minus calculated data from bands 20, 22-25, and 27-36 and numbers of land vs. water observations. The data is global in extent at 25-km resolution. MYDCSR_8 files are in  Hierarchical Data Format (HDF).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDCSR_8.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDCSR_8.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDCSR_8.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDCSR_8.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDCSR_8--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDCSR_8--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDCSR_8/",
-                    "description": "Direct access to MYDCSR_8 C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MYDCSR_8 C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDCSR_8/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDCSR_8/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDCSR_8/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1444147198-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "ultraviolet wavelengths",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYDCSR_8.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Clear Sky Radiance 8-Day Composite Daily L3 Global 25km Equal Area"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/OMGEV-CTDS1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OMG. 2020-08-24. OMG CTD Conductivity Temperature Depth. Version 1. OMG CTD Conductivity Temperature Depth. NASA/JPL/PODAAC. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/OMGEV-CTDS1. OMG, NASA/JPL/PODAAC, 2020-08-24, OMG Conductivity Temperature Depth (CTD) Profiles, .",
-            "issued": "2020-01-30",
-            "temporal": "2015-07-25T07:17:58Z/2020-08-23T17:57:58Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-30",
-            "keyword": [
-                "oceans",
-                "salinity/density",
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
-            "identifier": "C2491772156-POCLOUD",
-            "description": "This dataset contains in situ measurements from Conductivity Temperature Depth (CTD) casts and tows. It provides salinity, density, temperature and sound velocity of the water column. The CTDs were deployed from a ship either as single profile casts or towed yo-yo behind the ship to measure the physical properties of the water. This provided measurements of the ocean's physical characteristics around Greenland. The CTDs are part of the Oceans Melting Greenland (OMG) project. The goal of the project is to find out what contributions the ocean has on Greenland's melting glaciers.",
-            "release-place": "NASA/JPL/PODAAC",
-            "series-name": "OMG CTD Conductivity Temperature Depth",
-            "graphic-preview-description": "Thumbnail",
             "creator": "OMG",
-            "title": "OMG Conductivity Temperature Depth (CTD) Profiles",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L2_CTD.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains in situ measurements from Conductivity Temperature Depth (CTD) casts and tows. It provides salinity, density, temperature and sound velocity of the water column. The CTDs were deployed from a ship either as single profile casts or towed yo-yo behind the ship to measure the physical properties of the water. This provided measurements of the ocean's physical characteristics around Greenland. The CTDs are part of the Oceans Melting Greenland (OMG) project. The goal of the project is to find out what contributions the ocean has on Greenland's melting glaciers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOMGEV-CTDS1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOMGEV-CTDS1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2015/ORP_OMG_Debrief___Opportunity_2015.pdf",
-                    "description": "2015 ORP Field Report",
                     "@type": "dcat:Distribution",
+                    "description": "2015 ORP Field Report",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2015/ORP_OMG_Debrief___Opportunity_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2016/ORP_2016_ctd_report.pdf",
-                    "description": "2016 ORP Field Report",
                     "@type": "dcat:Distribution",
+                    "description": "2016 ORP Field Report",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2016/ORP_2016_ctd_report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2017/JPL_OMG_Arctic_Access_2017_Overview.pdf",
-                    "description": "2017 Arctic Access / UCI Field Report",
                     "@type": "dcat:Distribution",
+                    "description": "2017 Arctic Access / UCI Field Report",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2017/JPL_OMG_Arctic_Access_2017_Overview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/docs/2016/AXCTD/OMG-AXCTD-2016-Campaign-Field-Report.pdf",
-                    "description": "All field reports from the 2016 OMG campaign",
                     "@type": "dcat:Distribution",
+                    "description": "All field reports from the 2016 OMG campaign",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/docs/2016/AXCTD/OMG-AXCTD-2016-Campaign-Field-Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2015/JPL_OMG_TerraSond_Rev0_Dec_14.pdf",
-                    "description": "2015 Terrasond Field Report",
                     "@type": "dcat:Distribution",
+                    "description": "2015 Terrasond Field Report",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2015/JPL_OMG_TerraSond_Rev0_Dec_14.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2018/ORP_OMG_2018_Report.pdf",
-                    "description": "2018 ORP Field Report",
                     "@type": "dcat:Distribution",
+                    "description": "2018 ORP Field Report",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2018/ORP_OMG_2018_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L2_CTD.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L2_CTD.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/docs/2015/Bathy-CTD-ORP/ORP_OMG_Debrief___Opportunity_2015.pdf",
-                    "description": "All field reports from the 2015 OMG campaign",
                     "@type": "dcat:Distribution",
+                    "description": "All field reports from the 2015 OMG campaign",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/docs/2015/Bathy-CTD-ORP/ORP_OMG_Debrief___Opportunity_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2016/JPL_OMG_Rev0_Nov_2016.pdf",
-                    "description": "2016 Terrasond Field Report",
                     "@type": "dcat:Distribution",
+                    "description": "2016 Terrasond Field Report",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/omg/L2/docs/2016/JPL_OMG_Rev0_Nov_2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/docs/omg-ocean-ctd-users-guide.pdf",
-                    "description": "User guidance documentation for this dataset",
                     "@type": "dcat:Distribution",
+                    "description": "User guidance documentation for this dataset",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/docs/omg-ocean-ctd-users-guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/CTD/CTD/README.txt",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/omg/open/L2/CTD/CTD/README.txt",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772156-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772156-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772156-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772156-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OMG_L2_CTD.jpg",
+            "identifier": "C2491772156-POCLOUD",
+            "issued": "2020-01-30",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/OMGEV-CTDS1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-01-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "NASA/JPL/PODAAC",
+            "series-name": "OMG CTD Conductivity Temperature Depth",
             "spatial": "-74.576 60.351 53.406 79.841",
+            "temporal": "2015-07-25T07:17:58Z/2020-08-23T17:57:58Z",
             "theme": [
                 "OMG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMG Conductivity Temperature Depth (CTD) Profiles"
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
-            "identifier": "NASA-730",
             "description": "RSS",
-            "title": "PDS Odyssey Radio Science Data (73)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1129178,82 +1129159,79 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-730",
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
+            "title": "PDS Odyssey Radio Science Data (73)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-A-ROMAP-2-AST2-SPM-V1.0",
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
-                "21 lutetia"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 2 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the AST2 (Lutetia fly-by) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-a-romap-2-ast2-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "21 lutetia"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-A-ROMAP-2-AST2-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-a-romap-2-ast2-spm-v1.0",
-            "description": "This archive contains level 2 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the AST2 (Lutetia fly-by) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER LUTETIA ROMAP 2 AST2 SPM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER LUTETIA ROMAP 2 AST2 SPM V1.0"
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
-                "flow",
-                "turbulence",
-                "cases",
-                "compressible"
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
-            "identifier": "NASA-843__2",
             "description": "This grouping contains the compressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Compressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1129261,146 +1129239,139 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-843__2",
+            "issued": "2018-06-25",
+            "keyword": [
+                "models",
+                "flow",
+                "turbulence",
+                "cases",
+                "compressible"
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
+            "title": "Collaborative Testing of Turbulence Models: Compressible Flow Cases from 1980-81 Data Library"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1607",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Williamson, C.J., A. Kupc, J.C. Wilson, D.W. Gesler, J.M. Reeves, F. Erdesz, R.J. Mclaughlin, and C.A. Brock. 2018. ATom: Nucleation Mode Aerosol Size Spectrometer Calibration and Performance Data. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1607",
-            "issued": "2018-11-01",
-            "temporal": "2016-10-15T00:00:00Z/2018-01-20T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "aerosols",
-                "air quality",
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
-            "identifier": "C2675810947-ORNL_CLOUD",
             "description": "This dataset provides extensive calibration and in-flight performance data for two nucleation mode aerosol size spectrometer (NMASS) instruments utilized in the NASA Atmospheric Tomography Mission (ATom). Each NMASS has five condensation particle counters (CPCs) that detect particles above a different minimum size, determined by the maximum vapor supersaturation encountered by the particles. Operated in parallel, the CPCs provide continuous concentrations of particles in different cumulative size classes between 3 and 60 nm. Knowing the response function of each CPC, numerical inversion techniques were applied to recover size distributions from the continuous concentrations. Data provided include: NMASS counting efficiencies and diameters of calibration aerosols, inverted particle size distributions; comparisons of NMASS and Scanning Mobility Particle Sizer (SMPS) results; and performance at flows, temperatures, and pressures measured by both NMASSs and comparison with Ultra-High Sensitivity Aerosol Spectrometer (UHSAS) concentrations collected on board the NASA DC-8 aircraft during an ATom flight in February 2017.",
-            "graphic-preview-description": "Schematic of the NMASS layout and flow system (Williamson et al., 2018).",
-            "title": "ATom: Nucleation Mode Aerosol Size Spectrometer Calibration and Performance Data",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_NMASS_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1607",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1607",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_NMASS_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_NMASS_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_NMASS_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_NMASS_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1607",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1607",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_NMASS_Data/comp/ATom_NMASS_Data.pdf",
-                    "description": "ATom: Nucleation Mode Aerosol Size Spectrometer Calibration and Performance Data: ATom_NMASS_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Nucleation Mode Aerosol Size Spectrometer Calibration and Performance Data: ATom_NMASS_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_NMASS_Data/comp/ATom_NMASS_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_NMASS_Data_Fig1.png",
-                    "description": "Schematic of the NMASS layout and flow system (Williamson et al., 2018).",
                     "@type": "dcat:Distribution",
+                    "description": "Schematic of the NMASS layout and flow system (Williamson et al., 2018).",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_NMASS_Data_Fig1.png",
+                    "mediaType": "image/png",
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
+            "graphic-preview-description": "Schematic of the NMASS layout and flow system (Williamson et al., 2018).",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_NMASS_Data_Fig1.png",
+            "identifier": "C2675810947-ORNL_CLOUD",
+            "issued": "2018-11-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "aerosols",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1607",
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
             "spatial": "-180.0 -65.33 180.0 80.52",
+            "temporal": "2016-10-15T00:00:00Z/2018-01-20T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: Nucleation Mode Aerosol Size Spectrometer Calibration and Performance Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/11845",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-08-01",
-            "temporal": "2012-08-01T00:00:00Z/2015-07-01T00:00:00Z",
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
-                "nasa headquarters",
-                "active",
-                "project"
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
-            "identifier": "TECHPORT_11845",
             "description": "&lt;p&gt;\r\n\tImprove the use of land cover data by developing an advanced framework for robust classification using multi-source datasets:&lt;br /&gt;\r\n\tDevelop, validate and optimize a generalized multi-kernel, active learning (MKL-AL) pattern recognition framework for multi-source data fusion.&lt;br /&gt;\r\n\tDevelop both single- and ensemble-classifier versions (MKL-AL and Ensemble-MKL-AL) of the system.&lt;br /&gt;\r\n\tUtilize multi-source remotely sensed and in situ data to create land-cover classification and perform accuracy assessment with available labeled data; utilize first results to query new samples that, if inducted into the training of the system, will significantly improve classification performance and accuracy.&lt;br /&gt;\r\n\t&amp;nbsp;&lt;/p&gt;",
-            "title": "An Advanced Learning Framework for High Dimensional Multi-Sensor Remote Sensing Data Project",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1129408,612 +1129379,650 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "TECHPORT_11845",
+            "issued": "2012-08-01",
+            "keyword": [
+                "nasa headquarters",
+                "active",
+                "project"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/11845",
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
+            "temporal": "2012-08-01T00:00:00Z/2015-07-01T00:00:00Z",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "An Advanced Learning Framework for High Dimensional Multi-Sensor Remote Sensing Data Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/NPOL/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wolff, David  and David A Marks.2016. GPM Ground Validation NASA S-Band Dual Polarimetric (NPOL) Doppler Radar IPHEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/NPOL/DATA101",
-            "issued": "2016-10-18",
-            "temporal": "2014-04-27T18:49:46Z/2014-06-16T11:29:16Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
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
-            "identifier": "C1979638428-GHRC_DAAC",
             "description": "The GPM Ground Validation NASA S-Band Dual Polarimetric (NPOL) Doppler Radar IPHEx dataset was collected during the GPM Ground Validation Integrated Precipitation and Hydrology Experiment (IPHEx) field campaign conducted in South Carolina from April 27, 2014 through June 16, 2014. The NPOL Doppler Radar scanned in high-resolution Plan Position Indicator (PPI), Range-Height Indicator (RHI), and PPI Sector (PPS) scan modes and provided measurements of precipitation in liquid, mixed, and ice phases. Data files are available in tarred universal format (UF) files, and browse images are available in compressed PNG files.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GPM Ground Validation NASA S-Band Dual Polarimetric (NPOL) Doppler Radar IPHEx V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/NPOL/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FNPOL%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FNPOL%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmnpoliphx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmnpoliphx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/iphex/gpmnpoliphx/iphex_npol1_20140607_000402_CZ_sw01_PPI.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/fieldCampaigns/gpmValidation/iphex/gpmnpoliphx/iphex_npol1_20140607_000402_CZ_sw01_PPI.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "http://iowafloodcenter.org/nasa-university-of-iowa-ground-measurement-campaign-to-improve-flood-forecasting/",
-                    "description": "Improving Flood Forecasting",
                     "@type": "dcat:Distribution",
+                    "description": "Improving Flood Forecasting",
+                    "downloadURL": "http://iowafloodcenter.org/nasa-university-of-iowa-ground-measurement-campaign-to-improve-flood-forecasting/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://wallops-prf.gsfc.nasa.gov/Field_Campaigns/IPHEx/",
-                    "description": "Integrated Precipitation Hydrology Experiment (IPHEx)",
                     "@type": "dcat:Distribution",
+                    "description": "Integrated Precipitation Hydrology Experiment (IPHEx)",
+                    "downloadURL": "http://wallops-prf.gsfc.nasa.gov/Field_Campaigns/IPHEx/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/NPOL/doc/gpmnpoliphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/NPOL/doc/gpmnpoliphx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1175/2008BAMS2177.1",
-                    "description": "Potential Role of Dual-Polarization Radar in the Validation of Satellite Precipitation Measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Potential Role of Dual-Polarization Radar in the Validation of Satellite Precipitation Measurements",
+                    "downloadURL": "http://dx.doi.org/10.1175/2008BAMS2177.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
-                    "description": "GHRC IPHEx project web page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRC IPHEx project web page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/NPOL/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/NPOL/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/NPOL/browse/",
+            "identifier": "C1979638428-GHRC_DAAC",
+            "issued": "2016-10-18",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/NPOL/DATA101",
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
             "spatial": "-81.9631 35.1958 -81.9631 35.1958",
+            "temporal": "2014-04-27T18:49:46Z/2014-06-16T11:29:16Z",
             "theme": [
                 "IPHEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation NASA S-Band Dual Polarimetric (NPOL) Doppler Radar IPHEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/PRESW-WAJ10",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.. 2021-02-10. West Atlantic Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/PRESW-WAJ10. Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I. 2021. West Atlantic Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0. PO.DAAC, CA, USA. Dataset accessed[YYYY-MM-DD] at https://doi.org/10.5067/PRESW-WAJ10.",
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
-                "ocean heat budget",
-                "salinity/density",
-                "earth science",
-                "ocean circulation",
-                "ocean temperature",
-                "oceans"
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
-            "identifier": "C2263419126-POCLOUD",
-            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the West Atlantic region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Menemenlis, D., Hill, C., Henze, C. E., Wang, J., & Fenty, I.",
-            "title": "West Atlantic Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_WestAtlantic_v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides a regional multivariate oceanographic state estimate from a global ocean numerical simulation with a focus on the West Atlantic region. The global ocean simulation is based on the MIT general circulation model (MITgcm) with Lat-Lon-Cap grid (LLC) layout and 1/48-degree (2km at equator) nominal horizontal resolution. This simulation is often referred to as LLC4320 in the community and existing publications. The simulation has 90 vertical levels, with about 1-m vertical resolution at the surface and 30 m down to 500 m, for optimized resolution of the upper-ocean processes. The model has zero parameterized horizontal diffusivity. In the vertical direction, the K-Profile Parameterization (KPP) is used for boundary layer turbulent mixing. It is spun up progressively from the lower resolution MITgcm simulation from the Estimating the Circulation & Climate of the Ocean (ECCO), and forced by the 6-hourly ERA-Interim atmosphere reanalysis ( https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-interim ). A synthetic surface pressure field consisting of the 16 most dominant tidal constituents is used to dynamically mimic the tidal forcing. The dataset provides hourly oceanographic variables at native grid. Three-dimensional variables include temperature, salinity, and velocity. Two-dimensional variables include sea level anomaly, ocean mixed layer thickness, bottom pressure anomaly, net freshwater flux, net heat flux, shortwave radiative flux, net salt flux, and ocean surface stress.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-WAJ10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FPRESW-WAJ10",
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
-                    "downloadURL": "https://doi.org/10.5067/PRESW-WAJ10",
-                    "description": "Access the dataset landing page for the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page for the collection",
+                    "downloadURL": "https://doi.org/10.5067/PRESW-WAJ10",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_WestAtlantic_v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_WestAtlantic_v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2263419126-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2263419126-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2263419126-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2263419126-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/Pre-SWOT_LLC4320/preswot_llc4320_user_guide.pdf",
-                    "description": "PRE-SWOT NUMERICAL SIMULATION VERSION 1 USER GUIDE",
                     "@type": "dcat:Distribution",
+                    "description": "PRE-SWOT NUMERICAL SIMULATION VERSION 1 USER GUIDE",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/Pre-SWOT_LLC4320/preswot_llc4320_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/Pre-SWOT_LLC4320/README",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/Pre-SWOT_LLC4320/README",
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
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MITgcm_LLC4320_Pre-SWOT_JPL_L4_WestAtlantic_v1.0.jpg",
+            "identifier": "C2263419126-POCLOUD",
+            "issued": "2021-01-20",
+            "keyword": [
+                "ocean heat budget",
+                "salinity/density",
+                "earth science",
+                "ocean circulation",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/PRESW-WAJ10",
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
             "spatial": "-76.5 32.7 -72.0 38.7",
+            "temporal": "2011-09-13T00:00:00Z/2012-11-15T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "West Atlantic Pre-SWOT Level-4 Hourly MITgcm LLC4320 Native Grid 2km Oceanographic Dataset Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Airborne/Aeolus-CalVal-MetNav_DC8_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-07-29. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Airborne/Aeolus-CalVal-MetNav_DC8_1.",
-            "issued": "2020-07-07",
-            "temporal": "2019-04-17T00:00:00Z/2019-04-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-11",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "altitude",
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
-            "identifier": "C1918229851-LARC_ASDC",
             "description": "Aeolus-CalVal-MetNav_DC8_1 is the Aeolus CalVal Meteorological and Navigational data product. Data was collected using the Global Positioning System (GPS) instrument on the Douglas (DC-8) Aircraft. Data collection for this product is complete. \r\n\r\nNASA conducted an airborne campaign from 17 April to 30 April 2019 to: 1) demonstrate the performance of the Doppler Aerosol WiNd Lidar (DAWN) and High Altitude Lidar Observatory (HALO) instruments across a range of aerosol, cloud, and weather conditions; 2) compare these measurements with the European Space Agency Aeolus mission to gain an initial perspective of Aeolus performance in preparation for a future \r\ninternational Aeolus Cal/Val airborne campaign; and 3) demonstrate how weather processes can be resolved and better understood through simultaneous airborne wind, water vapor (WV), and aerosol profile observations, coupled with numerical model and other remote sensing observations. Five NASA DC-8 aircraft flights, comprising 46 flight hours, were conducted over the Eastern Pacific and Southwest U.S., based out of NASA Armstrong Flight Research Center in Palmdale, CA and Kona, HI. Yankee Environmental Systems, Inc High Definition Sounding System (HDSS) eXpendable Digitial Dropsondes (XDD) were used to validate the DAWN and Aeolus wind observations. The LaRC Diode Laser Hygrometer instrument, which was integrated on the DC-8 in preparation for another NASA airborne campaign, provided in-situ WV measurements used during one flight to validate HALO and dropsonde WV profile products.",
-            "title": "Aeolus CalVal Meteorological and Navigational",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FAeolus-CalVal-MetNav_DC8_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FAeolus-CalVal-MetNav_DC8_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/illuminating-gases-in-the-sky-nasa-technology-pinpoints-potent-greenhouse-gases",
-                    "description": "NASA.gov Article \"Illuminating Gases in the Sky: NASA Technology Pinpoints Potent Greenhouse Gases\" (April 19, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \"Illuminating Gases in the Sky: NASA Technology Pinpoints Potent Greenhouse Gases\" (April 19, 2019)",
+                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/illuminating-gases-in-the-sky-nasa-technology-pinpoints-potent-greenhouse-gases",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-testing-airborne-lasers-to-touch-the-wind",
-                    "description": "NASA Langley Article: \"NASA Testing Airborne Lasers to Touch the Wind\" (April 18, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Langley Article: \"NASA Testing Airborne Lasers to Touch the Wind\" (April 18, 2019)",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-testing-airborne-lasers-to-touch-the-wind",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eoportal.org/web/eoportal/airborne-sensors/halo",
-                    "description": "Earth Observatory Overview of the HALO (High Altitude Lidar Observatory) Instrument",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observatory Overview of the HALO (High Altitude Lidar Observatory) Instrument",
+                    "downloadURL": "https://eoportal.org/web/eoportal/airborne-sensors/halo",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1918229851-LARC_ASDC",
-                    "description": "Earthdata Search for Aeolus-CalVal-MetNav_DC8_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for Aeolus-CalVal-MetNav_DC8_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1918229851-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Airborne/Aeolus-CalVal-MetNav_DC8_1",
-                    "description": "DOI data set landing page for Aeolus-CalVal-MetNav_DC8_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for Aeolus-CalVal-MetNav_DC8_1",
+                    "downloadURL": "https://doi.org/10.5067/Airborne/Aeolus-CalVal-MetNav_DC8_1",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/image-feature/langley/going-where-the-wind-takes-it",
-                    "description": "NASA.gov Article \"Going Where the Wind Takes It\" (March 18, 2019)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \"Going Where the Wind Takes It\" (March 18, 2019)",
+                    "downloadURL": "https://www.nasa.gov/image-feature/langley/going-where-the-wind-takes-it",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/AEOLUS/2019",
-                    "description": "Aeolus Data on the Sub-Orbital Order Tool",
                     "@type": "dcat:Distribution",
+                    "description": "Aeolus Data on the Sub-Orbital Order Tool",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/AEOLUS/2019",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/Aeolus/CalVal-MetNav_DC8_1/",
-                    "description": "ASDC Direct Data Download for Aeolus-CalVal-MetNav_DC8_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for Aeolus-CalVal-MetNav_DC8_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/Aeolus/CalVal-MetNav_DC8_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1918229851-LARC_ASDC",
+            "issued": "2020-07-07",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "altitude",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/Airborne/Aeolus-CalVal-MetNav_DC8_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>5.0 -159.0 5.0 -113.0 52.0 -113.0 52.0 -159.0 5.0 -159.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-04-17T00:00:00Z/2019-04-30T23:59:59.999Z",
             "theme": [
                 "Aeolus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aeolus CalVal Meteorological and Navigational"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/758/",
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
-            "identifier": "DASHLINK_758",
             "description": "Within the area of systems health management, the task of prognostics centers on predicting when components will fail. Model-based prognostics exploits domain knowledge of the system, its components, and how they fail by casting the un- derlying physical phenomena in a physics-based model that is derived from first principles. Uncertainty cannot be avoided in prediction, therefore, algorithms are employed that help in managing these uncertainties. The particle filtering algorithm has become a popular choice for model-based prognostics due to its wide applicability, ease of implementation, and support for uncertainty management. We develop a general model- based prognostics methodology within a robust probabilistic framework using particle filters. As a case study, we consider a pneumatic valve from the Space Shuttle cryogenic refuel- ing system. We develop a detailed physics-based model of the pneumatic valve, and perform comprehensive simulation experiments to illustrate our prognostics approach and evalu- ate its effectiveness and robustness. The approach is demon- strated using historical pneumatic valve data from the refuel- ing system.",
-            "title": "A Model-Based Prognostics Approach Applied to Pneumatic Valves",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_IJPHM_valves.pdf",
-                    "description": "2011_IJPHM_valves.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2011_IJPHM_valves.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_IJPHM_valves.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2011_IJPHM_valves.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_758",
+            "issued": "2013-06-19",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/758/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Model-Based Prognostics Approach Applied to Pneumatic Valves"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-CS2-5-RDR-DEVICO-ATLAS-V1.0",
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
-                "122p/devico 1 (1846 d1)",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Atlas of cometary spectral lines from high resolution measurements of comet deVico.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-cs2-5-rdr-devico-atlas-v1.0_nbut-kq3r",
+            "issued": "2021-05-21",
+            "keyword": [
+                "122p/devico 1 (1846 d1)",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-CS2-5-RDR-DEVICO-ATLAS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-cs2-5-rdr-devico-atlas-v1.0_nbut-kq3r",
-            "description": "Atlas of cometary spectral lines from high resolution measurements of comet deVico.",
-            "title": "HIGH SPECTRAL RESOLUTION ATLAS OF COMET 122P/DEVICO",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "HIGH SPECTRAL RESOLUTION ATLAS OF COMET 122P/DEVICO"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-REX-2-JUPITER-V1.0",
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
-                "jupiter",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons                Radio Science Experiment                                               instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-rex-2-jupiter-v1.0_nbzf-ac5w",
+            "issued": "2018-09-05",
+            "keyword": [
+                "jupiter",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-REX-2-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-rex-2-jupiter-v1.0_nbzf-ac5w",
-            "description": "This data set contains Raw data taken by the New Horizons                Radio Science Experiment                                               instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      REX JUPITER ENCOUNTER                                                   \n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      REX JUPITER ENCOUNTER                                                   \n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1282",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Veraverbeke, S., B.M. Rogers, and J.T. Randerson. 2015. CARVE: Alaskan Fire Emissions Database (AKFED), 2001-2013. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1282",
-            "issued": "2015-09-17",
-            "temporal": "2001-01-01T00:00:00Z/2013-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "human dimensions",
-                "ngda",
-                "natural hazards",
-                "national geospatial data asset",
-                "ecosystems",
-                "ecological dynamics",
-                "earth science",
-                "biosphere",
-                "atmosphere",
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
-            "identifier": "C2236222661-ORNL_CLOUD",
             "description": "This data set provides estimates of annual carbon emissions (kg carbon per square meter) from boreal fires at 450-m resolution for the state of Alaska between 2001 and 2013. To produce these data, daily burned area for 2001 to 2013 was mapped using imagery from the Moderate Resolution Imaging Spectroradiometer (MODIS) combined with perimeters from the Alaska Large Fire Database. Carbon consumption was calibrated using available field measurements from black spruce forests in Alaska. Above- and below-ground carbon consumption were modeled based on environmental variables including elevation, day of burning within the fire season, pre-fire tree cover and the differenced normalized burn ratio (dNBR). Modeled uncertainties in carbon consumption are included in the data set. The derived burn area and carbon emissions product, referred to as the Alaskan Fire Emissions Database (AKFED), provides a resource for study of the environmental controls on daily fire dynamics, boreal fire emissions in biogeochemical models, and potential feedbacks from changing fire regimes.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CARVE: Alaskan Fire Emissions Database (AKFED), 2001-2013",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1282_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1282",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1282",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/carve/AKFED_V1/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/carve/AKFED_V1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/AKFED_V1.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/AKFED_V1.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1282",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1282",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/AKFED_V1/comp/AKFED_V1.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/AKFED_V1/comp/AKFED_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1282_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1282_1_fit.png",
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
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1282",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1282",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1282_1_fit.png",
+            "identifier": "C2236222661-ORNL_CLOUD",
+            "issued": "2015-09-17",
+            "keyword": [
+                "human dimensions",
+                "ngda",
+                "natural hazards",
+                "national geospatial data asset",
+                "ecosystems",
+                "ecological dynamics",
+                "earth science",
+                "biosphere",
+                "atmosphere",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1282",
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
             "spatial": "-168.5 58.0 -141.0 71.5",
+            "temporal": "2001-01-01T00:00:00Z/2013-12-31T23:59:59Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: Alaskan Fire Emissions Database (AKFED), 2001-2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://turbmodels.larc.nasa.gov/Other_exp_Data/cfdval2004_exp.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-07",
-            "references": [
-                "http://turbmodels.larc.nasa.gov/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Christopher Rumsey",
+                "hasEmail": "mailto:c.l.rumsey@nasa.gov"
+            },
+            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_lower_xc_0.9_cm_0.115.dat",
+                    "mediaType": "application/dat"
+                }
             ],
+            "identifier": "NASA-851__12",
+            "issued": "2018-06-25",
             "keyword": [
                 "models",
                 "tangential",
@@ -1130025,302 +1130034,307 @@
                 "experiment",
                 "jets"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Christopher Rumsey",
-                "hasEmail": "mailto:c.l.rumsey@nasa.gov"
-            },
+            "landingPage": "https://turbmodels.larc.nasa.gov/Other_exp_Data/cfdval2004_exp.html",
+            "modified": "2024-08-07",
+            "programCode": [
+                "026:023"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-851__12",
-            "description": "2-D Coanda Airfoil with Tangential Wall Jet. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Coanda/ldv_lower_xc_0.9_cm_0.115.dat",
-                    "mediaType": "application/dat"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments: 2-D Coanda Airfoil with Tangential Wall Jet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=STARDUST-C%2FE%2FL-NC-2-EDR-V1.0",
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
-                "calimg",
-                "stardust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This volume contains the results of the early cruise images of the Stardust Navigation Camera. These images are of no clear scientific or engineering use. They were acquired to ascertain the state of the camera during a time of successive contaminations and decontamination actions, as described in detail below. None are considered useful for calibration of future scientific images, given the nearly continuous changes in the state of the camera during this period.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.stardust-c-e-l-nc-2-edr-v1.0_ncat-vt2f",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calimg",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=STARDUST-C%2FE%2FL-NC-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.stardust-c-e-l-nc-2-edr-v1.0_ncat-vt2f",
-            "description": "This volume contains the results of the early cruise images of the Stardust Navigation Camera. These images are of no clear scientific or engineering use. They were acquired to ascertain the state of the camera during a time of successive contaminations and decontamination actions, as described in detail below. None are considered useful for calibration of future scientific images, given the nearly continuous changes in the state of the camera during this period.",
-            "title": "STARDUST NAVCAM EARLY CRUISE IMAGES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "STARDUST NAVCAM EARLY CRUISE IMAGES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109CMG_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2023-10-10. VIIRS/JPSS1 Surface Reflectance Daily L3 Global 0.05 Deg CMG NRT. Version 2. NASA GSFC LANCE. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ109CMG_NRT.002. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt.",
-            "issued": "2023-10-10",
-            "temporal": "2023-10-10T00:00:00Z/2023-10-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-11",
-            "keyword": [
-                "surface thermal properties",
-                "land surface",
-                "earth science",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LANCEMODIS",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
-            },
-            "identifier": "C2780814625-LANCEMODIS",
-            "description": "The VJ109CMG_NRT is a Near Real Time (NRT) daily surface reflectance Climate Modeling Grid Version 2 product which provides an estimate of land surface reflectance from the NOAA-20 (previously called JPSS1) Visible Infrared Imager Radiometer Suite (VIIRS) sensor. Data are provided for three imagery bands (I1-I3) and nine moderate resolution bands (M1-M5, M7, M8, M10, M11) at 0.05 degree (~5,600 meter) resolution. The data are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. This product uses a weighted average of the best quality observation and is formatted as a CMG for use in climate simulation models. This product includes the twelve reflectance bands, five moderate resolution brightness temperature bands (M12-M16) and information layers representing relative azimuth angle, sensor zenith angle, solar zenith angle, reflectance band quality, time of day, and number mapping.\r\n\r\n\r\nSurface reflectance is obtained by adjusting top-of-atmosphere reflectance to compensate for atmospheric effects. Corrections are made for the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. The inputs to the surface reflectance algorithm include top-of-atmosphere reflectance for the VIIRS visible bands (VJ102MOD, VJ102IMG), the VIIRS cloud mask and aerosol product, aerosol optical thickness, and atmospheric data obtained from a reanalysis (surface pressure, atmospheric precipitable water, and ozone concentration).\r\n\r\n\r\nAll surface reflectance products are produced for daytime conditions only. The product is produced under all atmospheric conditions except for night and oceans. Pixels when not produced are replaced by fill values in the Level-2 and Level-2G products.\r\n\r\n\r\nFor more information read Suomi-NPP VIIRS Surface Reflectance User's Guide at https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf\r\n\r\nor \r\n\r\nvisit VIIRS Land website at https://viirsland.gsfc.nasa.gov/Products/NASA/ReflectanceESDR.html",
-            "release-place": "NASA GSFC LANCE",
             "creator": "LANCEMODIS",
-            "title": "VIIRS/JPSS1 Surface Reflectance Daily L3 Global 0.05 Deg CMG NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VJ109CMG_NRT is a Near Real Time (NRT) daily surface reflectance Climate Modeling Grid Version 2 product which provides an estimate of land surface reflectance from the NOAA-20 (previously called JPSS1) Visible Infrared Imager Radiometer Suite (VIIRS) sensor. Data are provided for three imagery bands (I1-I3) and nine moderate resolution bands (M1-M5, M7, M8, M10, M11) at 0.05 degree (~5,600 meter) resolution. The data are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. This product uses a weighted average of the best quality observation and is formatted as a CMG for use in climate simulation models. This product includes the twelve reflectance bands, five moderate resolution brightness temperature bands (M12-M16) and information layers representing relative azimuth angle, sensor zenith angle, solar zenith angle, reflectance band quality, time of day, and number mapping.\r\n\r\n\r\nSurface reflectance is obtained by adjusting top-of-atmosphere reflectance to compensate for atmospheric effects. Corrections are made for the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. The inputs to the surface reflectance algorithm include top-of-atmosphere reflectance for the VIIRS visible bands (VJ102MOD, VJ102IMG), the VIIRS cloud mask and aerosol product, aerosol optical thickness, and atmospheric data obtained from a reanalysis (surface pressure, atmospheric precipitable water, and ozone concentration).\r\n\r\n\r\nAll surface reflectance products are produced for daytime conditions only. The product is produced under all atmospheric conditions except for night and oceans. Pixels when not produced are replaced by fill values in the Level-2 and Level-2G products.\r\n\r\n\r\nFor more information read Suomi-NPP VIIRS Surface Reflectance User's Guide at https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf\r\n\r\nor \r\n\r\nvisit VIIRS Land website at https://viirsland.gsfc.nasa.gov/Products/NASA/ReflectanceESDR.html",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109CMG_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ109CMG_NRT.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ109CMG_NRT",
-                    "description": "Direct access to the download site and directory hosting the VJ109CMG_NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the VJ109CMG_NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VJ109CMG_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf",
-                    "description": "surface reflectance product's User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "surface reflectance product's User Guide",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/PDF/VIIRS_Surf_Refl_UserGuide_v2.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C2780814625-LANCEMODIS",
+            "issued": "2023-10-10",
+            "keyword": [
+                "surface thermal properties",
+                "land surface",
+                "earth science",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ109CMG_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
+            },
+            "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "2023-10-10T00:00:00Z/2023-10-16T00:00:00Z",
             "theme": [
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Surface Reflectance Daily L3 Global 0.05 Deg CMG NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-2-CVP-RAW-V3.0",
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
+            "description": "This dataset contains EDITED RAW DATA of all three commissioning\nphases CVP1,CVP2,CVP3 and also data of the interference campaign. All\nthese phases together are labeled as Commissioning Phase CVP.\n(Version 3.0 is the first version archived.)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-2-cvp-raw-v3.0_ncc5-f9aj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "checkout",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-2-CVP-RAW-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-2-cvp-raw-v3.0_ncc5-f9aj",
-            "description": "This dataset contains EDITED RAW DATA of all three commissioning\nphases CVP1,CVP2,CVP3 and also data of the interference campaign. All\nthese phases together are labeled as Commissioning Phase CVP.\n(Version 3.0 is the first version archived.)",
-            "title": "ROSETTA-ORBITER CHECK RPCMAG 2 CVP RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCMAG 2 CVP RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/905/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CIES Incorporated",
+                "hasEmail": "mailto:ciescorp221@gmail.com"
+            },
+            "description": "Dataset from the NASA ASRS from Light GA Aircraft - looking for fuel exhaustion fuel starvation fuel gauge engine rough engine stopped",
+            "identifier": "DASHLINK_905",
             "issued": "2014-04-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "ames",
                 "dashlink",
                 "nasa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CIES Incorporated",
-                "hasEmail": "mailto:ciescorp221@gmail.com"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/905/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_905",
-            "description": "Dataset from the NASA ASRS from Light GA Aircraft - looking for fuel exhaustion fuel starvation fuel gauge engine rough engine stopped",
-            "title": "ASRS Fuel Related",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASRS Fuel Related"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ENVISAT/MERIS/L1B/FRS/4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ENVISAT/MERIS/L1B/FRS/4.",
-            "issued": "2022-01-31",
-            "temporal": "2002-03-21T00:00:00Z/2012-05-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-31",
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
-            "identifier": "C1569867387-OB_DAAC",
             "description": "MERIS (Medium Resolution Imaging Spectrometer) is a programmable, medium-spectral resolution, imaging spectrometer operating in the solar reflective spectral range. Fifteen spectral bands can be selected by ground command. The instrument scans the Earth's surface by the so called 'push-broom' method. Linear CCD arrays provide spatial sampling in the across-track direction, while the satellite's motion provides scanning in the along-track direction. MERIS is designed so that it can acquire data over the Earth whenever illumination conditions are suitable. The instrument's 68.5-degree field-of-view around nadir covers a swath width of 1150 km. This wide field of view is shared between five identical optical modules arranged in a fan shape configuration.",
-            "title": "ENVISAT MERIS Full Resolution, Full Swath (FRS) Data, version 4",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FENVISAT%2FMERIS%2FL1B%2FFRS%2F4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FENVISAT%2FMERIS%2FL1B%2FFRS%2F4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MERIS/L1/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/MERIS/L1/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ENVISAT/MERIS/L1B/FRS/4",
-                    "description": "MERIS L1B Full Resolution, Full Swath (FRS) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MERIS L1B Full Resolution, Full Swath (FRS) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ENVISAT/MERIS/L1B/FRS/4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1569867387-OB_DAAC",
+            "issued": "2022-01-31",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ENVISAT/MERIS/L1B/FRS/4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-03-21T00:00:00Z/2012-05-09T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ENVISAT MERIS Full Resolution, Full Swath (FRS) Data, version 4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/nchm-qejz",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Using diamagnetic levitation we have exposed A. thaliana in vitro callus cultures to five environments with different levels of effective gravity (from levitation i.e. simulated mg* to 2g*) and magnetic fields (10.1 to 16.5 Tesla) and we have compared the results with those of similar experiments done in a Random Position Machine (simulated micro g) and a Large Diameter Centrifuge (2g) free of high magnetic fields. Microarray analysis indicates that there are changes in overall gene expression of the cultured cells exposed to these unusual environments but also that gravitational and magnetic field produce synergic variations in the steady state of the transcriptional profile of A. thaliana. Significant changes in the expression of structural abiotic stress and secondary metabolism genes were observed into the magnet field. These results confirm that the strong magnetic field both at micro g* or 2g* has a significant effect on the expression of these genes but subtle gravitational effects are still observable. These subtle responses to microgravity environments are opposite to the ones observed in a hypergravity one. seven-condition experiment MM2D Arabidopsis culture callus control vs. Treatment (altered gravity simulation GBF). Three GBF were used (LDC (2g) + control RPM (mg) + control and Magnet (mg* 0.1g* 1g* 1.9g* 2g*) + control). Biological replicates: 3 replicates in all conditions and controls except 1.9g* (2 replicates)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-8",
+                    "mediaType": "text/html",
+                    "title": "An environment with strong gravitational and magnetic field alterations synergizes to promote variations in Arabidopsis thaliana callus global transcriptional state"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-8_nchm-qejz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse29787-4",
                 "hybridization",
@@ -1130341,146 +1130355,110 @@
                 "p-gse29787-6",
                 "grow"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/nchm-qejz",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-8_nchm-qejz",
-            "description": "Using diamagnetic levitation we have exposed A. thaliana in vitro callus cultures to five environments with different levels of effective gravity (from levitation i.e. simulated mg* to 2g*) and magnetic fields (10.1 to 16.5 Tesla) and we have compared the results with those of similar experiments done in a Random Position Machine (simulated micro g) and a Large Diameter Centrifuge (2g) free of high magnetic fields. Microarray analysis indicates that there are changes in overall gene expression of the cultured cells exposed to these unusual environments but also that gravitational and magnetic field produce synergic variations in the steady state of the transcriptional profile of A. thaliana. Significant changes in the expression of structural abiotic stress and secondary metabolism genes were observed into the magnet field. These results confirm that the strong magnetic field both at micro g* or 2g* has a significant effect on the expression of these genes but subtle gravitational effects are still observable. These subtle responses to microgravity environments are opposite to the ones observed in a hypergravity one. seven-condition experiment MM2D Arabidopsis culture callus control vs. Treatment (altered gravity simulation GBF). Three GBF were used (LDC (2g) + control RPM (mg) + control and Magnet (mg* 0.1g* 1g* 1.9g* 2g*) + control). Biological replicates: 3 replicates in all conditions and controls except 1.9g* (2 replicates)",
-            "title": "An environment with strong gravitational and magnetic field alterations synergizes to promote variations in Arabidopsis thaliana callus global transcriptional state",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-8",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "An environment with strong gravitational and magnetic field alterations synergizes to promote variations in Arabidopsis thaliana callus global transcriptional state"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "An environment with strong gravitational and magnetic field alterations synergizes to promote variations in Arabidopsis thaliana callus global transcriptional state"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-15MIN",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "THIS DATA SET CONSISTS OF RESAMPLED DATA FROM THE LOW ENERGY CHARGED PARTICLE (LECP) EXPERIMENT ON VOYAGER 2 WHILE THE SPACECRAFT WAS IN THE VICINITY OF JUPITER. THIS INSTRUMENT MEASURES THE INTENSITIES OF IN-SITU CHARGED PARTICLES (>26 KEV ELECTRONS AND >30 KEV IONS) WITH VARIOUS LEVELS OF DISCRIMINATION BASED ON ENERGY, MASS SPECIES, AND ANGULAR ARRIVAL DIRECTION. A SUBSET OF ALMOST 100 LECP CHANNELS ARE INCLUDED WITH THIS DATA SET. THE LECP DATA ARE GLOBALLY CALIBRATED TO THE EXTENT POSSIBLE (SEE BELOW) AND THEY ARE TIME AVERAGED TO ABOUT 15 MINUTE TIME INTERVALS WITH THE EXACT BEGINNING AND ENDING TIMES FOR THOSE INTERVALS MATCHING THE LECP INSTRUMENTAL CYCLE PERIODS (THE ANGULAR SCANNING PERIODS). THE LECP INSTUMENT HAS A ROTATING HEAD FOR OBTAINING ANGULAR ANISOTROPY MEASUREMENTS OF THE MEDIUM ENERGY CHARGED PARTICLES THAT IT MEASURES. THE CYCLE TIME FOR THE ROTATION IF VARIABLE, BUT DURING ENCOUNTERS IT IS ALWAYS FASTER THAN 15 MINUTES. THUS, THE FULL ANGULAR ANISOTROPY INFORMATION IS PRESERVED WITH THIS DATA. THE DATA IS IN THE FORM OF 'RATE' DATA WHICH HAS NOT BEEN CONVERTED TO THE USUAL PHYSICAL UNITS. THE REASON IS THAT SUCH A CONVERSION WOULD DEPEND ON UNCERTAIN DETERMINATIONS SUCH AS THE MASS SPECIES OF THE PARTICLES AND THE LEVEL OF BACKGROUND. BOTH MASS SPECIES AND BACKGROUND ARE GENERALLY DETERMINED FROM CONTEXT DURING THE STUDY OF PARTICULAR REGIONS. TO CONVERT 'RATE' TO 'INTENSITY' FOR A PARTICULAR CHANNEL ONE PERFORMS THE FOLLOWING TASKS: 1) DECIDE ON THE LEVEL OF BACKGROUND CONTAMINATION AND SUBTRACT THAT OFF THE GIVEN RATE LEVEL. BACKGROUND IS TO BE DETERMINED FROM CONTEXT AND FROM MAKING USE OF SECTOR 8 RATES (SECTOR 8 HAS A 2 mm AL SHIELD COVERING IT). 2) DIVIDE THE BACKGROUND CORRECTED RATE BY THE CHANNEL GEOMETRIC FACTOR AND BY THE ENERGY BANDPASS OF THE CHANNEL. THE GEOMETRIC FACTOR IS FOUND IN ENTRY 'channel_geometric_ factor' AS ASSOCIATED WITH EACH CHANNEL 'channel_id'. TO DETERMINE THE ENERGY BANDPASS, ONE MUST JUDGE THE MASS SPECIES OF THE OF THE DETECTED PARTICLES (FOR IONS BUT NOT FOR ELECTRONS). THE ENERGY BAND PASSES ARE GIVEN IN ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPENERGY', AND ARE GIVEN IN THE FORM 'ENERGY/NUCLEON'. FOR CHANNELS THAT BEGIN THEIR NAMES WITH THE DESIGNATIONS 'CH' THESE BANDPASSES CAN BE USED ON MASS SPECIES THAT ARE ACCEPTED INTO THAT CHANNEL (SEE ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPCHANZ', WHICH GIVE THE MINIMUM AND MAXIMUM 'Z' VALUE ACCEPTED -- THESE ENTRIES ARE BLANK FOR ELECTRON CHANNELS). FOR OTHER CHANNELS THE GIVEN BANDPASS REFERS ONLY TO THE LOWEST 'Z' VALUE ACCEPTED. THE BANDPASSES FOR OTHER 'Z' VALUES ARE NOT ALL KNOWN, BUT SOME ARE GIVEN IN THE LITERATURE (E.G. KRIMIGIS ET AL., 1979). THE FINAL PRODUCT OF THESE INSTRUCTIONS WILL BE THE PARTICLE INTENSITY WITH THE UNITS: COUNTS/(CM**2.STR.SEC.KEV). SOME CHANNELS ARE SUBJECT TO SERIOUS CONTAMINATIONS, AND MANY OF THESE CONTAMINATIONS CANNOT BE REMOVED EXCEPT WITH A REGION-BY-REGION ANALYSIS, WHICH HAS NOT BEEN DONE FOR THIS DATA. THUS, TO USE THIS DATA IT IS ABSOLUTELY VITAL THAT THE CONTAMINATION TYPES ('contamination_id' , 'contamination_desc') AND THE LEVELS OF CONTAMINATION ('data_quality_id' CORRESPONDING TO THE DEFINITIONS 'data_quality_desc') BE CAREFULLY EXAMINED FOR ALL REGIONS OF STUDY. A DEAD TIME CORRECTION PROCEDURE HAS BEEN APPLIED IN AN ATTEMPT TO CORRECT THE LINEAR EFFECTS OF DETECTOR OVERDRIVE (PULSE-PILEUP). THIS PROCEDURE DOES NOT FIX SEVERELY OVERDRIVEN DETECTORS. A PROCEDURE IS AVAILABLE FOR CORRECTING VOYAGER 2 LECP ELECTRON CONTAMINATION OF LOW ENERGY ION CHANNELS, BUT ITS EFFECTIVENESS HAS BEEN EVALUATED ONLY FOR THE URANUS DATA SET. THUS, CORRECTIONS HAVE BEEN APPLIED ONLY TO THE URANUS DATA SET. Also included with this data are one standard deviation statistical uncertainties for the directional data (sectors 1 through 8) expressed as a percent. Unknown values are generally coded as s",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-15min_ncj6-ziv7",
             "issued": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-15MIN",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-15min_ncj6-ziv7",
-            "description": "THIS DATA SET CONSISTS OF RESAMPLED DATA FROM THE LOW ENERGY CHARGED PARTICLE (LECP) EXPERIMENT ON VOYAGER 2 WHILE THE SPACECRAFT WAS IN THE VICINITY OF JUPITER. THIS INSTRUMENT MEASURES THE INTENSITIES OF IN-SITU CHARGED PARTICLES (>26 KEV ELECTRONS AND >30 KEV IONS) WITH VARIOUS LEVELS OF DISCRIMINATION BASED ON ENERGY, MASS SPECIES, AND ANGULAR ARRIVAL DIRECTION. A SUBSET OF ALMOST 100 LECP CHANNELS ARE INCLUDED WITH THIS DATA SET. THE LECP DATA ARE GLOBALLY CALIBRATED TO THE EXTENT POSSIBLE (SEE BELOW) AND THEY ARE TIME AVERAGED TO ABOUT 15 MINUTE TIME INTERVALS WITH THE EXACT BEGINNING AND ENDING TIMES FOR THOSE INTERVALS MATCHING THE LECP INSTRUMENTAL CYCLE PERIODS (THE ANGULAR SCANNING PERIODS). THE LECP INSTUMENT HAS A ROTATING HEAD FOR OBTAINING ANGULAR ANISOTROPY MEASUREMENTS OF THE MEDIUM ENERGY CHARGED PARTICLES THAT IT MEASURES. THE CYCLE TIME FOR THE ROTATION IF VARIABLE, BUT DURING ENCOUNTERS IT IS ALWAYS FASTER THAN 15 MINUTES. THUS, THE FULL ANGULAR ANISOTROPY INFORMATION IS PRESERVED WITH THIS DATA. THE DATA IS IN THE FORM OF 'RATE' DATA WHICH HAS NOT BEEN CONVERTED TO THE USUAL PHYSICAL UNITS. THE REASON IS THAT SUCH A CONVERSION WOULD DEPEND ON UNCERTAIN DETERMINATIONS SUCH AS THE MASS SPECIES OF THE PARTICLES AND THE LEVEL OF BACKGROUND. BOTH MASS SPECIES AND BACKGROUND ARE GENERALLY DETERMINED FROM CONTEXT DURING THE STUDY OF PARTICULAR REGIONS. TO CONVERT 'RATE' TO 'INTENSITY' FOR A PARTICULAR CHANNEL ONE PERFORMS THE FOLLOWING TASKS: 1) DECIDE ON THE LEVEL OF BACKGROUND CONTAMINATION AND SUBTRACT THAT OFF THE GIVEN RATE LEVEL. BACKGROUND IS TO BE DETERMINED FROM CONTEXT AND FROM MAKING USE OF SECTOR 8 RATES (SECTOR 8 HAS A 2 mm AL SHIELD COVERING IT). 2) DIVIDE THE BACKGROUND CORRECTED RATE BY THE CHANNEL GEOMETRIC FACTOR AND BY THE ENERGY BANDPASS OF THE CHANNEL. THE GEOMETRIC FACTOR IS FOUND IN ENTRY 'channel_geometric_ factor' AS ASSOCIATED WITH EACH CHANNEL 'channel_id'. TO DETERMINE THE ENERGY BANDPASS, ONE MUST JUDGE THE MASS SPECIES OF THE OF THE DETECTED PARTICLES (FOR IONS BUT NOT FOR ELECTRONS). THE ENERGY BAND PASSES ARE GIVEN IN ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPENERGY', AND ARE GIVEN IN THE FORM 'ENERGY/NUCLEON'. FOR CHANNELS THAT BEGIN THEIR NAMES WITH THE DESIGNATIONS 'CH' THESE BANDPASSES CAN BE USED ON MASS SPECIES THAT ARE ACCEPTED INTO THAT CHANNEL (SEE ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPCHANZ', WHICH GIVE THE MINIMUM AND MAXIMUM 'Z' VALUE ACCEPTED -- THESE ENTRIES ARE BLANK FOR ELECTRON CHANNELS). FOR OTHER CHANNELS THE GIVEN BANDPASS REFERS ONLY TO THE LOWEST 'Z' VALUE ACCEPTED. THE BANDPASSES FOR OTHER 'Z' VALUES ARE NOT ALL KNOWN, BUT SOME ARE GIVEN IN THE LITERATURE (E.G. KRIMIGIS ET AL., 1979). THE FINAL PRODUCT OF THESE INSTRUCTIONS WILL BE THE PARTICLE INTENSITY WITH THE UNITS: COUNTS/(CM**2.STR.SEC.KEV). SOME CHANNELS ARE SUBJECT TO SERIOUS CONTAMINATIONS, AND MANY OF THESE CONTAMINATIONS CANNOT BE REMOVED EXCEPT WITH A REGION-BY-REGION ANALYSIS, WHICH HAS NOT BEEN DONE FOR THIS DATA. THUS, TO USE THIS DATA IT IS ABSOLUTELY VITAL THAT THE CONTAMINATION TYPES ('contamination_id' , 'contamination_desc') AND THE LEVELS OF CONTAMINATION ('data_quality_id' CORRESPONDING TO THE DEFINITIONS 'data_quality_desc') BE CAREFULLY EXAMINED FOR ALL REGIONS OF STUDY. A DEAD TIME CORRECTION PROCEDURE HAS BEEN APPLIED IN AN ATTEMPT TO CORRECT THE LINEAR EFFECTS OF DETECTOR OVERDRIVE (PULSE-PILEUP). THIS PROCEDURE DOES NOT FIX SEVERELY OVERDRIVEN DETECTORS. A PROCEDURE IS AVAILABLE FOR CORRECTING VOYAGER 2 LECP ELECTRON CONTAMINATION OF LOW ENERGY ION CHANNELS, BUT ITS EFFECTIVENESS HAS BEEN EVALUATED ONLY FOR THE URANUS DATA SET. THUS, CORRECTIONS HAVE BEEN APPLIED ONLY TO THE URANUS DATA SET. Also included with this data are one standard deviation statistical uncertainties for the directional data (sectors 1 through 8) expressed as a percent. Unknown values are generally coded as s",
-            "title": "VOYAGER 2 JUP LOW ENERGY CHARGED PARTICLE CALIB. 15MIN",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 2 JUP LOW ENERGY CHARGED PARTICLE CALIB. 15MIN"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-CAL-ITS-2-9P-CRUISE-V1.0",
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
+            "description": "This data set contains raw science calibration images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the cruise phase of the mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-cal-its-2-9p-cruise-v1.0_nckj-pipa",
+            "issued": "2018-06-26",
+            "keyword": [
+                "deep impact",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DII-CAL-ITS-2-9P-CRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dii-cal-its-2-9p-cruise-v1.0_nckj-pipa",
-            "description": "This data set contains raw science calibration images acquired by the Deep Impact Impactor Targeting Sensor Visible CCD during the cruise phase of the mission.",
-            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW ITS CALIB DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW ITS CALIB DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114213-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. TOMSN7L3daer. Version 008. TOMS Nimbus-7 UV Aerosol Index Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSN7L3daer_008.html. Digital Science Data.",
-            "issued": "2004-04-30",
-            "temporal": "1978-11-01T00:00:00Z/1993-05-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PAWAN BHARTIA, PH. D",
                 "hasEmail": "mailto:Pawan.K.Bhartia@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1237114213-GES_DISC",
-            "description": "This Nimbus-7 Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains UV aerosol index values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TOMSN7L3daer",
             "creator": "TOMS Science Team",
-            "title": "TOMS Nimbus-7 UV Aerosol Index Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3daer) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSN7L3daer_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This Nimbus-7 Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains UV aerosol index values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1130489,506 +1130467,506 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSN7L3daer_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSN7L3daer_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_TOMS_Level3/TOMSN7L3daer.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_TOMS_Level3/TOMSN7L3daer.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSN7L3daer",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSN7L3daer",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/NIMBUS7_USERGUIDE.PDF",
-                    "description": "Nimbus-7 TOMS Data Product User's Guide.",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus-7 TOMS Data Product User's Guide.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/NIMBUS7_USERGUIDE.PDF",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/v8toms_atbd.pdf",
-                    "description": "TOMS V8 ATBD document.",
                     "@type": "dcat:Distribution",
+                    "description": "TOMS V8 ATBD document.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/v8toms_atbd.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=TOMS+Mission+Preservation+Documents",
-                    "description": "Documentation related to legacy TOMS mission.",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation related to legacy TOMS mission.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=TOMS+Mission+Preservation+Documents",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSN7L3daer_008.png",
+            "identifier": "C1237114213-GES_DISC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114213-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-04-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "TOMSN7L3daer",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-11-01T00:00:00Z/1993-05-06T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Nimbus-7 UV Aerosol Index Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSN7L3daer) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43A1N.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-09-16. MODIS/Terra Aqua BRDF/Albedo Model Parameters Daily L3 Global 500 m SIN Grid. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MCD43A1N.NRT.061.",
-            "issued": "2021-09-10",
-            "temporal": "2021-09-15T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-11",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "surface radiative properties",
-                "ngda",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LANCE USER SUPPORT TEAM",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
-            },
-            "identifier": "C2128952410-LANCEMODIS",
             "description": "The MODIS Near Real Time (NRT) MCD43A1N, MODIS Combined Aqua and Terra Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Model Parameters is produced daily using 16 days of Terra and Aqua MODIS data. This global gridded tiled product provides model parameters/coefficients (isotropic, volume and surface) for characterizing the BRDF of each pixel at 500m resolution in the sinusoidal map projection. BRDF at each pixel for the current day is derived by inverting all available good quality corrected surface reflectance observations acquired by Terra and Aqua MODIS from the 16-day period ending with the current data day. The daily observation are weighed as a function of quality, observation coverage and temporal distance from the current data date. Model parameters are stored as 3D datasets for each of the 7 land bands, visible, near-infrared and shortwave bands along with corresponding mandatory QA flags.\r\nThere is a significant change in the science algorithm of the Collection 61 (C61) NRT BRDF/Albedo products and, therefore significant differences/discontinuities between the C6 and C61 products.  C61 algorithm changes are intended to minimize the differences between the NRT and Standard BRDF. The C61 NRT BRDF code has been modified to allow for an extra round of magnitude inversion, following a full inversion using the full set of inputs. This extra magnitude inversion will only use the set of 9 days that are overlapping between standard and NRT, with the highest weight being assigned to the last day.\r\n\r\nAdditional information at MODIS Land Science Team website at https://modis-land.gsfc.nasa.gov/brdf.html",
-            "release-place": "MODAPS at NASA/GSFC",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Model Parameters Daily L3 Global 500 m SIN Grid",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43A1N.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43A1N.NRT.061",
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
-                    "description": "Access Collection 6 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MCD43A1N",
-                    "description": "Direct access to the download site and directory hosting the MCD43A1N 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MCD43A1N 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MCD43A1N",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2128952410-LANCEMODIS",
+            "issued": "2021-09-10",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43A1N.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-02-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-09-15T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Aqua",
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Model Parameters Daily L3 Global 500 m SIN Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-EXT2-V2.0",
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
+            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the ROSETTA EXTENSION 2 mission phase. The primary target was comet 67P/C-G. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6. This is V2.0 updated after Science Review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-ext2-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-EXT2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-ext2-v2.0",
-            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the ROSETTA EXTENSION 2 mission phase. The primary target was comet 67P/C-G. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6. This is V2.0 updated after Science Review.",
-            "title": "ROSETTA-ORBITER 67P RPCMIP 3 EXT2 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMIP 3 EXT2 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V1.0",
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
-                "new horizons",
-                "dust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v1.0_ncri-6hbw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-3-PLUTO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-3-pluto-v1.0_ncri-6hbw",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GBMBES47TUOI",
             "citation": "Kevin W. Bowman. 2023-04-11. TRPSYL2ALLCRSMGBEI. Version 1. TROPESS CrIS-SNPP L2 for Beijing Megacity, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GBMBES47TUOI. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGBEI_1.html. Digital Science Data.",
-            "issued": "2022-12-22",
-            "temporal": "2016-01-02T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-22",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
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
-            "identifier": "C2569844139-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Beijing Megacity, Summary Product contains the vertical distribution of six retrieved atmospheric gases (CH4, CO, HDO, NH3, O3 and PAN), along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream summary product is centered on a 3x3 degree region over Beijing for the time period from 2021-02-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2ALLCRSMGBEI",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Beijing Megacity (Forward Stream, Summary Product) CO column on 01 July 2020.",
-            "title": "TROPESS CrIS-SNPP L2 for Beijing Megacity, Summary Product V1 (TRPSYL2ALLCRSMGBEI) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGBEI_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGBMBES47TUOI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGBMBES47TUOI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGBEI_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Beijing Megacity (Forward Stream, Summary Product) CO column on 01 July 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Beijing Megacity (Forward Stream, Summary Product) CO column on 01 July 2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGBEI_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGBEI_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGBEI_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGBEI.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGBEI.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2ALLCRSMGBEI_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2ALLCRSMGBEI_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGBEI.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGBEI.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGBEI.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGBEI.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Beijing Megacity (Forward Stream, Summary Product) CO column on 01 July 2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGBEI_Sample.png",
+            "identifier": "C2569844139-GES_DISC",
+            "issued": "2022-12-22",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GBMBES47TUOI",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-22",
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
+            "series-name": "TRPSYL2ALLCRSMGBEI",
             "spatial": "115.0 38.0 118.0 41.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Beijing Megacity, Summary Product V1 (TRPSYL2ALLCRSMGBEI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-PIXC-1.1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-11-30. SWOT Level 2 Water Mask Pixel Cloud Data Product. Version 1.1. SWOT Level 2 Water Mask Pixel Cloud Data Product, Version 1.1. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-PIXC-1.1. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-07-20",
-            "temporal": "2022-12-16T00:00:00Z/2023-12-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-20",
-            "keyword": [
-                "earth science",
-                "sea surface topography",
-                "oceans",
-                "ocean waves"
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
-            "identifier": "C2758162620-POCLOUD",
-            "description": "Point cloud of water mask pixels (\u201cpixel cloud\u201d) with geolocated heights, backscatter, geophysical fields, and flags. Point cloud over tile (approx 64x64 km2); half swath (left or right side of full swath). Available in netCDF-4 file format.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 Water Mask Pixel Cloud Data Product",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Water Mask Pixel Cloud Data Product, Version 1.1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_DEFAULT_THUMBNAIL.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Point cloud of water mask pixels (\u201cpixel cloud\u201d) with geolocated heights, backscatter, geophysical fields, and flags. Point cloud over tile (approx 64x64 km2); half swath (left or right side of full swath). Available in netCDF-4 file format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-PIXC-1.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-PIXC-1.1",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2758162620-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2758162620-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2758162620-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2758162620-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_DEFAULT_THUMBNAIL.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_DEFAULT_THUMBNAIL.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56411_SWOT_Product_Description_L2_HR_PIXC_20220727b_RevA.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/D-56411_SWOT_Product_Description_L2_HR_PIXC_20220727b_RevA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_DEFAULT_THUMBNAIL.jpg",
+            "identifier": "C2758162620-POCLOUD",
+            "issued": "2022-07-20",
+            "keyword": [
+                "earth science",
+                "sea surface topography",
+                "oceans",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-PIXC-1.1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Jet Propulsion Laboratory",
+            "series-name": "SWOT Level 2 Water Mask Pixel Cloud Data Product",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2023-12-04T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Water Mask Pixel Cloud Data Product, Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-3lcdqiv",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)/Netherlands Institute for Space Research (SRON). 2021-07-05. S5P_L2__CH4____HiR. Version 2. Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 5.5km x 7km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-3lcdqiv. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____HiR_2.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2021-07-01T18:44:53Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jochen Landgraf",
                 "hasEmail": "mailto:j.landgraf@sron.nl"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2087216530-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__CH4____1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe retrieval algorithm for Sentinel-5P TROPOMI methane product is a physics based method that uses the Oxygen-A band (760 nm) and absorption bands in shortwave infrared spectrum. In Sentinel-5P/TROPOMI methane algorithm, the atmosphere forward model simulates the absorbing gas (oxygen, methane, water vapor, and carbon monoxide) optical properties, as well as aerosol optical properties with size distribution, refractive index, and number concentration. The inversion is performed based on the forward calculation, the measurement, and the prior information. Cloud filtering is critical in methane retrieval, S5P methane algorithm applies re-gridded Visible Infrared Imaging Radiometer Suite (VIIRS) cloud mask data. Additional cloud filters based on S5P/TROPOMI measurements and the FRESCO apparent surface pressure will be applied when VIIRS cloud data are not available. Other current data filters in the retrieval algorithm include land-only pixels (excluding mountainous areas), spectrum intensity, solar zenith angle and instrument zenith angle. \n\nThe S5P/TROPOMI methane retrieval is for non-time-critical (NTC) data stream only, and its main outputs include the column averaged dry air mixing ratio of methane, the random error, and the biased corrected dry air methane fraction data based on the retrieved surface albedo. \n\nStarting from orbit #12432 on March 7th of 2020, the S-NPP auxiliary cloud data source used in the methane product data processing has been transitioned from the VIIRS Cloud Mask (VCM) into the Enterprise Cloud Mask (ECM).\n\nThe data are stored in an enhanced netCDF-4 format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__CH4____HiR",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)/Netherlands Institute for Space Research (SRON)",
-            "title": "Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 5.5km x 7km V2 (S5P_L2__CH4____HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__CH4____HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__CH4____1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe retrieval algorithm for Sentinel-5P TROPOMI methane product is a physics based method that uses the Oxygen-A band (760 nm) and absorption bands in shortwave infrared spectrum. In Sentinel-5P/TROPOMI methane algorithm, the atmosphere forward model simulates the absorbing gas (oxygen, methane, water vapor, and carbon monoxide) optical properties, as well as aerosol optical properties with size distribution, refractive index, and number concentration. The inversion is performed based on the forward calculation, the measurement, and the prior information. Cloud filtering is critical in methane retrieval, S5P methane algorithm applies re-gridded Visible Infrared Imaging Radiometer Suite (VIIRS) cloud mask data. Additional cloud filters based on S5P/TROPOMI measurements and the FRESCO apparent surface pressure will be applied when VIIRS cloud data are not available. Other current data filters in the retrieval algorithm include land-only pixels (excluding mountainous areas), spectrum intensity, solar zenith angle and instrument zenith angle. \n\nThe S5P/TROPOMI methane retrieval is for non-time-critical (NTC) data stream only, and its main outputs include the column averaged dry air mixing ratio of methane, the random error, and the biased corrected dry air methane fraction data based on the retrieved surface albedo. \n\nStarting from orbit #12432 on March 7th of 2020, the S-NPP auxiliary cloud data source used in the methane product data processing has been transitioned from the VIIRS Cloud Mask (VCM) into the Enterprise Cloud Mask (ECM).\n\nThe data are stored in an enhanced netCDF-4 format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-3lcdqiv",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-3lcdqiv",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1130998,112 +1130976,112 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____HiR_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____HiR_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__CH4____HiR.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__CH4____HiR.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__CH4____HiR.2",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__CH4____HiR.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Methane-Product-Readme-File",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Methane-Product-Readme-File",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__CH4____HiR_2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__CH4____HiR_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-Methane-retrieval",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-Methane-retrieval",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Methane",
-                    "description": "Product User Manual Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Methane",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/web/sentinel/missions/sentinel-5p",
-                    "description": "ESA Copernicus Sentinel 5P Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ESA Copernicus Sentinel 5P Home Page",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__CH4____HiR_1.png",
+            "identifier": "C2087216530-GES_DISC",
+            "issued": "2017-05-05",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5270/S5P-3lcdqiv",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-05-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "S5P_L2__CH4____HiR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-07-01T18:44:53Z/2023-02-28T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 5.5km x 7km V2 (S5P_L2__CH4____HiR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mgs-configs",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/mgs/index.html"
-            ],
-            "keyword": [
-                "mars global surveyor",
-                "satellite",
-                "3d model",
-                "orbiter",
-                "vehicles"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brian Kumanchik",
                 "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-380",
             "description": "Model of the Mars Global Surveyor spacecraft. Polygons: 19314 Vertices: 10250",
-            "title": "NASA 3D Models: Mars Global Surveyor Config",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1131111,89 +1131089,89 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-380",
+            "issued": "2018-06-25",
+            "keyword": [
+                "mars global surveyor",
+                "satellite",
+                "3d model",
+                "orbiter",
+                "vehicles"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/mgs-configs",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/mgs/index.html"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: Mars Global Surveyor Config"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V5.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Names, designations, and discovery circumstances for the numbered asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v5.0_ncw6-vjvf",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V5.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v5.0_ncw6-vjvf",
-            "description": "Names, designations, and discovery circumstances for the numbered asteroids.",
-            "title": "ASTEROID NAMES AND DISCOVERY V5.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID NAMES AND DISCOVERY V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AI7QGND2FX1H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO Science Team/Michael Gunson, AnnmarieEldering. 2024-04-10. OCO3_L2_IMAPDOAS. Version 11r. OCO-3 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Retrospective Processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/AI7QGND2FX1H. https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_IMAPDOAS_11r.html. Digital Science Data.",
-            "issued": "2021-05-31",
-            "temporal": "2019-08-06T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-31",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
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
-            "identifier": "C2910089793-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO3_L2_IMAPDOAS",
             "creator": "OCO Science Team/Michael Gunson, AnnmarieEldering",
-            "title": "OCO-3 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Retrospective Processing V11r (OCO3_L2_IMAPDOAS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory -3 (OCO-3) was deployed to the International Space Station in May, 2019. It is technically a single instrument, almost identical to OCO-2.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere.\n\nOCO-3 incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. \n\nOxygen-A Band cloud screening algorithm is one of the primary cloud screening tools implemented in the operational OCO processing pipeline. The algorithm was introduced and applied to early GOSAT data  with further analysis performed on OCO-2 simulations.\n\nThe OCO ABO2 algorithm employs a fast Bayesian retrieval to estimate surface pressure and surface albedo from high resolution spectra of the molecular oxygen (O2) A-band, near 0.765 \u00b5m. The radiative transfer forward model (FM) assumes a clear-sky condition, i.e. Rayleigh scattering only, such that differences between the modeled and measured radiances are apparent when the measurement scene contains cloud or aerosol.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAI7QGND2FX1H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAI7QGND2FX1H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1131203,66 +1131181,66 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_IMAPDOAS_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO3_L2_IMAPDOAS_11r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_DQ_Statement_v10.pdf",
-                    "description": "OCO-3 Data Quality Statement",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Data Quality Statement",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_L2_DQ_Statement_v10.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_IMAPDOAS.11r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO3_DATA/OCO3_L2_IMAPDOAS.11r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L2_IMAPDOAS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO3_L2_IMAPDOAS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_IMAPDOAS.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO3_L2_IMAPDOAS.11r/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov3.jpl.nasa.gov/",
-                    "description": "OCO-3 Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Project Home Page",
+                    "downloadURL": "https://ocov3.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf",
-                    "description": "README document",
                     "@type": "dcat:Distribution",
+                    "description": "README document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_OCO3_B10_DUG.pdf",
-                    "description": "USER'S GUIDE",
                     "@type": "dcat:Distribution",
+                    "description": "USER'S GUIDE",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_OCO3_B10_DUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Fluorescence.V6.pdf",
-                    "description": "Software Interface Specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software Interface Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Fluorescence.V6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
@@ -1131272,695 +1131250,718 @@
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "downloadURL": "https://ocov3.jpl.nasa.gov/science/publications/",
-                    "description": "Publications from the Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "Publications from the Science Team",
+                    "downloadURL": "https://ocov3.jpl.nasa.gov/science/publications/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
-                    "description": "OCO Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "OCO Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-2+Documents",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-3+Known+Data+Issues",
-                    "description": "OCO-3 Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Data Gaps",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=OCO-3+Known+Data+Issues",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO3_logo.jpg",
+            "identifier": "C2910089793-GES_DISC",
+            "issued": "2021-05-31",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AI7QGND2FX1H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO3_L2_IMAPDOAS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-08-06T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-3",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-3 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP), Retrospective Processing V11r (OCO3_L2_IMAPDOAS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/397",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Westberg, H., B. Hall, A.V. Jackson, and C.N. Hewitt. 1998. BOREAS TGB-10 Oxidant Flux Data over the SSA. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/397",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-25T00:00:00Z/1994-09-09T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "air quality",
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
-            "identifier": "C2808132223-ORNL_CLOUD",
             "description": "Contains oxidant flux data collected by TGB-10 for sites in the Southern Study Area.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-10 Oxidant Flux Data over the SSA",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F397",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F397",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb10ofd/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgb10ofd/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB10_OXFLUX.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB10_OXFLUX.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/397",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/397",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb10ofd/comp/tgb10ofd.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb10ofd/comp/tgb10ofd.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb10ofd/comp/TGB10_OXFLUX.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb10ofd/comp/TGB10_OXFLUX.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb10ofd/comp/TGB10_OXFLUX.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb10ofd/comp/TGB10_OXFLUX.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb10ofd/comp/TGB10_OXFLUX.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgb10ofd/comp/TGB10_OXFLUX.txt",
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
+            "identifier": "C2808132223-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/397",
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
             "spatial": "53.99 -105.12",
+            "temporal": "1994-05-25T00:00:00Z/1994-09-09T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-10 Oxidant Flux Data over the SSA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MEaSUREs/GLDTA/XAERDT_L2_AHI_H08.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2024-02-21. AHI/Himawari-08 Dark Target Aerosol 10-Min L2 Full Disk 10 km. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MEaSUREs/GLDTA/XAERDT_L2_AHI_H08.001. https://doi.org/10.5067/MEaSUREs/GLDTA/XAERDT_L2_AHI_H08.001.",
-            "issued": "2023-07-31",
-            "temporal": "2019-01-01T00:00:00Z/2022-12-31T23:59:59.990Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-31",
-            "keyword": [
-                "atmosphere",
-                "aerosols",
-                "earth science"
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
-            "identifier": "C2859255251-LAADS",
-            "description": "The AHI/Himawari-08 Dark Target Aerosol 10-Min L2 Full Disk 10 km product, short-name XAERDT_L2_AHI_H08 is provided at 10-km spatial resolution (at-nadir) and a 10-minute full-disk cadence that typically yields about 142 granules over the daylit hours of a 24-hour period (there are no images produced at 02:20 or 14:20 UTC for navigation purposes).  The Himawari-8 platform served in the operational Himawari position (near 140.7\u00b0E) between October 2014 and 13 December 2022.  Himawari-9 replaced Himawari-8 and is currently operational.  The Himawari-8/AHI collection record spans from January 2019 through 12th December 2022.  The final 19 days of 2022 (December 13 through 31) are served by L2 products derived from the Himawari-9/AHI instrument.\r\n\r\nThe XAERDT_L2_AHI_H08 product is a part of the Geostationary Earth Orbit (GEO)\u2013Low-Earth Orbit (LEO) Dark Target Aerosol project under NASA\u2019s Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, led by Robert Levy, uses a special version of the MODIS Dark Target (DT) aerosol retrieval algorithm to produce Aerosol Optical Depth (AOD) and other aerosol parameters derived independently from seven sensor/platform combinations, where 3 are in GEO and 4 are in LEO.  The 3 GEO sensors include Advanced Baseline Imagers (ABI) on both GOES-16 (GOES-East) and GOES-17 (GOES-West), and Advanced Himawari Imager (AHI) on Himawari-8. The 4 LEO sensors include MODIS on both Terra and Aqua, and VIIRS on both Suomi-NPP and NOAA-20.  Adding the LEO sensors reinforces a major goal of this project, which is to render a consistent science maturity level across DT aerosol products derived from both types and sources of orbital satellites.\r\n\r\nThe XAERDT_L2_AHI_H08 product, in netCDF4 format, contains 45 Science Data Set (SDS) layers that include 8 geolocation and 37 geophysical SDSs.\r\n\r\n\r\nFor more information consult LAADS product description page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/XAERDT_L2_AHI_H08\r\n\r\nOr, Dark Target aerosol team Page at: \r\nhttps://darktarget.gsfc.nasa.gov/",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "AHI/Himawari-08 Dark Target Aerosol 10-Min L2 Full Disk 10 km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The AHI/Himawari-08 Dark Target Aerosol 10-Min L2 Full Disk 10 km product, short-name XAERDT_L2_AHI_H08 is provided at 10-km spatial resolution (at-nadir) and a 10-minute full-disk cadence that typically yields about 142 granules over the daylit hours of a 24-hour period (there are no images produced at 02:20 or 14:20 UTC for navigation purposes).  The Himawari-8 platform served in the operational Himawari position (near 140.7\u00b0E) between October 2014 and 13 December 2022.  Himawari-9 replaced Himawari-8 and is currently operational.  The Himawari-8/AHI collection record spans from January 2019 through 12th December 2022.  The final 19 days of 2022 (December 13 through 31) are served by L2 products derived from the Himawari-9/AHI instrument.\r\n\r\nThe XAERDT_L2_AHI_H08 product is a part of the Geostationary Earth Orbit (GEO)\u2013Low-Earth Orbit (LEO) Dark Target Aerosol project under NASA\u2019s Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, led by Robert Levy, uses a special version of the MODIS Dark Target (DT) aerosol retrieval algorithm to produce Aerosol Optical Depth (AOD) and other aerosol parameters derived independently from seven sensor/platform combinations, where 3 are in GEO and 4 are in LEO.  The 3 GEO sensors include Advanced Baseline Imagers (ABI) on both GOES-16 (GOES-East) and GOES-17 (GOES-West), and Advanced Himawari Imager (AHI) on Himawari-8. The 4 LEO sensors include MODIS on both Terra and Aqua, and VIIRS on both Suomi-NPP and NOAA-20.  Adding the LEO sensors reinforces a major goal of this project, which is to render a consistent science maturity level across DT aerosol products derived from both types and sources of orbital satellites.\r\n\r\nThe XAERDT_L2_AHI_H08 product, in netCDF4 format, contains 45 Science Data Set (SDS) layers that include 8 geolocation and 37 geophysical SDSs.\r\n\r\n\r\nFor more information consult LAADS product description page at:\r\n\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/XAERDT_L2_AHI_H08\r\n\r\nOr, Dark Target aerosol team Page at: \r\nhttps://darktarget.gsfc.nasa.gov/",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEaSUREs%2FGLDTA%2FXAERDT_L2_AHI_H08.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEaSUREs%2FGLDTA%2FXAERDT_L2_AHI_H08.001",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/XAERDT_L2_AHI_H08--5019",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/XAERDT_L2_AHI_H08--5019",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/DT_Aerosol_UG_MODIS_VIIRS_March_2023.pdf",
-                    "description": "A pdf version User's Guide for dark target products.",
                     "@type": "dcat:Distribution",
+                    "description": "A pdf version User's Guide for dark target products.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/DT_Aerosol_UG_MODIS_VIIRS_March_2023.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://darktarget.gsfc.nasa.gov/atbd/overview",
-                    "description": "An Agorithm Theoretical Basis Document (ATBD) for dark target products.",
                     "@type": "dcat:Distribution",
+                    "description": "An Agorithm Theoretical Basis Document (ATBD) for dark target products.",
+                    "downloadURL": "https://darktarget.gsfc.nasa.gov/atbd/overview",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "identifier": "C2859255251-LAADS",
+            "issued": "2023-07-31",
+            "keyword": [
+                "atmosphere",
+                "aerosols",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEaSUREs/GLDTA/XAERDT_L2_AHI_H08.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-01-01T00:00:00Z/2022-12-31T23:59:59.990Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AHI/Himawari-08 Dark Target Aerosol 10-Min L2 Full Disk 10 km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/J7GVFM11OGIX",
             "citation": "Nadia Smith. 2019-01-15. SNDRAQIML2CPS. Version 2.1. Sounder SIPS: AQUA AIRS IR + MW Level 2 CLIMCAPS: Retrieved atmospheric state V2.1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/J7GVFM11OGIX. https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML2CPS_2.1.html. Digital Science Data.",
-            "issued": "2002-08-31",
-            "temporal": "2002-08-31T00:00:00Z/2024-08-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-25",
-            "references": [
-                "https://doi.org/DOI  10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "precipitation",
-                "clouds",
-                "oceans",
-                "ocean temperature",
-                "atmosphere",
-                "atmospheric temperature",
-                "surface thermal properties",
-                "atmospheric radiation",
-                "atmospheric chemistry",
-                "altitude",
-                "air quality",
-                "land surface",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Nadia Smith",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2790934208-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the AIRS (Atmospheric Infrared Sounder) and AMSU (Advanced Microwave Sounding Unit). The AIRS instrument is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. The AIRS in combination with the AMSU constitutes an innovative atmospheric sounding group of infrared and microwave sensors. The AIRS Standard Retrieval Product consists of retrieved estimates of cloud and surface properties, plus profiles of retrieved temperature, water vapor, ozone, carbon monoxide and methane. The temperature profile vertical resolution is 100 levels total between 1100 mb and 0.1 mb, while moisture profile is reported at atmospheric layers between 1100 mb and 300 mb. The horizontal resolution is 50 km.\n\nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n\nAn AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track for each of the approximate 2378 channels. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRAQIML2CPS",
-            "creator": "Nadia Smith",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
-            "title": "Sounder SIPS: AQUA AIRS IR + MW Level 2 CLIMCAPS: Retrieved atmospheric state V2.1 (SNDRAQIML2CPS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML2CPS_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ7GVFM11OGIX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ7GVFM11OGIX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML2CPS_2.1.png",
-                    "description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML2CPS_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML2CPS_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRAQIML2CPS_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level2/SNDRAQIML2CPS.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/Aqua_Sounder_Level2/SNDRAQIML2CPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level2/SNDRAQIML2CPS.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/Aqua_Sounder_Level2/SNDRAQIML2CPS.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIML2CPS+2.1",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRAQIML2CPS+2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.1.README.pdf",
-                    "description": "CLIMCAPS L2 Product User Guide: File Format and Definition",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS L2 Product User Guide: File Format and Definition",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS_V2.1_L2_science_guides.pdf",
-                    "description": "CLIMCAPS Science Application Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS Science Application Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS_V2.1_L2_science_guides.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CrIS/ATMS CLIMCAPS Level 2.1 retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRAQIML2CPS_2.1.png",
+            "identifier": "C2790934208-GES_DISC",
+            "issued": "2002-08-31",
+            "keyword": [
+                "atmospheric water vapor",
+                "precipitation",
+                "clouds",
+                "oceans",
+                "ocean temperature",
+                "atmosphere",
+                "atmospheric temperature",
+                "surface thermal properties",
+                "atmospheric radiation",
+                "atmospheric chemistry",
+                "altitude",
+                "air quality",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/J7GVFM11OGIX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-09-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/DOI  10.3390/rs11101227",
+                "https://doi.org/10.1109/TGRS.2012.2220369",
+                "https://doi.org/10.1016/S0022-4073(97)00169-6",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRAQIML2CPS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-31T00:00:00Z/2024-08-12T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: AQUA AIRS IR + MW Level 2 CLIMCAPS: Retrieved atmospheric state V2.1 (SNDRAQIML2CPS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0675-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-26T21:45:45.000 to 2015-03-27T06:45:10.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0675-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0675-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0675-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-26T21:45:45.000 to 2015-03-27T06:45:10.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0675 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0675 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR20-V1.0",
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
+            "description": "The Cassini Radio Science Rhea Gravity Science Experiment (TIGR20) Raw Data Archive is a time-ordered collection of radio science raw data acquired on August 9, 10, and 11, 2016, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr20-v1.0_ndgf-rdgr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR20-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr20-v1.0_ndgf-rdgr",
-            "description": "The Cassini Radio Science Rhea Gravity Science Experiment (TIGR20) Raw Data Archive is a time-ordered collection of radio science raw data acquired on August 9, 10, and 11, 2016, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR20 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TIGR20 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image. Note that the two datasets RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07-V1.0 and RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07B-V1.0 have been merged into one dataset: RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m07-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "bias",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-prl-67pchuryumov-m07-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image. Note that the two datasets RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07-V1.0 and RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07B-V1.0 have been merged into one dataset: RO-C-OSINAC-2-PRL-67PCHURYUMOV-M07-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 2 PRL-MTP007 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 2 PRL-MTP007 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/WRF/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Colle, Brian  and Stacy  Brodzik.2022. Weather Research and Forecasting (WRF) Model IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/WRF/DATA101",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-12T00:00:00Z/2020-03-07T14:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "atmosphere",
-                "weather events",
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
-            "identifier": "C1995874860-GHRC_DAAC",
             "description": "The Weather Research and Forecasting (WRF) Model IMPACTS dataset includes model data simulated by the Weather Research and Forecasting (WRF) model for the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast (2020-2022). The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. The WRF model provided simulations of the precipitation events that were observed during the campaign using initial and boundary conditions from the Global Forecast System (GFS) model and the North American Mesoscale Forecast System (NAM). The WRF IMPACTS dataset files are available from January 12 through March 7, 2020 in netCDF-3 format.",
-            "title": "Weather Research and Forecasting (WRF) Model IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FWRF%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FWRF%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=wrfimpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=wrfimpacts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/IMPACTS/DATA101",
-                    "description": "IMPACTS Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/IMPACTS/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/impacts/content/IMPACTS",
-                    "description": "IMPACT Field Campaign Information",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACT Field Campaign Information",
+                    "downloadURL": "https://espo.nasa.gov/impacts/content/IMPACTS",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cloud.gsfc.nasa.gov/index.php?section=35",
-                    "description": "WRF Model Information",
                     "@type": "dcat:Distribution",
+                    "description": "WRF Model Information",
+                    "downloadURL": "https://cloud.gsfc.nasa.gov/index.php?section=35",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.mmm.ucar.edu/weather-research-and-forecasting-model",
-                    "description": "WRF Model Information",
                     "@type": "dcat:Distribution",
+                    "description": "WRF Model Information",
+                    "downloadURL": "https://www.mmm.ucar.edu/weather-research-and-forecasting-model",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/WRF/doc/wrfimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/WRF/doc/wrfimpacts_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "description": "IMPACTS Field Campaign Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Project Home Page",
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
+            "identifier": "C1995874860-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "atmosphere",
+                "weather events",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/WRF/DATA101",
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
             "spatial": "-114.202 22.9706 -53.798 53.5889",
+            "temporal": "2020-01-12T00:00:00Z/2020-03-07T14:59:59Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Weather Research and Forecasting (WRF) Model IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-4%2F6-CDR-V1.0",
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
+            "description": "This dataset contains CRISM VNIR and IR Calibration Data Records (CDRs), which are used to convert data from raw DNs to units of radiance or I/F for the CRISM instrument on MRO.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-4-6-cdr-v1.0_ndkm-f85d",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-CRISM-4%2F6-CDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-crism-4-6-cdr-v1.0_ndkm-f85d",
-            "description": "This dataset contains CRISM VNIR and IR Calibration Data Records (CDRs), which are used to convert data from raw DNs to units of radiance or I/F for the CRISM instrument on MRO.",
-            "title": "MRO CRISM CALIBRATION DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO CRISM CALIBRATION DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214353593-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
-            "issued": "2012-05-15",
-            "temporal": "2008-07-24T21:06:27Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "solid earth",
-                "earth science",
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
-            "identifier": "C1214353593-ASF",
             "description": "UAVSAR PolSAR Scene DEM TIFF",
-            "title": "UAVSAR_POLSAR_DEM",
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
+            "identifier": "C1214353593-ASF",
+            "issued": "2012-05-15",
+            "keyword": [
+                "solid earth",
+                "earth science",
+                "tectonics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214353593-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>64.623877 -9.140625 81.898451 -7.734375 83.84881 -34.453125 83.559717 -78.925781 77.915669 -124.804688 64.320872 -150.996094 55.776573 165.585938 45.58329 137.636719 36.456636 127.96875 29.840644 129.023438 18.646245 -159.433594 -47.989922 -76.640625 -47.989922 -64.6875 -37.160317 -52.382812 64.623877 -9.140625</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2008-07-24T21:06:27Z/2024-11-11T00:00:00Z",
             "theme": [
                 "Hayward Fault, CA",
                 "Laurentides Reserve, QC, Canada",
@@ -1132426,56 +1132427,69 @@
                 "Peace River and I17 Corridor, FL",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UAVSAR_POLSAR_DEM"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M17-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m17-inf-refl-v1.0_ndqj-tbad",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67P-M17-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67p-m17-inf-refl-v1.0_ndqj-tbad",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP017 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP017 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/ndt7-xzft",
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
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-103",
+                    "mediaType": "text/html",
+                    "title": "Rodent Research-1 (RR1) NASA Validation Flight: Mouse quadriceps muscle transcriptomic proteomic and epigenomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-103_ndt7-xzft",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid extraction",
                 "library construction",
@@ -1132492,219 +1132506,181 @@
```

