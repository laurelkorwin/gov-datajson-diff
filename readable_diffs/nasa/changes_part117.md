# Change History for nasa.json (Part 117)

### Changes from 31606f9 to dd2190f (Part 106/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ground_Oildale_Data_1",
-                    "description": "DOI for DISCOVERAQ_California_Ground_Oildale_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for DISCOVERAQ_California_Ground_Oildale_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ground_Oildale_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2369088561-LARC_ASDC",
-                    "description": "Earthdata Search client for DISCOVERAQ_California_Ground_Oildale_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for DISCOVERAQ_California_Ground_Oildale_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2369088561-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_Ground_Oildale_Data_1/",
-                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_Ground_Oildale_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DISCOVERAQ_California_Ground_Oildale_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DISCOVER-AQ/California_Ground_Oildale_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2369088561-LARC_ASDC",
+            "issued": "2021-08-25",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/DISCOVERAQ_California_Ground_Oildale_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -130.0 25.0 -70.0 45.0 -70.0 45.0 -130.0 25.0 -130.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-01-16T00:00:00Z/2013-02-14T23:59:59.999Z",
             "theme": [
                 "DISCOVER-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DISCOVER-AQ California Deployment Oildale Ground Site Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-CRUISE2-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-cruise2-v1.0_my24-atan",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-CRUISE2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-cruise2-v1.0_my24-atan",
-            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
-            "title": "NEAR SPICE KERNELS CRUISE2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR SPICE KERNELS CRUISE2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IRRDR-CLEANED-EXT5-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-irrdr-cleaned-ext5-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars express",
                 "calibration",
@@ -1110752,409 +1110754,418 @@
                 "deimos",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-SPI-2-IRRDR-CLEANED-EXT5-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-spi-2-irrdr-cleaned-ext5-v1.0",
-            "description": "The Mars Express SPICAM level 1A IR data set contains clean measurements from the infrared SPICAM spectrometer collected during the nominal MARS phases",
-            "title": "MEX EXT5 SPICAM MARS CLEANED IR RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MEX EXT5 SPICAM MARS CLEANED IR RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/JVZDF9954H0H",
             "citation": "Nadia Smith. 2019-01-15. SNDRSNIML2PLEVCPSN. Version 2.1. Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Normal Spectral Resolution: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/JVZDF9954H0H. https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2PLEVCPSN_2.1.html. Digital Science Data.",
-            "issued": "2012-01-20",
-            "temporal": "2012-01-20T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://doi.org/DOI  10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.1016/S0022-4073(97)00169-6",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric water vapor",
-                "ocean temperature",
-                "land surface",
-                "surface thermal properties",
-                "earth science",
-                "oceans",
-                "atmospheric chemistry",
-                "clouds",
-                "air quality",
-                "altitude"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Nadia Smith",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2791419732-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite). This file contains the fixed Pressure Level product (PLEV) variables derived from the CLIMCAPS algorithm using Normal Spectral Resolution data from the Suomi-NPP satellite. They include including gas mixing ratio profiles, column totals, surface values, tropopause properties, and relative humidity, together with per-field quality flagging. The profiles are specified at the surface and layer boundaries and are estimated from layer amounts using the L2 algorithm \n\nAn level 2 granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day. \n\nThe CLIMCAPS algorithm uses data from the second Modern-Era Retrospective analysis for Research and Applications (MERRA-2) as a first-guess for the atmospheric state.  Because MERRA-2 products typically have a latency from 3 to 7 weeks, so too do the CLIMCAPS products.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNIML2PLEVCPSN",
-            "creator": "Nadia Smith",
-            "graphic-preview-description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
-            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Normal Spectral Resolution: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRSNIML2PLEVCPSN) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2PLEVCPSN_2.1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJVZDF9954H0H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJVZDF9954H0H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2PLEVCPSN_2.1.png",
-                    "description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2PLEVCPSN_2.1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2PLEVCPSN_2.1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML2PLEVCPSN_2.1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level2/SNDRSNIML2PLEVCPSN.2.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level2/SNDRSNIML2PLEVCPSN.2.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level2/SNDRSNIML2PLEVCPSN.2.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level2/SNDRSNIML2PLEVCPSN.2.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML2PLEVCPSN+2.1",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML2PLEVCPSN+2.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.L2.V2.1.README.pdf",
-                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS L2 Product User Guide:File Format and Definition",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.L2.V2.1.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
-                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS PLEV_CPS",
                     "@type": "dcat:Distribution",
+                    "description": "Mapping of data variables from v2 CLIMCAPS to V2.1 CLIMCAPS PLEV_CPS",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/L2_CLIMCAPS_V2.to.V2.1_Mapping.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.V2.1.ATBD.pdf",
-                    "description": "CLIMCAPS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.PLEV.CPS.V2.1.ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CLIMCAPS Level 2 Pressure Level product.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML2PLEVCPSN_2.1.png",
+            "identifier": "C2791419732-GES_DISC",
+            "issued": "2012-01-20",
+            "keyword": [
+                "atmospheric temperature",
+                "atmosphere",
+                "atmospheric water vapor",
+                "ocean temperature",
+                "land surface",
+                "surface thermal properties",
+                "earth science",
+                "oceans",
+                "atmospheric chemistry",
+                "clouds",
+                "air quality",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/JVZDF9954H0H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-21",
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
+            "series-name": "SNDRSNIML2PLEVCPSN",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-20T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 2 CLIMCAPS Normal Spectral Resolution: Atmospheric state at Standard Pressure Levels derived from CLIMCAPS V2.1 (SNDRSNIML2PLEVCPSN) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67P-M26-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67p-m26-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67P-M26-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67p-m26-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP026 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP026 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/GOES/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. GOES IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/GOES/DATA101",
-            "issued": "2022-06-07",
-            "temporal": "2020-01-01T00:01:18Z/2022-02-28T23:58:56Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "visible wavelengths",
-                "infrared wavelengths",
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
-            "identifier": "C1995568158-GHRC_DAAC",
             "description": "The GOES IMPACTS dataset consists of single reflective band radiance products from the Advanced Baseline Imager (ABI) onboard the GOES-16 geostationary satellite. These data were collected in support of the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast (2020-2022). The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. The GOES IMPACTS dataset files are available in netCDF-4 format from January 1, 2020 through February 28, 2022. This dataset contains data from the GOES-16 CONUS and Mesoscale sectors, although IMPACTS uses a subset of the GOES-16 CONUS domain. The complete collection of GOES data is available from the NOAA Comprehensive Large Array-Data Stewardship System (CLASS). It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "GOES IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FGOES%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FGOES%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=goesimpacts&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=goesimpacts&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.goes-r.gov/products/RIMPs/RIMP_ABI-L2_DSR-RSR_v1.0.pdf",
-                    "description": "GOES - R Series: ABI L2+ Surface DSR-RSR Beta, Provisional and Full Validation RIMP",
                     "@type": "dcat:Distribution",
+                    "description": "GOES - R Series: ABI L2+ Surface DSR-RSR Beta, Provisional and Full Validation RIMP",
+                    "downloadURL": "https://www.goes-r.gov/products/RIMPs/RIMP_ABI-L2_DSR-RSR_v1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://www.goes-r.gov/spacesegment/ABI-tech-summary.html",
-                    "description": "ABI Technical Summary Chart",
                     "@type": "dcat:Distribution",
+                    "description": "ABI Technical Summary Chart",
+                    "downloadURL": "https://www.goes-r.gov/spacesegment/ABI-tech-summary.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.goes-r.gov/spacesegment/abi.html",
-                    "description": "Instruments: Advanced Baseline Imager",
                     "@type": "dcat:Distribution",
+                    "description": "Instruments: Advanced Baseline Imager",
+                    "downloadURL": "https://www.goes-r.gov/spacesegment/abi.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/impacts/content/IMPACTS",
-                    "description": "IMPACTS Field Campaign Information",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Information",
+                    "downloadURL": "https://espo.nasa.gov/impacts/content/IMPACTS",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/GOES/doc/goesimpacts_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/GOES/doc/goesimpacts_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/impacts",
-                    "description": "IMPACTS Field Campaign Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Project Page",
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
+            "identifier": "C1995568158-GHRC_DAAC",
+            "issued": "2022-06-07",
+            "keyword": [
+                "visible wavelengths",
+                "infrared wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/GOES/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-114.64 8.24104 -50.1259 51.4165",
+            "temporal": "2020-01-01T00:01:18Z/2022-02-28T23:58:56Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOES IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MO-M-RSS-1-OIDR-V1.0",
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
-                "mars observer"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The data set consists of several CD-WO volumes which contain radiometric and open loop data acquired from the Mars Observer spacecraft during its Cruise between Earth and Mars. The basic data are supplemented by ancillary data including DSN weather files and media calibrations, spacecraft maneuver information, and operations schedules. There are fourteen data types.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mo-m-rss-1-oidr-v1.0_my6u-kfmc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars observer"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MO-M-RSS-1-OIDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mo-m-rss-1-oidr-v1.0_my6u-kfmc",
-            "description": "The data set consists of several CD-WO volumes which contain radiometric and open loop data acquired from the Mars Observer spacecraft during its Cruise between Earth and Mars. The basic data are supplemented by ancillary data including DSN weather files and media calibrations, spacecraft maneuver information, and operations schedules. There are fourteen data types.",
-            "title": "MO MARS RADIO SCIENCE 1 ORIGINAL/INTERMEDIATE DATA REC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MO MARS RADIO SCIENCE 1 ORIGINAL/INTERMEDIATE DATA REC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3822-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-15T13:45:39 to 2015-09-15T16:24:53.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3822-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3822-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3822-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-15T13:45:39 to 2015-09-15T16:24:53.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3822 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3822 V1.0"
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
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000209",
             "issued": "2018-06-25",
-            "temporal": "2008-08-04/2014-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "gbm",
                 "astrophysics",
@@ -1111167,1403 +1111178,1362 @@
                 "solar flares",
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
-            "identifier": "NASA-0000209",
-            "description": "Fermi is a powerful space observatory that will open a wide window on the universe. Gamma rays are the highest-energy form of light, and the gamma-ray sky is spectacularly different from the one we perceive with our own eyes. With a huge leap in all key capabilities, Fermi data will enable scientists to answer persistent questions across a broad range of topics, including supermassive black-hole systems, pulsars, the origin of cosmic rays, and searches for signals of new physics.",
-            "title": "LAT Data Server",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-04/2014-06-25",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT Data Server"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-NORMAL-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-normal-ops-v1.0_my97-tt6f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-PANCAM-5-NORMAL-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-pancam-5-normal-ops-v1.0_my97-tt6f",
-            "description": "NULL",
-            "title": "MER 2 MARS PANORAMIC CAMERA\n                                      SURFACE NORMAL RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS PANORAMIC CAMERA\n                                      SURFACE NORMAL RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PRA-3-RDR-LOWBAND-6SEC-V1.0",
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
+            "description": "This data set (VG1-J-PRA-3-RDR-LOWBAND-6SEC-V1.0) contains data acquired by the Voyager-1 Planetary Radio Astronomy (PRA) instrument during the Jupiter encounter. The bounding time interval set for most Voyager 1 Jupiter PDS data sets is the Voyager project defined 'far encounter' mission phase boundary (1979-02-28 to 1979-03-22). Since, however, the PRA instrument is able to observe planetary phenomenon at much larger ranges than other fields and particles experiments, this boundary is artificial with respect to PRA.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pra-3-rdr-lowband-6sec-v1.0_myae-xwkf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-PRA-3-RDR-LOWBAND-6SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pra-3-rdr-lowband-6sec-v1.0_myae-xwkf",
-            "description": "This data set (VG1-J-PRA-3-RDR-LOWBAND-6SEC-V1.0) contains data acquired by the Voyager-1 Planetary Radio Astronomy (PRA) instrument during the Jupiter encounter. The bounding time interval set for most Voyager 1 Jupiter PDS data sets is the Voyager project defined 'far encounter' mission phase boundary (1979-02-28 to 1979-03-22). Since, however, the PRA instrument is able to observe planetary phenomenon at much larger ranges than other fields and particles experiments, this boundary is artificial with respect to PRA.",
-            "title": "VG1 JUP PRA CALIBRATED HI-RES LOW FREQ.\n                                      REC. BAND DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 JUP PRA CALIBRATED HI-RES LOW FREQ.\n                                      REC. BAND DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/DMDMOR7JSIEG",
             "citation": "NASA/GSFC. 2021-04-22. TIROS2L1FMRT. Version 001. TIROS-2 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/DMDMOR7JSIEG. https://disc.gsfc.nasa.gov/datacollection/TIROS2L1FMRT_001.html. Digital Science Data.",
-            "issued": "2021-04-01",
-            "temporal": "1960-11-23T00:00:00Z/1961-04-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-01",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2046458866-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "TIROS-2 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data (FMRT) product contains radiances expressed in five infrared/visible wavelength regions, expressed in either equivalent blackbody temperature (IR channels 1 and 2) or effective radiant emmitance (visible channels 3 and 5). The data will trace an elliptical, parabolic, or hyperbolic pattern on the ground due to the rotating of the instrument about the satellite spin axis. There is one orbit per file. The data were originally written on IBM 7094 machines, and these have been recovered from magnetic tapes, referred to as the Final Meteorological Radiation Tapes (FMRT). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe TIROS-2 satellite was successfully launched on November 23, 1960. The Medium-Resolution Scanning Radiometer experiment successfully returned data for about five months, becoming the first radiometer to make meteorlogical measurements from space. Three follow-on instruments were flown on TIROS-3, -4 and -7. Initially, all channels performed normally. However, channels 1 and 4 gradually deteriorated and by January 1961 were useless. The signal to noise ratio of channels 3 and 5 was extremely low, and the output was highly questionable. The instrument is a five channel radiometer with a 55 km footprint at nadir with the following characteristics:\n\nChannel 1: 6.0 to 6.5 microns - water vapor absorption\nChannel 2: 8.0 to 12.0 microns - atmospheric window\nChannel 3: 0.2 to 6.0 microns - reflected solar radiation\nChannel 4: 8.0 to 30 microns - terrestial radiation\nChannel 5: 0.55 to 0.75 microns - response to the TV system\n\nThe Principal Investigator for these data was Joseph D. Barksdale from NASA Goddard Space Flight Center. This product was previously available from the NSSDC with the identifier ESAD-00113 (old ID 60-016A-02A).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TIROS2L1FMRT",
-            "creator": "NASA/GSFC",
-            "title": "TIROS-2 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS2L1FMRT) at GES DISC",
-            "graphic-preview-description": "TIROS-2 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on June 19, 1963.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS2L1FMRT_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDMDMOR7JSIEG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FDMDMOR7JSIEG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS2L1FMRT_Sample.png",
-                    "description": "TIROS-2 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on June 19, 1963.",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS-2 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on June 19, 1963.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS2L1FMRT_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS2L1FMRT.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS2L1FMRT.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TIROS2L1FMRT",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TIROS2L1FMRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS2L1FMRT.001/doc/README.TIROS2FMRT.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS2L1FMRT.001/doc/README.TIROS2FMRT.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/Tiros_II_Radiation_Data_Users_Manual.pdf",
-                    "description": "TIROS II Radiation Data Users' Manual",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS II Radiation Data Users' Manual",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/Tiros_II_Radiation_Data_Users_Manual.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/TIROS_2_Radiation_Data_Catalog.pdf",
-                    "description": "TIROS II Radiation Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS II Radiation Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/TIROS_2_Radiation_Data_Catalog.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TIROS/Tiros_Inventory.xlsx",
-                    "description": "TIROS Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TIROS/Tiros_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "TIROS-2 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on June 19, 1963.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS2L1FMRT_Sample.png",
+            "identifier": "C2046458866-GES_DISC",
+            "issued": "2021-04-01",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/DMDMOR7JSIEG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TIROS2L1FMRT",
             "spatial": "-180.0 -66.0 180.0 66.0",
+            "temporal": "1960-11-23T00:00:00Z/1961-04-13T23:59:59.999Z",
             "theme": [
                 "TIROS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TIROS-2 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS2L1FMRT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67PCHURYUMOV-M13-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission, covering the period from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67pchuryumov-m13-v1.0_myfr-ds7x",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67PCHURYUMOV-M13-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67pchuryumov-m13-v1.0_myfr-ds7x",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 1 phase of the Rosetta mission, covering the period from 2015-02-10T23:25:00.000 to 2015-03-10T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP013 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP013 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1950",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and R.O. Green. 2022. MASTER: HyspIRI Airborne Campaign, California,  Summer 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1950",
-            "issued": "2024-05-10",
-            "temporal": "2017-06-07T17:51:32Z/2017-06-28T21:45:55Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-10",
-            "keyword": [
-                "land surface",
-                "spectral/engineering",
-                "visible wavelengths",
-                "surface thermal properties",
-                "infrared wavelengths",
-                "surface radiative properties",
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
-            "identifier": "C2731664497-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) and Level 2 (L2) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected as part of the Hyperspectral Infrared Imager (HyspIRI) airborne campaign during 9 flights aboard a NASA ER-2 aircraft over southern California and western Nevada, U.S., from 2017-06-07 to 2017-06-28. Two flights on 2017-06-26 and 2017-06-28 were flown jointly for the Student Airborne Research Program (SARP). SARP was an eight-week summer program for junior and senior undergraduate students to acquire hands-on research experience in all aspects of a scientific campaign using airborne science laboratories. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 50-meter spatial resolution. Derived L2 data products are emissivity in 5 bands in thermal infrared range (8.58 to 12.13 micrometers) and land surface temperature. The L1B file format is HDF-4, and L2 products are provided in ENVI and KMZ formats. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and an RGB composite image from flight track 6 as acquired on 28 June 2017 near Mountain Pass, California, U.S. Source: MASTERL1B_1764700_06_20170628_1655_1701_V01.jpg",
-            "title": "MASTER: HyspIRI Airborne Campaign, California,  Summer 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Summer_2017_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1950",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1950",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/master/MASTER_HyspIRI_Summer_2017/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/master/MASTER_HyspIRI_Summer_2017/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Summer_2017.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Summer_2017.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1950",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1950",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_HyspIRI_Summer_2017/comp/MASTER_HyspIRI_Summer_2017.pdf",
-                    "description": "MASTER: HyspIRI Airborne Campaign, California,  Summer 2017: MASTER_HyspIRI_Summer_2017.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: HyspIRI Airborne Campaign, California,  Summer 2017: MASTER_HyspIRI_Summer_2017.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_HyspIRI_Summer_2017/comp/MASTER_HyspIRI_Summer_2017.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Summer_2017_Fig1.jpg",
-                    "description": "Single-band images and an RGB composite image from flight track 6 as acquired on 28 June 2017 near Mountain Pass, California, U.S. Source: MASTERL1B_1764700_06_20170628_1655_1701_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and an RGB composite image from flight track 6 as acquired on 28 June 2017 near Mountain Pass, California, U.S. Source: MASTERL1B_1764700_06_20170628_1655_1701_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Summer_2017_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and an RGB composite image from flight track 6 as acquired on 28 June 2017 near Mountain Pass, California, U.S. Source: MASTERL1B_1764700_06_20170628_1655_1701_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_HyspIRI_Summer_2017_Fig1.jpg",
+            "identifier": "C2731664497-ORNL_CLOUD",
+            "issued": "2024-05-10",
+            "keyword": [
+                "land surface",
+                "spectral/engineering",
+                "visible wavelengths",
+                "surface thermal properties",
+                "infrared wavelengths",
+                "surface radiative properties",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1950",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-123.75 31.95 -112.5 40.98",
+            "temporal": "2017-06-07T17:51:32Z/2017-06-28T21:45:55Z",
             "theme": [
                 "MASTER",
                 "HyspIRI Airborne",
                 "SARP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: HyspIRI Airborne Campaign, California,  Summer 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-D-GDDS-5-DUST-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains information on the dust environment in interplanetary space within the inner solar system and in the Jupiter system, within and without the Jovian magnetosphere and around the Galilean satellites.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-d-gdds-5-dust-v2.0_myhr-k82q",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "galileo",
                 "dust"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-D-GDDS-5-DUST-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-d-gdds-5-dust-v2.0_myhr-k82q",
-            "description": "This data set contains information on the dust environment in interplanetary space within the inner solar system and in the Jupiter system, within and without the Jovian magnetosphere and around the Galilean satellites.",
-            "title": "GALILEO DUST DETECTION SYSTEM V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO DUST DETECTION SYSTEM V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/CERES/ES8-FM2_L2.004",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-09-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/CERES/ES8-FM2_L2.004.",
-            "issued": "2017-08-18",
-            "temporal": "2000-02-29T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-10",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science"
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
-            "identifier": "C1419931602-LARC_ASDC",
             "description": "CER_ES8_Terra-FM2_Edition4 is the Clouds and the Earth's Radiant Energy System (CERES) Earth Radiation Budget Experiment (ERBE)-like Instantaneous Top-of-the-Atmosphere (TOA) Estimates Terra Flight Model 2 (FM2) Edition 4 data product, which was collected using the CERES-FM2 instrument on the Terra platform. Data collection for this product is ongiong.\r\n\r\nThe ERBE-like Footprint TOA Fluxes (ES-8) product contains 24 hours of instantaneous CERES data for a single scanner instrument, FM3 on the Aqua spacecraft. The ES-8 contains filtered radiances recorded every 0.01-second for the total (TOT), shortwave (SW), and window (WN) channels and the unfiltered SW, longwave (LW), and WN radiances. The SW and LW radiances at spacecraft altitude are converted to TOA fluxes with a scene identification algorithm and Angular Distribution Models (ADMs) which are \"like\" those used for the ERBE. The TOA fluxes, scene identification, and angular geometry are included on the ES-8.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful ERBE mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES ERBE-like Instantaneous TOA Estimates Terra FM2 Edition4",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FES8-FM2_L2.004",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FES8-FM2_L2.004",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/ES8-FM2_L2.004",
-                    "description": "DOI data set landing page for CER_ES8_Terra-FM2_Edition4",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ES8_Terra-FM2_Edition4",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/ES8-FM2_L2.004",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1419931602-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ES8_Terra-FM2_Edition4 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ES8_Terra-FM2_Edition4 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1419931602-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES8/Terra-FM2_Edition4/",
-                    "description": "ASDC Direct Data Download for CER_ES8_Terra-FM2_Edition4",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ES8_Terra-FM2_Edition4",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES8/Terra-FM2_Edition4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES8/Terra-FM2_Edition4/contents.html",
-                    "description": "OPeNDAP data access for CER_ES8_Terra-FM2_Edition4",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ES8_Terra-FM2_Edition4",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES8/Terra-FM2_Edition4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1419931602-LARC_ASDC",
+            "issued": "2017-08-18",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/CERES/ES8-FM2_L2.004",
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
+            "temporal": "2000-02-29T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES ERBE-like Instantaneous TOA Estimates Terra FM2 Edition4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/A192FWGA55G1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLPX-Airborne: Airborne Synthetic Aperture Radar (AIRSAR) Imagery, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/A192FWGA55G1.",
-            "issued": "2002-02-19",
-            "temporal": "2002-02-19T00:00:00Z/2003-03-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-03-30",
-            "keyword": [
-                "radar",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Chapman",
                 "hasEmail": "mailto:chapman@faldo.atmos.uiuc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386203823-NSIDCV0",
             "description": "Airborne Synthetic Aperture Radar (AIRSAR) is a side-looking imaging radar that is able to collect data irrespective of daylight or cloud cover. The AIRSAR instrument operated in two modes over each Cold Land Processes Field Experiment (CLPX) Meso-cell Study Area (MSA). In the first mode (POLSAR), polarimetric radar data were collected at P-, L-, and C-bands. In the second mode (TOPSAR), cross-track interferometry data were collected at C- and L-bands.",
-            "title": "CLPX-Airborne: Airborne Synthetic Aperture Radar (AIRSAR) Imagery, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FA192FWGA55G1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FA192FWGA55G1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0153_clpx_air_airsar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0153_clpx_air_airsar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0153_clpx_air_airsar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0153_clpx_air_airsar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0153_clpx_air_airsar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0153_clpx_air_airsar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0153_clpx_air_airsar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0153_clpx_air_airsar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/A192FWGA55G1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/A192FWGA55G1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/A192FWGA55G1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/A192FWGA55G1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386203823-NSIDCV0",
+            "issued": "2002-02-19",
+            "keyword": [
+                "radar",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/A192FWGA55G1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-03-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-106.7 39.9 -105.9 40.7",
+            "temporal": "2002-02-19T00:00:00Z/2003-03-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLPX-Airborne: Airborne Synthetic Aperture Radar (AIRSAR) Imagery, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-CVP1-COMMISSIONING1-V1.0",
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
+            "description": "This volume contains Experiment Data acquired by GIADA during 'Commissioning 1' phase. More in detail it refers to the data provided during the following in-flight tests: 'First GIADA switch ON' held on 03/04-04-2004. It also contains documentation which describes the GIADA experiment. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-cvp1-commissioning1-v1.0_myjj-mxrh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-CVP1-COMMISSIONING1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-cvp1-commissioning1-v1.0_myjj-mxrh",
-            "description": "This volume contains Experiment Data acquired by GIADA during 'Commissioning 1' phase. More in detail it refers to the data provided during the following in-flight tests: 'First GIADA switch ON' held on 03/04-04-2004. It also contains documentation which describes the GIADA experiment. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
-            "title": "ROSETTA-ORBITER CHECK GIADA 2 CVP1 COMMISSIONING1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK GIADA 2 CVP1 COMMISSIONING1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-MAG-4-RDR-HGCOORDS-9.6SEC-V1.0",
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
+            "description": "This data set includes data from the Low Field Magnetometer (LFM) during the inbound Neptune encounter beginning in the solar wind and continuing until the first magnetopause crossing. The magnetometer are given in Heliographic coordinates and the data have been averaged from the 1.92 second averages to a 9.6 second resampled rate.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-mag-4-rdr-hgcoords-9.6sec-v1.0_mykf-mh8r",
+            "issued": "2021-05-21",
+            "keyword": [
+                "neptune",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-MAG-4-RDR-HGCOORDS-9.6SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-mag-4-rdr-hgcoords-9.6sec-v1.0_mykf-mh8r",
-            "description": "This data set includes data from the Low Field Magnetometer (LFM) during the inbound Neptune encounter beginning in the solar wind and continuing until the first magnetopause crossing. The magnetometer are given in Heliographic coordinates and the data have been averaged from the 1.92 second averages to a 9.6 second resampled rate.",
-            "title": "VG2 NEP MAG RESAMP RDR HELIOGRAPHIC COORDINATES 9.6SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 NEP MAG RESAMP RDR HELIOGRAPHIC COORDINATES 9.6SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR1-NBFLT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SPURS PROJECT, Fred Bingham. 2015-05-11. Neutrally buoyant float data for the SPURS-1 N. Atlantic field campaign. Version 1.0. SPURS-1 Field Campaign Neutrally Buoyant Float Data Products. Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR1-NBFLT. http://podaac.jpl.nasa.gov/SPURS. SPURS PROJECT, Fred Bingham, SPURS Data Management PI, Fred Bingham, 2015-05-11, Neutrally buoyant float data for the SPURS-1 N. Atlantic field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2015-04-07",
-            "temporal": "2012-09-18T00:00:00Z/2013-02-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "ocean temperature",
-                "salinity/density",
-                "oceans",
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
-            "identifier": "C2491772227-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is an oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes.  SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales.  The SPURS-1 campaign involved a series of 5 cruises during 2012 - 2013 seeking to characterize the salinity structure and balance in a high salinity, high evaporation, and low rainfall region of the subtropical North Atlantic. It aims to resolve processes responsible for maintaining the subtropical surface salinity maximum in this region and within a 900 x 800-mile square study area centered at 25N, 38W.  Neutrally buoyant floats drift and move through the water column providing continuous temperature and salinity profiles via 2 integrated CTDs and GPS surface position location data. Two floats were deployed during SPURS-1, one during the Knorr cruise in September 2012 another deployed during the April 2013 Endeavor cruise.  Recoveries were in April and September 2013 respectively.  Neutrally buoyant float trajectory profile data include georeferenced time series of salinity, temperature, and pressure/depth observations.",
-            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
-            "series-name": "Neutrally buoyant float data for the SPURS-1 N. Atlantic field campaign",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SPURS PROJECT, Fred Bingham",
-            "title": "Neutrally buoyant float data for the SPURS-1 N. Atlantic field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_FLOAT_NEUTRALLYBUOYANT.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is an oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes.  SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales.  The SPURS-1 campaign involved a series of 5 cruises during 2012 - 2013 seeking to characterize the salinity structure and balance in a high salinity, high evaporation, and low rainfall region of the subtropical North Atlantic. It aims to resolve processes responsible for maintaining the subtropical surface salinity maximum in this region and within a 900 x 800-mile square study area centered at 25N, 38W.  Neutrally buoyant floats drift and move through the water column providing continuous temperature and salinity profiles via 2 integrated CTDs and GPS surface position location data. Two floats were deployed during SPURS-1, one during the Knorr cruise in September 2012 another deployed during the April 2013 Endeavor cruise.  Recoveries were in April and September 2013 respectively.  Neutrally buoyant float trajectory profile data include georeferenced time series of salinity, temperature, and pressure/depth observations.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR1-NBFLT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR1-NBFLT",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_FLOAT_NEUTRALLYBUOYANT.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_FLOAT_NEUTRALLYBUOYANT.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772227-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772227-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772227-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772227-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS1_FLOAT_NEUTRALLYBUOYANT.jpg",
+            "identifier": "C2491772227-POCLOUD",
+            "issued": "2015-04-07",
+            "keyword": [
+                "ocean temperature",
+                "salinity/density",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR1-NBFLT",
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
+            "series-name": "Neutrally buoyant float data for the SPURS-1 N. Atlantic field campaign",
             "spatial": "-39.0 21.0 -34.0 26.0",
+            "temporal": "2012-09-18T00:00:00Z/2013-02-22T00:00:00Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Neutrally buoyant float data for the SPURS-1 N. Atlantic field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3818-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-12T11:08:42.000 to 2015-09-12T11:32:34.949.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3818-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3818-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3818-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-12T11:08:42.000 to 2015-09-12T11:32:34.949.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3818 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3818 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-PRL-67P-M09-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-prl-67p-m09-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-PRL-67P-M09-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-prl-67p-m09-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 PRL-MTP009 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 PRL-MTP009 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1415",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chapin, E., S. Flores, L. Harcke, B.P. Hawkins, S. Hensley, T.R. Michel, R.J. Muellerschoen, J.G. Shimada, W.W. Tung, and C. Veeramachaneni. 2018. AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, Walnut Gulch, 2012-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1415",
-            "issued": "2018-05-01",
-            "temporal": "2012-09-20T00:00:00Z/2015-09-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "spectral/engineering",
-                "radar",
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
-            "identifier": "C2275408187-ORNL_CLOUD",
             "description": "This data set provides level 1 (L1) polarimetric radar backscattering coefficient (sigma-0), multilook complex, polarimetrically calibrated, and georeferenced data products from the Airborne Microwave Observatory of Subcanopy and Subsurface (AirMOSS) radar instrument collected over the Walnut Gulch site in Arizona. The AirMOSS radar is a P-band (UHF) fully polarimetric synthetic aperture radar (SAR) currently operating in the 420-440 MHz band designed to measure root-zone soil moisture (RZSM) and is flown on a NASA Gulfstream-III aircraft. Flight campaigns took place at least biannually from 2012 to 2015 at 10 study sites across North America. The acquired L1 P-band radar backscatter data will be used to retrieve the RZSM at the study sites. Subsequent analyses will investigate both seasonal and inter-annual variability in soil moisture and the relationships to carbon fluxes and their associated uncertainties on a continental scale.",
-            "graphic-preview-description": "Browse Image",
-            "title": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, Walnut Gulch, 2012-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1415_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1415",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1415",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L1_Sigma0_Walnut/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/airmoss/campaign/AirMOSS_L1_Sigma0_Walnut/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L1_Sigma0_Walnut.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AIRMOSS/guides/AirMOSS_L1_Sigma0_Walnut.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1415",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1415",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_L1_Sigma0_Walnut/comp/AirMOSS_L1_Sigma0_Walnut.pdf",
-                    "description": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, Walnut Gulch, 2012-2015: AirMOSS_L1_Sigma0_Walnut.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, Walnut Gulch, 2012-2015: AirMOSS_L1_Sigma0_Walnut.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/airmoss/campaign/AirMOSS_L1_Sigma0_Walnut/comp/AirMOSS_L1_Sigma0_Walnut.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1415_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1415_1_fit.png",
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
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1415/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1415/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1415_1_fit.png",
+            "identifier": "C2275408187-ORNL_CLOUD",
+            "issued": "2018-05-01",
+            "keyword": [
+                "spectral/engineering",
+                "radar",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1415",
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
             "spatial": "-111.24 31.58 -109.48 32.08",
+            "temporal": "2012-09-20T00:00:00Z/2015-09-01T23:59:59Z",
             "theme": [
                 "AirMOSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AirMOSS: L1 S-0 Polarimetric Data from AirMOSS P-band SAR, Walnut Gulch, 2012-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA1003",
             "citation": "Jarnot, R. and Perun, V.. 2015-02-19. ML1RADG. Version 004. MLS/Aura L1 Radiances from Filter Banks for GHz V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA1003. https://disc.gsfc.nasa.gov/datacollection/ML1RADG_004.html. Digital Science Data.",
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
-            "identifier": "C1265737480-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "ML1RADG is the EOS Aura Microwave Limb Sounder (MLS) product containing the level 1 radiances from the filter banks for the GHz radiometers. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), and files contain a full days worth of data (15 orbits). Users of the ML1RADG data product should read the 'A Short Guide to the Use and Interpretation of v4.2x Level 1 Data' document for additional information.\n\nThe data are stored in the version 5 Hierarchical Data Format, or HDF-5. Each file contains radiances and ancillary information written as HDF-5 dataset objects (n-dimensional arrays), along with file attributes and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML1RADG",
-            "creator": "Jarnot, R. and Perun, V.",
-            "title": "MLS/Aura L1 Radiances from Filter Banks for GHz V004 (ML1RADG) at GES DISC",
-            "graphic-preview-description": "Aura MLS logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADG_004.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA1003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA1003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADG_004.jpeg",
-                    "description": "Aura MLS logo",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADG_004.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML1RADG_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML1RADG_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level1/ML1RADG.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level1/ML1RADG.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML1RADG_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML1RADG_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1RADG_004.jpeg",
+            "identifier": "C1265737480-GES_DISC",
+            "issued": "2014-10-21",
+            "keyword": [
+                "spectral/engineering",
+                "microwave",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA1003",
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
+            "series-name": "ML1RADG",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura L1 Radiances from Filter Banks for GHz V004 (ML1RADG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ION-MOM-96.0SEC",
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
+            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 1 ENCOUNTER. RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IS SOME REGIONS. DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY. THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY. THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983). DATA FORMAT: COLUMNS 1-5 ARE TIME (YEAR, DAY, HOUR, MIN, SEC) AND COLUMN 6 IS THE MOMENT DENSITY IN CM-3. EACH ROW HAS FORMAT (I5,I4,2I3,I4,F8.3). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN LAZARUS AND MCNUTT (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ion-mom-96.0sec_myyf-9kxc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-ION-MOM-96.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-ion-mom-96.0sec_myyf-9kxc",
-            "description": "THIS DATA SET CONTAINS ESTIMATES OF THE ION MOMENT DENSITY IN THE PLS VOLTAGE RANGE (10-5950 EV/Q) AT SATURN DURING THE VOYAGER 1 ENCOUNTER. RIGID COROTATION IS ASSUMED, WHICH LEADS TO AN UNDERESTIMATE OF THE DENSITY IN SOME REGIONS, AS DOES THE USE OF AN ACCEPTANCE AREA RELEVANT FOR A COLD BEAM FOR PLASMA WHICH IS TRANSONIC IS SOME REGIONS. DENSITIES MAY BE UNDERESTIMATED BY A FACTOR OF 2-3 IN THE INNER MAGNETOSPHERE, SO THIS DATA SET SHOULD BE USED PRIMARILY FOR STUDIES USING VARIATIONS IN PLASMA DENSITY. THE FIT DENSITIES GIVE A BETTER ESTIMATE OF THE ABSOLUTE DENSITY. THIS IS THE DATA SHOWN AND DESCRIBED IN DETAIL IN LAZARUS AND MCNUTT (1983). DATA FORMAT: COLUMNS 1-5 ARE TIME (YEAR, DAY, HOUR, MIN, SEC) AND COLUMN 6 IS THE MOMENT DENSITY IN CM-3. EACH ROW HAS FORMAT (I5,I4,2I3,I4,F8.3). VALUES OF 1.E32 INDICATE THAT THE PARAMETER COULD NOT BE OBTAINED FROM THE DATA USING THE STANDARD ANALYSIS TECHNIQUE. ADDITIONAL INFORMATION ABOUT THIS DATASET AND THE INSTRUMENT WHICH PRODUCED IT CAN BE FOUND ELSEWHERE IN THIS CATALOG. AN OVERVIEW OF THE DATA IN THIS DATA SET CAN BE FOUND IN LAZARUS AND MCNUTT (1983) AND A COMPLETE INSTRUMENT DESCRIPTION CAN BE FOUND IN BRIDGE (1977).",
-            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION MOMENTS 96 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN PLASMA DERIVED ION MOMENTS 96 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "OMPS_NPP_NMSO2_PCA_L3_DAILY",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/OMPS/OMPS_NPP_NMSO2_PCA_L3_DAILY.1",
             "citation": "Can Li, Nickolay A. Krotkov, Peter Leonard, et al.. 2023-03-14. OMPS_NPP_NMSO2_PCA_L3_DAILY. Version 1. OMPS/NPP L3 NM PCA Sulfur Dioxide (SO2) Total Column Daily Best Pixel Global Gridded 0.25 degree x 0.25 degree V1. Greenbelt, MD, USA. OMPS_NPP_NMSO2_PCA_L3_DAILY. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/OMPS/OMPS_NPP_NMSO2_PCA_L3_DAILY.1. https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_PCA_L3_DAILY_1.html. Digital Science Data.",
-            "issued": "2022-12-27",
-            "temporal": "2012-01-26T00:00:00Z/2023-03-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-27",
-            "references": [
-                "https://doi.org/10.5194/amt-10-1495-2017",
-                "https://doi.org/10.5194/amt-10-445-2017",
-                "https://doi.org/10.1002/2013GL058134",
-                "https://doi.org/10.5194/amt-2020-186"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Can Li, PH. D",
                 "hasEmail": "mailto:can.li@nasa.gov"
             },
+            "creator": "Can Li, Nickolay A. Krotkov, Peter Leonard, et al.",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2567923363-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMPS-NPP L3 NM PCA Sulfur Dioxide (SO2) Total Column Daily Best Pixel Global Gridded 0.25 x 0.25 degree product contains sulfur dioxide amounts gridded at 0.25 x 0.25 degree resolution using the 'best' pixel method. Data are measured by the Ozone Mapping and Profiling Suite (OMPS) Nadir-Mapper (NM) sensor on the Suomi-NPP satellite. The product is based on the NASA Goddard Space Flight Center principal component analysis (PCA) spectral fitting algorithm (Li et al., 2013, 2017).\n\nEach granule contains data from the daylight portion of each orbit measured for a full day. Spatial coverage is global (-90 to  90 degrees latitude), and the spatial resolution is 0.25 x 0.25 degrees.\n\nThe files are written using netCDF version 4.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMPS_NPP_NMSO2_PCA_L3_DAILY",
-            "creator": "Can Li, Nickolay A. Krotkov, Peter Leonard, et al.",
-            "graphic-preview-description": "Annual mean SO2 vertical column densities (VCDs) in Dobson Units (DU, 1 DU = 2.69 \u00d71016 molecules/cm2) for 2018 from the OMPS_NPP_NMSO2_PCA_L3_DAILY V2.0 product. Pixels with large cloud fractions (> 0.3) or solar zenith angles (> 65\u00ba) or near the edge of the swath (rows 1-2 and 35-36 out of 36 OMPS rows) or low sensitivities to SO2 (air mass factor, AMF < 0.3) have been excluded. In addition, days with large volcanic plumes from explosive eruptions have also been excluded. Areas having major anthropogenic SO2 sources (e.g., India, eastern China, the Middle East, and South Africa) or degassing volcanoes (e.g., Kilauea and Etna) can be identified from the map.",
-            "title": "OMPS/NPP L3 NM PCA Sulfur Dioxide (SO2) Total Column Daily Best Pixel Global Gridded 0.25 degree x 0.25 degree V1 (OMPS_NPP_NMSO2_PCA_L3_DAILY) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/OMPS_NPP_NMSO2_PCA_L3_DAILY_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOMPS%2FOMPS_NPP_NMSO2_PCA_L3_DAILY.1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOMPS%2FOMPS_NPP_NMSO2_PCA_L3_DAILY.1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1112573,69 +1112543,101 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_PCA_L3_DAILY_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMPS_NPP_NMSO2_PCA_L3_DAILY_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level3/OMPS_NPP_NMSO2_PCA_L3_DAILY.1",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level3/OMPS_NPP_NMSO2_PCA_L3_DAILY.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level3/OMPS_NPP_NMSO2_PCA_L3_DAILY.1",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/opendap/SNPP_OMPS_Level3/OMPS_NPP_NMSO2_PCA_L3_DAILY.1",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMSO2_PCA_L3_DAILY",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMPS_NPP_NMSO2_PCA_L3_DAILY",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level3/OMPS_NPP_NMSO2_PCA_L3_DAILY.1/doc/README.OMPS_NPP_NMSO2_PCA_L3_DAILY.1.pdf",
-                    "description": "README document",
                     "@type": "dcat:Distribution",
+                    "description": "README document",
+                    "downloadURL": "https://omps.gesdisc.eosdis.nasa.gov/data/SNPP_OMPS_Level3/OMPS_NPP_NMSO2_PCA_L3_DAILY.1/doc/README.OMPS_NPP_NMSO2_PCA_L3_DAILY.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nesdis.noaa.gov/current-satellite-missions/currently-flying/joint-polar-satellite-system",
-                    "description": "Joint Polar Satellite System (JPSS) home page",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) home page",
+                    "downloadURL": "https://www.nesdis.noaa.gov/current-satellite-missions/currently-flying/joint-polar-satellite-system",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Annual mean SO2 vertical column densities (VCDs) in Dobson Units (DU, 1 DU = 2.69 \u00d71016 molecules/cm2) for 2018 from the OMPS_NPP_NMSO2_PCA_L3_DAILY V2.0 product. Pixels with large cloud fractions (> 0.3) or solar zenith angles (> 65\u00ba) or near the edge of the swath (rows 1-2 and 35-36 out of 36 OMPS rows) or low sensitivities to SO2 (air mass factor, AMF < 0.3) have been excluded. In addition, days with large volcanic plumes from explosive eruptions have also been excluded. Areas having major anthropogenic SO2 sources (e.g., India, eastern China, the Middle East, and South Africa) or degassing volcanoes (e.g., Kilauea and Etna) can be identified from the map.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/Krotkov/OMPS_NPP_NMSO2_PCA_L3_DAILY_1.png",
+            "identifier": "C2567923363-GES_DISC",
+            "issue-identification": "OMPS_NPP_NMSO2_PCA_L3_DAILY",
+            "issued": "2022-12-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/OMPS/OMPS_NPP_NMSO2_PCA_L3_DAILY.1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-10-1495-2017",
+                "https://doi.org/10.5194/amt-10-445-2017",
+                "https://doi.org/10.1002/2013GL058134",
+                "https://doi.org/10.5194/amt-2020-186"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMPS_NPP_NMSO2_PCA_L3_DAILY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-26T00:00:00Z/2023-03-20T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMPS/NPP L3 NM PCA Sulfur Dioxide (SO2) Total Column Daily Best Pixel Global Gridded 0.25 degree x 0.25 degree V1 (OMPS_NPP_NMSO2_PCA_L3_DAILY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PWS-2-REDR-RTS-SA-FULL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes full resolution electric and magnetic wave spectra obtained during the period for which real time science data was acquired from the Galileo plasma wave receiver during Jupiter orbital operations. The parameters provided for both the electric and magnetic field spectral data are uncalibrated data numbers. Software and calibration tables provided as part of this data set allow for fully calibrated data for the electric field measurements in raw data numbers, voltage at the antenna inputs (V), electric field (V/m), electric field spectral density (V**2/m**2/Hz), or power flux (W/m**2/Hz).  The magnetic field measurements can be provided in units of magnetic field spectral density (nT**2/Hz). The sources of these data are the High Frequency Receiver, Sweep Frequency Receiver, and Spectrum Analyzer which make up the Low Rate Science portion of the PWS.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pws-2-redr-rts-sa-full-v1.0_mz8t-sxw7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "ganymede",
                 "amalthea",
@@ -1112646,110 +1112648,81 @@
                 "europa",
                 "io"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PWS-2-REDR-RTS-SA-FULL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pws-2-redr-rts-sa-full-v1.0_mz8t-sxw7",
-            "description": "This data set includes full resolution electric and magnetic wave spectra obtained during the period for which real time science data was acquired from the Galileo plasma wave receiver during Jupiter orbital operations. The parameters provided for both the electric and magnetic field spectral data are uncalibrated data numbers. Software and calibration tables provided as part of this data set allow for fully calibrated data for the electric field measurements in raw data numbers, voltage at the antenna inputs (V), electric field (V/m), electric field spectral density (V**2/m**2/Hz), or power flux (W/m**2/Hz).  The magnetic field measurements can be provided in units of magnetic field spectral density (nT**2/Hz). The sources of these data are the High Frequency Receiver, Sweep Frequency Receiver, and Spectrum Analyzer which make up the Low Rate Science portion of the PWS.",
-            "title": "GO JUP PWS REFORMATTED REALTIME SPECTRUM ANALYZER FULL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUP PWS REFORMATTED REALTIME SPECTRUM ANALYZER FULL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENGR5-V1.0",
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
+            "description": "The Cassini Radio Science Enceladus Gravity Science Experiment (ENGR5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 1, 2, 20 and 21, 2009, during he Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-engr5-v1.0_mzav-4fp2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENGR5-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-engr5-v1.0_mzav-4fp2",
-            "description": "The Cassini Radio Science Enceladus Gravity Science Experiment (ENGR5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on November 1, 2, 20 and 21, 2009, during he Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - ENGR5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - ENGR5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA1005",
             "citation": "Marcel Dobber. 2007-09-20. OML1BRVZ. Version 003. OMI/Aura Level 1B VIS Zoom-in Geolocated Earthshine Radiances 1-orbit L2 Swath 13x12 km V003. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA1005. https://disc.gsfc.nasa.gov/datacollection/OML1BRVZ_003.html. Digital Science Data.",
-            "issued": "2004-08-09",
-            "temporal": "2004-10-06T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-09-20",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "visible wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JEROME ALFRED",
                 "hasEmail": "mailto:jerome.m.alfred@nasa.gov"
             },
+            "creator": "Marcel Dobber",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239966767-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Aura Ozone Monitoring Instrument (OMI) Level-1B (L1B) Geo-located Earth View VIS Radiance, Zoom-in-Mode (OML1BRVZ) Version-3 product contains geo-located Earth view spectral radiances from the VIS detectors in the wavelength range of 349 to 504 nm using spectral and spatial zoom-in measurement modes. In zoom-in measurement mode, OMI observes 60 ground pixels (13 km x 24 km at nadir) across the swath. Each file contains data from the day lit portion of an orbit (~60 minutes) and is roughly 190 MB in size. There are approximately 14 orbits per day. OMI performs spatial zoom-in measurements one day per month. For that day, this product also contains VIS measurements that are rebinned from the spatial zoom-in measurements. The lead algorithm scientist for this product is Dr. Marcel Dobber from the Royal Netherlands Meteorological Institude (KNMI).\n\nThe OML1BRVZ files are stored in the HDF4 based EOS Hierarchical Data Format (HDF-EOS). The radiances for the earth measurements (also referred as signal) and its precision are stored as a 16 bit mantissa and an 8-bit exponent. The signal can be computed using the equation: signal = mantissa x 10^exponent. For the precision, the same exponent is used as for the signal.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OML1BRVZ",
-            "creator": "Marcel Dobber",
-            "title": "OMI/Aura Level 1B VIS Zoom-in Geolocated Earthshine Radiances 1-orbit L2 Swath 13x12 km V003 (OML1BRVZ) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BRVZ_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA1005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA1005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1112759,73 +1112732,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BRVZ_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BRVZ_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRVZ.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRVZ.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BRVZ_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BRVZ_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRVZ.003/doc/README.OML1B.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRVZ.003/doc/README.OML1B.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-01.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/RD01_SD467_IODS_Vol_2_issue8.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/RD01_SD467_IODS_Vol_2_issue8.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/known_instrumental_effects_l1b_data_omi_v6.pdf",
-                    "description": "Known instrumental issues",
                     "@type": "dcat:Distribution",
+                    "description": "Known instrumental issues",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/known_instrumental_effects_l1b_data_omi_v6.pdf",
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
@@ -1112835,27 +1112808,56 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BRVZ_003.png",
+            "identifier": "C1239966767-GES_DISC",
+            "issued": "2004-08-09",
+            "keyword": [
+                "visible wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA1005",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-09-20",
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
+            "series-name": "OML1BRVZ",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-06T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Level 1B VIS Zoom-in Geolocated Earthshine Radiances 1-orbit L2 Swath 13x12 km V003 (OML1BRVZ) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-4-MARS-MARS-STR-REFL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-4-mars-mars-str-refl-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "21 lutetia",
                 "international rosetta mission",
@@ -1112864,202 +1112866,178 @@
                 "jupiter",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-4-MARS-MARS-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-4-mars-mars-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units  (normalized and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the MARS SWING-BY mission phase, covering the period  from 2006-07-29T00:00:00.000 to 2007-05-28T23:59:59.000. The prime target is planet Mars. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER MARS OSIWAC 4 MARS RDR-STR-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER MARS OSIWAC 4 MARS RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/ODU_CBM/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/ODU_CBM/DATA001.",
-            "issued": "2004-05-05",
-            "temporal": "2004-05-05T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "salinity/density",
-                "oceans",
-                "ocean chemistry",
-                "ocean temperature",
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
-            "identifier": "C1633360566-OB_DAAC",
             "description": "Measurements made of the Chesapeake Bay Mouth (CBM) by Old Dominion University (ODU) between 2004 and 2006.",
-            "title": "Old Dominion University (ODU) - Chesapeake Bay Mouth (CBM) measurements",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FODU_CBM%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FODU_CBM%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ODU_CBM/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ODU_CBM/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360566-OB_DAAC",
+            "issued": "2004-05-05",
+            "keyword": [
+                "ocean optics",
+                "salinity/density",
+                "oceans",
+                "ocean chemistry",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/ODU_CBM/DATA001",
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
+            "temporal": "2004-05-05T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Old Dominion University (ODU) - Chesapeake Bay Mouth (CBM) measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-3-PRL-CALIBRATED-V6.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nPRELANDING Phase (PRL) from March 23 until November 21, 2014 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).  The current\nversion of the dataset is V6.0 and the first being archived.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-3-prl-calibrated-v6.0_mzd5-s9sk",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "checkout"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-3-PRL-CALIBRATED-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-3-prl-calibrated-v6.0_mzd5-s9sk",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nPRELANDING Phase (PRL) from March 23 until November 21, 2014 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in the\nvicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).  The current\nversion of the dataset is V6.0 and the first being archived.",
-            "title": "ROSETTA-ORBITER SW RPCMAG 3 PRL CALIBRATED V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SW RPCMAG 3 PRL CALIBRATED V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCE1-V1.0",
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
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-sce1-v1.0_mzd6-56tr",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar system",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SS-RSS-1-SCE1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ss-rss-1-sce1-v1.0_mzd6-56tr",
-            "description": "not applicable",
-            "title": "CASSINI RSS RAW DATA SET - SCE1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SCE1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3519",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Read, W., Livesey, N., and Fuller, R.. 2021-04-29. ML3DBSO2. Version 005. MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3519. https://disc.gsfc.nasa.gov/datacollection/ML3DBSO2_005.html. Digital Science Data.",
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
-            "identifier": "C2042566261-GES_DISC",
-            "description": "ML3DBSO2 is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for sulfur dioxide (SO2) derived from radiances measured by the 240 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 215 to 10 hPa, and the vertical resolution is about 3 km. Users of the ML3DBSO2 data product should read chapter 4 and section 3.21 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DBSO2",
             "creator": "Read, W., Livesey, N., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V005 (ML3DBSO2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBSO2_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DBSO2 is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for sulfur dioxide (SO2) derived from radiances measured by the 240 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 215 to 10 hPa, and the vertical resolution is about 3 km. Users of the ML3DBSO2 data product should read chapter 4 and section 3.21 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3519",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3519",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1113069,111 +1113047,112 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBSO2_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBSO2_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBSO2.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBSO2.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBSO2.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBSO2.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBSO2_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBSO2_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBSO2_005.png",
+            "identifier": "C2042566261-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3519",
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
+            "series-name": "ML3DBSO2",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V005 (ML3DBSO2) at GES DISC"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/archives/past-issues/",
-            "bureauCode": [
-                "026:00"
-            ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://km.nasa.gov/knowledge-map/"
-            ],
-            "keyword": [
-                "ask magazine",
-                "appel",
-                "knowledge",
-                "sharing"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "026:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ed Hoffman",
                 "hasEmail": "mailto:ehoffman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-860__32",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1113181,23 +1113160,46 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__32",
+            "issued": "2018-06-25",
+            "keyword": [
+                "ask magazine",
+                "appel",
+                "knowledge",
+                "sharing"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.irtf-spex-collection.spectra&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains low-resolution,   near-infrared (0.8 - 2.5 micron) spectra of asteroids obtained with    SpeX at the NASA Infrared Telescope Facility (IRTF) on Mauna Kea.      Since it was commissioned in June 2000, SpeX has been the premier      instrument for producing high quality near-IR spectra of asteroids.    These spectra have been used for both taxonomic studies of asteroids,  and for more detailed mineralogical and compositional investigations.  This data set archives the reduced, calibrated spectra that have been  published in the peer-reviewed literature, and will be regularly       updated as more data become publicly available.",
+            "identifier": "urn:nasa:pds:gbo.ast.irtf-spex-collection.spectra",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "(1275) cimbria",
                 "(1251) hedera",
@@ -1113375,61 +1113377,37 @@
                 "(77) frigga",
                 "(44) nysa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.irtf-spex-collection.spectra&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.irtf-spex-collection.spectra",
-            "description": "This data set contains low-resolution,   near-infrared (0.8 - 2.5 micron) spectra of asteroids obtained with    SpeX at the NASA Infrared Telescope Facility (IRTF) on Mauna Kea.      Since it was commissioned in June 2000, SpeX has been the premier      instrument for producing high quality near-IR spectra of asteroids.    These spectra have been used for both taxonomic studies of asteroids,  and for more detailed mineralogical and compositional investigations.  This data set archives the reduced, calibrated spectra that have been  published in the peer-reviewed literature, and will be regularly       updated as more data become publicly available.",
-            "title": "IRTF NEAR-IR SPECTROSCOPY OF ASTEROIDS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IRTF NEAR-IR SPECTROSCOPY OF ASTEROIDS"
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
-                "incompressible",
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
-            "identifier": "NASA-842",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1113437,270 +1113415,304 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-842",
+            "issued": "2018-06-25",
+            "keyword": [
+                "turbulence",
+                "flow",
+                "cases",
+                "incompressible",
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
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567916-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
-            "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
-            "keyword": [
-                "topography",
-                "earth science",
-                "surface radiative properties",
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
-            "identifier": "C1220567916-USGS_LTA",
             "description": "National Land Cover Dataset 1992 (NLCD1992) is a 21-class land cover classification scheme that has been applied consistently across the lower 48 United States at a spatial resolution of 30 meters. NLCD92 is based primarily on the unsupervised classification of Landsat Thematic Mapper (TM) circa 1990's satellite data. Other ancillary data sources used to generate these data included topography, census, and agricultural statistics, soil characteristics, and other types of land cover and wetland maps. NLCD1992 is the only NLCD dataset that can be downloaded by state and by user defined area from the MRLC Consortium Viewer.",
-            "title": "National Land Cover Data set 1992 (NLCD1992)",
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
+            "identifier": "C1220567916-USGS_LTA",
+            "issued": "2019-09-20",
+            "keyword": [
+                "topography",
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567916-USGS_LTA.html",
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
+            "title": "National Land Cover Data set 1992 (NLCD1992)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-SIRS-4-RDR-SPECTRUM-V1.0",
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
-                "geologic remote sensing field experiment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The SIRIS measurement objectives were: 1) to measure reflectance spectra of a bright and dark target at each GRSFE site for potential use in AVIRIS calibration characterize selected sites at the GRSFE modeling site (Lunar Lake, NV) using visible/infrared reflectance reflectance spectra for selected endmember materials at each of the GRSFE sites inter-instrument calibration.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-sirs-4-rdr-spectrum-v1.0_mzkg-7xt3",
+            "issued": "2021-05-21",
+            "keyword": [
+                "earth",
+                "geologic remote sensing field experiment"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=FEXP-E-SIRS-4-RDR-SPECTRUM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.fexp-e-sirs-4-rdr-spectrum-v1.0_mzkg-7xt3",
-            "description": "The SIRIS measurement objectives were: 1) to measure reflectance spectra of a bright and dark target at each GRSFE site for potential use in AVIRIS calibration characterize selected sites at the GRSFE modeling site (Lunar Lake, NV) using visible/infrared reflectance reflectance spectra for selected endmember materials at each of the GRSFE sites inter-instrument calibration.",
-            "title": "FIELD EXP E SIRIS RESAMP REDUCED DATA RECORD SPECTRUM V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "FIELD EXP E SIRIS RESAMP REDUCED DATA RECORD SPECTRUM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSOH-3-EDR-CROMMELIN-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rsoh-3-edr-crommelin-v1.0_mzmv-awfu",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSOH-3-EDR-CROMMELIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rsoh-3-edr-crommelin-v1.0_mzmv-awfu",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET RSOH CALIB EXPERIMENT DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET RSOH CALIB EXPERIMENT DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GLOSSAC-L3-V2.21",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-02-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GLOSSAC-L3-V2.21.",
-            "issued": "2023-02-27",
-            "temporal": "1979-01-01T00:00:00Z/2022-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-27",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Larry Thomason",
                 "hasEmail": "mailto:l.w.thomason@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2705848058-LARC_ASDC",
             "description": "The Global Space-based Stratospheric Aerosol Climatology, or GloSSAC, is a 44-year climatology of stratospheric aerosol properties focused on extinction coefficient measurements by the Stratospheric Aerosol and Gas Experiment (SAGE) series of instruments through mid-2005 and later from mid-2017 and on the Optical Spectrograph and InfraRed Imager System (OSIRIS) and the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observation (CALIPSO) data thereafter. Data from other space instruments and from ground-based, air and balloon borne instruments to fill in key gaps in the data set. The end result is a global and gap-free data set focused on aerosol extinction coefficient at 525 and 1020 nm and other parameters on an \u2018as available\u2019 basis.",
-            "title": "Global Space-based Stratospheric Aerosol Climatology Version 2.21",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGLOSSAC-L3-V2.21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGLOSSAC-L3-V2.21",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.sparc-ssirc.org/",
-                    "description": "SSiRC Activity Summary",
                     "@type": "dcat:Distribution",
+                    "description": "SSiRC Activity Summary",
+                    "downloadURL": "http://www.sparc-ssirc.org/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/GloSSAC",
-                    "description": "ASDC Data and Information for GloSSAC",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for GloSSAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/GloSSAC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/glossac/guide/GloSSAC_Project_Guide_Document_v2.21.pdf",
-                    "description": "GloSSAC Project Guide Document",
                     "@type": "dcat:Distribution",
+                    "description": "GloSSAC Project Guide Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/glossac/guide/GloSSAC_Project_Guide_Document_v2.21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/glossac/quality_summaries/GloSSAC_Product_Quality_Summary_v2.21.pdf",
-                    "description": "GloSSAC Product Quality Summary",
                     "@type": "dcat:Distribution",
+                    "description": "GloSSAC Product Quality Summary",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/glossac/quality_summaries/GloSSAC_Product_Quality_Summary_v2.21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/glossac/readme/readme_glossac_v2.21.txt",
-                    "description": "GloSSAC Readme File",
                     "@type": "dcat:Distribution",
+                    "description": "GloSSAC Readme File",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/glossac/readme/readme_glossac_v2.21.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2705848058-LARC_ASDC",
-                    "description": "Earthdata Search for GloSSAC_2.21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GloSSAC_2.21 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2705848058-LARC_ASDC",
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
-                    "downloadURL": "https://doi.org/10.5067/GLOSSAC-L3-V2.21",
-                    "description": "DOI data set landing page for GloSSAC_2.21",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GloSSAC_2.21",
+                    "downloadURL": "https://doi.org/10.5067/GLOSSAC-L3-V2.21",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://creativecommons.org/licenses/by/4.0/",
-                    "description": "Creative Commons License CC BY 4.0",
                     "@type": "dcat:Distribution",
+                    "description": "Creative Commons License CC BY 4.0",
+                    "downloadURL": "https://creativecommons.org/licenses/by/4.0/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/GloSSAC/GloSSAC_2.21/",
-                    "description": "ASDC Direct Data Download for GloSSAC_2.21",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GloSSAC_2.21",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/GloSSAC/GloSSAC_2.21/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/GloSSAC/GloSSAC_2.21/contents.html",
-                    "description": "OPeNDAP data access for GloSSAC_2.21",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GloSSAC_2.21",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/GloSSAC/GloSSAC_2.21/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2705848058-LARC_ASDC",
+            "issued": "2023-02-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/GLOSSAC-L3-V2.21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-80.0 -180.0 -80.0 180.0 80.0 180.0 80.0 -180.0 -80.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1979-01-01T00:00:00Z/2022-12-31T23:59:59.999Z",
             "theme": [
                 "GloSSAC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Space-based Stratospheric Aerosol Climatology Version 2.21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567915-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, DOI/USGS/EROS.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ANNIEPAT JOHNSON",
+                "hasEmail": "mailto:lta@usgs.gov"
+            },
+            "description": "National Land Cover Database 2001 (NLCD2001) is a 16-class (additional four classes in Alaska only) land cover classification scheme that has been applied consistently across all 50 United States and Puerto Rico at a spatial resolution of 30 meters. NLCD2001 is based primarily on the unsupervised classification of Landsat Enhanced Thematic Mapper+ (ETM+) circa 2001 satellite data. NLCD2001 improves on NLCD92 in that it is comprised of three different elements: land cover, percent developed impervious surface and percent tree canopy density. NLCD2001 also uses improved classification algorithms, which have resulted in data with more precise rending of spatial boundaries between the land cover classes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1220567915-USGS_LTA",
             "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "earth science",
                 "landscape",
@@ -1113712,475 +1113724,443 @@
                 "erosion/sedimentation",
                 "geomorphic landforms/processes"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ANNIEPAT JOHNSON",
-                "hasEmail": "mailto:lta@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220567915-USGS_LTA.html",
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
-            "identifier": "C1220567915-USGS_LTA",
-            "description": "National Land Cover Database 2001 (NLCD2001) is a 16-class (additional four classes in Alaska only) land cover classification scheme that has been applied consistently across all 50 United States and Puerto Rico at a spatial resolution of 30 meters. NLCD2001 is based primarily on the unsupervised classification of Landsat Enhanced Thematic Mapper+ (ETM+) circa 2001 satellite data. NLCD2001 improves on NLCD92 in that it is comprised of three different elements: land cover, percent developed impervious surface and percent tree canopy density. NLCD2001 also uses improved classification algorithms, which have resulted in data with more precise rending of spatial boundaries between the land cover classes.",
-            "title": "NLCD 2001 Version 2",
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
+            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NLCD 2001 Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-APXS-2-EDR-OPS-V1.0",
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
+            "description": "This archive contains Mars Exploration Rover Operations (Ops) APXS Experiment Data Record (EDR) products and ancillary files.  Each EDR product has a detached PDS label that describes the file structure and instrument parameters used for that image. The APXS Operations EDR products archived on this volume are the original products used during mission operations by the Mars Exploration Rover project.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-apxs-2-edr-ops-v1.0_mzr3-7s89",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-APXS-2-EDR-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-apxs-2-edr-ops-v1.0_mzr3-7s89",
-            "description": "This archive contains Mars Exploration Rover Operations (Ops) APXS Experiment Data Record (EDR) products and ancillary files.  Each EDR product has a detached PDS label that describes the file structure and instrument parameters used for that image. The APXS Operations EDR products archived on this volume are the original products used during mission operations by the Mars Exploration Rover project.",
-            "title": "MER 2 MARS ALPHA PARTICLE X-RAY\n                                      SPECTROMETER 2 EDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 2 MARS ALPHA PARTICLE X-RAY\n                                      SPECTROMETER 2 EDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M20-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m20-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M20-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m20-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP020 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP020 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DAEF_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a day's products;See ProductionDateTime for Published date.",
-            "issued": "2007-07-30",
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
-            "identifier": "C156141681-LARC",
             "description": "This file contains the MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a day",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a day V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DAEF_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DAEF_L3.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C156141681-LARC",
+            "issued": "2007-07-30",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DAEF_L3.002",
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
+            "title": "MISR Level 3 FIRSTLOOK Component Global Aerosol Product covering a day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-RSS-1-ROCC-V1.0",
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
+            "description": "This data set consists of raw data collected during the Saturn egress radio occultation of Voyager 1 on 13 November 1980 plus ancillary files that might be useful in analysis of those data. The raw data are sampled voltage outputs from receivers tuned to the Voyager carrier frequencies at both S-band and X-band during the occultation.  The data have been reduced to give profiles of temperature and pressure as a function of height in the atmosphere, to infer magnetic field orientations in the upper ionosphere, and to determine the distribution of particles and particle properties in the ring system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-rss-1-rocc-v1.0_n24a-ar7x",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-RSS-1-ROCC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-rss-1-rocc-v1.0_n24a-ar7x",
-            "description": "This data set consists of raw data collected during the Saturn egress radio occultation of Voyager 1 on 13 November 1980 plus ancillary files that might be useful in analysis of those data. The raw data are sampled voltage outputs from receivers tuned to the Voyager carrier frequencies at both S-band and X-band during the occultation.  The data have been reduced to give profiles of temperature and pressure as a function of height in the atmosphere, to infer magnetic field orientations in the upper ionosphere, and to determine the distribution of particles and particle properties in the ring system.",
-            "title": "VOYAGER 1 SATURN EGRESS RADIO\n                                      OCCULTATION RAW DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 SATURN EGRESS RADIO\n                                      OCCULTATION RAW DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-HIW-V1.0",
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
-                "messenger",
-                "mercury"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes Map Projected High- Incidence Angle Basemap Illuminated from the West RDRs (HIWs) which comprise a global map of I/F measured by the NAC or WAC filter 7 (both centered near 750 nm) during the the Extended Mission at high incidence angles to accentuate subtle topography, photometrically normalized to a solar incidence angle (i) = 30 degrees, emission angle (e) = 0 degrees, and phase angle (g) = 30 degrees at a spatial sampling of 256 pixels per degree. The HIW data set is a companion to the Map Projected High-Incidence Angle Basemap Illuminated from the East RDR (HIE) data set. Together the two data sets are intended to detect and allow the mapping of subtle topography. They complement a Basemap Data Record (BDR) data set also composed of WAC filter 7 and NAC images acquired at moderate/high solar incidence angles centered near 68 degrees (changed to 74 degrees in the find end-of-mission data delivery), and an Low Incidence Angle (LOI) data set also composed of WAC filter 7 and NAC images acquired at lower incidence centered near 45 degrees, analogous to the geometry used for color imaging. The map is divided into 54 'tiles', each representing the NW, NE, SW, or SE quadrant of one of the 13 non-polar or one of the 2 polar quadrangles or 'Mercury charts' already defined by the USGS. Each tile also contains 5 backplanes: observation ID; BDR metric, a metric used to determine the stacking order of component images, modified for the higher incidence angle centered near 78 degrees; solar incidence angle; emission angle; and phase angle.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-mdis-5-rdr-hiw-v1.0_n25d-iuqi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "messenger",
+                "mercury"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-MDIS-5-RDR-HIW-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-mdis-5-rdr-hiw-v1.0_n25d-iuqi",
-            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes Map Projected High- Incidence Angle Basemap Illuminated from the West RDRs (HIWs) which comprise a global map of I/F measured by the NAC or WAC filter 7 (both centered near 750 nm) during the the Extended Mission at high incidence angles to accentuate subtle topography, photometrically normalized to a solar incidence angle (i) = 30 degrees, emission angle (e) = 0 degrees, and phase angle (g) = 30 degrees at a spatial sampling of 256 pixels per degree. The HIW data set is a companion to the Map Projected High-Incidence Angle Basemap Illuminated from the East RDR (HIE) data set. Together the two data sets are intended to detect and allow the mapping of subtle topography. They complement a Basemap Data Record (BDR) data set also composed of WAC filter 7 and NAC images acquired at moderate/high solar incidence angles centered near 68 degrees (changed to 74 degrees in the find end-of-mission data delivery), and an Low Incidence Angle (LOI) data set also composed of WAC filter 7 and NAC images acquired at lower incidence centered near 45 degrees, analogous to the geometry used for color imaging. The map is divided into 54 'tiles', each representing the NW, NE, SW, or SE quadrant of one of the 13 non-polar or one of the 2 polar quadrangles or 'Mercury charts' already defined by the USGS. Each tile also contains 5 backplanes: observation ID; BDR metric, a metric used to determine the stacking order of component images, modified for the higher incidence angle centered near 78 degrees; solar incidence angle; emission angle; and phase angle.",
-            "title": "MESS MDIS MAP PROJ HIGH-INCIDENCE\n                                      BASEMAP WEST RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESS MDIS MAP PROJ HIGH-INCIDENCE\n                                      BASEMAP WEST RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA3.001",
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2018-11-17. VNP43MA3. Version 001. VIIRS/NPP BRDF/Albedo Albedo Daily L3 Global 1km SIN Grid V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43MA3.001. https://doi.org/10.5067/VIIRS/VNP43MA3.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2018-11-17",
-            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-17",
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
+            "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1407099488-LPDAAC_ECS",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
             "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo (VNP43MA3) Version 1 product provides albedo values at 1 kilometer (km) resolution for the bihemispherical reflectance white-sky albedo (WSA) and directional hemispherical reflectance black-sky albedo (BSA) at local solar noon. The VNP43MA3 product is produced daily using 16 days of VIIRS data and is weighted temporally to the ninth day, which is reflected in the file name. The VNP43 data products are designed to promote the continuity of NASA\u2019s Moderate Resolution Imaging Spectroradiometer (MODIS) BRDF/Albedo data product suite. \r\n\r\nThe VNP43 algorithm uses the RossThick/Li-Sparse-Reciprocal (RTLSR) semi-empirical kernel-driven BRDF model, with the three kernel weights from (VNP43MA1) (https://doi.org/10.5067/VIIRS/VNP43MA1.001) to reconstruct surface anisotropic effects, correcting the directional reflectance to a common view geometry (VNP43MA4) (https://doi.org/10.5067/VIIRS/VNP43MA4.001), while also computing integrated black-sky albedo (BSA) at local solar noon and white-sky albedo (WSA) (VNP43MA3). Researchers can use the BRDF model parameters with a simple polynomial, to obtain black-sky albedo at any solar illumination angle. Likewise, both the BSA and WSA Science Dataset (SDS) layers can be used with a simple polynomial, to manually estimate instantaneous actual albedo (blue-sky albedo). Additional details regarding the methodology are available in the Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/194/VNP43_ATBD_V1.pdf).\r\n\r\nThe VNP43MA3 product provides a total of 36 SDS layers including: BSA, WSA, and mandatory quality layers for nine VIIRS moderate bands: M1-M5, M7-M8, and M10-M11, as well as three broadbands: near-infrared (NIR), shortwave, and visible. A low-resolution image is also available showing retrievals of WSA for band I1 in JPEG format.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43MA3",
-            "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Albedo Daily L3 Global 1km SIN Grid V001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP43MA3.A2019175.h19v04.001.2019183072445.1.jpg?_ga=2.83716054.116070394.1561987039-1109527761.1561753117",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43MA3.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43MA3.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43MA3.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43MA3.001",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43MA3.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43MA3.001/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1407099488-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1407099488-LPDAAC_ECS",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guide/vnp43ia3-and-vnp43ma3-albedo-products/",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/viirs-user-guide/vnp43ia3-and-vnp43ma3-albedo-products/",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43MA3",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43MA3",
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
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP43MA3.A2019175.h19v04.001.2019183072445.1.jpg?_ga=2.83716054.116070394.1561987039-1109527761.1561753117",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP43MA3.A2019175.h19v04.001.2019183072445.1.jpg?_ga=2.83716054.116070394.1561987039-1109527761.1561753117",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP101/VIIRS/VNP43MA3.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP101/VIIRS/VNP43MA3.001/contents.html",
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
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.02/BROWSE.VNP43MA3.A2019175.h19v04.001.2019183072445.1.jpg?_ga=2.83716054.116070394.1561987039-1109527761.1561753117",
+            "identifier": "C1407099488-LPDAAC_ECS",
+            "issued": "2018-11-17",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43MA3.001",
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
+            "series-name": "VNP43MA3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-17T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Albedo Daily L3 Global 1km SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CR4A-CHKOUT-REFLECT-V1.0",
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
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cr4a-chkout-reflect-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-4-CR4A-CHKOUT-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-4-cr4a-chkout-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled)  image data in reflectance units (normalized and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 4-1 mission phase, covering the period  from 2008-01-28T00:00:00.000 to 2008-08-03T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CR4A RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 4 CR4A RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_monthly_utc_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_monthly_utc_1.",
-            "issued": "2020-10-05",
-            "temporal": "1988-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-05",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "atmospheric radiation",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Colleen Mikovitz",
                 "hasEmail": "mailto:j.c.mikovitz@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2058669482-LARC_ASDC",
             "description": "GEWEXSRB_Rel4-IP_Longwave_monthly_utc is the Global Energy and Water Exchanges (GEWEX) Surface Radiation Budget (SRB) Integrated Product (Rel-4) Longwave Monthly Average by UTC data product. It contains global fields of 26 longwave surface, Top of Atmosphere (TOA), and atmospheric profile radiative parameters derived with the Longwave algorithm of the NASA World Climate Research Programme/Global Energy and Water-Cycle Experiment (WCRP/GEWEX) Surface Radiation Budget (SRB) Project. This version is known as Release 4-Integrated Product. The fluxes include all-sky, clear-sky and pristine-sky TOA upward fluxes (outgoing longwave radiation, OLR), all-sky, clear-sky and pristine-sky upward and downward fluxes at: tropopause, 200hPa, 500hPa and surface. A status flag of filled cloud properties is also included. Inputs to the longwave algorithm are cloud information based on ISCCP HXS, meteorology from ISCCP nnHIRS, SeaFlux SST and surface, LandFlux meteorology, and MERRA-2 conditionally. The temporal range is January 1988 through December 2009, with the ends bound by input constraints. Data collection for this product is complete.",
-            "title": "GEWEX SRB Integrated Product (Rel-4) Longwave Monthly Average by UTC",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Longwave_monthly_utc_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGEWEXSRB%2FRel4-IP_Longwave_monthly_utc_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gewex-srb.larc.nasa.gov/",
-                    "description": "NASA GEWEX Surface Radiation Budget project page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA GEWEX Surface Radiation Budget project page",
+                    "downloadURL": "https://gewex-srb.larc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_monthly_utc_1",
-                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_monthly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for GEWEXSRB_Rel4-IP_Longwave_monthly_utc_1",
+                    "downloadURL": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_monthly_utc_1",
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
@@ -1114196,142 +1114176,171 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2058669482-LARC_ASDC",
-                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Longwave_monthly_utc_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for GEWEXSRB_Rel4-IP_Longwave_monthly_utc_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2058669482-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Longwave_monthly_utc_1/",
-                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Longwave_monthly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for GEWEXSRB_Rel4-IP_Longwave_monthly_utc_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SRB/GEWEXSRB_Rel4-IP/Longwave_monthly_utc_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Longwave_monthly_utc_1/contents.html",
-                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Longwave_monthly_utc_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for GEWEXSRB_Rel4-IP_Longwave_monthly_utc_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/SRB/GEWEXSRB_Rel4-IP/Longwave_monthly_utc_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2058669482-LARC_ASDC",
+            "issued": "2020-10-05",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "atmospheric radiation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GEWEXSRB/Rel4-IP_Longwave_monthly_utc_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-10-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1988-01-01T00:00:00Z/2009-12-31T23:59:59.999Z",
             "theme": [
                 "SRB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEWEX SRB Integrated Product (Rel-4) Longwave Monthly Average by UTC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TCSP/GOES-IM/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Velden, Christopher , Dave  Stettner and Howard  Berger.2006. TCSP GOES 11 RAPID SCAN WINDS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/TCSP/GOES-IM/DATA201",
-            "issued": "2006-03-09",
-            "temporal": "2005-07-12T16:00:00Z/2005-07-31T23:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths"
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
-            "identifier": "C1979950521-GHRC_DAAC",
             "description": "The TCSP GOES 11 Rapid Scan Winds dataset was generated from image triplets with 30 or 60 minute intervals, and occasionally 15 minute intervals. During  Geostationary Operational Environmental Satellites (GOES) special rapid-scan operations, co-located images are available at intervals of 7.5, 5, 3, and even 1 minute. The area covered is reduced as the interval decreases. In this experiment, images at five minute intervals were used for the 0.65 micrometer visible, 3.9 micrometer infrared (darkness only), and 10.7 micrometer IR channels. GOES-11 was brought out of storage and image products were centered on the TCSP study region. The TCSP mission collected data for research and documentation of cyclogenesis, the interaction of temperature, humidity, precipitation, wind and air pressure that creates ideal birthing conditions for tropical storms, hurricanes and related phenomena. The goal of this mission was to help us better understand how hurricanes and other tropical storms are formed and intensify. Regular image processing was available beginning on 12 July. The scan schedule was maintained through the end of July.",
-            "graphic-preview-description": "N/A",
-            "title": "TCSP GOES 11 RAPID SCAN WINDS V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/grsw/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FGOES-IM%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FGOES-IM%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspgrsw",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspgrsw",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/grsw/browse/12Jul2005-17z-upperwindsg11.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/grsw/browse/12Jul2005-17z-upperwindsg11.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/tcsp/tcspgrsw/tcspgrsw_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/tcsp/tcspgrsw/tcspgrsw_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/grsw/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/grsw/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/grsw/browse/",
+            "identifier": "C1979950521-GHRC_DAAC",
+            "issued": "2006-03-09",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/TCSP/GOES-IM/DATA201",
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
             "spatial": "-110.0 5.03 -70.0 25.0",
+            "temporal": "2005-07-12T16:00:00Z/2005-07-31T23:00:00Z",
             "theme": [
                 "TCSP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TCSP GOES 11 RAPID SCAN WINDS V1"
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
+            "description": "Exp: Flow Behind a NACA 0012 Wingtip. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Wingtip/Wingtip_expdata.tar.gz",
+                    "mediaType": "application/x-gzip"
+                }
             ],
+            "identifier": "NASA-854",
+            "issued": "2018-06-25",
             "keyword": [
                 "naca",
                 "models",
@@ -1114341,190 +1114350,183 @@
                 "wingtip",
                 "turbulence"
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
-            "identifier": "NASA-854",
-            "description": "Exp: Flow Behind a NACA 0012 Wingtip. This web page provides data from experiments that may be useful for the validation of turbulence models. This resource is expected to grow gradually over time. All data herein arepublicly available.",
-            "title": "Turbulence Models: Data from Other Experiments: Flow Behind a NACA 0012 Wingtip",
-            "programCode": [
-                "026:023"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://turbmodels.larc.nasa.gov/Other_exp_Data/Wingtip/Wingtip_expdata.tar.gz",
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
+            "title": "Turbulence Models: Data from Other Experiments: Flow Behind a NACA 0012 Wingtip"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/721",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "McGill, M.J., D.L. Hlavka, and W.D. Hart. 2004. SAFARI 2000 Cloud Physics Lidar (CPL) Quicklook Images and Maps. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/721",
-            "issued": "2023-10-18",
-            "temporal": "2000-08-17T00:00:00Z/2000-09-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "clouds",
-                "aerosols",
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
-            "identifier": "C2788400595-ORNL_CLOUD",
             "description": "The effect of clouds and aerosols on regional and global climate is of great importance. Two longstanding elements of the NASA climate and radiation science program are field studies incorporating airborne remote-sensing and in-situ measurements of clouds and aerosols. is Data products include: (1) cloud profiling with 30-m vertical and 200-m horizontal resolution at 1064 nm, 532 nm, and 355 nm;(2) aerosol, boundary layer, and smoke plume profiling;(3) optical depth estimates (column and by layer); and(4) extinction profiles. The CPL provides information to permit a comprehensive analysis of radiative and optical properties of optically thin clouds. Data users are asked to read and abide by the CPL data usage policy found at [http://virl.gsfc.nasa.gov/cpl/cpl_register.htm].",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Cloud Physics Lidar (CPL) Quicklook Images and Maps",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F721",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F721",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/cp_lidar_images/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/cp_lidar_images/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/cp_lidar_images.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/cp_lidar_images.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/721",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/721",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/cp_lidar_images/comp/cp_lidar_images_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/cp_lidar_images/comp/cp_lidar_images_readme.pdf",
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
+            "identifier": "C2788400595-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "clouds",
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/721",
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
+            "temporal": "2000-08-17T00:00:00Z/2000-09-25T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Cloud Physics Lidar (CPL) Quicklook Images and Maps"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/EGEE3/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/EGEE3/DATA001.",
-            "issued": "2006-05-29",
-            "temporal": "2006-05-29T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "ocean chemistry",
-                "salinity/density",
-                "earth science",
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
-            "identifier": "C1633360226-OB_DAAC",
             "description": "Measurements made in the Gulf of Guinea off of west-central Africa in 2006 as part of the third cruise in the EGEE project (Gulf of Guinea climate and ocean circulation study, which is the oceanographic strand of the AMMA -African Monsoon Multidisciplinary Analyses program).",
-            "title": "Gulf of Guinea climate and ocean circulation study (EGEE) project - Gulf of Guinea off of west-central Africa",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FEGEE3%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FEGEE3%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/EGEE3/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/EGEE3/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360226-OB_DAAC",
+            "issued": "2006-05-29",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "salinity/density",
+                "earth science",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/EGEE3/DATA001",
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
+            "temporal": "2006-05-29T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gulf of Guinea climate and ocean circulation study (EGEE) project - Gulf of Guinea off of west-central Africa"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MDIS-2-EDR-RAWDATA-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes the Experiment Data Record (EDR) version of all available images acquired during the cruise phase to Mercury and includes post- launch checkout images, flyby images of Earth, Venus, Mercury, and the Moon, images acquired from Mercury orbit, and inflight calibration images. In addition to the imagery, anciliary information (including calibration files needed to process the data further) is included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mdis-2-edr-rawdata-v1.0_n2ky-gshn",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2p/encke 1 (1818 w1)",
                 "neptune",
@@ -1114557,789 +1114559,789 @@
                 "mirzam",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MDIS-2-EDR-RAWDATA-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mdis-2-edr-rawdata-v1.0_n2ky-gshn",
-            "description": "Abstract ======== The Mercury Dual Imaging System (MDIS) consists of two cameras, a Wide Angle Camera (WAC) and a Narrow Angle Camera (NAC), mounted on a common pivot platform. This dataset includes the Experiment Data Record (EDR) version of all available images acquired during the cruise phase to Mercury and includes post- launch checkout images, flyby images of Earth, Venus, Mercury, and the Moon, images acquired from Mercury orbit, and inflight calibration images. In addition to the imagery, anciliary information (including calibration files needed to process the data further) is included.",
-            "title": "MESSENGER MDIS EXPERIMENT DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER MDIS EXPERIMENT DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/819",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Huston, M.A., D.W. Johnson, D.E. Todd, J.W. Curlin, and F.W. Harris. 2013. Walker Branch Watershed Vegetation Inventory, 1967-2006, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/819",
-            "issued": "2023-08-20",
-            "temporal": "1967-01-01T00:00:00Z/2006-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-23",
-            "keyword": [
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
-            "identifier": "C2755668925-ORNL_CLOUD",
             "description": "This data set contains five data files, in comma-separated format (.csv), derived from the Walker Branch Watershed (WBW) vegetation inventory in eastern Tennessee. Field studies of permanent vegetation plots were conducted using one sampling design over a 40-year period (1967 to 2006). The data set contains long-term measurements of diameter at breast height (DBH) determined on stratified randomly-located inventory plots within the 4 different vegetation types (oak-hickory, pine-oak-hickory, pine, and mesophytic hardwoods) located in the WBW in 1967. The WBW plot-level vegetation DBH data are provided in four files. One file contains the complete set of inventory records (139,806 observations). To accommodate spreadsheet use, the complete inventory is split into three files, one containing 52,110 observations and the other two containing 48,231 and 39,465 observations, respectively. The fifth file contains the WBW vegetation species inventory with species names, the numeric species code for each species, a species group designation, the scientific name for each species, and the literature-derived ratio of g lignin/g N for leaves of each species. NPP values have been reported for various forest stands at different locations within the WBW by Olson et al. (2012a, b; DeAngelis et al. (1997); and Esser (1998). Total NPP values range from 380 gC/m2/yr for forest stands dominated by yellow poplar to 790 gC/m2/yr for forest stands dominated by oaks. Revision Notes: This updated vegetation inventory data set includes results of the 2006 survey and updates to previous results based on the latest survey. The 1967-2006 data set completely supersedes the 1967-1997 data set. If you downloaded the 1967-1997 data set before September 3, 2013, you should download the 1967-2006 version at your earliest convenience.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Walker Branch Watershed Vegetation Inventory, 1967-2006, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F819",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F819",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/temperate_forest/NPP_WBW/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/temperate_forest/NPP_WBW/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_WBW.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_WBW.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/819",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/819",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_WBW/comp/NPP_WBW.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_WBW/comp/NPP_WBW.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_WBW/comp/WBW_Curlin_Nelson_TM2271.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_WBW/comp/WBW_Curlin_Nelson_TM2271.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_WBW/comp/WBW_Vegetation_2006.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/temperate_forest/NPP_WBW/comp/WBW_Vegetation_2006.pdf",
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
+            "identifier": "C2755668925-ORNL_CLOUD",
+            "issued": "2023-08-20",
+            "keyword": [
+                "vegetation",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/819",
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
             "spatial": "35.9 -84.3",
+            "temporal": "1967-01-01T00:00:00Z/2006-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Walker Branch Watershed Vegetation Inventory, 1967-2006, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISCCP/B3_NAT",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-09-10. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISCCP/B3_NAT.",
-            "issued": "1999-09-08",
-            "temporal": "1983-07-01T00:00:00Z/2009-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-06",
-            "keyword": [
-                "infrared wavelengths",
-                "visible wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William ROSSOW",
                 "hasEmail": "mailto:wbrossow@ccny.cuny.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C7994310-LARC_ASDC",
             "description": "The ISCCP_B3_NAT data is the International Satellite Cloud Climatology Project (ISCCP) Stage B3 Reduced Radiances in Native Format data product. This is the original radiance data, sampled to 30 Km and 3-hour spacing. Data collection for this product is complete and was collected using several instruments on multiple platforms, please see the instrument and platform list of this record for a comprehensive list. The normalization of all radiances to a standard calibration made these data a globally uniform set of measurements that can be used for detailed cloud process studies.\r\n\r\nISCCP was the first project of the World Climate Research Program (WCRP) and was established in 1982 (WMO-35 1982, Schiffer and Rossow 1983) to: produce a global, reduced resolution, calibrated and normalized radiance data set containing basic information on the properties of the atmosphere from which cloud parameters can be derived; stimulate and coordinate basic research on techniques for inferring the physical properties of clouds from the condensed radiance data set and to apply the resulting algorithms to derive and validate a global cloud climatology for improving the parameterization of clouds in climate models; and promote research using ISCCP data that contributes to improved understanding of the Earth's radiation budget and hydrological cycle. \r\n\r\nSince 1983 an international group of institutions has collected and analyzed satellite radiance measurements from up to five geostationary and two polar orbiting satellites to infer the global distribution of cloud properties and their diurnal, seasonal and inter-annual variations. The primary focus of the first phase of the project (1983-1995) was the elucidation of the role of clouds in the radiation budget (top of the atmosphere and surface). In the second phase of the project (1995 onwards) the analysis also concerns improving understanding of clouds in the global hydrological cycle. \r\n\r\nISCCP analysis combined satellite-measured radiances (Stage B3 data, Schiffer and Rossow 1985), Rossow et al. 1987) with the TOVS atmospheric temperature-humidity and ice/snow correlative data sets to obtain information about clouds and the surface. The analysis method first determined the presence of absence of clouds in each individual image pixel and retrieves the radiometric properties of the cloud for each cloudy pixel and of the surface for each clear pixel. The pixel analysis is performed separately for each satellite radiance data set and the results reported in the Stage DX data product, which has a nominal resolution of 30 km and 3 hours. The Stage D1 product is produced by summarizing the pixel-level results every 3 hours on an equal-area map with 280 km resolution and merging the results from separate satellites with the atmospheric and ice/snow data sets to produce global coverage at each time. The Stage D2 data product is produced by averaging the Stage D1 data over each month, first at each of the eight three hour time intervals and then over all time intervals.",
-            "title": "International Satellite Cloud Climatology Project (ISCCP) Stage B3 Reduced Radiances in Native Format",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISCCP%2FB3_NAT",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISCCP%2FB3_NAT",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISCCP/B3_NAT",
-                    "description": "DOI data set landing page for ISCCP_B3_NAT_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ISCCP_B3_NAT_1",
+                    "downloadURL": "https://doi.org/10.5067/ISCCP/B3_NAT",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7994310-LARC_ASDC",
-                    "description": "Earthdata Search for ISCCP_B3_NAT_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ISCCP_B3_NAT_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C7994310-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/guide/abstract_ISCCP_Stage_B3.pdf",
-                    "description": "ISCCP Stage B3 Reduced Radiances in Native (NAT) Format(ISCCP_B3_NAT) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP Stage B3 Reduced Radiances in Native (NAT) Format(ISCCP_B3_NAT) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/guide/abstract_ISCCP_Stage_B3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/isccp_b3_details.pdf",
-                    "description": "ISCCP_B3_NAT Detailed Temporal Coverage by Satellite",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP_B3_NAT Detailed Temporal Coverage by Satellite",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/isccp_b3_details.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/readme/readme_isccp_b3_nat.txt",
-                    "description": "ISCCP_B3_NAT Data Set Readme",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP_B3_NAT Data Set Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/readme/readme_isccp_b3_nat.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/read_software/isccp_b3_kind.f",
-                    "description": "MODULE B3_KIND - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "MODULE B3_KIND - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/read_software/isccp_b3_kind.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/read_software/isccp_b3_module.f",
-                    "description": "Program to read SRB Release 3 QCSQ Monthly nc - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to read SRB Release 3 QCSQ Monthly nc - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/read_software/isccp_b3_module.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/read_software/isccp_b3_read.f",
-                    "description": "Fortran 90 Code Version of B3READ with the same variable names as older Version set to read one image - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Fortran 90 Code Version of B3READ with the same variable names as older Version set to read one image - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/read_software/isccp_b3_read.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/read_software/isccp_b3_read_linux.f",
-                    "description": "ISCCP B3 read software for use with the Portland Group Compiler (Linux machine only) - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP B3 read software for use with the Portland Group Compiler (Linux machine only) - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/read_software/isccp_b3_read_linux.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/ISCCP",
-                    "description": "ASDC Data and Information for ISCCP",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for ISCCP",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/ISCCP",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/but-the-winds-but-the-spaces",
-                    "description": "Earth Observing System Data and Information System (EOSDIS) Article: \"But the winds... but the spaces\" By Annette Varani",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and Information System (EOSDIS) Article: \"But the winds... but the spaces\" By Annette Varani",
+                    "downloadURL": "https://earthdata.nasa.gov/learn/sensing-our-planet/but-the-winds-but-the-spaces",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/ShadowsDoubt",
-                    "description": "NASA Earth Observatory Article: Shadows of Doubt - Monitoring Cloud Effects",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Shadows of Doubt - Monitoring Cloud Effects",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/ShadowsDoubt",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/StarsCloudsCrops",
-                    "description": "NASA Earth Observatory Article: Stars, Clouds, Crops",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Stars, Clouds, Crops",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/StarsCloudsCrops",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://isccp.giss.nasa.gov/products/products.html",
-                    "description": "ISCCP Data Products List",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP Data Products List",
+                    "downloadURL": "https://isccp.giss.nasa.gov/products/products.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://isccp.giss.nasa.gov/errors.html",
-                    "description": "ISCCP Known and Fixed Errors in Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP Known and Fixed Errors in Data Products",
+                    "downloadURL": "https://isccp.giss.nasa.gov/errors.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://isccp.giss.nasa.gov/newalg.html",
-                    "description": "ISCCP New Algorithm: Summary of Changes",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP New Algorithm: Summary of Changes",
+                    "downloadURL": "https://isccp.giss.nasa.gov/newalg.html",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://isccp.giss.nasa.gov/",
-                    "description": "ISCCP project home page",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP project home page",
+                    "downloadURL": "https://isccp.giss.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/guide/isccp_project.pdf",
-                    "description": "ISCCP Project/Campaign Document for the Langley DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "ISCCP Project/Campaign Document for the Langley DAAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/isccp/guide/isccp_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://isccp.giss.nasa.gov/docs/documents.html",
-                    "description": "Publications for ISCCP",
                     "@type": "dcat:Distribution",
+                    "description": "Publications for ISCCP",
+                    "downloadURL": "https://isccp.giss.nasa.gov/docs/documents.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://avdc.gsfc.nasa.gov/Overview/",
-                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena CA, USA",
                     "@type": "dcat:Distribution",
+                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena CA, USA",
+                    "downloadURL": "https://avdc.gsfc.nasa.gov/Overview/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/esds/competitive-programs/measures/data-analysis-for-isccp",
-                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: Global Cloud Process Studies in the Context of Decadal Climate Variability: Enhancement and Continuation of Data Analysis for the International Satellite Cloud Climatalogy Project (ISCCP)",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and InformationSystem (EOSDIS) Article: Global Cloud Process Studies in the Context of Decadal Climate Variability: Enhancement and Continuation of Data Analysis for the International Satellite Cloud Climatalogy Project (ISCCP)",
+                    "downloadURL": "https://earthdata.nasa.gov/esds/competitive-programs/measures/data-analysis-for-isccp",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://climatedataguide.ucar.edu/",
-                    "description": "NCAR UCAR Climate Data Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NCAR UCAR Climate Data Guide",
+                    "downloadURL": "https://climatedataguide.ucar.edu/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.giss.nasa.gov/tools/panoply/",
-                    "description": "Goddard's Panoply - plots geo-gridded data from netCDF, HDF, GRIB datasets.",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard's Panoply - plots geo-gridded data from netCDF, HDF, GRIB datasets.",
+                    "downloadURL": "https://www.giss.nasa.gov/tools/panoply/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ISCCP/B3_NAT_1/",
-                    "description": "ASDC Direct Data Download for ISCCP_B3_NAT_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ISCCP_B3_NAT_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ISCCP/B3_NAT_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C7994310-LARC_ASDC",
+            "issued": "1999-09-08",
+            "keyword": [
+                "infrared wavelengths",
+                "visible wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISCCP/B3_NAT",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-02-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1983-07-01T00:00:00Z/2009-12-31T23:59:59.999Z",
             "theme": [
                 "ISCCP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "International Satellite Cloud Climatology Project (ISCCP) Stage B3 Reduced Radiances in Native Format"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-2-VISEDR-V1.0",
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
-                "2001 mars odyssey",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The THEMIS VIS-EDR data set contains the raw visible observations. Each qube header includes basic parameters describing the observation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-2-visedr-v1.0_n2rb-cuqe",
+            "issued": "2021-05-21",
+            "keyword": [
+                "2001 mars odyssey",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-THM-2-VISEDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-thm-2-visedr-v1.0_n2rb-cuqe",
-            "description": "The THEMIS VIS-EDR data set contains the raw visible observations. Each qube header includes basic parameters describing the observation.",
-            "title": "ODYSSEY THEMIS VIS EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ODYSSEY THEMIS VIS EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0066-3-ITOKAWAPOL-V1.0",
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
-                "25143 itokawa",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the polarimetry of asteroid 25143 Itokawa published in Cellino et al. (2005). The observations were made from June 26 through July 3, 2004 with the Torino photopolarimeter at the 2.15 m telescope of the El Leoncito Observatory in Argentina. The degree of linear polarization was measured in five filters (Johnson-Cousins UBVRI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0066-3-itokawapol-v1.0_n2sw-d65v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "25143 itokawa",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0066-3-ITOKAWAPOL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0066-3-itokawapol-v1.0_n2sw-d65v",
-            "description": "This data set contains the polarimetry of asteroid 25143 Itokawa published in Cellino et al. (2005). The observations were made from June 26 through July 3, 2004 with the Torino photopolarimeter at the 2.15 m telescope of the El Leoncito Observatory in Argentina. The degree of linear polarization was measured in five filters (Johnson-Cousins UBVRI).",
-            "title": "POLARIMETRY OF ASTEROID ITOKAWA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "POLARIMETRY OF ASTEROID ITOKAWA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10846",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
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
-                "goddard space flight center",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Frederick Porter",
                 "hasEmail": "mailto:frederick.s.porter@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10846",
             "description": "\"Since the summer of 2000 we have successfully deployed a high resolution x-ray microcalorimeter spectrometer, based on the spaceflight XRS instrument, at the Electron Beam Ion Trap (EBIT) facility at the Lawrence Livermore National Laboratory. Over the last decade, this highly successful partnership has made fundamental measurements in laboratory astrophysics including the measurements of the absolute cross sections of all the Fe L shell transitions from Fe XVII to Fe XXIV, line ratios in Fe and Ni L shell transitions, measurements of Fe K shell emission over a wide range of electron energies, and direct measurements of charge exchange emission from highly ionized Fe, O, N, and most recently L shell S, using a variety of donor gases. This work has resulted in the publication of over 30 peer-reviewed articles with many more either submitted or in preparation. The newest addition to the facility, the ECS microcalorimeter spectrometer, developed under this program, has performed flawlessly as a facility-class instrument since 2007.\n\n\n\nWe propose here to continue our highly successful partnership and deploy new technology to resolve lines in the important 1/4 keV band that encompasses the M-shell iron emission and the L shell emission, including charge exchange, of many of the lower-Z elements, such as Si, S, Mg, Ne, Ca, and Ar. We thus propose completing a new spectrometer that will bring substantially improved performance to the laboratory astrophysics program at EBIT and will enable fundamentally new measurements. Thus, in addition to maintaining the current spectrometers, which will begin this work, a significant component of this proposal is the completion of a new spectrometer leveraged off of the substantial progress in high-resolution x-ray detectors developed for the International X-ray Observatory mission. The spectrometer will be composed of a detector system with unparalleled spectral resolution: 2 eV resolution across the 0.05-10 keV band. This will allow",
-            "title": "High Energy Laboratory Astrophysics using an X-Ray Microcalorimeter with an Electron Beam Ion Trap Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10846",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10846",
+            "issued": "2010-01-01",
+            "keyword": [
+                "project",
+                "goddard space flight center",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10846",
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
+            "temporal": "2010-01-01T00:00:00Z/2014-01-01T00:00:00Z",
+            "title": "High Energy Laboratory Astrophysics using an X-Ray Microcalorimeter with an Electron Beam Ion Trap Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-2-JUPITER-V3.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 3.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-2-jupiter-v3.0_n2up-9tv9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-2-JUPITER-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-2-jupiter-v3.0_n2up-9tv9",
-            "description": "This data set contains Raw data taken by the New Horizons                Solar Wind Around Pluto                                                instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 3.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SWAP JUPITER ENCOUNTER                                                  \n      RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      SWAP JUPITER ENCOUNTER                                                  \n      RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NQLCDOZJYAKX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP Enhanced L3 Radiometer Global and Northern Hemisphere Daily 9 km EASE-Grid Freeze/Thaw State V004. Version 004. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NQLCDOZJYAKX.",
-            "issued": "2015-03-31",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "keyword": [
-                "earth science",
-                "cryosphere",
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
-            "identifier": "C2938664439-NSIDC_CPRD",
             "description": "This enhanced Level-3 (L3) product provides a daily composite of global and Northern Hemisphere landscape freeze/thaw conditions retrieved by the Soil Moisture Active Passive (SMAP) radiometer from 6:00 a.m. descending and 6:00 p.m. ascending half-orbit passes. This product is derived from SMAP enhanced Level-1C brightness temperatures (SPL1CTB_E). Backus-Gilbert optimal interpolation techniques are used to extract maximum information from SMAP antenna temperatures and convert them to brightness temperatures. The data are then posted to two 9 km Earth-fixed, Equal-Area Scalable Earth Grids, Version 2.0 (EASE-Grid 2.0): a global cylindrical and a Northern Hemisphere azimuthal.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP Enhanced L3 Radiometer Global and Northern Hemisphere Daily 9 km EASE-Grid Freeze/Thaw State V004",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-208,-76,149,89&l=SMAP_L3_Passive_Enhanced_Night_Freeze_Thaw(disabled=2),SMAP_L3_Passive_Enhanced_Day_Freeze_Thaw(disabled=2),Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-14",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNQLCDOZJYAKX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNQLCDOZJYAKX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL3FTP_E+V004",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL3FTP_E+V004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938664439-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938664439-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-208%2C-76%2C149%2C89&l=SMAP_L3_Passive_Enhanced_Night_Freeze_Thaw%28disabled%3D2%29%2CSMAP_L3_Passive_Enhanced_Day_Freeze_Thaw%28disabled%3D2%29%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-14",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-208%2C-76%2C149%2C89&l=SMAP_L3_Passive_Enhanced_Night_Freeze_Thaw%28disabled%3D2%29%2CSMAP_L3_Passive_Enhanced_Day_Freeze_Thaw%28disabled%3D2%29%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-14",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NQLCDOZJYAKX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NQLCDOZJYAKX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NQLCDOZJYAKX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NQLCDOZJYAKX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-208,-76,149,89&l=SMAP_L3_Passive_Enhanced_Night_Freeze_Thaw(disabled=2),SMAP_L3_Passive_Enhanced_Day_Freeze_Thaw(disabled=2),Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor&t=2015-04-14",
+            "identifier": "C2938664439-NSIDC_CPRD",
+            "issued": "2015-03-31",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/NQLCDOZJYAKX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -85.044 180.0 85.044",
+            "temporal": "2015-03-31T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAP Enhanced L3 Radiometer Global and Northern Hemisphere Daily 9 km EASE-Grid Freeze/Thaw State V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AGN-1ROPD",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2021-06-22. Sentinel-6A MF Jason-CS L1B GNSS-RO-POD Tracking Data Hourly. Version F. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AGN-1ROPD.",
-            "issued": "2020-11-28",
-            "temporal": "2020-11-28T09:20:35Z/2023-05-15T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-09",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "solid earth",
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
-            "identifier": "C1968980589-POCLOUD",
-            "description": "Provides L1B GNSS-RO-POD tracking data for the Sentinel-6A radar altimetry mission.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L1B GNSS-RO-POD Tracking Data Hourly",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides L1B GNSS-RO-POD tracking data for the Sentinel-6A radar altimetry mission.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AGN-1ROPD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AGN-1ROPD",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968980589-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968980589-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968980589-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968980589-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L1B_GNSS_RO_POD_HOURLY.jpg",
+            "identifier": "C1968980589-POCLOUD",
+            "issued": "2020-11-28",
+            "keyword": [
+                "solid earth",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AGN-1ROPD",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-09",
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
+            "temporal": "2020-11-28T09:20:35Z/2023-05-15T00:00:00Z",
             "theme": [
                 "Sentinel-6",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-6A MF Jason-CS L1B GNSS-RO-POD Tracking Data Hourly"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-MET-2-L-EDR-V1.0",
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
+            "description": "The PHX Atmospheric Lidar Profiles product contains unprocessed laser scattering atmospheric profiles for photon counting data at 532nm, and analog data at both 532 and 1064nm wavelengths (expressed in Dignal Numbers). The range data is provided as a time series of profiles between 5 and 90 min in total duration, with each profile representing an accumulation or average over 1.28-20.24 sec. Supplemental data of estimated laser power and inter-profile analog background skylight estimates are also provided.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-met-2-l-edr-v1.0_n34d-i3d2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-MET-2-L-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-met-2-l-edr-v1.0_n34d-i3d2",
-            "description": "The PHX Atmospheric Lidar Profiles product contains unprocessed laser scattering atmospheric profiles for photon counting data at 532nm, and analog data at both 532 and 1064nm wavelengths (expressed in Dignal Numbers). The range data is provided as a time series of profiles between 5 and 90 min in total duration, with each profile representing an accumulation or average over 1.28-20.24 sec. Supplemental data of estimated laser power and inter-profile analog background skylight estimates are also provided.",
-            "title": "PHOENIX MARS MET LIDAR ATMOSPHERIC PROFILES EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS MET LIDAR ATMOSPHERIC PROFILES EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-ISS-2-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This Voyager 2 Uranus data set is available on CD-ROM and magnetic tape.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-iss-2-edr-v1.0_n37s-vmgz",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "plaque",
@@ -1115358,389 +1115360,401 @@
                 "vega",
                 "cal lamps"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-ISS-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-iss-2-edr-v1.0_n37s-vmgz",
-            "description": "This Voyager 2 Uranus data set is available on CD-ROM and magnetic tape.",
-            "title": "VG2 URANUS IMAGING SCIENCE SUBSYSTEM EDITED EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 URANUS IMAGING SCIENCE SUBSYSTEM EDITED EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/LT66296ATQD7",
             "citation": "Kevin W. Bowman. 2022-04-04. TRPSYL2O3CRSFS. Version 1. TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/LT66296ATQD7. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2O3CRSFS_1.html. Digital Science Data.",
-            "issued": "2022-04-01",
-            "temporal": "2021-02-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1029/2006JD007258",
-                "https://doi.org/10.5194/acp-10-9901-2010",
-                "https://doi.org/10.1029/2007JD008819",
-                "https://doi.org/10.5194/amt-6-1413-2013",
-                "https://doi.org/10.5194/amt-11-5587-2018"
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
-            "identifier": "C2247040772-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Summary Product contains the vertical distribution of the retrieved atmospheric state of ozone (O3),  and formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream standard product is global for the time period from 2021-02-01 to 2021-05-21, when the CrIS-SNPP processing was discontinued. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 26 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2O3CRSFS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP O3 (Forward Stream, Summary Product) at 261 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Summary Product V1 (TRPSYL2O3CRSFS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2O3CRSFS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLT66296ATQD7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLT66296ATQD7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2O3CRSFS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP O3 (Forward Stream, Summary Product) at 261 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP O3 (Forward Stream, Summary Product) at 261 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2O3CRSFS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2O3CRSFS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2O3CRSFS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2O3CRSFS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2O3CRSFS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2O3CRSFS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2O3CRSFS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Summary/TRPSYL2O3CRSFS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Summary/TRPSYL2O3CRSFS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2O3CRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Summary/TRPSYL2O3CRSFS.1/doc/TROPESS_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-O3_L2_Product_Quick_Start_User_Guide_Summary_only.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-O3_L2_Product_Quick_Start_User_Guide_Summary_only.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP O3 (Forward Stream, Summary Product) at 261 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2O3CRSFS_Sample.png",
+            "identifier": "C2247040772-GES_DISC",
+            "issued": "2022-04-01",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/LT66296ATQD7",
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
+                "https://doi.org/10.1029/2006JD007258",
+                "https://doi.org/10.5194/acp-10-9901-2010",
+                "https://doi.org/10.1029/2007JD008819",
+                "https://doi.org/10.5194/amt-6-1413-2013",
+                "https://doi.org/10.5194/amt-11-5587-2018"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSYL2O3CRSFS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-02-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Ozone for Forward Stream, Summary Product V1 (TRPSYL2O3CRSFS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L4M/GSM/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L4M/GSM/2022.",
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
-            "identifier": "C2802700402-OB_DAAC",
             "description": "The SeaWiFS instrument was launched by Orbital Sciences Corporation on the OrbView-2 (a.k.a. SeaStar) satellite in August 1997, and collected data from September 1997 until the end of mission in December 2010. SeaWiFS had 8 spectral bands from 412 to 865 nm. It collected global data at 4 km resolution, and local data (limited onboard storage and direct broadcast) at 1 km. The mission and sensor were optimized for ocean color measurements, with a local noon (descending) equator crossing time orbit, fore-and-aft tilt capability, full dynamic range, and low polarization sensitivity.",
-            "title": "OrbView-2 SeaWiFS 4M Global Mapped Garver-Siegel-Maritorena Model (GSM) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FORBVIEW-2%2FSeaWiFS%2FL4M%2FGSM%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FORBVIEW-2%2FSeaWiFS%2FL4M%2FGSM%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-4%20Mapped/SeaWiFS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-4%20Mapped/SeaWiFS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ORBVIEW-2/SeaWiFS/L4M/GSM/2022",
-                    "description": "OrbView-2 SeaWiFS Level-4M Garver-Siegel-Maritorena Model (GSM) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "OrbView-2 SeaWiFS Level-4M Garver-Siegel-Maritorena Model (GSM) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ORBVIEW-2/SeaWiFS/L4M/GSM/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/SeaWiFS/L4SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for OrbView-2 SeaWiFS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for OrbView-2 SeaWiFS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/SeaWiFS/L4SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2802700402-OB_DAAC",
+            "issued": "2023-11-16",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L4M/GSM/2022",
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
+            "title": "OrbView-2 SeaWiFS 4M Global Mapped Garver-Siegel-Maritorena Model (GSM) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-5-EDS-V1.0",
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
+            "description": "This data set contains 5600 ionospheric electron density profiles (EDS files) derived from Mars Global Surveyor (MGS) radio occultation data.  The profiles were previously archived in the MGS-M-RSS-5-SDP-V1.0 data set along with other reduced data products from the MGS Radio Science Team (RST).  Here they have been pulled from the original 38 volumes and reorganized in chronological order on a single volume.  The profiles themselves have not been modified, and the labels have been edited only to conform with the requirements of the new data set.  This set of profiles is accompanied by a single occultation summary file which lists key characteristics of each experiment.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-5-eds-v1.0_n39e-xaxa",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-5-EDS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-5-eds-v1.0_n39e-xaxa",
-            "description": "This data set contains 5600 ionospheric electron density profiles (EDS files) derived from Mars Global Surveyor (MGS) radio occultation data.  The profiles were previously archived in the MGS-M-RSS-5-SDP-V1.0 data set along with other reduced data products from the MGS Radio Science Team (RST).  Here they have been pulled from the original 38 volumes and reorganized in chronological order on a single volume.  The profiles themselves have not been modified, and the labels have been edited only to conform with the requirements of the new data set.  This set of profiles is accompanied by a single occultation summary file which lists key characteristics of each experiment.",
-            "title": "MGS RS: IONOSPHERIC ELECTRON DENSITY\n                                     PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS RS: IONOSPHERIC ELECTRON DENSITY\n                                     PROFILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD29.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS/Terra Sea Ice Extent 5-Min L2 Swath 1km V061. Version 61. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD29.061.",
-            "issued": "2000-02-24",
-            "temporal": "2000-02-24T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "oceans",
-                "sea ice",
-                "ngda",
-                "national geospatial data asset",
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
-            "identifier": "C1646610390-NSIDC_ECS",
             "description": "This global Level-2 (L2) product provides daily sea ice extent and ice surface temperature. The data are derived from Level-1B radiances acquired by the Moderate Resolution Imaging Spectroradiometer (MODIS) on board the Terra satellite. Each data granule contains 5 minutes of swath data observed at a resolution of 1000 m.\n\nThe terms \"Version 61\" and \"Collection 6.1\" are used interchangeably in reference to this release of MODIS data.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "MODIS/Terra Sea Ice Extent 5-Min L2 Swath 1km V061",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-185,-84,156,73&l=MODIS_Terra_Ice_Surface_Temp_Night,MODIS_Terra_Ice_Surface_Temp_Day,MODIS_Terra_Sea_Ice(disabled=1-2-3-4-5-6-7-8-9-10),Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD29.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD29.061",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOST/MOD29.061/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOST/MOD29.061/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD29+V061",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MOD29+V061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/MOD29/versions/61/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/MOD29/versions/61/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-185%2C-84%2C156%2C73&l=MODIS_Terra_Ice_Surface_Temp_Night%2CMODIS_Terra_Ice_Surface_Temp_Day%2CMODIS_Terra_Sea_Ice%28disabled%3D1-2-3-4-5-6-7-8-9-10%29%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-185%2C-84%2C156%2C73&l=MODIS_Terra_Ice_Surface_Temp_Night%2CMODIS_Terra_Ice_Surface_Temp_Day%2CMODIS_Terra_Sea_Ice%28disabled%3D1-2-3-4-5-6-7-8-9-10%29%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD29.061",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD29.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD29.061",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD29.061",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-185,-84,156,73&l=MODIS_Terra_Ice_Surface_Temp_Night,MODIS_Terra_Ice_Surface_Temp_Day,MODIS_Terra_Sea_Ice(disabled=1-2-3-4-5-6-7-8-9-10),Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C1646610390-NSIDC_ECS",
+            "issued": "2000-02-24",
+            "keyword": [
+                "oceans",
+                "sea ice",
+                "ngda",
+                "national geospatial data asset",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD29.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Sea Ice Extent 5-Min L2 Swath 1km V061"
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
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2005.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY05 NASA Operating Plan",
+                    "downloadURL": "http://www.nasa.gov/pdf/107781main_FY_05_op_plan.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "FY05 NASA Operating Plan"
+                }
+            ],
+            "identifier": "OCIO-Fitara-89",
             "issued": "2004-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "financial",
                 "budget",
@@ -1115749,611 +1115763,611 @@
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
-            "identifier": "OCIO-Fitara-89",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2005.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2005: NASA Operating Plan",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/107781main_FY_05_op_plan.pdf",
-                    "description": "FY05 NASA Operating Plan",
-                    "@type": "dcat:Distribution",
-                    "title": "FY05 NASA Operating Plan"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2005: NASA Operating Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/1a5z-3h71",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2023-07-22. SDG Indicator 11.2.1: Urban Access to Public Transport, 2023 Release. Version 2023.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/1a5z-3h71. https://doi.org/10.7927/1a5z-3h71.",
-            "issued": "2023-07-31",
-            "temporal": "2015-01-01T00:00:00Z/2022-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-31",
-            "references": [
-                "https://doi.org/10.7927/fcre-m572",
-                "https://doi.org/10.7927/zc4h-hh18",
-                "https://doi.org/10.7927/eavc-4k45",
-                "https://doi.org/10.7927/gxnr-sx57"
-            ],
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "infrastructure"
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
-            "identifier": "C2762314304-SEDAC",
-            "description": "The SDG Indicator 11.2.1: Urban Access to Public Transport, 2023 Release, part of the SDGI collection, measures the proportion of the population in a city that has convenient access to public transport. UN SDG 11 is \"make cities and human settlements inclusive, safe, resilient and sustainable\". Improving access to public transport services is integral to achieving the objectives of SDG 11. According to the UN Sustainable Transport, Sustainable Development 2021 Interagency Report, \"only about half the world's urban population have convenient access to public transport\". The report highlights that access to sustainable transport can help reduce food insecurity, boost economies, empower women, and connect people to key health, education, and financial services. As one measure of progress towards SDG 11, the UN has established SDG indicator 11.2.1. The indicator was computed as the proportion of WorldPop gridded population within either 0.5 kilometer walking distance to a low-capacity OpenStreetMap (OSM) public transport point or 1 kilometer walking distance to a high-capacity OSM public transport point. Cities were delineated using the European Commission Joint Research Centre (JRC) Urban Center Database (UCDB). The SDG indicator 11.2.1 data set provides estimates for the proportion of population with convenient access to public transport for 5,749 urban centers across 178 countries.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "SDG Indicator 11.2.1: Urban Access to Public Transport, 2023 Release",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SDG Indicator 11.2.1: Urban Access to Public Transport, 2023 Release, part of the SDGI collection, measures the proportion of the population in a city that has convenient access to public transport. UN SDG 11 is \"make cities and human settlements inclusive, safe, resilient and sustainable\". Improving access to public transport services is integral to achieving the objectives of SDG 11. According to the UN Sustainable Transport, Sustainable Development 2021 Interagency Report, \"only about half the world's urban population have convenient access to public transport\". The report highlights that access to sustainable transport can help reduce food insecurity, boost economies, empower women, and connect people to key health, education, and financial services. As one measure of progress towards SDG 11, the UN has established SDG indicator 11.2.1. The indicator was computed as the proportion of WorldPop gridded population within either 0.5 kilometer walking distance to a low-capacity OpenStreetMap (OSM) public transport point or 1 kilometer walking distance to a high-capacity OSM public transport point. Cities were delineated using the European Commission Joint Research Centre (JRC) Urban Center Database (UCDB). The SDG indicator 11.2.1 data set provides estimates for the proportion of population with convenient access to public transport for 5,749 urban centers across 178 countries.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F1a5z-3h71",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2F1a5z-3h71",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdgi/sdgi-11-2-1-urban-access-public-transport-2023/sdgi-11-2-1-urban-access-public-transport-2023-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/sdgi/sdgi-11-2-1-urban-access-public-transport-2023/sdgi-11-2-1-urban-access-public-transport-2023-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/sdgi-11-2-1-urban-access-public-transport-2023/maps",
+            "identifier": "C2762314304-SEDAC",
+            "issued": "2023-07-31",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "infrastructure"
+            ],
+            "landingPage": "https://doi.org/10.7927/1a5z-3h71",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/fcre-m572",
+                "https://doi.org/10.7927/zc4h-hh18",
+                "https://doi.org/10.7927/eavc-4k45",
+                "https://doi.org/10.7927/gxnr-sx57"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-01-01T00:00:00Z/2022-12-31T00:00:00Z",
             "theme": [
                 "SDGI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SDG Indicator 11.2.1: Urban Access to Public Transport, 2023 Release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRII%2FHRIV%2FMRI-6-EPOXI-TEMPS-V2.0",
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
-                "calibration",
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains the raw and smoothed (averaged) instrument thermal telemetry for the entire EPOXI mission, from 04 October 2007 through 06 February 2011. Measurements were collected by 59 thermal sensors located in the HRII, HRIV, and MRI instruments, on the instrument platform, and on the solar wings of the Deep Impact flyby spacecraft.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hrii-hriv-mri-6-epoxi-temps-v2.0_n3ey-64q8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-HRII%2FHRIV%2FMRI-6-EPOXI-TEMPS-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-hrii-hriv-mri-6-epoxi-temps-v2.0_n3ey-64q8",
-            "description": "This dataset contains the raw and smoothed (averaged) instrument thermal telemetry for the entire EPOXI mission, from 04 October 2007 through 06 February 2011. Measurements were collected by 59 thermal sensors located in the HRII, HRIV, and MRI instruments, on the instrument platform, and on the solar wings of the Deep Impact flyby spacecraft.",
-            "title": "EPOXI HRII/HRIV/MRI INSTRUMENT TEMPERATURES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "EPOXI HRII/HRIV/MRI INSTRUMENT TEMPERATURES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRPHOT-3-RDR-HALLEY-V1.0",
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
-                "halley",
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Photometry subnetwork contains 2204 observations spanning dates from 1984 September 14 through 1988 April 08.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irphot-3-rdr-halley-v1.0_n3gy-v58b",
+            "issued": "2021-05-21",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRPHOT-3-RDR-HALLEY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irphot-3-rdr-halley-v1.0_n3gy-v58b",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Infrared Photometry subnetwork contains 2204 observations spanning dates from 1984 September 14 through 1988 April 08.",
-            "title": "IHW COMET HALLEY INFRARED PHOTOMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET HALLEY INFRARED PHOTOMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3O3M.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3O3M.006. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-03T00:00:00Z/2018-01-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "atmosphere",
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
-            "identifier": "C1703619764-LARC",
             "description": "TL3O3M_6 is the Tropospheric Emission Spectrometer (TES)/Aura Level 3 Ozone (O3) Monthly Gridded Version 6 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. This product consisted of daily atmospheric temperature and volume mixing ratio (VMR) for the atmospheric species, ozone, which were provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolated the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products were composed of L3 HDF-EOS grid data. A separate product file was produced for each different atmospheric species. TES obtained data in two basic observation modes: Limb or Nadir. The product may have contained, in separate folders, limb data, nadir data, or both folders could have been present. \r\rSpecific to L3 processing were the terms Daily and Monthly, representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process were complete Global Surveys; in other words a Global Survey was not split in relation to time when they were input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represented Global Surveys that were initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly. Details of the format of this product can be found in the TES Data Products Specifications (DPS).",
-            "title": "TES/Aura L3 Ozone Monthly Gridded V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3O3M.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3O3M.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3O3M.006",
-                    "description": "DOI data set landing page for TL3O3M_6",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3O3M_6",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3O3M.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3O3M.006/",
-                    "description": "ASDC Direct Data Download for TL3O3M_6",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL3O3M_6",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3O3M.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3O3M.006/contents.html",
-                    "description": "OPeNDAP data access for TL3O3M_6",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3O3M_6",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3O3M.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703619764-LARC",
-                    "description": "Earthdata Search for TL3O3M_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3O3M_6 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703619764-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
+            "identifier": "C1703619764-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3O3M.006",
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
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-09-03T00:00:00Z/2018-01-31T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 Ozone Monthly Gridded V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/7K31MCH5XXZA",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge IMU L0 Raw Inertial Measurement Unit Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/7K31MCH5XXZA.",
-            "issued": "2009-01-01",
-            "temporal": "2009-01-01T00:00:00Z/2010-12-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2010-12-30",
-            "keyword": [
-                "spectral/engineering",
-                "platform characteristics",
-                "earth science"
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
-            "identifier": "C1386246599-NSIDCV0",
             "description": "This data set contains Inertial Measurement Unit (IMU) readings, including latitude, longitude, altitude, velocity, pitch, roll, and true heading, taken over Antarctica using the Systron Donner Inertial MMQ-G inertial measurement unit. The data were collected by scientists working on the Investigating the Cryospheric Evolution of the Central Antarctic Plate (ICECAP) project, which is funded by the National Science Foundation (NSF) and the Natural Environment Research Council (NERC), with additional support from NASA Operation IceBridge.",
-            "title": "IceBridge IMU L0 Raw Inertial Measurement Unit Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7K31MCH5XXZA",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F7K31MCH5XXZA",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IPUTI0_UTIGIMUraw_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IPUTI0_UTIGIMUraw_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7K31MCH5XXZA",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/7K31MCH5XXZA",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/7K31MCH5XXZA",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/7K31MCH5XXZA",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246599-NSIDCV0",
+            "issued": "2009-01-01",
+            "keyword": [
+                "spectral/engineering",
+                "platform characteristics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/7K31MCH5XXZA",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2010-12-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2009-01-01T00:00:00Z/2010-12-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge IMU L0 Raw Inertial Measurement Unit Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/510/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-01-19",
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
-            "identifier": "DASHLINK_510",
             "description": "The environmental impact of aviation is enormous given the fact that\r\nin the US alone there are nearly 6 million flights per year of commercial aircraft.\r\nThis situation has driven numerous policy and procedural measures to help develop\r\nenvironmentally friendly technologies which are safe and affordable and reduce the\r\nenvironmental impact of aviation. However, many of these technologies require significant\r\ninitial investment in newer aircraft fleets and modifications to existing regulations\r\nwhich are both long and costly enterprises. We propose to use an anomaly\r\ndetection method based on Virtual Sensors to help detect overconsumption of fuel in\r\naircraft which relies only on the data recorded during flight of most existing commercial\r\naircraft, thus significantly reducing the cost and complexity of implementing this\r\nmethod. The Virtual Sensors developed here are ensemble-learning regression models\r\nfor detecting the overconsumption of fuel based on instantaneous measurements\r\nof the aircraft state. This approach requires no additional information about standard\r\noperating procedures or other encoded domain knowledge. We present experimental\r\nresults on three data sets and compare five different Virtual Sensors algorithms. The\r\nfirst two data sets are publicly available and consist of a simulated data set from a\r\nflight simulator and a real-world turbine disk.We show the ability to detect anomalies\r\nwith high accuracy on these data sets. These sets contain seeded faults, meaning that\r\nthey have been deliberately injected into the system. The second data set is from realworld\r\nfleet of 84 jet aircraft where we show the ability to detect fuel overconsumption\r\nwhich can have a significant environmental and economic impact. To the best of our\r\nknowledge, this is the first study of its kind in the aviation domain.",
-            "title": "Greener Aviation with Virtual Sensors:  A Case Study",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Srivastava_DMKD_2012.pdf",
-                    "description": "Greener Aviation",
                     "@type": "dcat:Distribution",
+                    "description": "Greener Aviation",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Srivastava_DMKD_2012.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Srivastava DMKD 2012.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_510",
+            "issued": "2012-01-19",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/510/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Greener Aviation with Virtual Sensors:  A Case Study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-LET-3-RDR-FLUX-32SEC-V1.0",
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
+            "description": "This data set contains COSPIN Low Energy Telescope (LET) particle flux rates from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-16.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-let-3-rdr-flux-32sec-v1.0_n3qw-v9rp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-COSPIN-LET-3-RDR-FLUX-32SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-cospin-let-3-rdr-flux-32sec-v1.0_n3qw-v9rp",
-            "description": "This data set contains COSPIN Low Energy Telescope (LET) particle flux rates from the Ulysses Jupiter encounter 1992-Jan-25 to 1992-Feb-16.",
-            "title": "ULY JUP COSPIN LOW ENERGY TELESCOPE 32 SEC PARTICLE FLUX",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULY JUP COSPIN LOW ENERGY TELESCOPE 32 SEC PARTICLE FLUX"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/QF7VBMUAKBVP",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Ancillary Soil Characteristics Data, Oklahoma, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/QF7VBMUAKBVP.",
-            "issued": "2003-06-01",
-            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-31",
-            "keyword": [
-                "soils",
-                "agriculture",
-                "land surface",
-                "earth science"
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
-            "identifier": "C1386250722-NSIDCV0",
             "description": "The SMEX03 Ancillary Soil Characteristics data set contains data for the regional study areas of Alabama, Georgia, and Oklahoma, USA as part of the 2003 Soil Moisture Experiment (SMEX03). The original data were extracted from a multi-layer soil characteristics database for the conterminous United States and generated using Environmental Systems Research Institute (ESRI) ArcMap software for each regional study area.",
-            "title": "SMEX03 Ancillary Soil Characteristics Data, Oklahoma, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQF7VBMUAKBVP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FQF7VBMUAKBVP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/soils/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/soils/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/soils/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/soils/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QF7VBMUAKBVP",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/QF7VBMUAKBVP",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/QF7VBMUAKBVP",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/QF7VBMUAKBVP",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250722-NSIDCV0",
+            "issued": "2003-06-01",
+            "keyword": [
+                "soils",
+                "agriculture",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/QF7VBMUAKBVP",
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
             "spatial": "-98.39 34.44 -97.7 36.87",
+            "temporal": "2003-06-01T00:00:00Z/2003-07-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Ancillary Soil Characteristics Data, Oklahoma, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566467-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "U.S. Geological Survey (USGS) EROS Data Center \n(EDC). 1980-01-01. National High Altitude Photography. Sioux Falls, SD USA. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. http://earthexplorer.usgs.gov. Photographs.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EROS CENTER",
+                "hasEmail": "mailto:lta@usgs.gov"
+            },
+            "creator": "U.S. Geological Survey (USGS) EROS Data Center \n(EDC)",
+            "data-presentation-form": "Photographs",
+            "description": "The National High Altitude Photography (NHAP) program, which was operated from 1980 - 1989, was coordinated by the U.S. Geological Survey as an interagency project to eliminate duplicate photography in various Government programs.  The aim of the program was to cover the 48 conterminous states of the USA over a 5-year span.  In the NHAP program, black-and-white and color-infrared aerial photographs were obtained on 9-inch film from an altitude of 40,000 feet above mean terrain elevation and are centered over USGS 7.5-minute quadrangles.  The color-infrared photographs are at a scale of 1:58,000 (1 inch equals about .9 miles) and the black-and-white photographs are at a scale of 1:80,000 (1 inch equals about 1.26 miles).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         Query and order satellite images, aerial photographs, and cartographic products through the U.S. Geological Survey. Log in as a guest or as a registered user. Registered users have access to more features than guests do. If you plan on using EarthExplorer frequently, you may wish to register. Please note that this site uses Session Cookies and Java applets.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1220566467-USGS_LTA",
             "issued": "2019-09-20",
-            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-25",
             "keyword": [
                 "spectral/engineering",
                 "surface radiative properties",
@@ -1116362,332 +1116376,294 @@
                 "earth science",
                 "topography"
             ],
-            "data-presentation-form": "Photographs",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EROS CENTER",
-                "hasEmail": "mailto:lta@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566467-USGS_LTA.html",
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
-            "identifier": "C1220566467-USGS_LTA",
-            "description": "The National High Altitude Photography (NHAP) program, which was operated from 1980 - 1989, was coordinated by the U.S. Geological Survey as an interagency project to eliminate duplicate photography in various Government programs.  The aim of the program was to cover the 48 conterminous states of the USA over a 5-year span.  In the NHAP program, black-and-white and color-infrared aerial photographs were obtained on 9-inch film from an altitude of 40,000 feet above mean terrain elevation and are centered over USGS 7.5-minute quadrangles.  The color-infrared photographs are at a scale of 1:58,000 (1 inch equals about .9 miles) and the black-and-white photographs are at a scale of 1:80,000 (1 inch equals about 1.26 miles).",
             "release-place": "Sioux Falls, SD USA",
-            "creator": "U.S. Geological Survey (USGS) EROS Data Center \n(EDC)",
-            "title": "National High Altitude Photography",
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
+            "temporal": "1970-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National High Altitude Photography"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_ER2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_ER2_Data_1.",
-            "issued": "2022-09-09",
-            "temporal": "1998-11-10T00:00:00Z/2000-03-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-09",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "platform characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carl Sorenson",
                 "hasEmail": "mailto:cesorenson@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836877-LARC_ASDC",
             "description": "SOLVE1_Miscellaneous_ER2_Data is the supplementary miscellaneous data for the ER-2 aircraft collected during the SAGE III Ozone Loss and Validation Experiment (SOLVE). Data collection for this product is complete.\r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE I Miscellaneous ER-2 Aircraft Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_Miscellaneous_ER2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_Miscellaneous_ER2_Data_1",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836877-LARC_ASDC",
-                    "description": "Earthdata Search client for SOLVE1_Miscellaneous_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for SOLVE1_Miscellaneous_ER2_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836877-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_ER2_Data_1",
-                    "description": "DOI for SOLVE1_Miscellaneous_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SOLVE1_Miscellaneous_ER2_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Miscellaneous_ER2_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE1_Miscellaneous_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE1_Miscellaneous_ER2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Miscellaneous_ER2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836877-LARC_ASDC",
+            "issued": "2022-09-09",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "platform characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Miscellaneous_ER2_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>11.0 -128.2 11.0 75.0 89.2 75.0 89.2 -128.2 11.0 -128.2</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-11-10T00:00:00Z/2000-03-18T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE I Miscellaneous ER-2 Aircraft Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/JOSSWALDVOGEL/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Moisseev, Dmitri N, Matti  Leskinen and Sabine  Goeke.2019. GPM Ground Validation Joss-Waldvogel Disdrometer (JW) LPVEx [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/LPVEX/JOSSWALDVOGEL/DATA101",
-            "issued": "2019-12-11",
-            "temporal": "2010-09-10T00:00:00Z/2010-11-09T07:56:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "clouds",
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
-            "identifier": "C1979606207-GHRC_DAAC",
             "description": "The GPM Ground Validation Joss-Waldvogel Disdrometer (JW) LPVEx dataset consists of precipitation drop size distribution (DSD) data collected by the Joss-Waldvogel (JW) disdrometer during the GPM Ground Validation Light Precipitation Validation Experiment (LPVEx). This field campaign took place around the Gulf of Finland in September and October of 2010. The goal of the campaign was to provide additional high-latitude, light rainfall measurements for the improvement of GPM satellite precipitation algorithms. The JW disdrometer dataset files are available in ASCII text format from September 10 through November 9, 2010.",
-            "title": "GPM Ground Validation Joss-Waldvogel Disdrometer (JW) LPVEx V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FJOSSWALDVOGEL%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FJOSSWALDVOGEL%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmjwlpvex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmjwlpvex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.arm.gov/publications/tech_reports/handbooks/disdrometer_handbook.pdf",
-                    "description": "Impact Disdrometer Instrument Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Impact Disdrometer Instrument Handbook",
+                    "downloadURL": "https://www.arm.gov/publications/tech_reports/handbooks/disdrometer_handbook.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ictinternational.com/content/uploads/2018/07/Disdrodata-User-Guide-4.0-January-2018.pdf",
-                    "description": "Disdrometer RD-80: User Guide for DISDRODATA 4.0",
                     "@type": "dcat:Distribution",
+                    "description": "Disdrometer RD-80: User Guide for DISDRODATA 4.0",
+                    "downloadURL": "http://www.ictinternational.com/content/uploads/2018/07/Disdrodata-User-Guide-4.0-January-2018.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/sites/default/files/lpvex_science_plan_June2010.pdf",
-                    "description": "Light Precipitation Validation Experiment (LPVEx) Science Plan",
                     "@type": "dcat:Distribution",
+                    "description": "Light Precipitation Validation Experiment (LPVEx) Science Plan",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/sites/default/files/lpvex_science_plan_June2010.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ntrs.nasa.gov/search.jsp?R=20110015768",
-                    "description": "The NASA CloudSat/GPM Light Precipitation Validation Experiment (LPVEx)",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA CloudSat/GPM Light Precipitation Validation Experiment (LPVEx)",
+                    "downloadURL": "https://ntrs.nasa.gov/search.jsp?R=20110015768",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GPMGV/LPVEX/DATA101",
-                    "description": "LPVEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx Field Campaign Collection DOI",
+                    "downloadURL": "https://doi.org/10.5067/GPMGV/LPVEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/jw/doc/gpmjwlpvex_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/lpvex/jw/doc/gpmjwlpvex_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH1734.1",
-                    "description": "Error Characteristics of Rainfall Measurements by Collocated Joss\u2013Waldvogel Disdrometers",
                     "@type": "dcat:Distribution",
+                    "description": "Error Characteristics of Rainfall Measurements by Collocated Joss\u2013Waldvogel Disdrometers",
+                    "downloadURL": "https://doi.org/10.1175/JTECH1734.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/lpvex",
-                    "description": "LPVEx Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "LPVEx Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/lpvex",
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
+            "identifier": "C1979606207-GHRC_DAAC",
+            "issued": "2019-12-11",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/JOSSWALDVOGEL/DATA101",
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
             "spatial": "25.072 60.475 25.092 60.495",
+            "temporal": "2010-09-10T00:00:00Z/2010-11-09T07:56:00Z",
             "theme": [
                 "LPVEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Joss-Waldvogel Disdrometer (JW) LPVEx V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-09-15",
-            "temporal": "2021-09-15T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "iss",
-                "topo",
-                "trajectory",
-                "station",
-                "international",
-                "ephemeris",
-                "coordinates",
-                "location",
-                "space",
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
-            "identifier": "nasa-iss-data_2021-09-15_n3up-4f97",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-09-15",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1116810,54 +1116786,54 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-09-15_n3up-4f97",
+            "issued": "2021-09-15",
+            "keyword": [
+                "iss",
+                "topo",
+                "trajectory",
+                "station",
+                "international",
+                "ephemeris",
+                "coordinates",
+                "location",
+                "space",
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
+            "temporal": "2021-09-15T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-09-15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652224-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Flynn, Lawrence E., et al.. 2004-06-01. SBUV2N16O3. Version 008. SBUV2/NOAA-16 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SBUV2N16O3_008.html. Digital Science Data.",
-            "issued": "2000-10-03",
-            "temporal": "2000-10-03T00:00:00Z/2003-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-12-31",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "aerosols",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LARRY FLYNN, PH. D",
                 "hasEmail": "mailto:Lawrence.E.Flynn@noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1273652224-GES_DISC",
-            "description": "The version 8 SBUV/2 NOAA-16 ozone data were first released at the 2004 Quadrennial Ozone Symposium on DVD. The DVD contained all of the SBUV/2 data from NOAA-9, NOAA-11 and NOAA-16 satellites as well as SBUV data from the Nimbus-7 satellite. The DVD is no longer available, however all the data are available on-line from the NASA GES DISC. The NOAA-16 SBUV/2 v8 data are available from 2000-10-03 to 2003-12-31. The instrument spatial resolution is 180 km x 180 km footprint at nadir. The ozone profiles are made at 21 pressure levels between 1000 and 0.1 hPa. Each data file contains a days worth of ozone measurements, and is written in an ASCII text format.\n\nThe SBUV/2 is a scanning double monochromator and a cloud cover radiometer (CCR) designed to measure ultraviolet (UV) spectral intensities. In its primary mode of operation, the monochromator measures solar radiation backscattered by the atmosphere in 12 discrete wavelength bands in the near-UV, ranging from 252.0 to 339.8 nanometers, each with a bandpass of 1.1 nm. The total-ozone algorithm uses the four longest wavelength bands (312.5, 317.5, 331.2 and 339.8 nm), whereas the profiling algorithm uses the shorter wavelengths. The cloud cover radiometer operates at 379 nm (i.e., outside the ozone absorption band) with a 3.0 nm bandpass and was designed to measure the reflectivity of the surface in the IFOV. The SBUV/2 also makes periodic measurements of the solar flux by deploying a diffuser plate into the FOV to reflect sunlight into the measurement.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SBUV2N16O3",
             "creator": "Flynn, Lawrence E., et al.",
-            "title": "SBUV2/NOAA-16 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008 (SBUV2N16O3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N16O3_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The version 8 SBUV/2 NOAA-16 ozone data were first released at the 2004 Quadrennial Ozone Symposium on DVD. The DVD contained all of the SBUV/2 data from NOAA-9, NOAA-11 and NOAA-16 satellites as well as SBUV data from the Nimbus-7 satellite. The DVD is no longer available, however all the data are available on-line from the NASA GES DISC. The NOAA-16 SBUV/2 v8 data are available from 2000-10-03 to 2003-12-31. The instrument spatial resolution is 180 km x 180 km footprint at nadir. The ozone profiles are made at 21 pressure levels between 1000 and 0.1 hPa. Each data file contains a days worth of ozone measurements, and is written in an ASCII text format.\n\nThe SBUV/2 is a scanning double monochromator and a cloud cover radiometer (CCR) designed to measure ultraviolet (UV) spectral intensities. In its primary mode of operation, the monochromator measures solar radiation backscattered by the atmosphere in 12 discrete wavelength bands in the near-UV, ranging from 252.0 to 339.8 nanometers, each with a bandpass of 1.1 nm. The total-ozone algorithm uses the four longest wavelength bands (312.5, 317.5, 331.2 and 339.8 nm), whereas the profiling algorithm uses the shorter wavelengths. The cloud cover radiometer operates at 379 nm (i.e., outside the ozone absorption band) with a 3.0 nm bandpass and was designed to measure the reflectivity of the surface in the IFOV. The SBUV/2 also makes periodic measurements of the solar flux by deploying a diffuser plate into the FOV to reflect sunlight into the measurement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1116866,587 +1116842,625 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N16O3_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N16O3_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/NOAA_SBUV2_Level2/SBUV2N16O3.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/NOAA_SBUV2_Level2/SBUV2N16O3.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SBUV2N16O3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SBUV2N16O3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/smcd/spb/ozone/",
-                    "description": "NOAA NESDIS SBUV/2 web site",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA NESDIS SBUV/2 web site",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/smcd/spb/ozone/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N16O3_008.png",
+            "identifier": "C1273652224-GES_DISC",
+            "issued": "2000-10-03",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "aerosols",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652224-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SBUV2N16O3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-10-03T00:00:00Z/2003-12-31T23:59:59.999Z",
             "theme": [
                 "POES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SBUV2/NOAA-16 Level 2 Daily Ozone Profile and Total Column from CD-ROM V008 (SBUV2N16O3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-NALT-OGDR-1.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2023-06-01. SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA. Version 2.0. SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA, Version 2.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWOT-NALT-OGDR-1.0.",
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
-            "identifier": "C2799465544-POCLOUD",
-            "description": "Same as L2_NALT_GDR using predicted values for some auxiliary data, and does not have GIM ionosphere model values. Uses the onboard DORIS orbit ephemeris. Available with latency of < 7 hours. Discrete measurements at nadir for each data downlink, along the ground track. Available in netCDF-4 file format.",
-            "series-name": "SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA, Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_OGDR_1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Same as L2_NALT_GDR using predicted values for some auxiliary data, and does not have GIM ionosphere model values. Uses the onboard DORIS orbit ephemeris. Available with latency of < 7 hours. Discrete measurements at nadir for each data downlink, along the ground track. Available in netCDF-4 file format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-OGDR-1.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-NALT-OGDR-1.0",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2628593693-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2628593693-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2628593693-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2628593693-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_OGDR_1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_OGDR_1.0.jpg",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_NALT_OGDR_1.0.jpg",
+            "identifier": "C2799465544-POCLOUD",
+            "issued": "2022-06-28",
+            "keyword": [
+                "oceans",
+                "ocean waves",
+                "sea surface topography",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-NALT-OGDR-1.0",
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
+            "series-name": "SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA",
             "spatial": "-180.0 -77.6 180.0 77.6",
+            "temporal": "2022-12-16T00:00:00Z/2023-11-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Nadir Altimeter Operational Geophysical Data Record with Waveforms - SSHA, Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GXN4C7MNIY4C",
             "citation": "NLDAS project. David M. Mocko, NASA/GSFC/HSL. 2022-07-01. NLDAS_MOS0125_MC. Version 2.0. NLDAS Mosaic Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V2.0. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GXN4C7MNIY4C. https://disc.gsfc.nasa.gov/datacollection/NLDAS_MOS0125_MC_2.0.html. Digital Science Data.",
-            "issued": "2020-06-18",
-            "temporal": "1981-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-01",
-            "references": [
-                "https://doi.org/10.1029/2011JD016048",
-                "https://doi.org/10.1029/2011JD016051",
-                "https://doi.org/10.1016/0309-1708(94)90024-8"
-            ],
-            "keyword": [
-                "precipitation",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "biosphere",
-                "earth science",
-                "land surface",
-                "snow/ice",
-                "soils",
-                "surface radiative properties",
-                "surface thermal properties",
-                "surface water",
-                "terrestrial hydrosphere",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashley Heath",
                 "hasEmail": "mailto:ashley.l.heath@nasa.gov"
             },
+            "creator": "NLDAS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1888969742-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This monthly climatology data set contains a series of land surface parameters simulated from the Mosaic land-surface model (LSM) for Phase 2 of the North American Land Data Assimilation System (NLDAS-2). The data are in 1/8th degree grid spacing. The temporal resolution is monthly, ranging from January to December. The NLDAS-2 monthly climatology data are the monthly data averaged over forty years (1981 - 2020). The file format is netCDF. The previous version of this dataset (NLDAS_MC 002) was a 30-year average and was stored in GRIB file format.\n\nA brief description about the NLDAS-2 hourly and monthly Mosaic LSM data can be found from the NLDAS_MOS0125_H_2.0 and NLDAS_MOS0125_M_2.0 landing pages.\n\nDetails about the NLDAS-2 configuration of the Mosaic LSM can be found in Xia et al. (2012).\n\nFor more information, please see the README Document.",
-            "editor": "David M. Mocko, NASA/GSFC/HSL",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "NLDAS_MOS0125_MC",
-            "creator": "NLDAS project",
-            "graphic-preview-description": "NLDAS-2 Mosaic 0.125-degree Monthly Climatology Soil moisture content 0-100 cm [kg m-2] January (1981 - 2020).",
-            "title": "NLDAS Mosaic Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V2.0 (NLDAS_MOS0125_MC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_MOS0125_MC_2.0.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGXN4C7MNIY4C",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGXN4C7MNIY4C",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_MOS0125_MC_2.0.png",
-                    "description": "NLDAS-2 Mosaic 0.125-degree Monthly Climatology Soil moisture content 0-100 cm [kg m-2] January (1981 - 2020).",
                     "@type": "dcat:Distribution",
+                    "description": "NLDAS-2 Mosaic 0.125-degree Monthly Climatology Soil moisture content 0-100 cm [kg m-2] January (1981 - 2020).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_MOS0125_MC_2.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_MOS0125_MC_2.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_MOS0125_MC_2.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_MOS0125_MC.2.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_MOS0125_MC.2.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_MOS0125_MC",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_MOS0125_MC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS2_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS2_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ldas.gsfc.nasa.gov/nldas/",
-                    "description": "NLDAS Project Web Site",
                     "@type": "dcat:Distribution",
+                    "description": "NLDAS Project Web Site",
+                    "downloadURL": "https://ldas.gsfc.nasa.gov/nldas/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=hydrology",
-                    "description": "How to read and plot the data.",
                     "@type": "dcat:Distribution",
+                    "description": "How to read and plot the data.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=hydrology",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
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
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/NLDAS/NLDAS_MOS0125_MC.2.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/NLDAS/NLDAS_MOS0125_MC.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/NLDAS_aggregation/NLDAS_MOS0125_MC.2.0/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/NLDAS_aggregation/NLDAS_MOS0125_MC.2.0/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_MOS0125_MC.2.0",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_MOS0125_MC.2.0",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 }
             ],
+            "editor": "David M. Mocko, NASA/GSFC/HSL",
+            "graphic-preview-description": "NLDAS-2 Mosaic 0.125-degree Monthly Climatology Soil moisture content 0-100 cm [kg m-2] January (1981 - 2020).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_MOS0125_MC_2.0.png",
+            "identifier": "C1888969742-GES_DISC",
+            "issued": "2020-06-18",
+            "keyword": [
+                "precipitation",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "biosphere",
+                "earth science",
+                "land surface",
+                "snow/ice",
+                "soils",
+                "surface radiative properties",
+                "surface thermal properties",
+                "surface water",
+                "terrestrial hydrosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GXN4C7MNIY4C",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2011JD016048",
+                "https://doi.org/10.1029/2011JD016051",
+                "https://doi.org/10.1016/0309-1708(94)90024-8"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "NLDAS_MOS0125_MC",
             "spatial": "-125.0 25.0 -67.0 53.0",
+            "temporal": "1981-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
             "theme": [
                 "NLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NLDAS Mosaic Land Surface Model L4 Monthly Climatology 0.125 x 0.125 degree V2.0 (NLDAS_MOS0125_MC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67P-M29-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67p-m29-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67P-M29-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67p-m29-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP029 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP029 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-MRI-2-EPOXI-CALIBRATIONS-V1.0",
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
-                "epoxi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains raw calibration images acquired by the Deep Impact Medium Resolution Visible CCD from 04 October 2007 through 09 January 2008 for the EPOXI mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-mri-2-epoxi-calibrations-v1.0_n43t-7vrp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calibration",
+                "epoxi"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-MRI-2-EPOXI-CALIBRATIONS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-mri-2-epoxi-calibrations-v1.0_n43t-7vrp",
-            "description": "This data set contains raw calibration images acquired by the Deep Impact Medium Resolution Visible CCD from 04 October 2007 through 09 January 2008 for the EPOXI mission.",
-            "title": "EPOXI INFLIGHT CALIBRATIONS - MRI RAW IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI INFLIGHT CALIBRATIONS - MRI RAW IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67P-M34-STRLIGHT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-02T06:40:00.000 to 2016-09-26T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67p-m34-strlight-v1.0_n43z-ismw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT3-67P-M34-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext3-67p-m34-strlight-v1.0_n43z-ismw",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-09-02T06:40:00.000 to 2016-09-26T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP034 RDR-STRLIGHT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT3-MTP034 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2051",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sun, X., P.T. Kolbeck, J.B. Abshire, S.R. Kawa, and J. Mao. 2022. ABoVE/ASCENDS: Atmospheric Backscattering Coefficient Profiles from CO2 Sounder, 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2051",
-            "issued": "2024-05-08",
-            "temporal": "2017-07-20T16:58:23Z/2017-08-08T20:36:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "lidar"
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
-            "identifier": "C2264344759-ORNL_CLOUD",
             "description": "This dataset provides atmospheric backscattering coefficient profiles collected during Active Sensing of CO2 Emissions over Nights, Days, and Seasons (ASCENDS) deployments from 2017-07-20 to 2017-08-08 over Alaska, U.S., and the Yukon and Northwest Territories of Canada. These profiles were measured by the CO2 Sounder Lidar instrument carried on a DC-8 aircraft. The airborne CO2 Sounder is a pulsed, multi-wavelength Integrated Path Differential Absorption lidar that estimates column-averaged dry-air CO2 mixing ratio (XCO2) in the nadir path from the aircraft to the scattering surface. In addition to XCO2, the lidar receiver recorded the time-resolved atmospheric backscatter signal strength as the laser pulses propagated through the atmosphere. Raw lidar data were converted to the atmospheric backscatter cross-section product and the two-way atmosphere transmission, also known as attenuated backscatter profiles. These ASCENDS flights were coordinated with the 2017 Arctic-Boreal Vulnerability Experiment (ABoVE) campaign and are provided in ICARTT format.",
-            "graphic-preview-description": "A map showing the ground tracks for the airborne campaign, with a table summarizing each flight. The colors in the table match those shown in the ground tracks.",
-            "title": "ABoVE/ASCENDS: Atmospheric Backscattering Coefficient Profiles from CO2 Sounder, 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_Backscatter_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2051",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2051",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/ABoVE_ASCENDS_Backscatter/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/ABoVE_ASCENDS_Backscatter/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_Backscatter.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_Backscatter.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2051",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2051",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_ASCENDS_Backscatter/comp/ABoVE_ASCENDS_Backscatter-SoftwareCodes.zip",
-                    "description": "ABoVE/ASCENDS: Atmospheric Backscattering Coefficient Profiles from CO2 Sounder, 2017: ABoVE_ASCENDS_Backscatter-SoftwareCodes.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE/ASCENDS: Atmospheric Backscattering Coefficient Profiles from CO2 Sounder, 2017: ABoVE_ASCENDS_Backscatter-SoftwareCodes.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_ASCENDS_Backscatter/comp/ABoVE_ASCENDS_Backscatter-SoftwareCodes.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_ASCENDS_Backscatter/comp/ABoVE_ASCENDS_Backscatter.pdf",
-                    "description": "ABoVE/ASCENDS: Atmospheric Backscattering Coefficient Profiles from CO2 Sounder, 2017: ABoVE_ASCENDS_Backscatter.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE/ASCENDS: Atmospheric Backscattering Coefficient Profiles from CO2 Sounder, 2017: ABoVE_ASCENDS_Backscatter.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_ASCENDS_Backscatter/comp/ABoVE_ASCENDS_Backscatter.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_Backscatter_Fig1.jpg",
-                    "description": "A map showing the ground tracks for the airborne campaign, with a table summarizing each flight. The colors in the table match those shown in the ground tracks.",
                     "@type": "dcat:Distribution",
+                    "description": "A map showing the ground tracks for the airborne campaign, with a table summarizing each flight. The colors in the table match those shown in the ground tracks.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_Backscatter_Fig1.jpg",
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
+            "graphic-preview-description": "A map showing the ground tracks for the airborne campaign, with a table summarizing each flight. The colors in the table match those shown in the ground tracks.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_Backscatter_Fig1.jpg",
+            "identifier": "C2264344759-ORNL_CLOUD",
+            "issued": "2024-05-08",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "lidar"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2051",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-165.68 34.59 -98.15 71.27",
+            "temporal": "2017-07-20T16:58:23Z/2017-08-08T20:36:00Z",
             "theme": [
                 "ABoVE",
                 "ASCENDS Airborne",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE/ASCENDS: Atmospheric Backscattering Coefficient Profiles from CO2 Sounder, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-ESC1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the 67P/Churyumov-Gerasimenko comet escort 1 mission phase, which took place between 2014-11-19 and 2015-03-10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-esc1-v1.0_n46y-rpkr",
             "issued": "2018-06-26",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-ESC1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-esc1-v1.0_n46y-rpkr",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the 67P/Churyumov-Gerasimenko comet escort 1 mission phase, which took place between 2014-11-19 and 2015-03-10.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 ESC1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 ESC1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/n47v-4ngw",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "This experiment compared the spaceflight transcriptomes of four commonly used natural variants (ecotypes) of Arabidopsis thaliana using RNAseq. In nature Arabidopsis is a native of Europe/Asia/Northwestern Africa and is found across the globe growing in a wide range of environments. The geographical spread of these various populations has led to a slow divergence leading to distinct ecotypes. Understanding the impact of this ecotypic variability is an important factor when using Arabidopsis as a model. Seeds of the ecotypes Col_0 Ler-2 Ws-2 and Cvi-0 were flown to the International Space Station as part of CRS-4 mission in the Biological Research in Canister (BRIC) hardware. The seeds were germinated on orbit grown for 8 days and then fixed in RNAlater and frozen in the MELFI freezer for return to Earth. Once returned RNA was isolated and RNAseq performed to catalog the transcriptional patterns of the plants grown in space. An identical set of samples were grown in parallel on the ground to provide controls to allow assessment of transcriptional changes specifically associated with the spaceflight environment. This data release includes 48 out of 56 sample expression files with the remaining 8 files to be released at a later date.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-37",
+                    "mediaType": "text/html",
+                    "title": "Comparison of the spaceflight transcriptome of four commonly used Arabidopsis thaliana ecotypes"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-37_n47v-4ngw",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "nucleic acid extraction",
                 "spaceflight",
@@ -1117456,430 +1117470,418 @@
                 "library construction",
                 "ecotype"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/n47v-4ngw",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-37_n47v-4ngw",
-            "description": "This experiment compared the spaceflight transcriptomes of four commonly used natural variants (ecotypes) of Arabidopsis thaliana using RNAseq. In nature Arabidopsis is a native of Europe/Asia/Northwestern Africa and is found across the globe growing in a wide range of environments. The geographical spread of these various populations has led to a slow divergence leading to distinct ecotypes. Understanding the impact of this ecotypic variability is an important factor when using Arabidopsis as a model. Seeds of the ecotypes Col_0 Ler-2 Ws-2 and Cvi-0 were flown to the International Space Station as part of CRS-4 mission in the Biological Research in Canister (BRIC) hardware. The seeds were germinated on orbit grown for 8 days and then fixed in RNAlater and frozen in the MELFI freezer for return to Earth. Once returned RNA was isolated and RNAseq performed to catalog the transcriptional patterns of the plants grown in space. An identical set of samples were grown in parallel on the ground to provide controls to allow assessment of transcriptional changes specifically associated with the spaceflight environment. This data release includes 48 out of 56 sample expression files with the remaining 8 files to be released at a later date.",
-            "title": "Comparison of the spaceflight transcriptome of four commonly used Arabidopsis thaliana ecotypes",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-37",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Comparison of the spaceflight transcriptome of four commonly used Arabidopsis thaliana ecotypes"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Comparison of the spaceflight transcriptome of four commonly used Arabidopsis thaliana ecotypes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-3-CR5-CHECKOUT-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 5 mission phase, covering the period  from 2009-12-14T00:00:00.000 to 2010-05-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-3-cr5-checkout-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "4 vesta",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSINAC-3-CR5-CHECKOUT-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osinac-3-cr5-checkout-v2.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the CRUISE 5 mission phase, covering the period  from 2009-12-14T00:00:00.000 to 2010-05-16T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 3 CR5 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSINAC 3 CR5 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR4-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 10 and June 12, 2007 during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr4-v1.0_n495-p6gt",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR4-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr4-v1.0_n495-p6gt",
-            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR4) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 10 and June 12, 2007 during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR4 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SAGR4 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-P-I0962%2FI0964-5-BENECCHIOCC-V1.0",
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
-                "pluto",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The dataset include simultaneous imaging obtained at the MMT in the infrared (H-band, 1.65 micron) and visible (unfiltered, approximately 0.24-1.24 micron) of Pluto occulting the star P445.3 (2UCAC 25823784) on 2007 March 18. The measurements included in the dataset were obtained continuously from 10:10:00 to 11:30:00 UTC. The midpoint of the occultation, at the MMT, was 10:53:49+/-00:01. The event was grazing and gives information about the atmosphere of Pluto to a depth of 1348 km above the surface. Images from the other observing sites for this event are not contained within this dataset, however lightcurve tables are included.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-p-i0962-i0964-5-benecchiocc-v1.0_n4ac-sum9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pluto",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-P-I0962%2FI0964-5-BENECCHIOCC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-p-i0962-i0964-5-benecchiocc-v1.0_n4ac-sum9",
-            "description": "The dataset include simultaneous imaging obtained at the MMT in the infrared (H-band, 1.65 micron) and visible (unfiltered, approximately 0.24-1.24 micron) of Pluto occulting the star P445.3 (2UCAC 25823784) on 2007 March 18. The measurements included in the dataset were obtained continuously from 10:10:00 to 11:30:00 UTC. The midpoint of the occultation, at the MMT, was 10:53:49+/-00:01. The event was grazing and gives information about the atmosphere of Pluto to a depth of 1348 km above the surface. Images from the other observing sites for this event are not contained within this dataset, however lightcurve tables are included.",
-            "title": "P445.3 (PLUTO) OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P445.3 (PLUTO) OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP03NM_L3.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-03-03. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MOPITT/MOP03NM_L3.008. https://asdc.larc.nasa.gov/project/MOPITT.",
-            "issued": "2018-10-26",
-            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "air quality",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmosphere"
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
-            "identifier": "C1575974130-LARC",
             "description": "MOP03NM_8 is the Measurements Of Pollution In The Troposphere (MOPITT) Carbon Monoxide (CO) gridded monthly means (Near Infrared Radiances) version 8 data product. It contains monthly mean gridded versions of the daily Level 2 CO profile and total column retrievals. For this data product, the averaging kernels associated with each retrieval are also gridded and included in the Level 3 files.For a description of the file contents, refer to the File Spec Document. The MOPITT Level 2 Data Quality Statement contains additional information about the quality and the limitations of the retrievals. MOPITT was successfully launched into sun-synchronous polar orbit aboard Terra, NASA's first Earth Observing System spacecraft, on December 18, 1999. The MOPITT instrument was constructed by a consortium of Canadian companies and funded by the Space Science Division of the Canadian Space Agency. Data collection for this product was completed in March of 2020.",
-            "graphic-preview-description": "NASA Worldview",
-            "title": "MOPITT CO gridded monthly means (Near Infrared Radiances) V008",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP03NM_L3.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMOPITT%2FMOP03NM_L3.008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575974130-LARC",
-                    "description": "Earthdata Search for MOP03NM_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MOP03NM_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1575974130-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MOPITT/MOP03NM.008/contents.html",
-                    "description": "OPeNDAP data access for MOP03NM_8",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MOP03NM_8",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MOPITT/MOP03NM.008/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf",
-                    "description": "MOPITT Version 8 Product User's Guide - December 2018",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Version 8 Product User's Guide - December 2018",
+                    "downloadURL": "https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/48",
-                    "description": "NASA EOS ATB Documents: MOPITT",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MOPITT",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/48",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www2.acom.ucar.edu/mopitt/publications",
-                    "description": "U.S. MOPITT Project home page list of publications",
                     "@type": "dcat:Distribution",
+                    "description": "U.S. MOPITT Project home page list of publications",
+                    "downloadURL": "https://www2.acom.ucar.edu/mopitt/publications",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP03NM_L3.008",
-                    "description": "DOI data set landing page for MOP03NM_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MOP03NM_8",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MOPITT/MOP03NM_L3.008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://subset.larc.nasa.gov/mopitt/",
-                    "description": "MOPITT Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "MOPITT Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/mopitt/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MOPITT/MOP03NM.008/",
-                    "description": "ASDC Direct Data Download for MOP03NM_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MOP03NM_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MOPITT/MOP03NM.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
-                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
                     "@type": "dcat:Distribution",
+                    "description": "Proceedings of the National Academy of Sciences (PNAS) Article: Unexpected slowdown of US pollutant emission reduction in the past decade\u00a0(Ground and satellite observations show that air pollution regulations in the United States (US) have resulted in substantial reductions in emissions and corresponding improvements in air quality over the last several decades)",
+                    "downloadURL": "https://www.pnas.org/content/115/20/5099",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/quality_summaries/MOPV8_L3_DQ_statement.pdf",
-                    "description": "Quality Summary: MOPITT Level 3, Version 8 (V8; L3V5.6.x), first released December, 2018",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: MOPITT Level 3, Version 8 (V8; L3V5.6.x), first released December, 2018",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/mopitt/quality_summaries/MOPV8_L3_DQ_statement.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
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
                 }
             ],
+            "graphic-preview-description": "NASA Worldview",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/",
+            "identifier": "C1575974130-LARC",
+            "issued": "2018-10-26",
+            "keyword": [
+                "air quality",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MOPITT/MOP03NM_L3.008",
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
+            "temporal": "2000-03-03T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MOPITT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MOPITT CO gridded monthly means (Near Infrared Radiances) V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-2-EDR-RAW-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set provides raw energetic (MeV) particle data measured by the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. This data set contains both real-time and recorded data for all Jupiter orbits.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-2-edr-raw-v1.0_n4gt-d76b",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "europa",
                 "callisto",
@@ -1117890,210 +1117892,187 @@
                 "io",
                 "ganymede"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-2-EDR-RAW-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-2-edr-raw-v1.0_n4gt-d76b",
-            "description": "This data set provides raw energetic (MeV) particle data measured by the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. This data set contains both real-time and recorded data for all Jupiter orbits.",
-            "title": "GO JUP HIC HIGHRES RAW DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GO JUP HIC HIGHRES RAW DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/674/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-03-20",
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
-            "identifier": "DASHLINK_674",
             "description": "This chapter described at a very high level some of the considerations that need to be made when designing algorithms for a vehicle health management application. The choices made here affect the quality of the diagnosis and prognosis (covered in Chapter 7). Therefore, the algorithmic design choices are made in conjunction with the design choices for diagnostics and prognostics to optimally support these tasks. Furthermore, additional considerations imposed by computational constraints, resource availability, algorithm maintenance, need for algorithm re-tuning, etc. will impact the solutions.\r\nIt should also be noted that technological advances, both in hardware and software, impose the need for new solutions. For example, as new materials and new sensors are being developed, the algorithmic solutions will need to follow suit.\r\nIn general, there seems to be a trend to have more sensor data available. While this is potentially a good thing, sensor data provides value only when it is being processed and interpreted properly, in part by the techniques described here. Testing of the methods, however, requires the \u201cright\u201d kind of data. Generally, there is a lack of seeded fault data which are required to train and validate algorithms. It is also important to migrate information from the component to the subsystem to the system levels so that health management technologies can be applied effectively and efficiently at the vehicle level. It may be required to perform elements described in this chapter between different levels of the vehicle architecture.",
-            "title": "Basic Principles - Chapter 6",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Pre_R-405_Chapter_6.pdf",
-                    "description": "Pre_R-405_Chapter_6.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Pre_R-405_Chapter_6.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Pre_R-405_Chapter_6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Pre_R-405_Chapter_6.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_674",
+            "issued": "2013-03-20",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/674/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Basic Principles - Chapter 6"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1147-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-01T00:25:46.000 to 2015-11-01T05:00:34.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1147-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1147-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1147-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-01T00:25:46.000 to 2015-11-01T05:00:34.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1147 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1147 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0294-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-14T17:13:03.000 to 2014-09-14T23:35:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0294-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0294-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0294-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-14T17:13:03.000 to 2014-09-14T23:35:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0294 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0294 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0605-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-26T08:15:20.000 to 2015-02-26T10:24:31.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0605-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0605-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0605-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-26T08:15:20.000 to 2015-02-26T10:24:31.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0605 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0605 V1.0"
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
-            "identifier": "NASA-862__9",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1118101,105 +1118080,140 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__9",
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
-            "landingPage": "https://doi.org/10.5067/CSPBASWAQJ0Z",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus Temperature-Humidity Infrared Radiometer Global Montage Grayscale L1, TIFF V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CSPBASWAQJ0Z.",
-            "issued": "1978-10-30",
-            "temporal": "1978-10-30T00:00:00Z/1984-05-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1984-05-18",
-            "keyword": [
-                "atmospheric water vapor",
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C1703454246-NSIDC_ECS",
             "description": "This data set consists of daily, global grayscale TIFF images measured in the 6.7 \u00b5m window (6.5 \u00b5m - 7.0 \u00b5m) and the 11.5 \u00b5m window (10.5 \u00b5m - 12.5 \u00b5m) by the Temperature-Humidity Infrared Radiometer (THIR) on board the Nimbus 7 satellite. Each data granule is a daytime or nighttime global composite of all the swaths in a day. Note: This data set is not georeferenced and there are some gaps in the temporal coverage because of missing data.",
-            "title": "Nimbus Temperature-Humidity Infrared Radiometer Global Montage Grayscale L1, TIFF V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCSPBASWAQJ0Z",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCSPBASWAQJ0Z",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIRmtg-1T.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmTHIRmtg-1T.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703454246-NSIDC_ECS&q=NmTHIRmtg-1T+&m=-59.43570100523044%21-4.1220703125%211%211%210%210%2C2&tl=1568750791%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1703454246-NSIDC_ECS&q=NmTHIRmtg-1T+&m=-59.43570100523044%21-4.1220703125%211%211%210%210%2C2&tl=1568750791%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIRmtg-1T/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmTHIRmtg-1T/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CSPBASWAQJ0Z",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CSPBASWAQJ0Z",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CSPBASWAQJ0Z",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CSPBASWAQJ0Z",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1703454246-NSIDC_ECS",
+            "issued": "1978-10-30",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CSPBASWAQJ0Z",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1984-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-10-30T00:00:00Z/1984-05-18T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus Temperature-Humidity Infrared Radiometer Global Montage Grayscale L1, TIFF V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/n4rm-hn8p",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Draft Genome sequences of Rhodotorula mucilaginosa isolated from the International space station.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-293",
+                    "mediaType": "text/html",
+                    "title": "Draft Genome sequences of Rhodotorula mucilaginosa isolated from the International space station"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-293_n4rm-hn8p",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "strain",
                 "spaceflight",
@@ -1118209,1118 +1118223,1076 @@
                 "nucleic acid extraction",
                 "nucleic acid sequencing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/n4rm-hn8p",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-293_n4rm-hn8p",
-            "description": "Draft Genome sequences of Rhodotorula mucilaginosa isolated from the International space station.",
-            "title": "Draft Genome sequences of Rhodotorula mucilaginosa isolated from the International space station",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-293",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Draft Genome sequences of Rhodotorula mucilaginosa isolated from the International space station"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Draft Genome sequences of Rhodotorula mucilaginosa isolated from the International space station"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-EARTH-V1.0",
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
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-earth-v1.0_n4t5-tbsv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-MAG-3-RDR-EARTH-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-mag-3-rdr-earth-v1.0_n4t5-tbsv",
-            "description": "NEAR MAG RDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR MAG DATA FOR EARTH",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR MAG DATA FOR EARTH"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA1001",
             "citation": "Jarnot, R. and Perun, V.. 2015-02-19. ML1OA. Version 004. MLS/Aura L1 Orbit/Attitude and Tangent Point Geolocation Data V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA1001. https://disc.gsfc.nasa.gov/datacollection/ML1OA_004.html. Digital Science Data.",
-            "issued": "2014-10-21",
-            "temporal": "2004-08-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-10-21",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "platform characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATHANIEL LIVESEY",
                 "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
             },
+            "creator": "Jarnot, R. and Perun, V.",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1265737437-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "ML1OA is the EOS Aura Microwave Limb Sounder (MLS) product containing the level 1 orbit attitude and tangent point geolocation data. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), and files contain a full days worth of data (15 orbits). Users of the ML1OA data product should read the 'A Short Guide to the Use and Interpretation of v4.2x Level 1 Data' document for additional information.\n\nThe data are stored in the version 5 Hierarchical Data Format, or HDF-5. Each file contains orbital and attitude information written as HDF-5 dataset objects (n-dimensional arrays), along with file attributes and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML1OA",
-            "creator": "Jarnot, R. and Perun, V.",
-            "title": "MLS/Aura L1 Orbit/Attitude and Tangent Point Geolocation Data V004 (ML1OA) at GES DISC",
-            "graphic-preview-description": "Aura MLS logo",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1OA_004.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA1001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA1001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1OA_004.jpeg",
-                    "description": "Aura MLS logo",
                     "@type": "dcat:Distribution",
+                    "description": "Aura MLS logo",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1OA_004.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML1OA_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML1OA_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level1/ML1OA.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level1/ML1OA.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML1OA_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML1OA_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML1OA_004.jpeg",
+            "identifier": "C1265737437-GES_DISC",
+            "issued": "2014-10-21",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "platform characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA1001",
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
+            "series-name": "ML1OA",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura L1 Orbit/Attitude and Tangent Point Geolocation Data V004 (ML1OA) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-3-EDR-EROS%2FORBIT-V1.0",
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
+            "description": "The GRS Level 2 data products in this archive include daily time series of spectra collected by the instrument along with selected spacecraft engineering and instrument configuration and orbital ephemerides. Supporting documentation includes as to the specifics of how these data were generated. Selected ephemerides and engineering parameters are averaged for the composite set of information.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-3-edr-eros-orbit-v1.0_n4u4-hf84",
+            "issued": "2018-06-26",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-GRS-3-EDR-EROS%2FORBIT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-grs-3-edr-eros-orbit-v1.0_n4u4-hf84",
-            "description": "The GRS Level 2 data products in this archive include daily time series of spectra collected by the instrument along with selected spacecraft engineering and instrument configuration and orbital ephemerides. Supporting documentation includes as to the specifics of how these data were generated. Selected ephemerides and engineering parameters are averaged for the composite set of information.",
-            "title": "NEAR GRS SPECTRA FOR EROS/ORBIT",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR GRS SPECTRA FOR EROS/ORBIT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/BIO-GO-SHIP/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/BIO-GO-SHIP/DATA001.",
-            "issued": "2022-05-01",
-            "temporal": "2016-01-01T00:00:01Z/2024-06-10T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-12",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "ocean temperature",
-                "ocean chemistry",
-                "earth science",
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
-            "identifier": "C3065483572-OB_DAAC",
             "description": "Bio-GO-SHIP aims to become an international collaboration to measure, understand, and predict the distribution and biogeochemical role of pelagic plankton communities. The project leverages the global-reaching [GO-SHIP](https://www.go-ship.org/) platform and its complementary hydrographic measurements. The mission of Bio-GO-SHIP is to quantify the molecular diversity, size spectrum, chemical composition, and abundances of plankton communities across large spatial, vertical, and eventually temporal scales. This will be achieved through systematic, high-quality, and calibrated sampling of omics, plankton imaging, particle chemistry, and optical techniques as operational oceanographic tools. Integration with regular GO-SHIP measurements and their analyses of the physical and chemical environment will allow us to understand (and eventually predict) how plankton communities respondto ocean changes and how biological processes feeds backon carbon, oxygen and nutrient cycles.",
-            "title": "Biological Global Ocean Ship-based Hydrographic Investigations Program (Bio-GO-SHIP)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBIO-GO-SHIP%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBIO-GO-SHIP%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BIO-GO-SHIP/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BIO-GO-SHIP/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C3065483572-OB_DAAC",
+            "issued": "2022-05-01",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean temperature",
+                "ocean chemistry",
+                "earth science",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/BIO-GO-SHIP/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-01-01T00:00:01Z/2024-06-10T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Biological Global Ocean Ship-based Hydrographic Investigations Program (Bio-GO-SHIP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4N29TWJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Intergovernmental Panel on Climate Change - IPCC. 2000-07-31. IPCC Special Report on Emissions Scenarios (SRES) Emissions Scenarios Dataset Version 1.1. Version 1.01. New York, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Cambridge University Press. https://doi.org/10.7927/H4N29TWJ. https://doi.org/10.7927/H4N29TWJ.",
-            "issued": "2000-07-31",
-            "temporal": "1990-01-01T00:00:00Z/2100-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-07-31",
-            "references": [
-                "https://doi.org/10.7927/H4RV0KMH",
-                "https://doi.org/10.7927/H4HD7SKJ",
-                "https://doi.org/10.7927/H41C1TT4",
-                "https://doi.org/10.7927/H4WM1BB7",
-                "https://doi.org/10.7927/H4XG9P2R",
-                "https://doi.org/10.7927/H4542KJV",
-                "https://doi.org/10.7927/H4FT8J0X"
-            ],
-            "keyword": [
-                "atmosphere",
-                "air quality",
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
-            "identifier": "C179001932-SEDAC",
-            "description": "The Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) Emissions Scenarios Dataset Version 1.1 consists of 40 global and regional greenhouse gases (GHGs) and sulfur emissions scenarios projected every 10 years beginning in 1990 through 2100. The scenarios are based on extensive assessment of driving forces and emissions in the scenario literature, alternative modeling approaches, and an open process that solicited wide participation and feedback. The scenarios provide the basis for future assessments of climate change and possible response strategies. This data set is produced by the IPCC and is distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "New York, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Intergovernmental Panel on Climate Change - IPCC",
-            "title": "IPCC Special Report on Emissions Scenarios (SRES) Emissions Scenarios Dataset Version 1.1",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-emissions-v1-1/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Intergovernmental Panel on Climate Change (IPCC) Special Report on Emissions Scenarios (SRES) Emissions Scenarios Dataset Version 1.1 consists of 40 global and regional greenhouse gases (GHGs) and sulfur emissions scenarios projected every 10 years beginning in 1990 through 2100. The scenarios are based on extensive assessment of driving forces and emissions in the scenario literature, alternative modeling approaches, and an open process that solicited wide participation and feedback. The scenarios provide the basis for future assessments of climate change and possible response strategies. This data set is produced by the IPCC and is distributed by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4N29TWJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4N29TWJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-emissions-v1-1/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-emissions-v1-1/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-emissions-v1-1/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-emissions-v1-1/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-emissions-v1-1",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ipcc-emissions-v1-1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/ipcc/ipcc-emissions-v1-1/sedac-logo.jpg",
+            "identifier": "C179001932-SEDAC",
+            "issued": "2000-07-31",
+            "keyword": [
+                "atmosphere",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4N29TWJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2000-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4RV0KMH",
+                "https://doi.org/10.7927/H4HD7SKJ",
+                "https://doi.org/10.7927/H41C1TT4",
+                "https://doi.org/10.7927/H4WM1BB7",
+                "https://doi.org/10.7927/H4XG9P2R",
+                "https://doi.org/10.7927/H4542KJV",
+                "https://doi.org/10.7927/H4FT8J0X"
+            ],
+            "release-place": "New York, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1990-01-01T00:00:00Z/2100-12-31T00:00:00Z",
             "theme": [
                 "IPCC",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IPCC Special Report on Emissions Scenarios (SRES) Emissions Scenarios Dataset Version 1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-HIRISE-2-EDR-V1.0",
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
-                "mars reconnaissance orbiter",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes the Experimental Data Records from the HiRISE instrument on MRO. These products are the permanent record of the raw images obtained by the HiRISE Instrument and contain the properties of unprocessed and unrectified imaging maintaining the original spacecraft viewing orientation and optical distortion properties. .",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-hirise-2-edr-v1.0_n4uz-sp62",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars reconnaissance orbiter",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-HIRISE-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-hirise-2-edr-v1.0_n4uz-sp62",
-            "description": "This data set includes the Experimental Data Records from the HiRISE instrument on MRO. These products are the permanent record of the raw images obtained by the HiRISE Instrument and contain the properties of unprocessed and unrectified imaging maintaining the original spacecraft viewing orientation and optical distortion properties. .",
-            "title": "MRO MARS HIGH RESOLUTION IMAGE SCIENCE EXPERIMENT EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MRO MARS HIGH RESOLUTION IMAGE SCIENCE EXPERIMENT EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSMGEXP_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, Global Navigation Satellite System (GNSS) IGS Multi-GNSS Experiment (MGEX) Products from NASA CDDIS, Greenbelt, MD, USA: NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:110.5067/GNSS/GNSS_IGSMGEXP_001",
-            "issued": "2012-06-01",
-            "temporal": "2009-02-01T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-09",
-            "keyword": [
-                "tectonics",
-                "solid earth",
-                "earth science",
-                "geodetics",
-                "gravity/gravitational field"
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
-            "identifier": "C1708969932-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System satellite orbit products (daily files, generated daily) from the real-time IGS analysis center submissions available from NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. These products include satellite orbit, satellite and station clock, and station position solutions. They are generated multi-GNSS data in support of the IGS Multi-GNSS Experiment (MGEX). The observation data from a global permanent network of ground-based receivers are transmitted from the CDDIS and downloaded by analysis centers who generate these MGEX products. More information about the MGEX products is available at: https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/gnss_mgex.html.",
-            "title": "Global Navigation Satellite System (GNSS) IGS Multi-GNSS Products from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSMGEXP_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSMGEXP_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/products/mgex",
-                    "description": "URL for retrieval of GNSS MGEX derived products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS MGEX derived products through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/products/mgex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/gnss_mgex.html",
-                    "description": "URL for more information about GNSS MGEX derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS MGEX derived products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/gnss_mgex.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_IGSMGEXP_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_IGSMGEXP_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1708969932-CDDIS",
+            "issued": "2012-06-01",
+            "keyword": [
+                "tectonics",
+                "solid earth",
+                "earth science",
+                "geodetics",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSMGEXP_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2009-02-01T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) IGS Multi-GNSS Products from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3288-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-15T13:09:18.000 to 2012-05-15T15:33:18.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3288-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3288-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3288-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-15T13:09:18.000 to 2012-05-15T15:33:18.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3288 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3288 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-LEFS60-V1.0",
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
-                "ulysses",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set consists of HISCALE Low-Energy Foil Spectrometer (LEFS) electron and ion counts at 60 degrees from the spacecraft spin axis. These measurements were taken during the Ulysses Jupiter encounter 1991-12-31 to 1992-02-16, and include 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-lefs60-v1.0_n4zf-4dxf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "ulysses",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-HISCALE-4-SUMM-LEFS60-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-hiscale-4-summ-lefs60-v1.0_n4zf-4dxf",
-            "description": "This data set consists of HISCALE Low-Energy Foil Spectrometer (LEFS) electron and ion counts at 60 degrees from the spacecraft spin axis. These measurements were taken during the Ulysses Jupiter encounter 1991-12-31 to 1992-02-16, and include 1 hour averaged inbound cruise data (1991-12-31 to 1992-02-01), and 15 minute averaged encounter data (1992-02-02 to 1992-02-16).",
-            "title": "ULYSSES JUPITER HISCALE LEFS 60\n                                        ELECTRON/ION COUNTS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULYSSES JUPITER HISCALE LEFS 60\n                                        ELECTRON/ION COUNTS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-SUMM-HGCOORDS-48.0SEC-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-summ-hgcoords-48.0sec-v1.0_n53t-sck4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-SUMM-HGCOORDS-48.0SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-summ-hgcoords-48.0sec-v1.0_n53t-sck4",
-            "description": "not applicable",
-            "title": "VG2 JUP MAG RESAMPLED HELIOGRAPHIC (RTN)COORDS 48.0SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 JUP MAG RESAMPLED HELIOGRAPHIC (RTN)COORDS 48.0SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0907-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-19T21:18:55.000 to 2015-07-20T03:29:11.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0907-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0907-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0907-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-19T21:18:55.000 to 2015-07-20T03:29:11.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0907 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0907 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1661710578-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
-            "issued": "2019-11-27",
-            "temporal": "1994-04-09T00:00:00Z/1994-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-11",
-            "keyword": [
-                "nasa"
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
-            "identifier": "C1661710578-ASF",
             "description": "Browse for STS-59 SIR-C Ground Range Product",
-            "title": "STS-59_BROWSE_GRD",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
-                    "description": "Vertex, the ASF search and download interface",
                     "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1661710578-ASF",
+            "issued": "2019-11-27",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1661710578-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>60.5933 -167.484 60.5933 173.996 -58.2098 173.996 -58.2098 -167.484 60.5933 -167.484</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1994-04-09T00:00:00Z/1994-04-22T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STS-59_BROWSE_GRD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1327-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-10T01:13:35.000 to 2016-01-10T09:25:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1327-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1327-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1327-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-10T01:13:35.000 to 2016-01-10T09:25:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1327 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1327 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NIS-5-EDR-EROS%2FORBIT-V1.0",
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
-                "eros"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Unknown",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nis-5-edr-eros-orbit-v1.0_n55m-5uxj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NIS-5-EDR-EROS%2FORBIT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nis-5-edr-eros-orbit-v1.0_n55m-5uxj",
-            "description": "Unknown",
-            "title": "NEAR NIS CALIBRATED SPECTRA FOR EROS/ORBIT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR NIS CALIBRATED SPECTRA FOR EROS/ORBIT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4SB43P8",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "World Economic Forum - WEF - Global Leaders for Tomorrow Environment Task Force, Yale Center for Environmental Law and Policy - YCELP - Yale University, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2002-12-31. 2002 Environmental Sustainability Index (ESI). Version 2002.00. New Haven, CT. Archived by National Aeronautics and Space Administration, U.S. Government, Yale Center for Environmental Law and Policy (YCELP)/Yale University. https://doi.org/10.7927/H4SB43P8. https://doi.org/10.7927/H4SB43P8.",
-            "issued": "2002-12-31",
-            "temporal": "1980-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4NK3BZJ",
-                "https://doi.org/10.7927/H4X34VDM",
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
-            "identifier": "C179001967-SEDAC",
-            "description": "The 2002 Environmental Sustainability Index (ESI) measures overall progress toward environmental sustainability for 142 countries based on  environmental systems, stresses, human vulnerability, social and institutional capacity and global stewardship. The addition of a climate change indicator, reduction in number of capacity indicators, and  an improved imputation methodology contributed to an improvement from the 2001 ESI. The index was unveiled at the World Economic Forum's annual meeting, January 2002, New York. The 2002 ESI is the result of collaboration among the World Economic Forum (WEF), Yale Center for Environmental Law and Policy (YCELP), and the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "New Haven, CT",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "World Economic Forum - WEF - Global Leaders for Tomorrow Environment Task Force, Yale Center for Environmental Law and Policy - YCELP - Yale University, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "2002 Environmental Sustainability Index (ESI)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/esi-environmental-sustainability-index-2002/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 2002 Environmental Sustainability Index (ESI) measures overall progress toward environmental sustainability for 142 countries based on  environmental systems, stresses, human vulnerability, social and institutional capacity and global stewardship. The addition of a climate change indicator, reduction in number of capacity indicators, and  an improved imputation methodology contributed to an improvement from the 2001 ESI. The index was unveiled at the World Economic Forum's annual meeting, January 2002, New York. The 2002 ESI is the result of collaboration among the World Economic Forum (WEF), Yale Center for Environmental Law and Policy (YCELP), and the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4SB43P8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4SB43P8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/esi/esi-environmental-sustainability-index-2002/2002-esi-scores-by-country-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/esi/esi-environmental-sustainability-index-2002/2002-esi-scores-by-country-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-environmental-sustainability-index-2002/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-environmental-sustainability-index-2002/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-environmental-sustainability-index-2002/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-environmental-sustainability-index-2002/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-environmental-sustainability-index-2002",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/esi-environmental-sustainability-index-2002",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/esi-environmental-sustainability-index-2002/maps",
+            "identifier": "C179001967-SEDAC",
+            "issued": "2002-12-31",
+            "keyword": [
+                "sustainability",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4SB43P8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4NK3BZJ",
+                "https://doi.org/10.7927/H4X34VDM",
+                "https://doi.org/10.7927/H40V89R6"
+            ],
+            "release-place": "New Haven, CT",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "ESI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2002 Environmental Sustainability Index (ESI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Suborbital/OWLETS-2/Pandora_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-01-27. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Suborbital/OWLETS-2/Pandora_Data_1.",
-            "issued": "2020-11-18",
-            "temporal": "2018-05-08T00:00:00Z/2019-03-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Sullivan",
                 "hasEmail": "mailto:john.t.sullivan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1997468728-LARC_ASDC",
             "description": "OWLETS2_Pandora_Data_1 is the Ozone Water-Land Environmental Transition Study (OWLETS-2) ozone and nitrogen dioxide data collected by the NASA GSFC Pandora Spectrometer Project located at various ground sites and onboard the SERC research vessel during the OWLETS-2 field campaign. OWLETS was supported by the NASA Science Innovation Fund (SIF). Data collection is complete.\r\n\r\nCoastal regions have typically posed a challenge for air quality researchers due to a lack of measurements available over water and water-land boundary transitions. Supported by NASA\u2019s Science Innovation Fund (SIF), the Ozone Water-Land Environmental Transition Study (OWLETS) field campaign examined ozone concentrations and gradients over the Chesapeake Bay from July 5, 2017 \u2013 August 3, 2017, with twelve intensive measurement days occurring during this time period. OWLETS utilized a unique combination of instrumentation, including aircraft, TOLNet ozone lidars (NASA Goddard Space Flight Center Tropospheric Ozone Differential Absorption Lidar and NASA Langley Research Center Mobile Ozone Lidar), UAV/drones, ozonesondes, AERONET sun photometers, and mobile and ship-based measurements, to characterize the land-water differences in ozone and other pollutants. Two main research sites were established as part of the campaign: an over-land site at NASA LaRC, and an over-water site at the Chesapeake Bay Bridge Tunnel. These two research sites were established to provide synchronous vertical measurements of meteorology and pollutants over water and over land. In combination with mobile observations between the two sites, pollutant gradients were able to be observed and used to better understand the fundamental processes occurring at the land-water interface. OWLETS-2 was completed from June 6, 2018 \u2013 July 6, 2018 in the upper Chesapeake Bay region. Research sites were established at the University of Maryland, Baltimore County (UMBC), Hart Miller Island (HMI), and Howard University Beltsville (HUBV), with HMI representing the over-water location and UMBC and HUBV representing the over-land sites. Similar measurements were carried out to further characterize water-land gradients in the upper Chesapeake Bay. The measurements completed during OWLETS are of importance in enhancing air quality models, and improving future satellite retrievals, particularly, NASA\u2019s Tropospheric Emissions: Monitoring of Pollution, which is scheduled to launch in 2022.",
-            "title": "OWLETS-2 NASA GSFC Pandora Spectrometer Project Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FOWLETS-2%2FPandora_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSuborbital%2FOWLETS-2%2FPandora_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/bams/article/100/2/291/69189/The-Ozone-Water-Land-Environmental-Transition",
-                    "description": "The Ozone Water\u2013Land Environmental Transition Study: An Innovative Strategy for Understanding Chesapeake Bay Pollution Events",
                     "@type": "dcat:Distribution",
+                    "description": "The Ozone Water\u2013Land Environmental Transition Study: An Innovative Strategy for Understanding Chesapeake Bay Pollution Events",
+                    "downloadURL": "https://journals.ametsoc.org/bams/article/100/2/291/69189/The-Ozone-Water-Land-Environmental-Transition",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-chesapeake-bay-study-to-help-improve-air-quality-forecasts",
-                    "description": "NASA Chesapeake Bay Study To Help Improve Air-Quality Forecasts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Chesapeake Bay Study To Help Improve Air-Quality Forecasts",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/nasa-chesapeake-bay-study-to-help-improve-air-quality-forecasts",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/owlets/docs/OwletsSlides.pdf",
-                    "description": "Ozone Water-Land Environmental Transition Study (OWLETS) Introduction Presentation Slides",
                     "@type": "dcat:Distribution",
+                    "description": "Ozone Water-Land Environmental Transition Study (OWLETS) Introduction Presentation Slides",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/owlets/docs/OwletsSlides.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Suborbital/OWLETS-2/Pandora_Data_1",
-                    "description": "DOI data set landing page for OWLETS2_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for OWLETS2_Pandora_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Suborbital/OWLETS-2/Pandora_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997468728-LARC_ASDC",
-                    "description": "Earthdata Search for OWLETS2_Pandora_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for OWLETS2_Pandora_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1997468728-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/OWLETS/2_Pandora_Data_1/",
-                    "description": "ASDC Direct Data Download for OWLETS2_Pandora_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for OWLETS2_Pandora_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/OWLETS/2_Pandora_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1997468728-LARC_ASDC",
+            "issued": "2020-11-18",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Suborbital/OWLETS-2/Pandora_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>36.0 -78.0 36.0 -75.0 41.0 -75.0 41.0 -78.0 36.0 -78.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-05-08T00:00:00Z/2019-03-15T23:59:59.999Z",
             "theme": [
                 "OWLETS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OWLETS-2 NASA GSFC Pandora Spectrometer Project Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOESRPLT/GCAS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Janz, Scott J., Dale  Allen, Ken  Pickering and Matt  Kowalewski.2019. GOES-R PLT Geostationary Coastal and Air Pollution Event (GEO-CAPE) Airborne Simulator (GCAS) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GOESRPLT/GCAS/DATA101",
-            "issued": "2019-08-08",
-            "temporal": "2017-03-21T18:48:57Z/2017-05-14T18:57:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-25",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "ocean optics",
-                "oceans",
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
-            "identifier": "C1979115813-GHRC_DAAC",
             "description": "The GOES-R PLT Geostationary Coastal and Air Pollution Event (GEO-CAPE) Airborne Simulator (GCAS) dataset consist of solar backscattered radiation measured by the Geostationary Coastal and Air Pollution Event (GEO-CAPE) Airborne Simulator (GCAS) flown aboard a NASA ER-2 high-altitude aircraft during the GOES-R Post Launch Test (PLT) field campaign. The GOES-R PLT field campaign took place from March to May of 2017 in support of post-launch L1B product validation of the Advanced Baseline Image (ABI) and the Geostationary Lightning Mapper (GLM). Data files in HDF-5 format are available for March 21, 2017 through May 14, 2017.",
-            "title": "GOES-R PLT Geostationary Coastal and Air Pollution Event (GEO-CAPE) Airborne Simulator (GCAS) V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FGCAS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FGCAS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltgcas",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltgcas",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GOESRPLT/DATA101",
-                    "description": "GOES-R PLT Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "GOES-R PLT Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GOESRPLT/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/GCAS/doc/goesrpltgcas_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/GCAS/doc/goesrpltgcas_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1002/2016JD025483",
-                    "description": "High-resolution NO2 observations from the Airborne Compact Atmospheric Mapper: Retrieval and validation",
                     "@type": "dcat:Distribution",
+                    "description": "High-resolution NO2 observations from the Airborne Compact Atmospheric Mapper: Retrieval and validation",
+                    "downloadURL": "https://doi.org/10.1002/2016JD025483",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/amt-9-2647-2016",
-                    "description": "Nitrogen dioxide observations from the Geostationary Trace gas and Aerosol Sensor Optimization (GeoTASO) airborne instrument: Retrieval algorithm and measurements during DISCOVER-AQ Texas 2013",
                     "@type": "dcat:Distribution",
+                    "description": "Nitrogen dioxide observations from the Geostationary Trace gas and Aerosol Sensor Optimization (GeoTASO) airborne instrument: Retrieval algorithm and measurements during DISCOVER-AQ Texas 2013",
+                    "downloadURL": "https://doi.org/10.5194/amt-9-2647-2016",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2017.2744323",
-                    "description": "Atmospheric Correction of Hyperspectral GCAS Airborne Measurements Over the North Atlantic Ocean and Louisiana Shelf",
                     "@type": "dcat:Distribution",
+                    "description": "Atmospheric Correction of Hyperspectral GCAS Airborne Measurements Over the North Atlantic Ocean and Louisiana Shelf",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2017.2744323",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1016/j.ecss.2017.10.021",
-                    "description": "Diurnal changes of remote sensing reflectance over Chesapeake Bay: Observations from the Airborne Compact Atmospheric Mapper",
                     "@type": "dcat:Distribution",
+                    "description": "Diurnal changes of remote sensing reflectance over Chesapeake Bay: Observations from the Airborne Compact Atmospheric Mapper",
+                    "downloadURL": "https://doi.org/10.1016/j.ecss.2017.10.021",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/goes-r-post-launch-test-plt",
-                    "description": "GOES-R Post Launch Test (PLT) Field Campaign Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "GOES-R Post Launch Test (PLT) Field Campaign Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/goes-r-post-launch-test-plt",
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
+            "identifier": "C1979115813-GHRC_DAAC",
+            "issued": "2019-08-08",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "ocean optics",
+                "oceans",
+                "weather events"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOESRPLT/GCAS/DATA101",
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
             "spatial": "-124.838 27.4778 -72.1396 43.6489",
+            "temporal": "2017-03-21T18:48:57Z/2017-05-14T18:57:21Z",
             "theme": [
                 "GOES-R PLT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOES-R PLT Geostationary Coastal and Air Pollution Event (GEO-CAPE) Airborne Simulator (GCAS) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHB2-M-TS-2-THERM%2FVIS-IMGEDR-V1.0",
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
-                "phobos 2",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "In February and March, 1989, the Termoskan instrument on board the Phobos '88 spacecraft of the USSR acquired a limited set of very high resolution simultaneous observations of the reflected solar flux (hereafter referred to as the visible channel) and emitted thermal flux (thermal infrared (IR)) from Mars's equatorial region. These are, so far, the highest spatial resolution thermal data ever obtained for Mars. Four slightly overlapping thermal panoramas (also called scans or swaths) cover a large portion of the equatorial region from 30 deg.S to 6 deg.N latitude. Simultaneous visible panoramas were taken during each of the four observing sessions; due to spacecraft memory limitations, visible channel processing was stopped early relative to the thermal channel for 2 of the sessions (2 and 4). Thus, the visible channel panoramas are shorter than the thermal panoramas for these sessions. These data are saved for historical reasons; they are not considered to be of archival quality.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phb2-m-ts-2-therm-vis-imgedr-v1.0_n5eg-j4iz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phobos 2",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHB2-M-TS-2-THERM%2FVIS-IMGEDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phb2-m-ts-2-therm-vis-imgedr-v1.0_n5eg-j4iz",
-            "description": "In February and March, 1989, the Termoskan instrument on board the Phobos '88 spacecraft of the USSR acquired a limited set of very high resolution simultaneous observations of the reflected solar flux (hereafter referred to as the visible channel) and emitted thermal flux (thermal infrared (IR)) from Mars's equatorial region. These are, so far, the highest spatial resolution thermal data ever obtained for Mars. Four slightly overlapping thermal panoramas (also called scans or swaths) cover a large portion of the equatorial region from 30 deg.S to 6 deg.N latitude. Simultaneous visible panoramas were taken during each of the four observing sessions; due to spacecraft memory limitations, visible channel processing was stopped early relative to the thermal channel for 2 of the sessions (2 and 4). Thus, the visible channel panoramas are shorter than the thermal panoramas for these sessions. These data are saved for historical reasons; they are not considered to be of archival quality.",
-            "title": "PHOBOS 2 MARS TERMOSCAN THERMAL/VISIBLE IMAGING EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOBOS 2 MARS TERMOSCAN THERMAL/VISIBLE IMAGING EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CAR/DATA111",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2018-01-10. CAR_SCARB_L1C. Version 1. CAR SCAR-B Smoke, Clouds, and Radiation-Brazil L1 V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CAR/DATA111. https://disc.gsfc.nasa.gov/datacollection/CAR_SCARB_L1C_1.html.",
-            "issued": "2017-11-29",
-            "temporal": "1995-08-17T00:00:00Z/1995-09-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-11-29",
-            "keyword": [
-                "aerosols",
-                "surface radiative properties",
-                "oceans",
-                "clouds",
-                "ocean optics",
-                "atmospheric radiation",
-                "land surface",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C1442068305-GES_DISC",
-            "description": "The objectives for the SCAR mission are to advance our knowledge of how the physical, chemical and radiative processes in our atmosphere are affected by sulfate aerosol and smoke from biomass burning; to improve our expertise at remotely sensing smoke, water vapor, clouds, vegetation and fires; and to assess the effects of deforestation and biomass burning on tropical landscapes. The SCAR-B campaign occurred in Brazil.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_SCARB_L1C",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR SCAR-B Smoke, Clouds, and Radiation-Brazil L1 V1 (CAR_SCARB_L1C) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_SCAR_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The objectives for the SCAR mission are to advance our knowledge of how the physical, chemical and radiative processes in our atmosphere are affected by sulfate aerosol and smoke from biomass burning; to improve our expertise at remotely sensing smoke, water vapor, clouds, vegetation and fires; and to assess the effects of deforestation and biomass burning on tropical landscapes. The SCAR-B campaign occurred in Brazil.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAR%2FDATA111",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCAR%2FDATA111",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1119330,102 +1119302,132 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_SCARB_L1C_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_SCARB_L1C_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_SCARB_L1C.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_SCARB_L1C.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CAR/CAR_SCARB_L1C.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/opendap/CAR/CAR_SCARB_L1C.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_SCARB_L1C.1/doc/CAR_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_SCARB_L1C.1/doc/CAR_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_SCAR_L1C_1.jpg",
+            "identifier": "C1442068305-GES_DISC",
+            "issued": "2017-11-29",
+            "keyword": [
+                "aerosols",
+                "surface radiative properties",
+                "oceans",
+                "clouds",
+                "ocean optics",
+                "atmospheric radiation",
+                "land surface",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CAR/DATA111",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-11-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CAR_SCARB_L1C",
             "spatial": "-63.8871 -16.4624 -47.9686 -7.2875",
+            "temporal": "1995-08-17T00:00:00Z/1995-09-07T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR SCAR-B Smoke, Clouds, and Radiation-Brazil L1 V1 (CAR_SCARB_L1C) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/184/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
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
-            "identifier": "DASHLINK_184",
             "description": "Air transportation, one of the most important modes of transportation, is also one of the safest. Nevertheless, the public demands that safety levels continuously improve and that the absolute number of aviation accidents continue to decline, even as air-traffic levels increase.  On February 12, 1997, after the tragedy of TWA 800, President William J. Clinton declared,\r\n\u201cWe will achieve a national goal of reducing the fatal aircraft accident rate by 80% within 10 years.\u201d\r\n \r\nIn response to this presidential declaration, the administrator of NASA announced that NASA would undertake a new program in aviation safety in support of this objective. NASA quickly formed the Aviation Safety Investment Strategy Team (ASIST) in collaboration with the Federal Aviation Administration (FAA) and the National Transportation Safety Board (NTSB), which organized a series of five workshops to examine the options and recommend an approach for NASA to develop the enabling technologies that address the president's goal. The exceptional and dedicated participation from all sectors of the aviation industry in the development of NASA\u2019s strategy was remarkable.",
-            "title": "Aviation System Monitoring and Modeling Project",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/TP-2007-214556_Statler.pdf",
-                    "description": "Paper",
                     "@type": "dcat:Distribution",
+                    "description": "Paper",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/TP-2007-214556_Statler.pdf",
+                    "mediaType": "application/pdf",
                     "title": "TP-2007-214556_Statler.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_184",
+            "issued": "2010-09-22",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/184/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Aviation System Monitoring and Modeling Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-PFS-2-EDR-EXT3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Mars Express PFS data set contains raw (CODMAC Level 2) measurements from the Planetary Fourier Spectrometer collected during the first extension Mars orbit phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-pfs-2-edr-ext3-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars express",
                 "mars",
@@ -1119434,36 +1119436,48 @@
                 "deep space",
                 "internal source"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-PFS-2-EDR-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-pfs-2-edr-ext3-v1.0",
-            "description": "The Mars Express PFS data set contains raw (CODMAC Level 2) measurements from the Planetary Fourier Spectrometer collected during the first extension Mars orbit phases.",
-            "title": "MARS EXPRESS MARS PFS EDR THIRD\n                                 EXTENSION MISSION DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS PFS EDR THIRD\n                                 EXTENSION MISSION DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/n5gq-2sq5",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Worms spun at higher than normal g values for 4 days on 20G centrifuge vs. worms kept at 1 X G. Both are mixed stage cultures. A stimulus or stress experiment design type is where that tests response of an organism(s) to stress/stimulus. e.g. osmotic stress behavioral treatment Physical Characteristics: worms kept at increased g values for 4 days (x g value) stimulus_or_stress_design.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-190",
+                    "mediaType": "text/html",
+                    "title": "Worms spun in centrifuge at elevated g values"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-190_n5gq-2sq5",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sample treatment protocol",
                 "labelling protocol",
@@ -1119479,45 +1119493,43 @@
                 "p-gse38877-5",
                 "p-gse38877-6"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/n5gq-2sq5",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-190_n5gq-2sq5",
-            "description": "Worms spun at higher than normal g values for 4 days on 20G centrifuge vs. worms kept at 1 X G. Both are mixed stage cultures. A stimulus or stress experiment design type is where that tests response of an organism(s) to stress/stimulus. e.g. osmotic stress behavioral treatment Physical Characteristics: worms kept at increased g values for 4 days (x g value) stimulus_or_stress_design.",
-            "title": "Worms spun in centrifuge at elevated g values",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-190",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Worms spun in centrifuge at elevated g values"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Worms spun in centrifuge at elevated g values"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/n5kh-nrt6",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brent Holben",
+                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
+            },
+            "description": "SolRad-Net (Solar Radiation Network) is an established network of ground-based sensors providing high-frequency solar flux measurements in quasi-realtime to the scientific community and various other end users. This network was implemented as a companion to AERONET and its instrumentation are invariably collocated with AERONET sites.  The Brazilian core of the present network was developed within the scientific framework of the LBA-ECO component of the Large-Scale Biosphere-Atmosphere Experiment in Amaz\u00f4nia. Historically, SolRad-Nethas preferentially selected sites that routinely experience intervals of biomass-burning, such as Amaz\u00f4nia and Sub-Saharan Africa for its long-term monitoring. Data that have been cleared as free of any operational problems are designated as Level 1.5. The raw, unscreened data are Level 1.0 by default and may contain observations that have been compromised for any of the (occasionally subtle) reasons described above. The Level 1.0 data are made available in the interest of presenting a comprehensive  dataset and to provide full transparency of our methods, however any use of these data is strongly discouraged. Data are available from several flux instruments including filtered and unfiltered pyranometers, photosynthetically active radiation (PAR) energy and quantum sensors, and UV-A and UV-B flux sensors. To maintain the integrity of the database and fairness to the individuals who have contributed, use of these data for publication requires an offer of authorship to the SolRad-Net PI(s).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://solrad-net.gsfc.nasa.gov/index.html",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000126",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "precipitable water",
                 "satellite",
@@ -1119527,179 +1119539,169 @@
                 "inversions",
                 "radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brent Holben",
-                "hasEmail": "mailto:Brent.N.Holben@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/n5kh-nrt6",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000126",
-            "description": "SolRad-Net (Solar Radiation Network) is an established network of ground-based sensors providing high-frequency solar flux measurements in quasi-realtime to the scientific community and various other end users. This network was implemented as a companion to AERONET and its instrumentation are invariably collocated with AERONET sites.  The Brazilian core of the present network was developed within the scientific framework of the LBA-ECO component of the Large-Scale Biosphere-Atmosphere Experiment in Amaz\u00f4nia. Historically, SolRad-Nethas preferentially selected sites that routinely experience intervals of biomass-burning, such as Amaz\u00f4nia and Sub-Saharan Africa for its long-term monitoring. Data that have been cleared as free of any operational problems are designated as Level 1.5. The raw, unscreened data are Level 1.0 by default and may contain observations that have been compromised for any of the (occasionally subtle) reasons described above. The Level 1.0 data are made available in the interest of presenting a comprehensive  dataset and to provide full transparency of our methods, however any use of these data is strongly discouraged. Data are available from several flux instruments including filtered and unfiltered pyranometers, photosynthetically active radiation (PAR) energy and quantum sensors, and UV-A and UV-B flux sensors. To maintain the integrity of the database and fairness to the individuals who have contributed, use of these data for publication requires an offer of authorship to the SolRad-Net PI(s).",
-            "title": "Sol-Rad Net Flux (L 1.0, 1.5, 2.0)",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://solrad-net.gsfc.nasa.gov/index.html",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Sol-Rad Net Flux (L 1.0, 1.5, 2.0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OETP-5-BOWSHOCKLOCATION-V1.0",
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
-                "pioneer venus",
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Bow Shock File. This file gives the orbit-by-orbit times and locations of the bow shock crossings, which are characterized by distinct changes in Ne. Multiple shock crossing are listed if they are sufficiently separated to be resolved accurately. (Bow shock crossings will be evident in the High Resolution Ne File when they occurred within 30 minutes of periapsis)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oetp-5-bowshocklocation-v1.0_n5mr-mi3v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer venus",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OETP-5-BOWSHOCKLOCATION-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-oetp-5-bowshocklocation-v1.0_n5mr-mi3v",
-            "description": "The Bow Shock File. This file gives the orbit-by-orbit times and locations of the bow shock crossings, which are characterized by distinct changes in Ne. Multiple shock crossing are listed if they are sufficiently separated to be resolved accurately. (Bow shock crossings will be evident in the High Resolution Ne File when they occurred within 30 minutes of periapsis)",
-            "title": "PVO VENUS ELECT TEMP PROBE DERVD\n                                      BOW SHOCK LOCATION VER 1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PVO VENUS ELECT TEMP PROBE DERVD\n                                      BOW SHOCK LOCATION VER 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/731",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kittel, T.G.F., N.A. Rosenbloom, T.H. Painter, D.S. Schimel, H.H. Fisher, A. Grimsdell, VEMAP Participants, C. Daly, and E.R. Hunt. 2004. VEMAP 1: Selected Model Results . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/731",
-            "issued": "2024-03-24",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-25",
-            "keyword": [
-                "atmospheric water vapor",
-                "soils",
-                "earth science",
-                "biosphere",
-                "ecological dynamics",
-                "land surface",
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
-            "identifier": "C2762253796-ORNL_CLOUD",
             "description": "The Vegetation/Ecosystem Modeling and Analysis Project (VEMAP) was a multi-institutional, international effort addressing the response of biogeography and biogeochemistry to environmental variability in climate and other drivers in both space and time domains. The objectives of VEMAP are the intercomparison of biogeochemistry models and vegetation type distribution models (biogeography models) and determination of their sensitivity to changing climate, elevated atmospheric carbon dioxide concentrations, and other sources of altered forcing.Selected variable output results from the VEMAP Phase I modeling exercise are now available for several combinations of biogeochemistry and biogeography models and climate change scenarios through the ORNL DAAC. For a description of the models and climate scenarios employed in the VEMAP 1 project and a discussion of the results please refer to the following publication: VEMAP Members. 1995. Vegetation/Ecosystem Modeling and Analysis Project: Comparing biogeography and biogeochemistry models in a continental-scale study of terrestrial ecosystem responses to climate change and CO2 doubling. Global Biogeochem. Cycles 9:407-437.",
-            "graphic-preview-description": "Browse Image",
-            "title": "VEMAP 1: Selected Model Results",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F731",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F731",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-1_results/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/vemap/vemap-1_results/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/vemap1_results_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEMAP/guides/vemap1_results_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/731",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/731",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_results/comp/VEMAP1_model_results_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_results/comp/VEMAP1_model_results_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_results/comp/vemap1_results_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/vemap/vemap-1_results/comp/vemap1_results_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vemap_logo_square.png",
+            "identifier": "C2762253796-ORNL_CLOUD",
+            "issued": "2024-03-24",
+            "keyword": [
+                "atmospheric water vapor",
+                "soils",
+                "earth science",
+                "biosphere",
+                "ecological dynamics",
+                "land surface",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/731",
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
             "spatial": "-124.0 26.0 -66.0 50.0",
+            "temporal": "2000-01-01T00:00:00Z/2000-12-31T23:59:59Z",
             "theme": [
                 "VEMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VEMAP 1: Selected Model Results"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67PCHURYUMOV-M18-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67pchuryumov-m18-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas",
@@ -1119707,39 +1119709,39 @@
                 "pluto",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67PCHURYUMOV-M18-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67pchuryumov-m18-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E%2FCAL-NAVCAM-2-EAR2-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Cruise Phase EAR2 from 16th Sep 2007 to 22nd Jan 2008 during the 2nd Earth Fly By on its journey to comet 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, adding of the FITS version, clarification of calibration target, document updates and resolve other minor outstanding errata.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-cal-navcam-2-ear2-v1.1",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "scat light",
                 "starfield",
@@ -1119748,113 +1119750,113 @@
                 "earth",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E%2FCAL-NAVCAM-2-EAR2-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-cal-navcam-2-ear2-v1.1",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Cruise Phase EAR2 from 16th Sep 2007 to 22nd Jan 2008 during the 2nd Earth Fly By on its journey to comet 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, adding of the FITS version, clarification of calibration target, document updates and resolve other minor outstanding errata.",
-            "title": "ROSETTA-ORBITER EARTH/CAL NAVCAM 2 EARTH SWING-BY 2 V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH/CAL NAVCAM 2 EARTH SWING-BY 2 V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR18-V1.0",
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
-                "titan",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Rhea Gravity Science Experiment (TIGR18) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 5, 6 and 7, 2014, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr18-v1.0_n5sf-4bbf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR18-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr18-v1.0_n5sf-4bbf",
-            "description": "The Cassini Radio Science Rhea Gravity Science Experiment (TIGR18) Raw Data Archive is a time-ordered collection of radio science raw data acquired on March 5, 6 and 7, 2014, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR18 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TIGR18 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC3-RAW-V9.0",
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
+            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nCOMET ESCORT 3 Phase from July 1,2016 until October 20, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.\nThis applies mainly to CALIBRATED and RESAMPLED datasets. The RAW dataset,\nhowever, has been updated as well in order provide all datasets at the\nsame stage, although RAW data proper did not change.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc3-raw-v9.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC3-RAW-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc3-raw-v9.0",
-            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nCOMET ESCORT 3 Phase from July 1,2016 until October 20, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.\nThis applies mainly to CALIBRATED and RESAMPLED datasets. The RAW dataset,\nhowever, has been updated as well in order provide all datasets at the\nsame stage, although RAW data proper did not change.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC3 RAW V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC3 RAW V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-VIS-2-EDR-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is a digital archive of images acquired by the Viking Orbiter 1 and 2 spacecraft. The archive will include the best available Experiment Data Record (EDR) versions of images acquired by the Viking Orbiter Visual Imaging Subsystems (VIS). The archive is stored on compact read-only optical disk media (CD-ROM) for distribution. The EDR image data are stored on CD-ROM in a compressed format that allows exact reconstruction of the original image. The images were compressed in order to reduce the number of CD-ROMs required for the archive. The average Viking Orbiter image is compressed by a factor of about 3.5. Each CD-ROM in the archive also includes documentation about the organization and contents of the disk. Software is included to provide programmers with tools to decompress image files. The CD-ROM has index files containing information about all the images stored in the archive. These index files can be loaded into a database management system to help the user locate images of interest.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-vis-2-edr-v2.0_n5ve-5bvk",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "viking",
                 "mars",
@@ -1119862,147 +1119864,118 @@
                 "phobos",
                 "deimos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VO1%2FVO2-M-VIS-2-EDR-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vo1-vo2-m-vis-2-edr-v2.0_n5ve-5bvk",
-            "description": "This data set is a digital archive of images acquired by the Viking Orbiter 1 and 2 spacecraft. The archive will include the best available Experiment Data Record (EDR) versions of images acquired by the Viking Orbiter Visual Imaging Subsystems (VIS). The archive is stored on compact read-only optical disk media (CD-ROM) for distribution. The EDR image data are stored on CD-ROM in a compressed format that allows exact reconstruction of the original image. The images were compressed in order to reduce the number of CD-ROMs required for the archive. The average Viking Orbiter image is compressed by a factor of about 3.5. Each CD-ROM in the archive also includes documentation about the organization and contents of the disk. Software is included to provide programmers with tools to decompress image files. The CD-ROM has index files containing information about all the images stored in the archive. These index files can be loaded into a database management system to help the user locate images of interest.",
-            "title": "VO1/VO2 MARS VISUAL IMAGING SS EXPRMNT DATA RECORD V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VO1/VO2 MARS VISUAL IMAGING SS EXPRMNT DATA RECORD V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1012-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-04T10:08:00.000 to 2015-09-04T14:51:13.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1012-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1012-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1012-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-04T10:08:00.000 to 2015-09-04T14:51:13.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1012 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1012 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT1-MTP026-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 26 period of the EXTENSION 1 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext1-mtp026-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT1-MTP026-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext1-mtp026-v1.0",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 26 period of the EXTENSION 1 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 1\n    MTP026 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 1\n    MTP026 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA1001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Marcel Dobber. 2007-09-20. OML1BIRR. Version 003. OMI/Aura Level 1B Solar Irradiances V003. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA1001. https://disc.gsfc.nasa.gov/datacollection/OML1BIRR_003.html. Digital Science Data.",
-            "issued": "2004-08-09",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2007-09-20",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "solar activity",
-                "sun-earth interactions",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JEROME ALFRED",
                 "hasEmail": "mailto:jerome.m.alfred@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1239966744-GES_DISC",
-            "description": "The OMI Level 1B solar irradiance product is the radiometrically calibrated and geolocated measurements of the UV and Visible channels of the spectral solar irradiance. It is the averaged measurements of the solar irradiances over a single solar observation in the wavelength ranges of UV1 (264-311 nm, 159 channels), UV2 (307-383 nm, 557 channels) and VIS (349-504 nm, 751 channels). The data contain solar measurement products for both the global and the spatial zoom-in mode. This product only contains measurements obtained with the quartz volume diffuser and provides average of the individual measurements made along track to average out the solar elevation dependent bidirectional reflectance distribution function (BRDF) features of the diffuser. The shortname for this OMI Level-1B Product is OML1BIRR. The lead algorithm scientists for this product is Dr. Marcel Dobber from the Roayl Netherlands Meteorological Institude (KNMI).\n\nOMI calibrated and geolocated radiances for the UV and Visible channels, spectral irradiances, calibration measurements, and all derived geophysical atmospheric products are archived at the NASA Goddard Earth Sciences Data and Information Services Center (GES DISC). OML1BIRR files are stored in the HDF4 based EOS Hierarchical Data Format. The radiances for the earth measurements (also referred as signal) and its precision are stored as a 16 bit mantissa and an 8-bit exponent. The signal can be computed using the equation: signal = mantissa x 10^exponent. For the precision, the same exponent is used as for the signal.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OML1BIRR",
             "creator": "Marcel Dobber",
-            "title": "OMI/Aura Level 1B Solar Irradiances V003 (OML1BIRR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BIRR_003.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The OMI Level 1B solar irradiance product is the radiometrically calibrated and geolocated measurements of the UV and Visible channels of the spectral solar irradiance. It is the averaged measurements of the solar irradiances over a single solar observation in the wavelength ranges of UV1 (264-311 nm, 159 channels), UV2 (307-383 nm, 557 channels) and VIS (349-504 nm, 751 channels). The data contain solar measurement products for both the global and the spatial zoom-in mode. This product only contains measurements obtained with the quartz volume diffuser and provides average of the individual measurements made along track to average out the solar elevation dependent bidirectional reflectance distribution function (BRDF) features of the diffuser. The shortname for this OMI Level-1B Product is OML1BIRR. The lead algorithm scientists for this product is Dr. Marcel Dobber from the Roayl Netherlands Meteorological Institude (KNMI).\n\nOMI calibrated and geolocated radiances for the UV and Visible channels, spectral irradiances, calibration measurements, and all derived geophysical atmospheric products are archived at the NASA Goddard Earth Sciences Data and Information Services Center (GES DISC). OML1BIRR files are stored in the HDF4 based EOS Hierarchical Data Format. The radiances for the earth measurements (also referred as signal) and its precision are stored as a 16 bit mantissa and an 8-bit exponent. The signal can be computed using the equation: signal = mantissa x 10^exponent. For the precision, the same exponent is used as for the signal.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA1001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA1001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1120012,73 +1119985,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BIRR_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BIRR_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BIRR.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BIRR.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BIRR_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BIRR_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BIRR.003/doc/README.OML1B.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BIRR.003/doc/README.OML1B.pdf",
+                    "mediaType": "application/pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/RD01_SD467_IODS_Vol_2_issue8.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/RD01_SD467_IODS_Vol_2_issue8.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/known_instrumental_effects_l1b_data_omi_v6.pdf",
-                    "description": "Known instrumental issues",
                     "@type": "dcat:Distribution",
+                    "description": "Known instrumental issues",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/known_instrumental_effects_l1b_data_omi_v6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-01.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
@@ -1120088,175 +1120061,204 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BIRR_003.png",
+            "identifier": "C1239966744-GES_DISC",
+            "issued": "2004-08-09",
+            "keyword": [
+                "solar activity",
+                "sun-earth interactions",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA1001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2007-09-20",
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
+            "series-name": "OML1BIRR",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Level 1B Solar Irradiances V003 (OML1BIRR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3347-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-13T09:32:41.000 to 2012-07-13T13:08:34.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3347-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3347-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3347-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-13T09:32:41.000 to 2012-07-13T13:08:34.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3347 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3347 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC-3-AST2-LUTETIAFLYBY-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the LUTETIA FLY-BY mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-3-ast2-lutetiaflyby-v1.1_n63w-khzv",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "16 cyg b",
                 "vega",
                 "21 lutetia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-OSINAC-3-AST2-LUTETIAFLYBY-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-osinac-3-ast2-lutetiaflyby-v1.1_n63w-khzv",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the LUTETIA FLY-BY mission phase",
-            "title": "ROSETTA-ORBITER LUTETIA FLY-BY OSINAC 3 RDR data",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER LUTETIA FLY-BY OSINAC 3 RDR data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V6.0",
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
+            "description": "This data set is intended to include all groundbased asteroid radar detections. These entries were collected by Steven J. Ostro, and selected data have been provided as collected from the published literature.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v6.0_n64x-q6pr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-RADAR-V6.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-radar-v6.0_n64x-q6pr",
-            "description": "This data set is intended to include all groundbased asteroid radar detections. These entries were collected by Steven J. Ostro, and selected data have been provided as collected from the published literature.",
-            "title": "ASTEROID RADAR V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID RADAR V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-3-EXT2-V2.0",
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
+            "description": "This data set contains CODMAC level 3 science data acquired by the DFMS and RTOF ROSINA sensors between 2016-04-06 and 2016-06-29 during the Extension phase 2 of the Rosetta mission to comet 67P/CG. V2.0 : Mass scale has been enhanced for a selection of masses which are now provided with 4 digits after the coma and the offset removal has been improved, corrupted files have been removed in the V2.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-3-ext2-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-3-EXT2-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-3-ext2-v2.0",
-            "description": "This data set contains CODMAC level 3 science data acquired by the DFMS and RTOF ROSINA sensors between 2016-04-06 and 2016-06-29 during the Extension phase 2 of the Rosetta mission to comet 67P/CG. V2.0 : Mass scale has been enhanced for a selection of masses which are now provided with 4 digits after the coma and the offset removal has been improved, corrupted files have been removed in the V2.0",
-            "title": "ROSETTA-ORBITER 67P ROSINA 3\n                                      EXT2 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 3\n                                      EXT2 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-CUBE-V1.3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Spectrographic observations of Jupiter, Saturnian rings, satellites, atmospheres and the interplanetary medium in the far and extreme ultraviolet.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-cube-v1.3_n68k-wyh3",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "sun",
                 "albiorix",
@@ -1120292,58 +1120294,36 @@
                 "titan",
                 "tethys"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-CUBE-V1.3",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-cube-v1.3_n68k-wyh3",
-            "description": "Spectrographic observations of Jupiter, Saturnian rings, satellites, atmospheres and the interplanetary medium in the far and extreme ultraviolet.",
-            "title": "CASSINI ORBITER SATURN UVIS SPATIAL SPECTRAL IMAGE CUBE V1.3",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI ORBITER SATURN UVIS SPATIAL SPECTRAL IMAGE CUBE V1.3"
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
-                "data",
-                "sharad"
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
-            "identifier": "NASA-432",
             "description": "SHARAD",
-            "title": "PDS MRO SHARAD Radargram Release 2",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1120351,23 +1120331,52 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-432",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "data",
+                "sharad"
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
+            "title": "PDS MRO SHARAD Radargram Release 2"
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
+            "description": "ASE, MECA, MET, OM, RAC, SSI, TEGA, TT",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090223.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-775",
+            "issued": "2018-06-25",
             "keyword": [
                 "ase",
                 "tt",
@@ -1120379,42 +1120388,47 @@
                 "met",
                 "meca"
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
-            "identifier": "NASA-775",
-            "description": "ASE, MECA, MET, OM, RAC, SSI, TEGA, TT",
-            "title": "PDS Phoenix Data Release 2",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20090223.shtml",
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
+            "title": "PDS Phoenix Data Release 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition07/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "Press kit for ISS mission Expedition 07 from 04/2003-10/2003. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Press Kit PDF",
+                    "downloadURL": "http://www.shuttlepresskit.com/EXPEDITION7/Expd-7_PKit.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "ISS 07 Press Kit"
+                }
+            ],
+            "identifier": "OCIO-Fitara-19",
             "issued": "2003-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "launch",
                 "iss",
@@ -1120426,940 +1120440,902 @@
                 "7",
                 "mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition07/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "JSC"
             },
-            "identifier": "OCIO-Fitara-19",
-            "description": "Press kit for ISS mission Expedition 07 from 04/2003-10/2003. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
-            "title": "ISS Expedition 07 Press Kit",
-            "programCode": [
-                "026:037"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.shuttlepresskit.com/EXPEDITION7/Expd-7_PKit.pdf",
-                    "description": "Press Kit PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS 07 Press Kit"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ISS Expedition 07 Press Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-S-TRD-4-SUMM-1HR-V1.0",
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
-                "saturn",
-                "pioneer 11"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 11 trapped radiation detector 1 hour data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-s-trd-4-summ-1hr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "pioneer 11"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-S-TRD-4-SUMM-1HR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-s-trd-4-summ-1hr-v1.0",
-            "description": "Pioneer 11 trapped radiation detector 1 hour data.",
-            "title": "P11 S TRD 4 SUMM 1HR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P11 S TRD 4 SUMM 1HR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1833",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nehrir, A.R., J.E. Collins, S.A. Kooi, and R.A. Barton-Grimley. 2022. ACT-America: HALO Lidar Measurements of AOP and ML Heights, 2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1833",
-            "issued": "2022-12-29",
-            "temporal": "2019-06-17T00:00:00Z/2019-07-28T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "spectral/engineering",
-                "atmospheric chemistry",
-                "altitude",
-                "earth science",
-                "atmosphere",
-                "aerosols",
-                "lidar"
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
-            "identifier": "C2704996986-ORNL_CLOUD",
             "description": "This dataset provides measurements from the High Altitude Lidar Observatory (HALO) instrument, an airborne multi-function Differential Absorption Lidar (DIAL) and High Spectral Resolution Lidar (HSRL), operating at 532 nm and 1064 nm wavelengths onboard a C-130 aircraft during the June and July 2019 ACT-America campaign. The flights took place over eastern and central North America based from Shreveport, Louisiana; Lincoln, Nebraska; and NASA Wallops Flight Facility located on the eastern shore of Virginia. HALO data were sampled at 0.5 s temporal and 1.25 m vertical resolutions. The data include profiles of aerosol optical properties (AOP), distributions of mixed layer heights (MLH), columns of tropospheric methane, and navigation parameters. The data are provided in HDF5 format along with PNG images and a companion files in Portable Document (*.pdf) format.",
-            "graphic-preview-description": "Map of mixing layer height across the sampling area. Source: 20190617_MixedLayerHeight_map.png",
-            "title": "ACT-America: HALO Lidar Measurements of AOP and ML Heights, 2019",
-            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/HALO_LiDAR_AOP_ML_Heights_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1833",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1833",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/actamerica/HALO_LiDAR_AOP_ML_Heights/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/actamerica/HALO_LiDAR_AOP_ML_Heights/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/HALO_LiDAR_AOP_ML_Heights.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/HALO_LiDAR_AOP_ML_Heights.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1833",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1833",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/HALO_LiDAR_AOP_ML_Heights/comp/actamerica-HALO_C130_aerosol_description.pdf",
-                    "description": "ACT-America: HALO Lidar Measurements of AOP and ML Heights, 2019: actamerica-HALO_C130_aerosol_description.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: HALO Lidar Measurements of AOP and ML Heights, 2019: actamerica-HALO_C130_aerosol_description.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/HALO_LiDAR_AOP_ML_Heights/comp/actamerica-HALO_C130_aerosol_description.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/HALO_LiDAR_AOP_ML_Heights/comp/HALO_LiDAR_AOP_ML_Heights.pdf",
-                    "description": "ACT-America: HALO Lidar Measurements of AOP and ML Heights, 2019: HALO_LiDAR_AOP_ML_Heights.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: HALO Lidar Measurements of AOP and ML Heights, 2019: HALO_LiDAR_AOP_ML_Heights.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/HALO_LiDAR_AOP_ML_Heights/comp/HALO_LiDAR_AOP_ML_Heights.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/HALO_LiDAR_AOP_ML_Heights_Fig1.png",
-                    "description": "Map of mixing layer height across the sampling area. Source: 20190617_MixedLayerHeight_map.png",
                     "@type": "dcat:Distribution",
+                    "description": "Map of mixing layer height across the sampling area. Source: 20190617_MixedLayerHeight_map.png",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/HALO_LiDAR_AOP_ML_Heights_Fig1.png",
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
                 }
             ],
+            "graphic-preview-description": "Map of mixing layer height across the sampling area. Source: 20190617_MixedLayerHeight_map.png",
+            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/HALO_LiDAR_AOP_ML_Heights_Fig1.png",
+            "identifier": "C2704996986-ORNL_CLOUD",
+            "issued": "2022-12-29",
+            "keyword": [
+                "spectral/engineering",
+                "atmospheric chemistry",
+                "altitude",
+                "earth science",
+                "atmosphere",
+                "aerosols",
+                "lidar"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1833",
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
             "spatial": "-102.0 28.0 -73.0 50.0",
+            "temporal": "2019-06-17T00:00:00Z/2019-07-28T23:59:59Z",
             "theme": [
                 "ACT-America",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACT-America: HALO Lidar Measurements of AOP and ML Heights, 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SASSIE-GLID2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "James Thomson. 2023-05-08. SASSIE Arctic Field Campaign Wave Glider Data Fall 2022. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, SASSIE Project Data Manager, Frederick Bingham. https://doi.org/10.5067/SASSIE-GLID2. https://doi.org/10.5067/SASSIE-GLID2.",
-            "issued": "2022-08-12",
-            "temporal": "2022-08-12T00:00:00Z/2022-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-28",
-            "references": [
-                "https://doi.org/doi.org/10.1175/JTECH-D-17-0091.1"
-            ],
-            "keyword": [
-                "ocean winds",
-                "atmosphere",
-                "ocean temperature",
-                "oceans",
-                "ocean circulation",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "salinity/density",
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
-            "identifier": "C2637536168-POCLOUD",
-            "description": "The Salinity and Stratification at the Sea Ice Edge (SASSIE) project is a NASA experiment that aims to understand how salinity anomalies in the upper ocean generated by melting sea ice affect sea surface temperature (SST), stratification, and subsequent sea-ice growth. SASSIE involved a field campaign that sampled the transition from summer melt to autumn ice advance in the Beaufort Sea during August-October 2022, making intensive in situ and remote sensing observations within ~200 km of the sea ice edge. A waveglider is an autonomous platform propelled by the conversion of ocean wave energy into forward thrust and employing solar panels to power instrumentation. During the SASSIE deployment, four wavegliders were deployed near Prudhoe Bay on 12-14 August 2022. The wavegliders collect measurements of ocean surface salinity, temperature, currents, waves, and meteorological data. Custom integrated Casting CTDs provide additional profiles of salinity and temperature to a depth of 150m below the surface. Data are available in netCDF format.",
-            "graphic-preview-description": "Thumbnail",
             "creator": "James Thomson",
-            "title": "SASSIE Arctic Field Campaign Wave Glider Data Fall 2022 Version 1",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_WAVEGLIDERS_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Salinity and Stratification at the Sea Ice Edge (SASSIE) project is a NASA experiment that aims to understand how salinity anomalies in the upper ocean generated by melting sea ice affect sea surface temperature (SST), stratification, and subsequent sea-ice growth. SASSIE involved a field campaign that sampled the transition from summer melt to autumn ice advance in the Beaufort Sea during August-October 2022, making intensive in situ and remote sensing observations within ~200 km of the sea ice edge. A waveglider is an autonomous platform propelled by the conversion of ocean wave energy into forward thrust and employing solar panels to power instrumentation. During the SASSIE deployment, four wavegliders were deployed near Prudhoe Bay on 12-14 August 2022. The wavegliders collect measurements of ocean surface salinity, temperature, currents, waves, and meteorological data. Custom integrated Casting CTDs provide additional profiles of salinity and temperature to a depth of 150m below the surface. Data are available in netCDF format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSASSIE-GLID2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSASSIE-GLID2",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2637536168-POCLOUD",
-                    "description": "Browse and download granules over HTTPS using the virtual directories",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2637536168-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2637536168-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2637536168-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_WAVEGLIDERS_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_WAVEGLIDERS_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SASSIE-GLID2",
-                    "description": "Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Dataset Landing Page",
+                    "downloadURL": "https://doi.org/10.5067/SASSIE-GLID2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SASSIE_L2_WAVEGLIDERS_V1.jpg",
+            "identifier": "C2637536168-POCLOUD",
+            "issued": "2022-08-12",
+            "keyword": [
+                "ocean winds",
+                "atmosphere",
+                "ocean temperature",
+                "oceans",
+                "ocean circulation",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "salinity/density",
+                "ocean waves"
+            ],
+            "landingPage": "https://doi.org/10.5067/SASSIE-GLID2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/doi.org/10.1175/JTECH-D-17-0091.1"
+            ],
             "spatial": "-156.0 70.0 -142.0 73.5",
+            "temporal": "2022-08-12T00:00:00Z/2022-09-30T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASSIE Arctic Field Campaign Wave Glider Data Fall 2022 Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-VESTA-GAMMA-IRON-COR-V1.0",
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
+            "description": "This data set provides tables of         net counting rates of Fe gamma rays at 7.6 MeV measured by the BGO      detector of Dawn's Gamma Ray and Neutron Detector acquired at the       low altitude mapping orbit.                                             The counting rates were normalized for variations of live time,         solid angle of Vesta, and galactic cosmic ray intensity. They  were     also corrected for variations of neutron number density derived from    thermal and epithermal neutron observations by GRaND                    (PRETTYMANETAL2013). The table contains the original Fe counting        rates reported by YAMASHITAETAL2013.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-vesta-gamma-iron-cor-v1.0_n6ev-nd9s",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "4 vesta"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-VESTA-GAMMA-IRON-COR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-vesta-gamma-iron-cor-v1.0_n6ev-nd9s",
-            "description": "This data set provides tables of         net counting rates of Fe gamma rays at 7.6 MeV measured by the BGO      detector of Dawn's Gamma Ray and Neutron Detector acquired at the       low altitude mapping orbit.                                             The counting rates were normalized for variations of live time,         solid angle of Vesta, and galactic cosmic ray intensity. They  were     also corrected for variations of neutron number density derived from    thermal and epithermal neutron observations by GRaND                    (PRETTYMANETAL2013). The table contains the original Fe counting        rates reported by YAMASHITAETAL2013.",
-            "title": "DAWN GRAND MAP VESTA GAMMA FE           \n                                     CORRECTED COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN GRAND MAP VESTA GAMMA FE           \n                                     CORRECTED COUNTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67P-M28-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-04-05T23:25:00.000 to 2016-05-03T23:25:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67p-m28-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67P-M28-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67p-m28-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-04-05T23:25:00.000 to 2016-05-03T23:25:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP028 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP028 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1732",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "McKain, K., and C. Sweeney. 2021. ATom: CO2, CH4, and CO Measurements from Picarro, 2016-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1732",
-            "issued": "2021-10-28",
-            "temporal": "2016-07-26T00:00:00Z/2018-05-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
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
-            "identifier": "C2676917139-ORNL_CLOUD",
             "description": "This dataset contains atmospheric measurements of CO2, CH4, and CO mixing ratios made with a Picarro G2401 spectrometer during the four ATom campaigns. Picarro G2401 uses Wavelength-Scanned Cavity Ring Down Spectroscopy (WS-CRDS), a time-based measurement utilizing a near-infrared laser to measure a spectral signature of the molecule. For the ATom mission, the Picarro instrument was modified in the laboratory to operate across the full pressure altitude range of flight campaigns. The instrument was also modified to have a shorter measurement interval.",
-            "graphic-preview-description": "The forward-facing side of the NOAA Picarro G2401 instrument used on the four ATom campaigns.",
-            "title": "ATom: CO2, CH4, and CO Measurements from Picarro, 2016-2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Picarro_Instrument_Data_Fig1.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1732",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1732",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Picarro_Instrument_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_Picarro_Instrument_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Picarro_Instrument_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Picarro_Instrument_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1732",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1732",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Picarro_Instrument_Data/comp/ATom_Picarro_Instrument_Data.pdf",
-                    "description": "ATom: CO2, CH4, and CO Measurements from Picarro, 2016-2018: ATom_Picarro_Instrument_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: CO2, CH4, and CO Measurements from Picarro, 2016-2018: ATom_Picarro_Instrument_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Picarro_Instrument_Data/comp/ATom_Picarro_Instrument_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Picarro_Instrument_Data/comp/NOAA-Picarro_ATom1234_readme.pdf",
-                    "description": "ATom: CO2, CH4, and CO Measurements from Picarro, 2016-2018: NOAA-Picarro_ATom1234_readme.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: CO2, CH4, and CO Measurements from Picarro, 2016-2018: NOAA-Picarro_ATom1234_readme.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_Picarro_Instrument_Data/comp/NOAA-Picarro_ATom1234_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Picarro_Instrument_Data_Fig1.jpeg",
-                    "description": "The forward-facing side of the NOAA Picarro G2401 instrument used on the four ATom campaigns.",
                     "@type": "dcat:Distribution",
+                    "description": "The forward-facing side of the NOAA Picarro G2401 instrument used on the four ATom campaigns.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_Picarro_Instrument_Data_Fig1.jpeg",
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
+            "graphic-preview-description": "The forward-facing side of the NOAA Picarro G2401 instrument used on the four ATom campaigns.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_Picarro_Instrument_Data_Fig1.jpeg",
+            "identifier": "C2676917139-ORNL_CLOUD",
+            "issued": "2021-10-28",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "air quality",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1732",
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
+            "temporal": "2016-07-26T00:00:00Z/2018-05-21T23:59:59Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: CO2, CH4, and CO Measurements from Picarro, 2016-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SIMBAD_DESCHAMPS_LOA/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SIMBAD_DESCHAMPS_LOA/DATA001.",
-            "issued": "1996-10-14",
-            "temporal": "1996-10-13T00:42:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "ocean temperature",
-                "ocean optics",
-                "earth science",
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
-            "identifier": "C1633360661-OB_DAAC",
             "description": "Measurements made by Laboratoire dOptique Atmospherique (LOA) PI Pierr-Yves Deschamps using the SIMBAD radiometer during 1996 to 2001.",
-            "title": "Measurements using the SIMBAD radiometer by the Laboratoire dOptique Atmospherique (LOA)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSIMBAD_DESCHAMPS_LOA%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSIMBAD_DESCHAMPS_LOA%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/SIMBAD_DESCHAMPS_LOA/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/SIMBAD_DESCHAMPS_LOA/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360661-OB_DAAC",
+            "issued": "1996-10-14",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean temperature",
+                "ocean optics",
+                "earth science",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SIMBAD_DESCHAMPS_LOA/DATA001",
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
+            "temporal": "1996-10-13T00:42:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements using the SIMBAD radiometer by the Laboratoire dOptique Atmospherique (LOA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H45Q4T1N",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University. 2011-12-31. Natural Resource Management Index (NRMI), 2011 Release. Version 2011.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H45Q4T1N. https://doi.org/10.7927/H45Q4T1N.",
-            "issued": "2011-12-31",
-            "temporal": "2006-01-01T00:00:00Z/2010-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-12-31",
-            "references": [
-                "https://doi.org/10.7927/H49G5JRZ",
-                "https://doi.org/10.7927/H41Z4299",
-                "https://doi.org/10.7927/H4NZ85MP",
-                "https://doi.org/10.7927/H46M34RP",
-                "https://doi.org/10.7927/H4G73BM2",
-                "https://doi.org/10.7927/H48913TX",
-                "https://doi.org/10.7927/H4SQ8XGT",
-                "https://doi.org/10.7927/6t8a-es66",
-                "https://doi.org/10.7927/r6mv-sv82"
-            ],
-            "keyword": [
-                "sustainability",
-                "human dimensions",
-                "earth science",
-                "environmental impacts"
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
-            "identifier": "C1000000031-SEDAC",
-            "description": "The Natural Resource Management Index (NRMI), 2011 Release is a composite index for 174 countries derived from the average of four proximity-to-target indicators for eco-region protection (weighted average percentage of biomes under protected status), access to improved sanitation, access to improved water and child mortality. The 2011 release of the NRMI includes a consistent time series of NRMIs for 2006 to 2011. In addition, the 2011 release includes two new indicators that will eventually supplant the NRMI: a Natural Resource Protection Indicator (NRPI) that is solely composed of the eco-region protection indicator, and a Child Health Indicator (CHI), which is an unweighted average of the proximtiy-to-target scores for access to water, access to sanitation, and child mortality. The data set is produced and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the Yale Center for Environmental Law and Policy (YCELP), Yale University.",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Natural Resource Management Index (NRMI), 2011 Release",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-management-index-2011/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Natural Resource Management Index (NRMI), 2011 Release is a composite index for 174 countries derived from the average of four proximity-to-target indicators for eco-region protection (weighted average percentage of biomes under protected status), access to improved sanitation, access to improved water and child mortality. The 2011 release of the NRMI includes a consistent time series of NRMIs for 2006 to 2011. In addition, the 2011 release includes two new indicators that will eventually supplant the NRMI: a Natural Resource Protection Indicator (NRPI) that is solely composed of the eco-region protection indicator, and a Child Health Indicator (CHI), which is an unweighted average of the proximtiy-to-target scores for access to water, access to sanitation, and child mortality. The data set is produced and distributed by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the Yale Center for Environmental Law and Policy (YCELP), Yale University.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH45Q4T1N",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH45Q4T1N",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-management-index-2011/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-management-index-2011/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-management-index-2011/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-management-index-2011/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-management-index-2011/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-management-index-2011/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-management-index-2011",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/nrmi-natural-resource-management-index-2011",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/nrmi/nrmi-natural-resource-management-index-2011/sedac-logo.jpg",
+            "identifier": "C1000000031-SEDAC",
+            "issued": "2011-12-31",
+            "keyword": [
+                "sustainability",
+                "human dimensions",
+                "earth science",
+                "environmental impacts"
+            ],
+            "landingPage": "https://doi.org/10.7927/H45Q4T1N",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H49G5JRZ",
+                "https://doi.org/10.7927/H41Z4299",
+                "https://doi.org/10.7927/H4NZ85MP",
+                "https://doi.org/10.7927/H46M34RP",
+                "https://doi.org/10.7927/H4G73BM2",
+                "https://doi.org/10.7927/H48913TX",
+                "https://doi.org/10.7927/H4SQ8XGT",
+                "https://doi.org/10.7927/6t8a-es66",
+                "https://doi.org/10.7927/r6mv-sv82"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -55.0 180.0 90.0",
+            "temporal": "2006-01-01T00:00:00Z/2010-12-31T00:00:00Z",
             "theme": [
                 "NRMI",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Natural Resource Management Index (NRMI), 2011 Release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0129",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-28. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0129.",
-            "issued": "1999-10-28",
-            "temporal": "1987-07-01T00:00:00Z/1987-07-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-03",
-            "keyword": [
-                "atmosphere",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JACK SNIDER",
                 "hasEmail": "mailto:jsnider@etl.noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001261-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.Microwave radiometer with steerable antenna was used for the measurement of column amounts of liquid water in clouds, and precipitable water vapor in the atmosphere. Antenna was directed to the zenith during FIRE I.Operating frequencies: 20.6, 31.65, 90.0 GHzSpatial resolution: 2.5 deg antenna beamwidth (44m @ 1.0 km range)Temporal resolution: 60 secEstimated accuracies Liquid water: +/- 10 percent or better (absolute) Noise level +/- .025 mm Water vapor: 0.08 cm rms relative to radiosonde (Vapor and liquid data retrievals were from 20.6 and 31.65 GHz data only)Radiometer location: San Nicolas Island, northwestern tip 33.27N, 119.58W",
-            "title": "First ISCCP Regional Experiment (FIRE) Marine Stratocumulus Microwave Radiometer Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0129",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0129",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001261-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_MS_MCRW_RAD_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_MS_MCRW_RAD_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001261-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ms_mcrw_rad_dataset.pdf",
-                    "description": "FIRE Marine Stratocumulus Microwave Radiometer Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Marine Stratocumulus Microwave Radiometer Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ms_mcrw_rad_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ms_mcrw_rad_info1.txt",
-                    "description": "Instrument Description for microwave radiometer Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description for microwave radiometer Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ms_mcrw_rad_info1.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ms_mcrw_rad.ps",
-                    "description": "FIRE Marine Stratocumulus sample read software and data files - Direct File Download (.ps) Readme",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Marine Stratocumulus sample read software and data files - Direct File Download (.ps) Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ms_mcrw_rad.ps",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fms_mcw_rad.c",
-                    "description": "Reads in NOAA MICROWAVE RADIOMETER data at SAN NICOLAS ISLAND site taken during the FIRE Marine Stratacumulus Experiment - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Reads in NOAA MICROWAVE RADIOMETER data at SAN NICOLAS ISLAND site taken during the FIRE Marine Stratacumulus Experiment - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fms_mcw_rad.c",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0129",
-                    "description": "DOI data set landing page for FIRE_MS_MCRW_RAD_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_MS_MCRW_RAD_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0129",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_MS_MCRW_RAD/",
-                    "description": "ASDC Direct Data Download for FIRE_MS_MCRW_RAD_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_MS_MCRW_RAD_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_MS_MCRW_RAD/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_MS_MCRW_RAD/contents.html",
-                    "description": "OPeNDAP data access for FIRE_MS_MCRW_RAD_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_MS_MCRW_RAD_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_MS_MCRW_RAD/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001261-LARC_ASDC",
+            "issued": "1999-10-28",
+            "keyword": [
+                "atmosphere",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0129",
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
             "spatial": "33.27 -119.58",
+            "temporal": "1987-07-01T00:00:00Z/1987-07-19T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Marine Stratocumulus Microwave Radiometer Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOESRPLT/LMA/DATA601",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sills, David .2019. GOES-R PLT Southern Ontario Lightning Mapping Array (LMA) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GOESRPLT/LMA/DATA601",
-            "issued": "2019-03-06",
-            "temporal": "2017-04-01T00:00:00Z/2017-06-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "earth science",
-                "atmospheric electricity",
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
-            "identifier": "C1980036345-GHRC_DAAC",
             "description": "The GOES-R PLT Southern Ontario Lightning Mapping Array (LMA) dataset consists of total lightning data measured from the Southern Ontario LMA (SOLMA) network during the GOES-R Post Launch Test (PLT) airborne science field campaign. The GOES-R PLT airborne science field campaign took place in support of the post-launch product validation of the Advanced Baseline Imager (ABI) and the Geostationary Lightning Mapper (GLM). The LMA measures the arrival time of radiation from a lightning discharge at multiple stations and locates the sources of radiation to produce a three-dimensional map of total lightning activity. These data files are available in compressed ASCII files and are available from April 1, 2017 through June 1, 2017.",
-            "title": "GOES-R PLT Southern Ontario Lightning Mapping Array (LMA) V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FLMA%2FDATA601",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FLMA%2FDATA601",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltsolma",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltsolma",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GOESRPLT/DATA101",
-                    "description": "GOES-R PLT Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "GOES-R PLT Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GOESRPLT/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LMA/doc/goesrpltlma_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/LMA/doc/goesrpltlma_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/JC076i006p01478",
-                    "description": "A Hyperbolic System for Obtaining VHF Radio Pictures of Lightning",
                     "@type": "dcat:Distribution",
+                    "description": "A Hyperbolic System for Obtaining VHF Radio Pictures of Lightning",
+                    "downloadURL": "https://doi.org/10.1029/JC076i006p01478",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/JC086iC05p04041",
-                    "description": "VHF radio pictures of cloud flashes",
                     "@type": "dcat:Distribution",
+                    "description": "VHF radio pictures of cloud flashes",
+                    "downloadURL": "https://doi.org/10.1029/JC086iC05p04041",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/JD093iD10p12683",
-                    "description": "VHF radio pictures of lightning flashes to ground",
                     "@type": "dcat:Distribution",
+                    "description": "VHF radio pictures of lightning flashes to ground",
+                    "downloadURL": "https://doi.org/10.1029/JD093iD10p12683",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/1999GL010856",
-                    "description": "A GPS-based Three-Dimensional Lightning Mapping System: Initial Observations in Central New Mexico",
                     "@type": "dcat:Distribution",
+                    "description": "A GPS-based Three-Dimensional Lightning Mapping System: Initial Observations in Central New Mexico",
+                    "downloadURL": "https://doi.org/10.1029/1999GL010856",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2004JD004549",
-                    "description": "Accuracy of the Lightning Mapping Array",
                     "@type": "dcat:Distribution",
+                    "description": "Accuracy of the Lightning Mapping Array",
+                    "downloadURL": "https://doi.org/10.1029/2004JD004549",
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
+            "identifier": "C1980036345-GHRC_DAAC",
+            "issued": "2019-03-06",
+            "keyword": [
+                "earth science",
+                "atmospheric electricity",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOESRPLT/LMA/DATA601",
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
             "spatial": "-79.6164 43.656 -79.5964 43.676",
+            "temporal": "2017-04-01T00:00:00Z/2017-06-01T00:00:00Z",
             "theme": [
                 "GOES-R PLT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOES-R PLT Southern Ontario Lightning Mapping Array (LMA) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-12-09",
-            "temporal": "2021-12-09T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coords",
-                "iss",
-                "ephemeris",
-                "international",
-                "location",
-                "station",
-                "trajectory",
-                "coordinates",
-                "topo",
-                "space"
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
-            "identifier": "nasa-iss-data_2021-12-09_n6jz-ic78",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-12-09",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1121482,352 +1121458,359 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-12-09_n6jz-ic78",
+            "issued": "2021-12-09",
+            "keyword": [
+                "coords",
+                "iss",
+                "ephemeris",
+                "international",
+                "location",
+                "station",
+                "trajectory",
+                "coordinates",
+                "topo",
+                "space"
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
+            "temporal": "2021-12-09T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-12-09"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ERBE/S4G_MFOV_SF_ZG_L3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-06-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ERBE/S4G_MFOV_SF_ZG_L3.",
-            "issued": "1999-06-14",
-            "temporal": "1984-11-05T00:00:00Z/1990-02-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-12",
-            "keyword": [
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
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
-            "identifier": "C1000000772-LARC_ASDC",
             "description": "ERBE_S4G_MFOV_SF_ZG_1 is the Earth Radiation Budget Experiment (ERBE) Non-scanner S-4G Medium-field of View (MFOV) Shape Factor (SF) Zonal and Global Averages data product. Data collection for this product is complete. This data set consists of non-scanner, medium field-of-view data, which was processed using the shape factor data reduction technique. The data are averaged over latitudinal bands(zones) as well as on a global level in which each parameter is averaged over the entire globe. The zonal averages are available in 10.0 degree resolution. Monthly (day), monthly (hour), daily, and monthly hourly averages are determined for each region. The data are represented as 8-bit, 16-bit, and 32-bit integers.\r\n\r\nEarth Radiation Budget Experiment (ERBE) was a multi-satellite system designed to measure the Earth's radiation budget. ERBE instruments flew on a mid-inclination National Aeronautics and Space Administration (NASA) Earth Radiation Budget Satellite (ERBS) and two sun-synchronous National Oceanic and Atmospheric Administration (NOAA) satellites, NOAA-9 and NOAA-10. NOAA-9 and NOAA-10 provided global coverage and the ERBS provided coverage between 67.5 degrees north and south latitude. Each satellite carried both a scanner and a non-scanner instrument package. The non-scanner instrument contained four Earth-viewing channels and a solar monitor. The Earth-viewing channels had two spatial resolutions: a horizon-to-horizon view of the Earth, and a field-of-view limited to about 1000 km in diameter. The former was called the wide field-of-view (WFOV) and the latter the medium field of view (MFOV) channels. For each of the two fields of view, there was a total spectral channel which is sensitive to all wavelengths and a shortwave channel which used a high purity, fused silica filter dome to transmit only the shortwave radiation from 0.2 to 5 microns. Because of the concern for spectral flatness and high accuracy, all five channels on the non-scanner package were active cavity radiometers. The ERBE S-4G product contained averages of radiant flux and albedo on regional, zonal, and global scales. The data for the S-4G product were arranged by parameter values. The ERBE S-4G WFOV product was available as a combination of all operational spacecraft. Products have been archived from November 1984 - January 1985 and June 1989 - February 1990 for ERBS; February 1985 - October 1986 for ERBS/NOAA-9; November 1986 - January 1987 for ERBS/NOAA-9/NOAA-10; and February 1987 - May 1989 for ERBS/NOAA-10. The various combinations of the satellites reflected the actual duration of the scanners.",
-            "title": "Earth Radiation Budget Experiment (ERBE) Nonscanner S-4G MediumField of View (MFOV) Shape Factor (SF) Zonal and Global Averages",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS4G_MFOV_SF_ZG_L3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS4G_MFOV_SF_ZG_L3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ERBE/S4G_MFOV_SF_ZG_L3",
-                    "description": "DOI data set landing page for ERBE_S4G_MFOV_SF_ZG_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ERBE_S4G_MFOV_SF_ZG_1",
+                    "downloadURL": "https://doi.org/10.5067/ERBE/S4G_MFOV_SF_ZG_L3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000772-LARC_ASDC",
-                    "description": "Earthdata Search for ERBE_S4G_MFOV_SF_ZG_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ERBE_S4G_MFOV_SF_ZG_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000772-LARC_ASDC",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/rds4gnshdf.c",
-                    "description": "S-4G HDF NONSCANNER READ PROGRAM, Version 2.4 August 08, 1994 - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "S-4G HDF NONSCANNER READ PROGRAM, Version 2.4 August 08, 1994 - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/rds4gnshdf.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/rds4gnshdf.f",
-                    "description": "Makefile: contains the last line on which the \"address\" of the HDF library required at link time is found - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Makefile: contains the last line on which the \"address\" of the HDF library required at link time is found - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/rds4gnshdf.f",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_s4g.pdf",
-                    "description": "ERBE Regional, Zonal, and Global Gridded Averages Output Product (S-4G) Langley ASDC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "ERBE Regional, Zonal, and Global Gridded Averages Output Product (S-4G) Langley ASDC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/guide/erbe_s4g.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s4g_mfov_nf.txt",
-                    "description": "Read Software File for ERBE S-4G HDF Nonscanner Read Program",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software File for ERBE S-4G HDF Nonscanner Read Program",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s4g_mfov_nf.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s4g_sc_2.5_daacnotice.txt",
-                    "description": "Note for ERBE S-4G Data",
                     "@type": "dcat:Distribution",
+                    "description": "Note for ERBE S-4G Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s4g_sc_2.5_daacnotice.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/ERBE",
-                    "description": "NASA Earthdata Forum - ERBE Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - ERBE Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/ERBE",
+                    "mediaType": "text/html",
```

