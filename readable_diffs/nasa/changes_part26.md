# Change History for nasa.json (Part 26)

### Changes from 31606f9 to dd2190f (Part 15/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-05-05T23:25:00.000 to 2015-06-02T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP016 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP016 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-RSS-5-GLGM3%2FGRAVITY-V1.0",
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
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-rss-5-glgm3-gravity-v1.0_4mrd-dkps",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-RSS-5-GLGM3%2FGRAVITY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-rss-5-glgm3-gravity-v1.0_4mrd-dkps",
-            "description": "Unknown",
-            "title": "LUNAR PROSPECTOR MOON RSS 5 GLGM3/GRAVITY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LUNAR PROSPECTOR MOON RSS 5 GLGM3/GRAVITY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-02-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/MACPEX_MetNav_AircraftInSitu_WB57_Data_1.",
-            "issued": "2021-11-26",
-            "temporal": "2011-03-18T00:00:00Z/2011-04-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-11",
-            "keyword": [
-                "atmospheric winds",
-                "atmosphere",
-                "altitude",
-                "atmospheric temperature",
-                "earth science",
-                "atmospheric pressure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Katja Drdla",
                 "hasEmail": "mailto:katja.drdla@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2218601235-LARC_ASDC",
             "description": "MACPEX_MetNav_AircraftInSitu_WB57_Data is the in-situ meteorology and navigational data collection during the Mid-latitude Airborne Cirrus Properties Experiment (MACPEX). Data from the Meteorological Measurement System (MMS) is featured in this collection. Data collection for this product is complete.\r\n\r\nThe MACPEX mission was an airborne field campaign that deployed from March 18th to April 26th, 2011. MACPEX sought to investigate cirrus cloud properties and the processes that affect their impact on radiation. The campaign conducted science flights using the NASA WB-57 aircraft based out of Ellington Airfield, Texas. Science flights were focused on the central North America vicinity, with an emphasis over the Southern Great Plains atmospheric observatory (established by the Department of Energy\u2019s (DoE) Atmospheric Radiation Measurement (ARM) user facility) site in Oklahoma. MACPEX was a joint effort between NASA, the NOAA Earth System Research Laboratory (ESRL), the National Center for Atmospheric Research (NCAR), and several U.S. universities.\r\n\r\nThe WB-57 contained a comprehensive instrument payload for detailed in-situ measurements that were targeted to answer MACPEX\u2019s four major science questions. The first science question that MACPEX explored was how prevalent the smaller crystals are in cirrus clouds, and how important they are for extinction, radiative forcing, and radiative heating. MACPEX also sought to understand how cirrus microphysical properties (particle size distribution, ice crystal habit, extinction, ice water content) are related to the dynamical forcing driving cloud formation. Researchers also investigated how cirrus microphysical properties are related to aerosol loading and composition, including the abundance of heterogeneous ice nuclei. Lastly, this campaign examined how cirrus microphysical properties evolve through the lifecycles of the clouds, and the role radiatively driven dynamical motions play.\r\n\r\nIn addition to the in-situ measurements, four flights were coordinated to validate the NASA EOS/A-Train satellite observations. NOAA also launched balloon sondes and ozonesondes, which were used to acquire data about the frost point and water vapor in the atmosphere. The balloon sondes and ozonesondes also acquired pressure, temperature, and humidity data, as well as measurements regarding the ozone in the atmosphere.",
-            "title": "MACPEX WB-57 Aircraft In-situ Meteorology and Navigational Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FMACPEX_MetNav_AircraftInSitu_WB57_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FMACPEX_MetNav_AircraftInSitu_WB57_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/macpex",
-                    "description": "MACPEX Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "MACPEX Project Home Page",
+                    "downloadURL": "https://espo.nasa.gov/macpex",
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
-                    "downloadURL": "https://espo.nasa.gov/macpex/content/MACPEX_Science_-_Flight_Information",
-                    "description": "MACPEX Science Flight Information",
                     "@type": "dcat:Distribution",
+                    "description": "MACPEX Science Flight Information",
+                    "downloadURL": "https://espo.nasa.gov/macpex/content/MACPEX_Science_-_Flight_Information",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2013JD020817",
-                    "description": "AGU Article, Evaluation of UT/LS hygrometer accuracy by intercomparison during the NASA MACPEX mission",
                     "@type": "dcat:Distribution",
+                    "description": "AGU Article, Evaluation of UT/LS hygrometer accuracy by intercomparison during the NASA MACPEX mission",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2013JD020817",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/view/journals/atsc/73/12/jas-d-16-0126.1.xml?tab_body=pdf",
-                    "description": "BAMS Article, The Microphysical Properties of Small Ice Particles Measured by the Small Ice Detector-3 Probe during the MACPEX Field Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "BAMS Article, The Microphysical Properties of Small Ice Particles Measured by the Small Ice Detector-3 Probe during the MACPEX Field Campaign",
+                    "downloadURL": "https://journals.ametsoc.org/view/journals/atsc/73/12/jas-d-16-0126.1.xml?tab_body=pdf",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/view/journals/apme/56/3/jamc-d-16-0222.1.xml",
-                    "description": "BAMS Article, Ice Particle Mass\u2013Dimensional Relationship Retrieval and Uncertainty Evaluation Using the Optimal Estimation Methodology Applied to the MACPEX Data",
                     "@type": "dcat:Distribution",
+                    "description": "BAMS Article, Ice Particle Mass\u2013Dimensional Relationship Retrieval and Uncertainty Evaluation Using the Optimal Estimation Methodology Applied to the MACPEX Data",
+                    "downloadURL": "https://journals.ametsoc.org/view/journals/apme/56/3/jamc-d-16-0222.1.xml",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/topics/earth/features/MACPEX_QandA.html",
-                    "description": "MACPEX Q&A on nasa.gov",
                     "@type": "dcat:Distribution",
+                    "description": "MACPEX Q&A on nasa.gov",
+                    "downloadURL": "https://www.nasa.gov/topics/earth/features/MACPEX_QandA.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
-                    "description": "DOI Data Set Landing Page for MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page for MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2218601235-LARC_ASDC",
-                    "description": "Earthdata Search Client for MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2218601235-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MACPEX/MetNav_AircraftInSitu_WB57_Data_1/",
-                    "description": "ASDC Direct Data Download for MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MACPEX/MetNav_AircraftInSitu_WB57_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2218601235-LARC_ASDC",
+            "issued": "2021-11-26",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "altitude",
+                "atmospheric temperature",
+                "earth science",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/MACPEX_MetNav_AircraftInSitu_WB57_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>15.0 -107.0 15.0 -80.0 45.0 -80.0 45.0 -107.0 15.0 -107.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2011-03-18T00:00:00Z/2011-04-27T23:59:59.999Z",
             "theme": [
                 "MACPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MACPEX WB-57 Aircraft In-situ Meteorology and Navigational Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ADEOS/OCTS_OC.2014.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ADEOS/OCTS_OC.2014.0.",
-            "issued": "2017-01-11",
-            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-10",
-            "keyword": [
-                "earth science",
-                "oceans",
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
-            "identifier": "C1200034380-OB_DAAC",
             "description": "On August 17, 1996, the Japanese Space Agency (NASDA - National Space Development Agency)\nlaunched the Advanced Earth Observing Satellite (ADEOS). ADEOS was in a descending, Sun\nsynchronous orbit with a nominal equatorial crossing time of 10:30 a.m. Amoung the\ninstruments carried aboard the ADEOS spacecraft was the Ocean Color and Temperature\nScanner (OCTS). OCTS is an optical radiometer with 12 bands covering the visible, near\ninfrared and thermal infrared regions. (Eight of the bands are in the VIS/NIR. These are\nthe only bands calibrated and processed by the OBPG) OCTS has a swath width of\napproximately 1400 km, and a nominal nadir resolution of 700 m. The instrument operated\nat three tilt states (20 degrees aft, nadir and 20 degrees fore), similar to SeaWiFS.",
-            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Ocean Color (OC) Regional Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS%2FOCTS_OC.2014.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FADEOS%2FOCTS_OC.2014.0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/OCTS/L2/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/OCTS/L2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/octs",
-                    "description": "NASA Ocean Color Web - Instrument Description Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Instrument Description Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/octs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
-                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Descriptions",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing",
-                    "description": "NASA Ocean Color Web - Data Processing History",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Processing History",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS/OCTS_OC.2014.0",
-                    "description": "OB.DAAC OCTS ADEOS-I L2 Ocean Color (OC) Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OCTS ADEOS-I L2 Ocean Color (OC) Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ADEOS/OCTS_OC.2014.0",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl",
-                    "description": "Ocean Color Forum",
                     "@type": "dcat:Distribution",
+                    "description": "Ocean Color Forum",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/forum/oceancolor/forum_show.pl",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1200034380-OB_DAAC",
+            "issued": "2017-01-11",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/ADEOS/OCTS_OC.2014.0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-10-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-11-01T00:00:00Z/1997-06-30T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ADEOS-I Ocean Color and Temperature Scanner (OCTS) Ocean Color (OC) Regional Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243140611-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "SMAP Level 1C Sigma Naught High Res Data Quality Info Version 3",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1243140611-ASF",
             "issued": "2015-07-31",
-            "temporal": "2015-02-12T16:02:58Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-05-24",
             "keyword": [
                 "active remote sensing",
                 "nasa decadal survey",
@@ -146451,269 +146463,266 @@
                 "earth observation satellites",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1243140611-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-05-24",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1243140611-ASF",
-            "description": "SMAP Level 1C Sigma Naught High Res Data Quality Info Version 3",
-            "title": "SMAP_L1C_SIGMA_NAUGHT_HIGH_RES_QA_V003",
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
+            "title": "SMAP_L1C_SIGMA_NAUGHT_HIGH_RES_QA_V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0186-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-07T14:19:05.000 to 2014-08-07T19:38:49.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0186-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0186-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0186-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-07T14:19:05.000 to 2014-08-07T19:38:49.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0186 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0186 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA4.001",
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2018-11-17. VNP43MA4. Version 001. VIIRS/NPP BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global 1km SIN Grid V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43MA4.001. https://doi.org/10.5067/VIIRS/VNP43MA4.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2018-11-17",
-            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-17",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "surface radiative properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
+            "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1412449610-LPDAAC_ECS",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
             "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Nadir Bidirectional Reflectance Distribution Function (BRDF) Adjusted Reflectance (NBAR) Version 1 product provides NBAR estimates at 1 kilometer (km) resolution. The VNP43IA4 product is produced daily using 16-day VIIRS data and is weighted temporally to the 9th day, which is reflected in the file name. The view angle effects are removed from the directional reflectances resulting in a stable and consistent NBAR product. The VNP43 data products are designed after the Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo product suite to promote the continuity of the Earth Observation System (EOS) mission. The VNP43 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite.\r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from VNP43MA1 to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43MA4), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43MA3). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nThe VNP43MA4 product includes 18 SDS layers for BRDF/Albedo mandatory quality and nadir reflectance for VIIRS nine moderate bands M1-M5, M7-M8, and M10-M11. A low resolution browse image is also available showing NBAR bands M5, M7, and M5 as an RGB image in JPEG format.\r\n\r\nProduct Maturity\r\n\r\nValidation at stage 1 has been achieved for the VIIRS BRDF/Albedo product suite. Visit the VIIRS Land Product Quality Assessment website for additional information on validation and product maturity status.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43MA4",
-            "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global 1km SIN Grid V001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP43MA4.A2019175.h19v04.001.2019183072445.1.jpg?_ga=2.79669076.116070394.1561987039-1109527761.1561753117",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43MA4.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43MA4.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43MA4.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43MA4.001",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43MA4.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43MA4.001/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1412449610-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1412449610-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guide/vnp43ia4-and-vnpma4-nbar-products/",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guide/vnp43ia4-and-vnpma4-nbar-products/",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43MA4",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43MA4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP43MA4.A2019175.h19v04.001.2019183072445.1.jpg?_ga=2.79669076.116070394.1561987039-1109527761.1561753117",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP43MA4.A2019175.h19v04.001.2019183072445.1.jpg?_ga=2.79669076.116070394.1561987039-1109527761.1561753117",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP104/VIIRS/VNP43MA4.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP104/VIIRS/VNP43MA4.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP43MA4.A2019175.h19v04.001.2019183072445.1.jpg?_ga=2.79669076.116070394.1561987039-1109527761.1561753117",
+            "identifier": "C1412449610-LPDAAC_ECS",
+            "issued": "2018-11-17",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA4.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-11-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "VNP43MA4",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Nadir BRDF-Adjusted Ref Daily L3 Global 1km SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBIS4-V1.0",
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
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Titan Bistatic experiments (TBIS4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 13 and 14, 2016, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tbis4-v1.0_4n7c-pp8m",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBIS4-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tbis4-v1.0_4n7c-pp8m",
-            "description": "The Cassini Radio Science Titan Bistatic experiments (TBIS4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 13 and 14, 2016, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TBIS4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TBIS4 V1.0"
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
+            "description": "Exp: FAITH Hill 3-D Separated Flow. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/FAITH_Hill/Geometry_files.tar.gz",
+                    "mediaType": "application/x-gzip"
+                }
             ],
+            "identifier": "NASA-853",
+            "issued": "2018-06-25",
             "keyword": [
                 "models",
                 "separation",
@@ -146724,591 +146733,591 @@
                 "flow",
                 "hill"
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
-            "identifier": "NASA-853",
-            "description": "Exp: FAITH Hill 3-D Separated Flow. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: FAITH Hill 3-D Separated Flow",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/FAITH_Hill/Geometry_files.tar.gz",
-                    "mediaType": "application/x-gzip"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments: FAITH Hill 3-D Separated Flow"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-1-BSR-V1.0",
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
-                "magellan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Magellan (MGN) Bistatic Radar (BSR) Raw Data Archive (RDA) is a time-ordered collection of raw and partially processed data from bistatic radar experiments conducted using the Magellan spacecraft while it orbited Venus.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-1-bsr-v1.0_4na5-dvw4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-1-BSR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-1-bsr-v1.0_4na5-dvw4",
-            "description": "The Magellan (MGN) Bistatic Radar (BSR) Raw Data Archive (RDA) is a time-ordered collection of raw and partially processed data from bistatic radar experiments conducted using the Magellan spacecraft while it orbited Venus.",
-            "title": "MAGELLAN BISTATIC RADAR RAW DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAGELLAN BISTATIC RADAR RAW DATA RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/SSMIS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kidd, Chris.2012. GPM GROUND VALIDATION SPECIAL SENSOR MICROWAVE IMAGER/SOUNDER (SSMI/S) LPVEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/LPVEX/SSMIS/DATA101",
-            "issued": "2012-01-31",
-            "temporal": "2010-09-01T03:52:00Z/2011-03-31T18:27:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
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
-            "identifier": "C1979814673-GHRC_DAAC",
             "description": "The GPM Ground Validation Special Sensor Microwave Imager/Sounder (SSMI/S) LPVEx dataset contains brightness temperature data processed from the NOAA CLASS QC temperature data records for the Light Precipitation Validation Experiment (LVPEX), part of the Global Precipitation Measurement project. The mission was to detect and characterize light rain and evaluate their estimates of rainfall intensity in high latitude, shallow freezing level environments.Only data with swaths within the area of interest are included. The temporal range of the data includes the LPVEx campaign period (September 1, 2010) and extends through the end of March 31, 2011.",
-            "title": "GPM GROUND VALIDATION SPECIAL SENSOR MICROWAVE IMAGER/SOUNDER (SSMI/S) LPVEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FSSMIS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FSSMIS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsslpvex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsslpvex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/LPVEX/DATA101",
-                    "description": "LPVEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/LPVEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/lpvex/gpmsslpvex/gpmsslpvex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/lpvex/gpmsslpvex/gpmsslpvex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/lpvex/gpmsslpvex/ssmis-tdr.pdf",
-                    "description": "NOAA's National Climatic Data Center: Temperature Data Record File (TOR) April 10, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA's National Climatic Data Center: Temperature Data Record File (TOR) April 10, 2007",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/lpvex/gpmsslpvex/ssmis-tdr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/lpvex/gpmsslpvex/LPVEx_TDRs.doc",
-                    "description": "LPVEx extracted SSMIS Temperature Data Records",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx extracted SSMIS Temperature Data Records",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/lpvex/gpmsslpvex/LPVEx_TDRs.doc",
+                    "mediaType": "application/msword",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/lpvex/gpmsslpvex/read_SSMIS_LPVEx_summary.f",
-                    "description": "program to read extracted NOAA TDR SSMIS data",
                     "@type": "dcat:Distribution",
+                    "description": "program to read extracted NOAA TDR SSMIS data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/lpvex/gpmsslpvex/read_SSMIS_LPVEx_summary.f",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/LPVEx",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/LPVEx",
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
+            "identifier": "C1979814673-GHRC_DAAC",
+            "issued": "2012-01-31",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/SSMIS/DATA101",
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
             "spatial": "-30.79 27.89 172.28 89.56",
+            "temporal": "2010-09-01T03:52:00Z/2011-03-31T18:27:00Z",
             "theme": [
                 "LPVEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION SPECIAL SENSOR MICROWAVE IMAGER/SOUNDER (SSMI/S) LPVEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-3-EDR-CROMMELIN-V1.0",
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
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-3-edr-crommelin-v1.0_4nd8-dzpv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-SPEC-3-EDR-CROMMELIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-spec-3-edr-crommelin-v1.0_4nd8-dzpv",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET SPEC CALIB EXPERIMENT DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET SPEC CALIB EXPERIMENT DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567290-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 2010-01-01. USGS Global Forest Observations Initiative (GFOI) Colombia. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://lsiexplorer.cr.usgs.gov.",
-            "issued": "1979-01-09",
-            "temporal": "1979-01-09T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "biosphere",
-                "agriculture",
-                "vegetation",
-                "terrestrial ecosystems",
-                "forest science",
-                "habitat conversion/fragmentation"
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
-            "identifier": "C1220567290-USGS_LTA",
-            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring sy\nstems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
             "creator": "U.S. Geological Survey",
-            "title": "USGS Global Forest Observations Initiative (GFOI) Colombia",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Forest Observations Initiative (GFOI) is an initiative of the inter-governmental Group on Earth Observations (GEO) that aims to:\n\nfoster the sustained availability of observations for national forest monitoring sy\nstems; support governments that are establishing national systems by providing a platform for coordinating observations, providing assistance and guidance on utilizing observations, developing accepted methods and protocols, and promoting ongoing research and development; and work with national governments that report into international forest assessments (such as the global Forest Resources Assessment (FRA) of the Food and Agriculture Organization, FAO) and the national greenhouse gas inventories reported to the UN Framework Convention on Climate Change (UNFCCC) using methods of the Intergovernmental Panel on Climate Change (IPCC).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.gfoi.org/",
-                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Group on Earth Observations (GEO) Global Forest Observations Initiative (GFOI)\n      ",
+                    "downloadURL": "http://www.gfoi.org/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C1220567290-USGS_LTA",
+            "issued": "1979-01-09",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "biosphere",
+                "agriculture",
+                "vegetation",
+                "terrestrial ecosystems",
+                "forest science",
+                "habitat conversion/fragmentation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567290-USGS_LTA.html",
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
             "spatial": "-80.9 -5.52 -65.31 13.99",
+            "temporal": "1979-01-09T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CWIC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USGS Global Forest Observations Initiative (GFOI) Colombia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M17-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m17-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M17-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m17-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP017 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP017 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0660-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-20T13:25:05.000 to 2015-03-20T16:24:20.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0660-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0660-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0660-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-20T13:25:05.000 to 2015-03-20T16:24:20.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0660 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0660 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-hgcoords-1.92sec-v1.0_4nhi-chjt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-rdr-hgcoords-1.92sec-v1.0_4nhi-chjt",
-            "description": "not applicable",
-            "title": "VG1 JUP MAG RESAMPLED HELIOGRAPHIC (RTN) COORDS 1.92SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 JUP MAG RESAMPLED HELIOGRAPHIC (RTN) COORDS 1.92SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/C3VP/VISSENSOR/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rodriguez, Peter .2021. GPM Ground Validation Environment Canada (EC) Visibility Sensor FD12P C3VP [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/C3VP/VISSENSOR/DATA101",
-            "issued": "2021-01-26",
-            "temporal": "2006-10-04T00:00:00Z/2007-03-31T23:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "air quality",
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1995871445-GHRC_DAAC",
             "description": "The GPM Ground Validation (GV) Environment Canada (EC) Visibility Sensor FD12P C3VP dataset consists of visibility and precipitation data collected at the Environment Canada Canadian Climate station at the Centre for Atmospheric Research Experiments (CARE) site during the Canadian CloudSat/CALIPSO Validation Project (C3VP) field campaign. The campaign took place in southern Canada in support of multiple science missions, including the NASA GPM mission, in order to improve the modeling and remote sensing of winter precipitation. The GPM GV Visibility Sensor FD12P C3VP data are available from October 4, 2006 through March 31, 2007 in a Microsoft Excel comma-separated variable spreadsheet.",
-            "title": "GPM Ground Validation Environment Canada (EC) Visibility Sensor FD12P C3VP V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FC3VP%2FVISSENSOR%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FC3VP%2FVISSENSOR%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmvisecc3vp",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmvisecc3vp",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/FD12P%20User%20Guide%20in%20English.pdf",
-                    "description": "Weather Sensor FD12P User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Weather Sensor FD12P User\u2019s Guide",
+                    "downloadURL": "https://www.vaisala.com/sites/default/files/documents/FD12P%20User%20Guide%20in%20English.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/c3vp/fd12p/doc/gpmvisecc3vp_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/relatedProjects/c3vp/fd12p/doc/gpmvisecc3vp_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://radarmet.atmos.colostate.edu/c3vp/petersenetal_C3VP.pdf",
-                    "description": "NASA GPM/PMM PARTICIPATION IN THE CANADIAN CLOUDSAT/CALIPSO VALIDATION PROJECT (C3VP): PHYSICAL PROCESS STUDIES IN SNOW",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GPM/PMM PARTICIPATION IN THE CANADIAN CLOUDSAT/CALIPSO VALIDATION PROJECT (C3VP): PHYSICAL PROCESS STUDIES IN SNOW",
+                    "downloadURL": "https://radarmet.atmos.colostate.edu/c3vp/petersenetal_C3VP.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
+            "identifier": "C1995871445-GHRC_DAAC",
+            "issued": "2021-01-26",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/C3VP/VISSENSOR/DATA101",
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
             "spatial": "-79.791 44.222 -79.772 44.242",
+            "temporal": "2006-10-04T00:00:00Z/2007-03-31T23:59:00Z",
             "theme": [
                 "C3VP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Environment Canada (EC) Visibility Sensor FD12P C3VP V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M14-V3.0",
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
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m14-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC2-67PCHURYUMOV-M14-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc2-67pchuryumov-m14-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC2-MTP014 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC2-MTP014 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC23-V1.0",
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
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC23) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 2, 12, 28, and on December 5 and 19, 2016, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc23-v1.0_4nkv-v9tm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SROC23-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sroc23-v1.0_4nkv-v9tm",
-            "description": "The Cassini Radio Science Saturn Ring and Atmospheric Occultation experiments (SROC23) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 2, 12, 28, and on December 5 and 19, 2016, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SROC23 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SROC23 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M14-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m14-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67P-M14-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67p-m14-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 2 mission phase, covering the period  from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP014 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP014 RDR-INF-REFL V1.0"
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
+            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SPICE",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130601.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-480",
+            "issued": "2018-06-25",
             "keyword": [
                 "mcs",
                 "spice",
@@ -147319,743 +147328,714 @@
                 "ctx",
                 "crism"
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
-            "identifier": "NASA-480",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 25",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130601.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 25"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "AMSRE_AVRMO",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/UJYEX3XPWWB2",
             "citation": "NEESPI Data Center Project. 2002-07-01. AMSRE_AVRMO. Version 005. AMSR-E/Aqua level 3 global monthly Surface Soil Moisture Averages V005. Greenbelt, MD, USA. AMSRE_AVRMO. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/UJYEX3XPWWB2. https://disc.gsfc.nasa.gov/datacollection/AMSRE_AVRMO_005.html. Digital Science Data.",
-            "issued": "2009-03-10",
-            "temporal": "2002-10-01T00:00:00Z/2011-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-09-30",
-            "keyword": [
-                "land surface",
-                "soils",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PETER ROMANOV, PHD",
                 "hasEmail": "mailto:Peter.Romanov@noaa.gov"
             },
+            "creator": "NEESPI Data Center Project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239898008-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The dataset contains global monthly-mean soil moisture statistics (average values) for 1 by 1 degree grid cells. The source for the data is AMSR-E daily estimates of soil moisture (AE_Land3.002: AMSR-E/Aqua Daily L3 Surface Soil Moisture, Interpretive Parameters, QC EASE-Grids. Version 2 ). The dataset covers the time period from 2002-10-01 to 2011-09-30.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AMSRE_AVRMO",
-            "creator": "NEESPI Data Center Project",
-            "graphic-preview-description": "Sample image of AMSR-E global monthly mean soil moisture at 1x1 degree, Jan 2010",
-            "title": "AMSR-E/Aqua level 3 global monthly Surface Soil Moisture Averages V005 (AMSRE_AVRMO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AMSRE_AVRMO_005.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUJYEX3XPWWB2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUJYEX3XPWWB2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AMSRE_AVRMO_005.png",
-                    "description": "Sample image of AMSR-E global monthly mean soil moisture at 1x1 degree, Jan 2010",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image of AMSR-E global monthly mean soil moisture at 1x1 degree, Jan 2010",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AMSRE_AVRMO_005.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AMSRE_AVRMO_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AMSRE_AVRMO_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Soil_Moisture/AMSRE_AVRMO.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Soil_Moisture/AMSRE_AVRMO.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Soil_Moisture/AMSRE_AVRMO.005/doc/README.AMSRE_SoilMoisture_1deg.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Soil_Moisture/AMSRE_AVRMO.005/doc/README.AMSRE_SoilMoisture_1deg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "Sample image of AMSR-E global monthly mean soil moisture at 1x1 degree, Jan 2010",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AMSRE_AVRMO_005.png",
+            "identifier": "C1239898008-GES_DISC",
+            "issue-identification": "AMSRE_AVRMO",
+            "issued": "2009-03-10",
+            "keyword": [
+                "land surface",
+                "soils",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/UJYEX3XPWWB2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AMSRE_AVRMO",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-10-01T00:00:00Z/2011-09-30T23:59:59.999Z",
             "theme": [
                 "NEESPI NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua level 3 global monthly Surface Soil Moisture Averages V005 (AMSRE_AVRMO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-CAL-SSI-6-V1.0",
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
-                "non science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-cal-ssi-6-v1.0_4ns7-tmsc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "non science"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-CAL-SSI-6-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-cal-ssi-6-v1.0_4ns7-tmsc",
-            "description": "not applicable",
-            "title": "GALILEO SOLID STATE IMAGING CALIBRATION FILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO SOLID STATE IMAGING CALIBRATION FILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-PROPERTIES-V1.0",
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
-                "comet"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set presents tables 1, 2, 3, 4, 5 and 7 of 'Sizes, Shapes, Albedos, and Colors of Cometary Nuclei' (Lamy et al., 2004), and includes references for the sources cited. The authors culled this data from published or well-known unpublished sources, and have indicated what they judge to be the most reliable value available.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-properties-v1.0_4ns8-y7gy",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "comet"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-C-COMPIL-5-COMET-NUC-PROPERTIES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-c-compil-5-comet-nuc-properties-v1.0_4ns8-y7gy",
-            "description": "This data set presents tables 1, 2, 3, 4, 5 and 7 of 'Sizes, Shapes, Albedos, and Colors of Cometary Nuclei' (Lamy et al., 2004), and includes references for the sources cited. The authors culled this data from published or well-known unpublished sources, and have indicated what they judge to be the most reliable value available.",
-            "title": "PROPERTIES OF COMET NUCLEI",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PROPERTIES OF COMET NUCLEI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/SKY-IMAGER/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tsay, Si-Chee , Adrian  Loftus and Peter  Pantina.2015. GPM GROUND VALIDATION TOTAL SKY IMAGER IPHEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/IPHEX/SKY-IMAGER/DATA101",
-            "issued": "2015-11-10",
-            "temporal": "2014-05-06T20:54:00Z/2014-06-15T22:19:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-25",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
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
-            "identifier": "C1980067507-GHRC_DAAC",
             "description": "The GPM Ground Validation Total Sky Imager IPHEx dataset was gathered during the GPM Ground Validation Integrated Precipitation and Hydrology Experiment (IPHEx) in North Carolina from May 9, 2014 through June 14, 2014. The dataset includes data from the total sky imager instrument which is part of the NASA Goddard Space Flight Center (GSFC) ACHIEVE ground-based mobile laboratory. It is an automatic, full-color sky imager system providing real-time, full color digital images of daytime sky conditions. Data files are available in the JPEG image format.",
-            "title": "GPM GROUND VALIDATION TOTAL SKY IMAGER IPHEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FSKY-IMAGER%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FIPHEX%2FSKY-IMAGER%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmasinaiphx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmasinaiphx",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/AllSkyImager/doc/gpmasinaiphx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/iphex/AllSkyImager/doc/gpmasinaiphx_dataset.pdf",
+                    "mediaType": "application/pdf",
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
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
-                    "description": "IPHEx Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Project Home Page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/iphex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/integrated-precipitation-and-hydrology-experiment-iphex",
-                    "description": "IPHEx Field Campaign Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "IPHEx Field Campaign Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/integrated-precipitation-and-hydrology-experiment-iphex",
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
+            "identifier": "C1980067507-GHRC_DAAC",
+            "issued": "2015-11-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/IPHEX/SKY-IMAGER/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-83.18 35.48 -83.04 35.56",
+            "temporal": "2014-05-06T20:54:00Z/2014-06-15T22:19:00Z",
             "theme": [
                 "IPHEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION TOTAL SKY IMAGER IPHEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1724",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Anderson, V., D.R.N. Brown, and T.J. Brinkman. 2019. ABoVE: Annual Thaw Slump Expansion on East Fork Chandalar River, Alaska, 2008-2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1724",
-            "issued": "2019-12-17",
-            "temporal": "2008-08-23T00:00:00Z/2017-09-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "erosion/sedimentation",
-                "frozen ground",
-                "cryosphere"
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
-            "identifier": "C2143402706-ORNL_CLOUD",
             "description": "This dataset provides a time series of spatial data showing the expansion of a thaw slump on the East Fork Chandalar River near the community of Venetie, Alaska, from 2008 through 2017. The erosion of vegetated areas along the river was documented by manually digitizing imagery from ESRI basemaps and Landsat 5 (TM), 7 (ETM+), and 8 (OLI), using the band combination of shortwave infrared 2, shortwave infrared 1, and red.",
-            "graphic-preview-description": "Annual expansion of a thaw slump on the East Fork Chandalar River near the community of Venetie, Alaska, from 2008 through 2017. The erosion time series was created by manually digitizing from ESRI basemap and Landsat 5, 7, and 8 imagery. The eroded area appears to be growing steadily, mostly to the east, with apparent limitation on growth to the north and south. Source: Thaw_Slump_Images.pdf companion file.",
-            "title": "ABoVE: Annual Thaw Slump Expansion on East Fork Chandalar River, Alaska, 2008-2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Annual_Thaw_Slump_Fig1.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1724",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1724",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Annual_Thaw_Slump/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Annual_Thaw_Slump/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Annual_Thaw_Slump.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Annual_Thaw_Slump.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1724",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1724",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Annual_Thaw_Slump/comp/Annual_Thaw_Slump.pdf",
-                    "description": "Annual thaw slump expansion on E. Fork Chandalar River, Alaska, 2008-2017: Annual_Thaw_Slump.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Annual thaw slump expansion on E. Fork Chandalar River, Alaska, 2008-2017: Annual_Thaw_Slump.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Annual_Thaw_Slump/comp/Annual_Thaw_Slump.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Annual_Thaw_Slump/comp/thaw_slump_expansion.kmz",
-                    "description": "Annual thaw slump expansion on E. Fork Chandalar River, Alaska, 2008-2017: thaw_slump_expansion.kmz",
                     "@type": "dcat:Distribution",
+                    "description": "Annual thaw slump expansion on E. Fork Chandalar River, Alaska, 2008-2017: thaw_slump_expansion.kmz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Annual_Thaw_Slump/comp/thaw_slump_expansion.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Annual_Thaw_Slump/comp/Thaw_Slump_Images.pdf",
-                    "description": "ABoVE: Annual Thaw Slump Expansion on East Fork Chandalar River, Alaska, 2008-2017: Thaw_Slump_Images.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Annual Thaw Slump Expansion on East Fork Chandalar River, Alaska, 2008-2017: Thaw_Slump_Images.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Annual_Thaw_Slump/comp/Thaw_Slump_Images.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Annual_Thaw_Slump_Fig1.PNG",
-                    "description": "Annual expansion of a thaw slump on the East Fork Chandalar River near the community of Venetie, Alaska, from 2008 through 2017. The erosion time series was created by manually digitizing from ESRI basemap and Landsat 5, 7, and 8 imagery. The eroded area appears to be growing steadily, mostly to the east, with apparent limitation on growth to the north and south. Source: Thaw_Slump_Images.pdf companion file.",
                     "@type": "dcat:Distribution",
+                    "description": "Annual expansion of a thaw slump on the East Fork Chandalar River near the community of Venetie, Alaska, from 2008 through 2017. The erosion time series was created by manually digitizing from ESRI basemap and Landsat 5, 7, and 8 imagery. The eroded area appears to be growing steadily, mostly to the east, with apparent limitation on growth to the north and south. Source: Thaw_Slump_Images.pdf companion file.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Annual_Thaw_Slump_Fig1.PNG",
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
+            "graphic-preview-description": "Annual expansion of a thaw slump on the East Fork Chandalar River near the community of Venetie, Alaska, from 2008 through 2017. The erosion time series was created by manually digitizing from ESRI basemap and Landsat 5, 7, and 8 imagery. The eroded area appears to be growing steadily, mostly to the east, with apparent limitation on growth to the north and south. Source: Thaw_Slump_Images.pdf companion file.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Annual_Thaw_Slump_Fig1.PNG",
+            "identifier": "C2143402706-ORNL_CLOUD",
+            "issued": "2019-12-17",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "erosion/sedimentation",
+                "frozen ground",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1724",
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
             "spatial": "-146.07 67.63 -146.06 67.64",
+            "temporal": "2008-08-23T00:00:00Z/2017-09-17T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Annual Thaw Slump Expansion on East Fork Chandalar River, Alaska, 2008-2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0880-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-07T03:20:40.000 to 2015-07-07T05:19:53.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0880-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0880-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0880-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-07T03:20:40.000 to 2015-07-07T05:19:53.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0880 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0880 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/220/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-10-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
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
-            "identifier": "DASHLINK_220",
             "description": "not available",
-            "title": "CIDU Proceedings",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/CIDU_Proceedings.pdf",
-                    "description": "CIDU Proceedings",
                     "@type": "dcat:Distribution",
+                    "description": "CIDU Proceedings",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/CIDU_Proceedings.pdf",
+                    "mediaType": "application/pdf",
                     "title": "CIDU_Proceedings.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_220",
+            "issued": "2010-10-04",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/220/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "CIDU Proceedings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/MARLON_LEWIS_92/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/MARLON_LEWIS_92/DATA001.",
-            "issued": "1992-08-28",
-            "temporal": "1992-08-28T00:09:56Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "oceans",
-                "ocean temperature",
-                "earth science",
-                "ocean chemistry",
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
-            "identifier": "C1633360473-OB_DAAC",
             "description": "Data from 3 drifting buoys deployed in fall, 1992. Two of the buoys were air launched near 140W, -999 degrees in the Pacific Ocean, and one was deployed in Monterey Bay attached to a fixed mooring.  The fixed mooring was recovered and subjected to post-calibration.",
-            "title": "Marlon Lewis drifting buoys 1992",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMARLON_LEWIS_92%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMARLON_LEWIS_92%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Marlon_Lewis_92/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Marlon_Lewis_92/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360473-OB_DAAC",
+            "issued": "1992-08-28",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "ocean temperature",
+                "earth science",
+                "ocean chemistry",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/MARLON_LEWIS_92/DATA001",
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
+            "temporal": "1992-08-28T00:09:56Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Marlon Lewis drifting buoys 1992"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_MetNav_AircraftInSitu_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-03-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/ORACLES_MetNav_AircraftInSitu_Data_1.",
-            "issued": "2019-11-06",
-            "temporal": "2016-08-02T00:00:00Z/2018-10-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-19",
-            "keyword": [
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "earth science",
-                "atmospheric temperature"
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
-            "identifier": "C1703976402-LARC_ASDC",
             "description": "ORACLES_MetNav_AircraftInSitu_Data are in situ meteorological and navigational measurements collected onboard the P-3 Orion or ER-2 aircraft during the ObseRvations of Aerosols above CLouds and their intEractionS (ORACLES) campaign. These measurements were collected from August 19, 2016 \u2013 October 27, 2016, August 1, 2017 \u2013 September 4, 2017 and September 21, 2018 \u2013 October 27, 2018. ORACLES provides multi-year airborne observations over the complete vertical column of key parameters that drive aerosol-cloud interactions in the southeast Atlantic, an area with some of the largest inter-model differences in aerosol forcing assessments on the planet. The P-3 Orion aircraft was utilized as a low-flying platform for simultaneous in situ and remote sensing measurements of aerosols and clouds and was supplemented by ER-2 remote sensing during the 2016 campaign. Data collection for this product is complete.\r\n\r\nSouthern Africa produces almost one-third of the Earth\u2019s biomass burning aerosol particles. The ORACLES (ObseRvations of Aerosols above CLouds and their intEractionS) experiment was a five year investigation with three intensive observation periods (August 19, 2016 \u2013 October 27, 2016; August 1, 2017 \u2013 September 4, 2017; September 21, 2018 \u2013 October 27, 2018) and was designed to study key processes that determine the climate impacts of African biomass burning aerosols. ORACLES provided multi-year airborne observations over the complete vertical column of the key parameters that drive aerosol-cloud interactions in the southeast Atlantic, an area with some of the largest inter-model differences in aerosol forcing assessments. These inter-model differences in aerosol and cloud distributions, as well as their combined climatic effects in the SE Atlantic are partly due to the persistence of aerosols above clouds. The varying separation of cloud and aerosol layers sampled during ORACLES allow for a process-oriented understanding of how variations in radiative heating profiles impact cloud properties, which is expected to improve model simulations for other remote regions experience long-range aerosol transport above clouds. ORACLES utilized two NASA aircraft, the P-3 and ER-2. The P-3 was used as a low-flying platform for simultaneous in situ and remote sensing measurements of aerosols and clouds in all three campaigns, supplemented by ER-2 remote sensing in 2016. ER-2 observations will be used to enhance satellite-based remote sensing by resolving variability within a particular scene, and by guiding the development of new and improved remote sensing techniques.",
-            "title": "ORACLES Navigational and Meteorological Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FORACLES_MetNav_AircraftInSitu_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FORACLES_MetNav_AircraftInSitu_Data_1",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_MetNav_AircraftInSitu_Data_1",
-                    "description": "DOI data set landing page for ORACLES_MetNav_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ORACLES_MetNav_AircraftInSitu_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_MetNav_AircraftInSitu_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703976402-LARC_ASDC",
-                    "description": "Earthdata Search for ORACLES_MetNav_AircraftInSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ORACLES_MetNav_AircraftInSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703976402-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ORACLES/MetNav_AircraftInSitu_Data_1/",
-                    "description": "ASDC Direct Data Download for ORACLES_MetNav_AircraftInSitu_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ORACLES_MetNav_AircraftInSitu_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ORACLES/MetNav_AircraftInSitu_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1703976402-LARC_ASDC",
+            "issued": "2019-11-06",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_MetNav_AircraftInSitu_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-70.0 -77.0 -70.0 40.0 41.0 40.0 41.0 -77.0 -70.0 -77.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2016-08-02T00:00:00Z/2018-10-27T23:59:59.999Z",
             "theme": [
                 "ORACLES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ORACLES Navigational and Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3355-V1.0",
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
-                "mars express"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-20T09:20:37.000 to 2012-07-20T13:05:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3355-v1.0_4p3h-3twn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3355-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3355-v1.0_4p3h-3twn",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-20T09:20:37.000 to 2012-07-20T13:05:57.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3355 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3355 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ110_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2023-10-10. VIIRS/JPSS1 Snow Cover 6-Min L2 Swath 375m NRT. Version 2. NASA GSFC LANCE. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VJ110_NRT.002. http://doi.org/10.5067/VIIRS/VJ110_NRT.002.",
-            "issued": "2023-10-10",
-            "temporal": "2023-10-10T00:00:00Z/2023-10-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
-                "snow/ice",
-                "cryosphere",
-                "earth science"
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
-            "identifier": "C2781269342-LANCEMODIS",
-            "description": "The VJ110_NRT is Near Real Time (NRT) VIIRS/JPSS1 Snow Cover 6-Min L2 Swath 375m data set which reports the location of snow cover using radiance data acquired by the Visible Infrared Imager Radiometer Suite (VIIRS) on board the NOAA-20 - formerly the Joint Polar Satellite System-1 (JPSS-1)  satellite. Snow cover is identified using the Normalized Difference Snow Index (NDSI) and a series of quality control screens. The VNP10_NRT product is provided in NETCDF format.\r\n\r\nMore information can be find from VIIRS Land website at:\r\nhttps://viirsland.gsfc.nasa.gov/Products/NASA/SnowESDR.html",
-            "release-place": "NASA GSFC LANCE",
             "creator": "LANCEMODIS",
-            "title": "VIIRS/JPSS1 Snow Cover 6-Min L2 Swath 375m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VJ110_NRT is Near Real Time (NRT) VIIRS/JPSS1 Snow Cover 6-Min L2 Swath 375m data set which reports the location of snow cover using radiance data acquired by the Visible Infrared Imager Radiometer Suite (VIIRS) on board the NOAA-20 - formerly the Joint Polar Satellite System-1 (JPSS-1)  satellite. Snow cover is identified using the Normalized Difference Snow Index (NDSI) and a series of quality control screens. The VNP10_NRT product is provided in NETCDF format.\r\n\r\nMore information can be find from VIIRS Land website at:\r\nhttps://viirsland.gsfc.nasa.gov/Products/NASA/SnowESDR.html",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ110_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ110_NRT.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -148065,852 +148045,844 @@
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/5200/VJ110_NRT",
-                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
                     "@type": "dcat:Distribution",
+                    "description": "Access VIIRS data set from the MODAPS/NRT server.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/allData/5200/VJ110_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LANCE"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/10.5067/VIIRS/VJ110_NRT.002",
-                    "description": "Product's DOI landing page",
                     "@type": "dcat:Distribution",
+                    "description": "Product's DOI landing page",
+                    "downloadURL": "http://doi.org/10.5067/VIIRS/VJ110_NRT.002",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2781269342-LANCEMODIS",
+            "issued": "2023-10-10",
+            "keyword": [
+                "snow/ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ110_NRT.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
+            },
+            "release-place": "NASA GSFC LANCE",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-10-10T00:00:00Z/2023-10-16T00:00:00Z",
             "theme": [
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Snow Cover 6-Min L2 Swath 375m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1072-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-01T20:57:55.000 to 2015-10-02T02:14:21.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1072-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1072-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1072-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-01T20:57:55.000 to 2015-10-02T02:14:21.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1072 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1072 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-3-RADIOMETRIC-OPS-V1.0",
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
-                "phoenix",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains radiometric data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-3-radiometric-ops-v1.0_4p57-55cc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-3-RADIOMETRIC-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-3-radiometric-ops-v1.0_4p57-55cc",
-            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains radiometric data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA \n                                     3 RADIOMETRIC OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA \n                                     3 RADIOMETRIC OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/479",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jordan, C.F., E. Cuevas, and E. Medina. 2013. NPP Tropical Forest: San Carlos de Rio Negro, Venezuela, 1975-1984, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/479",
-            "issued": "2013-10-17",
-            "temporal": "1950-01-01T00:00:00Z/1984-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "biosphere",
-                "vegetation",
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
-            "identifier": "C2751946380-ORNL_CLOUD",
             "description": "This data set includes five ASCII files (.txt format). Three files contain above- and below-ground biomass and net primary productivity (NPP) data, one file for each tropical forest study site near San Carlos de Rio Negro, Venezuela. The study sites are located along an ecosystem gradient from riverine to lateritic hill: Tall Amazon Caatinga forest on coarse sandy spodosols close to river level; Bana vegetation on sandy soils less prone to flooding; and Tierra Firme mixed forest on clay oxisols of higher ground. Bioelement concentrations are also provided. The other two files contain climate data from a weather station in San Carlos village.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Tropical Forest: San Carlos de Rio Negro, Venezuela, 1975-1984, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F479",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F479",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_SCR/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_SCR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_SCR.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_SCR.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/479",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/479",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_SCR/comp/NPP_SCR.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_SCR/comp/NPP_SCR.pdf",
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
+            "identifier": "C2751946380-ORNL_CLOUD",
+            "issued": "2013-10-17",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/479",
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
             "spatial": "1.93 -67.05",
+            "temporal": "1950-01-01T00:00:00Z/1984-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Tropical Forest: San Carlos de Rio Negro, Venezuela, 1975-1984, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141690-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 FIRSTLOOK Global Aerosol product in netCDF format covering a month's products;See ProductionDateTime for Published date.",
-            "issued": "2007-07-30",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-05",
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
-            "identifier": "C156141690-LARC",
             "description": "This file contains the MISR Level 3 FIRSTLOOK Component Global Aerosol product in netCDF format covering a month",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 FIRSTLOOK Global Aerosol product in netCDF format covering a month V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141690-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141690-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C156141690-LARC",
+            "issued": "2007-07-30",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141690-LARC.html",
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
+            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 FIRSTLOOK Global Aerosol product in netCDF format covering a month V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2352",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jensen, D.J., E. Casta\u00f1eda-Moya, E. Solohin, D.R. Thompson, and M. Simard. 2024. Delta-X AVIRIS-NG L3 Derived Vegetation Types, MRD, Louisiana, USA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2352",
-            "issued": "2024-09-30",
-            "temporal": "2021-08-20T00:00:00Z/2021-08-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-02",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "earth science",
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
-            "identifier": "C3255110465-ORNL_CLOUD",
             "description": "This dataset provides maps of vegetation types for the Atchafalaya and Terrebonne basins in coastal Louisiana, U.S., derived from NASA's Next Generation Airborne Visible Infrared Imaging Spectrometer (AVIRIS-NG) imagery acquired during spring and fall of 2021 for the Delta-X campaign.  Vegetation types were classified from Level-2B BRDF-adjusted surface reflectance. Local pixel reflectance spectra coincident with herbaceous vegetation field samples and vegetation plot data from Louisiana's Coastwide Reference Monitoring System were used to generate a machine learning-based model to classify vegetation types. This model was then applied to the AVIRIS-NG mosaic imagery to map vegetation types across the Atchafalaya and Terrebonne Basins. The data are provided in cloud optimized GeoTIFF (COG) format.",
-            "graphic-preview-description": "Vegetation type classification of the Atchafalaya and Terrebonne basins derived from AVIRIS-NG.",
-            "title": "Delta-X AVIRIS-NG L3 Derived Vegetation Types, MRD, Louisiana, USA",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Veg_Types_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2352",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2352",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_L3_AVIRIS-NG_Veg_Types/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_L3_AVIRIS-NG_Veg_Types/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_L3_AVIRIS-NG_Veg_Types_2352.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_L3_AVIRIS-NG_Veg_Types_2352.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Veg_Types.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Veg_Types.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2352",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2352",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_L3_AVIRIS-NG_Veg_Types_2352.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/DeltaX_L3_AVIRIS-NG_Veg_Types_2352.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L3_AVIRIS-NG_Veg_Types/comp/DeltaX_L3_AVIRIS-NG_Veg_Types.pdf",
-                    "description": "Delta-X AVIRIS-NG L3 Derived Vegetation Types, MRD, Louisiana, USA: DeltaX_L3_AVIRIS-NG_Veg_Types.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X AVIRIS-NG L3 Derived Vegetation Types, MRD, Louisiana, USA: DeltaX_L3_AVIRIS-NG_Veg_Types.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L3_AVIRIS-NG_Veg_Types/comp/DeltaX_L3_AVIRIS-NG_Veg_Types.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Veg_Types_Fig1.png",
-                    "description": "Vegetation type classification of the Atchafalaya and Terrebonne basins derived from AVIRIS-NG.",
                     "@type": "dcat:Distribution",
+                    "description": "Vegetation type classification of the Atchafalaya and Terrebonne basins derived from AVIRIS-NG.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Veg_Types_Fig1.png",
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
+            "graphic-preview-description": "Vegetation type classification of the Atchafalaya and Terrebonne basins derived from AVIRIS-NG.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Veg_Types_Fig1.png",
+            "identifier": "C3255110465-ORNL_CLOUD",
+            "issued": "2024-09-30",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science",
+                "land use/land cover",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2352",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-91.59 28.99 -90.36 29.71",
+            "temporal": "2021-08-20T00:00:00Z/2021-08-25T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X AVIRIS-NG L3 Derived Vegetation Types, MRD, Louisiana, USA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-CFT00",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "W. Asher. 2019-07-31. SPURS-2 Controlled Flux Technique (CFT) data for the E. Tropical Pacific field campaign R/V Revelle cruises. Version 1.0. SPURS Field Campaign Rawinsonde Products. Applied Physics Laboratory, University of Washington, 1013 NE 40th St, Seattle, WA 98105. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-CFT00. http://podaac.jpl.nasa.gov/SPURS. W. Asher, SPURS Data Management PI, Fred Bingham, 2019-07-31, SPURS-2 Controlled Flux Technique (CFT) data for the E. Tropical Pacific field campaign R/V Revelle cruises, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-07-08",
-            "temporal": "2016-08-24T23:30:15Z/2017-11-11T07:48:41Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-08",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean heat budget",
-                "ocean circulation"
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
-            "identifier": "C2036882419-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. The Controlled Flux Technique (CFT) is a system for measuring the net heat transfer velocity and turbulent kinetic energy (TKE) dissipation at the ocean surface, and is a useful tool for studying the turbulence generated at the ocean surface by the impact of raindrops. CFT was employed during both SPURS-2 Revelle cruises. It involves a laser heating a small patch of water on the ocean surface, and an infrared imaging camera then tracking the resulting thermal decay.  This decay is known to be proportional to the dissipation of TKE at the water surface, which in turn can be used to scale the transfer velocity for the net heat flux. SPURS2 CFT data take the form of a series of .raw video files each with corresponding .met text header files containing the associated file metadata.  The CFT data was recorded at 15 frames per second (fps) during the first Revelle cruise in 2016, and at 25 fps during the second in 2017.  Matlab CFT reader software are provided by UW/APL and distributed here with the CFT data files.",
-            "release-place": "Applied Physics Laboratory, University of Washington, 1013 NE 40th St, Seattle, WA 98105",
-            "series-name": "SPURS-2 Controlled Flux Technique (CFT) data for the E. Tropical Pacific field campaign R/V Revelle cruises",
-            "graphic-preview-description": "Thumbnail",
             "creator": "W. Asher",
-            "title": "SPURS-2 Controlled Flux Technique (CFT) data for the E. Tropical Pacific field campaign R/V Revelle cruises",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_CFT.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. The Controlled Flux Technique (CFT) is a system for measuring the net heat transfer velocity and turbulent kinetic energy (TKE) dissipation at the ocean surface, and is a useful tool for studying the turbulence generated at the ocean surface by the impact of raindrops. CFT was employed during both SPURS-2 Revelle cruises. It involves a laser heating a small patch of water on the ocean surface, and an infrared imaging camera then tracking the resulting thermal decay.  This decay is known to be proportional to the dissipation of TKE at the water surface, which in turn can be used to scale the transfer velocity for the net heat flux. SPURS2 CFT data take the form of a series of .raw video files each with corresponding .met text header files containing the associated file metadata.  The CFT data was recorded at 15 frames per second (fps) during the first Revelle cruise in 2016, and at 25 fps during the second in 2017.  Matlab CFT reader software are provided by UW/APL and distributed here with the CFT data files.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-CFT00",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-CFT00",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2017.pdf",
-                    "description": "SPURS-2 CFT dataset documentation (2017)",
                     "@type": "dcat:Distribution",
+                    "description": "SPURS-2 CFT dataset documentation (2017)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2017.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
-                    "description": "SPURS-2 CFT dataset documentation (2016)",
                     "@type": "dcat:Distribution",
+                    "description": "SPURS-2 CFT dataset documentation (2016)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/ReadmeCFT_2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://spurs.jpl.nasa.gov/",
-                    "description": "Project Website for SPURS",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for SPURS",
+                    "downloadURL": "https://spurs.jpl.nasa.gov/",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_CFT.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_CFT.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882419-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882419-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882419-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882419-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_CFT.jpg",
+            "identifier": "C2036882419-POCLOUD",
+            "issued": "2019-07-08",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean heat budget",
+                "ocean circulation"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-CFT00",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Applied Physics Laboratory, University of Washington, 1013 NE 40th St, Seattle, WA 98105",
+            "series-name": "SPURS-2 Controlled Flux Technique (CFT) data for the E. Tropical Pacific field campaign R/V Revelle cruises",
             "spatial": "-157.88 5.06 -118.32 21.26",
+            "temporal": "2016-08-24T23:30:15Z/2017-11-11T07:48:41Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 Controlled Flux Technique (CFT) data for the E. Tropical Pacific field campaign R/V Revelle cruises"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/XI6M58U7AEDP",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Oklahoma, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/XI6M58U7AEDP.",
-            "issued": "2003-06-25",
-            "temporal": "2003-06-25T00:00:00Z/2003-07-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-17",
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
-                "earth science"
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
-            "identifier": "C1386205607-NSIDCV0",
             "description": "This data set includes brightness temperature data for the C-band and X-band of the PSR/CX band radiometer.",
-            "title": "SMEX03 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Oklahoma, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXI6M58U7AEDP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXI6M58U7AEDP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/aircraft_remote_sensing/PSR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/aircraft_remote_sensing/PSR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/aircraft_remote_sensing/PSR/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/aircraft_remote_sensing/PSR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/XI6M58U7AEDP",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/XI6M58U7AEDP",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/XI6M58U7AEDP",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/XI6M58U7AEDP",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205607-NSIDCV0",
+            "issued": "2003-06-25",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/XI6M58U7AEDP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-07-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.34 34.42 -97.42 36.87",
+            "temporal": "2003-06-25T00:00:00Z/2003-07-17T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Oklahoma, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V17.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v17.0_4pi8-aq5y",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V17.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v17.0_4pi8-aq5y",
-            "description": "This data set is intended to include all published groundbased asteroid radar detections. The file is based on the collection of asteroid radar detections established by Steven J. Ostro and currently maintained by Lance A.M. Benner. The file includes disc-integrated radar properties extracted from the published papers.",
-            "title": "ASTEROID RADAR V17.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID RADAR V17.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-REACHABILITY-OPS-V1.0",
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
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-reachability-ops-v1.0_4pih-8b3f",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-HAZCAM-5-REACHABILITY-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-hazcam-5-reachability-ops-v1.0_4pih-8b3f",
-            "description": "not applicable",
-            "title": "MER 1 MARS HAZARD AVOID CAMERA REACHABILITY RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS HAZARD AVOID CAMERA REACHABILITY RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CPEX/MODIS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kakar, Ramesh , Edward J Zipser and Shuyi  Chen.2023. Moderate Resolution Imaging Spectroradiometer (MODIS) CPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CPEX/MODIS/DATA101",
-            "issued": "2023-02-22",
-            "temporal": "2017-05-09T04:15:00Z/2017-07-16T15:49:16Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-18",
-            "keyword": [
-                "earth science",
-                "clouds",
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
-            "identifier": "C2659160181-GHRC_DAAC",
             "description": "The Moderate Resolution Imaging Spectroradiometer (MODIS) CPEX dataset includes measurements gathered by MODIS during the Convective Processes Experiment (CPEX) field campaign. The CPEX field campaign took place in the North Atlantic-Gulf of Mexico-Caribbean Sea region and conducted a total of sixteen DC-8 missions. The CPEX campaign collected data to help explain convective storm initiation, organization, growth, and dissipation in the North Atlantic-Gulf of Mexico-Caribbean Oceanic region during the early summer of 2017. Data are available from May 9, 2017 through July 16, 2017 in netCDF-3 format.",
-            "title": "Moderate Resolution Imaging Spectroradiometer (MODIS) CPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPEX%2FMODIS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPEX%2FMODIS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=modiscpex&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=modiscpex&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis.gsfc.nasa.gov/",
-                    "description": "NASA Moderate Resolution Imaging Spectroradiometer (MODIS)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Moderate Resolution Imaging Spectroradiometer (MODIS)",
+                    "downloadURL": "https://modis.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/mission_pages/terra/spacecraft/index.html",
-                    "description": "NASA Terra Spacecraft",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Terra Spacecraft",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/terra/spacecraft/index.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/CPEX/DATA101",
-                    "description": "CPEX Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/CPEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpex/MODIS/doc/modiscpex_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpex/MODIS/doc/modiscpex_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/cpex",
-                    "description": "Convective Processes Experiment (CPEX) Field Campaign Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Convective Processes Experiment (CPEX) Field Campaign Project Home Page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/cpex",
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
+            "identifier": "C2659160181-GHRC_DAAC",
+            "issued": "2023-02-22",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CPEX/MODIS/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-133.329 -15.7699 -7.96509 62.0543",
+            "temporal": "2017-05-09T04:15:00Z/2017-07-16T15:49:16Z",
             "theme": [
                 "CPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Moderate Resolution Imaging Spectroradiometer (MODIS) CPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC3-MTP019-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 3\nMTP019 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-ESC3-MTP019-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc3-mtp019-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC3-MTP019-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc3-mtp019-v2.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 3\nMTP019 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-ESC3-MTP019-V1.0.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC3 MTP019 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC3 MTP019 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/MHS/NOAA18/1C/07",
             "citation": "Wesley Berg. 2022-05-09. GPM_1CNOAA18MHS. GPM MHS on NOAA-18 Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/MHS/NOAA18/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CNOAA18MHS_07.html. Digital Science Data.",
-            "issued": "2022-05-01",
-            "temporal": "2005-05-25T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "atmosphere",
-                "earth science",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264133406-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nAll 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent. 1CMHS contains common calibrated brightness temperature from the MHS passive microwave instrument flown on the NOAA and METOPS satellites. Swath S1 is the only swath and has 5 channels (89.0GHzV, 157.0GHzV, 183.3GHz+/-250MHzH, 183.3GHz+/- 500MHzH, and 190.3 GHzV). MHS is very similar to AMSU-B. The scan period is 2.667s.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_1CNOAA18MHS",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from GPM MHS on NOAA-18 (GPM_1CNOAA18MHS)",
-            "title": "GPM MHS on NOAA-18 Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CNOAA18MHS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.NOAA18.MHS.XCAL2016-V.20150101-S010625-E024826.049548.V05A.PNG",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FNOAA18%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FNOAA18%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.NOAA18.MHS.XCAL2016-V.20150101-S010625-E024826.049548.V05A.PNG",
-                    "description": "Common Calibrated Brightness Temperature from GPM MHS on NOAA-18 (GPM_1CNOAA18MHS)",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from GPM MHS on NOAA-18 (GPM_1CNOAA18MHS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.NOAA18.MHS.XCAL2016-V.20150101-S010625-E024826.049548.V05A.PNG",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CNOAA18MHS_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CNOAA18MHS_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CNOAA18MHS.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CNOAA18MHS.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CNOAA18MHS.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L1C/GPM_1CNOAA18MHS.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CNOAA18MHS_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CNOAA18MHS_07",
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
@@ -148920,168 +148892,172 @@
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/mhs.php",
-                    "description": "Instrument Description from EUMETSAT",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from EUMETSAT",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/mhs.php",
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
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from GPM MHS on NOAA-18 (GPM_1CNOAA18MHS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/1C-BR.NOAA18.MHS.XCAL2016-V.20150101-S010625-E024826.049548.V05A.PNG",
+            "identifier": "C2264133406-GES_DISC",
+            "issued": "2022-05-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/MHS/NOAA18/1C/07",
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
+            "series-name": "GPM_1CNOAA18MHS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-05-25T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM MHS on NOAA-18 Common Calibrated Brightness Temperature L1C 1.5 hours 17 km V07 (GPM_1CNOAA18MHS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0469-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-02T01:08:30.000 to 2014-12-02T13:01:51.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0469-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0469-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0469-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-02T01:08:30.000 to 2014-12-02T13:01:51.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0469 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0469 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the 67P/Churyumov-Gerasimenko comet escort 1 mission phase, which took place between 2014-11-19 and 2015-03-10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc1-v1.0_4pw3-5bbu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "calibration",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc1-v1.0_4pw3-5bbu",
-            "description": "This data set contains CODMAC level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the 67P/Churyumov-Gerasimenko comet escort 1 mission phase, which took place between 2014-11-19 and 2015-03-10.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10000",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2024-06-01. OCO2_L1B_Calibration. Version 11.2r. OCO-2 Level 1B calibrated, geolocated calibration spectra V11.2r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10000. https://disc.gsfc.nasa.gov/datacollection/OCO2_L1B_Calibration_11.2r.html. Digital Science Data.",
-            "issued": "2024-04-01",
-            "temporal": "2019-11-30T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-01",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "atmosphere"
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
-            "identifier": "C3090453484-GES_DISC",
-            "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2r.\n\nThe Orbiting Carbon Observatory is the first NASA missiondesigned to collect space-based measurements of atmospheric carbon dioxidewith the precision, resolution, and coverage needed to characterize theprocesses controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements ofreflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and inmolecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time tothe Level 1B process as Level 1A products. Each band has 1016 spectralelements, although some are masked out in the L2 retrieval.This L1B product results from calibration mode measurements (e.g., Lunar,Solar, Dark observations), and thus it differs from the OCO2_L1B_Science(L1bSc) product. The differences in the product formats are only in the geolocation information provided. Whereas the L1bSc products report geolocation data for each sounding, calibration products report the directionof the boresight vector.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L1B_Calibration",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 1B calibrated, geolocated calibration spectra Retrospective Processing V11.2r (OCO2_L1B_Calibration) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2r.\n\nThe Orbiting Carbon Observatory is the first NASA missiondesigned to collect space-based measurements of atmospheric carbon dioxidewith the precision, resolution, and coverage needed to characterize theprocesses controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements ofreflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and inmolecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time tothe Level 1B process as Level 1A products. Each band has 1016 spectralelements, although some are masked out in the L2 retrieval.This L1B product results from calibration mode measurements (e.g., Lunar,Solar, Dark observations), and thus it differs from the OCO2_L1B_Science(L1bSc) product. The differences in the product formats are only in the geolocation information provided. Whereas the L1bSc products report geolocation data for each sounding, calibration products report the directionof the boresight vector.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10000",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10000",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -149091,150 +149067,150 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1B_Calibration_11.2r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1B_Calibration_11.2r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1B_Calibration",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L1B_Calibration",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1B_Calibration.11.2r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1B_Calibration.11.2r/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1B_Calibration.11.2r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1B_Calibration.11.2r/",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_DQ_Statement_v11.2.pdf",
-                    "description": "Data Quality document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_DQ_Statement_v11.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
+            "identifier": "C3090453484-GES_DISC",
+            "issued": "2024-04-01",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10000",
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
+            "series-name": "OCO2_L1B_Calibration",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 1B calibrated, geolocated calibration spectra Retrospective Processing V11.2r (OCO2_L1B_Calibration) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-01-12",
-            "temporal": "2021-01-12T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "ephemeris",
-                "station",
-                "trajectory",
-                "coords",
-                "space",
-                "coordinates",
-                "location",
-                "iss",
-                "topo",
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
-            "identifier": "nasa-iss-data_2021-01-12",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-01-12",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149357,112 +149333,138 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-01-12",
+            "issued": "2021-01-12",
+            "keyword": [
+                "ephemeris",
+                "station",
+                "trajectory",
+                "coords",
+                "space",
+                "coordinates",
+                "location",
+                "iss",
+                "topo",
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
+            "temporal": "2021-01-12T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-01-12"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141684-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 FIRSTLOOK Global Cloud public Product in netCDF format covering a day;See ProductionDateTime for Published date.",
-            "issued": "2007-07-30",
-            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-05",
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
-            "identifier": "C156141684-LARC",
             "description": "This file contains the public MISR Level 3 FIRSTLOOK Global Cloud public Product in netCDF format covering a day",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 FIRSTLOOK Global Cloud public Product in netCDF covering a day V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141684-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C156141684-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C156141684-LARC",
+            "issued": "2007-07-30",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C156141684-LARC.html",
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
+            "temporal": "1999-12-18T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 FIRSTLOOK Global Cloud public Product in netCDF covering a day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-FTS-3-FOOTPAD-TEMP-V1.0",
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
-                "viking"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-fts-3-footpad-temp-v1.0_4py9-iqtv",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "viking"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-FTS-3-FOOTPAD-TEMP-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-fts-3-footpad-temp-v1.0_4py9-iqtv",
-            "description": "not applicable",
-            "title": "VL1/VL2 MARS METEOROLOGY CALIBRATED FOOTPAD TEMP V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VL1/VL2 MARS METEOROLOGY CALIBRATED FOOTPAD TEMP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-MAG-2-REDR-RAW-DATA-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw magnetic field data acquired by the Galileo Orbiter magnetometer at Jupiter. The data set covers the time period from 1995-11-06T00:21:30 UT (Jupiter approach) until the end of mission (March 2003). The raw magnetometer data set includes various forms of data: recorded high time resolution, real-time survey (RTS), optimal averager (opt/avg), snapshot, and the calibration parameters required to generate processed data products. In addition corrected rotor angles and spacecraft relative clock and cone angles are provided to simplify future calibration and reprocessing of the data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-mag-2-redr-raw-data-v1.0_4pz7-cvdz",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "callisto",
                 "io",
@@ -149473,1039 +149475,1007 @@
                 "amalthea",
                 "io plasma torus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-MAG-2-REDR-RAW-DATA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-mag-2-redr-raw-data-v1.0_4pz7-cvdz",
-            "description": "This data set contains raw magnetic field data acquired by the Galileo Orbiter magnetometer at Jupiter. The data set covers the time period from 1995-11-06T00:21:30 UT (Jupiter approach) until the end of mission (March 2003). The raw magnetometer data set includes various forms of data: recorded high time resolution, real-time survey (RTS), optimal averager (opt/avg), snapshot, and the calibration parameters required to generate processed data products. In addition corrected rotor angles and spacecraft relative clock and cone angles are provided to simplify future calibration and reprocessing of the data.",
-            "title": "GALILEO ORBITER JUPITER RAW MAGNETOMETER DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO ORBITER JUPITER RAW MAGNETOMETER DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC3-67PCHURYUMOV-M20-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc3-67pchuryumov-m20-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "international rosetta mission",
                 "bias",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC3-67PCHURYUMOV-M20-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc3-67pchuryumov-m20-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 2 ESC3-MTP020 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 2 ESC3-MTP020 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DRDR_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2006-03-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Terra/MISR/MI3DRDR_L3.002. https://asdc.larc.nasa.gov/project/MISR.",
-            "issued": "2006-02-13",
-            "temporal": "2001-07-22T00:00:00Z/2007-08-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths"
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
-            "identifier": "C179031517-LARC",
             "description": "MI3DRDR_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 3 Component Global Radiance Regional public Product covering a day version 2. It contains a global summary of the Level 1 and Level 2 radiance parameters of interest averaged over a day and reported on a geographic grid, with resolution of 0.5 degree by 0.5 degree. Data collection for this product is complete. The data are for distinct regions associated with associated field campaigns. The MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward, and four cameras pointing aftward. It takes seven minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally Gaussian, centered at 443, 555, 670, and 865 nm.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Component Global Radiance Regional public Product covering a day V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DRDR_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DRDR_L3.002",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031517-LARC",
-                    "description": "Earthdata Search for MI3DRDR_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MI3DRDR_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031517-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3DRDR.002/contents.html",
-                    "description": "OPeNDAP data access for MI3DRDR_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MI3DRDR_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3DRDR.002/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf",
-                    "description": "MISR Level 3 Component Products Quality Statement - December 1, 2005",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 3 Component Products Quality Statement - December 1, 2005",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MI3DRDR_L3.002",
-                    "description": "DOI data set landing page for MI3DRDR_2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MI3DRDR_2",
+                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MI3DRDR_L3.002",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3DRDR.002/",
-                    "description": "ASDC Direct Data Download for MI3DRDR_2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MI3DRDR_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3DRDR.002/",
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
+            "identifier": "C179031517-LARC",
+            "issued": "2006-02-13",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DRDR_L3.002",
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
+            "temporal": "2001-07-22T00:00:00Z/2007-08-30T23:59:59Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Component Global Radiance Regional public Product covering a day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR1-DRIFT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SPURS PROJECT, Fred Bingham. 2015-05-11. Drifter data for the SPURS-1 N. Atlantic field campaign. Version 1.0. SPURS-1 Field Campaign Drifter Data Products. Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR1-DRIFT. http://podaac.jpl.nasa.gov/SPURS. SPURS PROJECT, Fred Bingham, SPURS Data Management PI, Fred Bingham, 2015-05-11, Drifter data for the SPURS-1 N. Atlantic field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2015-04-07",
-            "temporal": "2011-10-19T00:00:00Z/2015-04-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "earth science",
-                "oceans",
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
-            "identifier": "C2491772174-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is an oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes.  SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales.  The SPURS-1 campaign involved a series of 5 cruises during 2012 - 2013 seeking to characterize the salinity structure and balance in a high salinity, high evaporation, and low rainfall region of the subtropical North Atlantic. It aims to resolve processes responsible for maintaining the subtropical surface salinity maximum in this region and within a 900 x 800-mile square study area centered at 25N, 38W.  Approximately 83 drifters were deployed during the SPURS-1 campaign. A drifter is a passive Lagrangian sensor platform consisting of a surface buoy and tethered subsurface drogue. Drifter buoys contain GPS/ARGOS and satellite data transmitters, with sensors measuring temperature and other properties. For SPURS-1, these were standard Surface Velocity Program (SVP) drifters with salinity sensors added (SVP/S). Data for both US and European drifter deployments during SPURS-1 are available here.  For each series, drifter data have been aggregrated within single netCDF data filea with their corresponding drifter-IDs and associaciated near-surface salinity, temperaure georeferenced (GPS and ARGOS) trajectory series data.",
-            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
-            "series-name": "Drifter data for the SPURS-1 N. Atlantic field campaign",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SPURS PROJECT, Fred Bingham",
-            "title": "Drifter data for the SPURS-1 N. Atlantic field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_DRIFTER.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is an oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes.  SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales.  The SPURS-1 campaign involved a series of 5 cruises during 2012 - 2013 seeking to characterize the salinity structure and balance in a high salinity, high evaporation, and low rainfall region of the subtropical North Atlantic. It aims to resolve processes responsible for maintaining the subtropical surface salinity maximum in this region and within a 900 x 800-mile square study area centered at 25N, 38W.  Approximately 83 drifters were deployed during the SPURS-1 campaign. A drifter is a passive Lagrangian sensor platform consisting of a surface buoy and tethered subsurface drogue. Drifter buoys contain GPS/ARGOS and satellite data transmitters, with sensors measuring temperature and other properties. For SPURS-1, these were standard Surface Velocity Program (SVP) drifters with salinity sensors added (SVP/S). Data for both US and European drifter deployments during SPURS-1 are available here.  For each series, drifter data have been aggregrated within single netCDF data filea with their corresponding drifter-IDs and associaciated near-surface salinity, temperaure georeferenced (GPS and ARGOS) trajectory series data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR1-DRIFT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR1-DRIFT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/DataDocumentation/SPURS1_DataSubmissionReport.pdf",
-                    "description": "Data Submission Report, Instrument Calibration Report, etc",
                     "@type": "dcat:Distribution",
+                    "description": "Data Submission Report, Instrument Calibration Report, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/DataDocumentation/SPURS1_DataSubmissionReport.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_DRIFTER.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_DRIFTER.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/SpursWebsiteContent/Calendar/SpursCalendar.pdf",
-                    "description": "Meeting Materials, Cruise Blogs, and other archive artifacts",
                     "@type": "dcat:Distribution",
+                    "description": "Meeting Materials, Cruise Blogs, and other archive artifacts",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/SpursWebsiteContent/Calendar/SpursCalendar.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/CruiseReports/12-10_Knorr_Cruise_Report.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs1/docs/CruiseReports/12-10_Knorr_Cruise_Report.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772174-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772174-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772174-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772174-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_DRIFTER.jpg",
+            "identifier": "C2491772174-POCLOUD",
+            "issued": "2015-04-07",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR1-DRIFT",
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
+            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
+            "series-name": "Drifter data for the SPURS-1 N. Atlantic field campaign",
             "spatial": "-66.0 16.0 -28.0 35.0",
+            "temporal": "2011-10-19T00:00:00Z/2015-04-07T00:00:00Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Drifter data for the SPURS-1 N. Atlantic field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1525896153-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-06-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "2018-04-09",
-            "temporal": "2018-01-05T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-06-06",
-            "keyword": [
-                "visible wavelengths",
-                "infrared wavelengths",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere",
-                "spectral/engineering",
-                "sensor characteristics"
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
-            "identifier": "C1525896153-LARC_ASDC",
             "description": "CER_BDS_J01-FM6_Edition1-CV is the Clouds and the Earth's Radiant Energy System (CERES) Bidirectional Scans (BDS) Joint Polar Satellite System 1 (NOAA-20) Flight Model 6 (FM6) Edition1-CV data product. Data collection for this product is ongoing. \r\n\r\nNote: Edition1-CV data are for instrument validation purposes only and not suited for science publications.\r\n\r\nCER_BDS_J01-FM6_Edition1-CV is CERES geolocated and calibrated Top-of-Atmosphere (TOA) filtered radiances and other instrument data. Edition1-CV data are for instrument validation purposes only and not suited for science publications. Each CERES BDS data product contains twenty-four hours of Level-1b data for each CERES scanner instrument mounted on each spacecraft. The BDS includes samples taken in normal and short Earth scan elevation profiles in both fixed and rotating azimuth scan modes (including space, internal calibration, and solar calibration views). The BDS contains Level-0 raw (unconverted) science and instrument data as well as the geolocated converted science and instrument data. The BDS contains additional data not found in the Level-0 input file, including converted satellite position and velocity data, celestial data, converted digital status data, and parameters used in the radiance count conversion equations. \r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Bidirectional Scans JPSS-1 FM6 Edition1-CV",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1525896153-LARC_ASDC",
-                    "description": "Earthdata Search for CER_BDS_J01-FM6_Edition1-CV (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_BDS_J01-FM6_Edition1-CV (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1525896153-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_BDS_J01_Edition1-CV.pdf",
-                    "description": "Quality Summary: CERES BDS J01 (JPSS-1/NOAA-20) Edition1-CV",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES BDS J01 (JPSS-1/NOAA-20) Edition1-CV",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_BDS_J01_Edition1-CV.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_bds_SampleRead_R5-890.txt",
-                    "description": "Readme Information on the CERES BDS Data Sets",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information on the CERES BDS Data Sets",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_bds_SampleRead_R5-890.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/BDS/J01-FM6_Edition1-CV/",
-                    "description": "ASDC Direct Data Download for CER_BDS_J01-FM6_Edition1-CV",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_BDS_J01-FM6_Edition1-CV",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/BDS/J01-FM6_Edition1-CV/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/BDS/J01-FM6_Edition1-CV/contents.html",
-                    "description": "OPeNDAP data access for CER_BDS_J01-FM6_Edition1-CV",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_BDS_J01-FM6_Edition1-CV",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/BDS/J01-FM6_Edition1-CV/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1525896153-LARC_ASDC",
+            "issued": "2018-04-09",
+            "keyword": [
+                "visible wavelengths",
+                "infrared wavelengths",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere",
+                "spectral/engineering",
+                "sensor characteristics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1525896153-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-06-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-01-05T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Bidirectional Scans JPSS-1 FM6 Edition1-CV"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/792",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Freiman, T. 2005. SAFARI 2000 Modeled Tropospheric Air Mass Trajectories, Dry Season 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/792",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-14T00:00:00Z/2000-09-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-25",
-            "keyword": [
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
-            "identifier": "C2789730089-ORNL_CLOUD",
             "description": "The ETA Forecast Trajectory Model was used to produce forecasts of air-parcel trajectories twice a day at three pressure levels over seven sites in Southern Africa for the period August 14, 2000 to September 23, 2000. These sites are Durban, Middleburg, Pietersburg, and Springbok, South Africa; Maun, Botswana; Mongu, Zambia; and Windhoek, Namibia. The twice daily three-dimensional wind field (at 0000 and 1200 UTC) was used as input to the trajectory model. By integrating the vertical motion of the air parcels over a period of time, the trajectory model was able to forecast the net vertical displacement of air parcels during 12-hour periods. The resulting trajectory plots represent the three-dimensional transport of air in time and can be used to examine what is happening in the low-to-mid troposphere during flight and ground-based observations. These levels are most significant in terms of the thermodynamic structure of the troposphere, especially the stable layers and accumulation of material between and below them, as well containing the major levels of subsidence over the subcontinent. The trajectory model output and  thermodynamic profiles of the troposphere were used to position aircraft for sampling trace gases, aerosols and other species during the SAFARI 2000 field campaign and to predict regions of high aerosol and trace gas concentrations downwind.The model output data are daily forward and backward trajectory plots at 850 hPa, 700 hPa, and 500 hPa pressure levels for each location. The plots are provided as JPEG images with coordinate, date, and time stamps.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Modeled Tropospheric Air Mass Trajectories, Dry Season 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F792",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F792",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/climate_meteorology/trajectory_images/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/climate_meteorology/trajectory_images/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/trajectory_images.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/trajectory_images.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/792",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/792",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/trajectory_images/comp/all_templates.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/trajectory_images/comp/all_templates.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/trajectory_images/comp/synoptic_data.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/trajectory_images/comp/synoptic_data.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/trajectory_images/comp/trajectory_images_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/trajectory_images/comp/trajectory_images_readme.pdf",
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
+            "identifier": "C2789730089-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "earth science",
+                "atmospheric winds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/792",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "17.1 -30.0 31.0 -15.3",
+            "temporal": "2000-08-14T00:00:00Z/2000-09-23T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Modeled Tropospheric Air Mass Trajectories, Dry Season 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F13/1C/07",
             "citation": "Wesley Berg. 2021-07-29. GPM_1CF13SSMI. GPM SSMI on F13 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMI/F13/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CF13SSMI_07.html. Digital Science Data.",
-            "issued": "2021-07-21",
-            "temporal": "1995-05-03T00:00:00Z/2009-11-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-21",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "spectral/engineering",
-                "atmosphere",
-                "microwave",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264132810-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "All 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent. 1CSSMIS contains common calibrated brightness temperature from the SSMIS passive microwave instruments flown on the DMSP satellites. Swath S1 has 3 low frequency channels (19V 19H 22V). Swath S2 has 2 low frequency channels (37V 37H). Swath S3 has 4 high frequency channels (150H 183+/-1H 183+/-3H 183+/-7H). S4 has 2 high frequency channels (91V 91H). All the above frequencies are in GHz. Earth observations for all four swaths are taken during a 144o segment of the instrument rotation when SSMIS scans in the direction of foreward satellite motion. We define the spacecraft vector (v) at the center of this segment.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_1CF13SSMI",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from F13 SSMI",
-            "title": "GPM SSMI on F13 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF13SSMI) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CF13SSMI.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF13%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF13%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CF13SSMI.png",
-                    "description": "Common Calibrated Brightness Temperature from F13 SSMI",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from F13 SSMI",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CF13SSMI.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CF13SSMI_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CF13SSMI_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CF13SSMI.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CF13SSMI.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CF13SSMI_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CF13SSMI_07",
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
@@ -150515,111 +150485,122 @@
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
-                    "downloadURL": "https://www.wmo-sat.info/oscar/instruments/view/533",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://www.wmo-sat.info/oscar/instruments/view/533",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from F13 SSMI",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CF13SSMI.png",
+            "identifier": "C2264132810-GES_DISC",
+            "issued": "2021-07-21",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "spectral/engineering",
+                "atmosphere",
+                "microwave",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F13/1C/07",
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
+            "references": [
+                "https://doi.org/10.1175/JTECH-D-16-0100.1",
+                "https://doi.org/10.3390/rs10081306"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GPM_1CF13SSMI",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-05-03T00:00:00Z/2009-11-20T23:59:59.999Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSMI on F13 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF13SSMI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-MAG-4-SUMM-NLSCOORDS-12SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "INTRODUCTION:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-mag-4-summ-nlscoords-12sec-v1.0_4q8t-an7u",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "neptune",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-MAG-4-SUMM-NLSCOORDS-12SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-mag-4-summ-nlscoords-12sec-v1.0_4q8t-an7u",
-            "description": "INTRODUCTION:",
-            "title": "VG2 NEP MAG RESAMPLED SUMMARY NLS COORDINATES 12SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEP MAG RESAMPLED SUMMARY NLS COORDINATES 12SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/mariana/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-07-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "classification",
-                "algorithm",
-                "regression",
-                "mariana",
-                "hyperparameters"
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
-            "identifier": "OCIO-Fitara-126",
             "description": "Mariana is an algorithm that efficiently optimizes the hyperparameters for Support Vector Machines for regression and classification.",
-            "title": "ARC Code TI: Mariana",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150627,81 +150608,109 @@
                     "mediaType": "application/x-tar"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-126",
+            "issued": "2015-07-21",
+            "keyword": [
+                "classification",
+                "algorithm",
+                "regression",
+                "mariana",
+                "hyperparameters"
+            ],
+            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/mariana/",
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
+            "title": "ARC Code TI: Mariana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL2TCCL_L2.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2015), Terra/MISR Level 2, TOA/Cloud Classifiers, version 3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: 10.5067/Terra/MISR/MIL2TCCL_L2.003",
-            "issued": "2003-03-24",
-            "temporal": "2000-02-24T16:33:37Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-15",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Roger Davies",
                 "hasEmail": "mailto:r.davies@auckland.ac.nz"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C43677712-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 2 TOA/Cloud Classifier parameters V003 contains the Angular Signature Cloud Mask (ASCM), Regional Cloud Classifiers, Cloud Shadow Mask, and Topographic Shadow Mask, with associated data.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 2 TOA/Cloud Classifier parameters V003",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL2TCCL_L2.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMIL2TCCL_L2.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/PRODOCS/misr/Quality_Summaries/L2_Cloud_Products.html",
-                    "description": "The product quality assessment may be downloaded directly from this link",
                     "@type": "dcat:Distribution",
+                    "description": "The product quality assessment may be downloaded directly from this link",
+                    "downloadURL": "http://eosweb.larc.nasa.gov/PRODOCS/misr/Quality_Summaries/L2_Cloud_Products.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C43677712-LARC",
+            "issued": "2003-03-24",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MIL2TCCL_L2.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-10-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T16:33:37Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 2 TOA/Cloud Classifier parameters V003"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-01-Aug-05.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-627",
+            "issued": "2018-06-25",
             "keyword": [
                 "spice",
                 "pancam",
@@ -150713,488 +150722,481 @@
                 "apxs",
                 "pds"
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
-            "identifier": "NASA-627",
-            "description": "APXS, HAZCAM, MB, MI, MTES, NAVCAM, PANCAM, SPICE",
-            "title": "PDS Mars Exploration Rovers Data Release 5",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/PDS-Subscription-Service-01-Aug-05.shtml",
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
+            "title": "PDS Mars Exploration Rovers Data Release 5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/295/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
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
-            "identifier": "DASHLINK_295",
             "description": "<b>Rectangular Supercritical Wing (Ricketts)</b> - design and measured locations are provided in an Excel file <a href=\"https://c3.ndc.nasa.gov/dashlink/static/media/dataset/RSW_airfoil_coordinates_ricketts.xls\">RSW_airfoil_coordinates_ricketts.xls</a> .  One sheet is with Non dimensional coordinates (RSW-nd) to be able to compare with other supercritical airfoils.  The other sheet (RectSupercriticalWing) has the data which should be used to generate the grids.\r\n\r\n<b>Benchmark Supercritical Wing</b> are available in PDF file of tables. The data was OCR'd.   Matlab code was written to read data line by line to be able to extract the data.  The \"*\" flag associated with points that have deviation greater the specified value were replaced with blank space.  Bad lines were omitted - lines that have non-numerical digits.  \r\n\r\n\r\nComparison of Rectangular Supercritical Wing (Ricketts), Benchmark Supercritical Wing, MBB_A3\r\n\r\n<img src=\"https://c3.ndc.nasa.gov/dashlink/static/media/dataset/SCWairfoils.png\">\r\n\r\n2D Airfoil tested at DLR - comparison of theoretical and actual.\r\n<img src=\"\r\nhttps://c3.ndc.nasa.gov/dashlink/static/media/dataset/mbb_a3.png\" height=200>",
-            "title": "Supercritical Airfoil Coordinates",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/vnd.ms-excel",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_airfoil_coordinates_ricketts.xls",
-                    "description": "RSW Airfoil Coordinates of model tested in 1980's by Ricketts",
                     "@type": "dcat:Distribution",
+                    "description": "RSW Airfoil Coordinates of model tested in 1980's by Ricketts",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW_airfoil_coordinates_ricketts.xls",
+                    "mediaType": "application/vnd.ms-excel",
                     "title": "RSW_airfoil_coordinates_ricketts.xls"
                 },
                 {
-                    "mediaType": "application/vnd.ms-excel",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AirfoilCoordinatesComparison.xls",
-                    "description": "Compares RSW(Ricketts), BSW, MBB_A3",
                     "@type": "dcat:Distribution",
+                    "description": "Compares RSW(Ricketts), BSW, MBB_A3",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/AirfoilCoordinatesComparison.xls",
+                    "mediaType": "application/vnd.ms-excel",
                     "title": "AirfoilCoordinatesComparison.xls"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/SCWairfoils.png",
-                    "description": "All 3 airfoil sections",
                     "@type": "dcat:Distribution",
+                    "description": "All 3 airfoil sections",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/SCWairfoils.png",
+                    "mediaType": "image/png",
                     "title": "SCWairfoils.png"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/mbb_a3.png",
-                    "description": "MBB_A3 coordinates - theoretical and actual comparison",
                     "@type": "dcat:Distribution",
+                    "description": "MBB_A3 coordinates - theoretical and actual comparison",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/mbb_a3.png",
+                    "mediaType": "image/png",
                     "title": "mbb_a3.png"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_295",
+            "issued": "2011-02-02",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/295/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Supercritical Airfoil Coordinates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-MAWD-4-V1.0",
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
-                "viking"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of the raster-averaged radiant intensities and associated data parameters produced from data acquired by the Mars Atmospheric Water Detectors (MAWD) onboard the Viking Orbiters. The basic observations give temporal coverage spanning just over two martian years and variable, but extensive, spatial coverage of the planet. MAWD was a five-channel grating spectrometer measuring solar radiation reflected from the surface and atmosphere of Mars in and out of water vapor bands in the 1.4 micrometer spectral interval. The data set described here contains the solar reflected radiant intensities (i.e., radiances) measured by MAWD, derived water vapor column abundances, a derived '1.4-micrometer brightness', and ancillary data (e.g., viewing geometry, surface elevation and air mass). Column water vapor abundances were derived by comparing the reflected radiant intensities in three water vapor absorption bands to radiant intensities in the two interspersed continua observed air mass and then normalized by the air mass to obtain a vertical column abundance. A basic description of the instrument, its observational modes and its derived data products is given in [FARMER_ETAL_1977]. A description of the global and seasonal variation of water vapor on Mars, based on the complete MAWD observational record, is given in [JAKOSKY_FARMER_1982]. This data set was generated from the raster-level data base constructed during the Viking Mission on the original data processing system (IRPS: Infrared Processing System) by the MAWD Science Team, led by C. B. Farmer, JPL. Together with the instantaneous field of view (IFOV) radiances and geometry, the raster-level radiances, associated water column abundances and ancillary data have been archived at the NSSDC (NSSDC id 75-075A-03A, 75-083A-03A). Data from the final phase of the VO-1 mission were added, supervised by R. Zurek, JPL. Eventually, the data set was restructured, additional quality flags were introduced, and a second estimate of the water vapor column abundance (WFAPT, termed COLUMN_H2O_A in the data set) was added [by R. Zurek, JPL [JAKOSKY_ETAL_1988].]. The data base was restructured, while preserving key unique parameters, into a consistent format with the Viking Orbiter Infrared Thermal Mapper (IRTM) data [R. Mehlman, R. Zurek]. Both the MAWD and IRTM data sets were then accessible with the XXFUNC package. Further quality checking of the MAWD data was carried out by B. Jakosky, U. Colorado.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-mawd-4-v1.0_4qcq-qd8s",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "viking"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-MAWD-4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-mawd-4-v1.0_4qcq-qd8s",
-            "description": "This data set consists of the raster-averaged radiant intensities and associated data parameters produced from data acquired by the Mars Atmospheric Water Detectors (MAWD) onboard the Viking Orbiters. The basic observations give temporal coverage spanning just over two martian years and variable, but extensive, spatial coverage of the planet. MAWD was a five-channel grating spectrometer measuring solar radiation reflected from the surface and atmosphere of Mars in and out of water vapor bands in the 1.4 micrometer spectral interval. The data set described here contains the solar reflected radiant intensities (i.e., radiances) measured by MAWD, derived water vapor column abundances, a derived '1.4-micrometer brightness', and ancillary data (e.g., viewing geometry, surface elevation and air mass). Column water vapor abundances were derived by comparing the reflected radiant intensities in three water vapor absorption bands to radiant intensities in the two interspersed continua observed air mass and then normalized by the air mass to obtain a vertical column abundance. A basic description of the instrument, its observational modes and its derived data products is given in [FARMER_ETAL_1977]. A description of the global and seasonal variation of water vapor on Mars, based on the complete MAWD observational record, is given in [JAKOSKY_FARMER_1982]. This data set was generated from the raster-level data base constructed during the Viking Mission on the original data processing system (IRPS: Infrared Processing System) by the MAWD Science Team, led by C. B. Farmer, JPL. Together with the instantaneous field of view (IFOV) radiances and geometry, the raster-level radiances, associated water column abundances and ancillary data have been archived at the NSSDC (NSSDC id 75-075A-03A, 75-083A-03A). Data from the final phase of the VO-1 mission were added, supervised by R. Zurek, JPL. Eventually, the data set was restructured, additional quality flags were introduced, and a second estimate of the water vapor column abundance (WFAPT, termed COLUMN_H2O_A in the data set) was added [by R. Zurek, JPL [JAKOSKY_ETAL_1988].]. The data base was restructured, while preserving key unique parameters, into a consistent format with the Viking Orbiter Infrared Thermal Mapper (IRTM) data [R. Mehlman, R. Zurek]. Both the MAWD and IRTM data sets were then accessible with the XXFUNC package. Further quality checking of the MAWD data was carried out by B. Jakosky, U. Colorado.",
-            "title": "VO1/VO2 MARS ATMOSPHERIC WATER DETECTOR 4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VO1/VO2 MARS ATMOSPHERIC WATER DETECTOR 4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD04_L2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Aqua Aerosol 5-Min L2 Swath 10km. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MYD04_L2.061. https://doi.org/10.5067/MODIS/MYD04_L2.061.",
-            "issued": "2017-10-01",
-            "temporal": "2002-07-04T00:45:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "atmospheric radiation",
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
-            "identifier": "C1443533683-LAADS",
-            "description": "The MODIS/Aqua Aerosol 5-Min L2 Swath 10km product (MYD04_L2) provides full global coverage of aerosol properties from the Dark Target (DT) and Deep Blue (DB) algorithms. The DT algorithm is applied over ocean and dark land (e.g., vegetation), while the DB algorithm now covers the entire land areas including both dark and bright surfaces. Both results are provided on a 10x10 pixel scale (10 km at nadir). Each MYD04_L2 product file covers a five-minute time interval. The output grid is 135 pixels in width by 203 pixels in length. Every tenth file has an output grid size of 135 by 204 pixels. MYD04_L2 product files are stored in Hierarchical Data Format (HDF-EOS).\r\n\r\nThe new Collection 6.1 (C61) MYD04_L2 product is an improved version based on algorithm changes in Dark Target (DT) Aerosol retrieval over urban areas and uncertainty estimates for Deep Blue (DB) Aerosol retrievals.\r\n\r\nThe MODIS level-2 atmospheric aerosol product provides retrieved ambient aerosol optical properties, quality assurance, and other parameters, globally over ocean and land. In Collection 5 and in earlier collections, there was only one aerosol product (MYD04_L2) at 10km (at nadir) spatial resolution. Starting from C6, the Dark Target (DT) Aerosol algorithm team provided a new 3 km spatial resolution product (MYD04_3k) intended for the air quality community.\r\n\r\n\r\nFor more information visit the MODIS Atmosphere website at:\r\nhttps://modis-atmos.gsfc.nasa.gov/products/aerosol\r\n\r\nAnd, for C6.1 changes and updates, visit:\r\nhttps://modis-atmosphere.gsfc.nasa.gov/documentation/collection-61",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Aerosol 5-Min L2 Swath 10km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Aerosol 5-Min L2 Swath 10km product (MYD04_L2) provides full global coverage of aerosol properties from the Dark Target (DT) and Deep Blue (DB) algorithms. The DT algorithm is applied over ocean and dark land (e.g., vegetation), while the DB algorithm now covers the entire land areas including both dark and bright surfaces. Both results are provided on a 10x10 pixel scale (10 km at nadir). Each MYD04_L2 product file covers a five-minute time interval. The output grid is 135 pixels in width by 203 pixels in length. Every tenth file has an output grid size of 135 by 204 pixels. MYD04_L2 product files are stored in Hierarchical Data Format (HDF-EOS).\r\n\r\nThe new Collection 6.1 (C61) MYD04_L2 product is an improved version based on algorithm changes in Dark Target (DT) Aerosol retrieval over urban areas and uncertainty estimates for Deep Blue (DB) Aerosol retrievals.\r\n\r\nThe MODIS level-2 atmospheric aerosol product provides retrieved ambient aerosol optical properties, quality assurance, and other parameters, globally over ocean and land. In Collection 5 and in earlier collections, there was only one aerosol product (MYD04_L2) at 10km (at nadir) spatial resolution. Starting from C6, the Dark Target (DT) Aerosol algorithm team provided a new 3 km spatial resolution product (MYD04_3k) intended for the air quality community.\r\n\r\n\r\nFor more information visit the MODIS Atmosphere website at:\r\nhttps://modis-atmos.gsfc.nasa.gov/products/aerosol\r\n\r\nAnd, for C6.1 changes and updates, visit:\r\nhttps://modis-atmosphere.gsfc.nasa.gov/documentation/collection-61",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD04_L2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD04_L2.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD04_L2.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD04_L2.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYD04_L2--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYD04_L2--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD04_L2/",
-                    "description": "Direct access to MYD04_L2 C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MYD04_L2 C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD04_L2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYD04_L2/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYD04_L2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1443533683-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "atmospheric radiation",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD04_L2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:45:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Aerosol 5-Min L2 Swath 10km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-ASI-3-ENTRY-V1.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set is most accurately described in [SEIFFETAL1996]:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-asi-3-entry-v1.0_4qh5-77qb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-ASI-3-ENTRY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-asi-3-entry-v1.0_4qh5-77qb",
-            "description": "This data set is most accurately described in [SEIFFETAL1996]:",
-            "title": "GALILEO PROBE ASI RAW DATA SET",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO PROBE ASI RAW DATA SET"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-CRS-5-SUMM-FLUX-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-crs-5-summ-flux-v1.0_4qiy-9b8y",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-CRS-5-SUMM-FLUX-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-crs-5-summ-flux-v1.0_4qiy-9b8y",
-            "description": "not applicable",
-            "title": "VG1 JUP CRS DERIVED PROTON/ION/ELECTRON FLUX BROWSE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 JUP CRS DERIVED PROTON/ION/ELECTRON FLUX BROWSE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2ANC.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-08-22. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2ANC.008. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-08-22T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmosphere",
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
-            "identifier": "C1619005021-LARC",
             "description": "TL2ANC_8 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Ancillary Version 8 product . TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. For this product, the geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updates the atmospheric parameters. L2 standard product files include information for one molecular species (or temperature) for an entire global survey or special observation run. \r\rA global survey consisted of a maximum of 16 consecutive orbits. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consisted of four files, where each file was composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. A Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMR), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. \r\rEach TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals were not reported. The organization of data within the Swath object was based on a superset of the UARS pressure levels used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus, in the Standard Product files each observation could have contained estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels were not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altitudes below the cloud top or surface, where measurements were not possible, a fill value was applied. \r\rTo minimize the duplication of information between the individual species standard products, data fields common to each species (such as spacecraft coordinates, emissivity, and other data fields) have been collected into a separate standard product, termed the TES L2 Ancillary Data product (ESDT short name: TL2ANC).",
-            "title": "TES/Aura L2 Ancillary Product V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2ANC.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2ANC.008",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/TES",
-                    "description": "ASDC Data and Information for TES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for TES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/TES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
-                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L2_ReadSoftware.tar",
-                    "description": "TES Level 2 Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 2 Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/read_software/TES_L2_ReadSoftware.tar",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2ANC.008",
-                    "description": "DOI data set landing page for TL2ANC_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2ANC_8",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2ANC.008",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2ANC.008/contents.html",
-                    "description": "OPeNDAP data access for TL2ANC_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2ANC_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2ANC.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1619005021-LARC",
-                    "description": "Earthdata Search for TL2ANC_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2ANC_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1619005021-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2ANC.008/",
-                    "description": "ASDC Direct Data Download for TL2ANC_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2ANC_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2ANC.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
-                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
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
+            "identifier": "C1619005021-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2ANC.008",
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
+            "title": "TES/Aura L2 Ancillary Product V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-Y%2FM-SPI-2-UVEDR-RAWXCRU%2FMARS-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Mars Express SPICAM level 0A UV data set contains raw measurements from the ultra violet SPICAM spectrometer collected during the cruise and MARS phases",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-y-m-spi-2-uvedr-rawxcru-mars-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "mars express",
@@ -151207,36 +151209,46 @@
                 "comet",
                 "deimos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-Y%2FM-SPI-2-UVEDR-RAWXCRU%2FMARS-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-y-m-spi-2-uvedr-rawxcru-mars-v2.0",
-            "description": "The Mars Express SPICAM level 0A UV data set contains raw measurements from the ultra violet SPICAM spectrometer collected during the cruise and MARS phases",
-            "title": "MEX SPICAM CRUISE/MARS UV\n                                      EDR-RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MEX SPICAM CRUISE/MARS UV\n                                      EDR-RAW V2.0"
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
+            "description": "This catalog of LAT sources above 10 GeV reports the locations, spectra, and variability properties of the 514 sources significantly detected in this range during the first three years of the Fermi mission. Many of these sources are already included in the 2FGL catalog, although in that catalog their characterization is dominated by the much larger numbers of gamma rays detected in the energy range 0.1 to 10 GeV.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/photthresh_P7v6clean_3years_100GeV.fits",
+                    "mediaType": "image/fits"
+                }
+            ],
+            "identifier": "NASA-0000220__4",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "bursts",
                 "acd",
@@ -151254,43 +151266,42 @@
                 "gro",
                 "gssc"
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
-            "identifier": "NASA-0000220__4",
-            "description": "This catalog of LAT sources above 10 GeV reports the locations, spectra, and variability properties of the 514 sources significantly detected in this range during the first three years of the Fermi mission. Many of these sources are already included in the 2FGL catalog, although in that catalog their characterization is dominated by the much larger numbers of gamma rays detected in the energy range 0.1 to 10 GeV.",
-            "title": "First Fermi-LAT Catalog of Sources above 10 GeV (1FHL)",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/1FHL/photthresh_P7v6clean_3years_100GeV.fits",
-                    "mediaType": "image/fits"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "First Fermi-LAT Catalog of Sources above 10 GeV (1FHL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/4qqq-u94f",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmclay-prov-v2-02_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000169",
             "issued": "2018-06-25",
-            "temporal": "2008-09-14/2010-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "radiation",
                 "eos",
@@ -151300,200 +151311,191 @@
                 "atmospheric science",
                 "aerosol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/4qqq-u94f",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000169",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 5 km Cloud Layer Data V2-02",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmclay-prov-v2-02_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-09-14/2010-03-28",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 5 km Cloud Layer Data V2-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-2HSNTR-F08",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2023-07-31. Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NTC Ocean Surface Topography F08. Version F08. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-2HSNTR-F08.",
-            "issued": "2023-02-18",
-            "temporal": "2020-11-30T00:00:00Z/2024-12-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "sea surface topography",
-                "oceans",
-                "earth science",
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
-            "identifier": "C2619443963-POCLOUD",
-            "description": "Provides L2 high resolution (HR) non-time critical (NTC; 60-day latency) altimetry from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft. It contains Sea Surface Height (SSH), Sea Surface Height Anomalies (SSHA) and Significant Wave Height (SWH), along with 1 Hz and 20 Hz Ku-band measurements processed from L1B altimetry including the range, orbital altitude, time, and water vapour. It also includes altimetry corrections, significant wave height and wind-speed from the AMR-C. This standard product release provides the geophysical parameters at both 1 and 20 Hz. The S6A NTC product is analogous to the Jason-3 GDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NTC Ocean Surface Topography F08",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides L2 high resolution (HR) non-time critical (NTC; 60-day latency) altimetry from the Poseidon-4 SAR altimeter on the Sentinel-6A Michael Freilich spacecraft. It contains Sea Surface Height (SSH), Sea Surface Height Anomalies (SSHA) and Significant Wave Height (SWH), along with 1 Hz and 20 Hz Ku-band measurements processed from L1B altimetry including the range, orbital altitude, time, and water vapour. It also includes altimetry corrections, significant wave height and wind-speed from the AMR-C. This standard product release provides the geophysical parameters at both 1 and 20 Hz. The S6A NTC product is analogous to the Jason-3 GDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2HSNTR-F08",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2HSNTR-F08",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619443963-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2619443963-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619443963-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2619443963-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_HR_STD_OST_NTC_F08.jpg",
+            "identifier": "C2619443963-POCLOUD",
+            "issued": "2023-02-18",
+            "keyword": [
+                "sea surface topography",
+                "oceans",
+                "earth science",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-2HSNTR-F08",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-04",
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
+            "temporal": "2020-11-30T00:00:00Z/2024-12-09T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter High Resolution (HR) NTC Ocean Surface Topography F08"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ROSINA-2-CR4B-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set present engineering data of the COPS and DFMS ROSINA sensors during the S/C Themal Characterization test- Cruise 4-2 phase. Version 2.0 contains significant corrections to the V1.0 data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rosina-2-cr4b-v2.0_4qvx-jf39",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "unknown",
@@ -151502,360 +151504,336 @@
                 "2867 steins",
                 "21 lutetia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ROSINA-2-CR4B-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rosina-2-cr4b-v2.0_4qvx-jf39",
-            "description": "This data set present engineering data of the COPS and DFMS ROSINA sensors during the S/C Themal Characterization test- Cruise 4-2 phase. Version 2.0 contains significant corrections to the V1.0 data set.",
-            "title": "ROSETTA-ORBITER CHECK ROSINA 2 CR4B V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK ROSINA 2 CR4B V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-3-EAR2-CALIBRATED-V9.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the SECOND EARTH\nSWINGBY (EAR2) of the ROSETTA orbiter magnetometer RPCMAG.\nThe closest approach (CA) took place on November 13, 2007 at 20:57.\nIncluded are data of the Active Checkout 6 in September 2007  and  the Passive\nCheckout PC7 in January 2008.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-3-ear2-calibrated-v9.0_4qw2-yje9",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "earth",
                 "checkout"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-3-EAR2-CALIBRATED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-3-ear2-calibrated-v9.0_4qw2-yje9",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the SECOND EARTH\nSWINGBY (EAR2) of the ROSETTA orbiter magnetometer RPCMAG.\nThe closest approach (CA) took place on November 13, 2007 at 20:57.\nIncluded are data of the Active Checkout 6 in September 2007  and  the Passive\nCheckout PC7 in January 2008.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 3 EAR2 CALIBRATED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 3 EAR2 CALIBRATED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1418-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-12T02:57:25.000 to 2016-02-12T12:05:38.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1418-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1418-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1418-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-12T02:57:25.000 to 2016-02-12T12:05:38.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1418 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1418 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0743-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-01T09:35:40.000 to 2015-05-01T12:13:01.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0743-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0743-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0743-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-01T09:35:40.000 to 2015-05-01T12:13:01.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0743 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0743 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD11A2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Zhengming Wan, Simon Hook, Glynn Hulley. 2021-02-04. MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD11A2.061. https://doi.org/10.5067/MODIS/MOD11A2.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-04",
-            "temporal": "2000-02-18T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-04",
-            "keyword": [
-                "surface thermal properties",
-                "national geospatial data asset",
-                "land surface",
-                "earth science",
-                "surface radiative properties",
-                "ngda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Zhengming Wan",
                 "hasEmail": "mailto:sadashiva.devadiga-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2269056084-LPCLOUD",
-            "description": "The MOD11A2 Version 6.1 product provides an average 8-day per-pixel Land Surface Temperature and Emissivity (LST&E) with a 1 kilometer (km) spatial resolution in a 1,200 by 1,200 km grid. Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 (https://doi.org/10.5067/MODIS/MOD11A1.006) LST pixels collected within that 8-day period. The 8-day compositing period was chosen because twice that period is the exact ground track repeat period of the Terra and Aqua platforms. Provided along with the daytime and nighttime surface temperature bands are associated quality control assessments, observation times, view zenith angles, and clear-sky coverages along with bands 31 and 32 emissivities from land cover types.\r\n\r\nValidation at stage 2 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for all MODIS Land Surface Temperature and Emissivity products. Further details regarding MODIS land product validation for the MOD11 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD11). \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Zhengming Wan, Simon Hook, Glynn Hulley",
-            "title": "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2343744123-LPCLOUD?h=500&w=500",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MOD11A2 Version 6.1 product provides an average 8-day per-pixel Land Surface Temperature and Emissivity (LST&E) with a 1 kilometer (km) spatial resolution in a 1,200 by 1,200 km grid. Each pixel value in the MOD11A2 is a simple average of all the corresponding MOD11A1 (https://doi.org/10.5067/MODIS/MOD11A1.006) LST pixels collected within that 8-day period. The 8-day compositing period was chosen because twice that period is the exact ground track repeat period of the Terra and Aqua platforms. Provided along with the daytime and nighttime surface temperature bands are associated quality control assessments, observation times, view zenith angles, and clear-sky coverages along with bands 31 and 32 emissivities from land cover types.\r\n\r\nValidation at stage 2 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for all MODIS Land Surface Temperature and Emissivity products. Further details regarding MODIS land product validation for the MOD11 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD11). \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD11A2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD11A2.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD11A2.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD11A2.061",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD11A2.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD11A2.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2269056084-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2269056084-LPCLOUD",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD11A2.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD11A2.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf",
-                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Theoretical Basis Document (ATBD) describes the physical and mathematical algorithms for the product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/715/MOD11_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD11A2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD11A2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD11",
-                    "description": "Further details regarding MODIS land product validation for the MOD11 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MOD11 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD11",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 2 has been achieved for all MODIS Land Surface Temperature and Emissivity products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 2 has been achieved for all MODIS Land Surface Temperature and Emissivity products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=terra&ver=C6",
-                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assessment provides information regarding the usability and usefulness of the data product.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=terra&ver=C6",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2343744123-LPCLOUD?h=500&w=500",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2343744123-LPCLOUD?h=500&w=500",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2343744123-LPCLOUD?h=500&w=500",
+            "identifier": "C2269056084-LPCLOUD",
+            "issued": "2021-02-04",
+            "keyword": [
+                "surface thermal properties",
+                "national geospatial data asset",
+                "land surface",
+                "earth science",
+                "surface radiative properties",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD11A2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-18T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/180/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kanishka Bhaduri",
                 "hasEmail": "mailto:kanishka.bhaduri-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_180",
             "description": "In a large network of computers or wireless sensors, each of the components (henceforth, peers) has some data about the global state of the system. Much of the system's functionality such as message routing, information retrieval and load sharing relies on modeling the global state. We refer to the outcome of the function (e.g., the load experienced by each peer) as the emph{model} of the system. Since the state of the system is constantly changing, it is necessary to keep the models up-to-date. Computing global data mining models e.g. decision trees, k-means clustering in large distributed systems may be very costly due to the scale of the system and due to communication cost, which may be high. The cost further increases in a dynamic scenario when the data changes rapidly. In this paper we describe a two step approach for dealing with these costs. First, we describe a highly efficient emph{local} algorithm which can be used to monitor a wide class of data mining models. Then, we use this algorithm as a feedback loop for the monitoring of complex functions of the data such as its k-means clustering. The theoretical claims are corroborated with a thorough experimental analysis.",
-            "title": "A Generic Local Algorithm for Mining Data Streams in Large Distributed Systems",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/L2_Journal_2.pdf",
-                    "description": "L2_Journal_2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "L2_Journal_2.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/L2_Journal_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "L2_Journal_2.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_180",
+            "issued": "2010-09-22",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/180/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Generic Local Algorithm for Mining Data Streams in Large Distributed Systems"
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
-                "safety",
-                "incident",
-                "aviation",
-                "arrival",
-                "rnav"
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
-            "identifier": "NASA-824",
             "description": "A sampling of reports that reference RNAV Arrival related incidents.",
-            "title": "Aviation Safety Reporting System: RNAV Arrival Reports",
-            "programCode": [
-                "026:021"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -151863,364 +151841,362 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-824",
+            "issued": "2018-06-25",
+            "keyword": [
+                "safety",
+                "incident",
+                "aviation",
+                "arrival",
+                "rnav"
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
+            "title": "Aviation Safety Reporting System: RNAV Arrival Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D54.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band3 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D54.061. https://doi.org/10.5067/MODIS/MCD43D54.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C2540273075-LPCLOUD",
-            "description": "The MCD43D54 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D54 is the white-sky albedo for MODIS band 3. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band3 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D54 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D54 is the white-sky albedo for MODIS band 3. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D54.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D54.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D54.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D54.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273075-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273075-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D54.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D54.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D54",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D54",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D54.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D54.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540273075-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "national geospatial data asset",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D54.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band3 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4ZG6QBX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Meiyappan, P., P. S. Roy, A. Soliman, T. Li, P. Mondal, S. Wang, and A. K. Jain. 2018-03-30. India Village-Level Geospatial Socio-Economic Data Set: 1991, 2001. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4ZG6QBX. https://doi.org/10.7927/H4CN71ZJ.",
-            "issued": "2018-03-30",
-            "temporal": "1991-01-01T00:00:00Z/2001-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-03-30",
-            "references": [
-                "https://doi.org/10.1007/s10113-016-1068-2",
-                "https://doi.org/10.7927/H43776SR"
-            ],
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "socioeconomics"
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
-            "identifier": "C1513253831-SEDAC",
-            "description": "The India Village-Level Geospatial Socio-Economic Data Set: 1991, 2001 is a compilation of the finest level of administrative boundaries in India (village/town-level) and over 200 socio-economic variables collected during the Indian Census in 1991 and 2001. This data set was developed by digitizing village/town level boundaries from the official analog maps published by the Survey of India for 2001. This data set also utilized tabular data for 1991 and 2001 from the Primary Census Abstract (PCA) and Village Directory (VD) data series of the Indian census. The data are in UTM 44N projection and are distributed primarily as shapefiles. Separate files are provided for each of the 28 states (number of states during 1991 and 2001 census) and combined Union Territories for 1991 and 2001.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Meiyappan, P., P. S. Roy, A. Soliman, T. Li, P. Mondal, S. Wang, and A. K. Jain",
-            "title": "India Village-Level Geospatial Socio-Economic Data Set: 1991, 2001",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The India Village-Level Geospatial Socio-Economic Data Set: 1991, 2001 is a compilation of the finest level of administrative boundaries in India (village/town-level) and over 200 socio-economic variables collected during the Indian Census in 1991 and 2001. This data set was developed by digitizing village/town level boundaries from the official analog maps published by the Survey of India for 2001. This data set also utilized tabular data for 1991 and 2001 from the Primary Census Abstract (PCA) and Village Directory (VD) data series of the Indian census. The data are in UTM 44N projection and are distributed primarily as shapefiles. Separate files are provided for each of the 28 states (number of states during 1991 and 2001 census) and combined Union Territories for 1991 and 2001.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4ZG6QBX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4ZG6QBX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/india/india-india-village-level-geospatial-socio-econ-1991-2001/india-india-village-level-geospatial-socio-econ-1991-2001-female-literates-gj-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/india/india-india-village-level-geospatial-socio-econ-1991-2001/india-india-village-level-geospatial-socio-econ-1991-2001-female-literates-gj-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/india-india-village-level-geospatial-socio-econ-1991-2001/maps",
+            "identifier": "C1513253831-SEDAC",
+            "issued": "2018-03-30",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "socioeconomics"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4ZG6QBX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-03-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.1007/s10113-016-1068-2",
+                "https://doi.org/10.7927/H43776SR"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "68.106253 8.083816 89.150397 37.073831",
+            "temporal": "1991-01-01T00:00:00Z/2001-12-31T00:00:00Z",
             "theme": [
                 "INDIA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "India Village-Level Geospatial Socio-Economic Data Set: 1991, 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-2-EDR-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-2-edr-ops-v1.0_4ri7-k58u",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-2-EDR-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-2-edr-ops-v1.0_4ri7-k58u",
-            "description": "NULL",
-            "title": "MER 1 MARS NAVIGATION CAMERA EDR\n                                      OPS VERSION 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS NAVIGATION CAMERA EDR\n                                      OPS VERSION 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/MHS/NOAA19/GPROFCLIM/2A/07",
             "citation": "GPM Science Team. 2022-05-09. GPM_2AGPROFNOAA19MHS_CLIM. Version 07. GPM MHS on NOAA-19 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/MHS/NOAA19/GPROFCLIM/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNOAA19MHS_CLIM_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2009-02-12T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "earth science",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHRISTIAN KUMMEROW",
                 "hasEmail": "mailto:kummerow@atmos.colostate.edu"
             },
+            "creator": "GPM Science Team",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264134366-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions are no longer available and have been superseded by Version 07.\n\nThe \"CLIM\"  products differ from their \"regular\" counterparts (without the \"CLIM\" in the name) by the ancillary data they use. They are Climate-Reference products, which requires homogeneous ancillary data over the climate time series.  Hence, the ECMWF-Interim (European Centre for Medium-Range Weather Forecasts, 2-3 months lag behind the regular production) reanalysis is used as ancillary data to derive surface and atmospheric conditions required by the GPROF algorithm for the \"CLIM\" output. The GPROF databases are also adjusted accordingly for these climate-referenced retrievals.\n\nThe 2AGPROF (also known as, GPM GPROF (Level 2)) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors: GMI, SSMI (DMSP F15), SSMIS (DMSP F16, F17, F18) AMSR2 (GCOM-W1), TMI MHS (NOAA 18&19, METOP A&B), ATMS (NPP), SAPHIR (MT1) This provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are near-realtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. The NRT product uses GANAL forecast fields. Standard products use the GANAL analysis product, while the climate product uses ECMWF reanalysis in order to allow for consistent data records with earlier missions. These earlier data may be archived separately. The main strength of the product is the large sampling provided. The GPM radiometer algorithms are Bayesian-type algorithms. These algorithms search an a-priori database of potential rain profiles and retrieve a weighted average of these entries based upon the proximity of the observed brightness temperature (Tb) to the simulated Tb corresponding to each rain profile. By using the same a-priori database of rain profiles, with appropriate simulated Tb for each constellation sensor, the Bayesian method is completely parametric and thus well suited for GPM's constellation approach. The a-priori information will be supplied by the combined algorithm supplied by GPM's core satellite as soon after launch as feasible. Databases for V0 of the algorithm had to be constructed from various sources as described in the ATBD. The solution provides a mean rain rate as well as the vertical structure of cloud and precipitation hydrometeors and their uncertainty.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_2AGPROFNOAA19MHS_CLIM",
-            "creator": "GPM Science Team",
-            "title": "GPM MHS on NOAA-19 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA19MHS_CLIM) at GES DISC",
-            "graphic-preview-description": "Surface Precipitation from GPM MHS on NOAA-19 GPROF (17 km x 17 km) (GPM_2AGPROFNOAA19MHS)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFNOAA19MHS_CLIM_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FNOAA19%2FGPROFCLIM%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FMHS%2FNOAA19%2FGPROFCLIM%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFNOAA19MHS_CLIM_07.png",
-                    "description": "Surface Precipitation from GPM MHS on NOAA-19 GPROF (17 km x 17 km) (GPM_2AGPROFNOAA19MHS)",
                     "@type": "dcat:Distribution",
+                    "description": "Surface Precipitation from GPM MHS on NOAA-19 GPROF (17 km x 17 km) (GPM_2AGPROFNOAA19MHS)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFNOAA19MHS_CLIM_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNOAA19MHS_CLIM_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFNOAA19MHS_CLIM_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFNOAA19MHS_CLIM.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFNOAA19MHS_CLIM.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFNOAA19MHS_CLIM.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFNOAA19MHS_CLIM.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFNOAA19MHS_CLIM_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFNOAA19MHS_CLIM_07",
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
@@ -152230,1361 +152206,1399 @@
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
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/gpm_anomalous.html",
-                    "description": "GPM and partner sensors anomalous events",
                     "@type": "dcat:Distribution",
+                    "description": "GPM and partner sensors anomalous events",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/tsdis/AB/docs/gpm_anomalous.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/mhs.php",
-                    "description": "Instrument Description from EUMETSAT",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description from EUMETSAT",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/mirs/mhs.php",
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
+            "graphic-preview-description": "Surface Precipitation from GPM MHS on NOAA-19 GPROF (17 km x 17 km) (GPM_2AGPROFNOAA19MHS)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFNOAA19MHS_CLIM_07.png",
+            "identifier": "C2264134366-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "earth science",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/MHS/NOAA19/GPROFCLIM/2A/07",
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
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GPM_2AGPROFNOAA19MHS_CLIM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2009-02-12T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM MHS on NOAA-19 (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 17 km V07 (GPM_2AGPROFNOAA19MHS_CLIM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRSPEC-3-EDR-HALLEY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Spectroscopy subnetwork contains 75 spectra of Halley and 9 data used for calibration. The calibration spectra had as targets stars (HYA 106, BETA LEP) and a planet (MARS). The data covers dates from 1985 October 29 through 1986 May 24.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irspec-3-edr-halley-v1.0_4rmi-4h4c",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international halley watch",
                 "mars",
                 "star",
                 "halley"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRSPEC-3-EDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irspec-3-edr-halley-v1.0_4rmi-4h4c",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Spectroscopy subnetwork contains 75 spectra of Halley and 9 data used for calibration. The calibration spectra had as targets stars (HYA 106, BETA LEP) and a planet (MARS). The data covers dates from 1985 October 29 through 1986 May 24.",
-            "title": "IHW COMET HALLEY INFRARED SPECTRA REFERENCES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY INFRARED SPECTRA REFERENCES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/JHUAPL_SRI_KAUAI/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/JHUAPL_SRI_KAUAI/DATA001.",
-            "issued": "1993-03-25",
-            "temporal": "1993-03-25T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "oceans",
-                "ocean temperature",
-                "earth science",
-                "salinity/density",
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
-            "identifier": "C1633360389-OB_DAAC",
             "description": "Measurements made by the Johns Hopkins University Applied Physics Laboratory (JHUAPL) near the island of Kauai in 1993.",
-            "title": "Johns Hopkins University Applied Physics Laboratory (JHUAPL) measurements near the island of Kauai in 1993",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FJHUAPL_SRI_KAUAI%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FJHUAPL_SRI_KAUAI%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/JHUAPL_SRI_Kauai/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/JHUAPL_SRI_Kauai/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360389-OB_DAAC",
+            "issued": "1993-03-25",
+            "keyword": [
+                "ocean chemistry",
+                "oceans",
+                "ocean temperature",
+                "earth science",
+                "salinity/density",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/JHUAPL_SRI_KAUAI/DATA001",
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
+            "temporal": "1993-03-25T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Johns Hopkins University Applied Physics Laboratory (JHUAPL) measurements near the island of Kauai in 1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566178-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey. 1995-01-01. CORONA Satellite Photography. Sioux Falls, South Dakota, \nUSA. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. Photograph.",
-            "issued": "1960-07-31",
-            "temporal": "1960-07-31T00:00:00Z/1972-05-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1972-05-31",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths",
-                "infrared wavelengths"
-            ],
-            "data-presentation-form": "Photograph",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EROS CENTER",
                 "hasEmail": "mailto:lta@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOI/USGS/EROS"
-            },
-            "identifier": "C1220566178-USGS_LTA",
-            "description": "On February 24, 1995, President Clinton signed an Executive Order,      \ndirecting the declassification of intelligence imagery acquired by  the       \nfirst generation of United States photo-reconnaissance satellites,  including  \nthe systems code-named CORONA, ARGON, and LANYARD.  More than  860,000 images\nof the Earth's surface, collected between 1960 and 1972, were  declassified\nwith the issuance of this Executive Order.\n\nImage collection was driven, in part, by the need to confirm  purported \ndevelopments in then-Soviet strategic missile capabilities.  The  images\nalso were used to produce maps and charts for the Department of Defense \nand for other Federal Government mapping programs.  In addition to the \nimages, documents and reports (collateral information) are available, \npertaining to frame ephemeris data, orbital ephemeris data, and mission \nperformance. Document availability varies by mission; documentation was\nnot  produced for unsuccessful missions.",
-            "release-place": "Sioux Falls, South Dakota, \nUSA",
             "creator": "U.S. Geological Survey",
-            "title": "CORONA Satellite Photography",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Photograph",
+            "description": "On February 24, 1995, President Clinton signed an Executive Order,      \ndirecting the declassification of intelligence imagery acquired by  the       \nfirst generation of United States photo-reconnaissance satellites,  including  \nthe systems code-named CORONA, ARGON, and LANYARD.  More than  860,000 images\nof the Earth's surface, collected between 1960 and 1972, were  declassified\nwith the issuance of this Executive Order.\n\nImage collection was driven, in part, by the need to confirm  purported \ndevelopments in then-Soviet strategic missile capabilities.  The  images\nalso were used to produce maps and charts for the Department of Defense \nand for other Federal Government mapping programs.  In addition to the \nimages, documents and reports (collateral information) are available, \npertaining to frame ephemeris data, orbital ephemeris data, and mission \nperformance. Document availability varies by mission; documentation was\nnot  produced for unsuccessful missions.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov/",
-                    "description": "\n         Query and order satellite images, aerial photographs, and  cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If  you plan on using EarthExplorer frequently, you may wish to register. Please  note that this site uses Session Cookies and Java applets.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and  cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If  you plan on using EarthExplorer frequently, you may wish to register. Please  note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1220566178-USGS_LTA",
+            "issued": "1960-07-31",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "visible wavelengths",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566178-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1972-05-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOI/USGS/EROS"
+            },
+            "release-place": "Sioux Falls, South Dakota, \nUSA",
             "spatial": "-180.0 -85.0 180.0 85.0",
+            "temporal": "1960-07-31T00:00:00Z/1972-05-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CORONA Satellite Photography"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GCPEX/NEXRAD/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "National Climatic Data Center.2015. GPM GROUND VALIDATION KAPX NEXRAD GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GCPEX/NEXRAD/DATA201",
-            "issued": "2015-06-09",
-            "temporal": "2012-01-09T16:58:12Z/2012-03-12T14:58:39Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-10",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C1980479829-GHRC_DAAC",
             "description": "The GPM Ground Validation KAPX NEXRAD GCPEx dataset was collected during January 9, 2012 to March 12, 2012 for the GPM Cold-season Precipitation Experiment (GCPEx). GCPEx addressed shortcomings in GPM snowfall retrieval algorithm by collecting microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. This data set were collected toward achieving the overarching goal of GCPEx which is to characterize the ability of multi-frequency active and passive microwave sensors to detect and estimate falling snow. The Next Generation Weather Radar system (NEXRAD) is comprised of 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) sites throughout the United States and select overseas locations. The GPM Ground Validation NEXRAD GCPEx datasets include data files and browse image files. These data files are available as level 2 binary files and level 3 compressed binary files.",
-            "graphic-preview-description": "N/A",
-            "title": "GPM GROUND VALIDATION KAPX NEXRAD GCPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KAPX/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGCPEX%2FNEXRAD%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGCPEX%2FNEXRAD%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkapxgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmkapxgcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KAPX/browse/2012-02-24/2012-02-24_14-03-17_KAPX_ELEV_01.png",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KAPX/browse/2012-02-24/2012-02-24_14-03-17_KAPX_ELEV_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/gcpex/doc_aggregate/nexradgcpex/gpmnexradgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/gcpex/doc_aggregate/nexradgcpex/gpmnexradgcpex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KAPX/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KAPX/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/NEXRAD/KAPX/browse/",
+            "identifier": "C1980479829-GHRC_DAAC",
+            "issued": "2015-06-09",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GCPEX/NEXRAD/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-90.55 40.77 -78.89 49.04",
+            "temporal": "2012-01-09T16:58:12Z/2012-03-12T14:58:39Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION KAPX NEXRAD GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/1OOD0AX232CJ",
             "citation": "Kevin W. Bowman. 2021-05-27. TRPSDL2O3AIRSFS. Version 1. TROPESS AIRS-Aqua L2 Ozone for Forward Stream, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/1OOD0AX232CJ. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3AIRSFS_1.html. Digital Science Data.",
-            "issued": "2021-05-22",
-            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-22",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1029/2006JD007258",
-                "https://doi.org/10.5194/acp-10-9901-2010",
-                "https://doi.org/10.1029/2007JD008819",
-                "https://doi.org/10.5194/amt-6-1413-2013",
-                "https://doi.org/10.5194/amt-11-5587-2018"
-            ],
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2041966388-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS AIRS-Aqua L2 Ozone for Forward Stream, Standard Product contains the vertical distribution of the retrieved atmospheric state of ozone (O3), formal uncertainties, and diagnostic information measured by the AIRS instrument on the EOS Aqua satellite. The forward stream standard product is global for the time period from 2021-02-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 13.5 km (AIRS nadir FOV), and are reported at 26 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2O3AIRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS AIRS-Aqua O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
-            "title": "TROPESS AIRS-Aqua L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3AIRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3AIRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1OOD0AX232CJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1OOD0AX232CJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3AIRSFS_Sample.png",
-                    "description": "TROPESS AIRS-Aqua O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS AIRS-Aqua O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3AIRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3AIRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3AIRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3AIRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3AIRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3AIRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3AIRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2O3AIRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Standard/TRPSDL2O3AIRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3AIRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Standard/TRPSDL2O3AIRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CRIS-O3_L2_Product_Quick_Start_User_Guide_Standard_only_2-22-21.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-CRIS-O3_L2_Product_Quick_Start_User_Guide_Standard_only_2-22-21.pdf",
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
+            "graphic-preview-description": "TROPESS AIRS-Aqua O3 (Forward Stream, Standard Product) at 261 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3AIRSFS_Sample.png",
+            "identifier": "C2041966388-GES_DISC",
+            "issued": "2021-05-22",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/1OOD0AX232CJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.1029/2006JD007258",
+                "https://doi.org/10.5194/acp-10-9901-2010",
+                "https://doi.org/10.1029/2007JD008819",
+                "https://doi.org/10.5194/amt-6-1413-2013",
+                "https://doi.org/10.5194/amt-11-5587-2018"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2O3AIRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS AIRS-Aqua L2 Ozone for Forward Stream, Standard Product V1 (TRPSDL2O3AIRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL09QL.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3A Calibrated Backscatter Profiles and Atmospheric Layer Characteristics Quick Look V006. Version 006. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL09QL.006.",
-            "issued": "2024-08-29",
-            "temporal": "2024-08-29T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds",
-                "spectral/engineering",
-                "lidar"
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
-            "identifier": "C2551528419-NSIDC_ECS",
             "description": "ATL09QL is the quick look version of ATL09. Once final ATL09 files are available the corresponding ATL09QL files will be removed. \nATL09 contains calibrated, attenuated backscatter profiles, layer integrated attenuated backscatter, and other parameters including cloud layer height and atmospheric characteristics obtained from the data. The data were acquired by the Advanced Topographic Laser Altimeter System (ATLAS) instrument on board the Ice, Cloud and land Elevation Satellite-2 (ICESat-2) observatory.",
-            "title": "ATLAS/ICESat-2 L3A Calibrated Backscatter Profiles and Atmospheric Layer Characteristics Quick Look V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL09QL.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL09QL.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL09QL.006/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL09QL.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL09QL+V006",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL09QL+V006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL09QL/versions/6/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL09QL/versions/6/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL09QL.006",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL09QL.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL09QL.006",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL09QL.006",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2551528419-NSIDC_ECS",
+            "issued": "2024-08-29",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds",
+                "spectral/engineering",
+                "lidar"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL09QL.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2024-08-29T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3A Calibrated Backscatter Profiles and Atmospheric Layer Characteristics Quick Look V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-CRS-4-SUMM-D1%2FD2-192SEC-V1.0",
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
+            "description": "This data set describes the counting\nrate data from detectors D1 and D2 in the Cosmic Ray System (CRS) electron\ntelescope (TET) on Voyager 2 during the Saturn encounter. The D1 detector\nnominally responds to electrons with kinetic energies above approximately\n1 MeV, and the D2 detector, above approximately 2.5 MeV.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-crs-4-summ-d1-d2-192sec-v1.0_4rrn-d9w6",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-CRS-4-SUMM-D1%2FD2-192SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-crs-4-summ-d1-d2-192sec-v1.0_4rrn-d9w6",
-            "description": "This data set describes the counting\nrate data from detectors D1 and D2 in the Cosmic Ray System (CRS) electron\ntelescope (TET) on Voyager 2 during the Saturn encounter. The D1 detector\nnominally responds to electrons with kinetic energies above approximately\n1 MeV, and the D2 detector, above approximately 2.5 MeV.",
-            "title": "VG2 SAT CRS RESAMPLED SUMMARY D1 RATE\n                                      ELEC 192SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT CRS RESAMPLED SUMMARY D1 RATE\n                                      ELEC 192SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/doi:10.5067/N0BWP445491R",
             "citation": "Daniel Tong at Geroge Mason University . 2023-04-18. HAQES_NA_PM25_TOT. Version 1. HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration, North America V1.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/doi:10.5067/N0BWP445491R. https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_1.html. Digital Science Data.",
-            "issued": "2023-04-15",
-            "temporal": "2022-01-02T00:00:00Z/2023-05-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-15",
-            "references": [
-                "https://doi.org/%20http%3A//doi.org/10.1016/j.atmosenv.2015.11.004"
-            ],
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "aerosols",
-                "public health",
-                "air quality",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Suhung Shen",
                 "hasEmail": "mailto:suhung.shen-1@nasa.gov"
             },
+            "creator": "Daniel Tong at Geroge Mason University",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2623694314-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product provides HAQES 3-hourly ensemble mean surface total PM2.5 concentration over the continental United States (CONUS) and surrounding regions. The data is mapped on Lambert projection. \n\nThe Hazardous Air Quality Ensemble System (HAQES) is a real-time ensemble forecast of hazardous air quality events, such as wildfires, dust storms, and Volcanic eruptions. Both regional and global models from multiple agencies are used to create the ensemble, including the Goddard Earth Observing System (GEOS) from the National Aeronautics and Space Administration (NASA), the Navy Aerosol Analysis and Prediction System (NAAPS) from Naval Research Laboratory, the Global Ensemble Forecast System Aerosols (GEFS), High-Resolution Rapid Refresh (HRRR), and National Oceanic and Atmospheric Administration-U.S. Environmental Protection Agency (NOAA-EPA) Atmosphere-Chemistry Coupler-Community Multiscale Air Quality model (NACC-CMAQ) from NOAA.  The prototypes of HAQES products were developed by the George Mason University Air Quality Laboratory as part of the NASA Health Air Quality Applied Science Team (HAQAST).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HAQES_NA_PM25_TOT",
-            "creator": "Daniel Tong at Geroge Mason University",
-            "graphic-preview-description": "Sample image:The surface total PM2.5 concentration from the HAQES model for November 12, 2022 at 18:00Z.",
-            "title": "HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration, North America V1 (HAQES_NA_PM25_TOT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FN0BWP445491R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FN0BWP445491R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_1.png",
-                    "description": "Sample image:The surface total PM2.5 concentration from the HAQES model for November 12, 2022 at 18:00Z.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image:The surface total PM2.5 concentration from the HAQES model for November 12, 2022 at 18:00Z.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT.1/doc/README_HAQES_PM25_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT.1/doc/README_HAQES_PM25_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQES_NA_PM25_TOT",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQES_NA_PM25_TOT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/HAQES_NA_PM25_TOT.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/HAQES_NA_PM25_TOT.1/contents.html",
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
+            "graphic-preview-description": "Sample image:The surface total PM2.5 concentration from the HAQES model for November 12, 2022 at 18:00Z.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_1.png",
+            "identifier": "C2623694314-GES_DISC",
+            "issued": "2023-04-15",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "aerosols",
+                "public health",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/doi:10.5067/N0BWP445491R",
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
+            "series-name": "HAQES_NA_PM25_TOT",
             "spatial": "-132.0 21.0 -58.5 53.5",
+            "temporal": "2022-01-02T00:00:00Z/2023-05-08T00:00:00Z",
             "theme": [
                 "HAQAST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration, North America V1 (HAQES_NA_PM25_TOT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-A-ROMAP-3-AST2-MAG-V1.0",
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
-                "21 lutetia",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 3 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the AST2 (Lutetia fly-by) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-a-romap-3-ast2-mag-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "21 lutetia",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-A-ROMAP-3-AST2-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-a-romap-3-ast2-mag-v1.0",
-            "description": "This archive contains level 3 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the AST2 (Lutetia fly-by) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER LUTETIA ROMAP 3 AST2 MAG\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER LUTETIA ROMAP 3 AST2 MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ESROGSS/AERDB_L2G_GEOLEO_Merged.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2024-12-27. GEO-LEO Merged Deep Blue Aerosol 0.25x0.25 degree Gridded L2. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/ESROGSS/AERDB_L2G_GEOLEO_Merged.001. https://doi.org/10.5067/ESROGSS/AERDB_L2G_GEOLEO_Merged.001.",
-            "issued": "2024-04-30",
-            "temporal": "2019-05-01T00:00:00Z/2020-05-01T23:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-01",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere",
-                "national geospatial data asset",
-                "ngda"
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
-            "identifier": "C3348093425-LAADS",
-            "description": "The GEO-LEO Merged Deep Blue Aerosol 0.25x0.25 degree Gridded L2 product, short-name AERDB_L2G_GEOLEO_Merged contains gridded Aerosol Optical Thickness (AOT) at 550 nm reference wavelength, derived from seven merged GEO-LEO AOT layers (G16-ABI, G17-ABI, H08-AHI, SNPP-VIIRS, NOAA20-VIIRS, Terra MODIS and Aqua MODIS) and from each of the individual (three GEO and four LEO) instrument sources. Each L2G aggregated datafile is spatially comprised of a 0.25\u02da x 0.25\u02da horizontal grid that exists for every 30 minutes. This represents a 30-minute Deep Blue best-estimate AOT from each of the seven sources besides an error-weighted merged AOT layer. This first release of these products spans from May 2019 through April 2020 with a potential to generate additional temporal coverage in the future.  \n\nThe Level-2G (L2G) Geostationary Earth Orbit (GEO)-Low-Earth Orbit (LEO) Merged Deep Blue Aerosol 0.25 x 0.25-degree Gridded dataset is part of a 12-product suite produced by an Earth Science Research from Operational Geostationary Satellite Systems (ESROGSS)-funded project. The 12 products in this project include nine derived from three Geostationary Earth Observation (GEO) instruments and three from merged data from GEO and Low-Earth Orbit (LEO) instruments.\n\nThe AERDB_L2G_GEOLEO_Merged product, in netCDF4 format, contains 16 GEO-LEO Merged Group Science Data Set (SDS) layers and 15 GEO and LEO SDSs. \n\nFor more information consult LAADS product description page at:\n\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDB_L2G_GEOLEO_Merged\n\nOr, Deep Blue aerosol project webpage at: \nhttps://earth.gsfc.nasa.gov/climate/data/deep-blue",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "GEO-LEO Merged Deep Blue Aerosol 0.25x0.25 degree Gridded L2",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The GEO-LEO Merged Deep Blue Aerosol 0.25x0.25 degree Gridded L2 product, short-name AERDB_L2G_GEOLEO_Merged contains gridded Aerosol Optical Thickness (AOT) at 550 nm reference wavelength, derived from seven merged GEO-LEO AOT layers (G16-ABI, G17-ABI, H08-AHI, SNPP-VIIRS, NOAA20-VIIRS, Terra MODIS and Aqua MODIS) and from each of the individual (three GEO and four LEO) instrument sources. Each L2G aggregated datafile is spatially comprised of a 0.25\u02da x 0.25\u02da horizontal grid that exists for every 30 minutes. This represents a 30-minute Deep Blue best-estimate AOT from each of the seven sources besides an error-weighted merged AOT layer. This first release of these products spans from May 2019 through April 2020 with a potential to generate additional temporal coverage in the future.  \n\nThe Level-2G (L2G) Geostationary Earth Orbit (GEO)-Low-Earth Orbit (LEO) Merged Deep Blue Aerosol 0.25 x 0.25-degree Gridded dataset is part of a 12-product suite produced by an Earth Science Research from Operational Geostationary Satellite Systems (ESROGSS)-funded project. The 12 products in this project include nine derived from three Geostationary Earth Observation (GEO) instruments and three from merged data from GEO and Low-Earth Orbit (LEO) instruments.\n\nThe AERDB_L2G_GEOLEO_Merged product, in netCDF4 format, contains 16 GEO-LEO Merged Group Science Data Set (SDS) layers and 15 GEO and LEO SDSs. \n\nFor more information consult LAADS product description page at:\n\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDB_L2G_GEOLEO_Merged\n\nOr, Deep Blue aerosol project webpage at: \nhttps://earth.gsfc.nasa.gov/climate/data/deep-blue",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FESROGSS%2FAERDB_L2G_GEOLEO_Merged.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FESROGSS%2FAERDB_L2G_GEOLEO_Merged.001",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/AERDB_L2G_GEOLEO_Merged--5019",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/AERDB_L2G_GEOLEO_Merged--5019",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/Document%20Archive/Science%20Data%20Product%20Documentation/GEO-LEO_Deep-Blue_Aerosol_UG_v1.0.pdf",
-                    "description": "A pdf version User's Guide for dark target products.",
                     "@type": "dcat:Distribution",
+                    "description": "A pdf version User's Guide for dark target products.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/Document%20Archive/Science%20Data%20Product%20Documentation/GEO-LEO_Deep-Blue_Aerosol_UG_v1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C3348093425-LAADS",
+            "issued": "2024-04-30",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere",
+                "national geospatial data asset",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/ESROGSS/AERDB_L2G_GEOLEO_Merged.001",
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
+            "temporal": "2019-05-01T00:00:00Z/2020-05-01T23:59:00Z",
             "theme": [
                 "GOES",
                 "Suomi-NPP",
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEO-LEO Merged Deep Blue Aerosol 0.25x0.25 degree Gridded L2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1314",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Luus, K.A., and J.C. Lin. 2017. CARVE Modeled Gross Ecosystem CO2 Exchange and Respiration, Alaska, 2012-2014. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1314",
-            "issued": "2017-01-17",
-            "temporal": "2012-01-01T00:00:00Z/2014-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "ngda",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "vegetation",
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
-            "identifier": "C2236236883-ORNL_CLOUD",
             "description": "This data set provides 3-hourly estimates of gross ecosystem CO2 exchange (GEE) and respiration (autotrophic and heterotrophic) for the state of Alaska from 2012 to 2014. The data were generated using the Polar Vegetation Photosynthesis and Respiration Model (PolarVPRM) and are provided at ~ 1 km2 [1/4-degree (longitude) by 1/6-degree (latitude)] pixel resolution. The PolarVPRM produces high-frequency estimates of GEE of CO2 for North American biomes from remotely-sensed data sets. For Alaska, the model used meteorological inputs from the North American regional re-analysis (NARR) and inputs of fractional snow cover and land surface water index (LSWI) from the Moderate Resolution Imaging Spectroradiometer (MODIS). Land surface greenness was factored into the model from three sources: 1) Enhanced Vegetation Index (EVI) from MODIS; 2) Solar Induced Florescence (SIF) from the Orbiting Carbon Observatory 2 (OCO-2); and 3) SIF from the Global Ozone Monitoring Experiment 2 (GOME-2). Three independent estimates of GEE are included in the data set, one for each source of greenness observations.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CARVE Modeled Gross Ecosystem CO2 Exchange and Respiration, Alaska, 2012-2014",
-            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/GEE_MODIS_EVI2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1314",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1314",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/carve/Polar-VPRM_Alaskan-NEE/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/carve/Polar-VPRM_Alaskan-NEE/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/Polar-VPRM_Alaskan-NEE.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/Polar-VPRM_Alaskan-NEE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1314",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1314",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/Polar-VPRM_Alaskan-NEE/comp/Polar-VPRM_Alaskan-NEE.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/Polar-VPRM_Alaskan-NEE/comp/Polar-VPRM_Alaskan-NEE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/GEE_MODIS_EVI2.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/GEE_MODIS_EVI2.png",
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
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/GEE_MODIS_EVI2.png",
+            "identifier": "C2236236883-ORNL_CLOUD",
+            "issued": "2017-01-17",
+            "keyword": [
+                "ngda",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "vegetation",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1314",
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
             "spatial": "-179.0 55.0 -134.0 73.0",
+            "temporal": "2012-01-01T00:00:00Z/2014-12-31T23:59:59Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE Modeled Gross Ecosystem CO2 Exchange and Respiration, Alaska, 2012-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-ESC4-NEL-V1.0",
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
+            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the COMET ESCORT 4 mission\nphase where the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1\n(1969 R1). It contains electron density at higher time resolution than\nin the DERIV2 data sets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-esc4-nel-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-ESC4-NEL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-esc4-nel-v1.0",
-            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the COMET ESCORT 4 mission\nphase where the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1\n(1969 R1). It contains electron density at higher time resolution than\nin the DERIV2 data sets.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nESC4 NEL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nESC4 NEL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0742-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-30T21:11:20.000 to 2015-05-01T07:30:03.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0742-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0742-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0742-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-30T21:11:20.000 to 2015-05-01T07:30:03.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0742 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0742 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0717-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-18T21:21:10.000 to 2015-04-19T05:39:06.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0717-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0717-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0717-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-18T21:21:10.000 to 2015-04-19T05:39:06.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0717 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0717 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-3-RADIOMETRIC-SCI-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Science RDR  data set contains radiometric data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-3-radiometric-sci-v1.0_4s9v-wr8t",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-3-RADIOMETRIC-SCI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-3-radiometric-sci-v1.0_4s9v-wr8t",
-            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Science RDR  data set contains radiometric data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER 3 \n                                     RADIOMETRIC SCI V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER 3 \n                                     RADIOMETRIC SCI V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-3-JUPITER-V1.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Student Dust Counter instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-3-jupiter-v1.0_4sa7-xp4t",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SDC-3-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-sdc-3-jupiter-v1.0_4sa7-xp4t",
-            "description": "This data set contains Calibrated data taken by the New Horizons Student Dust Counter instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS SDC JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS SDC JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/41/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
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
-            "identifier": "DASHLINK_41",
             "description": "In clique tree clustering, inference consists of propagation in a clique tree compiled from a Bayesian network. In this paper, we develop an analytical approach to characterizing clique tree growth as a function of increasing Bayesian network connectedness, specifically: (i) the expected number of moral edges in their moral graphs or (ii) the ratio of the number of non-root nodes to the number of root nodes.  In experiments, we systematically increase the connectivity of bipartite Bayesian networks, and find that clique tree size growth is well-approximated by Gompertz growth curves.  This research improves the understanding of the scaling behavior of clique tree clustering, provides a foundation for benchmarking and developing improved BN inference algorithms, and presents an aid for analytical trade-off studies of tree clustering using growth curves.\r\n\r\n**Reference:**\r\n\r\nO. J. Mengshoel, \"Macroscopic Models of Clique Tree Growth for Bayesian Networks.\"  In Proc. of the 22nd National Conference on Artificial Intelligence (AAAI-07). July 2007, Vancouver, Canada, pp. 1256-1262.\r\n\r\n**BibTex Reference:**\r\n\r\n@inproceedings{mengshoel07macroscopic,\r\n    author = \"Mengshoel, O. J.\",\r\n    title = \"Macroscopic Models of Clique Tree Growth for {Bayesian} Networks\",\r\n        year = \"2007\",\r\n  booktitle = {Proceedings of the Twenty-Second National Conference on Artificial Intelligence (AAAI-07)},\r\n  pages = \"1256-1262\",\r\n  address = \"Vancouver, British Columbia\"\r\n}",
-            "title": "Macroscopic Models of Clique Tree Growth for Bayesian Networks",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/GrowthV26aaai.pdf",
-                    "description": "GrowthV26aaai.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "GrowthV26aaai.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/GrowthV26aaai.pdf",
+                    "mediaType": "application/pdf",
                     "title": "GrowthV26aaai.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_41",
+            "issued": "2010-09-10",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/41/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Macroscopic Models of Clique Tree Growth for Bayesian Networks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AMSR-E/AMSREL1A.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AMSR-E/Aqua L1A Raw Observation Counts V003. Version 3. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/AMSR-E/AMSREL1A.003.",
-            "issued": "2002-06-01",
-            "temporal": "2002-06-01T00:00:00Z/2011-10-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-10-04",
-            "keyword": [
-                "microwave",
-                "earth science",
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
-            "identifier": "C186584407-NSIDC_ECS",
             "description": "AMSR-E Level-1A observation counts are processed from Level-0 science packet data by the Japan Aerospace Exploration Agency (JAXA) Earth Observation Center (EOC) in Japan.",
-            "title": "AMSR-E/Aqua L1A Raw Observation Counts V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAMSREL1A.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSR-E%2FAMSREL1A.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AMSREL1A.003",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/AMSA/AMSREL1A.003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C186584407-NSIDC_ECS&m=-31.359375%211.6875%211%211%210%210%2C2&q=AMSREL1A",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C186584407-NSIDC_ECS&m=-31.359375%211.6875%211%211%210%210%2C2&q=AMSREL1A",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/AMSREL1A/versions/3/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/AMSREL1A/versions/3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AMSREL1A.003",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AMSREL1A.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AMSREL1A.003",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/AMSR-E/AMSREL1A.003",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C186584407-NSIDC_ECS",
+            "issued": "2002-06-01",
+            "keyword": [
+                "microwave",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/AMSR-E/AMSREL1A.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-10-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-06-01T00:00:00Z/2011-10-04T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR-E/Aqua L1A Raw Observation Counts V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1110",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Greenberg, J.P. 2012. LBA-ECO TG-02 Biogenic VOC Emissions from Brazilian Amazon Forest and Pasture Sites. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1110",
-            "issued": "2012-09-05",
-            "temporal": "1998-03-22T00:00:00Z/2000-02-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-18",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2768941787-ORNL_CLOUD",
             "description": "This data set reports concentrations of biogenic volatile organic compounds (BVOCs) collected from tethered balloon-sampling platforms above selected forest and pasture sites in the Brazilian Amazon in March 1998, February 1999, and February 2000. The air samples were collected from forested sites in Brazil: the Tapajos forest (Para) in the Tapajos/Xingu moist forest; Balbina (Amazonas) in the Uatuma moist forest; and Jaru (Rondonia) in the Purus/Madeira moist forest. Two other sites were also located in Rondonia: at a forest reserve (Rebio Jaru) and a pasture (Fazenda Nossa Senhora Aparecida). The BVOCs measured included isoprene, alpha and beta pinene, camphene, sabinene, myrcene, limonene, and other monoterpenes. Approximately 24 to 40 soundings, including as many as four VOC samples collected simultaneously at various altitudes, were made at each site. There is one comma-delimited data file with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO TG-02 Biogenic VOC Emissions from Brazilian Amazon Forest and Pasture Sites",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1110",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1110",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/trace_gases/TG02_Balloon_VOC/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/trace_gases/TG02_Balloon_VOC/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/TG02_Balloon_VOC.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/TG02_Balloon_VOC.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1110",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1110",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/trace_gases/TG02_Balloon_VOC/comp/TG02_Balloon_VOC.PDF",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/trace_gases/TG02_Balloon_VOC/comp/TG02_Balloon_VOC.PDF",
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
+            "identifier": "C2768941787-ORNL_CLOUD",
+            "issued": "2012-09-05",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1110",
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
             "spatial": "-62.2 -10.08 -54.97 -0.86",
+            "temporal": "1998-03-22T00:00:00Z/2000-02-16T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO TG-02 Biogenic VOC Emissions from Brazilian Amazon Forest and Pasture Sites"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-3-EAR3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-3-ear3-v1.0_4si2-du2s",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "international rosetta mission",
                 "earth",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FE-ALICE-3-EAR3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-e-alice-3-ear3-v1.0_4si2-du2s",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the third earth flyby mission phase, which took place between 2009-09-14 and 2009-12-13.",
-            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 3 EAR3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL/EARTH ALICE 3 EAR3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206909-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Arctic EASE-Grid Freeze and Thaw Depths, 1901 - 2002, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1901-01-01",
-            "temporal": "1901-01-01T00:00:00Z/2002-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-12-31",
-            "keyword": [
-                "earth science",
-                "frozen ground",
-                "land surface",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tingjun Zhang",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206909-NSIDCV0",
             "description": "This data set contains mean, median, minimum and maximum freeze and thaw depths for each year from \n1901 to 2002 on the 25 km resolution Equal-Area Scalable Earth Grid (EASE-Grid) for areas north of 50 \ndeg. Freeze and thaw depths are estimated using a variant of the Stefan solution using an edaphic factor \nand freezing or thawing indices as inputs. The edaphic factor is estimated based on different land surface \ntypes; the freezing and thawing indices are from Northern Hemisphere EASE-Grid annual freezing \nand thawing indices, 1901 - 2002 (Zhang, et al. 2005).\n\nTwo ASCII files are available for each year for freeze depth and thaw depth, respectively. Each file is \napproximately 25.6 MB in size. In addition, there is one 10.5 MB ASCII file defining the latitude and longitude coordinates for each grid point. The data set is available via FTP as three compressed files.",
-            "title": "Arctic EASE-Grid Freeze and Thaw Depths, 1901 - 2002, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD651_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD651_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD651/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD651/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD651/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD651/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "spatial": "-180.0 50.0 180.0 90.0",
-            "theme": [
-                "geospatial"
+            "identifier": "C1386206909-NSIDCV0",
+            "issued": "1901-01-01",
+            "keyword": [
+                "earth science",
+                "frozen ground",
+                "land surface",
+                "cryosphere"
             ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206909-NSIDCV0.html",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2002-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
+            "spatial": "-180.0 50.0 180.0 90.0",
+            "temporal": "1901-01-01T00:00:00Z/2002-12-31T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Arctic EASE-Grid Freeze and Thaw Depths, 1901 - 2002, Version 1"
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
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2003.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY03 NASA OMB Budget",
+                    "downloadURL": "http://www.whitehouse.gov/omb/budget/fy2003/",
+                    "mediaType": "application/html",
+                    "title": "FY03 NASA OBM Budget"
+                }
+            ],
+            "identifier": "OCIO-Fitara-95",
             "issued": "2002-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "strategic",
                 "financial",
@@ -153593,265 +153607,229 @@
                 "finance",
                 "budget"
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
-            "identifier": "OCIO-Fitara-95",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2003.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2003: NASA OBM Budget",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/html",
-                    "downloadURL": "http://www.whitehouse.gov/omb/budget/fy2003/",
-                    "description": "FY03 NASA OMB Budget",
-                    "@type": "dcat:Distribution",
-                    "title": "FY03 NASA OBM Budget"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2003: NASA OBM Budget"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0926-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-28T21:24:50.000 to 2015-07-29T00:24:27.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0926-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0926-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0926-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-28T21:24:50.000 to 2015-07-29T00:24:27.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0926 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0926 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/533",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Veldhuis, H. 2000. BOREAS TE-20 Soils Data over the NSA-MSA and Tower Sites in Vector Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/533",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-01T00:00:00Z/1994-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "earth science",
-                "geomorphic landforms/processes",
-                "land surface",
-                "soils",
-                "frozen ground"
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
-            "identifier": "C2808093369-ORNL_CLOUD",
             "description": "Vector layers of soil maps. The vector layers were converted to ARC/INFO EXPORT files.  These data cover 1-km diameters around each of the NSA tower sites and another layer covers the NSA-MSA.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TE-20 Soils Data over the NSA-MSA and Tower Sites in Vector Format",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F533",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F533",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/soilt20v/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TE/soilt20v/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE20_NSA_Soils_Vector.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TE20_NSA_Soils_Vector.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/533",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/533",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/0_readme1.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/0_readme1.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/0_readme2.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/0_readme2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/soilt20v_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/soilt20v_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/TE20_NSA_Soils_Vector.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/TE20_NSA_Soils_Vector.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/TE20_NSA_Soils_Vector.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/TE20_NSA_Soils_Vector.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/TE20_NSA_Soils_Vector.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TE/soilt20v/comp/TE20_NSA_Soils_Vector.txt",
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
+            "identifier": "C2808093369-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "geomorphic landforms/processes",
+                "land surface",
+                "soils",
+                "frozen ground"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/533",
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
             "spatial": "-98.79 55.73 -98.09 56.06",
+            "temporal": "1994-01-01T00:00:00Z/1994-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TE-20 Soils Data over the NSA-MSA and Tower Sites in Vector Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-MAG-4-SUMM-EARTH1-SUMMARY-V1.0",
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
+            "description": "Galileo Orbiter Magnetometer (MAG) calibrated 20 second averaged data from the Earth-1 flyby in spacecraft, GSE, and GSM coordinates. These data cover the interval 1990-11-05 to 1990-12-31.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-mag-4-summ-earth1-summary-v1.0_4skx-mxsf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-E-MAG-4-SUMM-EARTH1-SUMMARY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-e-mag-4-summ-earth1-summary-v1.0_4skx-mxsf",
-            "description": "Galileo Orbiter Magnetometer (MAG) calibrated 20 second averaged data from the Earth-1 flyby in spacecraft, GSE, and GSM coordinates. These data cover the interval 1990-11-05 to 1990-12-31.",
-            "title": "GALILEO ORBITER EARTH MAG SUMM EARTH1 SUMMARY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO ORBITER EARTH MAG SUMM EARTH1 SUMMARY V1.0"
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
-                "radio science",
-                "pds",
-                "grs",
-                "themis",
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
-            "identifier": "NASA-492",
             "description": "GRS, RADIO SCIENCE (Releases 124-126), SPICE, THEMIS",
-            "title": "PDS Odyssey Data Release 42",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153859,41 +153837,45 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-492",
+            "issued": "2018-06-25",
+            "keyword": [
+                "radio science",
+                "pds",
+                "grs",
+                "themis",
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
+            "title": "PDS Odyssey Data Release 42"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/pour/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "information service",
-                "pour",
-                "xml",
-                "xpath"
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
-            "identifier": "OCIO-Fitara-134",
             "description": "Pour is a general-purpose information service framework designed to accommodate a wide variety of information types with support for high volume, low frequency periodic updates, user-specified updates, and automatic updates collected on-demand when needed. Information is stored exclusively in XML and retrieved using standard XPath queries over a single unified namespace independent of the information's source.",
-            "title": "ARC Code TI: Pour",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -153901,95 +153883,94 @@
                     "mediaType": "application/x-tar"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-134",
+            "issued": "2015-01-07",
+            "keyword": [
+                "information service",
+                "pour",
+                "xml",
+                "xpath"
+            ],
+            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/pour/",
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
+            "title": "ARC Code TI: Pour"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/243/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-10-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "ames",
-                "dashlink"
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
-            "identifier": "DASHLINK_243",
             "description": "DYNAMIC STRAIN MAPPING AND REAL-TIME DAMAGE STATE\r\nESTIMATION UNDER BIAXIAL RANDOM FATIGUE LOADING\r\n\r\nSUBHASISH MOHANTY*, ADITI CHATTOPADHYAY*, JOHN N. RAJADAS**, AND CLYDE COELHO*\r\n\r\nAbstract. Fatigue damage and its prediction is one of the foremost concerns of structural integrity\r\nresearch community. The current research in structural health monitoring (SHM) is to\r\nprovide continuous (or on demand) information about the state of a structure. The SHM system\r\ncan be based on either active or passive sensor measurements. Though the current research on\r\nultrasonic wave propagation based active sensing approach has the potential to estimate very small\r\ndamage, it has severe drawbacks in terms of low sensing radius and external power requirements.\r\nTo alleviate these disadvantages passive sensing based SHM techniques can be used. Currently,\r\nfew efforts have been made towards, time-series fatigue damage state estimation over the entire\r\nfatigue life (stage-I, II & III). A majority of the available literature on passive sensing SHM techniques\r\ndemonstrates the clear trend in damage growth during the final failure regime (stage-III\r\nregime) or during when the damage is comparatively large enough. The present paper proposes a\r\npassive sensing technique that demonstrates a clear trend in damage growth almost over the entire\r\nstage-II and III damage growth regime. A strain gauge measurement based passive SHM frameworks\r\nthat can estimate the time-series fatigue damage state under random loading is proposed.\r\nFor this purpose, a Bayesian Gaussian process nonlinear dynamic model is developed to map the\r\nreference condition dynamic strain at a given instant of time. The predicted strains are compared\r\nwith the actual sensor measurements to estimate the corresponding error signals. The error signals\r\nestimated at two different locations are correlated to estimate the corresponding fatigue damage\r\nstate. The approach is demonstrated for an Al-2434 complex cruciform structure applied with\r\nbiaxial random loading.",
-            "title": "DYNAMIC STRAIN MAPPING AND REAL-TIME DAMAGE STATE ESTIMATION UNDER BIAXIAL RANDOM FATIGUE LOADING",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper_21_.pdf",
-                    "description": "DYNAMIC STRAIN MAPPING AND REAL-TIME DAMAGE STATE ESTIMATION UNDER BIAXIAL RANDOM FATIGUE LOADING",
                     "@type": "dcat:Distribution",
+                    "description": "DYNAMIC STRAIN MAPPING AND REAL-TIME DAMAGE STATE ESTIMATION UNDER BIAXIAL RANDOM FATIGUE LOADING",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper_21_.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Paper 21 .pdf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper21_presentation.pdf",
-                    "description": "Presentation",
                     "@type": "dcat:Distribution",
+                    "description": "Presentation",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Paper21_presentation.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Paper21_presentation.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_243",
+            "issued": "2010-10-13",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/243/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "DYNAMIC STRAIN MAPPING AND REAL-TIME DAMAGE STATE ESTIMATION UNDER BIAXIAL RANDOM FATIGUE LOADING"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ARESE/0001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-07-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/ARESE/0001. http://eosweb.larc.nasa.gov/project/arese/arese_table.",
-            "issued": "2008-04-29",
-            "temporal": "1995-09-25T00:00:00Z/1995-10-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-02",
-            "keyword": [
-                "atmospheric radiation",
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
-            "identifier": "C1535861569-LARC_ASDC",
             "description": "The ARM Enhanced Shortwave Experiment (ARESE) was conducted at the Department of Energy's ARM Southern Great Plains (SGP) Central Facility between September 22, 1995 and November 1, 1995. ARESE used a combination of satellite, aircraft, and ground observations to make highly accurate solar flux measurements at different altitudes throughout the atmospheric column. At the heart of this was a carefully stacked Twin Otter and Egrett cloud sandwich with the Otter at 1500 - 5000 feet and the Egrett at 43,000 feet overflown by an ER-2 flying at 65,000 feet.",
-            "title": "ARM Enhanced Shortwave Experiment (ARESE) Solar Radiation Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FARESE%2F0001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FARESE%2F0001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -154077,108 +154058,107 @@
                     "title": "View this dataset's data citation policy"
                 }
             ],
+            "identifier": "C1535861569-LARC_ASDC",
+            "issued": "2008-04-29",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ARESE/0001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-119.91 20.25 -84.93 38.55",
+            "temporal": "1995-09-25T00:00:00Z/1995-10-23T23:59:59Z",
             "theme": [
                 "ARESE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ARM Enhanced Shortwave Experiment (ARESE) Solar Radiation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/840/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "nasa",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shankar Sankararaman",
                 "hasEmail": "mailto:shankar.sankararaman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_840",
             "description": "This contains the list of all important figures and concepts my research work is based on.",
-            "title": "Figures",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Architecture.jpg",
-                    "description": "Architecture",
                     "@type": "dcat:Distribution",
+                    "description": "Architecture",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/Architecture.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Architecture.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/defG_2.jpg",
-                    "description": "Definition of G",
                     "@type": "dcat:Distribution",
+                    "description": "Definition of G",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/defG_2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "defG.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/FORM_MPP.jpg",
-                    "description": "MPP in FORM",
                     "@type": "dcat:Distribution",
+                    "description": "MPP in FORM",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/FORM_MPP.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "FORM MPP.jpg"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/safe_region.jpg",
-                    "description": "Acceptable Region",
                     "@type": "dcat:Distribution",
+                    "description": "Acceptable Region",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/safe_region.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "safe region.jpg"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_840",
+            "issued": "2013-09-30",
+            "keyword": [
+                "dashlink",
+                "nasa",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/840/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Figures"
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
-                "nut-92",
-                "models",
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
-            "identifier": "NASA-830",
             "description": "This web page gives detailed information on the equations for various forms of the Nut-92 one-equation turbulence model.",
-            "title": "Nut-92 Turbulence Model",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154186,23 +154166,52 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-830",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nut-92",
+                "models",
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
+            "description": "Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cubrc.org/_iassets/docs/6_Wadhams_AIAA_Atlanta_SWTBI.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-850__2",
+            "issued": "2018-06-25",
             "keyword": [
                 "layer",
                 "models",
@@ -154213,275 +154222,244 @@
                 "turbulence",
                 "mach"
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
-            "identifier": "NASA-850__2",
-            "description": "Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments:  Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cubrc.org/_iassets/docs/6_Wadhams_AIAA_Atlanta_SWTBI.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Turbulence Models: Data from Other Experiments:  Shock Wave / Turbulent Boundary Layer Flows at High Mach Numbers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0226-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-20T18:55:55.000 to 2014-08-21T01:32:53.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0226-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0226-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0226-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-20T18:55:55.000 to 2014-08-21T01:32:53.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0226 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0226 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-GRNS-4-NS-DDR-V2.0",
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
-                "mercury",
-                "messenger"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract ======== This data set consists of the MESSENGER Neutron Spectrometer (NS) 'derived' data records (DDRs). The NS experiment is a neutron spectrometer designed to observe neutrons emitted from Mercury's surface in the energy range from 0.01 eV to 7 MeV. There is 1 NS DDR standard data product (Neutron Count Rate, NS_DDR_NCR) and 1 NS DDR special data product (Neutron Composition, NS_DDR_NCP). The NCR data products contain net neutron count rates from the LG1, LG2, and BP sensors and uncertainties from each of these sensors. The NCP data product contains fast and epithermal count rates as a function of latitude, along with simulated count rates for the cases of no hydrogen and for a thick layer of 100 wt. percent water ice in all radar bright regions. This is version 2 of this data set; version 1 has been superceded.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-grns-4-ns-ddr-v2.0_4sv2-i2xi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mercury",
+                "messenger"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-GRNS-4-NS-DDR-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-grns-4-ns-ddr-v2.0_4sv2-i2xi",
-            "description": "Abstract ======== This data set consists of the MESSENGER Neutron Spectrometer (NS) 'derived' data records (DDRs). The NS experiment is a neutron spectrometer designed to observe neutrons emitted from Mercury's surface in the energy range from 0.01 eV to 7 MeV. There is 1 NS DDR standard data product (Neutron Count Rate, NS_DDR_NCR) and 1 NS DDR special data product (Neutron Composition, NS_DDR_NCP). The NCR data products contain net neutron count rates from the LG1, LG2, and BP sensors and uncertainties from each of these sensors. The NCP data product contains fast and epithermal count rates as a function of latitude, along with simulated count rates for the cases of no hydrogen and for a thick layer of 100 wt. percent water ice in all radar bright regions. This is version 2 of this data set; version 1 has been superceded.",
-            "title": "MESSENGER E/V/H GRNS 4 NEUTRON SPECTROMETER DDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER E/V/H GRNS 4 NEUTRON SPECTROMETER DDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Mike Smyth, Tom Logan, William Johnson. 2022-11-14. ECOSTRESS Swath Geolocation Instantaneous L1B Global 70 m v002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002. https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2022-11-14",
-            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "surface thermal properties",
-                "land surface",
-                "earth science"
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
-            "identifier": "C2076087338-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Swath Geolocation Instantaneous Level 1B Global (ECO_L1B_GEO) Version 2 data product provides the geolocation information for the radiance values retrieved in the ECO_L1B_RAD (https://doi.org/10.5067/ecostress/eco_l1b_rad.002) Version 2 data product. The geolocation product gives geo-tagging to each of the radiance pixels. The geolocation processing corrects the ISS-reported ephemeris and attitude data by image matching with a global ortho-base derived from Landsat data, and then assigns latitude and longitude values to each of the Level 1 radiance pixels. When image matching is successful, the data are geolocated to better than 50 meter (m) accuracy. The ECO_L1B_GEO data product is provided as swath data.\n\nThe ECO_L1B_GEO data product contains data layers for latitude and longitude values, solar and view geometry information, surface height, and the fraction of pixel on land versus water distributed in HDF5 format.\n\nImprovements/Changes from Previous Versions\n\n-\tIf the initial co-registration is of poor quality or fails, up to four retries are attempted using modified parameters to match the scene. See Section 4.2 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\nKnown Issues\n\n-\tGeolocation accuracy: In cases where scenes were not successfully matched with the ortho-base, the geolocation error is significantly larger; the worst-case geolocation error for uncorrected data is 7 kilometers (km). Within the metadata of the ECO_L1B_GEO file, if the field \"L1GEOMetadata/OrbitCorrectionPerformed\" is \"True\", the data was corrected, and geolocation accuracy should be better than 50 m. If this field is \"False\", then the data was processed without correcting the geolocation and will have up to 7 km geolocation error.\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "title": "ECOSTRESS Swath Geolocation Instantaneous L1B Global 70 m V002",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\n\nThe ECOSTRESS Swath Geolocation Instantaneous Level 1B Global (ECO_L1B_GEO) Version 2 data product provides the geolocation information for the radiance values retrieved in the ECO_L1B_RAD (https://doi.org/10.5067/ecostress/eco_l1b_rad.002) Version 2 data product. The geolocation product gives geo-tagging to each of the radiance pixels. The geolocation processing corrects the ISS-reported ephemeris and attitude data by image matching with a global ortho-base derived from Landsat data, and then assigns latitude and longitude values to each of the Level 1 radiance pixels. When image matching is successful, the data are geolocated to better than 50 meter (m) accuracy. The ECO_L1B_GEO data product is provided as swath data.\n\nThe ECO_L1B_GEO data product contains data layers for latitude and longitude values, solar and view geometry information, surface height, and the fraction of pixel on land versus water distributed in HDF5 format.\n\nImprovements/Changes from Previous Versions\n\n-\tIf the initial co-registration is of poor quality or fails, up to four retries are attempted using modified parameters to match the scene. See Section 4.2 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\nKnown Issues\n\n-\tGeolocation accuracy: In cases where scenes were not successfully matched with the ortho-base, the geolocation error is significantly larger; the worst-case geolocation error for uncorrected data is 7 kilometers (km). Within the metadata of the ECO_L1B_GEO file, if the field \"L1GEOMetadata/OrbitCorrectionPerformed\" is \"True\", the data was corrected, and geolocation accuracy should be better than 50 m. If this field is \"False\", then the data was processed without correcting the geolocation and will have up to 7 km geolocation error.\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tData acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L1B_GEO.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L1B_GEO.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf5",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076087338-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076087338-LPCLOUD",
+                    "mediaType": "application/x-hdf5",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/223/ECO1B_Geolocation_ATBD_V1.pdf",
-                    "description": "The Geolocation ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Geolocation ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/223/ECO1B_Geolocation_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ecostress.jpl.nasa.gov/science",
-                    "description": "The ECOSTRESS website provides detailed information on the mission, instruments, products, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The ECOSTRESS website provides detailed information on the mission, instruments, products, etc.",
+                    "downloadURL": "https://ecostress.jpl.nasa.gov/science",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/222/ECO1B_Calibration_ATBD_V1.pdf",
-                    "description": "The Calibration ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Calibration ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/222/ECO1B_Calibration_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
-                    "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
-                    "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
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
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (AppEEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
                 }
             ],
+            "identifier": "C2076087338-LPCLOUD",
+            "issued": "2022-11-14",
+            "keyword": [
+                "surface thermal properties",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Swath Geolocation Instantaneous L1B Global 70 m V002"
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
-                "incompressible",
-                "flow",
-                "models",
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
-            "identifier": "NASA-842__1",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -154489,20 +154467,56 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "turbulence",
+                "incompressible",
+                "flow",
+                "models",
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
-            "landingPage": "https://data.nasa.gov/d/4sw4-46nz",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The Rodent Research-3 (RR-3) mission was sponsored by the pharmaceutical company Eli Lilly and Co. and the Center for the Advancement of Science in Space to study the effectiveness of a potential countermeasure for the loss of muscle and bone mass that occurs during spaceflight. Twenty BALB/c 18-weeks old female mice (ten controls and ten treated) were flown to the ISS and housed in the Rodent Habitat for 39-42 days. Twenty mice of similar age sex and strain were used for ground controls housed in identical hardware and matching ISS environmental conditions. Basal controls were housed in standard vivarium cages. Spaceflight ground controls and basal groups had blood collected then were euthanized had one hind limb removed and finally whole carcasses were stored at -80 C until dissection. All mice in this data set received only the control/sham injection. Microdissection of retinae from previously frozen eyes and RNA isolation were performed in the laboratory of Dr. Xiao Mao at Loma Linda University.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-194",
+                    "mediaType": "text/html",
+                    "title": "Rodent Research-3-CASIS: Mouse retina transcriptomic data"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-194_4sw4-46nz",
             "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid extraction",
                 "treatment",
@@ -154517,1297 +154531,1285 @@
                 "mouse habitat",
                 "nucleic acid sequencing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/4sw4-46nz",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-194_4sw4-46nz",
-            "description": "The Rodent Research-3 (RR-3) mission was sponsored by the pharmaceutical company Eli Lilly and Co. and the Center for the Advancement of Science in Space to study the effectiveness of a potential countermeasure for the loss of muscle and bone mass that occurs during spaceflight. Twenty BALB/c 18-weeks old female mice (ten controls and ten treated) were flown to the ISS and housed in the Rodent Habitat for 39-42 days. Twenty mice of similar age sex and strain were used for ground controls housed in identical hardware and matching ISS environmental conditions. Basal controls were housed in standard vivarium cages. Spaceflight ground controls and basal groups had blood collected then were euthanized had one hind limb removed and finally whole carcasses were stored at -80 C until dissection. All mice in this data set received only the control/sham injection. Microdissection of retinae from previously frozen eyes and RNA isolation were performed in the laboratory of Dr. Xiao Mao at Loma Linda University.",
-            "title": "Rodent Research-3-CASIS: Mouse retina transcriptomic data",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-194",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Rodent Research-3-CASIS: Mouse retina transcriptomic data"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Rodent Research-3-CASIS: Mouse retina transcriptomic data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3800-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-08-27T17:03:13 to 2015-08-28T08:04:49.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3800-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3800-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3800-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-08-27T17:03:13 to 2015-08-28T08:04:49.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3800 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3800 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3B/PIC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/NOAA-21/VIIRS/L3B/PIC/2022.",
-            "issued": "2023-04-04",
-            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean chemistry"
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
-            "identifier": "C2652675328-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011.  JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA).  S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation.  VIIRS has 22 spectral bands ranging from 412 nm to 12 nm.  There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "NOAA-21 VIIRS Global Binned Particulate Inorganic Carbon (PIC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3B%2FPIC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA-21%2FVIIRS%2FL3B%2FPIC%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3B/PIC/2022",
-                    "description": "VIIRS-NOAA-21 L3B Particulate Inorganic Carbon (PIC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-NOAA-21 L3B Particulate Inorganic Carbon (PIC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NOAA-21/VIIRS/L3B/PIC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2652675328-OB_DAAC",
+            "issued": "2023-04-04",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA-21/VIIRS/L3B/PIC/2022",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-11-10T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-21 VIIRS Global Binned Particulate Inorganic Carbon (PIC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT3-MTP032-V1.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 3 MTP032 mission phase. Comet C-G/67P was the primary target.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext3-mtp032-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-EXT3-MTP032-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-ext3-mtp032-v1.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the ROSETTA\nEXTENSION 3 MTP032 mission phase. Comet C-G/67P was the primary target.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT3 MTP032 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nEXT3 MTP032 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/edbc-3z60",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kennedy, C. M., J. R. Oakleaf, D. M. Theobald, S. Baruch-Mordo, and J. Kiesecker. 2020-06-05. Global Human Modification of Terrestrial Systems. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/edbc-3z60. https://doi.org/10.7927/edbc-3z60.",
-            "issued": "2020-06-05",
-            "temporal": "2016-01-01T00:00:00Z/2016-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-05",
-            "references": [
-                "https://doi.org/10.7927/jw1p-am22"
-            ],
-            "keyword": [
-                "earth science",
-                "ecosystems",
-                "biosphere"
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
-            "identifier": "C1871814255-SEDAC",
-            "description": "The Global Human Modification of Terrestrial Systems data set provides a cumulative measure of the human modification of terrestrial lands across the globe at a 1-km resolution. It is a continuous 0-1 metric that reflects the proportion of a landscape modified, based on modeling the physical extents of 13 anthropogenic stressors and their estimated impacts using spatially-explicit global data sets with a median year of 2016.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Kennedy, C. M., J. R. Oakleaf, D. M. Theobald, S. Baruch-Mordo, and J. Kiesecker",
-            "title": "Global Human Modification of Terrestrial Systems",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Human Modification of Terrestrial Systems data set provides a cumulative measure of the human modification of terrestrial lands across the globe at a 1-km resolution. It is a continuous 0-1 metric that reflects the proportion of a landscape modified, based on modeling the physical extents of 13 anthropogenic stressors and their estimated impacts using spatially-explicit global data sets with a median year of 2016.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fedbc-3z60",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2Fedbc-3z60",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/lulc/lulc-human-modification-terrestrial-systems/lulc-human-modification-terrestrial-systems-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/lulc/lulc-human-modification-terrestrial-systems/lulc-human-modification-terrestrial-systems-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/lulc-human-modification-terrestrial-systems/maps",
+            "identifier": "C1871814255-SEDAC",
+            "issued": "2020-06-05",
+            "keyword": [
+                "earth science",
+                "ecosystems",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.7927/edbc-3z60",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/jw1p-am22"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -60.0 180.0 83.64",
+            "temporal": "2016-01-01T00:00:00Z/2016-12-31T00:00:00Z",
             "theme": [
                 "LULC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Human Modification of Terrestrial Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-3-PLUTO-V2.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains PEPSSI observations taken during the              the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-3-pluto-v2.0_4t9s-b57v",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-PEPSSI-3-PLUTO-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-pepssi-3-pluto-v2.0_4t9s-b57v",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains PEPSSI observations taken during the              the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO ENCOUNTER                                                  \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206867-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seasonal frost depths, midwestern USA, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1971-01-12",
-            "temporal": "1971-01-12T00:00:00Z/1983-03-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1983-03-03",
-            "keyword": [
-                "earth science",
-                "frozen ground",
-                "land surface",
-                "snow/ice",
-                "soils",
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "agriculture"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Haugen",
                 "hasEmail": "mailto:Richard.K.Haugen@hanover.valley.net"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206867-NSIDCV0",
             "description": "This dataset includes frost tube data from 37 stations in the Upper Midwest (Minnesota, North Dakota, Wisconsin), USA. The responsible agency was the St. Paul District of the U.S. Army Corps of Engineers. These data were collected during 1971-1981 (no data for 1976/77) by cooperative observers who gathered the data for use in their spring run-off hydrologic predictions. The observers had frost tubes installed by District personnel in their back yards. The early penetration of frost at the beginning of the freezing season was not observed, but most observers picked up the record when 1 or 2' of frost had occurred. This data base, a preliminary version, was constructed by Richard K. Haugen and Glenn King from the manuscript records of the cooperative observers and is presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Seasonal frost depths, midwestern USA, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD498_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD498_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD498/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD498/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD498/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD498/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206867-NSIDCV0",
+            "issued": "1971-01-12",
+            "keyword": [
+                "earth science",
+                "frozen ground",
+                "land surface",
+                "snow/ice",
+                "soils",
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "agriculture"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206867-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1983-03-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-101.3 43.767 -90.183 48.833",
+            "temporal": "1971-01-12T00:00:00Z/1983-03-03T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Seasonal frost depths, midwestern USA, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SAKIG-C-IMF-3-RDR-HALLEY-V1.0",
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
-                "sakigake",
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The original Data Set Name was MST5IMF. The data was delivered personally by Oyama. The component values indicate a crossing of the neutral sheet. The magnetic field is defined in terms of solar ecliptic coordinates with spacecraft at the center and the x direction positive towards the Sun, the y direction in the ecliptic plane, and the z direction given by a left handed coordinate system. A total force value is also given.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sakig-c-imf-3-rdr-halley-v1.0_4tah-cqh9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "sakigake",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SAKIG-C-IMF-3-RDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sakig-c-imf-3-rdr-halley-v1.0_4tah-cqh9",
-            "description": "The original Data Set Name was MST5IMF. The data was delivered personally by Oyama. The component values indicate a crossing of the neutral sheet. The magnetic field is defined in terms of solar ecliptic coordinates with spacecraft at the center and the x direction positive towards the Sun, the y direction in the ecliptic plane, and the z direction given by a left handed coordinate system. A total force value is also given.",
-            "title": "SAKIGAKE INTERPLANETARY MAGNETIC FIELD DATA V 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SAKIGAKE INTERPLANETARY MAGNETIC FIELD DATA V 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PLS-5-RDR-2PROMAGSPH-48SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set gives the best available values for ion densities, temperatures, and velocities near Neptune derived from data obtained by the Voyager 2 plasma experiment. All parameters are obtained by fitting the observed spectra (current as a function of energy) with Maxwellian plasma distributions, using a non-linear least squares fitting routine to find the plasma parameters which, when coupled with the full instrument response, best simulate the data. The PLS instrument measures energy/charge, so composition is not uniquely determined but can be deduced in some cases by the separation of the observed current peaks in energy (assuming the plasma is co-moving). In the upstream solar wind protons are fit to the M-long data since high energy resolution is needed to obtain accurate plasma parameters. In the magnetosheath the ion flux so low that several L-long spectra (3-5) had to be averaged to increase the signal-to-noise ratio to a level at which the data could be reliably fit. These averaged spectra were fit using two proton maxwellians with the same velocity. The values given in the upstream magnetosheath are the total density and the density-weighted temperature. In both the upstream solar wind and magnetosheath full vector velocities, densities and temperatures are derived for each fit component. In the magnetosphere spectra do not contain enough information to obtain full velocity vectors, so flow is assumed to be purely azimuthal. In some cases the azimuthal velocity is a fit parameter, in some cases rigid corotation is assumed. In the 'outer' magnetosphere (L>5) two distinct current peaks appear in the spectra H+ and N+. In the inner magnetosphere the plasma is hot and the composition is ambiguous, although two superimposed Maxwellians are still required to fit the data. These spectra are fit using two compositions, one with H+ and N+ and the second with two H+ components. The N+ composition is preferred by the data provider. All fit values in the magnetosphere come with one sigma errors. It should be noted that no attempt has been made to account for the spacecraft potential, which is probably about -10 V in this region and will effect the density and velocity values. In the outbound magnetosheath and solar wind both moment and fit values are given for velocity, density, and thermal speed. The signal-to-noise ratio in the M-longs is very low, especially near the magnetopause, which can result in the analysis giving incorrect values. The L-long spectra have too low an energy resolution to permit accurate determinations parameters in many regions temperature and non-radial velocity components may be inaccurate.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pls-5-rdr-2promagsph-48sec-v1.0_4tb8-mesp",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "voyager",
                 "neptune"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-PLS-5-RDR-2PROMAGSPH-48SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-pls-5-rdr-2promagsph-48sec-v1.0_4tb8-mesp",
-            "description": "This data set gives the best available values for ion densities, temperatures, and velocities near Neptune derived from data obtained by the Voyager 2 plasma experiment. All parameters are obtained by fitting the observed spectra (current as a function of energy) with Maxwellian plasma distributions, using a non-linear least squares fitting routine to find the plasma parameters which, when coupled with the full instrument response, best simulate the data. The PLS instrument measures energy/charge, so composition is not uniquely determined but can be deduced in some cases by the separation of the observed current peaks in energy (assuming the plasma is co-moving). In the upstream solar wind protons are fit to the M-long data since high energy resolution is needed to obtain accurate plasma parameters. In the magnetosheath the ion flux so low that several L-long spectra (3-5) had to be averaged to increase the signal-to-noise ratio to a level at which the data could be reliably fit. These averaged spectra were fit using two proton maxwellians with the same velocity. The values given in the upstream magnetosheath are the total density and the density-weighted temperature. In both the upstream solar wind and magnetosheath full vector velocities, densities and temperatures are derived for each fit component. In the magnetosphere spectra do not contain enough information to obtain full velocity vectors, so flow is assumed to be purely azimuthal. In some cases the azimuthal velocity is a fit parameter, in some cases rigid corotation is assumed. In the 'outer' magnetosphere (L>5) two distinct current peaks appear in the spectra H+ and N+. In the inner magnetosphere the plasma is hot and the composition is ambiguous, although two superimposed Maxwellians are still required to fit the data. These spectra are fit using two compositions, one with H+ and N+ and the second with two H+ components. The N+ composition is preferred by the data provider. All fit values in the magnetosphere come with one sigma errors. It should be noted that no attempt has been made to account for the spacecraft potential, which is probably about -10 V in this region and will effect the density and velocity values. In the outbound magnetosheath and solar wind both moment and fit values are given for velocity, density, and thermal speed. The signal-to-noise ratio in the M-longs is very low, especially near the magnetopause, which can result in the analysis giving incorrect values. The L-long spectra have too low an energy resolution to permit accurate determinations parameters in many regions temperature and non-radial velocity components may be inaccurate.",
-            "title": "VG2 NEP PLS DERIVED RDR 2 PROTON MAGSPHERE 48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEP PLS DERIVED RDR 2 PROTON MAGSPHERE 48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3H2OM.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3H2OM.006. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-03T00:00:00Z/2018-01-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric water vapor",
-                "earth science",
-                "atmosphere",
-                "atmospheric temperature"
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
-            "identifier": "C1703619841-LARC",
             "description": "TL3H2OM_6 is the Tropospheric Emission Spectrometer (TES)/Aura Level 3 Water Vapor Monthly Gridded Version 6 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. This data product consists of monthly atmospheric temperature and volume mixing ratios (VMRs) for the Water Vapor atmospheric species, which are provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels.\r\rThe TES Science Data Processing L3 subsystem interpolated L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products are composed of L3 HDF-EOS grid data. A separate product file was produced for each different atmospheric species. TES obtained data in two basic observation modes: Limb or Nadir; Nadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. The product file may contain, in separate folders, limb data, nadir data, or both folders may be present. Specific to L3 processing were the terms Daily and Monthly representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process are complete Global Surveys; in other words a Global Survey was not split in relation to time when input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represent Global Surveys that are initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly.",
-            "title": "TES/Aura L3 Water Vapor Monthly Gridded V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3H2OM.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3H2OM.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_alg_req_prod.pdf",
-                    "description": "TES Level 3 Algorithms, Requirements & Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 Algorithms, Requirements & Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_alg_req_prod.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L3monthly.cgi",
-                    "description": "Report of TES Level 3 Monthly Data Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 3 Monthly Data Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L3monthly.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/TES",
-                    "description": "NASA Earthdata Forum - TES Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - TES Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/TES",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3H2OM.006",
-                    "description": "DOI data set landing page for TL3H2OM_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3H2OM_6",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3H2OM.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703619841-LARC",
-                    "description": "Earthdata Search for TL3H2OM_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3H2OM_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703619841-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3H2OM.006/",
-                    "description": "ASDC Direct Data Download for TL3H2OM_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL3H2OM_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3H2OM.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3H2OM.006/contents.html",
-                    "description": "OPeNDAP data access for TL3H2OM_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3H2OM_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3H2OM.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/vnd.ms-powerpoint",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_STM_2013_Data_User_Session-2.ppt",
-                    "description": "2013 TES Data User Session Presentation - Direct File Download (.ppt)",
                     "@type": "dcat:Distribution",
+                    "description": "2013 TES Data User Session Presentation - Direct File Download (.ppt)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_STM_2013_Data_User_Session-2.ppt",
+                    "mediaType": "application/vnd.ms-powerpoint",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/TES_Validation_Report_v7_Final.pdf",
-                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Data Validation Report (Version F08_11 data) - Version 7.0",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Data Validation Report (Version F08_11 data) - Version 7.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/TES_Validation_Report_v7_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
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
                 }
             ],
+            "identifier": "C1703619841-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3H2OM.006",
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
+            "temporal": "2004-09-03T00:00:00Z/2018-01-31T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 Water Vapor Monthly Gridded V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/481",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cihlar, J. 1999. BOREAS Level-3b AVHRR-LAC Imagery: Scaled At-Sensor Radiance in LGSOWG Format. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/481",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-30T00:00:00Z/1996-09-18T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
-            "keyword": [
-                "surface radiative properties",
-                "earth science",
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
-            "identifier": "C2929133860-ORNL_CLOUD",
             "description": "Data acquired from the AVHRR instrument on the NOAA-9, -11, -12, and -14 satellites were processed and archived. A few winter acquisitions are available, but the archive contains primarily growing season imagery.  These gridded, at-sensor radiance image data cover the period of 30-Jan-1994 to 18-Sep-1996.  Geographically, the data cover the entire 1000 km x 1000 km BOREAS Region.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Level-3b AVHRR-LAC Imagery: Scaled At-Sensor Radiance in LGSOWG Format",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F481",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F481",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/avhrrl3b/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/avhrrl3b/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AVHRR_L3b.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AVHRR_L3b.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/481",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/481",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/avhrrl3b.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/avhrrl3b.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/AVHRR_L3b.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/AVHRR_L3b.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/AVHRR_L3b.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/AVHRR_L3b.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/AVHRR_L3b.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/AVHRR_L3b.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/avhrr_level_3b_inv.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/avhrr_level_3b_inv.dat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/avhrrl3b/comp/README",
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
+            "identifier": "C2929133860-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "surface radiative properties",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/481",
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
             "spatial": "-111.0 50.09 -93.5 59.98",
+            "temporal": "1994-01-30T00:00:00Z/1996-09-18T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Level-3b AVHRR-LAC Imagery: Scaled At-Sensor Radiance in LGSOWG Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/FZ3KL32LBPA2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx23 Oct23 Ground Surface Roughness Imagery V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/FZ3KL32LBPA2.",
-            "issued": "2023-10-17",
-            "temporal": "2023-10-17T00:00:00Z/2023-10-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-28",
-            "keyword": [
-                "earth science",
-                "topography",
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
-            "identifier": "C3333536645-NSIDC_ECS",
             "description": "This data set presents photographs of snow pit ground surface collected using a digital camera during the NASA SnowEx 2023 field campaign between 17 and 28 October 2023. The images were collected from 22 snow pits located across three study sites: Upper Kuparuk and Toolik (UKT), an arctic tundra environment in Northern Alaska, and Caribou Poker Creek watershed (CPCW) and Farmers Loop Creamers Field (FLCF), two boreal forest sites near Fairbanks, Alaska. These photographs were used to derive point cloud data representative of ground surface roughness, which are available as <a href=\"https://doi.org/10.5067/9BTG86R3ISRB\">SnowEx23 Oct23 Ground Surface Roughness Reconstruction, Version 1</a>.",
-            "title": "SnowEx23 Oct23 Ground Surface Roughness Imagery V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFZ3KL32LBPA2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFZ3KL32LBPA2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_OCT23_GSR_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_OCT23_GSR_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_OCT23_GSR_Raw/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_OCT23_GSR_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_OCT23_GSR_Raw+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_OCT23_GSR_Raw+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FZ3KL32LBPA2",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/FZ3KL32LBPA2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/FZ3KL32LBPA2",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/FZ3KL32LBPA2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3333536645-NSIDC_ECS",
+            "issued": "2023-10-17",
+            "keyword": [
+                "earth science",
+                "topography",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/FZ3KL32LBPA2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-149.6 68.5 -149.3 68.7",
+            "temporal": "2023-10-17T00:00:00Z/2023-10-28T23:59:59.999Z",
             "theme": [
                 "SnowEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx23 Oct23 Ground Surface Roughness Imagery V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/OAHU/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/OAHU/DATA001.",
-            "issued": "2007-06-12",
-            "temporal": "2007-06-12T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "oceans",
-                "earth science",
-                "ocean optics",
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
-            "identifier": "C1633360532-OB_DAAC",
             "description": "Measurements made in the west-central Pacific near Wake Island in 2007.",
-            "title": "Measurements made in the west-central Pacific near Wake Island",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FOAHU%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FOAHU%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/OAHU/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/OAHU/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360532-OB_DAAC",
+            "issued": "2007-06-12",
+            "keyword": [
+                "ocean chemistry",
+                "oceans",
+                "earth science",
+                "ocean optics",
+                "salinity/density",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/OAHU/DATA001",
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
+            "temporal": "2007-06-12T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements made in the west-central Pacific near Wake Island"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/api-documents/foundry/#/data.nasa.gov/fk38-4khf",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://data.nasa.gov/developer"
-            ],
-            "keyword": [
-                "agency management operations",
-                "open data",
-                "api",
-                "open government"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jason Duley",
                 "hasEmail": "mailto:jason.duley@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "API-23",
             "description": "This dataset lists out all software in use by NASA.",
-            "title": "NASA Open Source And General Resource Software API",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.nasa.gov/resource/fk38-4khf.json",
-                    "description": "This dataset lists out all software in use by NASA.",
                     "@type": "dcat:Distribution",
+                    "description": "This dataset lists out all software in use by NASA.",
+                    "downloadURL": "https://data.nasa.gov/resource/fk38-4khf.json",
+                    "mediaType": "text/html",
                     "title": "NASA Open Source And General Resource Software API"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "API-23",
+            "issued": "2015-11-30",
+            "keyword": [
+                "agency management operations",
+                "open data",
+                "api",
+                "open government"
+            ],
+            "landingPage": "https://data.nasa.gov/api-documents/foundry/#/data.nasa.gov/fk38-4khf",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "https://data.nasa.gov/developer"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Open Source And General Resource Software API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1384-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-30T20:13:15.000 to 2016-01-30T23:14:37.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1384-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1384-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1384-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-30T20:13:15.000 to 2016-01-30T23:14:37.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1384 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1384 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include all reported timings of observed asteroid occultation events through Feb. 23, 2005, as well as asteroid occultation axes derived from those timings by David W. Dunham and David Herald. Some occultations by planetary satellites are also included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v3.0_4tib-7xt3",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "satellite",
                 "asteroid",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v3.0_4tib-7xt3",
-            "description": "This data set is intended to include all reported timings of observed asteroid occultation events through Feb. 23, 2005, as well as asteroid occultation axes derived from those timings by David W. Dunham and David Herald. Some occultations by planetary satellites are also included.",
-            "title": "ASTEROID OCCULTATIONS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID OCCULTATIONS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67PCHURYUMOV-M13-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67pchuryumov-m13-v2.0_4tjb-f4f8",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67PCHURYUMOV-M13-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67pchuryumov-m13-v2.0_4tjb-f4f8",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP013 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP013 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0066",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0066.",
-            "issued": "1999-11-10",
-            "temporal": "1992-05-30T00:00:00Z/1992-06-23T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "spectral/engineering",
-                "altitude",
-                "microwave",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOUG JOHNSON",
                 "hasEmail": "mailto:dwjohnson@email.meto.govt.uk"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001050-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems. These data were collected by the United Kingdom Meteorological Office (UKMO) from the Meteorological Research Flight C-130 Aircraft. This data set is a 1 to 64 Hertz time series data set.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) United Kingdom Meteorological Office (UKMO) C-130 Aircraft Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0066",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0066",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001050-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_UKMO_C130_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_UKMO_C130_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001050-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fhdf_netcdf.c",
-                    "description": "Sample read software for netcdf formatted science Data Sets - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read software for netcdf formatted science Data Sets - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fhdf_netcdf.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire.netcdf.rd.make.txt",
-                    "description": "Read Software - FIRE Makefile for NetCDF",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software - FIRE Makefile for NetCDF",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire.netcdf.rd.make.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_ukmo_c130_dataset.pdf",
-                    "description": "FIRE ASTEX United Kingdom Meteorological Office C-130 Aircraft Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX United Kingdom Meteorological Office C-130 Aircraft Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_ukmo_c130_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_ukmo_c130",
-                    "description": "Meteorological Research Flight: FIRE Central Archive Catalog Information Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Meteorological Research Flight: FIRE Central Archive Catalog Information Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_ukmo_c130",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_ukmo_c130_info1",
-                    "description": "Readme Information about the FIRE_AX_UKMO_C130 data set read software",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the FIRE_AX_UKMO_C130 data set read software",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_ukmo_c130_info1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0066",
-                    "description": "DOI data set landing page for FIRE_AX_UKMO_C130_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_UKMO_C130_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0066",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_UKMO_C130/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_UKMO_C130_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_UKMO_C130_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_UKMO_C130/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_UKMO_C130/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_UKMO_C130_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_UKMO_C130_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_UKMO_C130/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001050-LARC_ASDC",
+            "issued": "1999-11-10",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "spectral/engineering",
+                "altitude",
+                "microwave",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0066",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>28.0 -28.0 28.0 -15.0 41.0 -15.0 41.0 -28.0 28.0 -28.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-05-30T00:00:00Z/1992-06-23T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) United Kingdom Meteorological Office (UKMO) C-130 Aircraft Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-CRUISE3-V1.0",
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
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-cruise3-v1.0_4tmh-hnej",
+            "issued": "2018-06-26",
+            "keyword": [
+                "solar wind",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-CRUISE3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-cruise3-v1.0_4tmh-hnej",
-            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR MAG DATA FOR CRUISE3",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR MAG DATA FOR CRUISE3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-V%2FE%2FJ%2FS%2FSS-RPWS-2-REFDR-WFRFULL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Cassini Radio and Plasma Wave Science (RPWS) edited full resolution data set includes all waveform data for the entire Cassini mission.  This data set includes uncalibrated values for each waveform channel for each sensor for all times during the mission including the second Venus flyby, the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour. Data for this data set are acquired from the RPWS Waveform Receiver (WFR).  Data are presented in a set of time series organized so as to have fixed-length records for ease in data handling.  Data from the different WFR modes (i.e. 2.5-kHz and 26 Hz modes)  are segregated into separate files.  This data set includes all waveform data acquired by the RPWS.  A browse data set is included with these data which provides for a graphical search of the data using a series of thumbnail and full-sized spectrograms which lead the user to the particular data file(s) of interest.  The waveform data provide the highest resolution data from the RPWS instrument in the form of a set of waveform series for these two bandwidths and can be used, when data from two electric and three magnetic sensors are available, to perform wave-normal analyses on various plasma wave phenomena.  These data can be used in their original time domain in order to look for solitary features such as dust impacts or electrostatic solitary waves.  Or, they can be transformed into the frequency domain in order to examine the detailed time and spectral evolution of plasma waves or radio emissions or to do the wave-normal analysis. Usually, this data set includes time series measurements from more than one (up to five) sensors at a time and the samples are made simultaneously for all five sensors.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-v-e-j-s-ss-rpws-2-refdr-wfrfull-v1.0_4tmv-ssxs",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "cassini-huygens",
@@ -155825,187 +155827,155 @@
                 "titan",
                 "tethys"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-V%2FE%2FJ%2FS%2FSS-RPWS-2-REFDR-WFRFULL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-v-e-j-s-ss-rpws-2-refdr-wfrfull-v1.0_4tmv-ssxs",
-            "description": "The Cassini Radio and Plasma Wave Science (RPWS) edited full resolution data set includes all waveform data for the entire Cassini mission.  This data set includes uncalibrated values for each waveform channel for each sensor for all times during the mission including the second Venus flyby, the Earth flyby, the Jupiter flyby, interplanetary cruise, and the entire Saturn tour. Data for this data set are acquired from the RPWS Waveform Receiver (WFR).  Data are presented in a set of time series organized so as to have fixed-length records for ease in data handling.  Data from the different WFR modes (i.e. 2.5-kHz and 26 Hz modes)  are segregated into separate files.  This data set includes all waveform data acquired by the RPWS.  A browse data set is included with these data which provides for a graphical search of the data using a series of thumbnail and full-sized spectrograms which lead the user to the particular data file(s) of interest.  The waveform data provide the highest resolution data from the RPWS instrument in the form of a set of waveform series for these two bandwidths and can be used, when data from two electric and three magnetic sensors are available, to perform wave-normal analyses on various plasma wave phenomena.  These data can be used in their original time domain in order to look for solitary features such as dust impacts or electrostatic solitary waves.  Or, they can be transformed into the frequency domain in order to examine the detailed time and spectral evolution of plasma waves or radio emissions or to do the wave-normal analysis. Usually, this data set includes time series measurements from more than one (up to five) sensors at a time and the samples are made simultaneously for all five sensors.",
-            "title": "CASSINI V/E/J/S/SS RPWS EDITED WAVEFORM FULL RES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI V/E/J/S/SS RPWS EDITED WAVEFORM FULL RES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/REPORTS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A and Robert A. Houze.2018. GPM Ground Validation Campaign Reports OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/REPORTS/DATA101",
-            "issued": "2018-03-05",
-            "temporal": "2015-10-23T15:19:00Z/2016-01-22T16:25:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-25",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "platform characteristics"
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
-            "identifier": "C1979624676-GHRC_DAAC",
             "description": "The GPM Ground Validation Campaign Reports OLYMPEX dataset consists of flight reports, weather forecasts, instrument reports, scientist summaries, and plan-of-day reports collected during the Global Precipitation Measurement (GPM) Olympic Mountains Experiment (OLYMPEX) field campaign to help support the ground validation of the GPM. These campaign reports were collected during the intense operating period which occurred during November 2015 to February 2016.  The various campaign reports  are available in PDF, JPG, PNG, and Microsoft Powerpoint and Word formats, some of which are located within tarred data files.",
-            "title": "GPM Ground Validation Campaign Reports OLYMPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FREPORTS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FREPORTS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmisrepolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmmisrepolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
-                    "description": "OLYMPEX Collection Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX Collection Landing Page",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/reports/doc/gpmmisrepolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/reports/doc/gpmmisrepolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1979624676-GHRC_DAAC",
+            "issued": "2018-03-05",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "platform characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/REPORTS/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-130.045 34.6142 -117.881 49.634",
+            "temporal": "2015-10-23T15:19:00Z/2016-01-22T16:25:00Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Campaign Reports OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SDRON-SURF0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Saildrone. 2018-12-19. Saildrone Baja field campaign surface and ADCP measurements. Version 1.0. Saildrone Baja Field Campaign Products. Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501. Archived by National Aeronautics and Space Administration, U.S. Government, Saildrone Inc. https://doi.org/10.5067/SDRON-SURF0. http://podaac.jpl.nasa.gov/saildrone. Saildrone, Saildrone Inc, 2018-12-19, Saildrone  Baja field campaign surface and ADCP measurements, http://podaac.jpl.nasa.gov/saildrone.",
-            "issued": "2018-11-27",
-            "temporal": "2018-04-11T18:00:00Z/2018-06-11T20:17:26Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
-            "keyword": [
-                "earth science",
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric temperature",
-                "ocean temperature",
-                "oceans",
-                "ocean winds",
-                "ocean optics",
-                "salinity/density",
-                "ocean chemistry"
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
-            "identifier": "C2491772165-POCLOUD",
-            "description": "Saildrone is a wind and solar powered unmanned surface vehicle (USV) capable of long distance deployments lasting up to 12 months and providing high quality, near real-time, multivariate surface ocean and atmospheric observations while transiting at typical speeds of 3-5 knots. The drone is autonomous in that it may be guided remotely from land while being completely wind driven. \nThe saildrone Baja campaign was a 60-day cruise from San Francisco Bay, down along the US/Mexico coast to Guadalupe Island and back again over the period 11 April 2018 to 11 June 2018.  Repeat surveys were taken around NDBC moored buoys, and during the final week of the cruise a targeted front was sampled.  Scientific objectives included studies of upwelling and frontal region dynamics, air-sea interactions, and diurnal warming effects, while its validation objectives included establishing the utility of data from the saildrone platform for assessment of satellite data accuracy and model assimilation.  During the Baja campaign, the single deployed saildrone was equipped with a suite of instruments that included a CTD, IR pyrometer, fluorometer, dissolved oxygen sensor, anemometer, barometer, and Acoustic Doppler Current Profiler (ADCP).  Additionally, four temperature data loggers were positioned vertically along hull to provide further information on thermal variability near the ocean surface.\nThis Saildrone Baja dataset is comprised of one data file with the  saildrone platform telemetry and near-surface observational data (air temperature, sea surface skin and bulk temperatures, salinity, oxygen and chlorophyll-a concentrations, barometric pressure, wind speed and direction) for the entire cruise at 1 minute temporal resolution. A second file contains the ADCP current vector data that is depth-resolved to 100m at 2m intervals and binned temporally at 5 minute resolution.  All data files are in netCDF format and CF/ACDD compliant consistent with the NOAA/NCEI specification.",
-            "release-place": "Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501",
-            "series-name": "Saildrone Baja field campaign surface and ADCP measurements",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Saildrone",
-            "title": "Saildrone  Baja field campaign surface and ADCP measurements",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_BAJA_SURFACE.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Saildrone is a wind and solar powered unmanned surface vehicle (USV) capable of long distance deployments lasting up to 12 months and providing high quality, near real-time, multivariate surface ocean and atmospheric observations while transiting at typical speeds of 3-5 knots. The drone is autonomous in that it may be guided remotely from land while being completely wind driven. \nThe saildrone Baja campaign was a 60-day cruise from San Francisco Bay, down along the US/Mexico coast to Guadalupe Island and back again over the period 11 April 2018 to 11 June 2018.  Repeat surveys were taken around NDBC moored buoys, and during the final week of the cruise a targeted front was sampled.  Scientific objectives included studies of upwelling and frontal region dynamics, air-sea interactions, and diurnal warming effects, while its validation objectives included establishing the utility of data from the saildrone platform for assessment of satellite data accuracy and model assimilation.  During the Baja campaign, the single deployed saildrone was equipped with a suite of instruments that included a CTD, IR pyrometer, fluorometer, dissolved oxygen sensor, anemometer, barometer, and Acoustic Doppler Current Profiler (ADCP).  Additionally, four temperature data loggers were positioned vertically along hull to provide further information on thermal variability near the ocean surface.\nThis Saildrone Baja dataset is comprised of one data file with the  saildrone platform telemetry and near-surface observational data (air temperature, sea surface skin and bulk temperatures, salinity, oxygen and chlorophyll-a concentrations, barometric pressure, wind speed and direction) for the entire cruise at 1 minute temporal resolution. A second file contains the ADCP current vector data that is depth-resolved to 100m at 2m intervals and binned temporally at 5 minute resolution.  All data files are in netCDF format and CF/ACDD compliant consistent with the NOAA/NCEI specification.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSDRON-SURF0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSDRON-SURF0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/saildrone/docs/2018_04_Saildrone_Cruise_Report.pdf",
-                    "description": "Cruise Report, Data Submission Report, Instrument Calibration Report",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Report, Data Submission Report, Instrument Calibration Report",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/saildrone/docs/2018_04_Saildrone_Cruise_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/saildrone",
-                    "description": "Field Campaign and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/saildrone",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
@@ -156015,955 +155985,959 @@
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_BAJA_SURFACE.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_BAJA_SURFACE.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.saildrone.com/",
-                    "description": "Saildrone Website",
                     "@type": "dcat:Distribution",
+                    "description": "Saildrone Website",
+                    "downloadURL": "https://www.saildrone.com/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772165-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772165-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772165-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772165-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SAILDRONE_BAJA_SURFACE.jpg",
+            "identifier": "C2491772165-POCLOUD",
+            "issued": "2018-11-27",
+            "keyword": [
+                "earth science",
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric temperature",
+                "ocean temperature",
+                "oceans",
+                "ocean winds",
+                "ocean optics",
+                "salinity/density",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SDRON-SURF0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-11-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Saildrone Inc. 1050 W Tower Ave, Alameda, CA 94501",
+            "series-name": "Saildrone Baja field campaign surface and ADCP measurements",
             "spatial": "-125.55 28.01 -115.52 37.82",
+            "temporal": "2018-04-11T18:00:00Z/2018-06-11T20:17:26Z",
             "theme": [
                 "Saildrone Baja",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Saildrone  Baja field campaign surface and ADCP measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/657/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
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
-            "identifier": "DASHLINK_657",
             "description": "The following zip files contain individual flight recorded data in Matlab file format. There are 186 parameters each with a data structure that contains the following:\r\n\r\n<pre>\r\n-sensor recordings\r\n-sampling rate\r\n-units\r\n-parameter description\r\n-parameter ID\r\n</pre>",
-            "title": "Flight Data For Tail 680",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_1.zip",
-                    "description": "Tail 680 Set 1",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 680 Set 1",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_1.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_680_1.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_2.zip",
-                    "description": "Tail 680 Set 2",
                     "@type": "dcat:Distribution",
+                    "description": "Tail 680 Set 2",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_2.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_680_2.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_3.zip",
-                    "description": "Tail_680 Set 3\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_680 Set 3\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_3.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_680_3.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_4.zip",
-                    "description": "Tail_680 Set 4\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_680 Set 4\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_4.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_680_4.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_5.zip",
-                    "description": "Tail_680 Set 5\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_680 Set 5\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_5.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_680_5.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_6.zip",
-                    "description": "Tail_680 Set 6\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_680 Set 6\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_6.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_680_6.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_7.zip",
-                    "description": "Tail_680 Set 7\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_680 Set 7\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_7.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_680_7.zip"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_8.zip",
-                    "description": "Tail_680 Set 8\n",
                     "@type": "dcat:Distribution",
+                    "description": "Tail_680 Set 8\n",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/Tail_680_8.zip",
+                    "mediaType": "application/zip",
                     "title": "Tail_680_8.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_657",
+            "issued": "2012-12-04",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/657/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Flight Data For Tail 680"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PWS-2-SA-4.0SEC",
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
+            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 1 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Jovian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of intensities (16 channels) is the time of the beginning of the scan. During data gaps where complete 4-second spectra are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. When one or more channels are missing within a scan, the missing measurements are zero-filled. Data are edited but not calibrated. The data numbers in this data set can be plotted in raw form for event searches and simple trend analysis since they are roughly proportional to the log of the electric field strength. Calibration procedures and tables are provided for use with this data set described below.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pws-2-sa-4.0sec_4tt4-iicq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PWS-2-SA-4.0SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pws-2-sa-4.0sec_4tt4-iicq",
-            "description": "This data set consists of 4-second edited, wave electric field intensities from the Voyager 1 Plasma Wave Receiver spectrum analyzer obtained in the vicinity of the Jovian magnetosphere. For each 4-second interval, a field strength is determined for each of the 16 spectrum analyzer channels whose center frequencies range from 10 Hertz to 56.2 kiloHertz and which are logarithmically spaced in frequency, four channels per decade. The time associated with each set of intensities (16 channels) is the time of the beginning of the scan. During data gaps where complete 4-second spectra are missing, no entries exist in the file, that is, the gaps are not zero-filled or tagged in any other way. When one or more channels are missing within a scan, the missing measurements are zero-filled. Data are edited but not calibrated. The data numbers in this data set can be plotted in raw form for event searches and simple trend analysis since they are roughly proportional to the log of the electric field strength. Calibration procedures and tables are provided for use with this data set described below.",
-            "title": "VOYAGER 1 JUP PLASMA SPECTROMETER EDITED SPEC 4.0SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 1 JUP PLASMA SPECTROMETER EDITED SPEC 4.0SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5D-OBP4B",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-10-01. ECCO Ocean Bottom Pressure - Daily Mean llc90 Grid (Version 4 Release 4 Errata). Version V4r4b. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5D-OBP4B.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean pressure"
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
-            "identifier": "C2129195053-POCLOUD",
-            "description": "This dataset provides daily-averaged ocean bottom pressure and model ocean bottom pressure anomaly on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4b (V4r4b) ocean and sea-ice state estimate. V4r4b is an errata for ECCO Version 4, Release 4 (V4r4). Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4b is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4b include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4b covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean Bottom Pressure - Daily Mean llc90 Grid (Version 4 Release 4b)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides daily-averaged ocean bottom pressure and model ocean bottom pressure anomaly on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4b (V4r4b) ocean and sea-ice state estimate. V4r4b is an errata for ECCO Version 4, Release 4 (V4r4). Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4b is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4b include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4b covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5D-OBP4B",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5D-OBP4B",
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
-                    "description": "The project website for the ECCO Consortium",
                     "@type": "dcat:Distribution",
+                    "description": "The project website for the ECCO Consortium",
+                    "downloadURL": "https://www.ecco-group.org",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/",
-                    "description": "Software maintained by ECCO Consortium on GitHub",
                     "@type": "dcat:Distribution",
+                    "description": "Software maintained by ECCO Consortium on GitHub",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_reproduction_howto.pdf",
-                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_reproduction_howto.pdf",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_user_guide.pdf",
-                    "description": "ECCO Version 4 Release 4 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_synopsis.pdf",
-                    "description": "Synopsis of ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO Version 4 Release 4",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_synopsis.pdf",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_overview_plots.pdf",
-                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/ecco/docs/v4r4_overview_plots.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5D-OBP4B",
-                    "description": "Access the data set landing page for the collection",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection",
+                    "downloadURL": "https://doi.org/10.5067/ECL5D-OBP4B",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2129195053-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2129195053-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2129195053-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2129195053-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ecco-group.org/docs/ECCO_V4r4_errata.pdf",
-                    "description": "ECCO V4r4b (V4r4 Errata) Document",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO V4r4b (V4r4 Errata) Document",
+                    "downloadURL": "https://ecco-group.org/docs/ECCO_V4r4_errata.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View an important notice for this dataset"
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
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_OBP_LLC0090GRID_DAILY_V4R4.jpg",
+            "identifier": "C2129195053-POCLOUD",
+            "issued": "1992-01-01",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5D-OBP4B",
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
+            "title": "ECCO Ocean Bottom Pressure - Daily Mean llc90 Grid (Version 4 Release 4b)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MODST-8D4N9",
             "citation": "NASA OBPG. 2020-01-15. MODIS Terra Level 3 SST Thermal IR 8 Day 4km Nighttime. Version 2019.0. MODIS Terra Global Level 3 Mapped SST. OBPG, Goddard Space Flight Center  Greenbelt, MD,US. Archived by National Aeronautics and Space Administration, U.S. Government, OBPG. https://doi.org/10.5067/MODST-8D4N9. https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html. NASA OBPG, OBPG, 2020-01-15, MODIS Terra Level 3 SST Thermal IR 8 Day 4km Nighttime V2019.0, https://podaac-tools.jpl.nasa.gov/drive/files/allData/modis/L3/docs/modis_sst.html.",
-            "issued": "2019-12-14",
-            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-14",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2015.04.023",
-                "https://doi.org/10.1175/JTECH-D-18-0103.1"
-            ],
-            "keyword": [
-                "oceans",
-                "national geospatial data asset",
-                "ocean temperature",
-                "ngda",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036882292-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "Day and night spatially gridded (L3) global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODST-8D4N4",
-            "release-place": "OBPG, Goddard Space Flight Center  Greenbelt, MD,US",
-            "series-name": "MODIS Terra Level 3 SST Thermal IR 8 Day 4km Nighttime",
             "creator": "NASA OBPG",
-            "title": "MODIS Terra Level 3 SST Thermal IR 8 Day 4km Nighttime V2019.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V2019.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Day and night spatially gridded (L3) global NASA skin sea surface temperature (SST) products from the Moderate-resolution Imaging Spectroradiometer (MODIS) onboard the Terra satellite.  Average daily, weekly (8 day), monthly and annual skin SST products are available at both 4.63 and 9.26 km spatial resolution. Terra was launched by NASA on December 18, 1999, into a sun synchronous, polar orbit with a daylight descending node at 10:30 am, to study the global dynamics of the Earth atmosphere, land and oceans. The MODIS captures data in 36 spectral bands at a variety of spatial resolutions. Two SST products can be present in these files. The first is a skin SST produced for both day and night observations, derived from the long wave IR 11 and 12 micron  wavelength channels, using a modified nonlinear SST algorithm intended to provide continuity with SST derived from heritage and current NASA sensors. At night, a second SST product is produced using the mid-infrared 3.95 and 4.05 micron  channels which are unique to MODIS; the SST derived from these measurements is identified as SST4. The SST4 product has lower uncertainty, but due to sun glint can only be produced at night. To generate the L3 products the L2 pixels are binned into an integerized sinusoidal area grid (ISEAG) and mapped into an equidistant cylindrical (also known as Platte Carre) projection.  Additional projection detailed can be found at https://oceancolor.gsfc.nasa.gov/docs/format/ The NASA MODIS L3 SST data products are generated by the NASA Ocean Biology Processing Group (OBPG) Peter Minnett and his team at the Rosenstiel School of Marine and Atmospheric Science (RSMAS) are responsible for sea surface temperature algorithm development, error statistics and quality flagging. JPL acquires and distributes MODIS ocean L3 SST data from the OBPG as the official Physical Oceanography Data Archive (PO.DAAC) for SST. The R2019 superseded the previous v2014.1 datasets which can be found at https://doi.org/10.5067/MODST-8D4N4",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODST-8D4N9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODST-8D4N9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/r2019/sst/",
-                    "description": "OBPG SST Reprocessing v2019.0 summary",
                     "@type": "dcat:Distribution",
+                    "description": "OBPG SST Reprocessing v2019.0 summary",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/r2019/sst/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
-                    "description": "Additional resource to help better understand the algorithm(s) used in producing and/or calibrating/validating the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "Additional resource to help better understand the algorithm(s) used in producing and/or calibrating/validating the dataset",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V2019.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V2019.0.jpg",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/modis/open/L3/docs/modis_sst.html",
-                    "description": "describes all the level 3 MODIS data",
                     "@type": "dcat:Distribution",
+                    "description": "describes all the level 3 MODIS data",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/modis/open/L3/docs/modis_sst.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://oceancolor.gsfc.nasa.gov",
-                    "description": "Ocean Biology Processing Group homepage",
                     "@type": "dcat:Distribution",
+                    "description": "Ocean Biology Processing Group homepage",
+                    "downloadURL": "http://oceancolor.gsfc.nasa.gov",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882292-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882292-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882292-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882292-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/MODIS_TERRA_L3_SST_THERMAL_8DAY_4KM_NIGHTTIME_V2019.0.jpg",
+            "identifier": "C2036882292-POCLOUD",
+            "issued": "2019-12-14",
+            "keyword": [
+                "oceans",
+                "national geospatial data asset",
+                "ocean temperature",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODST-8D4N9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1016/j.rse.2015.04.023",
+                "https://doi.org/10.1175/JTECH-D-18-0103.1"
+            ],
+            "release-place": "OBPG, Goddard Space Flight Center  Greenbelt, MD,US",
+            "series-name": "MODIS Terra Level 3 SST Thermal IR 8 Day 4km Nighttime",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "EOS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS Terra Level 3 SST Thermal IR 8 Day 4km Nighttime V2019.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-KEMCRUISE1-V2.0",
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
-                "new horizons kuiper belt extended mission",
-                "dust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the                             New Horizons Student Dust Counter instrument during the                  CRUISE TO FIRST KBO ENCOUNTER mission phase.                             This is VERSION 2.0 of this data set.                                    This data set contains data acquired by the spacecraft between           10/17/2016 and 08/13/2018. This is the complete dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-kemcruise1-v2.0_4tuh-9cku",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission",
+                "dust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-SDC-2-KEMCRUISE1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-sdc-2-kemcruise1-v2.0_4tuh-9cku",
-            "description": "This data set contains Raw data taken by the                             New Horizons Student Dust Counter instrument during the                  CRUISE TO FIRST KBO ENCOUNTER mission phase.                             This is VERSION 2.0 of this data set.                                    This data set contains data acquired by the spacecraft between           10/17/2016 and 08/13/2018. This is the complete dataset.",
-            "title": "NEW HORIZONS                            \n      SDC KEMCRUISE1                                                          \n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SDC KEMCRUISE1                                                          \n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYDFNSS.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Science Team. 2017-10-01. MODIS/Aqua Atmosphere FluxNet Subsetting Product. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MYDFNSS.061. https://doi.org/10.5067/MODIS/MYDFNSS.061.",
-            "issued": "2017-10-01",
-            "temporal": "2002-07-04T11:25:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-10",
-            "keyword": [
-                "earth science",
-                "ngda",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "visible wavelengths",
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
-            "identifier": "C1444318098-LAADS",
-            "description": "The MODIS/Aqua Atmosphere FluxNet Subsetting Product (MODFNSS) consists of MODIS Atmosphere and Ancillary Products subsets that are generated over a global network of micrometeorological flux measurement (FLUXNET) sites. The process of generating cutouts for these sites involves locating and identifying a subset of sites taken from a global FLUXNET that are within the spatial coverage of a 5 minute Level 2 MODIS granule and extracting 0.5 x 0.5 degree cutouts. The MODFNSS data set consists of subsets for around 400 sites out of the total flux tower sites around the globe. There is one file per site with around 55 Science Data Sets (SDS) such as at-aperture radiances for 36 discrete MODIS bands, Cloud Mask, and Water Vapor, etc",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Science Team",
-            "title": "MODIS/Aqua Atmosphere FluxNet Subsetting Product",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Atmosphere FluxNet Subsetting Product (MODFNSS) consists of MODIS Atmosphere and Ancillary Products subsets that are generated over a global network of micrometeorological flux measurement (FLUXNET) sites. The process of generating cutouts for these sites involves locating and identifying a subset of sites taken from a global FLUXNET that are within the spatial coverage of a 5 minute Level 2 MODIS granule and extracting 0.5 x 0.5 degree cutouts. The MODFNSS data set consists of subsets for around 400 sites out of the total flux tower sites around the globe. There is one file per site with around 55 Science Data Sets (SDS) such as at-aperture radiances for 36 discrete MODIS bands, Cloud Mask, and Water Vapor, etc",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDFNSS.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYDFNSS.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDFNSS.061",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYDFNSS.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDFNSS--61",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MYDFNSS--61",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDFNSS/",
-                    "description": "Direct access to MYDFNSS C6.1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MYDFNSS C6.1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYDFNSS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDFNSS/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/61/MYDFNSS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://fluxnet.ornl.gov/",
-                    "description": "The FluxNet project page to see a list of FluxNet sites.",
                     "@type": "dcat:Distribution",
+                    "description": "The FluxNet project page to see a list of FluxNet sites.",
+                    "downloadURL": "https://fluxnet.ornl.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "identifier": "C1444318098-LAADS",
+            "issued": "2017-10-01",
+            "keyword": [
+                "earth science",
+                "ngda",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "visible wavelengths",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYDFNSS.061",
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
+            "temporal": "2002-07-04T11:25:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Atmosphere FluxNet Subsetting Product"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1787",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Potter, S., B.M. Rogers, and C. Dieleman. 2020. ABoVE: Spatial Estimates of Carbon Combustion from Wildfires across SK, Canada, 2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1787",
-            "issued": "2020-07-15",
-            "temporal": "2015-04-06T00:00:00Z/2015-08-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "soils",
-                "biosphere",
-                "earth science",
-                "natural hazards",
-                "human dimensions",
-                "land surface",
-                "ecosystems",
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
-            "identifier": "C2143401918-ORNL_CLOUD",
             "description": "This dataset provides spatial estimates of carbon combustion from all 2015 wildfire burned areas across Saskatchewan, Canada, on a 30-m grid. Carbon combustion (kg C/m2) was derived from post-fire field measurements of carbon stocks completed in 2016 at 47 stands that burned during three 2015 Saskatchewan wildfires (Egg, Philion, and Brady) and at 32 unburned stands in adjacent areas. The study areas covered two ecozones (Boreal Plains and Boreal Shield), two stand-replacing history types (fire and timber harvest), three soil moisture classes (xeric, mesic, and subhygric), and three stand dominance classifications (coniferous, deciduous, and mixed). To spatially extrapolate estimates of combustion to all 2015 fires in Saskatchewan, a predictive radial support vector machine model was trained on the 47 burned stands with associated environmental variables and geospatial predictors and applied to historical fire areas. The dataset also includes uncertainty estimates represented as per pixel standard deviations of model estimates derived using a Monte Carlo analysis.",
-            "graphic-preview-description": "Spatial estimates of total carbon combustion at 30-m resolution across the 2015 fire perimeters in Saskatchewan (a) and sampled fires (b, c, d). The spatial extents of sampled fires are shown as blue rectangles in (a). Source: Dieleman et al., 2020",
-            "title": "ABoVE: Spatial Estimates of Carbon Combustion from Wildfires across SK, Canada, 2015",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Post_Fire_C_Emissions_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1787",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1787",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Post_Fire_C_Emissions/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Post_Fire_C_Emissions/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Post_Fire_C_Emissions.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Post_Fire_C_Emissions.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1787",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1787",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Post_Fire_C_Emissions/comp/Post_Fire_C_Emissions.pdf",
-                    "description": "ABoVE: Spatial Estimates of Carbon Combustion from Wildfires across SK, Canada, 2015: Post_Fire_C_Emissions.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Spatial Estimates of Carbon Combustion from Wildfires across SK, Canada, 2015: Post_Fire_C_Emissions.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Post_Fire_C_Emissions/comp/Post_Fire_C_Emissions.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Post_Fire_C_Emissions_Fig1.png",
-                    "description": "Spatial estimates of total carbon combustion at 30-m resolution across the 2015 fire perimeters in Saskatchewan (a) and sampled fires (b, c, d). The spatial extents of sampled fires are shown as blue rectangles in (a). Source: Dieleman et al., 2020",
                     "@type": "dcat:Distribution",
+                    "description": "Spatial estimates of total carbon combustion at 30-m resolution across the 2015 fire perimeters in Saskatchewan (a) and sampled fires (b, c, d). The spatial extents of sampled fires are shown as blue rectangles in (a). Source: Dieleman et al., 2020",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Post_Fire_C_Emissions_Fig1.png",
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
+            "graphic-preview-description": "Spatial estimates of total carbon combustion at 30-m resolution across the 2015 fire perimeters in Saskatchewan (a) and sampled fires (b, c, d). The spatial extents of sampled fires are shown as blue rectangles in (a). Source: Dieleman et al., 2020",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Post_Fire_C_Emissions_Fig1.png",
+            "identifier": "C2143401918-ORNL_CLOUD",
+            "issued": "2020-07-15",
+            "keyword": [
+                "soils",
+                "biosphere",
+                "earth science",
+                "natural hazards",
+                "human dimensions",
+                "land surface",
+                "ecosystems",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1787",
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
             "spatial": "-116.06 51.19 -100.17 61.24",
+            "temporal": "2015-04-06T00:00:00Z/2015-08-11T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Spatial Estimates of Carbon Combustion from Wildfires across SK, Canada, 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/58ILBIVGP1RC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLASIC07 PALS Brightness Temperature Data V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/58ILBIVGP1RC.",
-            "issued": "2007-06-11",
-            "temporal": "2007-06-11T00:00:00Z/2007-07-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-07-06",
-            "keyword": [
-                "spectral/engineering",
-                "microwave",
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
-            "identifier": "C1000001422-NSIDC_ECS",
             "description": "This data set contains brightness temperature data obtained by the Passive Active L-band System (PALS) microwave aircraft radiometer instrument as part of the Cloud and Land Surface Interaction Campaign 2007 (CLASIC07).",
-            "title": "CLASIC07 PALS Brightness Temperature Data V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F58ILBIVGP1RC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F58ILBIVGP1RC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/CL07PLTB.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/CL07PLTB.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001422-NSIDC_ECS&m=25.751953125%21-97.716796875%214%211%210%210%2C2&q=CLASIC07&ok=CLASIC07",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
```

