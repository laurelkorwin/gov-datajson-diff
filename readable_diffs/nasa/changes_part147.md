# Change History for nasa.json (Part 147)

### Changes from 31606f9 to dd2190f (Part 136/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "This dataset contains the raw, preflight, thermal-vacuum calibration images collected by the Navigation Camera (NAVCAM) on 8-10 April 1998 for the Stardust mission. This is version 2.0 of the dataset, in which the original image data were converted from the standard PDS IMG format to the FITS format; no corrections were applied. The NExT mission to comet 9P/Tempel 1 used some of these preflight data to check the exposure time offsets due to shutter reversal and to determine dark current rates. This dataset supersedes version 1.0 which was safed by PDS because the data were not considered to be scientifically useful for the Stardust mission, due to problems encountered during the flight (stuck filter wheel, contamination on the instrument window, etc.) that changed the instrument characteristics.",
-            "title": "STARDUST NAVCAM RAW PREFLIGHT CALIBRATION IMAGES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "STARDUST NAVCAM RAW PREFLIGHT CALIBRATION IMAGES V2.0"
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
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120601.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-508",
+            "issued": "2018-06-25",
             "keyword": [
                 "crism",
                 "rss",
@@ -1429616,384 +1429625,376 @@
                 "sharad",
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
-            "identifier": "NASA-508",
-            "description": "CRISM, CTX, HiRISE, MARCI, MCS, RSS, SHARAD, SPICE",
-            "title": "PDS Mars Reconnaissance Orbiter Data 21",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120601.shtml",
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
+            "title": "PDS Mars Reconnaissance Orbiter Data 21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/N19_AVH02C1.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The Long-Term Data Record (LTDR) project. 2022-01-20. NOAA-19 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/N19_AVH02C1.006.",
-            "issued": "2022-10-23",
-            "temporal": "2009-05-31T00:00:00Z/2018-01-31T23:59:59.900Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-01",
-            "keyword": [
-                "land surface",
-                "atmosphere",
-                "infrared wavelengths",
-                "earth science",
-                "surface radiative properties",
-                "spectral/engineering",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2736284390-LAADS",
-            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe  NOAA-19 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05Deg CMG, short-name N19_ AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N19_ AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "The Long-Term Data Record (LTDR) project",
-            "title": "NOAA-19 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe  NOAA-19 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05Deg CMG, short-name N19_ AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N19_ AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FN19_AVH02C1.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FN19_AVH02C1.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ltdr.modaps.eosdis.nasa.gov/cgi-bin/ltdr/ltdrPage.cgi?fileName=docs",
-                    "description": "Overview of LTDR Products documents",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of LTDR Products documents",
+                    "downloadURL": "https://ltdr.modaps.eosdis.nasa.gov/cgi-bin/ltdr/ltdrPage.cgi?fileName=docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N19_AVH02C1--466",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N19_AVH02C1--466",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N19_AVH02C1/",
-                    "description": "Direct access to C6 N19_AVH02C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to C6 N19_AVH02C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N19_AVH02C1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/QA_WWW/forPage/user_guide/avhrr/LTDR_Ver5_Products_UserGuide_v1.0.pdf",
-                    "description": "A combined User's Guides for all L3 LTDR products",
                     "@type": "dcat:Distribution",
+                    "description": "A combined User's Guides for all L3 LTDR products",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/QA_WWW/forPage/user_guide/avhrr/LTDR_Ver5_Products_UserGuide_v1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C2736284390-LAADS",
+            "issued": "2022-10-23",
+            "keyword": [
+                "land surface",
+                "atmosphere",
+                "infrared wavelengths",
+                "earth science",
+                "surface radiative properties",
+                "spectral/engineering",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/N19_AVH02C1.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2009-05-31T00:00:00Z/2018-01-31T23:59:59.900Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-19 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V3.0",
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
+            "description": "This is a compilation of published lightcurve results up through 20 October, 1997. This compilation is maintained by Alan Harris, JPL.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v3.0_tqpx-rngu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-DERIVED-LIGHTCURVE-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-derived-lightcurve-v3.0_tqpx-rngu",
-            "description": "This is a compilation of published lightcurve results up through 20 October, 1997. This compilation is maintained by Alan Harris, JPL.",
-            "title": "ASTEROID LIGHTCURVE DERIVED DATA V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID LIGHTCURVE DERIVED DATA V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4CN71V6",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University. 2002-12-31. Last of the Wild Project, Version 1, 2002 (LWP-1): Global Human Footprint Dataset (Geographic). Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4CN71V6. https://doi.org/10.7927/H4CN71V6.",
-            "issued": "2002-12-31",
-            "temporal": "1992-01-01T00:00:00Z/1995-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4VM496V",
-                "https://doi.org/10.7927/H4QV3JG4",
-                "https://doi.org/10.7927/H47W694W",
-                "https://doi.org/10.7927/H4445JDG",
-                "https://doi.org/10.7927/H40C4SPR"
-            ],
-            "keyword": [
-                "land use/land cover",
-                "ecosystems",
-                "biosphere",
-                "land surface",
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
-            "identifier": "C179001934-SEDAC",
-            "description": "The Global Human Footprint Dataset of the Last of the Wild Project, Version 1, 2002 (LWP-1) is the Human Influence Index (HII) normalized by biome and realm. The HII is a global dataset of 1-kilometer grid cells, created from nine global data layers covering human population pressure (population density, population settlements), human land use and infrastructure (built up areas, nighttime lights, land use/land cover), and human access (coastlines, roads, railroads, navigable rivers). The dataset in Clarke 1866 Geographic Coordinate System is produced by the Wildlife Conservation Society (WCS) and the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Sample browse graphic of the data set.",
             "creator": "Wildlife Conservation Society - WCS, and Center for International Earth Science Information Network - CIESIN - Columbia University",
-            "title": "Last of the Wild Project, Version 1, 2002 (LWP-1): Global Human Footprint Dataset (Geographic)",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-human-footprint-geographic/sedac-logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Human Footprint Dataset of the Last of the Wild Project, Version 1, 2002 (LWP-1) is the Human Influence Index (HII) normalized by biome and realm. The HII is a global dataset of 1-kilometer grid cells, created from nine global data layers covering human population pressure (population density, population settlements), human land use and infrastructure (built up areas, nighttime lights, land use/land cover), and human access (coastlines, roads, railroads, navigable rivers). The dataset in Clarke 1866 Geographic Coordinate System is produced by the Wildlife Conservation Society (WCS) and the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4CN71V6",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4CN71V6",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-human-footprint-geographic/sedac-logo.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-human-footprint-geographic/sedac-logo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v1-human-footprint-geographic/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v1-human-footprint-geographic/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v1-human-footprint-geographic",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/wildareas-v1-human-footprint-geographic",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Sample browse graphic of the data set.",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/downloads/maps/wildareas-v1/wildareas-v1-human-footprint-geographic/sedac-logo.jpg",
+            "identifier": "C179001934-SEDAC",
+            "issued": "2002-12-31",
+            "keyword": [
+                "land use/land cover",
+                "ecosystems",
+                "biosphere",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4CN71V6",
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
+                "https://doi.org/10.7927/H4VM496V",
+                "https://doi.org/10.7927/H4QV3JG4",
+                "https://doi.org/10.7927/H47W694W",
+                "https://doi.org/10.7927/H4445JDG",
+                "https://doi.org/10.7927/H40C4SPR"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/1995-12-31T00:00:00Z",
             "theme": [
                 "LWP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Last of the Wild Project, Version 1, 2002 (LWP-1): Global Human Footprint Dataset (Geographic)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-ANAGLYPH-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-anaglyph-ops-v1.0_tqtv-vfyc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-ANAGLYPH-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-anaglyph-ops-v1.0_tqtv-vfyc",
-            "description": "NULL",
-            "title": "MER 1 MARS NAVIGATION CAMERA\n                                      ANAGLYPH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS NAVIGATION CAMERA\n                                      ANAGLYPH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/W2KXX0MYNJ9G",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge HiCARS 1 L1B Time-Tagged Echo Strength Profiles V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/W2KXX0MYNJ9G.",
-            "issued": "2009-01-02",
-            "temporal": "2009-01-02T00:00:00Z/2010-12-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2010-12-29",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "radar"
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
-            "identifier": "C1000001140-NSIDC_ECS",
             "description": "This data set contains Antarctica radar sounder echo strength profiles from the Hi-Capability Radar Sounder (HiCARS)  Version 1 instrument. The data were collected by scientists working on the Investigating the Cryospheric Evolution of the Central Antarctic Plate (ICECAP) project, which was funded by the National Science Foundation (NSF) and the Natural Environment Research Council (NERC) with additional support from NASA Operation IceBridge.",
-            "title": "IceBridge HiCARS 1 L1B Time-Tagged Echo Strength Profiles V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW2KXX0MYNJ9G",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FW2KXX0MYNJ9G",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/icebridge/portal/",
-                    "description": "Tool to visualize, search, and download IceBridge data.",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to visualize, search, and download IceBridge data.",
+                    "downloadURL": "http://nsidc.org/icebridge/portal/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IR1HI1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IR1HI1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001140-NSIDC_ECS&m=-59.949816515491705%21131.7677895930036%210%212%210%210%2C2&q=IR1HI1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001140-NSIDC_ECS&m=-59.949816515491705%21131.7677895930036%210%212%210%210%2C2&q=IR1HI1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IR1HI1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IR1HI1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/icebridge/portal/",
-                    "description": "Tool to visualize, search, and download IceBridge data.",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to visualize, search, and download IceBridge data.",
+                    "downloadURL": "http://nsidc.org/icebridge/portal/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IR1HI1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IR1HI1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001140-NSIDC_ECS&m=-59.949816515491705%21131.7677895930036%210%212%210%210%2C2&q=IR1HI1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001140-NSIDC_ECS&m=-59.949816515491705%21131.7677895930036%210%212%210%210%2C2&q=IR1HI1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IR1HI1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IR1HI1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W2KXX0MYNJ9G",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/W2KXX0MYNJ9G",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/W2KXX0MYNJ9G",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/W2KXX0MYNJ9G",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001140-NSIDC_ECS",
+            "issued": "2009-01-02",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/W2KXX0MYNJ9G",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2010-12-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2009-01-02T00:00:00Z/2010-12-29T23:59:59.999Z",
             "theme": [
                 "2008_AN_UTIG",
                 "2008_GR_UTIG",
@@ -1430015,535 +1430016,512 @@
                 "2016_GR_UTIG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge HiCARS 1 L1B Time-Tagged Echo Strength Profiles V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR11-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR11) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 23 and September 1, 2010, during the Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr11-v1.0_tqw2-6qgd",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR11-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr11-v1.0_tqw2-6qgd",
-            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR11) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 23 and September 1, 2010, during the Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR11 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SAGR11 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/51",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Markham, B. L., and C. L. Walthall. 1994. MMR Calibration Data (FIFE). Data set . Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration , Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/51",
-            "issued": "2024-05-05",
-            "temporal": "1987-06-06T00:00:00Z/1989-08-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "atmosphere",
-                "biosphere",
-                "vegetation",
-                "atmospheric radiation",
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
-            "identifier": "C2980103551-ORNL_CLOUD",
             "description": "Barnes MMR reflected radiance from calibration panels, adjusted for sun angle",
-            "graphic-preview-description": "Browse Image",
-            "title": "MMR Calibration Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F51",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F51",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_mmr_calb/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_sur_refl_mmr_calb/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/MMR_Calibration_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/MMR_Calibration_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/51",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/51",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_mmr_calb/comp/mmr_calb.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_mmr_calb/comp/mmr_calb.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_mmr_calb/comp/mmr_calb.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_mmr_calb/comp/mmr_calb.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_mmr_calb/comp/MMR_Calibration_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_sur_refl_mmr_calb/comp/MMR_Calibration_Data.pdf",
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
+            "identifier": "C2980103551-ORNL_CLOUD",
+            "issued": "2024-05-05",
+            "keyword": [
+                "atmosphere",
+                "biosphere",
+                "vegetation",
+                "atmospheric radiation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/51",
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
             "spatial": "-96.55 39.05 -96.54 39.09",
+            "temporal": "1987-06-06T00:00:00Z/1989-08-11T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MMR Calibration Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5KW5CZX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Baffin Bay Region Narwhal Research, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5KW5CZX.",
-            "issued": "2001-01-01",
-            "temporal": "2001-01-01T00:00:00Z/2006-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2006-06-30",
-            "keyword": [
-                "animals/vertebrates",
-                "earth science",
-                "biological classification"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Martin Nweeia",
                 "hasEmail": "mailto:martin_nweeia@hsdm.harvard.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206287-NSIDCV0",
             "description": "This data set highlights the research conducted by the Narwhal Tusk Research Project in Baffin Bay, between Canada and Greenland. Content includes laboratory and field studies directly investigating the physical and dental properties of the narwhal tusk, narwhal behavior, and an examination of the field expeditions and collected interviews from Inuit community members.",
-            "title": "Baffin Bay Region Narwhal Research, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5KW5CZX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5KW5CZX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://eloka-arctic.org/communities/narwhal/index.html",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "http://eloka-arctic.org/communities/narwhal/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5KW5CZX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5KW5CZX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5KW5CZX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5KW5CZX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206287-NSIDCV0",
+            "issued": "2001-01-01",
+            "keyword": [
+                "animals/vertebrates",
+                "earth science",
+                "biological classification"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5KW5CZX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2006-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-85.24028 62.69456 -51.37068 76.32567",
+            "temporal": "2001-01-01T00:00:00Z/2006-06-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Baffin Bay Region Narwhal Research, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-EXT3-67PCHURYUMOV-M33-V3.0",
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
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-ext3-67pchuryumov-m33-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-EXT3-67PCHURYUMOV-M33-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-ext3-67pchuryumov-m33-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Corrected START_TIME and STOP_TIME for BALLISTIC_STACKED images.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 EXT3-MTP033 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 EXT3-MTP033 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D51.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D51. Version 001. VIIRS/NPP BRDF/Albedo Valid Observation DNB Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D51.001. https://doi.org/10.5067/VIIRS/VNP43D51.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2019-11-07",
-            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-11-07",
-            "keyword": [
-                "earth science",
-                "land surface",
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
-            "identifier": "C1607332800-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Valid Observation Day/Night Band (DNB) product (VNP43D51) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer for each of the parameters included in the VNP43MA2 (https://doi.org/10.5067/VIIRS/VNP43MA2.001) product. VNP43D40 through VNP43D53 are the 30 arc second BRDF/Albedo Quality values, the Local Solar Noon values, the Valid Observations of the moderate resolution bands (M1 through M5, M7, M8, M10, and M11) plus the Day/Night Band (DNB), the Snow Status, and the Uncertainty. Details regarding methodology are available on the VNP43MA2 product page and in the Algorithm Theoretical Basis Document (ATBD). \r\n\r\nVNP43D51 contains the valid observation quality layer representing each of the 16 days of the retrieval period for VIIRS DNB.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D51",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo Valid Observation DNB Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Valid Observation Day/Night Band (DNB) product (VNP43D51) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer for each of the parameters included in the VNP43MA2 (https://doi.org/10.5067/VIIRS/VNP43MA2.001) product. VNP43D40 through VNP43D53 are the 30 arc second BRDF/Albedo Quality values, the Local Solar Noon values, the Valid Observations of the moderate resolution bands (M1 through M5, M7, M8, M10, and M11) plus the Day/Night Band (DNB), the Snow Status, and the Uncertainty. Details regarding methodology are available on the VNP43MA2 product page and in the Algorithm Theoretical Basis Document (ATBD). \r\n\r\nVNP43D51 contains the valid observation quality layer representing each of the 16 days of the retrieval period for VIIRS DNB.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D51.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D51.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D51.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D51.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D51.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D51.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607332800-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607332800-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D51.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D51.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D51",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D51",
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
+            "identifier": "C1607332800-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D51.001",
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
+            "series-name": "VNP43D51",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo Valid Observation DNB Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V8.0",
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
+            "description": "This data set includes names, designations, and discovery circumstances for the asteroids numbered as of April 18, 2004.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v8.0_tr93-jcfp",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V8.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v8.0_tr93-jcfp",
-            "description": "This data set includes names, designations, and discovery circumstances for the asteroids numbered as of April 18, 2004.",
-            "title": "ASTEROID NAMES AND DISCOVERY V8.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID NAMES AND DISCOVERY V8.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-PLUTOCRUISE-V2.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    Per the original mission plan for cruise operations, the PEPSSI            instrument was initially off for Pluto Cruise and only turned on           for functional tests and calibrations during Annual CheckOuts              (ACO); ACOs usually generate engineering data, but there is some           potential for science during those times. After extensive testing          in early 2012, in July of that year the project approved daily             science operations for the SWAP and PEPSSI instruments throughout          the rest of the cruise to Pluto.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-plutocruise-v2.0_trag-tqnh",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-PLUTOCRUISE-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-plutocruise-v2.0_trag-tqnh",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 2.0 of this data set.                    Per the original mission plan for cruise operations, the PEPSSI            instrument was initially off for Pluto Cruise and only turned on           for functional tests and calibrations during Annual CheckOuts              (ACO); ACOs usually generate engineering data, but there is some           potential for science during those times. After extensive testing          in early 2012, in July of that year the project approved daily             science operations for the SWAP and PEPSSI instruments throughout          the rest of the cruise to Pluto.                                           The changes in Version 2.0 were re-running of the ancillary data         in the data product, updated geometry from newer SPICE kernels,          minor editing of the documentation, catalogs, etc., and resolution       of liens from the December, 2014 review, plus those from the May,        2016 review of the Pluto Encounter data sets.                            New observations added with this version (V2.0) include ongoing          cruise observations from August, 2014 through January, 2015.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO CRUISE                                                     \n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO CRUISE                                                     \n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-SW-PA-6-TRAJ-1HR-V1.0",
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
+            "description": "Pioneer 11 plasma analyzer trajectory data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-sw-pa-6-traj-1hr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "pioneer 11"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-SW-PA-6-TRAJ-1HR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-sw-pa-6-traj-1hr-v1.0",
-            "description": "Pioneer 11 plasma analyzer trajectory data.",
-            "title": "P11 J SW PA 6 TRAJ 1HR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "P11 J SW PA 6 TRAJ 1HR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/LVEKYTNSRNKP",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "UW-Madison Space Science and Engineering Center: Hank Revercomb; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow. 2020-12-01. SNDRJ1CrISL1B. Version 3. JPSS-1 CrIS Level 1B Full Spectral Resolution V3. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/LVEKYTNSRNKP. https://disc.gsfc.nasa.gov/datacollection/SNDRJ1CrISL1B_3.html. Digital Science Data.",
-            "issued": "2018-02-16",
-            "temporal": "2018-01-05T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-26",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
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
-            "identifier": "C1952167461-GES_DISC",
-            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Full Spectral Resolution (FSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Joint Polar Satellite System-1 (JPSS-1) platform. This platform is also know as NOAA-20 (National Oceanic and Atmospheric Administration). The JPSS-1 mission with CrIS instrumentation is a follow-on to the Suomi National Polar-orbiting Partnership (SNPP)  mission. The CrIS instrumentation and data processing system is nearly identical to that of the SNPP satellite. \n\nCrIS is designed to be used with the ATMS (Advanced Technology Microwave Sounder) instrument. Processing the data from both of these instruments together is referred to as CrIMSS (Cross-Track Infrared and Microwave Sounder Suite).\n\n\nThe FSR files have 2,223 channels (*2211 apodized channels): 637 (*633) shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 869 (*865) midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 (*713)longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nIf you were redirected to this page from a DOI from an older version, please note this is the current version of the product. Please contact the GES DISC user support if you need information about previous data collections.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "SNDRJ1CrISL1B",
             "creator": "UW-Madison Space Science and Engineering Center: Hank Revercomb; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow",
-            "title": "JPSS-1 CrIS Level 1B Full Spectral Resolution V3 (SNDRJ1CrISL1B) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1CrISL1B_v3.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Full Spectral Resolution (FSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Joint Polar Satellite System-1 (JPSS-1) platform. This platform is also know as NOAA-20 (National Oceanic and Atmospheric Administration). The JPSS-1 mission with CrIS instrumentation is a follow-on to the Suomi National Polar-orbiting Partnership (SNPP)  mission. The CrIS instrumentation and data processing system is nearly identical to that of the SNPP satellite. \n\nCrIS is designed to be used with the ATMS (Advanced Technology Microwave Sounder) instrument. Processing the data from both of these instruments together is referred to as CrIMSS (Cross-Track Infrared and Microwave Sounder Suite).\n\n\nThe FSR files have 2,223 channels (*2211 apodized channels): 637 (*633) shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 869 (*865) midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 (*713)longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nIf you were redirected to this page from a DOI from an older version, please note this is the current version of the product. Please contact the GES DISC user support if you need information about previous data collections.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLVEKYTNSRNKP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLVEKYTNSRNKP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1430553,1011 +1430531,1035 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ1CrISL1B_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ1CrISL1B_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS1_Sounder_Level1/SNDRJ1CrISL1B.3/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS1_Sounder_Level1/SNDRJ1CrISL1B.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ1CrISL1B+3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ1CrISL1B+3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS1_Sounder_Level1/SNDRJ1CrISL1B.3/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS1_Sounder_Level1/SNDRJ1CrISL1B.3/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/JPSS-1/JPSS.CrIS.Sensor.Data.Record.ATBD.RevC.Code474_474-00032.pdf",
-                    "description": "Joint Polar Satellite System (JPSS) Cross Track Infrared Sounder (CrIS) Sensor Data Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) Cross Track Infrared Sounder (CrIS) Sensor Data Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/JPSS-1/JPSS.CrIS.Sensor.Data.Record.ATBD.RevC.Code474_474-00032.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/JPSS-1/CrIS_L1B_DeltaATBD_V3.0.pdf",
-                    "description": "NASA JPSS-1 and SNPP Cross Track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD).",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPSS-1 and SNPP Cross Track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/JPSS-1/CrIS_L1B_DeltaATBD_V3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Users_Guide_v3RevC.pdf",
-                    "description": "NASA Cross Track Infrared Sounder (CrIS) Level 1B Data Users\u2019 Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Cross Track Infrared Sounder (CrIS) Level 1B Data Users\u2019 Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Users_Guide_v3RevC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Quality_Flags_V3.pdf",
-                    "description": "NASA Cross Track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Cross Track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ1CrISL1B_v3.png",
+            "identifier": "C1952167461-GES_DISC",
+            "issued": "2018-02-16",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/LVEKYTNSRNKP",
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
+            "series-name": "SNDRJ1CrISL1B",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-05T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "JPSS-1 CrIS Level 1B Full Spectral Resolution V3 (SNDRJ1CrISL1B) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V10.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through March 2014. It includes some comets with Centaur orbits. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v10.0_trdg-ibe4",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "comet",
                 "asteroid"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-COLOR-V10.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-color-v10.0_trdg-ibe4",
-            "description": "This data set is intended to include published broadband colors of centaurs and Transneptunian Objects (TNOs) published through March 2014. It includes some comets with Centaur orbits. It supersedes all versions of the TNO colors data set EAR-A-3-RDR-TNO-PHOT.",
-            "title": "TNO AND CENTAUR COLORS V10.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TNO AND CENTAUR COLORS V10.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/keqj-x449",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cillaput: Our Weather, Yukon-Kuskowim Delta Weather Station Network, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. https://doi.org/10.7265/keqj-x449.",
-            "issued": "2018-02-16",
-            "temporal": "2018-02-16T00:00:00Z/2024-07-15T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
-            "keyword": [
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "earth science",
-                "cryosphere",
-                "atmosphere",
-                "frozen ground"
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
-            "identifier": "C2041284029-NSIDCV0",
             "description": "Cillaput: Our Weather, Yukon-Kuskowim Delta Weather Station Network provides access to current weather conditions in the villages of Chevak and Kotlik located in the Yukon-Kuskokwim Delta region of western Alaska. Measurements are collected hourly and include air temperature, humidity, wind speed, rainfall, solar radiation, and soil and surface temperatures. The weather stations were installed in late 2017 through a partnership between the Chevak Traditional Council, the US Geological Survey, and collaboration with the US Forest Service. The Cillaput data application displays the hourly conditions and graphs showing the past 24 hours of data. Users may download the data record by completing the user registration form on this page.",
-            "title": "Cillaput: Our Weather, Yukon-Kuskowim Delta Weather Station Network, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fkeqj-x449",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2Fkeqj-x449",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://eloka-arctic.org/cillaput/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "http://eloka-arctic.org/cillaput/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/keqj-x449",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/keqj-x449",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/keqj-x449",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/keqj-x449",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2041284029-NSIDCV0",
+            "issued": "2018-02-16",
+            "keyword": [
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science",
+                "cryosphere",
+                "atmosphere",
+                "frozen ground"
+            ],
+            "landingPage": "https://doi.org/10.7265/keqj-x449",
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
             "spatial": "-165.62 61.5 -163.56 63.02",
+            "temporal": "2018-02-16T00:00:00Z/2024-07-15T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Cillaput: Our Weather, Yukon-Kuskowim Delta Weather Station Network, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOESRPLT/AVIRIS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Olsen-Duvall, Winston .2019. GOES-R PLT Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GOESRPLT/AVIRIS/DATA101",
-            "issued": "2019-07-12",
-            "temporal": "2017-04-11T14:38:24Z/2017-05-14T19:22:07Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths",
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
-            "identifier": "C1979992256-GHRC_DAAC",
             "description": "The GOES-R PLT Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) dataset consists of radiance, reflectance, water phase, and navigation data delivered by the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) flown aboard the NASA ER-2 high-altitude aircraft during the GOES-R PLT field campaign. This field campaign took place from March through May 2017 in support of post-launch L1B and L2+ product validation of the Advanced Baseline Imager (ABI) and the Geostationary Lightning Mapper (GLM) satellite instruments. The GOES-R PLT AVIRIS data files are available from April 11, 2017 through May 14, 2017 in ASCII and binary formats along with browse imagery files in JPG format.",
-            "graphic-preview-description": "N/A",
-            "title": "GOES-R PLT Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/AVIRIS/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FAVIRIS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOESRPLT%2FAVIRIS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltaviris",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=goesrpltaviris",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/AVIRIS/browse/goesrplt_aviris_f20170507_t01p00r05_geo.jpg",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/AVIRIS/browse/goesrplt_aviris_f20170507_t01p00r05_geo.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aviris.jpl.nasa.gov/index.html",
-                    "description": "AVIRIS: Airborne Visible/Infrared Imaging Spectrometer",
                     "@type": "dcat:Distribution",
+                    "description": "AVIRIS: Airborne Visible/Infrared Imaging Spectrometer",
+                    "downloadURL": "https://aviris.jpl.nasa.gov/index.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/AVIRIS/doc/goesrpltaviris_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/AVIRIS/doc/goesrpltaviris_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1016/0034-4257(93)90014-O",
-                    "description": "Derivation of scaled surface reflectances from AVIRIS data",
                     "@type": "dcat:Distribution",
+                    "description": "Derivation of scaled surface reflectances from AVIRIS data",
+                    "downloadURL": "https://doi.org/10.1016/0034-4257(93)90014-O",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1016/S0034-4257(98)00064-9",
-                    "description": "Imaging Spectroscopy and the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS)",
                     "@type": "dcat:Distribution",
+                    "description": "Imaging Spectroscopy and the Airborne Visible/Infrared Imaging Spectrometer (AVIRIS)",
+                    "downloadURL": "https://doi.org/10.1016/S0034-4257(98)00064-9",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1016/j.rse.2006.03.002",
-                    "description": "Reflectance quantities in optical remote sensing \u2014 definitions and case studies",
                     "@type": "dcat:Distribution",
+                    "description": "Reflectance quantities in optical remote sensing \u2014 definitions and case studies",
+                    "downloadURL": "https://doi.org/10.1016/j.rse.2006.03.002",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/goes-r-post-launch-test-plt",
-                    "description": "GOES-R PLT Field Campaign Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "GOES-R PLT Field Campaign Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/goes-r-post-launch-test-plt",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/AVIRIS/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/AVIRIS/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/goesrplt/AVIRIS/browse/",
+            "identifier": "C1979992256-GHRC_DAAC",
+            "issued": "2019-07-12",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOESRPLT/AVIRIS/DATA101",
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
             "spatial": "-118.198 26.449 -72.2016 43.5726",
+            "temporal": "2017-04-11T14:38:24Z/2017-05-14T19:22:07Z",
             "theme": [
                 "GOES-R PLT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOES-R PLT Airborne Visible/Infrared Imaging Spectrometer (AVIRIS) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AMSRU/AU_SI12_NRT_R04",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Meier, Walt, Josefino C Comiso, and Thorsten Markus.2019. NRT AMSR2 Unified L3 Daily 12.5 km Brightness Temperature & Sea Ice Concentration [indicate subset used]. Dataset available online from the NASA Global Hydrology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/AMSRU/AU_SI12_NRT_R04",
-            "issued": "2020-06-30",
-            "temporal": "2020-06-29T08:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-30",
-            "keyword": [
-                "microwave",
-                "oceans",
-                "spectral/engineering",
-                "sea ice",
-                "earth science",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-ghrc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C1886605827-LANCEAMSR2",
             "description": "The Advanced Microwave Scanning Radiometer 2 (AMSR2) instrument on the Global Change Observation Mission - Water 1 (GCOM-W1) provides global passive microwave measurements of terrestrial, oceanic, and atmospheric parameters for the investigation of global water and energy cycles. Near real-time (NRT) products are generated within 3 hours of the last observations in the file, by the Land Atmosphere Near real-time Capability for EOS (LANCE) at the AMSR Science Investigator-led Processing System (AMSR SIPS), which is collocated with the Global Hydrology Resource Center (GHRC) DAAC.  The NRT AMSR2 Unified L3 Daily 12.5 km Brightness Temperature & Sea Ice Concentration, Version 4 uses as input the resampled brightness temperature (Level-1R) data provided by the Japanese Aerospace Exploration Agency (JAXA).  The Version 4 dataset uses the AMSR-U2 product generation algorithm with slight modifications for NRT product generation, same algorithm used to generation the standard, science quality, data that is available at the NSIDC DAAC.  This Level-3 gridded product includes brightness temperatures at 89.0 GHz. Data are mapped to a polar stereographic grid at 12.5 km spatial resolution. Sea ice concentration and brightness temperatures include daily ascending averages, daily descending averages, and daily averages. Data are stored in HDF-EOS5 format and are available via HTTP from the EOSDIS LANCE system at https://lance.nsstc.nasa.gov/amsr2-science/data/level3/seaice12.  If data latency is not a primary concern, please consider using science quality products. Science products are created using the best available ancillary, calibration and ephemeris information. Science quality products are an internally consistent, well-calibrated record of the Earth's geophysical properties to support science. These standard product, science quality, are available at the NSIDC DAAC: https://nsidc.org/",
-            "graphic-preview-description": "Sample browse image",
-            "title": "NRT AMSR2 Unified L3 Daily 12.5 km Brightness Temperature & Sea Ice Concentration V4",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_SI12.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSRU%2FAU_SI12_NRT_R04",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAMSRU%2FAU_SI12_NRT_R04",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lance.nsstc.nasa.gov/amsr2-science/data/level3/seaice12/R04/hdfeos5/",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://lance.nsstc.nasa.gov/amsr2-science/data/level3/seaice12/R04/hdfeos5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lance.itsc.uah.edu/amsr2-science/data/level3/seaice12/R04/hdfeos5/",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://lance.itsc.uah.edu/amsr2-science/data/level3/seaice12/R04/hdfeos5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LANCE"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?l=MODIS_Terra_CorrectedReflectance_TrueColor%2CAMSRU2_Sea_Ice_Concentration_12km%2CCoastlines",
-                    "description": "Interactively browse imagery in EOSDIS Worldview",
                     "@type": "dcat:Distribution",
+                    "description": "Interactively browse imagery in EOSDIS Worldview",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?l=MODIS_Terra_CorrectedReflectance_TrueColor%2CAMSRU2_Sea_Ice_Concentration_12km%2CCoastlines",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/all-data-recipes#drp-formatcon",
-                    "description": "Data Format Conversion Recipes",
                     "@type": "dcat:Distribution",
+                    "description": "Data Format Conversion Recipes",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/all-data-recipes#drp-formatcon",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_SI12.jpg",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_SI12.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/au_si12/versions/1",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://nsidc.org/data/au_si12/versions/1",
+                    "mediaType": "text/html",
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
+            "graphic-preview-description": "Sample browse image",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/lance/AMSR_U2_SI12.jpg",
+            "identifier": "C1886605827-LANCEAMSR2",
+            "issued": "2020-06-30",
+            "keyword": [
+                "microwave",
+                "oceans",
+                "spectral/engineering",
+                "sea ice",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AMSRU/AU_SI12_NRT_R04",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
             "spatial": "-180.0 -89.0 180.0 89.0",
+            "temporal": "2020-06-29T08:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "LANCE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NRT AMSR2 Unified L3 Daily 12.5 km Brightness Temperature & Sea Ice Concentration V4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.7-color-survey&version=1.0",
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
-                "multiple asteroids",
-                "none"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Seven-color Asteroid Survey (SCAS)   consists of photometry in seven filters from 0.9 to 2.3 microns, of a  total of 126 asteroids of types S, K, and M.",
+            "identifier": "urn:nasa:pds:gbo.ast.7-color-survey",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple asteroids",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.7-color-survey&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.7-color-survey",
-            "description": "The Seven-color Asteroid Survey (SCAS)   consists of photometry in seven filters from 0.9 to 2.3 microns, of a  total of 126 asteroids of types S, K, and M.",
-            "title": "SEVEN COLOR ASTEROID SURVEY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "SEVEN COLOR ASTEROID SURVEY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/LOBO_TIMESERIES/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/LOBO_TIMESERIES/DATA001.",
-            "issued": "2009-03-30",
-            "temporal": "2009-03-30T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "salinity/density",
-                "ocean temperature",
-                "oceans",
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
-            "identifier": "C1633360450-OB_DAAC",
             "description": "Measurements made near Dartmouth, Nova Scotia in 2009.",
-            "title": "Land/Ocean Biogeochemical Observatory (LOBO) water quality monitoring system timeseries",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLOBO_TIMESERIES%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FLOBO_TIMESERIES%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/LOBO_timeseries/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/LOBO_timeseries/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360450-OB_DAAC",
+            "issued": "2009-03-30",
+            "keyword": [
+                "ocean optics",
+                "salinity/density",
+                "ocean temperature",
+                "oceans",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/LOBO_TIMESERIES/DATA001",
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
+            "temporal": "2009-03-30T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Land/Ocean Biogeochemical Observatory (LOBO) water quality monitoring system timeseries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR17-V1.0",
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
+            "description": "The Cassini Radio Science Rhea Gravity Science Experiment (TIGR17) Raw Data Archive is a time-ordered collection of radio science raw data acquired on February 15, 16 and 17, 2013, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr17-v1.0_trt7-f5ex",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR17-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr17-v1.0_trt7-f5ex",
-            "description": "The Cassini Radio Science Rhea Gravity Science Experiment (TIGR17) Raw Data Archive is a time-ordered collection of radio science raw data acquired on February 15, 16 and 17, 2013, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR17 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - TIGR17 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1717",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sweeney, C., K. McKain, B.R. Miller, and S.E. Michel. 2019. ABoVE: Atmospheric Gas Concentrations from Airborne Flasks, Arctic-CAP, 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1717",
-            "issued": "2022-05-10",
-            "temporal": "2017-04-27T00:00:00Z/2017-11-04T23:59:59Z",
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
-            "identifier": "C2143812247-ORNL_CLOUD",
             "description": "This dataset provides atmospheric carbon dioxide (CO2), methane (CH4), carbon monoxide (CO), molecular hydrogen (H2), nitrous oxide (N2O), sulfur hexafluoride (SF6), and other trace gas mole fractions (i.e. \"concentrations\") from flights over Alaska and the Yukon and Northwest Territories of Canada during the Arctic Carbon Aircraft Profile (Arctic-CAP) monthly sampling campaigns from April-November 2017. The data were derived from laboratory measurements of whole air samples collected by Programmable Flask Packages (PFP) onboard the aircraft. During each of the six monthly campaigns, flights over the Arctic-Boreal Vulnerability Experiment (ABoVE) domain included 25 vertical profiles, from the surface up to 6 km altitude, at locations selected to complement regular long-term vertical profiles, remote sensing data, and ground-based flux tower measurements. Measurements were initiated by the aircraft pilot at predetermined locations within each profile in order to evenly distribute flask sampling points throughout each flight. A total of 408 flask samples were collected during 55 individual flights. The measurements included in this data set are crucial for understanding changes in Arctic carbon cycling and the potential threats posed by thawing of Arctic permafrost.",
-            "graphic-preview-description": "Arctic-CAP flight lines (orange) sample Arctic and boreal regions of Alaska and the Yukon and the Northwest Territories of Canada. Monthly campaigns extended from April through November, capturing the carbon dynamics of the 2017 growing season. Pins mark the locations of the 25 vertical profiles acquired during each monthly campaign. Source: Scientific Aviation, 2019.",
-            "title": "ABoVE: Atmospheric Gas Concentrations from Airborne Flasks, Arctic-CAP, 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Atmospheric_Flask_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1717",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1717",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_Atmospheric_Flask_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_Atmospheric_Flask_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Atmospheric_Flask_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Atmospheric_Flask_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1717",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1717",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_Atmospheric_Flask_Data/comp/ABoVE_Atmospheric_Flask_Data.pdf",
-                    "description": "ABoVE: Atmospheric Gas Concentrations, Airborne Flasks, Arctic-CAP, 2017: ABoVE_Atmospheric_Flask_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Atmospheric Gas Concentrations, Airborne Flasks, Arctic-CAP, 2017: ABoVE_Atmospheric_Flask_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_Atmospheric_Flask_Data/comp/ABoVE_Atmospheric_Flask_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_Atmospheric_Flask_Data/comp/sample_analysis_per_noaa_instaar_group.zip",
-                    "description": "ABoVE: Atmospheric Gas Concentrations, Airborne Flasks from Arctic-CAP, 2017: sample_analysis_per noaa_instaar_group.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Atmospheric Gas Concentrations, Airborne Flasks from Arctic-CAP, 2017: sample_analysis_per noaa_instaar_group.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_Atmospheric_Flask_Data/comp/sample_analysis_per_noaa_instaar_group.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Atmospheric_Flask_Data_Fig1.png",
-                    "description": "Arctic-CAP flight lines (orange) sample Arctic and boreal regions of Alaska and the Yukon and the Northwest Territories of Canada. Monthly campaigns extended from April through November, capturing the carbon dynamics of the 2017 growing season. Pins mark the locations of the 25 vertical profiles acquired during each monthly campaign. Source: Scientific Aviation, 2019.",
                     "@type": "dcat:Distribution",
+                    "description": "Arctic-CAP flight lines (orange) sample Arctic and boreal regions of Alaska and the Yukon and the Northwest Territories of Canada. Monthly campaigns extended from April through November, capturing the carbon dynamics of the 2017 growing season. Pins mark the locations of the 25 vertical profiles acquired during each monthly campaign. Source: Scientific Aviation, 2019.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Atmospheric_Flask_Data_Fig1.png",
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
+            "graphic-preview-description": "Arctic-CAP flight lines (orange) sample Arctic and boreal regions of Alaska and the Yukon and the Northwest Territories of Canada. Monthly campaigns extended from April through November, capturing the carbon dynamics of the 2017 growing season. Pins mark the locations of the 25 vertical profiles acquired during each monthly campaign. Source: Scientific Aviation, 2019.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Atmospheric_Flask_Data_Fig1.png",
+            "identifier": "C2143812247-ORNL_CLOUD",
+            "issued": "2022-05-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1717",
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
             "spatial": "-165.48 58.08 -111.57 71.27",
+            "temporal": "2017-04-27T00:00:00Z/2017-11-04T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Atmospheric Gas Concentrations from Airborne Flasks, Arctic-CAP, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_jValue_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-08-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_jValue_AircraftInSitu_DC8_Data_1.",
-            "issued": "1997-10-07",
-            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-11-12",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Shetter",
                 "hasEmail": "mailto:shetter@ucar.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2662394953-LARC_ASDC",
             "description": "SONEX_jValue_AircraftInSitu_DC8_Data_1 is the photolysis frequencies (j-values) measured along the DC-8 flight by the Scanning Actinic Flux Spectroradiometers (SAFS). Data collection is complete.\r\n\r\nThe SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) was an international, multi-organizational mission that took place in October-November 1997. NASA was the US sponsor of SONEX that partnered with POLINAT-2 (Pollution from Aircraft Emissions in the North Atlantic Flight Corridor) funded by the German DLR (Deutsches Zentrum f\u00fcr Luft- und Raumfahrt) or German Aerospace Agency. NASA flew the DC-8 aircraft out of NASA/Ames Research Center. DLR operated an instrumented Falcon 20 aircraft. The staging locations for NAFC sampling were primarily Bangor, Maine (US), and Shannon, Ireland. Subsonic aircraft emissions impact several aspects of atmospheric composition: nitrogen oxides (NOx), CO, and hydrocarbons from emissions can perturb upper tropospheric/lower stratospheric (UT/LS) ozone; water vapor, soot, and sulfur oxides (SOx) emitted by aircraft may perturb clouds and aerosols, changing UT/LS radiative forcing and global temperature.\r\nIn SONEX and POLINAT, flights were conducted in the vicinity of the North Atlantic Flight Coordinator (NAFC) to observe the impact of aircraft emissions on NOx and ozone (O3). The DC-8 aircraft payload (Singh et al., 1999) primarily measured in-situ CO, CO2, hydrocarbons/halocarbons, O3, aerosols (Dibb et al., 2000), OH/HO2, water vapor, nitric acid (Talbot et al., 1999), photolysis rates, temperature, pressure, winds, NOx, and NOy.\r\nThree sampling approaches were implemented during SONEX. First, special meteorological (Fuelberg et al., 2000) were developed to allow targeted sampling for air parcels affected by aircraft emissions and various meteorological events, e.g., convection, lightning (Jeker et al., 2000), stratospheric intrusions (Cho et al., 2000). Second, because the NAFC had not been extensively sampled in the past, it was important for SONEX to characterize the climatology of trace species like CN (Wang et al., 2000), NOx and NOy (Koike et al., 2000). Third, tracers (Simpson et al., 2000; Thompson et al., 1999) and model sensitivity studies (Meijer et al., 2000) were employed for Air Mass Identification. This sampling strategy answered the following questions: Where and when are air masses found with the greatest aircraft influence? When and where was stratospheric air sampled? SONEX showed a substantial impact of aircraft emissions on UT/LS NOx and CN in the vicinity of fresh aircraft emissions. However, during October-November 1997 over the NAFC, UT/LS NOx was dominated by surface emissions redistributed by convection and augmented by lightning.",
-            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) Photolysis Frequencies (J-Values)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_jValue_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_jValue_AircraftInSitu_DC8_Data_1",
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
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2662394953-LARC_ASDC",
-                    "description": "Earthdata Search client for SONEX_jValue_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for SONEX_jValue_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2662394953-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_jValue_AircraftInSitu_DC8_Data_1",
-                    "description": "DOI for SONEX_jValue_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SONEX_jValue_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_jValue_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/SONEX_jValue_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SONEX_jValue_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SONEX_jValue_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/SONEX_jValue_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2662394953-LARC_ASDC",
+            "issued": "1997-10-07",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_jValue_AircraftInSitu_DC8_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.89 -129.403 19.89 13.023 69.127 13.023 69.127 -129.403 19.89 -129.403</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-10-07T00:00:00Z/1997-11-13T23:59:59.999Z",
             "theme": [
                 "SONEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) Photolysis Frequencies (J-Values)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL13QL.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data Quick Look V006. Version 006. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL13QL.006.",
-            "issued": "2024-08-30",
-            "temporal": "2024-08-30T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "earth science",
-                "terrestrial hydrosphere",
-                "surface water"
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
-            "identifier": "C2650092501-NSIDC_ECS",
             "description": "ATL13QL is the quick look version of ATL13. Once final ATL13 files are available the corresponding ATL13QL files will be removed. ATL13 contains along-track surface water products for inland water bodies. Inland water bodies include lakes, reservoirs, rivers, bays, estuaries and a 7 km near-shore buffer. Principal data products include the along-track water surface height and standard deviation, subsurface signal (532 nm) attenuation, significant wave height, wind speed, and coarse depth to bottom topography (where data permit).",
-            "title": "ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data Quick Look V006",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL13QL.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL13QL.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL13QL.006/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL13QL.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL13QL+V006",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL13QL+V006",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL13QL/versions/6/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL13QL/versions/6/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL13QL.006",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL13QL.006",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL13QL.006",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL13QL.006",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2650092501-NSIDC_ECS",
+            "issued": "2024-08-30",
+            "keyword": [
+                "earth science",
+                "terrestrial hydrosphere",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL13QL.006",
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
+            "temporal": "2024-08-30T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3A Along Track Inland Surface Water Data Quick Look V006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-ESC1-MTP012-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the COMET ESCORT 1 MTP012 Phase from 14 Jan. 2015, 04:19:32 to 10 Feb. 2015, 23:22:55 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-esc1-mtp012-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-3-ESC1-MTP012-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-3-esc1-mtp012-v1.0",
-            "description": "This dataset contains ROSETTA NAVCAM RADIOMETRICALLY CALIBRATED DATA of the COMET ESCORT 1 MTP012 Phase from 14 Jan. 2015, 04:19:32 to 10 Feb. 2015, 23:22:55 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 3 COMET ESCORT 1 MTP012 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 3 COMET ESCORT 1 MTP012 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M26-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m26-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67P-M26-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67p-m26-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 1 mission phase, covering the period  from 2016-02-09T23:25:00.000 to 2016-03-08T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP026 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP026 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-5-DDR-ENERGETIC-ION-COMP-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set provides energetic (MeV) ion fluxes for a variety of different Z values (carbon, oxygen, sulfur) derived from the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. The data set includes all recorded intervals at Jupiter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-5-ddr-energetic-ion-comp-v1.0_ts78-dn2w",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "jupiter",
                 "amalthea",
@@ -1431568,653 +1431570,630 @@
                 "io",
                 "io plasma torus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-5-DDR-ENERGETIC-ION-COMP-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-5-ddr-energetic-ion-comp-v1.0_ts78-dn2w",
-            "description": "This data set provides energetic (MeV) ion fluxes for a variety of different Z values (carbon, oxygen, sulfur) derived from the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. The data set includes all recorded intervals at Jupiter.",
-            "title": "GO JUP HIC DERIVED ENERGETIC ION COMPOSITION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO JUP HIC DERIVED ENERGETIC ION COMPOSITION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DAER_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2006-03-13. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Terra/MISR/MI3DAER_L3.002. https://asdc.larc.nasa.gov/project/MISR.",
-            "issued": "2006-02-13",
-            "temporal": "2002-03-29T00:00:00Z/2007-08-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "aerosols",
-                "air quality",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C179031513-LARC",
             "description": "MI3DAER_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 3 Component Global Aerosol Regional public Product covering a day version 2. It contains a statistical summary of column aerosol 555 nanometer optical depth, and a monthly aerosol compositional type frequency histogram. This data product is a global summary of the Level 2 aerosol parameters of interest averaged over a day and reported on a geographic grid, with resolution of 0.5 degree by 0.5 degree. Data collection for this product is complete. The data are for distinct regions associated with associated field campaigns. The MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward, and four cameras pointing aftward. It takes seven minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally Gaussian, centered at 443, 555, 670, and 865 nm.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Component Global Aerosol Regional public Product covering a day V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DAER_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3DAER_L3.002",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031513-LARC",
-                    "description": "Earthdata Search for MI3DAER_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MI3DAER_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C179031513-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3DAER.002/contents.html",
-                    "description": "OPeNDAP data access for MI3DAER_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MI3DAER_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3DAER.002/contents.html",
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
-                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MI3DAER_L3.002",
-                    "description": "DOI data set landing page for MI3DAER_2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MI3DAER_2",
+                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MI3DAER_L3.002",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3DAER.002/",
-                    "description": "ASDC Direct Data Download for MI3DAER_2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MI3DAER_2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3DAER.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_CGAS_V032.20180125.pdf",
-                    "description": " Data Product Specification for the MISR Level 3 Component Global Aerosol Product - Incorporating the Science Data Processing Interface Control Document",
                     "@type": "dcat:Distribution",
+                    "description": " Data Product Specification for the MISR Level 3 Component Global Aerosol Product - Incorporating the Science Data Processing Interface Control Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_CGAS_V032.20180125.pdf",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_JOINT_AS_Product.pdf",
-                    "description": "MISR Level 3 Joint Aerosol Product Quality Statement - October 15, 2012",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 3 Joint Aerosol Product Quality Statement - October 15, 2012",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_JOINT_AS_Product.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
+            "identifier": "C179031513-LARC",
+            "issued": "2006-02-13",
+            "keyword": [
+                "aerosols",
+                "air quality",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3DAER_L3.002",
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
+            "temporal": "2002-03-29T00:00:00Z/2007-08-30T23:59:59Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Component Global Aerosol Regional public Product covering a day V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0269-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-03T17:56:15.000 to 2014-09-04T00:30:14.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0269-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0269-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0269-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-03T17:56:15.000 to 2014-09-04T00:30:14.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0269 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0269 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D66.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D66. Version 001. VIIRS/NPP BRDF/Albedo BSA at Solar Noon DNB Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D66.001. https://doi.org/10.5067/VIIRS/VNP43D66.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
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
-            "identifier": "C1607338680-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Black-Sky Albedo for DNB (VNP43D66) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D66 is the BSA for the VIIRS DNB (0.7 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D66",
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo BSA at Solar Noon DNB Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Black-Sky Albedo for DNB (VNP43D66) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D66 is the BSA for the VIIRS DNB (0.7 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D66.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D66.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D66.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D66.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D66.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D66.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607338680-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607338680-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D66.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D66.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D66",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D66",
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
+            "identifier": "C1607338680-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D66.001",
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
+            "series-name": "VNP43D66",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo BSA at Solar Noon DNB Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-SLOPE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-slope-ops-v1.0_tshg-pm2r",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-SLOPE-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-slope-ops-v1.0_tshg-pm2r",
-            "description": "not applicable",
-            "title": "MER 1 MARS NAVIGATION CAMERA SLOPE RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS NAVIGATION CAMERA SLOPE RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1270-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-20T01:36:25.000 to 2015-12-20T06:43:34.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1270-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1270-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1270-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-20T01:36:25.000 to 2015-12-20T06:43:34.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1270 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1270 V1.0"
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
-                "ask the academy",
-                "sharing",
-                "knowledge"
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
-            "identifier": "NASA-862__34",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1432222,393 +1432201,393 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__34",
+            "issued": "2018-06-25",
+            "keyword": [
+                "appel",
+                "ask the academy",
+                "sharing",
+                "knowledge"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1372-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-26T09:26:40.000 to 2016-01-26T13:26:12.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1372-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1372-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1372-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-26T09:26:40.000 to 2016-01-26T13:26:12.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1372 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1372 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0055",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0055.",
-            "issued": "1999-11-03",
-            "temporal": "1992-06-01T00:00:00Z/1992-06-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
-            "keyword": [
-                "atmospheric winds",
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric temperature"
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
-            "identifier": "C1000001039-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.SOFIA (Surface of the Ocean, Fluxes and Interaction with the Atmosphere) is a research program carried out by French groups from the Centre de Recherches en Physique de l'Environnement (CRPE), Laboratoire l'Aerologie (LA)-Toulouse, Centre de Meteorologie Marine (CMM)-Brest, Institut Francais de Rechercher sur la Mer (IFREMER)-Brest, Service d'Aeronomie-Paris, and Laboratoire de Meteorologie Dynamique (LMD)-Palaiseau with cooperation from Centre National de Recherche Meteorologique (CNRM)-Toulouse. The scientific objective of SOFIA during ASTEX was the study of energy transfer (heat, humidity and momentum fluxes) between the sea surface and the atmospheric boundary layer at scales ranging from the local scale to the mesoscale (50 km). The general concept of the program was to develop a measurement strategy based on nested boxes in which instrumentation would be used to estimate and quantify fluxes. These instruments, from which flux estimates at different scales would be measured, were used in connection with satellite measurements to understand and, hence, to validate the satellite integration of fluxes, particularly in the presence of mesoscale oceanic and atmospheric structures responsible for spatial inhomogeneity of fluxes. The FOKKER F27 aircraft with flux measurement package and the airborne Lidar Leandre was used during ASTEX. The FOKKER 27 ARAT capabilities were as follows: * Turbulence measurements of wind, temperature and moisture. Fast response sensors located on a nose boom 5m long, which measured - attack and sideslip angles by mobile vanes and by a five hole probe (Rosemound 858). - true airspeed by a Pitot probe - temperature by a fast response INSU probe - humidity by a Lyman-alpha humidity meter * Mean state sensors - Rosemount temperature probe - Reverse-flow temperature probe - General Eastern dew point sensor * Aerosols and cloud microphysics - 1-D drop size measurements from 0-6000 microns by four Knollenberg sensors - 2-D sensor OAP 2DC for drop sizes between 25 and 800 microns * Liquid water content - Johnson-Williams sensors * Radiative measurements, up- and downward - Longwave (14-40 microns) Eppley radiometers - Shortwave (0.2-2.8 microns) Eppley radiometers - Radiances (7.8-14 microns) Barnes PRT5 radiometers * Chemical measurements(isokinetic veins) * Pointint backscatter lidar (Leandre) * Directional reflectances meausrements (POLDER- Polarized Direct Reflectance)",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) SOFIA ARAT Fokker F27 Aircraft Turbulence",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0055",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0055",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001039-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_SOF_ARAT_TRB_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_SOF_ARAT_TRB_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001039-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0055",
-                    "description": "DOI data set landing page for FIRE_AX_SOF_ARAT_TRB_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_SOF_ARAT_TRB_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0055",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_SOF_ARAT_TRB/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_SOF_ARAT_TRB_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_SOF_ARAT_TRB_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_SOF_ARAT_TRB/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_SOF_ARAT_TRB/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_SOF_ARAT_TRB_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_SOF_ARAT_TRB_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_SOF_ARAT_TRB/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001039-LARC_ASDC",
+            "issued": "1999-11-03",
+            "keyword": [
+                "atmospheric winds",
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0055",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>34.69 -34.11 34.69 120.25 38.37 120.25 38.37 -34.11 34.69 -34.11</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-01T00:00:00Z/1992-06-20T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) SOFIA ARAT Fokker F27 Aircraft Turbulence"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-EXT3-V1.0",
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
+            "description": "This data set contains CODMAC\nlevel 4 science data acquired by the ROSINA COPS sensor between\n2016-06-28 and 2016-06-30 during the Extension phase 3 of the\nRosetta mission to comet 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-ext3-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-ext3-v1.0",
-            "description": "This data set contains CODMAC\nlevel 4 science data acquired by the ROSINA COPS sensor between\n2016-06-28 and 2016-06-30 during the Extension phase 3 of the\nRosetta mission to comet 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 4 EXT3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P ROSINA 4 EXT3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0048",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2006-11-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0048.",
-            "issued": "2013-11-14",
-            "temporal": "2000-10-12T00:00:00Z/2006-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "aerosols",
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
-            "identifier": "C2324345309-LARC_ASDC",
             "description": "The NARSTO_EPA_SS_FRESNO_PM25_NO3_SO4 is the North American Research Strategy for Tropospheric Ozone (NARSTO) Environmental Protection Agency (EPA) Supersite (SS) Fresno, Particulate Matter (PM) 2.5 Particulate Nitrate and Sulfate Data. This data set contains measurements taken from two nitrate monitors and one sulfate monitor operated at the Fresno Supersite. The sample collection time for all instruments was 8 minutes. The sample analysis time was 2 minutes. Data were output once every 10 minutes. The Rupprecht and Patashnick (R&P) Ambient Particulate Nitrate Monitor measured the amount of particulate nitrate in an air sample at a nearly continuous rate. The Rupprecht and Patashnick (R&P) Ambient Particulate Sulfate Monitor measured the amount of particulate sulfate in an air sample at a nearly continuous rate. The ambient aerosol was collected by impaction on a small metallic strip. At the end of collection, the strip was heated to vaporize and decompose the particulate matter into oxides which were then measured. \r\n\r\nThe Fresno Supersite is one of several Supersites established in urban areas within the United States by the EPA to better understand the measurement, sources, and health effects of suspended particulate matter (PM). The site is located at 3425 First Street, approximately 1 km north of the downtown commercial district. First Street was a four-lane artery with moderate traffic levels. Commercial establishments, office buildings, churches, and schools were located north and south of the monitor. Medium-density single-family homes and some apartments were located in the blocks to the east and west of First Street. The Fresno Supersite began operation in May of 1999.The EPA PM Supersites Program was an ambient air monitoring research program designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. \r\n\r\nEight geographically diverse projects were chosen to specifically address the following EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods.\r\n\r\nNARSTO, which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO EPA Supersite (SS) Fresno, Particulate Matter (PM) 2.5 Particulate Nitrate and Sulfate Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0048",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0048",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2324345309-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_FRESNO_PM25_NO3_SO4_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_FRESNO_PM25_NO3_SO4_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2324345309-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0048",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_FRESNO_PM25_NO3_SO4_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_FRESNO_PM25_NO3_SO4_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0048",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_fresno_pm25_no3_so4.pdf",
-                    "description": "Guide for NARSTO EPA_SS_FRESNO PM2.5 Particulate Nitrate and Sulfate Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_FRESNO PM2.5 Particulate Nitrate and Sulfate Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_fresno_pm25_no3_so4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Fresno_Final_Report.pdf",
-                    "description": "Fresno Supersite Final Report - March 31, 2005",
                     "@type": "dcat:Distribution",
+                    "description": "Fresno Supersite Final Report - March 31, 2005",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/EPA_SS_Fresno_Final_Report.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_FRESNO_PM25_NO3_SO4_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_FRESNO_PM25_NO3_SO4_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_FRESNO_PM25_NO3_SO4_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_FRESNO_PM25_NO3_SO4_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2324345309-LARC_ASDC",
+            "issued": "2013-11-14",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0048",
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
             "spatial": "36.78 -119.77",
+            "temporal": "2000-10-12T00:00:00Z/2006-01-01T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO EPA Supersite (SS) Fresno, Particulate Matter (PM) 2.5 Particulate Nitrate and Sulfate Data"
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
-                "appel",
-                "ask magazine",
-                "knowledge",
-                "sharing"
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
-            "identifier": "NASA-860__36",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1432616,47 +1432595,46 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__36",
+            "issued": "2018-06-25",
+            "keyword": [
+                "appel",
+                "ask magazine",
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
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114197-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. 1996-07-25. TOMSEPL3dref. Version 008. TOMS Earth Probe UV Reflectivity Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dref_008.html. Digital Science Data.",
-            "issued": "2004-04-30",
-            "temporal": "1996-07-22T00:00:00Z/2005-12-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation"
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
-            "identifier": "C1237114197-GES_DISC",
-            "description": "This Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains Lambertian effective surface reflectivity values (Rayleigh corrected). The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TOMSEPL3dref",
             "creator": "TOMS Science Team",
-            "title": "TOMS Earth Probe UV Reflectivity Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dref) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPL3dref_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains Lambertian effective surface reflectivity values (Rayleigh corrected). The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1432665,225 +1432643,229 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dref_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dref_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPL3dref.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPL3dref.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPL3dref",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPL3dref",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/EARTHPROBE_USERGUIDE.PDF",
-                    "description": "Earth Probe TOMS Data Product User's Guide.",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Probe TOMS Data Product User's Guide.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/EARTHPROBE_USERGUIDE.PDF",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPL3dref_008.png",
+            "identifier": "C1237114197-GES_DISC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114197-GES_DISC.html",
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
+            "series-name": "TOMSEPL3dref",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-07-22T00:00:00Z/2005-12-14T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Earth Probe UV Reflectivity Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dref) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/107",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kanemasu, E. T. 1994. Soil Hydraulic Conductivity Data (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/107",
-            "issued": "2024-05-04",
-            "temporal": "1989-10-31T00:00:00Z/1989-10-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-07",
-            "keyword": [
-                "soils",
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
-            "identifier": "C2980620398-ORNL_CLOUD",
             "description": "Field saturated hydraulic conductivity, using constant well head permeameter",
-            "graphic-preview-description": "Browse Image",
-            "title": "Soil Hydraulic Conductivity Data (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F107",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F107",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_soilprop_soilhydc/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_soilprop_soilhydc/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Soil_Hydraulic_Conductivity_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/Soil_Hydraulic_Conductivity_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/107",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/107",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilprop_soilhydc/comp/soilhydc.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilprop_soilhydc/comp/soilhydc.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilprop_soilhydc/comp/soilhydc.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilprop_soilhydc/comp/soilhydc.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilprop_soilhydc/comp/Soil_Hydraulic_Conductivity_Data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_soilprop_soilhydc/comp/Soil_Hydraulic_Conductivity_Data.pdf",
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
+            "identifier": "C2980620398-ORNL_CLOUD",
+            "issued": "2024-05-04",
+            "keyword": [
+                "soils",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/107",
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
             "spatial": "-96.6 39.05 -96.47 39.09",
+            "temporal": "1989-10-31T00:00:00Z/1989-10-31T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Hydraulic Conductivity Data (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC4-67P-M24-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 4 mission phase, covering the period  from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc4-67p-m24-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC4-67P-M24-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc4-67p-m24-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 4 mission phase, covering the period  from 2015-12-15T23:25:00.000 to 2016-01-12T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC4-MTP024 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC4-MTP024 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/tt5z-f7ms",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "wise",
-                "space science",
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
-            "identifier": "NASA-0000038__70",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1432891,874 +1432873,872 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__70",
+            "issued": "2018-06-25",
+            "keyword": [
+                "wise",
+                "space science",
+                "nen",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/tt5z-f7ms",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-3%2F4-EPOXI-HARTLEY2-V1.0",
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
+            "description": "This dataset contains calibrated, 1.05- to 4.8-micron spectral images of comet 103/P Hartley 2 acquired by the High Resolution Infrared Spectrometer from 01 October through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-3-4-epoxi-hartley2-v1.0_tt7q-khju",
+            "issued": "2018-06-26",
+            "keyword": [
+                "epoxi",
+                "103p/hartley 2 (1986 e2)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRII-3%2F4-EPOXI-HARTLEY2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hrii-3-4-epoxi-hartley2-v1.0_tt7q-khju",
-            "description": "This dataset contains calibrated, 1.05- to 4.8-micron spectral images of comet 103/P Hartley 2 acquired by the High Resolution Infrared Spectrometer from 01 October through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission.",
-            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRII CALIBRATED SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - HRII CALIBRATED SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-2-LAUNCH-V1.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-2-launch-v1.0_tt8e-uwuj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calibration",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LORRI-2-LAUNCH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-lorri-2-launch-v1.0_tt8e-uwuj",
-            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS LORRI POST-LAUNCH CHECKOUT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS LORRI POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/BGGIARFFWGF9",
             "citation": "Kevin W. Bowman. 2021-05-27. TRPSDL2O3CRSAUS. Version 1. TROPESS CrIS-SNPP L2 Ozone for Australian Fires, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/BGGIARFFWGF9. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSAUS_1.html. Digital Science Data.",
-            "issued": "2021-05-25",
-            "temporal": "2019-11-01T00:00:00Z/2020-01-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-25",
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
-            "identifier": "C2041966693-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Ozone for Australian Fires, Standard Product contains the vertical distribution of the retrieved atmospheric state of ozone (O3), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. This product focuses on the Australia region (60S-0S; 100E-177.5E) for the time period from 2019-11-01 to 2020-01-31, during the outbreak of Austrailan wildfires. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 26 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2O3CRSAUS",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP O3 (Australian Fires, Special Product) at 261 hPa on 4 January 2020.",
-            "title": "TROPESS CrIS-SNPP L2 Ozone for Australian Fires, Standard Product V1 (TRPSDL2O3CRSAUS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSAUS_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FBGGIARFFWGF9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FBGGIARFFWGF9",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSAUS_Sample.png",
-                    "description": "TROPESS CrIS-SNPP O3 (Australian Fires, Special Product) at 261 hPa on 4 January 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP O3 (Australian Fires, Special Product) at 261 hPa on 4 January 2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSAUS_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSAUS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2O3CRSAUS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2O3CRSAUS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2O3CRSAUS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3CRSAUS_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2O3CRSAUS_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2O3CRSAUS.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2O3CRSAUS.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2O3CRSAUS.1/doc/TROPESS_Australian_Fires_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2O3CRSAUS.1/doc/TROPESS_Australian_Fires_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP O3 (Australian Fires, Special Product) at 261 hPa on 4 January 2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2O3CRSAUS_Sample.png",
+            "identifier": "C2041966693-GES_DISC",
+            "issued": "2021-05-25",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/BGGIARFFWGF9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-05-25",
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
+            "series-name": "TRPSDL2O3CRSAUS",
             "spatial": "100.0 -60.0 177.5 0.0",
+            "temporal": "2019-11-01T00:00:00Z/2020-01-31T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Ozone for Australian Fires, Standard Product V1 (TRPSDL2O3CRSAUS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/915/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-07-02",
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
-            "identifier": "DASHLINK_915",
             "description": "Jam fault scenarios with tensile (+40 lbs) load (diagnostic and prognostic)",
-            "title": "2010_09_10_jam_+40 Lab",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-zip-compressed",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_10_jam_40.zip",
-                    "description": "2010_09_10_jam_+40.zip",
                     "@type": "dcat:Distribution",
+                    "description": "2010_09_10_jam_+40.zip",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/2010_09_10_jam_40.zip",
+                    "mediaType": "application/x-zip-compressed",
                     "title": "2010_09_10_jam_+40.zip"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_915",
+            "issued": "2014-07-02",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/915/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "2010_09_10_jam_+40 Lab"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D55.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band4 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D55.061. https://doi.org/10.5067/MODIS/MCD43D55.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "national geospatial data asset",
-                "surface radiative properties",
-                "earth science",
-                "ngda",
-                "land surface"
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
-            "identifier": "C2540273116-LPCLOUD",
-            "description": "The MCD43D55 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D55 is the white-sky albedo for MODIS band 4. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band4 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D55 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D55 is the white-sky albedo for MODIS band 4. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D55.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D55.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D55.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D55.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273116-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273116-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D55.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D55.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D55",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D55",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D55.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D55.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540273116-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "national geospatial data asset",
+                "surface radiative properties",
+                "earth science",
+                "ngda",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D55.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band4 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2050",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Abshire, J.B., J. Mao, H. Riris, S.R. Kawa, and X. Sun. 2022. ABoVE/ASCENDS: Active Sensing of CO2, CH4, and Water Vapor, Alaska and Canada, 2017. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2050",
-            "issued": "2023-02-09",
-            "temporal": "2017-07-20T16:58:21Z/2017-08-08T20:36:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "atmospheric temperature",
-                "atmospheric water vapor",
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
-            "identifier": "C2264340976-ORNL_CLOUD",
             "description": "This dataset provides in situ airborne measurements of atmospheric carbon dioxide (CO2), methane (CH4), and water vapor concentrations, plus air temperature, pressure, relative humidity, and wind speed values over Alaska and the Yukon and Northwest Territories of Canada during 2017-07-20 to 2017-08-08. Measurements were taken onboard a DC-8 aircraft during this Active Sensing of CO2 Emissions over Nights, Days and Seasons (ASCENDS) airborne deployment over portions of the Arctic-Boreal Vulnerability Experiment (ABoVE) domain. CO2 and CH4 were measured with NASA's Atmospheric Vertical Observations of CO2 in the Earth's Troposphere (AVOCET) instrument. Water vapor and relative humidity were measured with Diode Laser Hydrometer. Measurements of column-averaged dry-air mixing ratio CO2 measurements (XCO2) were taken with the CO2 Sounder Lidar instrument. The airborne CO2 Sounder is a pulsed, multi-wavelength Integrated Path Differential Absorption lidar. It estimates XCO2 in the nadir path from the aircraft to the scattering surface by measuring the shape of the 1572.33 nm CO2 absorption line. The data were collected in order to capture the spatial and temporal dynamics of the northern high latitude carbon cycle as part of ABoVE and are provided in ICARTT file format.",
-            "graphic-preview-description": "A map showing the ground tracks for the airborne campaign, with a table summarizing each flight. The colors in the table match those shown in the ground tracks.",
-            "title": "ABoVE/ASCENDS: Active Sensing of CO2, CH4, and Water Vapor, Alaska and Canada, 2017",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_XCO2_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2050",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2050",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/ABoVE_ASCENDS_XCO2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/ABoVE_ASCENDS_XCO2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_XCO2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_XCO2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2050",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2050",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_ASCENDS_XCO2/comp/ABoVE_ASCENDS_XCO2.pdf",
-                    "description": "ABoVE/ASCENDS: Active Sensing of CO2, CH4, and Water Vapor, Alaska and Canada, 2017: ABoVE_ASCENDS_XCO2.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE/ASCENDS: Active Sensing of CO2, CH4, and Water Vapor, Alaska and Canada, 2017: ABoVE_ASCENDS_XCO2.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_ASCENDS_XCO2/comp/ABoVE_ASCENDS_XCO2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_XCO2_Fig1.png",
-                    "description": "A map showing the ground tracks for the airborne campaign, with a table summarizing each flight. The colors in the table match those shown in the ground tracks.",
                     "@type": "dcat:Distribution",
+                    "description": "A map showing the ground tracks for the airborne campaign, with a table summarizing each flight. The colors in the table match those shown in the ground tracks.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_XCO2_Fig1.png",
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
+            "graphic-preview-description": "A map showing the ground tracks for the airborne campaign, with a table summarizing each flight. The colors in the table match those shown in the ground tracks.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_ASCENDS_XCO2_Fig1.png",
+            "identifier": "C2264340976-ORNL_CLOUD",
+            "issued": "2023-02-09",
+            "keyword": [
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2050",
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
             "spatial": "-165.68 34.59 -98.1 71.28",
+            "temporal": "2017-07-20T16:58:21Z/2017-08-08T20:36:00Z",
             "theme": [
                 "ABoVE",
                 "ASCENDS Airborne",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE/ASCENDS: Active Sensing of CO2, CH4, and Water Vapor, Alaska and Canada, 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-SESAME-2-PHC-V1.0",
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
+            "description": "This archive contains edited data (CODMAC level 2) from the SESAME instrument onboard ROSETTA Lander, acquired during the PHC phase. It also contains documentation which describes the SESAME experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-sesame-2-phc-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-SESAME-2-PHC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-sesame-2-phc-v1.0",
-            "description": "This archive contains edited data (CODMAC level 2) from the SESAME instrument onboard ROSETTA Lander, acquired during the PHC phase. It also contains documentation which describes the SESAME experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL SESAME 2 PHC\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL SESAME 2 PHC\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-MAGPHASE-V1.0",
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
+            "description": "A database of asteroid magnitude-phase relations compiled at the Institute of Astronomy of Kharkiv Kharazin University by Shevchenko et al., including observations from 1978 through 2008. Mainly the observations were performed at the Institute of Astronomy (Kharkiv, Ukraine) and at the Astrophysics Institute (Dushanbe, Tadjikistan). For most asteroids the magnitude-phase relations were obtained down to phase angles less than 1 deg. For some asteroids the magnitudes are presented in three (UBV) or four (BVRI) standard spectral bands.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-magphase-v1.0_ttdk-cara",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-MAGPHASE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-magphase-v1.0_ttdk-cara",
-            "description": "A database of asteroid magnitude-phase relations compiled at the Institute of Astronomy of Kharkiv Kharazin University by Shevchenko et al., including observations from 1978 through 2008. Mainly the observations were performed at the Institute of Astronomy (Kharkiv, Ukraine) and at the Astrophysics Institute (Dushanbe, Tadjikistan). For most asteroids the magnitude-phase relations were obtained down to phase angles less than 1 deg. For some asteroids the magnitudes are presented in three (UBV) or four (BVRI) standard spectral bands.",
-            "title": "KHARKIV ASTEROID MAGNITUDE-PHASE RELATIONS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "KHARKIV ASTEROID MAGNITUDE-PHASE RELATIONS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MODEL-M-AMES-GCM-5-LAT-TIME-V1.0",
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
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Ames Mars General Circulation Model is a three dimensional model based on the primitive equations of meteorology. It includes the radiative effects of dust and carbon dioxide as well as other features such as large-scale topography (see [POLLACKETAL1990]",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.model-m-ames-gcm-5-lat-time-v1.0_tti9-d6nc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MODEL-M-AMES-GCM-5-LAT-TIME-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.model-m-ames-gcm-5-lat-time-v1.0_tti9-d6nc",
-            "description": "The Ames Mars General Circulation Model is a three dimensional model based on the primitive equations of meteorology. It includes the radiative effects of dust and carbon dioxide as well as other features such as large-scale topography (see [POLLACKETAL1990]",
-            "title": "AMES MARS GENERAL CIRCULATION MODEL 5 LAT TIME VARIABLE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "AMES MARS GENERAL CIRCULATION MODEL 5 LAT TIME VARIABLE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ARCB%2FNRAO-V-RTLS%2FGBT-3-DELAYDOPPLER-V1.0",
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
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains Earth-based, polarimetric radar image data for Venus collected from 1988 onwards, using the Arecibo Observatory 12.6-cm (2380 MHz) transmitter and receivers at either Arecibo or the Green Bank Telescope in West Virginia.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.arcb-nrao-v-rtls-gbt-3-delaydoppler-v1.0_ttij-9tx5",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ARCB%2FNRAO-V-RTLS%2FGBT-3-DELAYDOPPLER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.arcb-nrao-v-rtls-gbt-3-delaydoppler-v1.0_ttij-9tx5",
-            "description": "This dataset contains Earth-based, polarimetric radar image data for Venus collected from 1988 onwards, using the Arecibo Observatory 12.6-cm (2380 MHz) transmitter and receivers at either Arecibo or the Green Bank Telescope in West Virginia.",
-            "title": "ARECIBO/NRAO VENUS RTLS/GBT 3 DELAY DOPPLER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ARECIBO/NRAO VENUS RTLS/GBT 3 DELAY DOPPLER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/690",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stone, T.A., and P. Schlesinger. 2003. RLC AVHRR-Derived Land Cover, Former Soviet Union, Far East, 1-km, 1990. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/690",
-            "issued": "2023-11-21",
-            "temporal": "1990-05-15T00:00:00Z/1990-08-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-02",
-            "keyword": [
-                "land use/land cover",
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
-            "identifier": "C2810670893-ORNL_CLOUD",
             "description": "This data set is a 1-kilometer resolution land cover map for the land area of the Primor'ye and Southern Khabarovsk Regions, in the Russian Far East, based on 1990 NOAA AVHRR data. Labeling of land cover classes depended upon the Russian 1990 Forest Cover Map (Garsia, 1990), the analyst's experience with AVHRR data, and Russian data sources. There are eight classes distinguished in this dataset, of which 5 are forest cover classes.The objective of this work was to create a 1-km resolution land cover map of the region of the Far Eastern Siberia based on NOAA AVHRR data which might be used by World Wildlife Fund researchers to aid in the definition of remaining habitats and range for threatened animal species (Stone  and Schlesinger, 1996).",
-            "graphic-preview-description": "Browse Image",
-            "title": "RLC AVHRR-Derived Land Cover, Former Soviet Union, Far East, 1-km, 1990",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/vegetation_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F690",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F690",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_landcover_far_east/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_landcover_far_east/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_AVHRR_1_km.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_AVHRR_1_km.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/690",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/690",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe_mapcode.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe_mapcode.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe_projection.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe_projection.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe_report.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/landcov_rfe_report.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/RLC_AVHRR_1_km.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/RLC_AVHRR_1_km.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/WWF_landcover_Stone_1996.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_landcover_far_east/comp/WWF_landcover_Stone_1996.pdf",
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
+            "identifier": "C2810670893-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "land use/land cover",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/690",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "25.0 23.21 180.0 71.0",
+            "temporal": "1990-05-15T00:00:00Z/1990-08-17T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RLC AVHRR-Derived Land Cover, Former Soviet Union, Far East, 1-km, 1990"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4JM27JZ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Iglesias, A., and C. Rosensweig. 2009-12-31. Effects of Climate Change on Global Food Production from SRES Emissions and Socioeconomic Scenarios. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4JM27JZ. https://doi.org/10.7927/H4JM27JZ.",
-            "issued": "2009-12-31",
-            "temporal": "1970-01-01T00:00:00Z/2080-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-12-31",
-            "references": [
-                "https://doi.org/10.7927/H43R0QR1"
-            ],
-            "keyword": [
-                "economic resources",
-                "atmosphere",
-                "earth science",
-                "socioeconomics",
-                "air quality",
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
-            "identifier": "C1418651576-SEDAC",
-            "description": "The Effects of Climate Change on Global Food Production from SRES Emissions and Socioeconomic Scenarios is an update to a major crop modeling study by the NASA Goddard Institute for Space Studies (GISS). The initial study was published in 1997, based on output of HadCM2 model forced with greenhouse gas concentration from the IS95 emission scenarios in 1997. Results of the initial study are presented at SEDAC's Potential Impacts of Climate Change on World Food Supply: Data Sets from a Major Crop Modeling Study, released in 2001. The co-authors developed and tested a method for investigating the spatial implications of climate change on crop production. The Decision Support System for Agrotechnology Transfer (DSSAT) dynamic process crop growth models, are specified and validated for one hundred and twenty seven sites in the major world agricultural regions. Results from the crop models, calibrated and validated in the major crop-growing regions, are then used to test functional forms describing the response of yield changes in the climate and environmental conditions. This updated version is based on HadCM3 model output along with GHG concentrations from the Special Report on Emissions Scenarios (SRES). The crop yield estimates incorporate some major improvements: 1) consistent crop simulation methodology and climate change scenarios; 2) weighting of model site results by contribution to regional and national, and rainfed and irrigated production; 3) quantitative foundation for estimation of physiological CO2 effects on crop yields; 4) Adaptation is explicitly considered; and 5) results are reported by country rather than by Basic Linked System region. The data are produced by A. Iglesias and C. Rosenzweig and the maps are produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Iglesias, A., and C. Rosensweig",
-            "title": "Effects of Climate Change on Global Food Production from SRES Emissions and Socioeconomic Scenarios",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Effects of Climate Change on Global Food Production from SRES Emissions and Socioeconomic Scenarios is an update to a major crop modeling study by the NASA Goddard Institute for Space Studies (GISS). The initial study was published in 1997, based on output of HadCM2 model forced with greenhouse gas concentration from the IS95 emission scenarios in 1997. Results of the initial study are presented at SEDAC's Potential Impacts of Climate Change on World Food Supply: Data Sets from a Major Crop Modeling Study, released in 2001. The co-authors developed and tested a method for investigating the spatial implications of climate change on crop production. The Decision Support System for Agrotechnology Transfer (DSSAT) dynamic process crop growth models, are specified and validated for one hundred and twenty seven sites in the major world agricultural regions. Results from the crop models, calibrated and validated in the major crop-growing regions, are then used to test functional forms describing the response of yield changes in the climate and environmental conditions. This updated version is based on HadCM3 model output along with GHG concentrations from the Special Report on Emissions Scenarios (SRES). The crop yield estimates incorporate some major improvements: 1) consistent crop simulation methodology and climate change scenarios; 2) weighting of model site results by contribution to regional and national, and rainfed and irrigated production; 3) quantitative foundation for estimation of physiological CO2 effects on crop yields; 4) Adaptation is explicitly considered; and 5) results are reported by country rather than by Basic Linked System region. The data are produced by A. Iglesias and C. Rosenzweig and the maps are produced by the Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4JM27JZ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4JM27JZ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/crop-climate/crop-climate-effects-climate-global-food-production/maize-a1fi-2020-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/crop-climate/crop-climate-effects-climate-global-food-production/maize-a1fi-2020-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/docs",
-                    "description": "Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation Page",
+                    "downloadURL": "http://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/crop-climate-effects-climate-global-food-production/maps",
+            "identifier": "C1418651576-SEDAC",
+            "issued": "2009-12-31",
+            "keyword": [
+                "economic resources",
+                "atmosphere",
+                "earth science",
+                "socioeconomics",
+                "air quality",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4JM27JZ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H43R0QR1"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 90.0",
+            "temporal": "1970-01-01T00:00:00Z/2080-12-31T00:00:00Z",
             "theme": [
                 "CROPCLIM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Effects of Climate Change on Global Food Production from SRES Emissions and Socioeconomic Scenarios"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/javagenes/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-07-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "algorithm",
-                "search",
-                "eos",
-                "genetic",
-                "java",
-                "javagenes"
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
-            "identifier": "OCIO-Fitara-123",
             "description": "JavaGenes is a fairly general purpose evolutionary software system written in Java. It implements several versions of the genetic algorithm, simulated annealing, stochastic hill climbing and other search techniques. JavaGenes has been used to evolve molecules, atomic force field parameters, digital circuits, Earth Observing Satellite schedules, and antennas.",
-            "title": "ARC Code TI: JavaGenes",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1433766,170 +1433746,166 @@
                     "mediaType": "application/x-tar"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-123",
+            "issued": "2015-07-21",
+            "keyword": [
+                "algorithm",
+                "search",
+                "eos",
+                "genetic",
+                "java",
+                "javagenes"
+            ],
+            "landingPage": "http://ti.arc.nasa.gov/opensource/projects/javagenes/",
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
+            "title": "ARC Code TI: JavaGenes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/WATVP_L2_VIIRS_SNPP.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2020-01-15. VIIRS/SNPP Level-2 Water Vapor Products 6-min Swath 750m. Version 1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/WATVP_L2_VIIRS_SNPP.001. https://doi.org/10.5067/VIIRS/WATVP_L2_VIIRS_SNPP.001.",
-            "issued": "2019-12-10",
-            "temporal": "2012-05-01T00:06:00Z/2024-04-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-10",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor"
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
-            "identifier": "C1681179895-LAADS",
-            "description": "The Suomi NPP VIIRS Water Vapor Products provide total column water vapor (TPW) properties from merged VIIRS infrared measurements and CrIS plus ATMS water vapor soundings to continue the depiction of global moisture at high spatial resolution started with MODIS on the Terra and Aqua platforms. While MODIS has two water vapor channels within the 6.5 &#956;m H2O absorption band and four channels within the 15 micrometer CO2 absorption band, VIIRS has no channels in either IR absorption band. The VNPWATVP algorithm is similar to the MODIS MOD07 synthetic regression algorithm. It uses the three VIIRS longwave IR window bands in a regression relation and adds the NUCAPS (CrIS+ATMS) water vapor product to compensate for the absence of VIIRS water vapor channels. The Level-2 6-minute granule and 750 m spatial resolution VIIRS TPW product file includes the collocated NUCAPS background TPW, the VIIRS-only TPW, and VIIRS+NUCAPS TPW retrievals with quality flags.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/SNPP Level-2 Water Vapor Products 6-min Swath 750m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Suomi NPP VIIRS Water Vapor Products provide total column water vapor (TPW) properties from merged VIIRS infrared measurements and CrIS plus ATMS water vapor soundings to continue the depiction of global moisture at high spatial resolution started with MODIS on the Terra and Aqua platforms. While MODIS has two water vapor channels within the 6.5 &#956;m H2O absorption band and four channels within the 15 micrometer CO2 absorption band, VIIRS has no channels in either IR absorption band. The VNPWATVP algorithm is similar to the MODIS MOD07 synthetic regression algorithm. It uses the three VIIRS longwave IR window bands in a regression relation and adds the NUCAPS (CrIS+ATMS) water vapor product to compensate for the absence of VIIRS water vapor channels. The Level-2 6-minute granule and 750 m spatial resolution VIIRS TPW product file includes the collocated NUCAPS background TPW, the VIIRS-only TPW, and VIIRS+NUCAPS TPW retrievals with quality flags.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FWATVP_L2_VIIRS_SNPP.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FWATVP_L2_VIIRS_SNPP.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/WATVP_L2_VIIRS_SNPP--5110",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/WATVP_L2_VIIRS_SNPP--5110",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5110/WATVP_L2_VIIRS_SNPP/",
-                    "description": "Direct access to WATVP_L2_VIIRS_SNPP data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to WATVP_L2_VIIRS_SNPP data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/5110/WATVP_L2_VIIRS_SNPP/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPPVIIRSWATVP001UserGuide2019.pdf",
-                    "description": "Suomi-NPP VIIRS WATVP Products User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Suomi-NPP VIIRS WATVP Products User Guide",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPPVIIRSWATVP001UserGuide2019.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPPVIIRSWATVP001ATBD2019.pdf",
-                    "description": "VIIRS/Suomi-NPP Water Vapor Products Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS/Suomi-NPP Water Vapor Products Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPPVIIRSWATVP001ATBD2019.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/allData/5110/WATVP_L2_VIIRS_SNPP/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/allData/5110/WATVP_L2_VIIRS_SNPP/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1681179895-LAADS",
+            "issued": "2019-12-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/WATVP_L2_VIIRS_SNPP.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-05-01T00:06:00Z/2024-04-08T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/SNPP Level-2 Water Vapor Products 6-min Swath 750m"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-A-NAVCAM-2-EDR-ANNEFRANK-V1.0",
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
-                "5535 annefrank",
-                "stardust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Annefrank data set is a collection of images taken by STARDUST Navigation Camera during the Annefrank asteroid encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-a-navcam-2-edr-annefrank-v1.0_ttse-jfmd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "5535 annefrank",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-A-NAVCAM-2-EDR-ANNEFRANK-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-a-navcam-2-edr-annefrank-v1.0_ttse-jfmd",
-            "description": "The Annefrank data set is a collection of images taken by STARDUST Navigation Camera during the Annefrank asteroid encounter.",
-            "title": "STARDUST NAVCAM IMAGES OF ANNEFRANK",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "STARDUST NAVCAM IMAGES OF ANNEFRANK"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2022-01-10",
-            "temporal": "2022-01-10T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coordinates",
-                "space",
-                "station",
-                "topo",
-                "trajectory",
-                "international",
-                "iss",
-                "ephemeris",
-                "coords",
-                "location"
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
-            "identifier": "nasa-iss-data_2022-01-10_ttt3-hs37",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2022-01-10",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1434052,157 +1434028,163 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2022-01-10_ttt3-hs37",
+            "issued": "2022-01-10",
+            "keyword": [
+                "coordinates",
+                "space",
+                "station",
+                "topo",
+                "trajectory",
+                "international",
+                "iss",
+                "ephemeris",
+                "coords",
+                "location"
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
+            "temporal": "2022-01-10T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2022-01-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SWAP-3-KEM1-V1.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-swap-3-kem1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SWAP-3-KEM1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-swap-3-kem1-v1.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 1.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 12/31/2018. It only includes data downlinked before 01/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 12/31/2018.",
-            "title": "NEW HORIZONS\n      SWAP KEM1\n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      SWAP KEM1\n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-ESC1-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-esc1-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
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
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-ESC1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-esc1-v2.0",
-            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V2.0 data set supersedes the previous V1.0 data set.  Pixel list data files have had corrections applied to their FITS formatting.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 ESC1 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 ESC1 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1368-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-25T01:01:40.000 to 2016-01-25T09:11:44.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1368-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1368-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1368-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-01-25T01:01:40.000 to 2016-01-25T09:11:44.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1368 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1368 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://data.nasa.gov",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-02-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ocio",
-                "open data",
-                "data.json",
-                "pdl"
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
-            "identifier": "NASA-1000",
             "description": "NASA Open Data Public Data List. This machine readable file contains meta-records for NASA open data sets.",
-            "title": "NASA Public Data Listing",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1434210,138 +1434192,175 @@
                     "mediaType": "application/json"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-1000",
+            "issued": "2015-02-26",
+            "keyword": [
+                "ocio",
+                "open data",
+                "data.json",
+                "pdl"
+            ],
+            "landingPage": "http://data.nasa.gov",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Public Data Listing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CPEXAW/APR3/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sy, Ousmane .2022. Airborne Precipitation Radar 3rd Generation (APR-3) CPEX-AW [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CPEXAW/APR3/DATA101",
-            "issued": "2022-06-02",
-            "temporal": "2021-08-20T19:28:22Z/2021-09-04T18:59:04Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-02",
-            "keyword": [
-                "spectral/engineering",
-                "atmosphere",
-                "radar",
-                "precipitation",
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
-            "identifier": "C2269541013-GHRC_DAAC",
             "description": "The Airborne Precipitation Radar 3rd Generation (APR-3) CPEX-AW dataset consists of radar reflectivity, Doppler velocity for all bands, linear depolarization ratio Ku-band, and normalized radar cross section measurements at Ka- and Ku- bands data collected by the APR-3 onboard the NASA DC-8 aircraft. These data were gathered during the Convective Processes Experiment \u2013 Aerosols & Winds (CPEX-AW) field campaign. CPEX-AW was a joint effort between the US National Aeronautics and Space Administration (NASA) and the European Space Agency (ESA) with the primary goal of conducting a post-launch calibration and validation activities of the Atmospheric Dynamics Mission-Aeolus (ADM-AEOLUS) Earth observation wind Lidar satellite in St. Croix. These data files are available from August 20, 2021 through September 4, 2021 in a MatLab file, with associated browse files in JPEG format.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "Airborne Precipitation Radar 3rd Generation (APR-3) CPEX-AW V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpexaw/apr3/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPEXAW%2FAPR3%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPEXAW%2FAPR3%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=apr3cpexaw%2Fdata%2F",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=apr3cpexaw%2Fdata%2F",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpexaw/apr3/browse/2021-08-28/CPEXAW_APR3_S20210828a223000_E20210828a230000_P9_sa_3DKHLoLPc.jpg",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpexaw/apr3/browse/2021-08-28/CPEXAW_APR3_S20210828a223000_E20210828a230000_P9_sa_3DKHLoLPc.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/CPEXAW/DATA101",
-                    "description": "CPEX-AW Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX-AW Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/CPEXAW/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpexaw/apr3/doc/apr3cpexaw_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpexaw/apr3/doc/apr3cpexaw_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/cpex-aw",
-                    "description": "CPEX-AW Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX-AW Project Home Page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/cpex-aw",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpexaw/apr3/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpexaw/apr3/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpexaw/apr3/browse/",
+            "identifier": "C2269541013-GHRC_DAAC",
+            "issued": "2022-06-02",
+            "keyword": [
+                "spectral/engineering",
+                "atmosphere",
+                "radar",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CPEXAW/APR3/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-06-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-80.7804 11.8615 -45.6417 34.046",
+            "temporal": "2021-08-20T19:28:22Z/2021-09-04T18:59:04Z",
             "theme": [
                 "CPEX-AW",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Precipitation Radar 3rd Generation (APR-3) CPEX-AW V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/KAIMIMOANA/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/KAIMIMOANA/DATA001.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
+            },
+            "description": "Measurements from the NOAA ship, the Kaimimoana between 1999 and 2002.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FKAIMIMOANA%2FDATA001",
+                    "mediaType": "text/html",
+                    "title": "Google Scholar search results"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/KAIMIMOANA/",
+                    "mediaType": "text/html",
+                    "title": "This dataset's landing page"
+                }
+            ],
+            "identifier": "C1633360390-OB_DAAC",
             "issued": "1999-07-15",
-            "temporal": "1999-07-15T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
             "keyword": [
                 "earth science",
                 "ocean optics",
@@ -1434350,150 +1434369,107 @@
                 "ocean chemistry",
                 "ocean temperature"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C1633360390-OB_DAAC",
-            "description": "Measurements from the NOAA ship, the Kaimimoana between 1999 and 2002.",
-            "title": "Measurements taken onboard R/V Kaimimoana between 1999 and 2002",
+            "landingPage": "https://doi.org/10.5067/SeaBASS/KAIMIMOANA/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
             "programCode": [
                 "026:001"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FKAIMIMOANA%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
-                    "@type": "dcat:Distribution",
-                    "title": "Google Scholar search results"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
             },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/KAIMIMOANA/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
-                    "@type": "dcat:Distribution",
-                    "title": "This dataset's landing page"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1999-07-15T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements taken onboard R/V Kaimimoana between 1999 and 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-5-TEMPEL1-PHOTOMETRY-V1.0",
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
+            "description": "This dataset contains photometric measurements of comet 9P/Tempel 1 from images taken with the Medium Resolution CCD Instrument during the approach phase of the Deep Impact mission (from 1 May 2005 to 4 July 2005). These data, based on circular apertures ranging from 5 to 30 pixels in diameter, were derived from both science and navigation images taken through clear filters.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-5-tempel1-photometry-v1.0_tue6-zfvy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "9p/tempel 1 (1867 g1)",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-5-TEMPEL1-PHOTOMETRY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-5-tempel1-photometry-v1.0_tue6-zfvy",
-            "description": "This dataset contains photometric measurements of comet 9P/Tempel 1 from images taken with the Medium Resolution CCD Instrument during the approach phase of the Deep Impact mission (from 1 May 2005 to 4 July 2005). These data, based on circular apertures ranging from 5 to 30 pixels in diameter, were derived from both science and navigation images taken through clear filters.",
-            "title": "DEEP IMPACT MRI PHOTOMETRY OF COMET 9P/TEMPEL 1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DEEP IMPACT MRI PHOTOMETRY OF COMET 9P/TEMPEL 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/932/",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "RODNEY MARTIN",
+                "hasEmail": "mailto:rodney.martin@nasa.gov"
+            },
+            "description": "Please find a detailed description here: [ROC Curve Code Augmentation](http://ti.arc.nasa.gov/opensource/projects/roc/)",
+            "identifier": "DASHLINK_932",
             "issued": "2015-05-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "nasa",
                 "ames",
                 "dashlink"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "RODNEY MARTIN",
-                "hasEmail": "mailto:rodney.martin@nasa.gov"
-            },
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/932/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dashlink"
             },
-            "identifier": "DASHLINK_932",
-            "description": "Please find a detailed description here: [ROC Curve Code Augmentation](http://ti.arc.nasa.gov/opensource/projects/roc/)",
-            "title": "ROC Curve Code Augmentation",
-            "programCode": [
-                "026:029"
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROC Curve Code Augmentation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282060544-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2011-07-01. TRMM_2A21. TRMM Precipitation Radar Surface Cross-Section L2 1.5 hours V7. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TRMM_2A21_7.html.",
-            "issued": "2011-07-01",
-            "temporal": "1997-12-31T00:00:00Z/2014-10-07T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-20",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "precipitation",
-                "spectral/engineering",
-                "radar"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1282060544-GES_DISC",
-            "description": "The new version of these data is in GPM-like format (consistent with the GPM Dual-frequency Radar data format), and can be found under the name GPM_2APR.\n\nThis is the sigma zero algorithm, which inputs the PR power (1B21) and computes estimates of the path attenuation and its reliability by using the surface as a reference target. It also computes the spatial and temporal statistics of the surface scattering cross section and classifies the cross sections into land/ocean and rain/no rain categories.\nChanges in horizontal resolution resulting from the TRMM boost that occurred on 24 August 2001:\n\nPre-Boost (before 7 August 2001): Temporal Resolution: 91.5 min/orbit ~ 16 orbits/day; Swath Width: 215 km; Horizontal Resolution: 4.3 km \n\nPost-Boost (after 24 August 2001): Temporal Resolution: 92.5 min/orbit ~ 16 orbits/day; Swath Width: 247 km; Horizontal Resolution: 5.0 km",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TRMM_2A21",
             "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "TRMM Precipitation Radar Surface Cross-Section L2 1.5 hours  V7 (TRMM_2A21) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_2A21_7.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The new version of these data is in GPM-like format (consistent with the GPM Dual-frequency Radar data format), and can be found under the name GPM_2APR.\n\nThis is the sigma zero algorithm, which inputs the PR power (1B21) and computes estimates of the path attenuation and its reliability by using the surface as a reference target. It also computes the spatial and temporal statistics of the surface scattering cross section and classifies the cross sections into land/ocean and rain/no rain categories.\nChanges in horizontal resolution resulting from the TRMM boost that occurred on 24 August 2001:\n\nPre-Boost (before 7 August 2001): Temporal Resolution: 91.5 min/orbit ~ 16 orbits/day; Swath Width: 215 km; Horizontal Resolution: 4.3 km \n\nPost-Boost (after 24 August 2001): Temporal Resolution: 92.5 min/orbit ~ 16 orbits/day; Swath Width: 247 km; Horizontal Resolution: 5.0 km",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1434502,94 +1434478,132 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_2A21_7.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRMM_2A21_7.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L2/TRMM_2A21.7",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L2/TRMM_2A21.7",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L2/TRMM_2A21.7/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L2/TRMM_2A21.7/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_2A21",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRMM_2A21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://trmm.gsfc.nasa.gov/",
-                    "description": "TRMM Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Project Home Page",
+                    "downloadURL": "https://trmm.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/filespec.TRMM.V7.pdf",
-                    "description": "File specification document.",
                     "@type": "dcat:Distribution",
+                    "description": "File specification document.",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/filespec.TRMM.V7.pdf",
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
-                    "downloadURL": "http://www.eorc.jaxa.jp/TRMM/documents/PR_algorithm_product_information/pr_manual/PR_Instruction_Manual_V7_L1.pdf",
-                    "description": "TRMM Precipitation Radar Instruction Manual (provided by JAXA)",
                     "@type": "dcat:Distribution",
+                    "description": "TRMM Precipitation Radar Instruction Manual (provided by JAXA)",
+                    "downloadURL": "http://www.eorc.jaxa.jp/TRMM/documents/PR_algorithm_product_information/pr_manual/PR_Instruction_Manual_V7_L1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L2/TRMM_2A21/doc/README.TRMM_V7.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L2/TRMM_2A21/doc/README.TRMM_V7.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TRMM_2A21_7.png",
+            "identifier": "C1282060544-GES_DISC",
+            "issued": "2011-07-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "precipitation",
+                "spectral/engineering",
+                "radar"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1282060544-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-04-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "TRMM_2A21",
             "spatial": "-180.0 -38.0 180.0 38.0",
+            "temporal": "1997-12-31T00:00:00Z/2014-10-07T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM Precipitation Radar Surface Cross-Section L2 1.5 hours  V7 (TRMM_2A21) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/tuhw-wp9m",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Methods: RNA-seq libraries were prepared using the Illumina TruSeq RNA kit and the TrueSeq method was employed for mRNA enrichment. The libraries were quantified and samples were multiplexed in each lane of the flowcell. Cluster generation was performed and then sequenced on the Illumina HiSeq1000 system. Reads were mapped on the Human Genome Reference and normalized expression table was generated. Results: Among differentially expressed genes 53 of them were up-regulated and 75 were down-regulated. Conclusions: Data demonstrate increased expression of genes associated with growth development and pro-survival in cardiac progenitors cultured under simulated microgravity compared with those cultured under standard gravity. RNA-sequencing analysis was performed to compare global gene expression profiles of cells at differentiation day 8 under simulated microgravity vs. standard gravity.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-127",
+                    "mediaType": "text/html",
+                    "title": "Global gene expression profiles of cardiac progenitors differentiated from human pluripotent stem cells in 3D culture under simulated microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-127_tuhw-wp9m",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse84582-2",
                 "p-gse84582-1",
@@ -1434599,128 +1434613,90 @@
                 "extraction protocol",
                 "condition"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/tuhw-wp9m",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-127_tuhw-wp9m",
-            "description": "Methods: RNA-seq libraries were prepared using the Illumina TruSeq RNA kit and the TrueSeq method was employed for mRNA enrichment. The libraries were quantified and samples were multiplexed in each lane of the flowcell. Cluster generation was performed and then sequenced on the Illumina HiSeq1000 system. Reads were mapped on the Human Genome Reference and normalized expression table was generated. Results: Among differentially expressed genes 53 of them were up-regulated and 75 were down-regulated. Conclusions: Data demonstrate increased expression of genes associated with growth development and pro-survival in cardiac progenitors cultured under simulated microgravity compared with those cultured under standard gravity. RNA-sequencing analysis was performed to compare global gene expression profiles of cells at differentiation day 8 under simulated microgravity vs. standard gravity.",
-            "title": "Global gene expression profiles of cardiac progenitors differentiated from human pluripotent stem cells in 3D culture under simulated microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-127",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Global gene expression profiles of cardiac progenitors differentiated from human pluripotent stem cells in 3D culture under simulated microgravity"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Global gene expression profiles of cardiac progenitors differentiated from human pluripotent stem cells in 3D culture under simulated microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/GMI/GPM/GPROF/2A/07",
             "citation": "Christian Kummerow. 2022-05-09. GPM_2AGPROFGPMGMI. Version 07. GPM GMI (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 13 km V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/GMI/GPM/GPROF/2A/07. https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFGPMGMI_07.html. Digital Science Data.",
-            "issued": "2022-05-09",
-            "temporal": "2014-03-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-01",
-            "keyword": [
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "Christian Kummerow",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2259345545-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07. \n\nThe 2AGPROF (Goddard Profiling) algorithm retrieves consistent precipitation and related science fields from the following GMI and partner passive microwave sensors:\n+ TMI (TRMM)\n+ GMI, (GPM)\n+ SSMI (DMSP F15), SSMIS (DMSP F16, F17, F18, F19)\n+ AMSR2 (GCOM-W1)\n+ MHS (NOAA 18,19)\n+ MHS (METOP A,B)\n+ ATMS (NPP)\n+ SAPHIR (MT1)\n\nThis provides the bulk of the 3-hour coverage achieved by GPM. For each sensor, there are nearrealtime (NRT) products, standard products, and climate products. These differ only in the amount of data that are available within 3 hours, 48 hours, and 3 months of collection, as well as the ancillary data used. The NRT product uses GANAL forecast fields. Standard products use the GANAL analysis product, while the climate product uses ECMWF reanalysis in order to allow for consistent data records with earlier missions. These earlier data may be archived separately. The main strength of the product is the large sampling provided.\n\nThe GPM radiometer algorithms are Bayesian-type algorithms. These algorithms search an apriori database of potential rain profiles and retrieve a weighted average of these entries based upon the proximity of the observed brightness temperature (Tb) to the simulated Tb corresponding to each rain profile. By using the same a-priori database of rain profiles, with appropriate simulated Tb for each constellation sensor, the Bayesian method is completely parametric and thus well suited for GPM's constellation approach. The a-priori information will be supplied by the combined algorithm supplied by GPM's core satellite as soon after launch as feasible. Databases for V0 of the algorithm had to be constructed from various sources as described in the ATBD. The solution provides a mean rain rate as well as the vertical structure of cloud and precipitation hydrometeors and their uncertainty.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_2AGPROFGPMGMI",
-            "creator": "Christian Kummerow",
-            "title": "GPM GMI (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 13 km V07 (GPM_2AGPROFGPMGMI) at GES DISC",
-            "graphic-preview-description": "GPM GMI (GPROF) Surface Precipitation Estimate (GPM_2AGPROFGPMGMI)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFGPMGMI_07.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FGMI%2FGPM%2FGPROF%2F2A%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FGMI%2FGPM%2FGPROF%2F2A%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFGPMGMI_07.png",
-                    "description": "GPM GMI (GPROF) Surface Precipitation Estimate (GPM_2AGPROFGPMGMI)",
                     "@type": "dcat:Distribution",
+                    "description": "GPM GMI (GPROF) Surface Precipitation Estimate (GPM_2AGPROFGPMGMI)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFGPMGMI_07.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFGPMGMI_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_2AGPROFGPMGMI_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFGPMGMI.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L2/GPM_2AGPROFGPMGMI.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFGPMGMI.07/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/opendap/GPM_L2/GPM_2AGPROFGPMGMI.07/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFGPMGMI_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_2AGPROFGPMGMI_07",
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
@@ -1434730,323 +1434706,325 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/GPMfilespec/filespec.GPM.pdf",
-                    "description": "FILE SPECIFICATION DOCUMENT",
                     "@type": "dcat:Distribution",
+                    "description": "FILE SPECIFICATION DOCUMENT",
+                    "downloadURL": "https://gpmweb2https.pps.eosdis.nasa.gov/pub/GPMfilespec/filespec.GPM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/GPROFV07A_releasenotes.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/GPROFV07A_releasenotes.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/GPROFV07A_releasenotes.pdf",
-                    "description": "Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Release Notes",
+                    "downloadURL": "https://arthurhou.pps.eosdis.nasa.gov/Documents/GPROFV07A_releasenotes.pdf",
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
-                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/gpminstruments.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "GPM GMI (GPROF) Surface Precipitation Estimate (GPM_2AGPROFGPMGMI)",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_2AGPROFGPMGMI_07.png",
+            "identifier": "C2259345545-GES_DISC",
+            "issued": "2022-05-09",
+            "keyword": [
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/GMI/GPM/GPROF/2A/07",
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
+            "series-name": "GPM_2AGPROFGPMGMI",
             "spatial": "-180.0 -70.0 180.0 70.0",
+            "temporal": "2014-03-04T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GMI (GPROF) Radiometer Precipitation Profiling L2A 1.5 hours 13 km V07 (GPM_2AGPROFGPMGMI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmLay",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmLay. https://asdc.larc.nasa.gov/project/CATS-ISS.",
-            "issued": "2018-08-13",
-            "temporal": "2015-03-25T00:00:00Z/2017-10-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-13",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols",
-                "clouds"
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
-            "identifier": "C1599922052-LARC_ASDC",
             "description": "CATS-ISS_L2O_D-M7.2-V3-01_05kmLay is the Cloud-Aerosol Transport System (CATS) International Space Station (ISS) Level 2 Operational Day Mode 7.2 Version 3-01 5 km Layer data product. This collection spans from March 25, 2015 to October 29, 2017. CATS, which was launched on January 10, 2015, was a lidar remote sensing instrument that provided range-resolved profile measurements of atmospheric aerosols and clouds from the ISS. CATS was intended to operate on-orbit for up to three years. CATS provides vertical profiles at three wavelengths, orbiting between ~230 and ~270 miles above the Earth's surface at a 51-degree inclination with nearly a three-day repeat cycle. For the first time, scientists were able to study diurnal (day-to-night) changes in cloud and aerosol effects from space by observing the same spot on Earth at different times each day. CATS Level 2 Layer data products contain geophysical parameters and are derived from Level 1 data, at 60m vertical and 5km horizontal resolution.",
-            "graphic-preview-description": "CATS Browse and Granule Availability",
-            "title": "CATS-ISS Level 2 Operational Day Mode 7.2 Version 3-01 5 km Layer",
-            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_D-M7.2-V3-01_05kmLay",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_D-M7.2-V3-01_05kmLay",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CATS-ISS",
-                    "description": "ASDC Data and Information for CATS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CATS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CATS-ISS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1599922052-LARC_ASDC",
-                    "description": "Earthdata Search for CATS-ISS_L2O_D-M7.2-V3-01_05kmLay_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CATS-ISS_L2O_D-M7.2-V3-01_05kmLay_V3-01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1599922052-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_D-M7.2-V3-01_05kmLay/contents.html",
-                    "description": "OPeNDAP data access for CATS-ISS_L2O_D-M7.2-V3-01_05kmLay_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CATS-ISS_L2O_D-M7.2-V3-01_05kmLay_V3-01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_D-M7.2-V3-01_05kmLay/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmLay",
-                    "description": "DOI data set landing page for CATS-ISS_L2O_D-M7.2-V3-01_05kmLay_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CATS-ISS_L2O_D-M7.2-V3-01_05kmLay_V3-01",
+                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmLay",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_D-M7.2-V3-01_05kmLay/",
-                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_D-M7.2-V3-01_05kmLay_V3-01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_D-M7.2-V3-01_05kmLay_V3-01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_D-M7.2-V3-01_05kmLay/",
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
+            "identifier": "C1599922052-LARC_ASDC",
+            "issued": "2018-08-13",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_D-M7.2-V3-01_05kmLay",
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
+            "title": "CATS-ISS Level 2 Operational Day Mode 7.2 Version 3-01 5 km Layer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/HNVFRD5ICZN1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Near Real-Time MODIS/Terra L3 Global Daily 500m SIN Grid Snow Cover, Grain Size, and Dust Radiative Forcing, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/HNVFRD5ICZN1.",
-            "issued": "2023-10-19",
-            "temporal": "2023-10-19T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "national geospatial data asset",
-                "snow/ice",
-                "ngda",
-                "earth science",
-                "land surface",
-                "biosphere",
-                "land use/land cover",
-                "cryosphere",
-                "vegetation"
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
-            "identifier": "C2949548721-NSIDCV0",
             "description": "This data set represents an updated version of the MODIS Snow Covered Area and Grain-size (MODSCAG) and MODIS Dust Radiative Forcing in Snow (MODDRF) data sets previously produced by the NASA Jet Propulsion Laboratory (JPL). Data are derived from NASA LANCE near real-time MODIS/Terra surface reflectance data (<a href=\"https://lance.modaps.eosdis.nasa.gov/modis/\">MOD09GA_NRT</a>) but are not themselves near real-time, nor part of NASA LANCE. This data set contains the following parameters: snow fraction, snow grain size (from the SCAG algorithm), vegetation fraction, rock fraction, ice fraction, shade fraction, deltavis, radiative forcing, and optical snow grain size (from the DRFS algorithm). Data are available from 19 October 2023 to the present and are currently available for five regions in the western United States (MODIS tiles h08v04, h08v05, h09v04, h09v05, h10v04). Additional tiles will be added over time. These data are provided in GeoTiff format.",
-            "title": "Near Real-Time MODIS/Terra L3 Global Daily 500m SIN Grid Snow Cover, Grain Size, and Dust Radiative Forcing, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHNVFRD5ICZN1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FHNVFRD5ICZN1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/MODSCGDRF_NRT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/MODSCGDRF_NRT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HNVFRD5ICZN1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/HNVFRD5ICZN1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/HNVFRD5ICZN1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/HNVFRD5ICZN1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2949548721-NSIDCV0",
+            "issued": "2023-10-19",
+            "keyword": [
+                "national geospatial data asset",
+                "snow/ice",
+                "ngda",
+                "earth science",
+                "land surface",
+                "biosphere",
+                "land use/land cover",
+                "cryosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/HNVFRD5ICZN1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-10-19T00:00:00Z/2024-12-23T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Near Real-Time MODIS/Terra L3 Global Daily 500m SIN Grid Snow Cover, Grain Size, and Dust Radiative Forcing, Version 1"
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
-                "themis",
-                "radio science",
-                "grs",
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
-            "identifier": "NASA-536",
             "description": "GRS, RADIO SCIENCE (Releases 106-108), SPICE, THEMIS",
-            "title": "PDS Odyssey Data Release 36",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1435054,23 +1435032,47 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-536",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "themis",
+                "radio science",
+                "grs",
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
+            "title": "PDS Odyssey Data Release 36"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M21-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m21-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dark",
                 "zeta cas",
@@ -1435079,213 +1435081,182 @@
                 "bias",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-ESC3-67PCHURYUMOV-M21-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-esc3-67pchuryumov-m21-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-09-22T23:25:00.000 to 2015-10-20T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC3-MTP021 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 ESC3-MTP021 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M18-REFLECT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m18-reflect-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "pluto",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M18-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m18-reflect-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/POLARWINDSI/0001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-03-14. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/POLARWINDSI/0001.",
-            "issued": "2018-01-30",
-            "temporal": "2014-10-29T00:00:00Z/2014-11-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-05-03",
-            "keyword": [
-                "earth science",
-                "lidar",
-                "spectral/engineering",
-                "atmospheric winds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "George Emmitt",
                 "hasEmail": "mailto:gde@swa.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1457763994-LARC_ASDC",
             "description": "PolarWindsI_DAWN_KingAirUC-12B is the Polar Winds I - Doppler Aerosol WiNd (DAWN) - KingAirUC-12B data product. Data for this was collected using the DAWN instrument flown on the NASA Langley Beechcraft UC-12B Huron aircraft. Data collection for this product is complete. Polar Winds I was based in Kangerlussuaq, Greenland and flew DAWN on board the NASA King Air UC-12B during Oct-Nov 2014 while Polar Winds II was based in Keflavik, Iceland and utilized the NASA DC-8 aircraft to fly DAWN and Dropsondes over the Arctic in May 2015. In total, twenty-four individual missions with over 80 hours of research flights were flown in the Arctic region near Greenland and Iceland during Polar Winds.\r\n\r\nThe focus instrument for the wind measurements taken over the Arctic during Polar Winds was the DAWN airborne wind lidar. At a wavelength of 2.05 microns and at 250 mj per pulse, DAWN is the most powerful airborne Doppler Wind Lidar available today for airborne missions. DAWN has previously been flown on the NASA DC-8 during the 2010 Genesis and Rapid Intensification Processes (GRIP) campaign and on the NASA UC-12 for wind field characterization off the coast of Virginia. In addition to DAWN, Polar Winds utilized the High Definition Sounding System (HDSS) dropsonde delivery system developed by Yankee Environmental Services to drop almost 100 dropsondes during Polar Wind II to obtain additional high-resolution vertical wind profiles during most missions. These dropsondes also provided needed calibration/validation for the much newer DAWN measurements.\r\n\r\nBeginning in the fall of 2014, NASA sponsored two airborne field campaigns, collectively called Polar Winds, designed to fly the Doppler Aerosol WiNd (DAWN) lidar and other instruments to take airborne wind measurements of the Arctic atmosphere, specifically over and off the coasts of Greenland during Oct-Nov 2014 and May 2015. In particular, Polar Winds conducted a series of science experiments focusing on the measurement and analyses of lower tropospheric winds and aerosols associated with coastal katabatic flows, barrier winds, the Greenland Tip Jet, boundary layer circulations such as rolls and OLEs (Organized Large Eddies), and near surface winds over open water, transitional ice zones and the Greenland Ice Cap.",
-            "title": "Polar Winds I - Doppler Aerosol WiNd (DAWN) - KingAirUC-12B",
-            "graphic-preview-file": "http://www.swa.com/images/LidarAirborne/Ppt0000020.pdf",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FPOLARWINDSI%2F0001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FPOLARWINDSI%2F0001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.swa.com/images/LidarAirborne/Ppt0000020.pdf",
-                    "description": "NASA Headquarters Presentation of The 2014 - 2015 PolarWinds DAWN Airborne Campaigns; Instrument Performance, Data Collection and Advanced data Processing Algorithm Development",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Headquarters Presentation of The 2014 - 2015 PolarWinds DAWN Airborne Campaigns; Instrument Performance, Data Collection and Advanced data Processing Algorithm Development",
+                    "downloadURL": "https://www.swa.com/images/LidarAirborne/Ppt0000020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1457763994-LARC_ASDC",
-                    "description": "Earthdata Search for PolarWindsI_DAWN_KingAirUC-12B_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for PolarWindsI_DAWN_KingAirUC-12B_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1457763994-LARC_ASDC",
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/POLARWINDSI/0001",
-                    "description": "DOI data set landing page for PolarWindsI_DAWN_KingAirUC-12B_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for PolarWindsI_DAWN_KingAirUC-12B_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/POLARWINDSI/0001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/polarwindsii/guide/Modeled_Barrier_Flow_Case_Study.pdf",
-                    "description": "A Case Study of Observed and Modeled Barrier Flow in the Denmark Strait in May 2015",
                     "@type": "dcat:Distribution",
+                    "description": "A Case Study of Observed and Modeled Barrier Flow in the Denmark Strait in May 2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/polarwindsii/guide/Modeled_Barrier_Flow_Case_Study.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/polarwindsii/guide/PolarWindsII_Overview.pdf",
-                    "description": "Polar Winds II Introduction/Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Polar Winds II Introduction/Overview",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/polarwindsii/guide/PolarWindsII_Overview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/polarwindsii/guide/Polar_Winds_References.pdf",
-                    "description": "Polar Winds Papers and Presentations as of Sep. 1, 2017",
                     "@type": "dcat:Distribution",
+                    "description": "Polar Winds Papers and Presentations as of Sep. 1, 2017",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/polarwindsii/guide/Polar_Winds_References.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/PolarWindsI/DAWN_KingAirUC-12B_1/",
-                    "description": "ASDC Direct Data Download for PolarWindsI_DAWN_KingAirUC-12B_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for PolarWindsI_DAWN_KingAirUC-12B_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/PolarWindsI/DAWN_KingAirUC-12B_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-file": "http://www.swa.com/images/LidarAirborne/Ppt0000020.pdf",
+            "identifier": "C1457763994-LARC_ASDC",
+            "issued": "2018-01-30",
+            "keyword": [
+                "earth science",
+                "lidar",
+                "spectral/engineering",
+                "atmospheric winds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/POLARWINDSI/0001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-05-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>59.0 -58.0 59.0 -42.0 69.0 -42.0 69.0 -58.0 59.0 -58.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2014-10-29T00:00:00Z/2014-11-13T23:59:59.999Z",
             "theme": [
                 "Polar Winds I",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Polar Winds I - Doppler Aerosol WiNd (DAWN) - KingAirUC-12B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10989",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-05-01",
-            "temporal": "2012-05-01T00:00:00Z/2016-05-01T00:00:00Z",
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
-                "nasa headquarters",
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
-            "identifier": "TECHPORT_10989",
             "description": "&lt;p&gt;\r\n\tN/A&lt;/p&gt;",
-            "title": "Next-Generation Real-Time Geodetic Station Sensor Web for Natural Hazards Research and Applications Project",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1435293,41 +1435264,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "TECHPORT_10989",
+            "issued": "2012-05-01",
+            "keyword": [
+                "active",
+                "nasa headquarters",
+                "project"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10989",
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
+            "temporal": "2012-05-01T00:00:00Z/2016-05-01T00:00:00Z",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Next-Generation Real-Time Geodetic Station Sensor Web for Natural Hazards Research and Applications Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/tuxa-9v9t",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nen",
-                "space science",
-                "wise",
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
-            "identifier": "NASA-0000038__3",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1435335,136 +1435317,156 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__3",
+            "issued": "2018-06-25",
+            "keyword": [
+                "nen",
+                "space science",
+                "wise",
+                "geography"
+            ],
+            "landingPage": "https://data.nasa.gov/d/tuxa-9v9t",
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
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Analysis_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-10-16. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Analysis_DC8_Data_1.",
-            "issued": "1995-12-06",
-            "temporal": "1995-12-03T00:00:00Z/1996-02-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "1996-02-19",
-            "keyword": [
-                "atmosphere",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric winds",
-                "altitude",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Newman",
                 "hasEmail": "mailto:paul.a.newman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2736731936-LARC_ASDC",
             "description": "TOTE-VOTE_Analysis_DC8_Data_1 is the modeled meteorological data along the flight path for the DC-8 aircraft collected during the Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) campaign. Data collection for this product is complete.\r\n\r\nThe Tropical Ozone Transport Experiment \u2013 Vortex Ozone Transport Experiment (TOTE-VOTE) campaign was conducted by NASA from December 1995 to February 1996. TOTE-VOTE took place in the Pacific region with the goal of gaining a better understanding of background transport processes from tropical/polar regions to midlatitudes. Nineteen flights were conducted using the NASA DC-8 aircraft and balloon sondes with the purpose of measuring the transport of filaments of air moved in or out of the arctic polar vortex and the tropical stratospheric reservoir. TOTE-VOTE also utilized ground-based instruments along with aircrafts.\r\n\r\nVarious instrumentation was used during TOTE-VOTE in order to achieve the mission objectives. The DC-8 aircraft was equipped with the NCAR NOxyO3 instrument, the NASA Langley Airborne Differential Absorption Lidar (DIAL) system, the Forward Scattering Spectrometer Probe (FSSP), the Microwave Temperature Profiler (MTP), the Multiple-Angle Aerosol Spectrometer Probe (MASP), and the diode laser spectrometer system, historically known as the Differential Absorption Carbon monOxide Measurement (DACOM). The NCAR NOxyO3 is a type of 4-channel chemiluminescence instrument that was used to quantify NOx (NO and NO2), NOy (total reactive nitrogen), and ozone (O3) in the air. The DIAL system used four lasers to make DIAL O3 profiles, along with collecting data on aerosol backscattering, aerosol depolarization ratio, aerosol extinction, and aerosol optical depth. The FSSP is an optical particle counter that measured particle size distribution. The MTP is a passive microwave radiometer that measured natural thermal emissions and was used during TOTE-VOTE to record temperature. The MASP spectrometer collected in-situ measurements of particle concentration, particle size distribution, and particle extinction. Along with the MASP\u2019s in-situ measurements, the DACOM spectrometer utilized three diode lasers at different wavelengths to take in-situ measurements of N2O, CO, CH4, and CO2 for TOTE-VOTE. Ground-based instruments collected lidar data while balloon sondes gathered information on wind direction, wind speed, atmospheric pressure, and air temperature.",
-            "title": "Tropical Ozone Transport Experiment - Vortex Ozone Transport Experiment (TOTE-VOTE) DC-8 Analysis Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTOTE-VOTE_Analysis_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FTOTE-VOTE_Analysis_DC8_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOTE-VOTE/Analysis_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for TOTE-VOTE_Analysis_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TOTE-VOTE_Analysis_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOTE-VOTE/Analysis_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736731936-LARC_ASDC",
-                    "description": "Earthdata Search for TOTE-VOTE_Analysis_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TOTE-VOTE_Analysis_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2736731936-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Analysis_DC8_Data_1",
-                    "description": "DOI for TOTE-VOTE_Analysis_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for TOTE-VOTE_Analysis_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Analysis_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2736731936-LARC_ASDC",
+            "issued": "1995-12-06",
+            "keyword": [
+                "atmosphere",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric winds",
+                "altitude",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/TOTE-VOTE_Analysis_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1996-02-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-23.1 -180.0 -23.1 180.0 89.993 180.0 89.993 -180.0 -23.1 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-12-03T00:00:00Z/1996-02-20T00:00:00Z",
             "theme": [
                 "TOTE-VOTE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tropical Ozone Transport Experiment - Vortex Ozone Transport Experiment (TOTE-VOTE) DC-8 Analysis Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-3-RDR-SURVEY-COUNTRATE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set provides energetic (MeV) ion count rates and events measured by the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. The data are derived from the raw real-time science (RTS) data. There are two basic types of data files associated with the full-rate reduced data: Detector Count Rates and Events (Pulse Heights).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-3-rdr-survey-countrate-v1.0_tv3i-zbe9",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "io",
                 "callisto",
@@ -1435475,185 +1435477,195 @@
                 "amalthea",
                 "io plasma torus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-HIC-3-RDR-SURVEY-COUNTRATE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-hic-3-rdr-survey-countrate-v1.0_tv3i-zbe9",
-            "description": "This data set provides energetic (MeV) ion count rates and events measured by the Heavy Ion Counter (HIC) instrument on the Galileo spacecraft. The data are derived from the raw real-time science (RTS) data. There are two basic types of data files associated with the full-rate reduced data: Detector Count Rates and Events (Pulse Heights).",
-            "title": "GO JUP HIC SURVEY ENERGETIC ION COUNT RATE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GO JUP HIC SURVEY ENERGETIC ION COUNT RATE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1424",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Oechel, W., J. Verfaillie, G. Vourlitis, and R. Zulueta. 2016. CARVE: L1 In-situ Carbon and CH4 Flux and Meteorology at EC Towers, Alaska, 2011-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1424",
-            "issued": "2016-12-12",
-            "temporal": "2011-05-30T23:30:00Z/2016-01-07T06:58:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-27",
-            "keyword": [
-                "climate indicators",
-                "land surface/agriculture indicators",
-                "ecological dynamics",
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science",
-                "atmospheric water vapor",
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
-            "identifier": "C2236316255-ORNL_CLOUD",
             "description": "This data set provides ground in situ flux and meteorological science data from fixed instruments at three eddy covariance tower sites located in the Alaskan Arctic tundra. Real and gap-filled observations of carbon dioxide, methane, water vapor, and latent energy flux in addition to standard meteorological and environmental variables are reported at half-hourly intervals between 2011 and 2015 for sites at Atqasuk, Barrow, and Ivotuk, Alaska. The three sites form a 300-km north-south transect on the North Slope of Alaska, each site representing distinct Arctic vegetation communities. These tower measurements create a long-term record of one of the largest, most volatile carbon stocks on the planet. Observations from these towers are being used to determine the seasonal and inter-annual patterns of CO2 and CH4 flux, and their relationship to changes in environmental factors.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CARVE: L1 In-situ Carbon and CH4 Flux and Meteorology at EC Towers, Alaska, 2011-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_Ground_Flux_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1424",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1424",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/carve/campaign/CARVE_L1_Ground_Flux/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/carve/campaign/CARVE_L1_Ground_Flux/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/CARVE_L1_Ground_Flux_1424.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/CARVE_L1_Ground_Flux_1424.zip",
+                    "mediaType": "application/zip",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_Ground_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_Ground_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1424",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1424",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/CARVE_L1_Ground_Flux_1424.zip",
-                    "description": "Collection bundle",
                     "@type": "dcat:Distribution",
+                    "description": "Collection bundle",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/protected/bundle/CARVE_L1_Ground_Flux_1424.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L1_Ground_Flux/comp/CARVE_L1_Ground_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L1_Ground_Flux/comp/CARVE_L1_Ground_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_Ground_Flux_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_Ground_Flux_Fig1.png",
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
+            "graphic-preview-file": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_Ground_Flux_Fig1.png",
+            "identifier": "C2236316255-ORNL_CLOUD",
+            "issued": "2016-12-12",
+            "keyword": [
+                "climate indicators",
+                "land surface/agriculture indicators",
+                "ecological dynamics",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "atmospheric water vapor",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1424",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-157.41 68.49 -155.75 71.32",
+            "temporal": "2011-05-30T23:30:00Z/2016-01-07T06:58:00Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: L1 In-situ Carbon and CH4 Flux and Meteorology at EC Towers, Alaska, 2011-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC3-67PCHURYUMOV-M19-V1.0",
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
+            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-07-28 to 2015-08-25.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc3-67pchuryumov-m19-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC3-67PCHURYUMOV-M19-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc3-67pchuryumov-m19-v1.0",
-            "description": "This data set contains calibrated images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-07-28 to 2015-08-25.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 3 RDR MTP 019 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 3 RDR MTP 019 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/observations/timeline/ft2/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "This utility permits you to download the most current version of the spacecraft (FT2) file predicting the LAT's pointing for a given mission week. The FT2 file is a FITS-formatted file describing Fermi's position and orientation, and thus the LAT's pointing, as a function of time. The FT2 files available here are created in planning Fermi's timeline, and thus provide the observatory's predicted pointing for a given mission week. Files with the string 'PRELIM' in the filename are produced approximately three weeks in advance, while files with 'FINAL' in the filename describe the timeline that will be uploaded to the spacecraft; thus you should use the latter if available. Note that the actual LAT pointing may differ from the predicted as a result of Target-of-Opportunity observations or Autonomous Repoints in response to a bright gamma-ray burst.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/observations/timeline/ft2/files/",
+                    "mediaType": "image/fits"
+                }
+            ],
+            "identifier": "NASA-0000235",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "photons",
                 "lat",
@@ -1435667,1235 +1435679,1235 @@
                 "particle physics",
                 "light arcs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/observations/timeline/ft2/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000235",
-            "description": "This utility permits you to download the most current version of the spacecraft (FT2) file predicting the LAT's pointing for a given mission week. The FT2 file is a FITS-formatted file describing Fermi's position and orientation, and thus the LAT's pointing, as a function of time. The FT2 files available here are created in planning Fermi's timeline, and thus provide the observatory's predicted pointing for a given mission week. Files with the string 'PRELIM' in the filename are produced approximately three weeks in advance, while files with 'FINAL' in the filename describe the timeline that will be uploaded to the spacecraft; thus you should use the latter if available. Note that the actual LAT pointing may differ from the predicted as a result of Target-of-Opportunity observations or Autonomous Repoints in response to a bright gamma-ray burst.",
-            "title": "Fermi FT2 Spacecraft Pointing Files",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fermi.gsfc.nasa.gov/ssc/observations/timeline/ft2/files/",
-                    "mediaType": "image/fits"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Fermi FT2 Spacecraft Pointing Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0642-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-13T14:11:10.000 to 2015-03-13T15:54:42.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0642-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0642-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0642-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-13T14:11:10.000 to 2015-03-13T15:54:42.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0642 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0642 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/NEXRAD/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Unidata  and   NWS Radar Operations Center.2018. GPM Ground Validation KLGX NEXRAD OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/NEXRAD/DATA201",
-            "issued": "2018-01-10",
-            "temporal": "2015-09-22T22:29:00Z/2016-05-01T23:56:00Z",
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
-            "identifier": "C1981979131-GHRC_DAAC",
             "description": "The GPM Ground Validation KLGX NEXRAD OLYMPEX dataset contains data from selected NEXt Generation Weather RADar system (NEXRAD) instruments in operation during the Olympic Mountains Experiment (OLYMPEX) field campaign to help support the ground validation of the Global Precipitation Measurement (GPM). NEXRAD is a network of 160 stationary S-Band radars dispersed throughout the United States and select locations abroad.  Datasets gathered from three NEXRAD stations, as listed below, extend from 22 September 2015 through 01 May 2016  as part of the GPM Ground Validation OLYMPEX data.  This dataset contain browse images of base reflectivity observations in the Portable Network Graphic (PNG) format. Base radar reflectivity is the measure of transmitted power returned to the radar after intercepting a target, for example, rain droplets. This information can illustrate the amount and size distribution of water particles in a given unit volume of atmosphere.",
-            "graphic-preview-description": "Sample Browse Image",
-            "title": "GPM Ground Validation KLGX NEXRAD OLYMPEX V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NEXRAD2/KLGX/browse/2015-11-15/olympex_Level2_KLGX_20151115_0027_ELEV_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FNEXRAD%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FNEXRAD%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmklgx2olyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmklgx2olyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NEXRAD2/KLGX/browse/2015-11-15/olympex_Level2_KLGX_20151115_0027_ELEV_01.png",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NEXRAD2/KLGX/browse/2015-11-15/olympex_Level2_KLGX_20151115_0027_ELEV_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
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
-                    "description": "Federal Meteorological Handbook Part A: System Concepts, Responsibilities, and Procedures",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook Part A: System Concepts, Responsibilities, and Procedures",
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
-                    "downloadURL": "https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc%3AC00345",
-                    "description": "NOAA Next Generation Radar (NEXRAD) Level 2 Base Data",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA Next Generation Radar (NEXRAD) Level 2 Base Data",
+                    "downloadURL": "https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc%3AC00345",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NEXRAD2/KLGX/doc/gpmnexradolyx_dataset.pdf",
-                    "description": "GPM\u200b \u200bGround\u200b \u200bValidation\u200b \u200bNEXRAD\u200b \u200bOLYMPEX User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "GPM\u200b \u200bGround\u200b \u200bValidation\u200b \u200bNEXRAD\u200b \u200bOLYMPEX User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NEXRAD2/KLGX/doc/gpmnexradolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1042&context=jto",
-                    "description": "A Review of NEXRAD Level II: Data, Distribution, and Applications",
                     "@type": "dcat:Distribution",
+                    "description": "A Review of NEXRAD Level II: Data, Distribution, and Applications",
+                    "downloadURL": "https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=1042&context=jto",
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
+            "graphic-preview-description": "Sample Browse Image",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/NEXRAD2/KLGX/browse/2015-11-15/olympex_Level2_KLGX_20151115_0027_ELEV_01.png",
+            "identifier": "C1981979131-GHRC_DAAC",
+            "issued": "2018-01-10",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/NEXRAD/DATA201",
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
             "spatial": "-124.784 46.6742 -123.45 47.5825",
+            "temporal": "2015-09-22T22:29:00Z/2016-05-01T23:56:00Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation KLGX NEXRAD OLYMPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/579",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Piedade, M.T.F., and W.J. Junk. 2013. NPP Tropical Forest: Manaus, Brazil, 1963-1990 , R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/579",
-            "issued": "2013-10-17",
-            "temporal": "1910-01-01T00:00:00Z/1993-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "earth science",
-                "ecological dynamics",
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
-            "identifier": "C2751947828-ORNL_CLOUD",
             "description": "This data set includes six ASCII files (.txt format). Five files contain productivity values for several types of tropical Amazon rainforest near Manaus, Brazil studied between 1963 and 1990, and one file contains monthly and annual climate data for the period 1910-1993.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Tropical Forest: Manaus, Brazil, 1963-1990 , R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F579",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F579",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_MNS/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_MNS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_MNS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_MNS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/579",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/579",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_MNS/comp/NPP_MNS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_MNS/comp/NPP_MNS.pdf",
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
+            "identifier": "C2751947828-ORNL_CLOUD",
+            "issued": "2013-10-17",
+            "keyword": [
+                "earth science",
+                "ecological dynamics",
+                "vegetation",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/579",
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
             "spatial": "-60.12 -3.0 -59.97 -2.5",
+            "temporal": "1910-01-01T00:00:00Z/1993-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Tropical Forest: Manaus, Brazil, 1963-1990 , R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MAPS_SRL1_CO5X5_HDF",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/MAPS_SRL1_CO5X5_HDF.",
-            "issued": "1999-07-12",
-            "temporal": "1994-04-09T00:00:00Z/1994-04-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-02-06",
-            "keyword": [
-                "air quality",
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
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
-            "identifier": "C1536049390-LARC_ASDC",
             "description": "MAPS OverviewThe MAPS experiment measures the global distribution of carbon monoxide (CO) mixing ratios in the free troposphere. Because of MAPS' previous flights on board the Space Shuttle, Earth system scientists now know that carbon monoxide concentrations in the troposphere are highly variable around the planet, and that widespread burning in the South American Amazon Basin and southern cerrados, the African savannahs,and the Australian grasslands and ranches are major sources of carbon monoxide in the southern hemisphere and tropical troposphere.The 1994 flights of the MAPS experiment provided CO measurements that show seasonal changes in CO emissions, sources, transports, and chemistry.Instrument The MAPS instrument is based on a technique called gas filter radiometry. Thermal energy from the Earth passes through the atmosphere and enters the viewport of the downlooking MAPS instrument. Carbon monoxide and nitrous oxide (N2O) in the atmosphere produce unique absorption lines in the transmitted energy. The energy which enters the MAPS instrument is split into three beams. One beam passes through a cell containing CO and falls onto a detector. This CO gas cell acts as a filter for the effects of CO present in the middle troposphere. A second beam falls directly onto a detector without passing through any gas filter. The difference in the voltage of the signals from these two detectors can be used to determine the amount of CO present in the atmosphere at an altitude of 7-8 km. During the dedicated Earth-Observing Space Shuttle mission in 1994, MAPS measured the distribution of carbon monoxide in the middle troposphere to evaluate CO sources and chemistry, and to evaluate the seasonal and interannual variation of this key atmospheric trace gas. Interpretation of these measurements will help us to better understand the atmosphere and the consequences that human activities initiate in global climate change. A third beam of the incident energy passes through a cell containing N2O and falls onto a detector. This N2O gas cell acts as a filter for the effects of N2O present in the atmosphere. The global distribution of N2O is well known, so the N2O signal can be used to detect the presence of clouds in the field of view and to correct the simultaneous CO measurement for systematic errors in the data.SRL-1 Mission GoalsThe MAPS SRL-1 mission took place during Northern Hemisphere Spring when global biomass burning does not typically occur. Some burning may occur for the purpose of clearing the damaged and felled trees in the forests of North America after the rather severe winter. The goals of the MAPS SRL-1 mission are to provide a validated, near-global atlas of the distribution of tropospheric Carbon Monoxide during the mission, and to assess the health status of the MAPS instrument as the mission progresses. SL1 SummaryHigh concentrations of carbon monoxide over the Northern Hemisphere can be seen in measurements made by the Measurement of Air Pollution from Space(MAPS) instrument. These April 1994 measurements, made from the Space Shuttle Endeavour(STS-59), show large sources of air pollution in the lower atmosphere (2 to 10 miles above the surface) over the industrialized Northern Hemisphere.The data that are available from MAPS SRL1 include a 5 by 5 degree gridded box (MAPS_SRL1_5X5_HDF) and a second by second data product (MAPS_SRL1_COSEC_HDF). These data sets are available from the Langley DAAC.",
-            "title": "Measurement of Air Pollution from Satellites (MAPS) Space Radar Laboratory - 1 (SRL1) Carbon Monoxide 5 degree by 5 degree data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMAPS_SRL1_CO5X5_HDF",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMAPS_SRL1_CO5X5_HDF",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/langley/news/factsheets/MAPS.html",
-                    "description": "NASA Langley Factsheet for MAPS",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Langley Factsheet for MAPS",
+                    "downloadURL": "https://www.nasa.gov/centers/langley/news/factsheets/MAPS.html",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MAPS_SRL1_CO5X5_HDF",
-                    "description": "DOI data set landing page for MAPS_SRL1_CO5X5_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MAPS_SRL1_CO5X5_HDF_1",
+                    "downloadURL": "https://doi.org/10.5067/MAPS_SRL1_CO5X5_HDF",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536049390-LARC_ASDC",
-                    "description": "Earthdata Search for MAPS_SRL1_CO5X5_HDF_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MAPS_SRL1_CO5X5_HDF_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536049390-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/guide/base_maps_co5x5_dataset.pdf",
-                    "description": "MAPS 5 degree by 5 degree Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "MAPS 5 degree by 5 degree Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/guide/base_maps_co5x5_dataset.pdf",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/readme/readme_maps_srl1_co5x5_hdf.txt",
-                    "description": "Readme Information about the MAPS sample read software and data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the MAPS sample read software and data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/readme/readme_maps_srl1_co5x5_hdf.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/compile_read_maps_co5x5.txt",
-                    "description": "Script that compiles the C code necessary to read the following MAPS HDF data files: 1) MAPS_OSTA3_CO5X5_HDF, 2) MAPS_SRL1_CO5X5_HDF, 3) MAPS_SRL2_CO5X5_HDF",
                     "@type": "dcat:Distribution",
+                    "description": "Script that compiles the C code necessary to read the following MAPS HDF data files: 1) MAPS_OSTA3_CO5X5_HDF, 2) MAPS_SRL1_CO5X5_HDF, 3) MAPS_SRL2_CO5X5_HDF",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/compile_read_maps_co5x5.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/maps_co5x5_read.c",
-                    "description": "Sample read program for the following MAPS data sets: MAPS_SRL1_CO5x5_HDF, MAPS_SRL2_CO5x5_HDF, MAPS_OSTA3_CO5x5_HDF - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample read program for the following MAPS data sets: MAPS_SRL1_CO5x5_HDF, MAPS_SRL2_CO5x5_HDF, MAPS_OSTA3_CO5x5_HDF - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/maps/read_software/maps_co5x5_read.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MAPS",
-                    "description": "ASDC Data and Information for MAPS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MAPS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MAPS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cdiac.ess-dive.lbl.gov/epubs/db/db1020/db1020.html",
-                    "description": "CDIAC Overview of Measurement of Air Pollution from Satellites (MAPS) 1994 Correlative Atmospheric Carbon Monoxide Mixing Ratios",
                     "@type": "dcat:Distribution",
+                    "description": "CDIAC Overview of Measurement of Air Pollution from Satellites (MAPS) 1994 Correlative Atmospheric Carbon Monoxide Mixing Ratios",
+                    "downloadURL": "https://cdiac.ess-dive.lbl.gov/epubs/db/db1020/db1020.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MAPS/MAPS_SRL1_CO5X5_HDF/",
-                    "description": "ASDC Direct Data Download for MAPS_SRL1_CO5X5_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MAPS_SRL1_CO5X5_HDF_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MAPS/MAPS_SRL1_CO5X5_HDF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MAPS/MAPS_SRL1_CO5X5_HDF/contents.html",
-                    "description": "OPeNDAP data access for MAPS_SRL1_CO5X5_HDF_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MAPS_SRL1_CO5X5_HDF_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MAPS/MAPS_SRL1_CO5X5_HDF/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1536049390-LARC_ASDC",
+            "issued": "1999-07-12",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/MAPS_SRL1_CO5X5_HDF",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-70.0 -180.0 -70.0 180.0 70.0 180.0 70.0 -180.0 -70.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1994-04-09T00:00:00Z/1994-04-19T23:59:59.999Z",
             "theme": [
                 "MAPS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurement of Air Pollution from Satellites (MAPS) Space Radar Laboratory - 1 (SRL1) Carbon Monoxide 5 degree by 5 degree data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/878/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-12-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
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
-            "identifier": "DASHLINK_878",
             "description": "This paper investigates a non-traditional use of differential current sensor and current sensor to detect intermittent disconnection problems in connectors. An intermittent disconnect, often resulting in an arc, creates an imbalance which is manifested in the current. The traveling wave generated due to the perturbation can be detected using current sensors. This paper shows the feasibility to detect disconnection based on this principle.",
-            "title": "On-line intermittent connector anomaly detection",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Ginart_et_al._-_2011_-_On-line_intermittent_connector_anomaly_detection.pdf",
-                    "description": "Ginart et al. - 2011 - On-line intermittent connector anomaly detection.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Ginart et al. - 2011 - On-line intermittent connector anomaly detection.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Ginart_et_al._-_2011_-_On-line_intermittent_connector_anomaly_detection.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Ginart et al. - 2011 - On-line intermittent connector anomaly detection.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_878",
+            "issued": "2013-12-25",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/878/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "On-line intermittent connector anomaly detection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1894",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fienup-riordan, A., G.V. Frost, R. Nayamin-kelly, U.S. Bhatt, A.S. Hendricks, M. John, and P. Odom. 2021. Alaska's Changing YK Delta: Knowledge Exchange between Elders and Geoscientists, 2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1894",
-            "issued": "2021-11-18",
-            "temporal": "2018-11-14T00:00:00Z/2018-11-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "climate indicators",
-                "cryosphere",
-                "cryospheric indicators",
-                "biospheric indicators",
-                "earth science",
-                "ecological dynamics",
-                "biosphere",
-                "environmental impacts",
-                "human dimensions",
-                "vegetation",
-                "human settlements",
-                "terrestrial hydrosphere indicators",
-                "snow/ice",
-                "population"
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
-            "identifier": "C2170972782-ORNL_CLOUD",
             "description": "This dataset provides a booklet documenting the discussions and outcomes from a knowledge-exchange meeting with Yup'ik elders from the Yukon-Kuskokwim Delta (YKD), western Alaska, community members, and natural scientist to discuss landscape and weather changes that have been observed in their homelands. The meeting was held during November 14-16, 2018. Yup'ik participants represented several YKD villages that occupy very different biophysical environments, and they have lifelong perspectives of environmental conditions and change that predate the era of Earth-observing satellites by many decades. Nearly 16 hours of discussion and testimonials from YKD elders were recorded during the meeting. The booklet is structured according to the environmental change processes that were discussed (e.g., coastal flooding, permafrost thaw, shrub expansion, climate change) and includes narrative summaries, quotations from participants, graphical illustrations, and examples of the field- and remote-sensing-based scientific findings, and map products developed as part of the larger ABoVE project.",
-            "graphic-preview-description": "Aerial view of the Yukon Delta landscape near the village of Emmonak, August 2017. \nSource: Fienup-Riordan et al. (2021)",
-            "title": "Alaska's Changing YK Delta: Knowledge Exchange between Elders and Geoscientists, 2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/YKDelta_EnvChange_InfoExchange_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1894",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1894",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/YKDelta_EnvChange_InfoExchange/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/YKDelta_EnvChange_InfoExchange/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/YKDelta_EnvChange_InfoExchange.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/YKDelta_EnvChange_InfoExchange.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1894",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1894",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/YKDelta_EnvChange_InfoExchange/comp/YKDelta_EnvChange_InfoExchange.pdf",
-                    "description": "Alaska's Changing YK Delta: Knowledge Exchange between Elders and Geoscientists, 2018: YKDelta_EnvChange_InfoExchange.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Alaska's Changing YK Delta: Knowledge Exchange between Elders and Geoscientists, 2018: YKDelta_EnvChange_InfoExchange.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/YKDelta_EnvChange_InfoExchange/comp/YKDelta_EnvChange_InfoExchange.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/YKDelta_EnvChange_InfoExchange_Fig1.png",
-                    "description": "Aerial view of the Yukon Delta landscape near the village of Emmonak, August 2017. \nSource: Fienup-Riordan et al. (2021)",
                     "@type": "dcat:Distribution",
+                    "description": "Aerial view of the Yukon Delta landscape near the village of Emmonak, August 2017. \nSource: Fienup-Riordan et al. (2021)",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/YKDelta_EnvChange_InfoExchange_Fig1.png",
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
+            "graphic-preview-description": "Aerial view of the Yukon Delta landscape near the village of Emmonak, August 2017. \nSource: Fienup-Riordan et al. (2021)",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/YKDelta_EnvChange_InfoExchange_Fig1.png",
+            "identifier": "C2170972782-ORNL_CLOUD",
+            "issued": "2021-11-18",
+            "keyword": [
+                "climate indicators",
+                "cryosphere",
+                "cryospheric indicators",
+                "biospheric indicators",
+                "earth science",
+                "ecological dynamics",
+                "biosphere",
+                "environmental impacts",
+                "human dimensions",
+                "vegetation",
+                "human settlements",
+                "terrestrial hydrosphere indicators",
+                "snow/ice",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1894",
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
             "spatial": "-166.55 59.58 -159.48 63.43",
+            "temporal": "2018-11-14T00:00:00Z/2018-11-16T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Alaska's Changing YK Delta: Knowledge Exchange between Elders and Geoscientists, 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR16-V1.0",
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
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR16) Raw Data Archive is a time-ordered collection of radio science raw data acquired on February 17, 18 and 19, 2011, during he Cassini Extended-Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr16-v1.0_tvde-jypk",
+            "issued": "2021-05-21",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR16-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr16-v1.0_tvde-jypk",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR16) Raw Data Archive is a time-ordered collection of radio science raw data acquired on February 17, 18 and 19, 2011, during he Cassini Extended-Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR16 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TIGR16 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GOES13/CERES/GEO_ED4_NH_V01.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-07-19. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/GOES13/CERES/GEO_ED4_NH_V01.2. https://www.doi.org/10.5067/GOES13/CERES/GEO_ED4_NH_V01.2.",
-            "issued": "2019-01-10",
-            "temporal": "2015-07-01T00:00:00Z/2023-12-25T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-18",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Data Manager",
                 "hasEmail": "mailto:larc@eos.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1587404696-LARC_ASDC",
             "description": "CER_GEO_Ed4_GOE13_NH_V01.2 is the Satellite Cloud and Radiation Property retrieval System (SatCORPS) Clouds and the Earth's Radiant Energy System (CERES) Geostationary Satellite (GEO) Edition 4 Geostationary Operational Environmental Satellite 13 (GOES-13) over the Northern Hemisphere (NH) Version 1.2 data product. Data was collected using the GOES-13 Imager on the GOES-13 Platform.\r\n\r\nNote: Version 1.2 is identical to version 1.0. No changes have been made to the retrieval algorithm.\r\n\r\nThis data set comprises cloud micro-physical and radiation properties derived hourly from GOES-13 geostationary satellite imager data using the Langley Research Center (LaRC) SATCORPS algorithms in support of the CERES project. The cloud microphysical and radiation properties from each active geostationary satellite are merged to create hourly global cloud properties that estimate fluxes between CERES instrument measurements to account for the changing diurnal cycle. The data set is arranged as files for each hour and in netCDF-4 format. The observations are at 4 km resolution (at nadir) and are sub-sampled to 8 km.\r\n\r\nCERES is a key Earth Observing System (EOS) program component. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions follow the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, the proto flight model (PFM), was launched on November 27, 1997, as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit onboard the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched onboard Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched onboard the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched onboard the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "graphic-preview-description": "Mission Logo",
-            "title": "SatCORPS CERES GEO Edition 4 GOES-13 Northern Hemisphere Version 1.2",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES13%2FCERES%2FGEO_ED4_NH_V01.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGOES13%2FCERES%2FGEO_ED4_NH_V01.2",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1587404696-LARC_ASDC",
-                    "description": "Earthdata Search for CER_GEO_Ed4_GOE13_NH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_GEO_Ed4_GOE13_NH_V01.2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1587404696-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GOES13/CERES/GEO_ED4_NH_V01.2",
-                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE13_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_GEO_Ed4_GOE13_NH_V01.2",
+                    "downloadURL": "https://doi.org/10.5067/GOES13/CERES/GEO_ED4_NH_V01.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight\u00a0-\u00a0The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.",
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
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
-                    "description": "Mission Logo",
                     "@type": "dcat:Distribution",
+                    "description": "Mission Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE13_NH_V01.2/",
-                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE13_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_GEO_Ed4_GOE13_NH_V01.2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/GEO/Edition4/GOE13_NH_V01.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE13_NH_V01.2/contents.html",
-                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE13_NH_V01.2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_GEO_Ed4_GOE13_NH_V01.2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/GEO/Edition4/GOE13_NH_V01.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/ceres.png",
+            "identifier": "C1587404696-LARC_ASDC",
+            "issued": "2019-01-10",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/GOES13/CERES/GEO_ED4_NH_V01.2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 -120.0 0.0 -30.0 60.0 -30.0 60.0 -120.0 0.0 -120.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-07-01T00:00:00Z/2023-12-25T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SatCORPS CERES GEO Edition 4 GOES-13 Northern Hemisphere Version 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PLS-5-SUMM-IONBR-48SEC-V1.0",
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
+            "description": "This data set contains the total ion density obtained from Voyager 2 PLS data (voltage range 10-5950 eV/Q) at Uranus by fitting the measured spectra with isotropic Maxwellian distributions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pls-5-summ-ionbr-48sec-v1.0_tvid-aqi2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "uranus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PLS-5-SUMM-IONBR-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pls-5-summ-ionbr-48sec-v1.0_tvid-aqi2",
-            "description": "This data set contains the total ion density obtained from Voyager 2 PLS data (voltage range 10-5950 eV/Q) at Uranus by fitting the measured spectra with isotropic Maxwellian distributions.",
-            "title": "VG2 URA PLS DERIVED SUMMARY ION FIT\n                                      48SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 URA PLS DERIVED SUMMARY ION FIT\n                                      48SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0315-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-24T17:24:50.000 to 2014-09-25T01:15:11.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0315-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0315-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0315-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-09-24T17:24:50.000 to 2014-09-25T01:15:11.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0315 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0315 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D63.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang\r\n. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band2 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D63.061. https://doi.org/10.5067/MODIS/MCD43D63.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "national geospatial data asset",
-                "land surface",
-                "surface radiative properties",
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
-            "identifier": "C2540275688-LPCLOUD",
-            "description": "The MCD43D63 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Nadir BRDF-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D62 through MCD43D68 are the NBAR products of the MCD43D BRDF/Albedo product suite for MODIS bands 1 through 7. The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon.\r\n\r\nMCD43D63 is the NBAR for MODIS band 2. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band2 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D63 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Nadir BRDF-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D62 through MCD43D68 are the NBAR products of the MCD43D BRDF/Albedo product suite for MODIS bands 1 through 7. The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon.\r\n\r\nMCD43D63 is the NBAR for MODIS band 2. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D63.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D63.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D63.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D63.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540275688-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540275688-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.nascom.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aquaTerra&ver=C6",
-                    "description": "Product Quality Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Product Quality Documentation",
+                    "downloadURL": "https://landweb.nascom.nasa.gov/cgi-bin/QA_WWW/qaFlagPage.cgi?sat=aquaTerra&ver=C6",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D63.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D63.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D63",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D63",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D63.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D63.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540275688-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "national geospatial data asset",
+                "land surface",
+                "surface radiative properties",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D63.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band2 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/828/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-07-29",
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
-            "identifier": "DASHLINK_828",
             "description": "Composite structures are gaining importance for use in the aerospace industry. Compared to metallic structures their behavior is less well understood. This lack of understanding may pose constraints on their use. One possible way to deal with some of the risks associated with potential failure is to perform in-situ monitoring to detect precursors of failures. Prognostic algorithms can be used to predict impending failures. They require large amounts of training data to build and tune damage model for making useful predictions. One of the key aspects is to get confirmatory feedback from data as damage progresses. These kinds of data are rarely available from actual systems. The next possible resource to collect such data is an accelerated aging platform. To that end this paper describes a fatigue cycling experiment with the goal to stress carbon-carbon composite coupons with various layups. Piezoelectric disc sensors were used to periodically interrogate the system. Analysis showed distinct differences in the signatures of growing failures between data collected at conditions. Periodic X-radiographs were taken to assess the damage ground truth. Results after signal processing showed clear trends of damage growth that were correlated to damage assessed from the X-ray images.",
-            "title": "Accelerated Aging Experiments for Prognostics of Damage Growth in Composite Materials",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_IWSHM_Composites.pdf",
-                    "description": "2011_IWSHM_Composites.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2011_IWSHM_Composites.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2011_IWSHM_Composites.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2011_IWSHM_Composites.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_828",
+            "issued": "2013-07-29",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/828/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Accelerated Aging Experiments for Prognostics of Damage Growth in Composite Materials"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA208",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-01-15. AIRS2SUP. Version 006. AIRS/Aqua L2 Support Retrieval (AIRS-only) V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA208. https://disc.gsfc.nasa.gov/datacollection/AIRS2SUP_006.html. Digital Science Data.",
-            "issued": "2002-08-30",
-            "temporal": "2002-08-30T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-21",
-            "references": [
-                "https://doi.org/10.5194/acp-14-399-2014",
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.1002/2014JD022551",
-                "https://doi.org/10.1002/2014JD02166",
-                "https://doi.org/10.1002/2016JD024806",
-                "https://doi.org/10.1002/2015JD024008",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.1109/TGRS.2002.808236"
-            ],
-            "keyword": [
-                "atmosphere",
-                "surface thermal properties",
-                "earth science",
-                "atmospheric pressure",
-                "air quality",
-                "surface radiative properties",
-                "land surface",
-                "clouds",
-                "atmospheric water vapor",
-                "oceans",
-                "ocean temperature",
-                "atmospheric radiation",
-                "precipitation",
-                "atmospheric temperature",
-                "altitude",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1243477382-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. This product is similar to AIRX2SUP. It is a new product produced using AIRS IR only because the radiometric noise in AMSU channel 4 started to increase significantly (since June 2007). The Support Product includes higher vertical resolution profiles of the quantities found in the Standard Product, plus intermediate outputs (e.g., microwave-only retrieval), research products such as the abundance of trace gases, and detailed quality assessment information. The Support Product profiles contain 100 levels between 1100 and .016 mb; this higher resolution simplifies the generation of radiances using forward models, though the vertical information content is no greater than that in the Standard Product profiles. The intended users of the Support Product are researchers interested in generating forward radiance or in examining research products, and the AIRS algorithm development team. The Support Product is generated at all locations as Standard Products. An AIRS granule has been set as 6 minutes of data, 30 footprints cross track by 45 lines along track. There are 240 granules per day, with an orbit repeat cycle of approximately 16 day.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRS2SUP",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "graphic-preview-description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS-only) H2O Column Density Profile and Cloud Fraction.",
-            "title": "AIRS/Aqua L2 Support Retrieval (AIRS-only) V006 (AIRS2SUP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2SUP_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA208",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA208",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2SUP_006.png",
-                    "description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS-only) H2O Column Density Profile and Cloud Fraction.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS-only) H2O Column Density Profile and Cloud Fraction.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2SUP_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2SUP_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRS2SUP_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRS2SUP.006/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level2/AIRS2SUP.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRS2SUP.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://airsl2.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level2/AIRS2SUP.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2SUP+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRS2SUP+006",
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
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/sites/default/files/atbd/20070301_L2_ATBD_signed.pdf",
-                    "description": "AIRS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS ATBD",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/sites/default/files/atbd/20070301_L2_ATBD_signed.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample plot of AIRS Level 2 Support Retrieval (AIRS-only) H2O Column Density Profile and Cloud Fraction.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRS2SUP_006.png",
+            "identifier": "C1243477382-GES_DISC",
+            "issued": "2002-08-30",
+            "keyword": [
+                "atmosphere",
+                "surface thermal properties",
+                "earth science",
+                "atmospheric pressure",
+                "air quality",
+                "surface radiative properties",
+                "land surface",
+                "clouds",
+                "atmospheric water vapor",
+                "oceans",
+                "ocean temperature",
+                "atmospheric radiation",
+                "precipitation",
+                "atmospheric temperature",
+                "altitude",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA208",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-14-399-2014",
+                "https://doi.org/10.1117/1.JRS.8.084994",
+                "https://doi.org/10.1002/2014JD022551",
+                "https://doi.org/10.1002/2014JD02166",
+                "https://doi.org/10.1002/2016JD024806",
+                "https://doi.org/10.1002/2015JD024008",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.1109/TGRS.2002.808236"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRS2SUP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L2 Support Retrieval (AIRS-only) V006 (AIRS2SUP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://planetarynames.wr.usgs.gov/Page/Images",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kelly",
+                "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
+            },
+            "description": "These images display asteriods documented and approved by the International Astronomical Union (IAU).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/dactyl.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-166",
             "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "steins",
                 "asteriods",
@@ -1436912,338 +1436924,304 @@
                 "mathilde",
                 "vesta"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kelly",
-                "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
-            },
+            "landingPage": "http://planetarynames.wr.usgs.gov/Page/Images",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
             },
-            "identifier": "OCIO-Fitara-166",
-            "description": "These images display asteriods documented and approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Asteroids: Dactyl",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/dactyl.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Asteroids: Dactyl"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0740-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-30T05:27:25.000 to 2015-04-30T09:19:20.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0740-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0740-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0740-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-30T05:27:25.000 to 2015-04-30T09:19:20.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0740 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0740 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A15C-L-XRFS-2-SURFACE-XRAY-COUNTS-V1.0",
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
-                "apollo 15"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains two tables of time-ordered, raw event count rates acquired by the Apollo 15 X-Ray Fluorescence Spectrometer from 30 July to 4 August 1971 during lunar orbit.  The tables include counts for all channels of the three proportional counters (unfiltered, magnesium filter, aluminum filter) and the solar monitor.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a15c-l-xrfs-2-surface-xray-counts-v1.0_tvug-txbq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "apollo 15"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A15C-L-XRFS-2-SURFACE-XRAY-COUNTS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a15c-l-xrfs-2-surface-xray-counts-v1.0_tvug-txbq",
-            "description": "This dataset contains two tables of time-ordered, raw event count rates acquired by the Apollo 15 X-Ray Fluorescence Spectrometer from 30 July to 4 August 1971 during lunar orbit.  The tables include counts for all channels of the three proportional counters (unfiltered, magnesium filter, aluminum filter) and the solar monitor.",
-            "title": "APOLLO 15 XRFS LUNAR SURFACE X-RAY\n      COUNTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "APOLLO 15 XRFS LUNAR SURFACE X-RAY\n      COUNTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-NIMS-3-GASPRASPEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data volume contains radiometrically corrected point spectra of asteroid 951 as acquired by the Galileo spacecraft Near Infrared Mapping Spectrometer (NIMS) on October 29, 1991. They record the spectra collected as the Galileo spacecraft approached the target asteroid. These data are products of the calibration of the raw data number files gap015tn.qub, gap035tn.qub, gap036tn.qub, gap037tn.qub, and gap038tn.qub (DATA SET ID ='GO-A-NIMS-3 TUBE-V1.0') with calibration factors acquired during the first Earth/Moon encounter of the Galileo mission.  These raw data .qub files are archived in the Imaging Node of the NASA Planetary Data System (PDS). The calibrated spectra consist of radiance measurements for wavelengths between 0.7 - 5.2 micrometers.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-nims-3-gaspraspec-v1.0_tvwf-rxk8",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "gaspra",
                 "951 gaspra",
                 "galileo",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-NIMS-3-GASPRASPEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-nims-3-gaspraspec-v1.0_tvwf-rxk8",
-            "description": "This data volume contains radiometrically corrected point spectra of asteroid 951 as acquired by the Galileo spacecraft Near Infrared Mapping Spectrometer (NIMS) on October 29, 1991. They record the spectra collected as the Galileo spacecraft approached the target asteroid. These data are products of the calibration of the raw data number files gap015tn.qub, gap035tn.qub, gap036tn.qub, gap037tn.qub, and gap038tn.qub (DATA SET ID ='GO-A-NIMS-3 TUBE-V1.0') with calibration factors acquired during the first Earth/Moon encounter of the Galileo mission.  These raw data .qub files are archived in the Imaging Node of the NASA Planetary Data System (PDS). The calibrated spectra consist of radiance measurements for wavelengths between 0.7 - 5.2 micrometers.",
-            "title": "NIMS RADIANCE POINT SPECTRA OF GASPRA\n        V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NIMS RADIANCE POINT SPECTRA OF GASPRA\n        V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Aerosol_AircraftInSitu_ER2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Aerosol_AircraftInSitu_ER2_Data_1.",
-            "issued": "2022-09-07",
-            "temporal": "1998-11-10T00:00:00Z/2000-03-18T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-07",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "clouds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Darrel Baumgardner",
                 "hasEmail": "mailto:darrel.baumgardner@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836791-LARC_ASDC",
             "description": "SOLVE1_Aerosol_AircraftInSItu_ER2_Data is the in-situ aerosol data for the ER-2 aircraft collected during the SAGE III Ozone Loss and Validation Experiment (SOLVE). Data were collected by instruments such as the Multiple-Angle Aerosol Spectrometer Probe (MASPR), Condensation Nuclei Counter (CNC), Focused Cavity Aerosol Spectrometer II (FCAS II), and the Nucleation-Mode Aerosol Size Spectrometer II (N-MASS). Data collection for this product is complete. \r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE I ER-2 Aircraft In-situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_Aerosol_AircraftInSitu_ER2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE1_Aerosol_AircraftInSitu_ER2_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Aerosol_AircraftInSitu_ER2_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE1_Aerosol_AircraftInSitu_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE1_Aerosol_AircraftInSitu_ER2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE/Aerosol_AircraftInSitu_ER2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836791-LARC_ASDC",
+            "issued": "2022-09-07",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE1_Aerosol_AircraftInSitu_ER2_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>11.0 -180.0 11.0 180.0 90.0 180.0 90.0 -180.0 11.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1998-11-10T00:00:00Z/2000-03-18T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE I ER-2 Aircraft In-situ Aerosol Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0",
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
+            "description": "This data set includes data from the Low Field Magnetometer (LFM) in the solar wind the near the Uranus encounter. The actual encounter data (1986-01-24T07:00:00  -> 1986-01-25T04:00:00) are provided in the Uranus Longitude coordinate system.  The magnetometer data in the solar wind are given in Heliographic coordinates and the data have been averaged from the 60ms instrument sample rate to a 1.92 second resampled rate.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-mag-4-rdr-hgcoords-1.92sec-v1.0_tvxv-h8p9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "uranus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-MAG-4-RDR-HGCOORDS-1.92SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-mag-4-rdr-hgcoords-1.92sec-v1.0_tvxv-h8p9",
-            "description": "This data set includes data from the Low Field Magnetometer (LFM) in the solar wind the near the Uranus encounter. The actual encounter data (1986-01-24T07:00:00  -> 1986-01-25T04:00:00) are provided in the Uranus Longitude coordinate system.  The magnetometer data in the solar wind are given in Heliographic coordinates and the data have been averaged from the 60ms instrument sample rate to a 1.92 second resampled rate.",
-            "title": "VG2 URA MAG RESAMP RDR HELIOGRAPHIC\n                                     COORDINATES 1.92SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 URA MAG RESAMP RDR HELIOGRAPHIC\n                                     COORDINATES 1.92SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114198-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TOMS Science Team. TOMSEPL3dtoz. Version 008. TOMS Earth Probe Total Column Ozone Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dtoz_008.html. Digital Science Data.",
-            "issued": "2004-04-30",
-            "temporal": "1996-07-22T00:00:00Z/2005-12-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-04-30",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
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
-            "identifier": "C1237114198-GES_DISC",
-            "description": "This Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains total column ozone values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
-            "release-place": "Greenbelt, MD",
-            "series-name": "TOMSEPL3dtoz",
             "creator": "TOMS Science Team",
-            "title": "TOMS Earth Probe Total Column Ozone Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dtoz) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPL3dtoz_008.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This Earth Probe (EP) Total Ozone Mapping Spectrometer (TOMS) version 8 daily global gridded data product contains total column ozone values. The data are mapped to a global grid of size 180 x 288 with a lat-long resolution of 1.00 x 1.25 degrees. These data are stored in an ASCII format.\n\nThe TOMS data were produced by the Laboratory for Atmospheres at NASA Goddard Space Flight Center (Code 614).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1437252,557 +1437230,555 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dtoz_008.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TOMSEPL3dtoz_008.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPL3dtoz.008/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/EarthProbe_TOMS_Level3/TOMSEPL3dtoz.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPL3dtoz",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TOMSEPL3dtoz",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/EARTHPROBE_USERGUIDE.PDF",
-                    "description": "Earth Probe TOMS Data Product User's Guide.",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Probe TOMS Data Product User's Guide.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TOMS/EARTHPROBE_USERGUIDE.PDF",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TOMSEPL3dtoz_008.png",
+            "identifier": "C1237114198-GES_DISC",
+            "issued": "2004-04-30",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1237114198-GES_DISC.html",
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
+            "series-name": "TOMSEPL3dtoz",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1996-07-22T00:00:00Z/2005-12-14T23:59:59.999Z",
             "theme": [
                 "TOMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOMS Earth Probe Total Column Ozone Daily L3 Global 1 deg x 1.25 deg Lat/Lon Grid V008 (TOMSEPL3dtoz) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-RANGE-OPS-V1.0",
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
-                "phoenix"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Robotic Arm Camera (RAC) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This RAC Imaging Operations RDR data set contains range data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-range-ops-v1.0_tw4c-92mf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-RANGE-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-range-ops-v1.0_tw4c-92mf",
-            "description": "The Robotic Arm Camera (RAC) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This RAC Imaging Operations RDR data set contains range data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 5 RANGE OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 5 RANGE OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-NORMAL-OPS-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Operations RDR  data set contains normal data from the Surface Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-normal-ops-v1.0_tw54-i74f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-NORMAL-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-normal-ops-v1.0_tw54-i74f",
-            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Operations RDR  data set contains normal data from the Surface Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER \n                                     5 NORMAL OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER \n                                     5 NORMAL OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-3N321",
             "citation": "CYGNSS. 2024-08-30. CYGNSS Level 3 MRG Science Data Record Near Real Time. Version 3.2.1. CYGNSS Level 3 MRG Science Data Record Near Real Time Version 3.2.1. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-3N321. https://cygnss.engin.umich.edu/.",
-            "issued": "2021-12-12",
-            "temporal": "2024-06-17T00:00:00Z/2024-08-26T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-12",
-            "references": [
-                "https://doi.org/10.1109/JSTARS.2024.3379934"
-            ],
-            "keyword": [
-                "ocean winds",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "identifier": "C3168810773-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains the version 3.2.1 CYGNSS Level 3 Merged (MRG) Science Data Record Near Real Time (NRT) Storm Wind Speed derived from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. It combines CYGNSS storm-centric gridded (SCG) wind speeds, which are derived from the L2 Young Seas Limited Fetch (YSLF) winds for a region surrounding a given tropical cyclone (TC), with L2 Fully Developed Seas (FDS) winds away from the TC center on a 0.2x0.2 degree latitude by longitude equirectangular grid. \r\n<br><br>\r\nL3 MRG is a product which combines the L2 FDS and YSLF winds and eliminates the need to choose between them depending on sea state development and the proximity to storms. The data are provided in netCDF-4 format and starts from the September 1, 2024 through the present with an approximate latency between 2 and 24 hours. A tapered weighted averaging scheme is used centered on the 25 m/s wind radius of the storm. The 34 knot wind radius (R34) algorithm has been updated for v3.2.1 release to center around the NHC/JTWC reported storm center instead of the CYGNSS Vmax location The algorithm produces global (+/- 40 deg latitude) wind speeds reported on a 0.1x0.1 deg grid every 6 hours for each tropical cyclone, although some 6-hourly increments may be missing if there are an insufficient number of satellite overpasses of the storm during that time interval. The netCDF files are output on a storm-by-storm basis. \r\n<br><br>\r\nThe CYGNSS is a NASA Earth System Science Pathfinder Mission that is intended to collect the first frequent space\u2010based measurements of surface wind speeds in the inner core of tropical cyclones. Made up of a constellation of eight micro-satellites, the observatories provide nearly gap-free Earth coverage using an orbital inclination of approximately 35\u00b0 from the equator, with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours. This inclination allows CYGNSS to measure ocean surface winds between approximately 38\u00b0 N and 38\u00b0 S latitude. This range includes the critical latitude band for tropical cyclone formation and movement.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 3 MRG Science Data Record Near Real Time",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 3 MRG Science Data Record Near Real Time Version 3.2.1",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_MRG_V3.2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the version 3.2.1 CYGNSS Level 3 Merged (MRG) Science Data Record Near Real Time (NRT) Storm Wind Speed derived from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. It combines CYGNSS storm-centric gridded (SCG) wind speeds, which are derived from the L2 Young Seas Limited Fetch (YSLF) winds for a region surrounding a given tropical cyclone (TC), with L2 Fully Developed Seas (FDS) winds away from the TC center on a 0.2x0.2 degree latitude by longitude equirectangular grid. \r\n<br><br>\r\nL3 MRG is a product which combines the L2 FDS and YSLF winds and eliminates the need to choose between them depending on sea state development and the proximity to storms. The data are provided in netCDF-4 format and starts from the September 1, 2024 through the present with an approximate latency between 2 and 24 hours. A tapered weighted averaging scheme is used centered on the 25 m/s wind radius of the storm. The 34 knot wind radius (R34) algorithm has been updated for v3.2.1 release to center around the NHC/JTWC reported storm center instead of the CYGNSS Vmax location The algorithm produces global (+/- 40 deg latitude) wind speeds reported on a 0.1x0.1 deg grid every 6 hours for each tropical cyclone, although some 6-hourly increments may be missing if there are an insufficient number of satellite overpasses of the storm during that time interval. The netCDF files are output on a storm-by-storm basis. \r\n<br><br>\r\nThe CYGNSS is a NASA Earth System Science Pathfinder Mission that is intended to collect the first frequent space\u2010based measurements of surface wind speeds in the inner core of tropical cyclones. Made up of a constellation of eight micro-satellites, the observatories provide nearly gap-free Earth coverage using an orbital inclination of approximately 35\u00b0 from the equator, with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours. This inclination allows CYGNSS to measure ocean surface winds between approximately 38\u00b0 N and 38\u00b0 S latitude. This range includes the critical latitude band for tropical cyclone formation and movement.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-3N321",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-3N321",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://cygnss.engin.umich.edu/",
-                    "description": "CYGNSS Mission Page at University of Michigan",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Mission Page at University of Michigan",
+                    "downloadURL": "https://cygnss.engin.umich.edu/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_MRG_V3.2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_MRG_V3.2.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3168810773-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3168810773-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3168810773-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3168810773-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0412_L3_MRG_ATBD_R6.pdf",
-                    "description": "Level 3 Merged Gridded Wind Speed Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Level 3 Merged Gridded Wind Speed Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0412_L3_MRG_ATBD_R6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0408-3_Level_3_Merged_Storm_netCDF_Data_Dictionary.xlsx",
-                    "description": "CYGNSS L3 MRG V3.2 netCDF Data Dictionary",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS L3 MRG V3.2 netCDF Data Dictionary",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0408-3_Level_3_Merged_Storm_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/06/CYGNSS_Handbook_April2016.pdf",
-                    "description": "Deriving Surface Winds from Tropical Cyclones",
                     "@type": "dcat:Distribution",
+                    "description": "Deriving Surface Winds from Tropical Cyclones",
+                    "downloadURL": "https://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/06/CYGNSS_Handbook_April2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0409-1_Level_3_Merged_Storm_Storage_Scheme.pdf",
-                    "description": "Level 3 Merged Storm Storage Scheme",
                     "@type": "dcat:Distribution",
+                    "description": "Level 3 Merged Storm Storage Scheme",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0409-1_Level_3_Merged_Storm_Storage_Scheme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org//10.1175/BAMS-D-14-00218.1",
-                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny. 2015. New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection, Bull. Amer. Meteor. Soc.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny. 2015. New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection, Bull. Amer. Meteor. Soc.",
+                    "downloadURL": "https://doi.org//10.1175/BAMS-D-14-00218.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org//10.1175/BAMS-D-18-0337.1",
-                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser. 2019. In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites, Bull. Amer. Meteor. Soc.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser. 2019. In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites, Bull. Amer. Meteor. Soc.",
+                    "downloadURL": "https://doi.org//10.1175/BAMS-D-18-0337.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3998/mpub.12741920",
-                    "description": "Ruf, C., D. McKague, D. Posselt, S. Gleason, M.P. Clarizia, V. Zavorotny, T. Butler, J. Redfern, W. Wells, M. Morris, J. Crespo, C. Chew, E. Small, D. Pasqual, T. Wang, A. Warnock, D. Mayers, M. Al-Khaldi, A. O\u2019Brien. 2022. CYGNSS Handbook (2nd ed.), Michigan Publishing Services, Ann Arbor, MI, ISBN 978-1-60785-549-1",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., D. McKague, D. Posselt, S. Gleason, M.P. Clarizia, V. Zavorotny, T. Butler, J. Redfern, W. Wells, M. Morris, J. Crespo, C. Chew, E. Small, D. Pasqual, T. Wang, A. Warnock, D. Mayers, M. Al-Khaldi, A. O\u2019Brien. 2022. CYGNSS Handbook (2nd ed.), Michigan Publishing Services, Ann Arbor, MI, ISBN 978-1-60785-549-1",
+                    "downloadURL": "https://doi.org/10.3998/mpub.12741920",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org//10.1175/JAMC-D-22-0054.1",
-                    "description": "Mayers, D. R., C. S. Ruf, A. M. Warnock. 2024. CYGNSS Storm-Centric Tropical Cyclone Gridded Wind Speed Product, J. Appl. Meteor. Climatol",
                     "@type": "dcat:Distribution",
+                    "description": "Mayers, D. R., C. S. Ruf, A. M. Warnock. 2024. CYGNSS Storm-Centric Tropical Cyclone Gridded Wind Speed Product, J. Appl. Meteor. Climatol",
+                    "downloadURL": "https://doi.org//10.1175/JAMC-D-22-0054.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org//10.1109/JSTARS.2024.3379934",
-                    "description": "Warnock, A. M., C. S. Ruf, A. Russel, M. Al-Khaldi, R. Balasubramaniam, 2024. CYGNSS Level 3 Merged Wind Speed Data Product for Storm Force and Surrounding Environmental Winds, J. Selected Topics Appl. Earth Obs.",
                     "@type": "dcat:Distribution",
+                    "description": "Warnock, A. M., C. S. Ruf, A. Russel, M. Al-Khaldi, R. Balasubramaniam, 2024. CYGNSS Level 3 Merged Wind Speed Data Product for Storm Force and Surrounding Environmental Winds, J. Selected Topics Appl. Earth Obs.",
+                    "downloadURL": "https://doi.org//10.1109/JSTARS.2024.3379934",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_MRG_V3.2.jpg",
+            "identifier": "C3168810773-POCLOUD",
+            "issued": "2021-12-12",
+            "keyword": [
+                "ocean winds",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-3N321",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-12-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1109/JSTARS.2024.3379934"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 3 MRG Science Data Record Near Real Time",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2024-06-17T00:00:00Z/2024-08-26T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 3 MRG Science Data Record Near Real Time Version 3.2.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-SESAME-3-PHC-V1.0",
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
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains calibrated data (CODMAC level 3) from the SESAME instrument onboard ROSETTA Lander, acquired during the PHC phase. It also contains documentation which describes the SESAME experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-sesame-3-phc-v1.0_twa7-cus7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-SESAME-3-PHC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-sesame-3-phc-v1.0_twa7-cus7",
-            "description": "This archive contains calibrated data (CODMAC level 3) from the SESAME instrument onboard ROSETTA Lander, acquired during the PHC phase. It also contains documentation which describes the SESAME experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL SESAME 3 PHC\n                            V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER CAL SESAME 3 PHC\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/3FGX7G40IDDP",
             "citation": "Indalecio Y. Galicinao. 2024-01-24. GEOS3STST. Version 001. GEOS-3 Satellite-to-Satellite Tracking Data. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/3FGX7G40IDDP. https://disc.gsfc.nasa.gov/datacollection/GEOS3STST_001.html. Digital Science Data.",
-            "issued": "2024-01-04",
-            "temporal": "1975-04-13T00:00:00Z/1976-04-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-04",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "geodetics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "Indalecio Y. Galicinao",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2829925415-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "619"
-            },
             "description": "GEOS3STST is the satellite-to-satellite tracking data product which contains observations, obtained from the S-band transponders on GEOS 3 relayed by the ATS 6 spacecraft to various ground stations, used for geodetic studies. Data are available for the time period from 1975-04-13 to 1976-04-28 in sixteen files, written in ASCII text, where each measurement is recorded as two lines of text.\\n\\nThe principal investigator for the Satellite-to-Satellite Tracking experiment was Indalecio Y. Galicinao from NASA/GSFC.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GEOS3STST",
-            "creator": "Indalecio Y. Galicinao",
-            "title": "GEOS-3 Satellite-to-Satellite Tracking Data V001 (GEOS3STST) at GES DISC",
-            "graphic-preview-description": "GEOS-3 satellite.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GEOS3STST_Sample.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3FGX7G40IDDP",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3FGX7G40IDDP",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GEOS3STST_Sample.jpg",
-                    "description": "GEOS-3 satellite.",
                     "@type": "dcat:Distribution",
+                    "description": "GEOS-3 satellite.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GEOS3STST_Sample.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GEOS3STST_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GEOS3STST_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GEOS/GEOS3STST.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GEOS/GEOS3STST.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GEOS3STST_001",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GEOS3STST_001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GEOS/GEOS3STST.001/doc/README.GEOS3STST.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/GEOS/GEOS3STST.001/doc/README.GEOS3STST.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DSC_0396.pdf",
-                    "description": "A User's Guide for Satellite to Satellite System Observations and Data Formats",
                     "@type": "dcat:Distribution",
+                    "description": "A User's Guide for Satellite to Satellite System Observations and Data Formats",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DSC_0396.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GEOS/GEOS_Inventory.xlsx",
-                    "description": "GEOS Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "GEOS Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GEOS/GEOS_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "GEOS-3 satellite.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GEOS3STST_Sample.jpg",
+            "identifier": "C2829925415-GES_DISC",
+            "issued": "2024-01-04",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/3FGX7G40IDDP",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-01-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "619"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GEOS3STST",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1975-04-13T00:00:00Z/1976-04-28T23:59:59.999Z",
             "theme": [
                 "EOSDIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEOS-3 Satellite-to-Satellite Tracking Data V001 (GEOS3STST) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0524-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-05T23:53:20.000 to 2015-01-06T12:00:49.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0524-v1.0_twbn-25pi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0524-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0524-v1.0_twbn-25pi",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-05T23:53:20.000 to 2015-01-06T12:00:49.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0524 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0524 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-LECP-4-15MIN",
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
+            "description": "THIS DATA SET CONSISTS OF RESAMPLED DATA FROM THE LOW ENERGY CHARGED PARTICLE (LECP) EXPERIMENT ON VOYAGER 1 WHILE THE SPACECRAFT WAS IN THE VICINITY OF SATURN. THIS INSTRUMENT MEASURES THE INTENSITIES OF IN-SITU CHARGED PARTICLES (>26 KEV ELECTRONS AND >30 KEV IONS) WITH VARIOUS LEVELS OF DISCRIMINATION BASED ON ENERGY, MASS SPECIES, AND ANGULAR ARRIVAL DIRECTION. A SUBSET OF ALMOST 100 LECP CHANNELS ARE INCLUDED WITH THIS DATA SET. THE LECP DATA ARE GLOBALLY CALIBRATED TO THE EXTENT POSSIBLE (SEE BELOW) AND THEY ARE TIME AVERAGED TO ABOUT 15 MINUTE TIME INTERVALS WITH THE EXACT BEGINNING AND ENDING TIMES FOR THOSE INTERVALS MATCHING THE LECP INSTRUMENTAL CYCLE PERIODS (THE ANGULAR SCANNING PERIODS). THE LECP INSTUMENT HAS A ROTATING HEAD FOR OBTAINING ANGULAR ANISOTROPY MEASUREMENTS OF THE MEDIUM ENERGY CHARGED PARTICLES THAT IT MEASURES. THE CYCLE TIME FOR THE ROTATION IF VARIABLE, BUT DURING ENCOUNTERS IT IS ALWAYS FASTER THAN 15 MINUTES. THUS, THE FULL ANGULAR ANISOTROPY INFORMATION IS PRESERVED WITH THIS DATA. THE DATA IS IN THE FORM OF 'RATE' DATA WHICH HAS NOT BEEN CONVERTED TO THE USUAL PHYSICAL UNITS. THE REASON IS THAT SUCH A CONVERSION WOULD DEPEND ON UNCERTAIN DETERMINATIONS SUCH AS THE MASS SPECIES OF THE PARTICLES AND THE LEVEL OF BACKGROUND. BOTH MASS SPECIES AND BACKGROUND ARE GENERALLY DETERMINED FROM CONTEXT DURING THE STUDY OF PARTICULAR REGIONS. TO CONVERT 'RATE' TO 'INTENSITY' FOR A PARTICULAR CHANNEL ONE PERFORMS THE FOLLOWING TASKS: 1) DECIDE ON THE LEVEL OF BACKGROUND CONTAMINATION AND SUBTRACT THAT OFF THE GIVEN RATE LEVEL. BACKGROUND IS TO BE DETERMINED FROM CONTEXT AND FROM MAKING USE OF SECTOR 8 RATES (SECTOR 8 HAS A 2 mm AL SHIELD COVERING IT). 2) DIVIDE THE BACKGROUND CORRECTED RATE BY THE CHANNEL GEOMETRIC FACTOR AND BY THE ENERGY BANDPASS OF THE CHANNEL. THE GEOMETRIC FACTOR IS FOUND IN ENTRY 'channel_geometric_ factor' AS ASSOCIATED WITH EACH CHANNEL 'channel_id'. TO DETERMINE THE ENERGY BANDPASS, ONE MUST JUDGE THE MASS SPECIES OF THE OF THE DETECTED PARTICLES (FOR IONS BUT NOT FOR ELECTRONS). THE ENERGY BAND PASSES ARE GIVEN IN ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPENERGY', AND ARE GIVEN IN THE FORM 'ENERGY/NUCLEON'. FOR CHANNELS THAT BEGIN THEIR NAMES WITH THE DESIGNATIONS 'CH' THESE BANDPASSES CAN BE USED ON MASS SPECIES THAT ARE ACCEPTED INTO THAT CHANNEL (SEE ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPCHANZ', WHICH GIVE THE MINIMUM AND MAXIMUM 'Z' VALUE ACCEPTED -- THESE ENTRIES ARE BLANK FOR ELECTRON CHANNELS). FOR OTHER CHANNELS THE GIVEN BANDPASS REFERS ONLY TO THE LOWEST 'Z' VALUE ACCEPTED. THE BANDPASSES FOR OTHER 'Z' VALUES ARE NOT ALL KNOWN, BUT SOME ARE GIVEN IN THE LITERATURE (E.G. KRIMIGIS ET AL., 1979). THE FINAL PRODUCT OF THESE INSTRUCTIONS WILL BE THE PARTICLE INTENSITY WITH THE UNITS: COUNTS/(CM**2.STR.SEC.KEV). SOME CHANNELS ARE SUBJECT TO SERIOUS CONTAMINATIONS, AND MANY OF THESE CONTAMINATIONS CANNOT BE REMOVED EXCEPT WITH A REGION-BY-REGION ANALYSIS, WHICH HAS NOT BEEN DONE FOR THIS DATA. THUS, TO USE THIS DATA IT IS ABSOLUTELY VITAL THAT THE CONTAMINATION TYPES ('contamination_id' , 'contamination_desc') AND THE LEVELS OF CONTAMINATION ('data_quality_id' CORRESPONDING TO THE DEFINITIONS 'data_quality_desc') BE CAREFULLY EXAMINED FOR ALL REGIONS OF STUDY. A DEAD TIME CORRECTION PROCEDURE HAS BEEN APPLIED IN AN ATTEMPT TO CORRECT THE LINEAR EFFECTS OF DETECTOR OVERDRIVE (PULSE-PILEUP). THIS PROCEDURE DOES NOT FIX SEVERELY OVERDRIVEN DETECTORS. A PROCEDURE IS AVAILABLE FOR CORRECTING VOYAGER 2 LECP ELECTRON CONTAMINATION OF LOW ENERGY ION CHANNELS, BUT ITS EFFECTIVENESS HAS BEEN EVALUATED ONLY FOR THE URANUS DATA SET. THUS, CORRECTIONS HAVE BEEN APPLIED ONLY TO THE URANUS DATA SET. Also included with this data are one standard deviation statistical uncertainties for the directional data (sectors 1 through 8) expressed as a percent. Unknown values are generally coded as su",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-lecp-4-15min_twbs-ta6k",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-LECP-4-15MIN",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-lecp-4-15min_twbs-ta6k",
-            "description": "THIS DATA SET CONSISTS OF RESAMPLED DATA FROM THE LOW ENERGY CHARGED PARTICLE (LECP) EXPERIMENT ON VOYAGER 1 WHILE THE SPACECRAFT WAS IN THE VICINITY OF SATURN. THIS INSTRUMENT MEASURES THE INTENSITIES OF IN-SITU CHARGED PARTICLES (>26 KEV ELECTRONS AND >30 KEV IONS) WITH VARIOUS LEVELS OF DISCRIMINATION BASED ON ENERGY, MASS SPECIES, AND ANGULAR ARRIVAL DIRECTION. A SUBSET OF ALMOST 100 LECP CHANNELS ARE INCLUDED WITH THIS DATA SET. THE LECP DATA ARE GLOBALLY CALIBRATED TO THE EXTENT POSSIBLE (SEE BELOW) AND THEY ARE TIME AVERAGED TO ABOUT 15 MINUTE TIME INTERVALS WITH THE EXACT BEGINNING AND ENDING TIMES FOR THOSE INTERVALS MATCHING THE LECP INSTRUMENTAL CYCLE PERIODS (THE ANGULAR SCANNING PERIODS). THE LECP INSTUMENT HAS A ROTATING HEAD FOR OBTAINING ANGULAR ANISOTROPY MEASUREMENTS OF THE MEDIUM ENERGY CHARGED PARTICLES THAT IT MEASURES. THE CYCLE TIME FOR THE ROTATION IF VARIABLE, BUT DURING ENCOUNTERS IT IS ALWAYS FASTER THAN 15 MINUTES. THUS, THE FULL ANGULAR ANISOTROPY INFORMATION IS PRESERVED WITH THIS DATA. THE DATA IS IN THE FORM OF 'RATE' DATA WHICH HAS NOT BEEN CONVERTED TO THE USUAL PHYSICAL UNITS. THE REASON IS THAT SUCH A CONVERSION WOULD DEPEND ON UNCERTAIN DETERMINATIONS SUCH AS THE MASS SPECIES OF THE PARTICLES AND THE LEVEL OF BACKGROUND. BOTH MASS SPECIES AND BACKGROUND ARE GENERALLY DETERMINED FROM CONTEXT DURING THE STUDY OF PARTICULAR REGIONS. TO CONVERT 'RATE' TO 'INTENSITY' FOR A PARTICULAR CHANNEL ONE PERFORMS THE FOLLOWING TASKS: 1) DECIDE ON THE LEVEL OF BACKGROUND CONTAMINATION AND SUBTRACT THAT OFF THE GIVEN RATE LEVEL. BACKGROUND IS TO BE DETERMINED FROM CONTEXT AND FROM MAKING USE OF SECTOR 8 RATES (SECTOR 8 HAS A 2 mm AL SHIELD COVERING IT). 2) DIVIDE THE BACKGROUND CORRECTED RATE BY THE CHANNEL GEOMETRIC FACTOR AND BY THE ENERGY BANDPASS OF THE CHANNEL. THE GEOMETRIC FACTOR IS FOUND IN ENTRY 'channel_geometric_ factor' AS ASSOCIATED WITH EACH CHANNEL 'channel_id'. TO DETERMINE THE ENERGY BANDPASS, ONE MUST JUDGE THE MASS SPECIES OF THE OF THE DETECTED PARTICLES (FOR IONS BUT NOT FOR ELECTRONS). THE ENERGY BAND PASSES ARE GIVEN IN ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPENERGY', AND ARE GIVEN IN THE FORM 'ENERGY/NUCLEON'. FOR CHANNELS THAT BEGIN THEIR NAMES WITH THE DESIGNATIONS 'CH' THESE BANDPASSES CAN BE USED ON MASS SPECIES THAT ARE ACCEPTED INTO THAT CHANNEL (SEE ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPCHANZ', WHICH GIVE THE MINIMUM AND MAXIMUM 'Z' VALUE ACCEPTED -- THESE ENTRIES ARE BLANK FOR ELECTRON CHANNELS). FOR OTHER CHANNELS THE GIVEN BANDPASS REFERS ONLY TO THE LOWEST 'Z' VALUE ACCEPTED. THE BANDPASSES FOR OTHER 'Z' VALUES ARE NOT ALL KNOWN, BUT SOME ARE GIVEN IN THE LITERATURE (E.G. KRIMIGIS ET AL., 1979). THE FINAL PRODUCT OF THESE INSTRUCTIONS WILL BE THE PARTICLE INTENSITY WITH THE UNITS: COUNTS/(CM**2.STR.SEC.KEV). SOME CHANNELS ARE SUBJECT TO SERIOUS CONTAMINATIONS, AND MANY OF THESE CONTAMINATIONS CANNOT BE REMOVED EXCEPT WITH A REGION-BY-REGION ANALYSIS, WHICH HAS NOT BEEN DONE FOR THIS DATA. THUS, TO USE THIS DATA IT IS ABSOLUTELY VITAL THAT THE CONTAMINATION TYPES ('contamination_id' , 'contamination_desc') AND THE LEVELS OF CONTAMINATION ('data_quality_id' CORRESPONDING TO THE DEFINITIONS 'data_quality_desc') BE CAREFULLY EXAMINED FOR ALL REGIONS OF STUDY. A DEAD TIME CORRECTION PROCEDURE HAS BEEN APPLIED IN AN ATTEMPT TO CORRECT THE LINEAR EFFECTS OF DETECTOR OVERDRIVE (PULSE-PILEUP). THIS PROCEDURE DOES NOT FIX SEVERELY OVERDRIVEN DETECTORS. A PROCEDURE IS AVAILABLE FOR CORRECTING VOYAGER 2 LECP ELECTRON CONTAMINATION OF LOW ENERGY ION CHANNELS, BUT ITS EFFECTIVENESS HAS BEEN EVALUATED ONLY FOR THE URANUS DATA SET. THUS, CORRECTIONS HAVE BEEN APPLIED ONLY TO THE URANUS DATA SET. Also included with this data are one standard deviation statistical uncertainties for the directional data (sectors 1 through 8) expressed as a percent. Unknown values are generally coded as su",
-            "title": "VOYAGER 1 SAT LOW ENERGY CHARGED PARTICLE CALIB. 15MIN",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 1 SAT LOW ENERGY CHARGED PARTICLE CALIB. 15MIN"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-7g4iapn",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI). 2021-07-05. S5P_L2__AER_LH_HiR. Version 2. Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 5.5km x 3.5km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-7g4iapn. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_HiR_2.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2021-07-01T19:06:28Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "air quality",
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry",
-                "aerosols"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pepijn Veefkind",
                 "hasEmail": "mailto:pepijn.veefkind@knmi.nl"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2087216100-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__AER_LH_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P TROPOMI aerosol layer height algorithm applies a forward model, which includes DISAMAR (Determining Instrument Specifications and Analyzing Methods for Atmospheric Retrieval, a Layer-Based Orders of Scattering algorithm) to calculate monochromatic reflectance, and also employs a neural network scheme for speedy processor performance. Data retrieval uses the Optimal Estimation Method (OEM) for spectral fitting with various aerosol layer pressures and aerosol optical thicknesses in the Oxygen-A band (758 -770nm). The aerosol baseline model assumes a single uniformly distributed aerosol layer with a fixed pressure thickness and a constant aerosol volume extinction coefficient and single scattering albedo. The aerosol parameterization is particularly suitable for elevated non-scattering aerosols such as volcanic ash, desert dust and biomass burning plume. The product main outputs include the mid-pressure and mid-altitude of aerosol layers, aerosol optical thickness at 760nm, error estimates, and other relevant diagnostics.\n\nStarting from orbit #12432 on March 7th of 2020, the S-NPP auxiliary cloud data source used in the aerosol layer height product data processing has been transitioned from the VIIRS Cloud Mask (VCM) into the Enterprise Cloud Mask (ECM).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__AER_LH_HiR",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)",
-            "title": "Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__AER_LH_HiR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__AER_LH_HiR_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data before August 6th of 2019, please check S5P_L2__AER_LH_1 data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nCopernicus Sentinel-5P TROPOMI aerosol layer height algorithm applies a forward model, which includes DISAMAR (Determining Instrument Specifications and Analyzing Methods for Atmospheric Retrieval, a Layer-Based Orders of Scattering algorithm) to calculate monochromatic reflectance, and also employs a neural network scheme for speedy processor performance. Data retrieval uses the Optimal Estimation Method (OEM) for spectral fitting with various aerosol layer pressures and aerosol optical thicknesses in the Oxygen-A band (758 -770nm). The aerosol baseline model assumes a single uniformly distributed aerosol layer with a fixed pressure thickness and a constant aerosol volume extinction coefficient and single scattering albedo. The aerosol parameterization is particularly suitable for elevated non-scattering aerosols such as volcanic ash, desert dust and biomass burning plume. The product main outputs include the mid-pressure and mid-altitude of aerosol layers, aerosol optical thickness at 760nm, error estimates, and other relevant diagnostics.\n\nStarting from orbit #12432 on March 7th of 2020, the S-NPP auxiliary cloud data source used in the aerosol layer height product data processing has been transitioned from the VIIRS Cloud Mask (VCM) into the Enterprise Cloud Mask (ECM).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-7g4iapn",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-7g4iapn",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1437812,407 +1437788,409 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_HiR_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__AER_LH_HiR_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.2/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.2",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__AER_LH_HiR.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Aerosol-Layer-Height-Product-Readme-File.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Aerosol-Layer-Height-Product-Readme-File.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__AER_LH_HiR_2",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__AER_LH_HiR_2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-Aerosol-Height",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-Aerosol-Height",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Aerosol-Layer-Height",
-                    "description": "Product User Manual Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Aerosol-Layer-Height",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__AER_LH_HiR_1.png",
+            "identifier": "C2087216100-GES_DISC",
+            "issued": "2017-05-05",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5270/S5P-7g4iapn",
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
+            "series-name": "S5P_L2__AER_LH_HiR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-07-01T19:06:28Z/2023-03-01T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Aerosol Layer Height 1-Orbit L2 5.5km x 3.5km V2 (S5P_L2__AER_LH_HiR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWOT-PIXCVEC-2.0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Surface Water Ocean Topography (SWOT). 2024-02-01. SWOT Level 2 Water Mask Pixel Cloud Auxiliary Data Product. Version 2.0. SWOT Level 2 Water Mask Pixel Cloud Auxiliary Data Product, Version 2.0. Jet Propulsion Laboratory. Archived by National Aeronautics and Space Administration, U.S. Government, JPL NASA. https://doi.org/10.5067/SWOT-PIXCVEC-2.0. https://swot.jpl.nasa.gov/.",
-            "issued": "2022-08-31",
-            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-31",
-            "keyword": [
-                "surface water",
-                "terrestrial hydrosphere",
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
-            "identifier": "C2799438260-POCLOUD",
-            "description": "Auxiliary information for pixel cloud product indicating to which water bodies the pixels are assigned in river and lake products. Also includes height-constrained pixel geolocation after reach- or lake-scale averaging. Point cloud over tile (approx 64x64 km2); half swath (left or right side of full swath). Available in netCDF-4 file format.",
-            "release-place": "Jet Propulsion Laboratory",
-            "series-name": "SWOT Level 2 Water Mask Pixel Cloud Auxiliary Data Product",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Surface Water Ocean Topography (SWOT)",
-            "title": "SWOT Level 2 Water Mask Pixel Cloud Auxiliary Data Product, Version 2.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_PIXCVec_2.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Auxiliary information for pixel cloud product indicating to which water bodies the pixels are assigned in river and lake products. Also includes height-constrained pixel geolocation after reach- or lake-scale averaging. Point cloud over tile (approx 64x64 km2); half swath (left or right side of full swath). Available in netCDF-4 file format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-PIXCVEC-2.0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWOT-PIXCVEC-2.0",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438260-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2799438260-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438260-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438260-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_PIXCVec_2.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_PIXCVec_2.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SWOT-TN-CDM-0677-CNES_Product_Description_L2_HR_PIXCVec_20231208_RevB_signed.pdf",
-                    "description": "Product Description Document (PDD)",
                     "@type": "dcat:Distribution",
+                    "description": "Product Description Document (PDD)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/pdd/SWOT-TN-CDM-0677-CNES_Product_Description_L2_HR_PIXCVec_20231208_RevB_signed.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438260-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
-                    "description": "Search Granules from Forward Processing (PIC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Forward Processing (PIC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438260-POCLOUD&pg%5B0%5D%5Bid%5D=*PIC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438260-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
-                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
                     "@type": "dcat:Distribution",
+                    "description": "Search Granules from Bulk Reprocessing (PGC0)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2799438260-POCLOUD&pg%5B0%5D%5Bid%5D=*PGC0*",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/releases/SWOT_VersionC_KaRIn_Products_Release_Note.pdf",
-                    "description": "Release Note",
                     "@type": "dcat:Distribution",
+                    "description": "Release Note",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/swot_mission_docs/releases/SWOT_VersionC_KaRIn_Products_Release_Note.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_L2_HR_PIXCVec_2.0.jpg",
+            "identifier": "C2799438260-POCLOUD",
+            "issued": "2022-08-31",
+            "keyword": [
+                "surface water",
+                "terrestrial hydrosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWOT-PIXCVEC-2.0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Jet Propulsion Laboratory",
+            "series-name": "SWOT Level 2 Water Mask Pixel Cloud Auxiliary Data Product",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2022-12-16T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT Level 2 Water Mask Pixel Cloud Auxiliary Data Product, Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/4N9BFV091ZXH",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX02 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/4N9BFV091ZXH.",
-            "issued": "2002-06-25",
-            "temporal": "2002-06-25T00:00:00Z/2002-07-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-07-12",
-            "keyword": [
-                "land surface",
-                "agriculture",
-                "microwave",
-                "soils",
-                "spectral/engineering",
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
-            "identifier": "C1386204145-NSIDCV0",
             "description": "This data set includes brightness temperature (Tb) and soil moisture data.",
-            "title": "SMEX02 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4N9BFV091ZXH",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4N9BFV091ZXH",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PSR",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PSR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PSR",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PSR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PSR",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PSR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PSR",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/aircraft_remote_sensing/PSR",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4N9BFV091ZXH",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/4N9BFV091ZXH",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4N9BFV091ZXH",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/4N9BFV091ZXH",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386204145-NSIDCV0",
+            "issued": "2002-06-25",
+            "keyword": [
+                "land surface",
+                "agriculture",
+                "microwave",
+                "soils",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/4N9BFV091ZXH",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-93.841 41.694 -93.161 42.732",
+            "temporal": "2002-06-25T00:00:00Z/2002-07-12T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX02 Aircraft Polarimetric Scanning Radiometer (PSR) Data, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2746-V1.0",
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
-                "mars express"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-01-29T16:23:43 to 2011-01-29T18:14:57.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2746-v1.0_twjg-e45v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-X-MRS-1%2F2%2F3-EXT3-2746-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-x-mrs-1-2-3-ext3-2746-v1.0_twjg-e45v",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Solar Conjunction measurement and covers the time 2011-01-29T16:23:43 to 2011-01-29T18:14:57.500.",
-            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2746 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS SUN MRS 1/2/3\n                                     EXTENDED MISSION 3 2746 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3544",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lambert, A., Livesey, N., Read, W., and Fuller, R.. 2021-04-29. ML3MBIWC. Version 005. MLS/Aura Level 3 Monthly Binned Cloud Ice (IWC) on Assorted Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3544. https://disc.gsfc.nasa.gov/datacollection/ML3MBIWC_005.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
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
-            "identifier": "C2042568626-GES_DISC",
-            "description": "ML3MBIWC is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for cloud ice water content (IWC) derived from radiances measured by the 240 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 215 to 82.5 hPa, and the vertical resolution is about 3 km. Users of the ML3MBIWC data product should read chapter 4 and sections 3.15 and 3.16 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs \"potential temperature\", lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3MBIWC",
             "creator": "Lambert, A., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Monthly Binned Cloud Ice (IWC) on Assorted Grids V005 (ML3MBIWC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBIWC_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3MBIWC is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for cloud ice water content (IWC) derived from radiances measured by the 240 GHz radiometer. The data version is 5.1. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 215 to 82.5 hPa, and the vertical resolution is about 3 km. Users of the ML3MBIWC data product should read chapter 4 and sections 3.15 and 3.16 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs \"potential temperature\", lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3544",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3544",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1438222,448 +1438200,452 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBIWC_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBIWC_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBIWC.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBIWC.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBIWC.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBIWC.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBIWC_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBIWC_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBIWC_005.png",
+            "identifier": "C2042568626-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3544",
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
+            "series-name": "ML3MBIWC",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Monthly Binned Cloud Ice (IWC) on Assorted Grids V005 (ML3MBIWC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/XUON18G3NDXX",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRU6H3D. Version 1. TROPESS Chemical Reanalysis Zonal Wind 6-Hourly 3-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/XUON18G3NDXX. https://disc.gsfc.nasa.gov/datacollection/TRPSCRU6H3D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric winds",
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
-            "identifier": "C2837624952-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Zonal Wind 6-Hourly 3-dimensional Product contains vertical zonal wind component (u vector) values, a meteorological field. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at 6-hourly resolution, and a spatial resolution of 1.125 x 1.125 degrees at 27 pressure levels between 1000 and 60 hPa. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRU6H3D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Zonal Wind 6-Hourly 3-dimensional Product V1 (TRPSCRU6H3D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRU6H3D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXUON18G3NDXX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXUON18G3NDXX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRU6H3D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRU6H3D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRU6H3D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRU6H3D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRU6H3D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_VERTCONCS/TRPSCRU6H3D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRU6H3D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRU6H3D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_6HR_METFIELDS/TRPSCRU6H3D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_6HR_METFIELDS/TRPSCRU6H3D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_METFIELDS/TRPSCRU6H3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_6HR_METFIELDS/TRPSCRU6H3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRU6H3D_Sample.png",
+            "identifier": "C2837624952-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/XUON18G3NDXX",
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
+            "series-name": "TRPSCRU6H3D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Zonal Wind 6-Hourly 3-dimensional Product V1 (TRPSCRU6H3D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-RDR-3-52COLOR-V1.0",
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
+            "description": "The observations were made using a double CVF (circularly variable filter). The short wavelength portion of the CVF covered the octave from 0.8 to 1.6 microns with 3 percent resolution, while the long wavelength portion covered 1.5 to 2.6 microns with 5 percent resolution. There is some overlap in the spectral coverage between 1.5 and 1.6 microns, which is evident as a discontinuity in the wavelengths after the first 32 values, which were obtained with the short wavelength portion, while the remaining 20 values were obtained with the long wavelength portion.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-rdr-3-52color-v1.0_twm4-7r67",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-RDR-3-52COLOR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-rdr-3-52color-v1.0_twm4-7r67",
-            "description": "The observations were made using a double CVF (circularly variable filter). The short wavelength portion of the CVF covered the octave from 0.8 to 1.6 microns with 3 percent resolution, while the long wavelength portion covered 1.5 to 2.6 microns with 5 percent resolution. There is some overlap in the spectral coverage between 1.5 and 1.6 microns, which is evident as a discontinuity in the wavelengths after the first 32 values, which were obtained with the short wavelength portion, while the remaining 20 values were obtained with the long wavelength portion.",
-            "title": "52 COLOR ASTEROID SURVEY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "52 COLOR ASTEROID SURVEY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-2-PRL-RAW-V9.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nPRELANDING Phase (PRL) from March 23,2014 until November 21, 2014\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.\nThis applies mainly to CALIBRATED and RESAMPLED datasets. The RAW dataset,\nhowever, has been updated as well in order provide all datasets at the\nsame stage, although RAW data proper did not change.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-2-prl-raw-v9.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "checkout",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-2-PRL-RAW-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-2-prl-raw-v9.0",
-            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nPRELANDING Phase (PRL) from March 23,2014 until November 21, 2014\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.\nThis applies mainly to CALIBRATED and RESAMPLED datasets. The RAW dataset,\nhowever, has been updated as well in order provide all datasets at the\nsame stage, although RAW data proper did not change.",
-            "title": "ROSETTA-ORBITER SW RPCMAG 2 PRL RAW V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SW RPCMAG 2 PRL RAW V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M18-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m18-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67P-M18-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67p-m18-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-06-30T23:25:00.000 to 2015-07-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP018 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1555",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Walker, D.A. 2018. Arctic Vegetation Plots, Prudhoe Bay ArcSEES Road Study, Lake Colleen, Alaska, 2014. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1555",
-            "issued": "2018-12-31",
-            "temporal": "2014-08-06T00:00:00Z/2014-08-13T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "solid earth",
-                "land surface",
-                "soils",
-                "biosphere",
-                "geomorphic landforms/processes",
-                "terrestrial hydrosphere",
-                "snow/ice",
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
-            "identifier": "C2162122325-ORNL_CLOUD",
             "description": "This dataset provides environmental, soil, and vegetation data collected from study plots in the vicinity of Lake Colleen off the Spine Road at Prudhoe Bay, Alaska, during August of 2014. Data include vegetation species, leaf area index (LAI), percent cover classes, soil moisture and color, and plot characteristics including geology, topographic position, slope, aspect, and plot disturbance.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Arctic Vegetation Plots, Prudhoe Bay ArcSEES Road Study, Lake Colleen, Alaska, 2014",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Prudhoe_Bay_ArcSEES_Veg_Plots_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1555",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1555",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Prudhoe_Bay_ArcSEES_Veg_Plots/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Prudhoe_Bay_ArcSEES_Veg_Plots/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Prudhoe_Bay_ArcSEES_Veg_Plots.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Prudhoe_Bay_ArcSEES_Veg_Plots.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1555",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1555",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Prudhoe_Bay_ArcSEES_Veg_Plots/comp/aava_pruarc_dwalker_2015_envlegend_anc.pdf",
-                    "description": "Pre-ABoVE: Arctic Vegetation Plots near Spine Road, Prudhoe Bay, Alaska, 2014: aava_pruarc_dwalker_2015_envlegend_anc.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Pre-ABoVE: Arctic Vegetation Plots near Spine Road, Prudhoe Bay, Alaska, 2014: aava_pruarc_dwalker_2015_envlegend_anc.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Prudhoe_Bay_ArcSEES_Veg_Plots/comp/aava_pruarc_dwalker_2015_envlegend_anc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Prudhoe_Bay_ArcSEES_Veg_Plots/comp/pruarc_dwalker_2015_plotphotos_anc.pdf",
-                    "description": "Pre-ABoVE: Arctic Vegetation Plots near Spine Road, Prudhoe Bay, Alaska, 2014: pruarc_dwalker_2015_plotphotos_anc.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Pre-ABoVE: Arctic Vegetation Plots near Spine Road, Prudhoe Bay, Alaska, 2014: pruarc_dwalker_2015_plotphotos_anc.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Prudhoe_Bay_ArcSEES_Veg_Plots/comp/pruarc_dwalker_2015_plotphotos_anc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Prudhoe_Bay_ArcSEES_Veg_Plots/comp/Prudhoe_Bay_ArcSEES_Veg_Plots.pdf",
-                    "description": "Pre-ABoVE: Arctic Vegetation Plots near Spine Road, Prudhoe Bay, Alaska, 2014: Prudhoe_Bay_ArcSEES_Veg_Plots.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Pre-ABoVE: Arctic Vegetation Plots near Spine Road, Prudhoe Bay, Alaska, 2014: Prudhoe_Bay_ArcSEES_Veg_Plots.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Prudhoe_Bay_ArcSEES_Veg_Plots/comp/Prudhoe_Bay_ArcSEES_Veg_Plots.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Prudhoe_Bay_ArcSEES_Veg_Plots/comp/walkerd_2015_datarpt_agc15-01_prudhoebaythermokarst.pdf",
-                    "description": "Pre-ABoVE: Arctic Vegetation Plots near Spine Road, Prudhoe Bay, Alaska, 2014: walkerd_2015_datarpt_agc15-01_prudhoebaythermokarst.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Pre-ABoVE: Arctic Vegetation Plots near Spine Road, Prudhoe Bay, Alaska, 2014: walkerd_2015_datarpt_agc15-01_prudhoebaythermokarst.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Prudhoe_Bay_ArcSEES_Veg_Plots/comp/walkerd_2015_datarpt_agc15-01_prudhoebaythermokarst.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Prudhoe_Bay_ArcSEES_Veg_Plots_Fig1.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Prudhoe_Bay_ArcSEES_Veg_Plots_Fig1.png",
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
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Prudhoe_Bay_ArcSEES_Veg_Plots_Fig1.png",
+            "identifier": "C2162122325-ORNL_CLOUD",
+            "issued": "2018-12-31",
+            "keyword": [
+                "solid earth",
+                "land surface",
+                "soils",
+                "biosphere",
+                "geomorphic landforms/processes",
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1555",
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
             "spatial": "70.22 -148.47",
+            "temporal": "2014-08-06T00:00:00Z/2014-08-13T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Vegetation Plots, Prudhoe Bay ArcSEES Road Study, Lake Colleen, Alaska, 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/twpr-7djk",
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
-                "nen",
-                "geography",
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
-            "identifier": "NASA-0000038__33",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1438671,334 +1438653,318 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__33",
+            "issued": "2018-06-25",
+            "keyword": [
+                "space science",
+                "nen",
+                "geography",
+                "wise"
+            ],
+            "landingPage": "https://data.nasa.gov/d/twpr-7djk",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC3-MTP021-V1.0",
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
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc3-mtp021-v1.0_twue-6b32",
             "description": "This data set contains count rates (1/s) as measured by the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, along with their standard deviations.  The primary target is comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 2 Experiment Data Record data, and provide a measure of the radiation in the spacecraft environment during the Medium Term Plan 21 period of the ESCORT 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 3\n    MTP021 V1.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-2-esc3-mtp021-v1.0_twue-6b32",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-2-ESC3-MTP021-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
             "programCode": [
                 "026:005"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
-            "theme": [
-                "Earth Science"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
             },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT3-MTP033-V1.0",
-            "bureauCode": [
-                "026:00"
-            ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "references": [
                 "https://pds.nasa.gov"
             ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
+            "theme": [
+                "Earth Science"
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 2 ESCORT 3\n    MTP021 V1.0"
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 33 period of the EXTENSION 3 mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext3-mtp033-v1.0_twxy-apti",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-EXT3-MTP033-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-ext3-mtp033-v1.0_twxy-apti",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 33 period of the EXTENSION 3 mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 3\n    MTP033 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 EXTENSION 3\n    MTP033 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PRA-3-RDR-LOWBAND-6SEC-V1.0",
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
+            "description": "This data set (VG2-S-PRA-3-RDR-LOWBAND-6SEC-V1.0) contains data acquired by the Voyager-2 Planetary Radio Astronomy (PRA) instrument during the Saturn encounter.  Since the PRA instrument is able to observe planetary phenomenon at much larger ranges than other fields and particles experiments, thus the PRA data cover a variable and longer encounter period. PRA lowband data provided here cover the entire Saturn Encounter Phase (1981-06-05 to 1981-09-28).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pra-3-rdr-lowband-6sec-v1.0_twy8-8ry9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-PRA-3-RDR-LOWBAND-6SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-pra-3-rdr-lowband-6sec-v1.0_twy8-8ry9",
-            "description": "This data set (VG2-S-PRA-3-RDR-LOWBAND-6SEC-V1.0) contains data acquired by the Voyager-2 Planetary Radio Astronomy (PRA) instrument during the Saturn encounter.  Since the PRA instrument is able to observe planetary phenomenon at much larger ranges than other fields and particles experiments, thus the PRA data cover a variable and longer encounter period. PRA lowband data provided here cover the entire Saturn Encounter Phase (1981-06-05 to 1981-09-28).",
-            "title": "VG2 SAT PRA CALIBRATED HI-RES LOW FREQ.\n                                        REC. BAND DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 SAT PRA CALIBRATED HI-RES LOW FREQ.\n                                        REC. BAND DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-3%2F4-9P-ENCOUNTER-V3.0",
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
+            "description": "This dataset contains calibrated images of comet 9P/Tempel 1 acquired by the Medium Resolution Instrument Visible CCD (MRI) from 01 May through 06 July 2005 during the encounter phase of the Deep Impact mission. Version 3.0 was calibrated by the EPOXI mission pipeline and includes corrected observation times with a maximum difference of about 40 milliseconds, a change to decompress the camera's zero-DN lookup table entry to the top of its range and flag the affected pixels as saturated, the replacement of the I-over-F data products by multiplicative constants for converting radiance products to I-over-F, and the application of a horizontal destriping process and improved absolute radiometric calibration constants.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-3-4-9p-encounter-v3.0_twzn-tq9g",
+            "issued": "2021-05-21",
+            "keyword": [
+                "9p/tempel 1 (1867 g1)",
+                "deep impact"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-3%2F4-9P-ENCOUNTER-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-3-4-9p-encounter-v3.0_twzn-tq9g",
-            "description": "This dataset contains calibrated images of comet 9P/Tempel 1 acquired by the Medium Resolution Instrument Visible CCD (MRI) from 01 May through 06 July 2005 during the encounter phase of the Deep Impact mission. Version 3.0 was calibrated by the EPOXI mission pipeline and includes corrected observation times with a maximum difference of about 40 milliseconds, a change to decompress the camera's zero-DN lookup table entry to the top of its range and flag the affected pixels as saturated, the replacement of the I-over-F data products by multiplicative constants for converting radiance products to I-over-F, and the application of a horizontal destriping process and improved absolute radiometric calibration constants.",
-            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED MRI IMAGES V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DEEP IMPACT 9P/TEMPEL ENCOUNTER - REDUCED MRI IMAGES V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0194-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-10T10:01:00.000 to 2014-08-10T13:50:58.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0194-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0194-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0194-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-10T10:01:00.000 to 2014-08-10T13:50:58.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0194 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0194 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M01-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m01-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M01-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m01-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-01-20T10:00:00.000 to 2014-05-07T12:47:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP001 RDR-INF-REFL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP001 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "GSSTFM_3",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA307",
             "citation": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, J. Ardizzone, and S. Gao. Andrey Savtchenko. 2012-08-14. GSSTFM. Version 3. Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Monthly Grid V3. Greenbelt, MD, USA. GSSTFM_3. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/GSSTF/DATA307. https://disc.gsfc.nasa.gov/datacollection/GSSTFM_3.html. Digital Science Data.",
-            "issued": "2012-08-14",
-            "temporal": "1987-07-01T00:00:00Z/2008-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-08-14",
-            "keyword": [
-                "ocean heat budget",
-                "ocean pressure",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "oceans",
-                "ocean winds",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "ocean temperature",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SILBERSTEIN",
                 "hasEmail": "mailto:david.s.silberstein@nasa.gov"
             },
+            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, J. Ardizzone, and S. Gao",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1237113442-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "These data are the Goddard Satellite-based Surface Turbulent Fluxes Version-3 Dataset recently produced through a MEaSUREs funded project led by Dr. Chung-Lin Shie (UMBC/GEST, NASA/GSFC), converted to HDF-EOS5 format. The stewardship of this HDF-EOS5 dataset is part of the MEaSUREs project. \n\nThis is the fine resolution version of the previously released GSSTFM.2c. \n\nThis is the Monthly product; data are projected to equidistant Grid that covers the globe at 0.25x00.25 degree cell size, resulting in data arrays of 1440x720 size. The monthly product is a result of averaging of a month worth of daily GSSTF3 files. Starting with Version 3, the \"WB\" variable, \"lowest 500-m precipitable water\" has been discontinued.  \n\nThe monthly temporal and one-degree spatial resolution of the product can be used to examining climate variability at these scales. Oceanic evaporation contributes to the net fresh water input to the oceans and drives the upper ocean density structure and consequently the circulation of the oceans.\n\n     The short name for this product is GSSTFM.",
-            "editor": "Andrey Savtchenko",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GSSTFM",
-            "creator": "Shie, C.-L., K. Hilburn, L. S. Chiu, R. Adler, I-I Lin, E. Nelkin, J. Ardizzone, and S. Gao",
-            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Monthly Averaged Precipitable Water 1 x 1 degree 01/1991 [g/cm2]",
-            "title": "Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Monthly Grid V3 (GSSTFM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFM_3.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA307",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FGSSTF%2FDATA307",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFM_3.png",
-                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Monthly Averaged Precipitable Water 1 x 1 degree 01/1991 [g/cm2]\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Monthly Averaged Precipitable Water 1 x 1 degree 01/1991 [g/cm2]\n      ",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFM_3.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTFM_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GSSTFM_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFM.3/",
-                    "description": "Access the data via HTTP.\n   ",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.\n   ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFM.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTFM_3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.\n      ",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.\n      ",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GSSTFM_3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTFM.3",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/GSSTF/GSSTFM.3",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFM.3/doc/Readme.GSSTF3.pdf",
-                    "description": "README Document\n   ",
                     "@type": "dcat:Distribution",
+                    "description": "README Document\n   ",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/GSSTF/GSSTFM.3/doc/Readme.GSSTF3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects",
-                    "description": "MEaSUREs Project Home Page\n   ",
                     "@type": "dcat:Distribution",
+                    "description": "MEaSUREs Project Home Page\n   ",
+                    "downloadURL": "https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
@@ -1439008,131 +1438974,167 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "editor": "Andrey Savtchenko",
+            "graphic-preview-description": "Goddard Satellite-based Surface Turbulent Fluxes (GSSTF)  Monthly Averaged Precipitable Water 1 x 1 degree 01/1991 [g/cm2]",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GSSTFM_3.png",
+            "identifier": "C1237113442-GES_DISC",
+            "issue-identification": "GSSTFM_3",
+            "issued": "2012-08-14",
+            "keyword": [
+                "ocean heat budget",
+                "ocean pressure",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "oceans",
+                "ocean winds",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "ocean temperature",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/GSSTF/DATA307",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-08-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "GSSTFM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1987-07-01T00:00:00Z/2008-12-31T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Goddard Satellite-Based Surface Turbulent Fluxes, 0.25 x 0.25 deg, Monthly Grid V3 (GSSTFM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1744",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Walker, X.J., J.L. Baltzer, L.L. Bourgeau-Chavez, N.J. Day, W.J. De groot, C. Dieleman, E.E. Hoy, J.F. Johnstone, E.S. Kane, M.A. Parisien, S. Potter, B.M. Rogers, M.R. Turetsky, S. Veraverbeke, E. Whitman, and M.C. Mack. 2020. ABoVE: Synthesis of Burned and Unburned Forest Site Data, AK and Canada, 1983-2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1744",
-            "issued": "2022-05-06",
-            "temporal": "1983-01-01T00:00:00Z/2016-08-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "vegetation",
-                "topography",
-                "soils",
-                "precipitation",
-                "natural hazards",
-                "land surface",
-                "human dimensions",
-                "environmental impacts",
-                "ecosystems",
-                "ecological dynamics",
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
-            "identifier": "C2143402559-ORNL_CLOUD",
             "description": "This dataset is a synthesis of field plot characterization data, derived above-ground and below-ground combusted carbon, and acquired Fire Weather Index (FWI) System components for burned boreal forest sites across Alaska, USA, the Northwest Territories, and Saskatchewan, Canada from 1983-2016. Unburned plot data are also included. Compiled plot-level characterization data include stand age, disturbance history, tree density, and tree biophysical measurements for calculation of the above-ground (ag) and below-ground (bg) biomass/carbon pools, pre-fire and residual post-fire soil organic layer (SOL) depths and estimates of combustion of tree structural classes. The measured slope and aspect for each site and an assigned moisture class based on topography are also provided. Data from 1019 burned and 152 unburned sites are included. From the estimates of combusted ag and bg carbon pools and SOL losses, the total carbon combusted, the proportion of pre-fire carbon combusted, and the proportion of total carbon combusted were calculated for each plot. FWI System components including moisture and drought codes and indices of fire danger were obtained for each plot from existing data sources based on the plot location, year of burn, and a dynamic start-up date (day of burn, DOB) from the global fire weather database. Data for soil characteristics are included in a separate file.",
-            "graphic-preview-description": "Field sites, ecoregions, and total area burned (millions of hectares; Mha) in each of the ecoregions in the study domain over time. Grey dotted line in the inset represents the simple linear regression, with red shading for the 95% confidence intervals, of burned area for all ecoregions combined. Analyses were completed using the field site groupings, located within the six ecoregions defined by the EPA Level II Ecoregions of North America. Source: Walker et al., 2020.",
-            "title": "ABoVE: Synthesis of Burned and Unburned Forest Site Data, AK and Canada, 1983-2016",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Plot_Data_Burned_Sites_fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1744",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1744",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_Plot_Data_Burned_Sites/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/ABoVE_Plot_Data_Burned_Sites/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Plot_Data_Burned_Sites.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Plot_Data_Burned_Sites.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1744",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1744",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_Plot_Data_Burned_Sites/comp/ABoVE_Plot_Data_Burned_Sites.pdf",
-                    "description": "ABoVE: Synthesis of Burned and Unburned Forest Site Data, AK and Canada, 1983-2016: ABoVE_Plot_Data_Burned_Sites.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Synthesis of Burned and Unburned Forest Site Data, AK and Canada, 1983-2016: ABoVE_Plot_Data_Burned_Sites.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/ABoVE_Plot_Data_Burned_Sites/comp/ABoVE_Plot_Data_Burned_Sites.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Plot_Data_Burned_Sites_fig1.png",
-                    "description": "Field sites, ecoregions, and total area burned (millions of hectares; Mha) in each of the ecoregions in the study domain over time. Grey dotted line in the inset represents the simple linear regression, with red shading for the 95% confidence intervals, of burned area for all ecoregions combined. Analyses were completed using the field site groupings, located within the six ecoregions defined by the EPA Level II Ecoregions of North America. Source: Walker et al., 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "Field sites, ecoregions, and total area burned (millions of hectares; Mha) in each of the ecoregions in the study domain over time. Grey dotted line in the inset represents the simple linear regression, with red shading for the 95% confidence intervals, of burned area for all ecoregions combined. Analyses were completed using the field site groupings, located within the six ecoregions defined by the EPA Level II Ecoregions of North America. Source: Walker et al., 2020.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Plot_Data_Burned_Sites_fig1.png",
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
+            "graphic-preview-description": "Field sites, ecoregions, and total area burned (millions of hectares; Mha) in each of the ecoregions in the study domain over time. Grey dotted line in the inset represents the simple linear regression, with red shading for the 95% confidence intervals, of burned area for all ecoregions combined. Analyses were completed using the field site groupings, located within the six ecoregions defined by the EPA Level II Ecoregions of North America. Source: Walker et al., 2020.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ABoVE_Plot_Data_Burned_Sites_fig1.png",
+            "identifier": "C2143402559-ORNL_CLOUD",
+            "issued": "2022-05-06",
+            "keyword": [
+                "vegetation",
+                "topography",
+                "soils",
+                "precipitation",
+                "natural hazards",
+                "land surface",
+                "human dimensions",
+                "environmental impacts",
+                "ecosystems",
+                "ecological dynamics",
+                "earth science",
+                "biosphere",
+                "atmospheric temperature",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1744",
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
             "spatial": "-150.9 53.19 -88.61 67.23",
+            "temporal": "1983-01-01T00:00:00Z/2016-08-08T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Synthesis of Burned and Unburned Forest Site Data, AK and Canada, 1983-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast_spectra_reddy_neos_marscrossers&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains low-resolution    (R~150) near-infrared (0.7-2.5 microns) spectra of 27 asteroids, 5     Mars-crossing and 22 near-Earth asteroids, observed with the SpeX      instrument on the NASA Infrared Telescope Facility (IRTF) on Mauna     Kea, Hawai'i. This data set archives reduced, calibrated spectra of    targets of opportunity observed from 2001 to 2008.",
+            "identifier": "urn:nasa:pds:ast_spectra_reddy_neos_marscrossers_txe2-6ajx",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "(391151) 2005 yy93",
                 "(137032) 1998 uo1",
@@ -1439164,356 +1439166,363 @@
                 "(323) brucia",
                 "(391) ingeborg"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast_spectra_reddy_neos_marscrossers&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast_spectra_reddy_neos_marscrossers_txe2-6ajx",
-            "description": "This data set contains low-resolution    (R~150) near-infrared (0.7-2.5 microns) spectra of 27 asteroids, 5     Mars-crossing and 22 near-Earth asteroids, observed with the SpeX      instrument on the NASA Infrared Telescope Facility (IRTF) on Mauna     Kea, Hawai'i. This data set archives reduced, calibrated spectra of    targets of opportunity observed from 2001 to 2008.",
-            "title": "REDDY NEAR-EARTH AND MARS-CROSSING ASTEROIDS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "REDDY NEAR-EARTH AND MARS-CROSSING ASTEROIDS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0034-3-WHITELEY-PHOT-V1.0",
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
+            "description": "This data set includes ECAS photometry and taxonomic types of 77 Near Earth Objects published by R.J. Whiteley.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0034-3-whiteley-phot-v1.0_txfq-3hya",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0034-3-WHITELEY-PHOT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0034-3-whiteley-phot-v1.0_txfq-3hya",
-            "description": "This data set includes ECAS photometry and taxonomic types of 77 Near Earth Objects published by R.J. Whiteley.",
-            "title": "WHITELEY NEO PHOTOMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "WHITELEY NEO PHOTOMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2027",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle,  Airborne Sensor Facility NASA Ames Research Center, and G. Peltzer. 2022. MASTER: Airborne Science, Southwest US, August 2006. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2027",
-            "issued": "2023-07-06",
-            "temporal": "2006-08-21T21:57:42Z/2006-09-06T18:24:23Z",
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
-            "identifier": "C2731726504-ORNL_CLOUD",
             "description": "This dataset includes Level 1B (L1B) data products from the MODIS/ASTER Airborne Simulator (MASTER) instrument. The spectral data were collected during 18 flights aboard a DOE B-200 aircraft over Nevada,  California and Colorado, U.S., from 2006-08-21 to 2006-09-06. This data collection focused on mapping geological faults. This deployment was coordinated by the U.S. Department of Energy's Remote Sensing Laboratory (RSL) located at Nellis Air Force Base near Las Vegas, Nevada. Data products include L1B georeferenced multispectral imagery of calibrated radiance in 50 bands covering wavelengths of 0.460 to 12.879 micrometers at approximately 10-meter spatial resolution. The L1B file format is HDF-4. In addition, the dataset includes flight paths, spectral band information, instrument configuration, ancillary notes, and summary information for each flight, and browse images derived from each L1B data file.",
-            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 2  acquired on 21 August 2006 over Valley of Fire State Park, south of Glendale, Nevada, U.S. Source: MASTERL1B_0601001_02_20060821_2205_2207_V01.jpg",
-            "title": "MASTER: Airborne Science, Southwest US, August 2006",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2006_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2027",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2027",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_August_2006/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/master/MASTER_RSL_August_2006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2006.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2006.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2027",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2027",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_August_2006/comp/MASTER_RSL_August_2006.pdf",
-                    "description": "MASTER: Airborne Science, Southwest US, August 2006: MASTER_RSL_August_2006.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Airborne Science, Southwest US, August 2006: MASTER_RSL_August_2006.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_RSL_August_2006/comp/MASTER_RSL_August_2006.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2006_Fig1.jpg",
-                    "description": "Single-band images and a RGB composite image from flight track 2  acquired on 21 August 2006 over Valley of Fire State Park, south of Glendale, Nevada, U.S. Source: MASTERL1B_0601001_02_20060821_2205_2207_V01.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Single-band images and a RGB composite image from flight track 2  acquired on 21 August 2006 over Valley of Fire State Park, south of Glendale, Nevada, U.S. Source: MASTERL1B_0601001_02_20060821_2205_2207_V01.jpg",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2006_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Single-band images and a RGB composite image from flight track 2  acquired on 21 August 2006 over Valley of Fire State Park, south of Glendale, Nevada, U.S. Source: MASTERL1B_0601001_02_20060821_2205_2207_V01.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_RSL_August_2006_Fig1.jpg",
+            "identifier": "C2731726504-ORNL_CLOUD",
+            "issued": "2023-07-06",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2027",
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
             "spatial": "-118.74 32.82 -106.96 38.97",
+            "temporal": "2006-08-21T21:57:42Z/2006-09-06T18:24:23Z",
             "theme": [
                 "MASTER",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Airborne Science, Southwest US, August 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECG5D-STR44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Ocean and Sea-Ice Surface Stress - Daily Mean 0.5 Degree (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECG5D-STR44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Ocean and Sea-Ice Surface Stress - Daily Mean 0.5 Degree (Version 4 Release 4); 10.5067/ECG5D-STR44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "oceans",
-                "earth science",
-                "models",
-                "earth science reanalyses/assimilation models",
-                "earth science services",
-                "ocean winds"
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
-            "identifier": "C1990404808-POCLOUD",
-            "description": "This dataset contains daily-averaged ocean and sea-ice surface stress interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Ocean and Sea-Ice Surface Stress - Daily Mean 0.5 Degree (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_STRESS_05DEG_DAILY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains daily-averaged ocean and sea-ice surface stress interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5D-STR44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5D-STR44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_STRESS_05DEG_DAILY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_STRESS_05DEG_DAILY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECG5D-STR44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECG5D-STR44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404808-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404808-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404808-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404808-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_STRESS_05DEG_DAILY_V4R4.jpg",
+            "identifier": "C1990404808-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "models",
+                "earth science reanalyses/assimilation models",
+                "earth science services",
+                "ocean winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECG5D-STR44",
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
+            "title": "ECCO Ocean and Sea-Ice Surface Stress - Daily Mean 0.5 Degree (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0390-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-27T04:56:57.000 to 2014-10-27T14:34:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0390-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0390-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0390-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-27T04:56:57.000 to 2014-10-27T14:34:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0390 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0390 V1.0"
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
+            "description": "Data Dictionary and Index Files",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20100408.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-578",
+            "issued": "2018-06-25",
             "keyword": [
                 "pds",
                 "cirs",
@@ -1439528,45 +1439537,38 @@
                 "cda",
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
-            "identifier": "NASA-578",
-            "description": "Data Dictionary and Index Files",
-            "title": "PDS Cassini Data Release 21",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20100408.shtml",
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
+            "title": "PDS Cassini Data Release 21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-5-REDDYSPEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains low-resolution near-infrared (~0.7-2.5 microns) spectra of 40 near-Earth asteroids observed with the SpeX instrument on the NASA Infrared Telescope Facility (IRTF) on Mauna Kea, Hawai'i. This data set archives reduced, calibrated spectra that were obtained as part of Vishnu Reddy's Ph.D. disseration at the University of North Dakota. They have been used for detailed mineralogical/compositional analysis and thermal modeling to constrain the albedo of these objects.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-5-reddyspec-v1.0_txjt-cuen",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid 136617",
                 "asteroid 185851",
@@ -1439610,271 +1439612,247 @@
                 "2005 rc34",
                 "2006 vv2"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-5-REDDYSPEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-5-reddyspec-v1.0_txjt-cuen",
-            "description": "This data set contains low-resolution near-infrared (~0.7-2.5 microns) spectra of 40 near-Earth asteroids observed with the SpeX instrument on the NASA Infrared Telescope Facility (IRTF) on Mauna Kea, Hawai'i. This data set archives reduced, calibrated spectra that were obtained as part of Vishnu Reddy's Ph.D. disseration at the University of North Dakota. They have been used for detailed mineralogical/compositional analysis and thermal modeling to constrain the albedo of these objects.",
-            "title": "REDDY IRTF NEAR-EARTH ASTEROID SPECTRA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "REDDY IRTF NEAR-EARTH ASTEROID SPECTRA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/ERR/KD/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/ERR/KD/2022.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "atmosphere",
-                "atmospheric radiation",
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
-            "identifier": "C2264534478-OB_DAAC",
             "description": "The Ocean and Land Colour Instrument (OLCI) is the successor to ENVISAT's Medium Resolution Imaging Spectrometer (MERIS) having additional spectral channels, different camera arrangements and simplified on-board processing. The OLCI is a push-broom instrument with five camera modules sharing the field of view. The field of view of the five cameras is arranged in a fan-shaped configuration in the vertical plane, perpendicular to the platform velocity. Each camera has an individual field of view of 14.2\u00b0 and a 0.6\u00b0 overlap with its neighbors. The whole field of view is shifted across track by 12.6\u00b0 away from the sun to minimize the impact of sun glint. OLCI is equipped with on-board calibration hardware based on sun diffusers. There are three sun diffusers--two 'white' diffusers dedicated to radiometric calibration and one dedicated to spectral calibration, with spectral reflectance features. The native resolution is approximately 300m, refered to as Full Resolution (FR). A Reduced Resolution (RR) processing mode provides Level-1B data at sampling rates decreased by a factor of four in both spatial dimensions resulting to resolution of approximately 1.2 km.",
-            "title": "Sentinel-3B OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL3B%2FERR%2FKD%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSENTINEL-3B%2FOLCI%2FL3B%2FERR%2FKD%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
+            "identifier": "C2264534478-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "atmosphere",
+                "atmospheric radiation",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SENTINEL-3B/OLCI/L3B/ERR/KD/2022",
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
+            "title": "Sentinel-3B OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/GO-BGC/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/GO-BGC/DATA001.",
-            "issued": "2021-03-24",
-            "temporal": "2021-03-24T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "ocean chemistry",
-                "oceans",
-                "ocean temperature",
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
-            "identifier": "C2431253176-OB_DAAC",
             "description": "The Global Ocean Biogeochemistry (GO-BGC) Array is a project funded by the US National Science Foundation (NSF Award 1946578 ) to build a global network of chemical and biological sensors that will monitor ocean health. This grant is being used to build and deploy 500 robotic ocean-monitoring floats around the globe as part of NSF\u2019s Mid-scale Research Infrastructure-2 program. This network of floats is collecting data on the chemistry and the biology of the ocean from the surface to a depth of 2,000 meters, augmenting the existing Argo array that monitors ocean temperature and salinity. The GO-BGC Array is led by Director Ken Johnson and administered by the Monterey Bay Aquarium Research Institute. For questions specific to the HPLC/POC/PON data submitted to SeaBASS please contact Josh Plant at jplant@mbari.org.",
-            "title": "Global Ocean Biogeochemistry Array",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FGO-BGC%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FGO-BGC%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/GO-BGC/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/GO-BGC/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2431253176-OB_DAAC",
+            "issued": "2021-03-24",
+            "keyword": [
+                "earth science",
+                "ocean chemistry",
+                "oceans",
+                "ocean temperature",
+                "ocean optics",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/GO-BGC/DATA001",
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
+            "temporal": "2021-03-24T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Ocean Biogeochemistry Array"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast_taxonomy&version=1.0",
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
-                "multiple asteroids",
-                "none"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set is a collection of         asteroid taxonomic classifications from various classification         methods, collected from the literature.",
+            "identifier": "urn:nasa:pds:ast_taxonomy",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple asteroids",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aast_taxonomy&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:ast_taxonomy",
-            "description": "This data set is a collection of         asteroid taxonomic classifications from various classification         methods, collected from the literature.",
-            "title": "ASTEROID TAXONOMY",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID TAXONOMY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0517-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-01T01:33:05.000 to 2015-01-01T10:39:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0517-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0517-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0517-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-01T01:33:05.000 to 2015-01-01T10:39:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0517 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0517 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2514",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lambert, A., Livesey, N. and Read, W.. 2020-06-11. ML2IWC. Version 005. MLS/Aura Level 2 Cloud Ice Product V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2514. https://disc.gsfc.nasa.gov/datacollection/ML2IWC_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
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
-            "identifier": "C1729925584-GES_DISC",
-            "description": "ML2IWC is the EOS Aura Microwave Limb Sounder (MLS) standard product for cloud ice water content derived from radiances measured by the 240 GHz radiometer. The data version is 5.0. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 82.5 hPa, and the vertical resolution is about 3 km. Users of the ML2IWC data product should read sections 3.15 and 3.16 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2IWC",
             "creator": "Lambert, A., Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Cloud Ice Product V005 (ML2IWC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2IWC_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2IWC is the EOS Aura Microwave Limb Sounder (MLS) standard product for cloud ice water content derived from radiances measured by the 240 GHz radiometer. The data version is 5.0. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 82.5 hPa, and the vertical resolution is about 3 km. Users of the ML2IWC data product should read sections 3.15 and 3.16 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2514",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2514",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1439884,120 +1439862,120 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2IWC_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2IWC_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2IWC.005/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2IWC.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2IWC.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2IWC.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2IWC_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2IWC_005",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2IWC_005.png",
+            "identifier": "C1729925584-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2514",
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
+            "title": "MLS/Aura Level 2 Cloud Ice Product V005 (ML2IWC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2020",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Read, W. and Livesey, N.. 2015-02-19. ML2SO2. Version 004. MLS/Aura Level 2 Sulfur Dioxide (SO2) Mixing Ratio V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2020. https://disc.gsfc.nasa.gov/datacollection/ML2SO2_004.html. Digital Science Data.",
-            "issued": "2015-02-19",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-19",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
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
-            "identifier": "C1251101777-GES_DISC",
-            "description": "ML2SO2 is the EOS Aura Microwave Limb Sounder (MLS) standard product for sulfur dioxide derived from radiances measured by the 240 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 10 hPa, and the vertical resolution is about 3 km. Users of the ML2SO2 data product should read section 3.21 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2SO2",
             "creator": "Read, W. and Livesey, N.",
-            "title": "MLS/Aura Level 2 Sulfur Dioxide (SO2) Mixing Ratio V004 (ML2SO2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2SO2_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2SO2 is the EOS Aura Microwave Limb Sounder (MLS) standard product for sulfur dioxide derived from radiances measured by the 240 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is from 215 to 10 hPa, and the vertical resolution is about 3 km. Users of the ML2SO2 data product should read section 3.21 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2020",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
```

