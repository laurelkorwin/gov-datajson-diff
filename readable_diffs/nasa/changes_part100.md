# Change History for nasa.json (Part 100)

### Changes from 31606f9 to dd2190f (Part 89/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "title": "A Survey of Artificial Intelligence for Prognostics"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Linda J. Connell",
+                "hasEmail": "mailto:linda.j.connell@nasa.gov"
+            },
+            "description": "A sampling of reports from flight crews encountering, or affected by, turbojet wake turbulence.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://asrs.arc.nasa.gov/docs/rpsts/waketurb.pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "NASA-828",
+            "issued": "2018-06-25",
             "keyword": [
                 "turbojet",
                 "safety",
@@ -930043,1318 +930052,1318 @@
                 "aviation",
                 "wake"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Linda J. Connell",
-                "hasEmail": "mailto:linda.j.connell@nasa.gov"
-            },
+            "landingPage": "http://asrs.arc.nasa.gov/search/reportsets.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:021"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-828",
-            "description": "A sampling of reports from flight crews encountering, or affected by, turbojet wake turbulence.",
-            "title": "Aviation Safety Reporting System: Wake Turbulence Encounters",
-            "programCode": [
-                "026:021"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://asrs.arc.nasa.gov/docs/rpsts/waketurb.pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "http://asrs.arc.nasa.gov/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Aviation Safety Reporting System: Wake Turbulence Encounters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2095",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Green, R.O., P.G. Brodrick, J.W. Chapman, M. Eastwood, S. Geier, M. Helmlinger, S.R. Lundeen, W. Olson-Duvall, R. Pavlick, L.M. Rios, D.R. Thompson, and A.K. Thorpe. 2023. AVIRIS-NG L1B Calibrated Radiance, Facility Instrument Collection, V1. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2095",
-            "issued": "2023-09-22",
-            "temporal": "2014-06-21T00:00:00Z/2022-09-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-01",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
-                "infrared wavelengths",
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
-            "identifier": "C2662359874-ORNL_CLOUD",
             "description": "This dataset contains Level 1B (L1B) orthocorrected, scaled radiance image files as well as files of observational geometry and illumination parameters and supporting sensor band information from the Airborne Visible / Infrared Imaging Spectrometer-Next Generation (AVIRIS-NG) instrument. This is the NASA Earth Observing System Data and Information System (EOSDIS) facility instrument archive of these data. The NASA AVIRIS-NG is a pushbroom spectral mapping system with high signal-to-noise ratio (SNR), designed and toleranced for high performance spectroscopy. AVIRIS-NG measures reflected radiance at 5-nm intervals in the Visible to Shortwave Infrared (VSWIR) spectral range from 380-2510 nm. The AVIRIS-NG sensor has a 1 milliradian instantaneous field of view, providing altitude dependent ground sampling distances from 20 m to sub-meter range.  In this dataset, for each flight line, six file types are included: orthocorrected calibrated radiance image (img) files, geometric lookup table (glt) and orthocorrected observation geometry and illumination (obs_ort) files. Also included are unprojected files of input geometry (igm), parameters relating to the geometry of observation and illumination (obs), and orthocorrected locations of each pixel (loc). In addition, ancillary files for the flight line are provided, including quick look images and polygon outlines of imagery footprints. The AVIRIS-NG L1B data are provided in ENVI binary format, which includes a flat binary file accompanied by a header (.hdr) file holding metadata in text format. The ancillary files include JPEG images and maps in Keyhole Markup Language (KML).  The AVIRIS-NG is flown on a variety of aircraft platforms including the Twin Otter, the King Air B-200, and NASA's high altitude ER-2.  This archive currently includes data from 2014 - 2022. Additional AVIRIS-NG facility instrument L1B data will be added as they become available.  AVIRIS-NG supports NASA Science and applications in many areas including plant composition and function, geology and soils, greenhouse gas mapping, and calibration of orbital platforms.",
-            "graphic-preview-description": "Portion of quick look image for flight ang20200907t214229 on 07 September 2020 over the Russian River in Sonoma County south of Cloverdale, California (approximately 38.7392 lat, -122.9387 lon). Source: ancillary file ang20200907t214229_geo.jpg",
-            "title": "AVIRIS-NG L1B Calibrated Radiance, Facility Instrument Collection, V1",
-            "graphic-preview-file": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-NG_L1B_radiance_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2095",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2095",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/aviris/AVIRIS-NG_L1B_radiance/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/aviris/AVIRIS-NG_L1B_radiance/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-NG_L1B_radiance.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-NG_L1B_radiance.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2095",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2095",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/aviris/AVIRIS-NG_L1B_radiance/comp/AVIRIS-NG_L1B_radiance.pdf",
-                    "description": "AVIRIS-NG L1B Calibrated Radiance, Facility Instrument Collection, V1: AVIRIS-NG_L1B_radiance.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "AVIRIS-NG L1B Calibrated Radiance, Facility Instrument Collection, V1: AVIRIS-NG_L1B_radiance.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/aviris/AVIRIS-NG_L1B_radiance/comp/AVIRIS-NG_L1B_radiance.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/aviris/AVIRIS-NG_L1B_radiance/comp/AVIRIS-NG_readme.txt",
-                    "description": "AVIRIS-NG L1B Calibrated Radiance, Facility Instrument Collection, V1: AVIRIS-NG_readme.txt",
                     "@type": "dcat:Distribution",
+                    "description": "AVIRIS-NG L1B Calibrated Radiance, Facility Instrument Collection, V1: AVIRIS-NG_readme.txt",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/aviris/AVIRIS-NG_L1B_radiance/comp/AVIRIS-NG_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-NG_L1B_radiance_Fig1.jpg",
-                    "description": "Portion of quick look image for flight ang20200907t214229 on 07 September 2020 over the Russian River in Sonoma County south of Cloverdale, California (approximately 38.7392 lat, -122.9387 lon). Source: ancillary file ang20200907t214229_geo.jpg",
                     "@type": "dcat:Distribution",
+                    "description": "Portion of quick look image for flight ang20200907t214229 on 07 September 2020 over the Russian River in Sonoma County south of Cloverdale, California (approximately 38.7392 lat, -122.9387 lon). Source: ancillary file ang20200907t214229_geo.jpg",
+                    "downloadURL": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-NG_L1B_radiance_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Portion of quick look image for flight ang20200907t214229 on 07 September 2020 over the Russian River in Sonoma County south of Cloverdale, California (approximately 38.7392 lat, -122.9387 lon). Source: ancillary file ang20200907t214229_geo.jpg",
+            "graphic-preview-file": "https://daac.ornl.gov/AVIRIS/guides/AVIRIS-NG_L1B_radiance_Fig1.jpg",
+            "identifier": "C2662359874-ORNL_CLOUD",
+            "issued": "2023-09-22",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2095",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-166.65 9.2 88.81 84.36",
+            "temporal": "2014-06-21T00:00:00Z/2022-09-17T23:59:59Z",
             "theme": [
                 "AVIRIS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AVIRIS-NG L1B Calibrated Radiance, Facility Instrument Collection, V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV%2FMRI-5-HARTLEY2-SHAPE-V1.0",
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
-                "epoxi",
-                "103p/hartley 2 (1986 e2)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Shape model of comet 103P/Hartley 2, as derived from the Deep Impact spacecraft images obtained around the time of closest approach to the comet during the EPOXI mission. Includes maps of the surface features on the nucleus.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-mri-5-hartley2-shape-v1.0_ipp6-wvub",
+            "issued": "2021-05-21",
+            "keyword": [
+                "epoxi",
+                "103p/hartley 2 (1986 e2)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-HRIV%2FMRI-5-HARTLEY2-SHAPE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-hriv-mri-5-hartley2-shape-v1.0_ipp6-wvub",
-            "description": "Shape model of comet 103P/Hartley 2, as derived from the Deep Impact spacecraft images obtained around the time of closest approach to the comet during the EPOXI mission. Includes maps of the surface features on the nucleus.",
-            "title": "PLATE SHAPE MODEL OF COMET 103P/HARTLEY 2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PLATE SHAPE MODEL OF COMET 103P/HARTLEY 2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1755",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Filippelli, S.K., M.J. Falkowski, A.T. Hudak, and P.A. Fekety. 2020. CMS: Pinyon-Juniper Forest Live Aboveground Biomass, Great Basin, USA, 2000-2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1755",
-            "issued": "2020-04-21",
-            "temporal": "2000-01-01T00:00:00Z/2016-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "vegetation",
-                "land use/land cover",
-                "land surface",
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
-            "identifier": "C2389194355-ORNL_CLOUD",
             "description": "This dataset provides annual maps of live aboveground tree biomass (Mg/ha) for pinyon-juniper forests across the Great Basin of the Western USA for the years 2000-2016 at a spatial resolution of 30 meters. Biomass estimates are limited to areas of the Great Basin defined as a pinyon-juniper ecosystem type by the 2016 Landfire Existing Vegetation Type map. The estimates of biomass were based on a linear relationship with pinyon-juniper canopy cover and crown-based allometrics developed from field data in Nevada and Idaho. Canopy cover was estimated from remote sensing by using annual composites of Landsat imagery, which were temporally segmented with the LandTrendr algorithm, along with biologically-relevant climate variables, and topographic indices in a Random Forest regression model. Models of canopy cover were trained from semi-automatic extraction of tree crowns from 2011 - 2013 high resolution imagery (1 m) from the National Agriculture Imagery Program, which were validated with photo interpretation.  Maps of the standard deviation of biomass estimates from decision trees in the Random Forest model are provided as an indicator of uncertainty. Biomass estimates were calibrated to estimates from the Forest Inventory and Analysis program (FIA) on an annual basis and corrections applied.",
-            "graphic-preview-description": "Figure 1: Annual map of live aboveground tree biomass (Mg/ha) for pinyon-juniper forests across a representative portion of the Great Basin of the Western USA for the year 2005 at a spatial resolution of 30 meters. (Source: greatbasin_biomass_2005.tif)",
-            "title": "CMS: Pinyon-Juniper Forest Live Aboveground Biomass, Great Basin, USA, 2000-2016",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Great_Basin_Biomass_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1755",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1755",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Great_Basin_Biomass/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/CMS_Great_Basin_Biomass/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Great_Basin_Biomass.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Great_Basin_Biomass.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1755",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1755",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Great_Basin_Biomass/comp/CMS_Great_Basin_Biomass.pdf",
-                    "description": "CMS: Great Basin Pinyon-Juniper Biomass, 2001-2016: CMS_Great_Basin_Biomass.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "CMS: Great Basin Pinyon-Juniper Biomass, 2001-2016: CMS_Great_Basin_Biomass.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/CMS_Great_Basin_Biomass/comp/CMS_Great_Basin_Biomass.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Great_Basin_Biomass_Fig1.png",
-                    "description": "Figure 1: Annual map of live aboveground tree biomass (Mg/ha) for pinyon-juniper forests across a representative portion of the Great Basin of the Western USA for the year 2005 at a spatial resolution of 30 meters. (Source: greatbasin_biomass_2005.tif)",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: Annual map of live aboveground tree biomass (Mg/ha) for pinyon-juniper forests across a representative portion of the Great Basin of the Western USA for the year 2005 at a spatial resolution of 30 meters. (Source: greatbasin_biomass_2005.tif)",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/CMS_Great_Basin_Biomass_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Figure 1: Annual map of live aboveground tree biomass (Mg/ha) for pinyon-juniper forests across a representative portion of the Great Basin of the Western USA for the year 2005 at a spatial resolution of 30 meters. (Source: greatbasin_biomass_2005.tif)",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/CMS_Great_Basin_Biomass_Fig1.png",
+            "identifier": "C2389194355-ORNL_CLOUD",
+            "issued": "2020-04-21",
+            "keyword": [
+                "vegetation",
+                "land use/land cover",
+                "land surface",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1755",
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
             "spatial": "-123.9 33.93 -109.31 47.12",
+            "temporal": "2000-01-01T00:00:00Z/2016-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS: Pinyon-Juniper Forest Live Aboveground Biomass, Great Basin, USA, 2000-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67PCHURYUMOV-M14-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67pchuryumov-m14-v2.0_iprs-ku9v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC2-67PCHURYUMOV-M14-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc2-67pchuryumov-m14-v2.0_iprs-ku9v",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-03-10T23:25:00.000 to 2015-04-08T11:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP014 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC2-MTP014 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP46A1.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VIIRS Land SIPS. 2024-05-10. VIIRS/NPP Daily Gridded Day Night Band 500 m Linear Lat Lon Grid Night. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/VNP46A1.002\r\n. https://doi.org/10.5067/VIIRS/VNP46A1.002.",
-            "issued": "2019-03-22",
-            "temporal": "2012-01-19T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "spectral/engineering",
-                "biosphere",
-                "earth science"
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
-            "identifier": "C2980666614-LAADS",
-            "description": "The VIIRS/NPP Daily Gridded Day Night Band 500m Linear Lat Lon Grid Night product, short-name VNP46A1 is a daily, top-of-atmosphere, at-sensor nighttime radiance product. This product is available at 15 arc-second spatial resolution from January 2012 onward. The VNP46A1/VJ146A1 product contains 26 Science Data Sets (SDS) that include sensor radiance, zenith and azimuth angles (at-sensor, solar, and lunar), cloud-mask flags, time, shortwave IR radiance, brightness temperatures, VIIRS quality flags, moon phase angle, and moon illumination fraction. It also provides Quality Flag (QF) information specific to the cloud-mask, VIIRS moderate-resolution bands M10, M11, M12, M13, M15, M16, and DNB.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VIIRS Land SIPS",
-            "title": "VIIRS/NPP Daily Gridded Day Night Band 500 m Linear Lat Lon Grid Night",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NPP Daily Gridded Day Night Band 500m Linear Lat Lon Grid Night product, short-name VNP46A1 is a daily, top-of-atmosphere, at-sensor nighttime radiance product. This product is available at 15 arc-second spatial resolution from January 2012 onward. The VNP46A1/VJ146A1 product contains 26 Science Data Sets (SDS) that include sensor radiance, zenith and azimuth angles (at-sensor, solar, and lunar), cloud-mask flags, time, shortwave IR radiance, brightness temperatures, VIIRS quality flags, moon phase angle, and moon illumination fraction. It also provides Quality Flag (QF) information specific to the cloud-mask, VIIRS moderate-resolution bands M10, M11, M12, M13, M15, M16, and DNB.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP46A1.002%0D%0A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP46A1.002%0D%0A",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP46A1.002",
-                    "description": "Data product's landing page",
                     "@type": "dcat:Distribution",
+                    "description": "Data product's landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP46A1.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VNP46A1--5200",
-                    "description": "Search and order VNP46A1 product from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order VNP46A1 product from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/VNP46A1--5200",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/VIIRS_Black_Marble_UG_v1.1_July_2020.pdf",
-                    "description": "VIIRS Black Marble Product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS Black Marble Product User Guide",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/VIIRS_Black_Marble_UG_v1.1_July_2020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/VIIRS_Black_Marble_ATBD_v1.1_July_2020.pdf",
-                    "description": "VIIRS Black Marble Nighttime Lights Product Suite Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS Black Marble Nighttime Lights Product Suite Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/VIIRS_Black_Marble_ATBD_v1.1_July_2020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5200/VNP46A1/contents.html",
-                    "description": "Data access from LAADS OPeNDAP service.",
                     "@type": "dcat:Distribution",
+                    "description": "Data access from LAADS OPeNDAP service.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5200/VNP46A1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2980666614-LAADS",
+            "issued": "2019-03-22",
+            "keyword": [
+                "spectral/engineering",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP46A1.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Daily Gridded Day Night Band 500 m Linear Lat Lon Grid Night"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ALBEDOS-V1.1",
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
+            "description": "This data set comprises a compilation of asteroid albedos for the convenience of the user. Most but not all of the albedos compiled here also appear in other PDS data sets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-albedos-v1.1_iptp-2jjm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ALBEDOS-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-albedos-v1.1_iptp-2jjm",
-            "description": "This data set comprises a compilation of asteroid albedos for the convenience of the user. Most but not all of the albedos compiled here also appear in other PDS data sets.",
-            "title": "ASTEROID ALBEDOS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID ALBEDOS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1812",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Scholten, R.C., S. Veraverbeke, R. Jandt, E.A. Miller, and B.M. Rogers. 2021. ABoVE: Ignitions, Burned Area, and Emissions of Fires in AK, YT, and NWT, 2001-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1812",
-            "issued": "2021-06-22",
-            "temporal": "2001-01-01T00:00:00Z/2018-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmosphere",
-                "land surface",
-                "biosphere",
-                "earth science",
-                "air quality",
-                "ecological dynamics",
-                "national geospatial data asset",
-                "ngda",
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
-            "identifier": "C2111719486-ORNL_CLOUD",
             "description": "This dataset provides estimates of daily burned area, carbon emissions, and uncertainty, and daily fire ignition locations for boreal fires in Alaska, U.S., and in the Yukon and Northwest Territories, Canada. The data are at 500 m resolution for the 18-year period from 2001-2018. Burned area was retrieved from combining fire perimeter data from the Alaskan and Canadian Large Fire Databases with surface reflectance and active fire data from the Moderate Resolution Imaging Spectroradiometer (MODIS) Collection 6. Per-pixel carbon consumption was estimated based on a statistical relationship between field estimates of pyrogenic consumption and several environmental variables. To derive the carbon consumption estimates, the approach from Alaskan Fire Emissions Database (AKFED) was updated and extended for the period 2001-2018. Fire weather variables, temperature, and the drought code complemented remotely sensed tree cover and burn severity as model predictors. Fire ignition location and timing were extracted from the daily burned area maps.",
-            "graphic-preview-description": "Ignition locations and burned area for Interior Alaska in 2015. Source: Scholten et al., 2021b",
-            "title": "ABoVE: Ignitions, Burned Area, and Emissions of Fires in AK, YT, and NWT, 2001-2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/BurnedArea_Emissions_AK_YT_NWT_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1812",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1812",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/BurnedArea_Emissions_AK_YT_NWT/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/BurnedArea_Emissions_AK_YT_NWT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/BurnedArea_Emissions_AK_YT_NWT.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/BurnedArea_Emissions_AK_YT_NWT.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1812",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1812",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/BurnedArea_Emissions_AK_YT_NWT/comp/BurnedArea_Emissions_AK_YT_NWT.pdf",
-                    "description": "ABoVE: Ignitions, Burned Area, and Emissions of Fires in AK, YT, and NWT, 2001-2018: BurnedArea_Emissions_AK_YT_NWT.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Ignitions, Burned Area, and Emissions of Fires in AK, YT, and NWT, 2001-2018: BurnedArea_Emissions_AK_YT_NWT.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/BurnedArea_Emissions_AK_YT_NWT/comp/BurnedArea_Emissions_AK_YT_NWT.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/BurnedArea_Emissions_AK_YT_NWT_Fig1.png",
-                    "description": "Ignition locations and burned area for Interior Alaska in 2015. Source: Scholten et al., 2021b",
                     "@type": "dcat:Distribution",
+                    "description": "Ignition locations and burned area for Interior Alaska in 2015. Source: Scholten et al., 2021b",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/BurnedArea_Emissions_AK_YT_NWT_Fig1.png",
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
+            "graphic-preview-description": "Ignition locations and burned area for Interior Alaska in 2015. Source: Scholten et al., 2021b",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/BurnedArea_Emissions_AK_YT_NWT_Fig1.png",
+            "identifier": "C2111719486-ORNL_CLOUD",
+            "issued": "2021-06-22",
+            "keyword": [
+                "atmosphere",
+                "land surface",
+                "biosphere",
+                "earth science",
+                "air quality",
+                "ecological dynamics",
+                "national geospatial data asset",
+                "ngda",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1812",
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
             "spatial": "-167.0 51.63 -99.98 79.26",
+            "temporal": "2001-01-01T00:00:00Z/2018-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Ignitions, Burned Area, and Emissions of Fires in AK, YT, and NWT, 2001-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/D82HE19R6R5H",
             "citation": "AIRS project. 2025-01-06. AIRSAQIRL1B. Version 8.0. AIRS/Aqua L1B Infrared (IR) geolocated and calibrated radiances V8.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/D82HE19R6R5H. https://disc.gsfc.nasa.gov/datacollection/AIRSAQIRL1B_8.0.html. Digital Science Data.",
-            "issued": "2011-12-31",
-            "temporal": "2002-08-30T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-06",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "aerosols",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "AIRS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C3173400482-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The AIRS Infrared (IR) level 1B data set contains AIRS calibrated and geolocated radiances in milliWatts/m^2/cm^-1/steradian for 2378 infrared channels in the 3.74 to 15.4 micron region of the spectrum. The AIRS Level 1B product consists of calibrated radiances, geolocation coordinates, quality control parameters, and calibration engineering support information.  This product converts the AIRS raw data in digital counts to radiances referenced to SI (Syst\u00e8me international) traceable standards established at NIST for each of the 2378 AIRS channels, and contains ancillary information pertaining to the instrument calibration and performance.  In general, the differences between the previous version, V5, and V8 are extremely small and not significant for most applications, however the improvements may have relevance for certain climate applications.  The differences also make the product more versatile and contains more information about the calibration that will be useful for future modifications.  More information can be found in the AIRS Version 8 Level 1B ATBD and Test Report. \n\nThe AIRS instrument is co-aligned with AMSU-A so that successive blocks of 3 x 3 AIRS footprints are contained within one AMSU-A footprint. The AIRSAQIRL1B_8 products are stored in files (often referred to as \"granules\") that contain 6 minutes of data, 90 footprints across track by 135 lines along track.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRSAQIRL1B",
-            "creator": "AIRS project",
-            "title": "AIRS/Aqua L1B Infrared (IR) geolocated and calibrated radiances V8.0 (AIRSAQIRL1B) at GES DISC at GES DISC",
-            "graphic-preview-description": "Sample image of AIRSAQIRL1B",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRIBRAD_005.jpeg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FD82HE19R6R5H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FD82HE19R6R5H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRIBRAD_005.jpeg",
-                    "description": "Sample image of AIRSAQIRL1B",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image of AIRSAQIRL1B",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRIBRAD_005.jpeg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRSAQIRL1B_8.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRSAQIRL1B_8.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level1/AIRSAQIRL1B.8.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://airsl1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level1/AIRSAQIRL1B.8.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level1/AIRSAQIRL1B.8.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://airsl1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level1/AIRSAQIRL1B.8.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRSAQIRL1B+8.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRSAQIRL1B+8.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
-                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument suite, algorithms, and other AIRS-related activities can be found.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument suite, algorithms, and other AIRS-related activities can be found.",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/README.AIRSAQIRL1B.v8.0.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/README.AIRSAQIRL1B.v8.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/AIRS_V8.0_L1B_Test_Report.pdf",
-                    "description": "Test Report, summary of validation status of products",
                     "@type": "dcat:Distribution",
+                    "description": "Test Report, summary of validation status of products",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/AIRS/AIRS_V8.0_L1B_Test_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eospso.nasa.gov/sites/default/files/atbd/AIRS_V8_L1B_ATBD.pdf",
-                    "description": "ATBD Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD Documentation",
+                    "downloadURL": "https://eospso.nasa.gov/sites/default/files/atbd/AIRS_V8_L1B_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample image of AIRSAQIRL1B",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRIBRAD_005.jpeg",
+            "identifier": "C3173400482-GES_DISC",
+            "issued": "2011-12-31",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "aerosols",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/D82HE19R6R5H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRSAQIRL1B",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L1B Infrared (IR) geolocated and calibrated radiances V8.0 (AIRSAQIRL1B) at GES DISC at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0718-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-19T05:59:42.000 to 2015-04-19T16:37:09.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0718-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0718-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0718-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-19T05:59:42.000 to 2015-04-19T16:37:09.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0718 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0718 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CPEX/MODEL/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kakar, Ramesh , Edward J Zipser and Shuyi  Chen.2022. Global Forecast System (GFS) CPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/CPEX/MODEL/DATA201",
-            "issued": "2022-11-11",
-            "temporal": "2017-05-24T00:00:00Z/2017-07-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-14",
-            "keyword": [
-                "atmospheric winds",
-                "atmospheric temperature",
-                "atmospheric water vapor",
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
-            "identifier": "C2611060678-GHRC_DAAC",
             "description": "The Global Forecast System (GFS) CPEX dataset includes model data simulated by the Global Forecast System (GFS) model for the Convective Process Experiment (CPEX) field campaign. The NASA Convective Processes Experiment (CPEX) aircraft field campaign took place in the North Atlantic-Gulf of Mexico-Caribbean Sea region from 25 May-25 June 2017. CPEX conducted a total of sixteen DC-8 missions from 27 May-24 June. The CPEX campaign collected data to help explain convective storm initiation, organization, growth, and dissipation in the North Atlantic-Gulf of Mexico-Caribbean Oceanic region during the early summer of 2017. These data are available from May 24, 2017 through July 20, 2017 and are available in netCDF-3 format.",
-            "title": "Global Forecast System (GFS) CPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPEX%2FMODEL%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPEX%2FMODEL%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=gfscpex&ghrccloud%2Fdata%2F=",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/portal/ghrc/search?q=gfscpex&ghrccloud%2Fdata%2F=",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast#:~:text=The%20Global%20Forecast%20System%20",
-                    "description": "NCEI NOAA Global Forecast System (GFS)",
                     "@type": "dcat:Distribution",
+                    "description": "NCEI NOAA Global Forecast System (GFS)",
+                    "downloadURL": "https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast#:~:text=The%20Global%20Forecast%20System%20",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://vlab.noaa.gov/web/gfs/documentation",
-                    "description": "NOAA Virtual Lab Global Forecast System - Global Spectral Model (GSM)",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA Virtual Lab Global Forecast System - Global Spectral Model (GSM)",
+                    "downloadURL": "https://vlab.noaa.gov/web/gfs/documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpex/GFS/doc/gfscpex_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/cpex/GFS/doc/gfscpex_dataset.pdf",
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
+            "identifier": "C2611060678-GHRC_DAAC",
+            "issued": "2022-11-11",
+            "keyword": [
+                "atmospheric winds",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CPEX/MODEL/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-100.0 5.0 -45.0 40.0",
+            "temporal": "2017-05-24T00:00:00Z/2017-07-20T00:00:00Z",
             "theme": [
                 "CPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Forecast System (GFS) CPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/2JBTORD9BCBN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX16 Manitoba Land Cover Classification Map V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/2JBTORD9BCBN.",
-            "issued": "2016-06-01",
-            "temporal": "2016-06-01T00:00:00Z/2016-07-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-07-31",
-            "keyword": [
-                "land surface",
-                "land use/land cover",
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
-            "identifier": "C1452895573-NSIDC_ECS",
             "description": "This data set contains land cover classification data collected for the Soil Moisture Active Passive Validation Experiment 2016 Manitoba (SMAPVEX16 Manitoba) campaign.",
-            "title": "SMAPVEX16 Manitoba Land Cover Classification Map V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2JBTORD9BCBN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F2JBTORD9BCBN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16M_LC.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV16M_LC.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1452895573-NSIDC_ECS&m=45.6064453125%21-98.0771484375%215%211%210%210%2C2&q=sv16m_lc&ok=sv16m_lc",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1452895573-NSIDC_ECS&m=45.6064453125%21-98.0771484375%215%211%210%210%2C2&q=sv16m_lc&ok=sv16m_lc",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16M_LC/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV16M_LC/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/2JBTORD9BCBN",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/2JBTORD9BCBN",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/2JBTORD9BCBN",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/2JBTORD9BCBN",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1452895573-NSIDC_ECS",
+            "issued": "2016-06-01",
+            "keyword": [
+                "land surface",
+                "land use/land cover",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/2JBTORD9BCBN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.363559 49.145916 -97.435997 49.997539",
+            "temporal": "2016-06-01T00:00:00Z/2016-07-31T23:59:59.999Z",
             "theme": [
                 "SMAPVEX16 Manitoba",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX16 Manitoba Land Cover Classification Map V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/KCHJL8HHDP40",
             "citation": "Xia, Y., et al. (2012), NCEP/EMC. David Mocko, NASA/GSFC/HSL. 2009-08-01. NLDAS_FORB0125_H. Version 002. NLDAS Secondary Forcing Data L4 Hourly 0.125 x 0.125 degree V002. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/KCHJL8HHDP40. https://disc.gsfc.nasa.gov/datacollection/NLDAS_FORB0125_H_002.html. Digital Science Data.",
-            "issued": "2009-08-01",
-            "temporal": "1979-01-01T00:00:00Z/2024-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2009-08-01",
-            "references": [
-                "https://doi.org/10.1029/2011JD016048",
-                "https://doi.org/10.1029/2011JD016051",
-                "https://doi.org/10.1029/2002JD003118",
-                "https://doi.org/10.1175/1520-0450(1984)023<0222:TIOASO>2.0.CO;2",
-                "https://doi.org/10.1029/2002JD003301"
-            ],
-            "keyword": [
-                "surface thermal properties",
-                "altitude",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "land surface",
-                "atmospheric pressure",
-                "earth science",
-                "atmospheric winds",
-                "atmosphere",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SILBERSTEIN",
                 "hasEmail": "mailto:david.s.silberstein@nasa.gov"
             },
+            "creator": "Xia, Y., et al. (2012), NCEP/EMC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1233767597-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This data set contains the secondary forcing data \"File B\" for Phase 2 of the North American Land Data Assimilation System (NLDAS-2).  The data are in 1/8th degree grid spacing and range from Jan 1979 to the present. The temporal resolution is hourly.  The file format is WMO GRIB-1. \n\nDetails about the generation of the NLDAS-2 forcing datasets can be found in Xia et al. (2012). \n\nThe non-precipitation land surface forcing fields for NLDAS-2 are derived from the analysis fields of the NCEP North American Regional Reanalysis (NARR). NARR analysis fields are 32-km spatial resolution and 3-hourly temporal frequency.  Those NARR fields that are utilized to generate NLDAS-2 forcing fields are spatially interpolated to the finer resolution of the NLDAS 1/8th-degree grid and then temporally disaggregated to the NLDAS hourly frequency.  NLDAS-2 is providing a second forcing file, \"File B\", in which the surface temperature, humidity, and wind fields are represented not at 2-meters and 10-meters above the height of the NLDAS terrain, but rather at the same height above the NLDAS terrain as the height above the NARR terrain of the lowest prognostic level of the NARR assimilation system (namely, the same height above the model terrain as the lowest prognostic level of the mesoscale Eta model, which is the assimilating model in NARR). \n\nThe surface downward surface radiation field in \"File B\" is taken directly from NARR, without any bias correction.  The precipitation and convective precipitation fields in \"File B\" are also taken directly from NARR, and are used to calculate the convective fraction provided in \"File A\".  The aerodynamic conductance is \"File B\" is also taken from NARR.\n\nThe hourly land surface forcing fields for NLDAS-2 are grouped into two GRIB files, \"File A\" and \"File B\".  \"File B\" is the secondary (optional) forcing file and contains ten fields.  The data set applies a user-defined parameter table to indicate the contents and parameter number.  The GRIBTAB file shows a list of parameters for this data set, along with their Product Definition Section (PDS) IDs and units. \n\nFor more information, please see the README Document.",
-            "editor": "David Mocko, NASA/GSFC/HSL",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "NLDAS_FORB0125_H",
-            "creator": "Xia, Y., et al. (2012), NCEP/EMC",
-            "graphic-preview-description": "NLDAS-2 Secondary Forcing hourly 0.125 degree NARR hybrid level 1 Temperature [K] at 18Z on July 01, 2007.",
-            "title": "NLDAS Secondary Forcing Data L4 Hourly 0.125 x 0.125 degree V002 (NLDAS_FORB0125_H) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_FORB0125_H_002.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKCHJL8HHDP40",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKCHJL8HHDP40",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_FORB0125_H_002.png",
-                    "description": "NLDAS-2 Secondary Forcing hourly 0.125 degree NARR hybrid level 1 Temperature [K] at 18Z on July 01, 2007.",
                     "@type": "dcat:Distribution",
+                    "description": "NLDAS-2 Secondary Forcing hourly 0.125 degree NARR hybrid level 1 Temperature [K] at 18Z on July 01, 2007.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_FORB0125_H_002.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_FORB0125_H_002.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_FORB0125_H_002.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_FORB0125_H.002/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_FORB0125_H.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_FORB0125_H",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_FORB0125_H",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_FORB0125_H.002",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_FORB0125_H.002",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_FORB0125_H.002/doc/gribtab_NLDAS_FORB_hourly.002.txt",
-                    "description": "The GRIBTAB file contains a list of variables, along with the GRIB Product Definition Section (PDS) ID, variable short name, long names, and unit.",
                     "@type": "dcat:Distribution",
+                    "description": "The GRIBTAB file contains a list of variables, along with the GRIB Product Definition Section (PDS) ID, variable short name, long names, and unit.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_FORB0125_H.002/doc/gribtab_NLDAS_FORB_hourly.002.txt",
+                    "mediaType": "text/html",
                     "title": "Access to this dataset's extended metadata"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/README.NLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/README.NLDAS2.pdf",
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
                 }
             ],
+            "editor": "David Mocko, NASA/GSFC/HSL",
+            "graphic-preview-description": "NLDAS-2 Secondary Forcing hourly 0.125 degree NARR hybrid level 1 Temperature [K] at 18Z on July 01, 2007.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_FORB0125_H_002.png",
+            "identifier": "C1233767597-GES_DISC",
+            "issued": "2009-08-01",
+            "keyword": [
+                "surface thermal properties",
+                "altitude",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "land surface",
+                "atmospheric pressure",
+                "earth science",
+                "atmospheric winds",
+                "atmosphere",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/KCHJL8HHDP40",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2009-08-01",
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
+                "https://doi.org/10.1029/2002JD003118",
+                "https://doi.org/10.1175/1520-0450(1984)023<0222:TIOASO>2.0.CO;2",
+                "https://doi.org/10.1029/2002JD003301"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "NLDAS_FORB0125_H",
             "spatial": "-125.0 25.0 -67.0 53.0",
+            "temporal": "1979-01-01T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "NLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NLDAS Secondary Forcing Data L4 Hourly 0.125 x 0.125 degree V002 (NLDAS_FORB0125_H) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0020",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2009-06-04. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0020.",
-            "issued": "2013-12-04",
-            "temporal": "2000-06-22T00:00:00Z/2003-07-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "atmospheric winds",
-                "aerosols",
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "earth science",
-                "precipitation"
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
-            "identifier": "C4211373-LARC_ASDC",
             "description": "The NARSTO_EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA were obtained between April 11, 2001 and July 21, 2003 during the St. Louis - Midwest Supersite program.The overall goal of the St. Louis - Midwest Supersite was to conduct aerosol physical and chemical measurements needed by the health effects community, the atmospheric science community and the regulatory community to properly assess the impact of particulate matter exposure on human health and to develop control strategies to mitigate these effects. Metropolitan St. Louis is a major population center well isolated from other urban centers of even moderate size, and is impacted by both distant and local sources. Local industry includes manufacturing,refining, and chemical plants. St. Louis is climatologically representative of the country's eastern interior, affected by a wide range of synoptic weather patterns and free of localized influences from the Great Lakes, Ocean, Gulf, and mountains. It accordingly provides an ideal environment for studying the sources, transport, and properties of ambient particles.The initial data types included:1) 5-minute PM 2.5 black carbon (880 nm) and uv-absorbing carbon (370 nm) measured by a Magee Scientific Aethalometer (Model AE-21).2) 1-hour PM 2.5 elemental carbon and blank-corrected organic carbon from semicontinuous thermo-optical analysis by the ACE-ASIA method.3) 24-hour PM 2.5 elemental carbon and organic carbon (both blank-corrected) from integrated filter with offline thermo-optical analysis by the ACE-ASIA method.4) 30-minute PM 2.5 metal composition from samples collected with a Semicontinuous Elements in Aerosol Sampler (SEAS) II.5) 5-minute meteorological data (wind, temperature, RH, solar radiation, atmospheric pressure, and precipitation) measured with a Climatronics anemometer, wind vane, thermocouple, lithium chloride sensor, pyranometer, barometer, and tipping bucket.6) 24-hour PM 1.0 filter mass concentration measured by sharp cut cyclone and gravimetric analysis.7) 1-hour PM 2.5 mass measured by an Andersen Continuous Ambient Mass Monitoring System (CAMMS).8) 24-hour PM 2.5 and PM 10 filter mass by Harvard Impactors and laboratory gravimetric analysis.The U.S. EPA Particulate Matter (PM) Supersites Program was an ambient air monitoring research program designed to provide information of value to the atmospheric sciences, and human health and exposure research communities. Eight geographically diverse projects were chosen to specifically address these EPA research priorities: (1) to characterize PM, its constituents, precursors, co-pollutants, atmospheric transport, and its source categories that affect the PM in any region; (2) to address the research questions and scientific uncertainties about PM source-receptor and exposure-health effects relationships; and (3) to compare and evaluate different methods of characterizing PM including testing new and emerging measurement methods. NARSTO (formerly North American Research Strategy for Tropospheric Ozone) is a public/private partnership, whose membership spans government, the utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission is to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are available.",
-            "title": "NARSTO_EPA_SS_ST_LOUIS Air Chemistry, Particulate Matter, Met Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0020",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0020",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C4211373-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C4211373-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0020",
-                    "description": "DOI data set landing page for NARSTO_EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0020",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_st_louis_air_chem_pm_met_data.pdf",
-                    "description": "Guide for NARSTO EPA_SS_ST_LOUIS Air Chemistry, Particulate Matter, and Meteorological Data",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO EPA_SS_ST_LOUIS Air Chemistry, Particulate Matter, and Meteorological Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_epa_ss_st_louis_air_chem_pm_met_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/stlprop.pdf",
-                    "description": "St. Louis-Midwest Supersite Project",
                     "@type": "dcat:Distribution",
+                    "description": "St. Louis-Midwest Supersite Project",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/stlprop.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/stlqapp.pdf",
-                    "description": "Quality Assurance Project Plan for the St. Louis \u2013 Midwest Fine Particulate Matter Supersite",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance Project Plan for the St. Louis \u2013 Midwest Fine Particulate Matter Supersite",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/stlqapp.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/STL_Supersite_QAFR_v1.pdf",
-                    "description": "Quality Assurance Final Report for the St. Louis \u2013 Midwest Fine Particulate Matter Supersite Version 1, July 2007",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Assurance Final Report for the St. Louis \u2013 Midwest Fine Particulate Matter Supersite Version 1, July 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/STL_Supersite_QAFR_v1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/STL-SS_FinalReport_Rev02_March2007.pdf",
-                    "description": "St. Louis \u2013 Midwest Fine Particulate Matter Supersite Revised Final Report, Version 2, March 2007",
                     "@type": "dcat:Distribution",
+                    "description": "St. Louis \u2013 Midwest Fine Particulate Matter Supersite Revised Final Report, Version 2, March 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/STL-SS_FinalReport_Rev02_March2007.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/EPA_SS_ST_LOUIS_AIR_CHEM_PM_MET_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C4211373-LARC_ASDC",
+            "issued": "2013-12-04",
+            "keyword": [
+                "atmospheric winds",
+                "aerosols",
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "earth science",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0020",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>38.5 -90.2 38.5 -90.0 38.7 -90.0 38.7 -90.2 38.5 -90.2</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-06-22T00:00:00Z/2003-07-20T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO_EPA_SS_ST_LOUIS Air Chemistry, Particulate Matter, Met Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/UH70WUPQKCFR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Near Real-time SMAP L1B Radiometer Half-Orbit Time-Ordered Brightness Temperatures V105. Version 105. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/UH70WUPQKCFR.",
-            "issued": "2025-01-08",
-            "temporal": "2025-01-08T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-26",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "microwave",
-                "infrared wavelengths"
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
-            "identifier": "C2257958430-NSIDC_ECS",
             "description": "This Near Real-Time (NRT) data set corresponds to the standard SMAP L1B Radiometer Half-Orbit Time-Ordered Brightness Temperatures (SPL1BTB) product. The data provide calibrated estimates of time-ordered geolocated brightness temperature data measured by the Soil Moisture Active Passive (SMAP) passive microwave radiometer, the SMAP L-band radiometer. These Near Real-Time data are available within three hours of satellite observation. The data are created using the latest available ancillary data and spacecraft and antenna attitude data to reduce latency. The SMAP satellite orbits Earth every two to three days, providing half-orbit, ascending and descending, coverage from 86.4\u00b0S to 86.4\u00b0N in swaths 1000 km across. Data are stored for approximately two to three weeks. Thus, at any given time, users have access to at least fourteen consecutive days of Near Real-Time data through the NSIDC DAAC. Users deciding between the NRT and standard SMAP products should consider the immediacy of their needs versus the quality of the data required. Near real-time data are provided for operational needs whereas standard products meet the quality needs of scientific research. If latency is not a primary concern, users are encouraged to use the standard science product, SPL1BTB (<a href=\"https://doi.org/10.5067/ZHHBN1KQLI20\">https://doi.org/10.5067/ZHHBN1KQLI20</a>).",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "Near Real-time SMAP L1B Radiometer Half-Orbit Time-Ordered Brightness Temperatures V105",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-188,-85,183,86&l=SMAP_L1_Passive_Faraday_Rotation_Fore,SMAP_L1_Passive_Faraday_Rotation_Aft,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUH70WUPQKCFR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUH70WUPQKCFR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/support/how/nsidc-daac-data-subscription-requests",
-                    "description": "Subscribe to have new data automatically sent when the data become available.",
                     "@type": "dcat:Distribution",
+                    "description": "Subscribe to have new data automatically sent when the data become available.",
+                    "downloadURL": "https://nsidc.org/support/how/nsidc-daac-data-subscription-requests",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL1BTB_NRT.105",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP/SPL1BTB_NRT.105",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL1BTB_NRT/versions/105/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SPL1BTB_NRT/versions/105/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL1BTB_NRT+V105",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL1BTB_NRT+V105",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/SMAP/SPL1BTB_NRT.105/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/SMAP/SPL1BTB_NRT.105/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-188%2C-85%2C183%2C86&l=SMAP_L1_Passive_Faraday_Rotation_Fore%2CSMAP_L1_Passive_Faraday_Rotation_Aft%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-188%2C-85%2C183%2C86&l=SMAP_L1_Passive_Faraday_Rotation_Fore%2CSMAP_L1_Passive_Faraday_Rotation_Aft%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/UH70WUPQKCFR",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/UH70WUPQKCFR",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/UH70WUPQKCFR",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/UH70WUPQKCFR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-188,-85,183,86&l=SMAP_L1_Passive_Faraday_Rotation_Fore,SMAP_L1_Passive_Faraday_Rotation_Aft,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C2257958430-NSIDC_ECS",
+            "issued": "2025-01-08",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/UH70WUPQKCFR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -86.4 180.0 86.4",
+            "temporal": "2025-01-08T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Near Real-time SMAP L1B Radiometer Half-Orbit Time-Ordered Brightness Temperatures V105"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M12-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m12-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M12-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m12-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 1 mission phase, covering the period  from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP012 RDR-INFLDSTR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP012 RDR-INFLDSTR V1.0"
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
+            "description": "CRaTER, DLRE, LAMP, LEND, LOLA, LROC, RSS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130617.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-477",
+            "issued": "2018-06-25",
             "keyword": [
                 "rss",
                 "lola",
@@ -931365,361 +931374,333 @@
                 "dlre",
                 "crater"
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
-            "identifier": "NASA-477",
-            "description": "CRaTER, DLRE, LAMP, LEND, LOLA, LROC, RSS",
-            "title": "PDS Lunar Reconnaissance Orbiter Data Release 14",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20130617.shtml",
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
+            "title": "PDS Lunar Reconnaissance Orbiter Data Release 14"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/NAAMES_Merge_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/NAAMES_Merge_Data_1.",
-            "issued": "2022-03-25",
-            "temporal": "2015-11-10T00:00:00Z/2017-09-22T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "keyword": [
-                "clouds",
-                "earth science",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude",
-                "air quality",
-                "aerosols"
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
-            "identifier": "C2303156583-LARC_ASDC",
             "description": "NAAMES_Merge_Data is the North Atlantic Aerosols and Marine Ecosystems Study (NAAMES) pre-generated aircraft merge data files created using data collected during the NAAMES campaign. NAAMES was a NASA funded Earth-Venture Suborbital (EVS) mission with 4 deployments occurring from 2015-2018. Data collection is complete.\r\n\r\nThe NASA North Atlantic Aerosols and Marine Ecosystems Study (NAAMES) project was the first NASA Earth Venture \u2013 Suborbital mission focused on studying the coupled ocean ecosystem and atmosphere. NAAMES utilizes a combination of ship-based, airborne, autonomous sensor, and remote sensing measurements that directly link ocean ecosystem processes, emissions of ocean-generated aerosols and precursor gases, and subsequent atmospheric evolution and processing. Four deployments coincide with the seasonal cycle of phytoplankton in the North Atlantic Ocean: the Winter Transition (November 5 \u2013 December 2, 2015), the Bloom Climax (May 11 \u2013 June 5, 2016), the Deceleration Phase (August 30 \u2013 September 24, 2017), and the Acceleration Phase (March 20 \u2013 April 13, 2018). Ship-based measurements were conducted from the Woods Hole Oceanographic Institution Research Vessel Atlantis in the middle of the North Atlantic Ocean, while airborne measurements were conducted on a NASA Wallops Flight Facility C-130 Hercules that was based at St. John's International Airport, Newfoundland, Canada. Data products in the ASDC archive focus on the NAAMES atmospheric aerosol, cloud, and trace gas data from the ship and aircraft, as well as related satellite and model data subsets. While a few ocean-remote sensing data products (e.g., from the high-spectral resolution lidar) are also included in the ASDC archive, most ocean data products reside in a companion archive at SeaBass.",
-            "title": "NAAMES C-130 Aircraft Merge Data Files",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FNAAMES_Merge_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FNAAMES_Merge_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science.larc.nasa.gov/NAAMES/",
-                    "description": "NAAMES Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "NAAMES Project Home Page",
+                    "downloadURL": "https://science.larc.nasa.gov/NAAMES/",
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
-                    "description": "NASA Earth Expeditions NAAMES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions NAAMES Posts",
+                    "downloadURL": "https://earthobservatory.nasa.gov/blogs/fromthefield/category/naames/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/five-year-nasa-study-to-look-at-the-immense-influence-of-petite-plankton",
-                    "description": "NASA.gov Article \u201cFive-Year NASA Study to Look at the Immense Influence of Petite Plankton\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cFive-Year NASA Study to Look at the Immense Influence of Petite Plankton\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/five-year-nasa-study-to-look-at-the-immense-influence-of-petite-plankton",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/all-in-the-naames-of-ocean-ecosystems-and-climate",
-                    "description": "NASA.gov Article \u201cAll in the NAAMES of Ocean Ecosystems and Climate\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cAll in the NAAMES of Ocean Ecosystems and Climate\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/all-in-the-naames-of-ocean-ecosystems-and-climate",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/naames-returns-to-air-and-sea-to-study-plankton-s-annual-cycle",
-                    "description": "NASA.gov Article \u201cNAAMES Returns to Air and Sea to Study Plankton\u2019s Annual Cycle\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cNAAMES Returns to Air and Sea to Study Plankton\u2019s Annual Cycle\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/naames-returns-to-air-and-sea-to-study-plankton-s-annual-cycle",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC/NAAMES_Merge_Data_1",
-                    "description": "doi for NAAMES_MERGE_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "doi for NAAMES_MERGE_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/NAAMES_Merge_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2303156583-LARC_ASDC",
-                    "description": "Earthdata Search client for NAAMES_MERGE_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for NAAMES_MERGE_DATA_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2303156583-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NAAMES/Merge_Data_1/",
-                    "description": "ASDC Direct Data Download for NAAMES_Merge_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NAAMES_Merge_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NAAMES/Merge_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2303156583-LARC_ASDC",
+            "issued": "2022-03-25",
+            "keyword": [
+                "clouds",
+                "earth science",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude",
+                "air quality",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/NAAMES_Merge_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.0 -80.0 30.0 -30.0 65.0 -30.0 65.0 -80.0 30.0 -80.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-11-10T00:00:00Z/2017-09-22T23:59:59.999Z",
             "theme": [
                 "NAAMES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NAAMES C-130 Aircraft Merge Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-SLOPE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-slope-ops-v1.0_iq9a-48b9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-SLOPE-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-slope-ops-v1.0_iq9a-48b9",
-            "description": "NULL",
-            "title": "MER 1 MARS PANORAMIC CAMERA SLOPE RDR\n                                      OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS PANORAMIC CAMERA SLOPE RDR\n                                      OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/14EU7OLF051V",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Grand Mesa Snow Depth from Snow Pole Time-Lapse Imagery V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/14EU7OLF051V.",
-            "issued": "2019-09-29",
-            "temporal": "2019-09-29T00:00:00Z/2020-06-10T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-10",
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
-            "identifier": "C2236390694-NSIDC_ECS",
             "description": "This data contains snow depth measurements derived from time-lapse images collected by cameras placed around Grand Mesa, CO at 29 sites coincident with other SnowEx 2020 measurements. The field view of all cameras includes a 3.049 m, (10 ft) vertical pole that was painted red with a yellow top to serve as a reference for quantifying snow depth. The time-lapse images are archived separately at NSIDC (SNEX20_TLI).",
-            "title": "SnowEx20 Grand Mesa Snow Depth from Snow Pole Time-Lapse Imagery V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F14EU7OLF051V",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F14EU7OLF051V",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SD_TLI.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_SD_TLI.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_SD_TLI/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_SD_TLI/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/14EU7OLF051V",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/14EU7OLF051V",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/14EU7OLF051V",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/14EU7OLF051V",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2236390694-NSIDC_ECS",
+            "issued": "2019-09-29",
+            "keyword": [
+                "snow/ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/14EU7OLF051V",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.228 39.0 -107.997 39.067",
+            "temporal": "2019-09-29T00:00:00Z/2020-06-10T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Grand Mesa Snow Depth from Snow Pole Time-Lapse Imagery V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://eosweb.larc.nasa.gov/project/calipso/calipso_table",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "radiation",
-                "clouds",
-                "aerosols",
-                "satellite",
-                "eos",
-                "climate"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John M. Kusterer",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000027__1",
+            "describedBy": "https://eosweb.larc.nasa.gov/project/calipso/calipso_table",
             "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international 'A-Train' (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES.",
-            "title": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO)",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -931727,364 +931708,361 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "https://eosweb.larc.nasa.gov/project/calipso/calipso_table",
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-0000027__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "radiation",
+                "clouds",
+                "aerosols",
+                "satellite",
+                "eos",
+                "climate"
+            ],
+            "landingPage": "https://eosweb.larc.nasa.gov/project/calipso/calipso_table",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-EXT3-67P-M31-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-ext3-67p-m31-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-EXT3-67P-M31-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-ext3-67p-m31-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 3 mission phase, covering the period from 2016-06-28T23:25:00.000 to 2016-07-26T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 EXT3-MTP031 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 EXT3-MTP031 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0029-V1.0",
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
-                "sun"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-04-07T06:56:32.500 to 2006-04-07T09:14:36.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0029-v1.0_iqf2-bbfz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0029-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0029-v1.0_iqf2-bbfz",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-04-07T06:56:32.500 to 2006-04-07T09:14:36.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0029 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0029 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D57.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler\r\n. 2019-11-07. VNP43D57. Version 001. VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M4 Daily L3 Global 30ArcSec CMG V001\r\n. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP43D57.001. https://doi.org/10.5067/VIIRS/VNP43D57.001. Digital Science Data. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
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
-                "fn": "undefined",
-                "hasEmail": "mailto:lpdaac@usgs.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1607333961-LPDAAC_ECS",
-            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Black-Sky Albedo for Band M4 (VNP43D57) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D57 is the BSA for VIIRS band M4 (0.555 \u03bcm).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "VNP43D57",
+                "fn": "undefined",
+                "hasEmail": "mailto:lpdaac@usgs.gov"
+            },
             "creator": "Crystal Schaaf, Zhuosen Wang, Xiaoyang Zhang, Alan Strahler",
-            "title": "VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M4 Daily L3 Global 30ArcSec CMG V001",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) Visible Infrared Imaging Radiometer Suite (VIIRS) Bidirectional Reflectance Distribution Function (BRDF) and Albedo Black-Sky Albedo for Band M4 (VNP43D57) is produced daily using 16 days of data at 30 arc second (1,000 meter) resolution. Data are temporally weighted to the ninth day, which is reflected in the file name. The VNP43D product suite is provided in a Climate Modeling Grid (CMG), which covers the entire globe for use in climate simulation models. Due to the large file size, each VNP43D product contains just one data layer. \r\n\r\nVNP43D54 through VNP43D79 are the albedo products of the VNP43D BRDF/Albedo product suite. Black-sky albedo (BSA) and white-sky albedo (WSA) values are provided for the nine VIIRS moderate resolution bands (M1 through M5, M7, M8, M10, and M11) along with the visible, near-infrared (NIR), and shortwave bands included in the VNP43MA3 (https://doi.org/10.5067/VIIRS/VNP43MA3.001) product. In addition to the bands included in VNP43MA3, this product suite includes albedo values for the VIIRS Day/Night Band (DNB). The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. Details regarding methodology are available on the VNP43MA3 product page and in the Algorithm Theoretical Basis Document (ATBD).\r\n\r\nVNP43D57 is the BSA for VIIRS band M4 (0.555 \u03bcm).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D57.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP43D57.001",
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
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D57.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP43D57.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D57.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP43D57.001/",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607333961-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1607333961-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D57.001/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP43D57.001/contents.html",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D57",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/VIIRS/1/VNP43D57",
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
+            "identifier": "C1607333961-LPDAAC_ECS",
+            "issued": "2019-11-07",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP43D57.001",
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
+            "series-name": "VNP43D57",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-19T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP BRDF/Albedo BSA at Solar Noon Band M4 Daily L3 Global 30ArcSec CMG V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2115",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Abshire, J.B., J. Mao, H. Riris, S.R. Kawa, and X. Sun. 2022. ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2115",
-            "issued": "2022-12-29",
-            "temporal": "2016-02-10T14:35:28Z/2016-02-12T02:46:50Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-18",
-            "keyword": [
-                "atmospheric chemistry",
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
-            "identifier": "C2734409850-ORNL_CLOUD",
             "description": "This dataset provides in situ airborne measurements of atmospheric carbon dioxide (CO2) over California and Nevada on February 10-11, 2016. Measurements were taken onboard a DC-8 aircraft during this Active Sensing of CO2 Emissions over Nights, Days and Seasons (ASCENDS) airborne deployment. CO2 was measured with NASA's Atmospheric Vertical Observations of CO2 in the Earth's Troposphere (AVOCET) instrument while over California and Nevada. The objective of this deployment was to assess the performance of the 2016 version of the CO2 Sounder LiDAR.  The two flights were flown to compare results from an experimental LiDAR sensor with the AVOCET instrument.  Aircraft navigation and flight meteorological data are also provided.  The data are provided in ICARTT and comma-separated values (CSV) formats.",
-            "graphic-preview-description": "(a) Flight track for 10 February 2016 flight over Edwards AFB, California. (b) Time-tagged location and altitude plot for the spiral-down maneuver over Edwards AFB for the same flight (Abshire et al., 2018).",
-            "title": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016",
-            "graphic-preview-file": "https://daac.ornl.gov/ASCENDS/guides/ASCENDS_AVOCET_CA_NV_Feb_2016_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2115",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2115",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ASCENDS/guides/ASCENDS_AVOCET_CA_NV_Feb_2016.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ASCENDS/guides/ASCENDS_AVOCET_CA_NV_Feb_2016.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2115",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2115",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/comp/ASCENDSFinalDraft81915_ID0.pdf",
-                    "description": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016: ASCENDSFinalDraft81915_ID0.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016: ASCENDSFinalDraft81915_ID0.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/comp/ASCENDSFinalDraft81915_ID0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/comp/ASCENDS_AVOCET_CA_NV_Feb_2016.pdf",
-                    "description": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016: ASCENDS_AVOCET_CA_NV_Feb_2016.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016: ASCENDS_AVOCET_CA_NV_Feb_2016.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/comp/ASCENDS_AVOCET_CA_NV_Feb_2016.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/comp/Co2LidarBackscatProfiles_1-19-2021_ID4.pdf",
-                    "description": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016: Co2LidarBackscatProfiles_1-19-2021_ID4.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016: Co2LidarBackscatProfiles_1-19-2021_ID4.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/comp/Co2LidarBackscatProfiles_1-19-2021_ID4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/comp/NASA_TP_2018-219034_ASCENDS_ID1.pdf",
-                    "description": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016: NASA_TP_2018-219034_ASCENDS_ID1.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016: NASA_TP_2018-219034_ASCENDS_ID1.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/ascends/ASCENDS_AVOCET_CA_NV_Feb_2016/comp/NASA_TP_2018-219034_ASCENDS_ID1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ASCENDS/guides/ASCENDS_AVOCET_CA_NV_Feb_2016_Fig1.png",
-                    "description": "(a) Flight track for 10 February 2016 flight over Edwards AFB, California. (b) Time-tagged location and altitude plot for the spiral-down maneuver over Edwards AFB for the same flight (Abshire et al., 2018).",
                     "@type": "dcat:Distribution",
+                    "description": "(a) Flight track for 10 February 2016 flight over Edwards AFB, California. (b) Time-tagged location and altitude plot for the spiral-down maneuver over Edwards AFB for the same flight (Abshire et al., 2018).",
+                    "downloadURL": "https://daac.ornl.gov/ASCENDS/guides/ASCENDS_AVOCET_CA_NV_Feb_2016_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "(a) Flight track for 10 February 2016 flight over Edwards AFB, California. (b) Time-tagged location and altitude plot for the spiral-down maneuver over Edwards AFB for the same flight (Abshire et al., 2018).",
+            "graphic-preview-file": "https://daac.ornl.gov/ASCENDS/guides/ASCENDS_AVOCET_CA_NV_Feb_2016_Fig1.png",
+            "identifier": "C2734409850-ORNL_CLOUD",
+            "issued": "2022-12-29",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2115",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-122.1 34.55 -113.53 41.61",
+            "temporal": "2016-02-10T14:35:28Z/2016-02-12T02:46:50Z",
             "theme": [
                 "ASCENDS Airborne",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASCENDS: Active Sensing of CO2 With AVOCET, California and Nevada, 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Livesey, N. and Read, W.. 2015-02-19. ML2BRO. Version 004. MLS/Aura Level 2 Bromine Monoxide (BrO) Mixing Ratio V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2001. https://disc.gsfc.nasa.gov/datacollection/ML2BRO_004.html. Digital Science Data.",
-            "issued": "2015-02-19",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-02-19",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
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
-            "identifier": "C1251101115-GES_DISC",
-            "description": "ML2BRO is the EOS Aura Microwave Limb Sounder (MLS) standard product for bromine monoxide derived from radiances measured by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 10 and 3.16 hPa, and the vertical resolution is about 5.5 km (6 km at 3.16 hPa). Users of the ML2BRO data product should read section 3.2 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2BRO",
             "creator": "Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Bromine Monoxide (BrO) Mixing Ratio V004 (ML2BRO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2BRO_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2BRO is the EOS Aura Microwave Limb Sounder (MLS) standard product for bromine monoxide derived from radiances measured by the 640 GHz radiometer. The data version is 4.2. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). The recommended useful vertical range is between 10 and 3.16 hPa, and the vertical resolution is about 5.5 km (6 km at 3.16 hPa). Users of the ML2BRO data product should read section 3.2 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5), which is based on the version 5 Hierarchical Data Format, or HDF-5. Each file contains two swath objects (profile and column data), each with a set of data and geolocation fields, swath attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -932094,118 +932072,111 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2BRO_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2BRO_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2BRO.004/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2BRO.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2BRO.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level2/ML2BRO.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2BRO_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2BRO_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2BRO_004.png",
+            "identifier": "C1251101115-GES_DISC",
+            "issued": "2015-02-19",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2001",
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
+            "series-name": "ML2BRO",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Bromine Monoxide (BrO) Mixing Ratio V004 (ML2BRO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10999",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-11-01",
-            "temporal": "2012-11-01T00:00:00Z/2015-08-01T00:00:00Z",
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
-                "project",
-                "active"
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
-            "identifier": "TECHPORT_10999",
             "description": "&lt;p&gt;\r\n\tN/A&lt;/p&gt;",
-            "title": "Land Information System for SMAP Tier-1 and AirMOSS Earth Venture-1 Decadal Survey Missions: Integration of SoilSCAPE, remote sensing, and modeling Project",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -932213,88 +932184,118 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "TECHPORT_10999",
+            "issued": "2012-11-01",
+            "keyword": [
+                "nasa headquarters",
+                "project",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10999",
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
+            "temporal": "2012-11-01T00:00:00Z/2015-08-01T00:00:00Z",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Land Information System for SMAP Tier-1 and AirMOSS Earth Venture-1 Decadal Survey Missions: Integration of SoilSCAPE, remote sensing, and modeling Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2151",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hook, S.J., E.W. Fraim, R.O. Green, J.S. Myers, K.J. Thome, M. Fitzgerald, A.B. Kahle, and  Airborne Sensor Facility NASA Ames Research Center. 2023. MASTER: Flight Line Geospatial Polygons and Contextual Data. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2151",
-            "issued": "2024-02-01",
-            "temporal": "1998-12-02T00:00:01Z/2023-05-02T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-06",
-            "keyword": [
-                "earth science",
-                "platform characteristics",
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
-            "identifier": "C2731799041-ORNL_CLOUD",
             "description": "This dataset provides resources for identifying flight lines of interest for the MODIS/ASTER Airborne Simulator (MASTER) instrument based on spatial and temporal criteria. MASTER first flew in 1998 and has ongoing deployments as a Facility Instrument in the NASA Airborne Science Program (ASP). MASTER is a joint project involving the Airborne Sensor Facility (ASF) at the Ames Research Center, the Jet Propulsion Laboratory (JPL), and the Earth Resources Observation and Science Center (EROS).  The primary goal of these airborne campaigns is to demonstrate important science and applications research that is uniquely enabled by the full suite of MASTER thermal infrared bands as well as the contiguous spectroscopic measurements of the AVIRIS (also flown in similar campaigns), or combinations of measurements from both instruments. This dataset includes a table of flight lines with dates, bounding coordinates, site names, investigators involved, flight attributes, and associated campaigns for the MASTER Facility Instrument Collection. A shapefile containing flights for all years, a GeoJSON version of the shapefile, and separate KMZ files for each year allow users to visualize flight line locations using GIS software.",
-            "graphic-preview-description": "Distribution of MASTER flight lines over Greenland, North America, and Pacific Ocean for 1998 to 2022. Insets show details of flights in the U.S. over (A) Washington and Oregon and (B) Louisiana, Mississippi, and Gulf of Mexico. Footprints of acquired imagery are shown as rectangular polygons.",
-            "title": "MASTER: Flight Line Geospatial Polygons and Contextual Data",
-            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_Flightline_Locator_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2151",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2151",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/master/MASTER_Flightline_Locator/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/master/MASTER_Flightline_Locator/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_Flightline_Locator.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_Flightline_Locator.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2151",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2151",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_Flightline_Locator/comp/MASTER_Flightline_Locator.pdf",
-                    "description": "MASTER: Flight Line Geospatial Polygons and Contextual Data: MASTER_Flightline_Locator.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "MASTER: Flight Line Geospatial Polygons and Contextual Data: MASTER_Flightline_Locator.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/master/MASTER_Flightline_Locator/comp/MASTER_Flightline_Locator.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_Flightline_Locator_Fig1.jpg",
-                    "description": "Distribution of MASTER flight lines over Greenland, North America, and Pacific Ocean for 1998 to 2022. Insets show details of flights in the U.S. over (A) Washington and Oregon and (B) Louisiana, Mississippi, and Gulf of Mexico. Footprints of acquired imagery are shown as rectangular polygons.",
                     "@type": "dcat:Distribution",
+                    "description": "Distribution of MASTER flight lines over Greenland, North America, and Pacific Ocean for 1998 to 2022. Insets show details of flights in the U.S. over (A) Washington and Oregon and (B) Louisiana, Mississippi, and Gulf of Mexico. Footprints of acquired imagery are shown as rectangular polygons.",
+                    "downloadURL": "https://daac.ornl.gov/MASTER/guides/MASTER_Flightline_Locator_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Distribution of MASTER flight lines over Greenland, North America, and Pacific Ocean for 1998 to 2022. Insets show details of flights in the U.S. over (A) Washington and Oregon and (B) Louisiana, Mississippi, and Gulf of Mexico. Footprints of acquired imagery are shown as rectangular polygons.",
+            "graphic-preview-file": "https://daac.ornl.gov/MASTER/guides/MASTER_Flightline_Locator_Fig1.jpg",
+            "identifier": "C2731799041-ORNL_CLOUD",
+            "issued": "2024-02-01",
+            "keyword": [
+                "earth science",
+                "platform characteristics",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2151",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-02-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-171.99 -55.38 179.47 78.68",
+            "temporal": "1998-12-02T00:00:01Z/2023-05-02T23:59:59Z",
             "theme": [
                 "MASTER",
                 "FIREX-AQ",
@@ -932304,288 +932305,299 @@
                 "WDTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MASTER: Flight Line Geospatial Polygons and Contextual Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/AA26EWZUNMDK",
             "citation": "Kevin W. Bowman. 2023-10-05. TRPSYL2ALLCRSMGSAO. Version 1. TROPESS CrIS-SNPP L2 for Sao Paulo Megacity, Summary Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/AA26EWZUNMDK. https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGSAO_1.html. Digital Science Data.",
-            "issued": "2023-09-06",
-            "temporal": "2016-01-02T00:00:00Z/2023-10-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-06",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2569849797-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 for Sao Paulo Megacity, Summary Product contains the vertical distribution of six retrieved atmospheric gases (CH4, CO, HDO, NH3, O3 and PAN), along with formal uncertainties measured by the CrIS instrument on the Suomi-NPP satellite. The forward stream summary product is centered on a 3x3 degree region over Sao Paulo for the time period from 2021-02-01 to present. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 17 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSYL2ALLCRSMGSAO",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Sao Paulo Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS CrIS-SNPP L2 for Sao Paulo Megacity, Summary Product V1 (TRPSYL2ALLCRSMGSAO) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGSAO_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAA26EWZUNMDK",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAA26EWZUNMDK",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGSAO_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Sao Paulo Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Sao Paulo Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGSAO_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGSAO_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSYL2ALLCRSMGSAO_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGSAO.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGSAO.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2ALLCRSMGSAO_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSYL2ALLCRSMGSAO_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGSAO.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGSAO.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGSAO.1/doc/TROPESS_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_MegaCities_Summary/TRPSYL2ALLCRSMGSAO.1/doc/TROPESS_Forward_Stream_README.pdf",
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
+            "graphic-preview-description": "TROPESS CrIS-SNPP Sao Paulo Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSYL2ALLCRSMGSAO_Sample.png",
+            "identifier": "C2569849797-GES_DISC",
+            "issued": "2023-09-06",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/AA26EWZUNMDK",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-06",
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
+            "series-name": "TRPSYL2ALLCRSMGSAO",
             "spatial": "-48.0 -25.0 -45.0 -22.0",
+            "temporal": "2016-01-02T00:00:00Z/2023-10-09T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 for Sao Paulo Megacity, Summary Product V1 (TRPSYL2ALLCRSMGSAO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2IRKNS.008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2IRKNS.008. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2019-02-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT Gluck",
                 "hasEmail": "mailto:scott.gluck@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1620804451-LARC",
             "description": "TL2IRKNS_8 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Instantaneous Radiative Kernel Nadir Special Observation Version 8 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. Using TES radiances, Jacobians and ozone profiles with hemispherical integration, it was possible to compute the TOA (top-of-atmosphere) flux from the infrared ozone band (in W/m2), instantaneous radiative kernels (IRK) (in W/m2/ppb), and logarithmic instantaneous radiative forcing kernels (LIRK) (in W/m2) for ozone. The IRK provided unique information for questions of chemistry-climate coupling since this was a direct measure of the radiative role of ozone, which explicitly accounted for more dominant radiative processes such as clouds and water vapor. These products can be compared to climate model predictions of the same quantities.\r\rTES Level 2 data contains retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits. \r\rA nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consisted of four files, where each file was composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. A Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species volume mixing ratios (VMRs), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals were not reported. \r\rThe organization of data within the Swath object was based on a superset of the Upper Atmosphere Research Satellite (UARS) pressure levels that was used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files each observation could potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels were not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altit",
-            "title": "TES/Aura L2 Instantaneous Radiative Kernel Nadir Special Observation V008",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2IRKNS.008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2IRKNS.008",
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2IRKNS.008",
-                    "description": "DOI data set landing page for TL2IRKNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2IRKNS_8",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2IRKNS.008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1620804451-LARC",
-                    "description": "Earthdata Search for TL2IRKNS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2IRKNS_8 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1620804451-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2IRKNS.008/",
-                    "description": "ASDC Direct Data Download for TL2IRKNS_8",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2IRKNS_8",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2IRKNS.008/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2SpecObs.cgi",
-                    "description": "Report of TES Level 2 Special Observation Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Special Observation Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2SpecObs.cgi",
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
+            "identifier": "C1620804451-LARC",
+            "issued": "2019-02-27",
+            "keyword": [
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2IRKNS.008",
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
+            "title": "TES/Aura L2 Instantaneous Radiative Kernel Nadir Special Observation V008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://planetarynames.wr.usgs.gov/Page/venus1to10m_Altimetry",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Michael Kelly",
+                "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
+            },
+            "description": "This set of maps diplays altimetric radar images of Venus approved by the International Astronomical Union (IAU).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/Aphrodite.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-156",
             "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "images",
                 "quadrangles",
@@ -932597,79 +932609,81 @@
                 "usgs",
                 "radar"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Michael Kelly",
-                "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
-            },
+            "landingPage": "http://planetarynames.wr.usgs.gov/Page/venus1to10m_Altimetry",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
             },
-            "identifier": "OCIO-Fitara-156",
-            "description": "This set of maps diplays altimetric radar images of Venus approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Venus: 1:10 million-scale Altimetry Quadrangles: Aphrodite",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/Aphrodite.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Venus: 1:10 million-scale Altimetry Quadrangles: Aphrodite"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1149-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-01T19:58:35.000 to 2015-11-02T04:59:27.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1149-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1149-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1149-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-01T19:58:35.000 to 2015-11-02T04:59:27.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1149 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1149 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/iqsc-nzgw",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "A combination therapy of electromagnetic fields (EMF) and simulated microgravity (SMG) has not been examined in regenerative medicine of cartilage. In the present study a bioreactor system using extremely low-frequency EMF and SMG was applied during the chondrogenic differentiation of human mesenchymal stem cells (hMSCs). It was hypothesized that a beneficial effect of EMF regarding chondrogenesis (COL2A) could be combined with an avoiding effect of SMG regarding hypertrophy (COLXA1) of cartilage. Pellet cultures of hMSCs formed cartilaginous tissue under the addition of growth factors (FGF; TGF-beta3). Pure SMG reduced COLXA1 expression but also COL2A expression of hMSCs. Pure EMF showed no gene expression changes of hMSCs during chondrogenic differentiation. Combining EMF/SMG resulted in a re-increase of COL2A but did not reach control levels. The COL2A to COLXA1 ratio of combined EMF/SMG was not significantly different from control levels. The combination therapy of EMF/SMG did not significantly improve the chondrogenic potential of hMSCs. chondrogenic differentiation electromagnetic stimulation-control 1 timepoint with/without stimulation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-124",
+                    "mediaType": "text/html",
+                    "title": "Effect of electromagnetic fields on the chondrogenic differentiation under microgravity conditions"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-124_iqsc-nzgw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse57298-5",
                 "p-gse57298-7",
@@ -932689,477 +932703,443 @@
                 "p-gse57298-1",
                 "growth protocol"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/iqsc-nzgw",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-124_iqsc-nzgw",
-            "description": "A combination therapy of electromagnetic fields (EMF) and simulated microgravity (SMG) has not been examined in regenerative medicine of cartilage. In the present study a bioreactor system using extremely low-frequency EMF and SMG was applied during the chondrogenic differentiation of human mesenchymal stem cells (hMSCs). It was hypothesized that a beneficial effect of EMF regarding chondrogenesis (COL2A) could be combined with an avoiding effect of SMG regarding hypertrophy (COLXA1) of cartilage. Pellet cultures of hMSCs formed cartilaginous tissue under the addition of growth factors (FGF; TGF-beta3). Pure SMG reduced COLXA1 expression but also COL2A expression of hMSCs. Pure EMF showed no gene expression changes of hMSCs during chondrogenic differentiation. Combining EMF/SMG resulted in a re-increase of COL2A but did not reach control levels. The COL2A to COLXA1 ratio of combined EMF/SMG was not significantly different from control levels. The combination therapy of EMF/SMG did not significantly improve the chondrogenic potential of hMSCs. chondrogenic differentiation electromagnetic stimulation-control 1 timepoint with/without stimulation.",
-            "title": "Effect of electromagnetic fields on the chondrogenic differentiation under microgravity conditions",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-124",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Effect of electromagnetic fields on the chondrogenic differentiation under microgravity conditions"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Effect of electromagnetic fields on the chondrogenic differentiation under microgravity conditions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1589",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Denbina, M., M. Simard, B.V. Riel, B.P. Hawkins, and N. Pinto. 2018. AfriSAR: Rainforest Canopy Height Derived from PolInSAR and Lidar Data, Gabon. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1589",
-            "issued": "2018-07-06",
-            "temporal": "2016-02-27T00:00:00Z/2016-03-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "land surface",
-                "topography",
-                "vegetation",
-                "earth science",
-                "biosphere",
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
-            "identifier": "C2734258687-ORNL_CLOUD",
             "description": "This dataset provides estimates of forest canopy height and canopy height uncertainty for study areas in the Pongara National Park and the Lope National Park, Gabon. Two canopy height products are included: 1) Canopy height was derived from multi-baseline Polarimetric Interferometric Synthetic Aperture Radar (PolInSAR) data using an inversion of the random volume over ground (RVoG) model and Kapok, an open source Python library. 2) Canopy height was derived from a fusion of PolInSAR and Land, Vegetation, and Ice Sensor (LVIS) Lidar data. This dataset also includes various intermediate parameters of the PolInSAR data (including radar backscatter, coherence, and viewing and terrain geometry) which provide additional insight into the input data used to invert the RVoG model and accuracy of the canopy height estimates. The AfriSAR campaign was flown from 2016-02-27 to 2016-03-08. AfriSAR data were collected by NASA, in collaboration with the European Space Agency (ESA) and the Gabonese Space Agency.",
-            "graphic-preview-description": "PolInSAR-derived canopy height map for Lope National Park, Gabon. The study areas contain a wide range of forest canopy heights up to 50 m. (figure from Denbina et al., 2017).",
-            "title": "AfriSAR: Rainforest Canopy Height Derived from PolInSAR and Lidar Data, Gabon",
-            "graphic-preview-file": "https://daac.ornl.gov/AFRISAR/guides/PolInSAR_Canopy_Height_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1589",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1589",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/afrisar/PolInSAR_Canopy_Height/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/afrisar/PolInSAR_Canopy_Height/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/AFRISAR/guides/PolInSAR_Canopy_Height.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/AFRISAR/guides/PolInSAR_Canopy_Height.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1589",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1589",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/afrisar/PolInSAR_Canopy_Height/comp/denbina_kapok_polinsar_canopyht_methods.pdf",
-                    "description": "A file provided by the investigator which provides additional details regarding methods",
                     "@type": "dcat:Distribution",
+                    "description": "A file provided by the investigator which provides additional details regarding methods",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/afrisar/PolInSAR_Canopy_Height/comp/denbina_kapok_polinsar_canopyht_methods.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/afrisar/PolInSAR_Canopy_Height/comp/lope_kapok_processing_script.py",
-                    "description": "AfriSAR: Rainforest Canopy Height Derived from PolInSAR and Lidar Data, Gabon: lope_kapok_processing_script.py",
                     "@type": "dcat:Distribution",
+                    "description": "AfriSAR: Rainforest Canopy Height Derived from PolInSAR and Lidar Data, Gabon: lope_kapok_processing_script.py",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/afrisar/PolInSAR_Canopy_Height/comp/lope_kapok_processing_script.py",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/afrisar/PolInSAR_Canopy_Height/comp/PolInSAR_Canopy_Height.pdf",
-                    "description": "A PDF of the guide document",
                     "@type": "dcat:Distribution",
+                    "description": "A PDF of the guide document",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/afrisar/PolInSAR_Canopy_Height/comp/PolInSAR_Canopy_Height.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/afrisar/PolInSAR_Canopy_Height/comp/pongara_kapok_processing_script.py",
-                    "description": "AfriSAR: Rainforest Canopy Height Derived from PolInSAR and Lidar Data, Gabon: pongara_kapok_processing_script.py",
                     "@type": "dcat:Distribution",
+                    "description": "AfriSAR: Rainforest Canopy Height Derived from PolInSAR and Lidar Data, Gabon: pongara_kapok_processing_script.py",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/afrisar/PolInSAR_Canopy_Height/comp/pongara_kapok_processing_script.py",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/AFRISAR/guides/PolInSAR_Canopy_Height_Fig1.png",
-                    "description": "PolInSAR-derived canopy height map for Lope National Park, Gabon. The study areas contain a wide range of forest canopy heights up to 50 m. (figure from Denbina et al., 2017).",
                     "@type": "dcat:Distribution",
+                    "description": "PolInSAR-derived canopy height map for Lope National Park, Gabon. The study areas contain a wide range of forest canopy heights up to 50 m. (figure from Denbina et al., 2017).",
+                    "downloadURL": "https://daac.ornl.gov/AFRISAR/guides/PolInSAR_Canopy_Height_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1589",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1589",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "PolInSAR-derived canopy height map for Lope National Park, Gabon. The study areas contain a wide range of forest canopy heights up to 50 m. (figure from Denbina et al., 2017).",
+            "graphic-preview-file": "https://daac.ornl.gov/AFRISAR/guides/PolInSAR_Canopy_Height_Fig1.png",
+            "identifier": "C2734258687-ORNL_CLOUD",
+            "issued": "2018-07-06",
+            "keyword": [
+                "land surface",
+                "topography",
+                "vegetation",
+                "earth science",
+                "biosphere",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1589",
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
             "spatial": "9.29 -0.35 11.83 0.24",
+            "temporal": "2016-02-27T00:00:00Z/2016-03-08T23:59:59Z",
             "theme": [
                 "AfriSAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AfriSAR: Rainforest Canopy Height Derived from PolInSAR and Lidar Data, Gabon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CVP1-CHECKOUT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 1 mission phase, covering the period  from 2004-03-05T00:00:00.000 to 2004-06-06T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cvp1-checkout-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "eps aqr",
                 "c/linear (2002 t7)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-4-CVP1-CHECKOUT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-4-cvp1-checkout-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMMISSIONING 1 mission phase, covering the period  from 2004-03-05T00:00:00.000 to 2004-06-06T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CVP1 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 4 CVP1 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-5-CDR-EROS%2FORBIT-V1.0",
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
+            "description": "NLR Level 2 Data Products include the along-track profiles of NLR data in SI units, together with spacecraft position, orientation, and timing data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-5-cdr-eros-orbit-v1.0_iqxu-i9i2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-5-CDR-EROS%2FORBIT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-5-cdr-eros-orbit-v1.0_iqxu-i9i2",
-            "description": "NLR Level 2 Data Products include the along-track profiles of NLR data in SI units, together with spacecraft position, orientation, and timing data.",
-            "title": "NEAR NLR LEVEL 2 DATA PRODUCTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR NLR LEVEL 2 DATA PRODUCTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PRA-2-RDR-HIGHRATE-60MS-V1.0",
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
-                "uranus",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set (VG2-U-PRA-2-RDR-HIGHRATE-60MS-V1.0) contains data\nacquired by the Voyager-2 Planetary Radio Astronomy (PRA) instrument\nduring the Uranus encounter.  Since the PRA instrument is able to\nobserve planetary phenomenon at much larger ranges than other fields\nand particles experiments, thus the PRA data cover a variable and\nlonger encounter period. PRA lowband data provided here cover the\nentire Uranus Encounter Phase (1985-10-24 to 1988-07-14).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pra-2-rdr-highrate-60ms-v1.0_iqxx-bmnn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "uranus",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PRA-2-RDR-HIGHRATE-60MS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pra-2-rdr-highrate-60ms-v1.0_iqxx-bmnn",
-            "description": "This data set (VG2-U-PRA-2-RDR-HIGHRATE-60MS-V1.0) contains data\nacquired by the Voyager-2 Planetary Radio Astronomy (PRA) instrument\nduring the Uranus encounter.  Since the PRA instrument is able to\nobserve planetary phenomenon at much larger ranges than other fields\nand particles experiments, thus the PRA data cover a variable and\nlonger encounter period. PRA lowband data provided here cover the\nentire Uranus Encounter Phase (1985-10-24 to 1988-07-14).",
-            "title": "VG2 URA PRA EDITED RDR HIGH RATE\n                                      60MS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG2 URA PRA EDITED RDR HIGH RATE\n                                      60MS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ATLAS/ATL16.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ATLAS/ICESat-2 L3B Weekly Gridded Atmosphere V005. Version 005. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/ATLAS/ATL16.005.",
-            "issued": "2018-10-15",
-            "temporal": "2018-10-13T00:00:00Z/2024-09-02T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-10",
-            "keyword": [
-                "lidar",
-                "snow/ice",
-                "aerosols",
-                "atmosphere",
-                "clouds",
-                "cryosphere",
-                "spectral/engineering",
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
-            "identifier": "C2737997243-NSIDC_ECS",
             "description": "This product reports weekly global cloud fraction, total column optical depth over the oceans, polar cloud fraction, blowing snow frequency, apparent surface reflectivity, and ground detection frequency.",
-            "title": "ATLAS/ICESat-2 L3B Weekly Gridded Atmosphere V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL16.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FATLAS%2FATL16.005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL16.005/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ATLAS/ATL16.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL16+V005",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ATL16+V005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL16/versions/5/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ATL16/versions/5/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL16.005",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL16.005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL16.005",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ATLAS/ATL16.005",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2737997243-NSIDC_ECS",
+            "issued": "2018-10-15",
+            "keyword": [
+                "lidar",
+                "snow/ice",
+                "aerosols",
+                "atmosphere",
+                "clouds",
+                "cryosphere",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ATLAS/ATL16.005",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-10-13T00:00:00Z/2024-09-02T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATLAS/ICESat-2 L3B Weekly Gridded Atmosphere V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1576",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ju, J., and J.G. Masek. 2018. ABoVE: NDVI Trends across Alaska and Canada from Landsat, 1984-2012. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1576",
-            "issued": "2019-03-14",
-            "temporal": "1984-01-01T00:00:00Z/2012-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
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
-            "identifier": "C2162131333-ORNL_CLOUD",
             "description": "This dataset provides the summer NDVI trend and trend significance for the period 1984-2012 over Alaska and Canada. The NDVI were calculated per-pixel from all available peak-summer 30-m Landsat 5 and 7 surface reflectance data for the period. NDVI time series were assembled for each 30-m land location (i.e., non-water, non-snow), from observations that were unaffected by clouds as indicated by data-quality masks and following additional processing to remove anomalous NDVI values. A simple linear regression via ordinary least squares was applied to the per-pixel NDVI time series. The slope of the regression was taken as the annual NDVI trend (unit NDVI change per year) and is reported in the \"trend\" data files. A Student's t-test was used to assess the significance of the trend and the per-pixel significance is reported in the \"trend_sig\" data files. A significant positive slope indicates a greening trend, and a significant negative slope indicates a browning trend.",
-            "graphic-preview-description": "Figure 1: NDVI trends derived from 30-m Landsat NDVI times series for 1984-2012 for Canada and Alaska (Ju and Masek, 2016).",
-            "title": "ABoVE: NDVI Trends across Alaska and Canada from Landsat, 1984-2012",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Vegetation_greenness_trend_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1576",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1576",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Vegetation_greenness_trend/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Vegetation_greenness_trend/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Vegetation_greenness_trend.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Vegetation_greenness_trend.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1576",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1576",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Vegetation_greenness_trend/comp/Vegetation_greenness_trend.pdf",
-                    "description": "ABoVE: Vegetation Greenness Trend from Landsat Imagery, Alaska and Canada, 1984-2012: Vegetation_greenness_trend.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Vegetation Greenness Trend from Landsat Imagery, Alaska and Canada, 1984-2012: Vegetation_greenness_trend.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Vegetation_greenness_trend/comp/Vegetation_greenness_trend.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Vegetation_greenness_trend_Fig1.png",
-                    "description": "Figure 1: NDVI trends derived from 30-m Landsat NDVI times series for 1984-2012 for Canada and Alaska (Ju and Masek, 2016).",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: NDVI trends derived from 30-m Landsat NDVI times series for 1984-2012 for Canada and Alaska (Ju and Masek, 2016).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Vegetation_greenness_trend_Fig1.png",
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
+            "graphic-preview-description": "Figure 1: NDVI trends derived from 30-m Landsat NDVI times series for 1984-2012 for Canada and Alaska (Ju and Masek, 2016).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Vegetation_greenness_trend_Fig1.png",
+            "identifier": "C2162131333-ORNL_CLOUD",
+            "issued": "2019-03-14",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1576",
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
             "spatial": "-169.97 41.61 -50.17 80.51",
+            "temporal": "1984-01-01T00:00:00Z/2012-12-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: NDVI Trends across Alaska and Canada from Landsat, 1984-2012"
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
-                "pds",
-                "themis"
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
-            "identifier": "NASA-669",
             "description": "THEMIS, SPICE",
-            "title": "PDS Odyssey Data Release 29",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -933167,831 +933147,853 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-669",
+            "issued": "2018-06-25",
+            "keyword": [
+                "spice",
+                "pds",
+                "themis"
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
+            "title": "PDS Odyssey Data Release 29"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/BOA/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/BOA/DATA001.",
-            "issued": "1991-05-17",
-            "temporal": "1991-05-17T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "ocean chemistry",
-                "salinity/density",
-                "earth science",
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
-            "identifier": "C1647028408-OB_DAAC",
             "description": "Measurements used to develop the Bio-Optical Algorithm (BOA), taken between 1991 and 1995 in the Northeast Pacific, North Atlantic, Gulf of Mexico, and Arabian Sea.",
-            "title": "Measurements used to develop the Bio-Optical Algorithm (BOA)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBOA%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FBOA%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BOA/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/BOA/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1647028408-OB_DAAC",
+            "issued": "1991-05-17",
+            "keyword": [
+                "ocean optics",
+                "ocean chemistry",
+                "salinity/density",
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/BOA/DATA001",
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
+            "temporal": "1991-05-17T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements used to develop the Bio-Optical Algorithm (BOA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-TNOCENALB-V4.0",
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
+            "description": "This data set is a compilation of published diameters, albedos, and densities for Transneptunian Objects (TNOs) and Centaurs.  A total of 190 objects are listed, many with more than one entry.  This version covers published values through 31 March 2016.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-tnocenalb-v4.0_ira4-e6y6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-TNOCENALB-V4.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-tnocenalb-v4.0_ira4-e6y6",
-            "description": "This data set is a compilation of published diameters, albedos, and densities for Transneptunian Objects (TNOs) and Centaurs.  A total of 190 objects are listed, many with more than one entry.  This version covers published values through 31 March 2016.",
-            "title": "TNO AND CENTAUR DIAMETERS, ALBEDOS, AND\n        DENSITIES V4.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TNO AND CENTAUR DIAMETERS, ALBEDOS, AND\n        DENSITIES V4.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHMTA-3US28",
             "citation": "NOAA/STAR. 2021-04-05. AVHRRF_MA-STAR-L3U-v2.80. Version 2.80. GHRSST L3U Metop-C AVHRR FRAC ACSPO v2.80 0.02-deg Dataset. Camp Springs, MD (USA). Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHMTA-3US28. https://podaac.jpl.nasa.gov/GHRSST. NOAA/STAR, The GHRSST Project Office, 2021-04-05, GHRSST NOAA/STAR Metop-A AVHRR FRAC ACSPO v2.80 0.02 L3U Dataset (GDS v2), https://podaac.jpl.nasa.gov/GHRSST.",
-            "issued": "2021-03-15",
-            "temporal": "2006-12-01T00:00:00Z/2021-11-14T23:59:59.900Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-15",
-            "references": [
-                "https://doi.org/10.3390/rs13204046"
-            ],
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
-            "identifier": "C2205121413-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This L3U (Level 3 Uncollated) dataset contains global daily Sea Surface Temperature (SST) on a 0.02 degree grid resolution. It is produced by the National Oceanic and Atmospheric Administration (NOAA) Advanced Clear Sky Processor for Ocean (ACSPO) using L2P (Level 2 Preprocessed) product acquired from the Meteorological Operational satellite A (Metop-A) Advanced Very High Resolution Radiometer 3 (AVHRR/3) (https://podaac.jpl.nasa.gov/dataset/AVHRRF_MA-STAR-L2P-v2.80 ) in Full Resolution Area Coverage (FRAC) mode as input. It is distributed as 10-minute granules in netCDF-4 format, compliant with the Group for High Resolution Sea Surface Temperature (GHRSST) Data Specification version 2 (GDS2). There are 144 granules per 24-hour interval. Fill values are reported in all invalid pixels, including land pixels with >5 km inland. For each valid water pixel (defined as ocean, sea, lake or river), and up to 5 km inland, the following major layers are reported: SSTs and ACSPO clear-sky mask (ACSM; provided in each grid as part of l2p_flags, which also includes day/night, land, ice, twilight, and glint flags). Only input L2P SSTs with QL=5 were gridded, so all valid SSTs are recommended for the users. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (SSES bias and standard deviation) are reported in each pixel with valid SST. Ancillary layers include wind speed and ACSPO minus reference Canadian Meteorological Centre (CMC) Level 4 (L4) SST. The ACSPO Metop-A AVHRR FRAC L3U product is monitored and validated against iQuam in situ data (Xu and Ignatov, 2014) in the NOAA SST Quality Monitor (SQUAM) system (Dash et al, 2010). SST imagery and clear-sky mask are evaluated, and checked for consistency with L2P and other satellites/sensors SST products, in the NOAA ACSPO Regional Monitor for SST (ARMS) system. More information about the dataset is found at AVHRRF_MA-STAR-L2P-v2.80 and in (Pryamitsyn et al., 2021).",
-            "release-place": "Camp Springs, MD (USA)",
-            "series-name": "AVHRRF_MA-STAR-L3U-v2.80",
             "creator": "NOAA/STAR",
-            "title": "GHRSST NOAA/STAR Metop-A AVHRR FRAC ACSPO v2.80 0.02 L3U Dataset (GDS v2)",
-            "graphic-preview-description": "SOTO (State Of The Ocean) Visualization",
-            "graphic-preview-file": "https://soto.podaac.earthdatacloud.nasa.gov/?l=AVHRR_MetOp-A_L3U_Sea_Surface_Temperature,BlueMarble_ShadedRelief_Bathymetry,Coastlines_15m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This L3U (Level 3 Uncollated) dataset contains global daily Sea Surface Temperature (SST) on a 0.02 degree grid resolution. It is produced by the National Oceanic and Atmospheric Administration (NOAA) Advanced Clear Sky Processor for Ocean (ACSPO) using L2P (Level 2 Preprocessed) product acquired from the Meteorological Operational satellite A (Metop-A) Advanced Very High Resolution Radiometer 3 (AVHRR/3) (https://podaac.jpl.nasa.gov/dataset/AVHRRF_MA-STAR-L2P-v2.80 ) in Full Resolution Area Coverage (FRAC) mode as input. It is distributed as 10-minute granules in netCDF-4 format, compliant with the Group for High Resolution Sea Surface Temperature (GHRSST) Data Specification version 2 (GDS2). There are 144 granules per 24-hour interval. Fill values are reported in all invalid pixels, including land pixels with >5 km inland. For each valid water pixel (defined as ocean, sea, lake or river), and up to 5 km inland, the following major layers are reported: SSTs and ACSPO clear-sky mask (ACSM; provided in each grid as part of l2p_flags, which also includes day/night, land, ice, twilight, and glint flags). Only input L2P SSTs with QL=5 were gridded, so all valid SSTs are recommended for the users. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (SSES bias and standard deviation) are reported in each pixel with valid SST. Ancillary layers include wind speed and ACSPO minus reference Canadian Meteorological Centre (CMC) Level 4 (L4) SST. The ACSPO Metop-A AVHRR FRAC L3U product is monitored and validated against iQuam in situ data (Xu and Ignatov, 2014) in the NOAA SST Quality Monitor (SQUAM) system (Dash et al, 2010). SST imagery and clear-sky mask are evaluated, and checked for consistency with L2P and other satellites/sensors SST products, in the NOAA ACSPO Regional Monitor for SST (ARMS) system. More information about the dataset is found at AVHRRF_MA-STAR-L2P-v2.80 and in (Pryamitsyn et al., 2021).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMTA-3US28",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMTA-3US28",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://doi.org/10.1002/2013JD020637",
-                    "description": "Evaluation and Selection of SST Regression Algorithms for JPSS VIIRS",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation and Selection of SST Regression Algorithms for JPSS VIIRS",
+                    "downloadURL": "https://doi.org/10.1002/2013JD020637",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://doi.org/10.1175/2010JTECHO756.1",
-                    "description": "The SST Quality Monitor (SQUAM)",
                     "@type": "dcat:Distribution",
+                    "description": "The SST Quality Monitor (SQUAM)",
+                    "downloadURL": "https://doi.org/10.1175/2010JTECHO756.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/socd/sst/arms/",
-                    "description": "ACSPO Regional Monitor for SST (ARMS)",
                     "@type": "dcat:Distribution",
+                    "description": "ACSPO Regional Monitor for SST (ARMS)",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/socd/sst/arms/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1117/1.JRS.11.032405",
-                    "description": "JPSS VIIRS level 3 uncollated sea surface temperature product at NOAA, J",
                     "@type": "dcat:Distribution",
+                    "description": "JPSS VIIRS level 3 uncollated sea surface temperature product at NOAA, J",
+                    "downloadURL": "https://doi.org/10.1117/1.JRS.11.032405",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-15-0166.1",
-                    "description": "Sensor-Specific Error Statistics for SST in the Advanced Clear-Sky Processor for Oceans",
                     "@type": "dcat:Distribution",
+                    "description": "Sensor-Specific Error Statistics for SST in the Advanced Clear-Sky Processor for Oceans",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-15-0166.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/2010JTECHA1413.1",
-                    "description": "Clear-Sky Mask for ACSPO",
                     "@type": "dcat:Distribution",
+                    "description": "Clear-Sky Mask for ACSPO",
+                    "downloadURL": "https://doi.org/10.1175/2010JTECHA1413.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-13-00121.1",
-                    "description": "In situ SST Quality Monitor (iQuam)",
                     "@type": "dcat:Distribution",
+                    "description": "In situ SST Quality Monitor (iQuam)",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-13-00121.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://www.ghrsst.org/",
-                    "description": "GHRSST Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project Home Page",
+                    "downloadURL": "https://www.ghrsst.org/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3390/rs8040346",
-                    "description": "Sensor Stability for SST (3S): Toward Improved Long-Term Characterization of AVHRR Thermal Bands",
                     "@type": "dcat:Distribution",
+                    "description": "Sensor Stability for SST (3S): Toward Improved Long-Term Characterization of AVHRR Thermal Bands",
+                    "downloadURL": "https://doi.org/10.3390/rs8040346",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-10-05023.1",
-                    "description": "Monitoring of IR Clear-sky Radiances over Oceans for SST (MICROS)",
                     "@type": "dcat:Distribution",
+                    "description": "Monitoring of IR Clear-sky Radiances over Oceans for SST (MICROS)",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-10-05023.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic Data Readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic Data Readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRF_MA-STAR-L3U-v2.80.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRF_MA-STAR-L3U-v2.80.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205121413-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205121413-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205121413-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205121413-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://soto.podaac.earthdatacloud.nasa.gov/?l=AVHRR_MetOp-A_L3U_Sea_Surface_Temperature%2CBlueMarble_ShadedRelief_Bathymetry%2CCoastlines_15m",
-                    "description": "SOTO (State Of The Ocean) Visualization",
                     "@type": "dcat:Distribution",
+                    "description": "SOTO (State Of The Ocean) Visualization",
+                    "downloadURL": "https://soto.podaac.earthdatacloud.nasa.gov/?l=AVHRR_MetOp-A_L3U_Sea_Surface_Temperature%2CBlueMarble_ShadedRelief_Bathymetry%2CCoastlines_15m",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 }
             ],
+            "graphic-preview-description": "SOTO (State Of The Ocean) Visualization",
+            "graphic-preview-file": "https://soto.podaac.earthdatacloud.nasa.gov/?l=AVHRR_MetOp-A_L3U_Sea_Surface_Temperature,BlueMarble_ShadedRelief_Bathymetry,Coastlines_15m",
+            "identifier": "C2205121413-POCLOUD",
+            "issued": "2021-03-15",
+            "keyword": [
+                "earth science",
+                "ocean temperature",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHMTA-3US28",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs13204046"
+            ],
+            "release-place": "Camp Springs, MD (USA)",
+            "series-name": "AVHRRF_MA-STAR-L3U-v2.80",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-12-01T00:00:00Z/2021-11-14T23:59:59.900Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST NOAA/STAR Metop-A AVHRR FRAC ACSPO v2.80 0.02 L3U Dataset (GDS v2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M09-REFLECT-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m09-reflect-v1.0_irb6-neaf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M09-REFLECT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m09-reflect-v1.0_irb6-neaf",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-10-24T10:00:00.000 to 2014-11-21T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP009 RDR-REFLECT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP009 RDR-REFLECT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASTER/ASTWBD.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team. 2019-08-05. ASTWBD.001. ASTER Global Water Bodies Database V001. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ASTER/ASTWBD.001. https://doi.org/10.5067/ASTER/ASTWBD.001. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2019-08-05",
-            "temporal": "2000-03-01T00:00:00Z/2013-11-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-05",
-            "keyword": [
-                "surface water",
-                "earth science",
-                "topography",
-                "land surface",
-                "national geospatial data asset",
-                "ngda",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:mjabrams@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1575734433-LPDAAC_ECS",
-            "description": "The ASTER Global Water Bodies Database (ASTWBD) Version 1 data product provides global coverage of water bodies larger than 0.2 square kilometers at a spatial resolution of 1 arc second (approximately 30 meters) at the equator, along with associated elevation information. \r\n\r\nThe ASTWBD data product was created in conjunction with the ASTER Global Digital Elevation Model (ASTER GDEM) Version 3 data product by the Sensor Information Laboratory Corporation (SILC) in Tokyo. The ASTER GDEM Version 3 data product was generated using ASTER Level 1A (https://doi.org/10.5067/ASTER/AST_L1A.003) scenes acquired between March 1, 2000, and November 30, 2013. The ASTWBD data product was then generated to correct elevation values of water body surfaces.\r\n\r\nTo generate the ASTWBD data product, water bodies were separated from land areas and then classified into three categories: ocean, river, or lake. Oceans and lakes have a flattened, constant elevation value. The effects of sea ice were manually removed from areas classified as oceans to better delineate ocean shorelines in high latitude areas. For lake waterbodies, the elevation for each lake was calculated from the perimeter elevation data using the mosaic image that covers the entire area of the lake. Rivers presented a unique challenge given that their elevations gradually step down from upstream to downstream; therefore, visual inspection and other manual detection methods were required. \r\n\r\nThe geographic coverage of the ASTWBD extends from 83\u00b0N to 83\u00b0S. Each tile is distributed in GeoTIFF format and referenced to the 1984 World Geodetic System (WGS84)/1996 Earth Gravitational Model (EGM96) geoid. Each data product is provided as a zipped file that contains an attribute file with the water body classification information and a DEM file, which provides elevation information in meters.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "ASTWBD.001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "NASA/METI/AIST/Japan Spacesystems and U.S./Japan ASTER Science Team",
-            "title": "ASTER Global Water Bodies Database V001",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/ASTWBDV001_N04E006.1.jpg?_ga=2.58926639.344140723.1565008229-1371303444.1563801461",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ASTER Global Water Bodies Database (ASTWBD) Version 1 data product provides global coverage of water bodies larger than 0.2 square kilometers at a spatial resolution of 1 arc second (approximately 30 meters) at the equator, along with associated elevation information. \r\n\r\nThe ASTWBD data product was created in conjunction with the ASTER Global Digital Elevation Model (ASTER GDEM) Version 3 data product by the Sensor Information Laboratory Corporation (SILC) in Tokyo. The ASTER GDEM Version 3 data product was generated using ASTER Level 1A (https://doi.org/10.5067/ASTER/AST_L1A.003) scenes acquired between March 1, 2000, and November 30, 2013. The ASTWBD data product was then generated to correct elevation values of water body surfaces.\r\n\r\nTo generate the ASTWBD data product, water bodies were separated from land areas and then classified into three categories: ocean, river, or lake. Oceans and lakes have a flattened, constant elevation value. The effects of sea ice were manually removed from areas classified as oceans to better delineate ocean shorelines in high latitude areas. For lake waterbodies, the elevation for each lake was calculated from the perimeter elevation data using the mosaic image that covers the entire area of the lake. Rivers presented a unique challenge given that their elevations gradually step down from upstream to downstream; therefore, visual inspection and other manual detection methods were required. \r\n\r\nThe geographic coverage of the ASTWBD extends from 83\u00b0N to 83\u00b0S. Each tile is distributed in GeoTIFF format and referenced to the 1984 World Geodetic System (WGS84)/1996 Earth Gravitational Model (EGM96) geoid. Each data product is provided as a zipped file that contains an attribute file with the water body classification information and a DEM file, which provides elevation information in meters.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FASTWBD.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASTER%2FASTWBD.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASTER/ASTWBD.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ASTER/ASTWBD.001",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1575734433-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1575734433-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ASTT/ASTWBD.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ASTT/ASTWBD.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/436/ASTWBD_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/436/ASTWBD_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/ASTWBDV001_N04E006.1.jpg?_ga=2.58926639.344140723.1565008229-1371303444.1563801461",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/ASTWBDV001_N04E006.1.jpg?_ga=2.58926639.344140723.1565008229-1371303444.1563801461",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov/WORKING/BRWS/Browse.001/2019.07.01/ASTWBDV001_N04E006.1.jpg?_ga=2.58926639.344140723.1565008229-1371303444.1563801461",
+            "identifier": "C1575734433-LPDAAC_ECS",
+            "issued": "2019-08-05",
+            "keyword": [
+                "surface water",
+                "earth science",
+                "topography",
+                "land surface",
+                "national geospatial data asset",
+                "ngda",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASTER/ASTWBD.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "ASTWBD.001",
             "spatial": "-180.0 -83.0 180.0 82.0",
+            "temporal": "2000-03-01T00:00:00Z/2013-11-30T23:59:59.999Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ASTER Global Water Bodies Database V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/K30XUYLP80I4",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Soil Moisture Active Passive (SMAP) L4 Carbon Ancillary Meteorology Preprocessor Output Log Files V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/K30XUYLP80I4.",
-            "issued": "2015-03-31",
-            "temporal": "2015-01-31T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-31",
-            "keyword": [
-                "ancillary models",
-                "earth science",
-                "models"
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
-            "identifier": "C1539057347-NSIDC_ECS",
             "description": "This ancillary SMAP product contains daily meteorological model log files, including model outputs. The meteorological model is derived from the Modern-Era Retrospective Analysis for Research and Applications (MERRA) data set and used as an input in the SMAP L4 Carbon algorithm.",
-            "title": "Soil Moisture Active Passive (SMAP) L4 Carbon Ancillary Meteorology Preprocessor Output Log Files V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FK30XUYLP80I4",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FK30XUYLP80I4",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_ANC/SMAP_L4_C_ANC_MET_LOG.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_ANC/SMAP_L4_C_ANC_MET_LOG.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SMAP_L4_C_ANC_MET_LOG+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SMAP_L4_C_ANC_MET_LOG+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/K30XUYLP80I4",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/K30XUYLP80I4",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/K30XUYLP80I4",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/K30XUYLP80I4",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1539057347-NSIDC_ECS",
+            "issued": "2015-03-31",
+            "keyword": [
+                "ancillary models",
+                "earth science",
+                "models"
+            ],
+            "landingPage": "https://doi.org/10.5067/K30XUYLP80I4",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -86.4 180.0 86.4",
+            "temporal": "2015-01-31T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Soil Moisture Active Passive (SMAP) L4 Carbon Ancillary Meteorology Preprocessor Output Log Files V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67PCHURYUMOV-M15-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission, covering the period from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67pchuryumov-m15-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC2-67PCHURYUMOV-M15-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc2-67pchuryumov-m15-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the COMET ESCORT 2 phase of the Rosetta mission, covering the period from 2015-04-08T11:25:00.000 to 2015-05-05T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP015 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC2-MTP015 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/RSX12-L2C20",
             "citation": "RapidScat Project. 2018-04-09. RapidScat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints. Version 2.0. Rapidscat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints Version 2.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/RSX12-L2C20. https://podaac.jpl.nasa.gov/ISS-RapidScat. RapidScat Project, PO.DAAC, 2018-04-09, RapidScat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints Version 2.0, https://podaac.jpl.nasa.gov/ISS-RapidScat.",
-            "issued": "2017-02-15",
-            "temporal": "2014-10-08T03:05:03Z/2016-08-19T15:01:26Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2012.2235843"
-            ],
-            "keyword": [
-                "ocean winds",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2036882499-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains the RapidScat Level 2B 12.5km Version 2.0 Climate quality ocean surface wind vectors. The Level 2B wind vectors are binned on a 12.5 km Wind Vector Cell (WVC) grid and processed using the using the \"full aperture\" normalized radar cross-section (NRCS, a.k.a. Sigma-0) from the L1B dataset. RapidScat is a Ku-band dual beam circular rotating scatterometer retaining much of the same hardware and functionality of QuikSCAT, with exception of the antenna sub-system and digital interface to the International Space Station (ISS) Columbus module, which is where RapidScat is mounted. The NASA mission is officially referred to as ISS-RapidScat. Unlike QuikSCAT, ISS-RapidScat is not in sun-synchronous orbit, and flies at roughly half the altitude with a low inclination angle that restricts data coverage to the tropics and mid-latitude regions; the extent of latitudinal coverage stretches from approximately 61 degrees North to 61 degrees South. Furthermore, there is no consistent local time of day retrieval. The new version has two important improvements over the previous version 1.0. First, an SST-dependent GMF developed by Lucrezia Ricciardulli of Remote Sensing Systems is used in wind retrieval in order to fix persistent speed biases in Ku-band data over cold ocean.  Second, flagging is simplified and extra flags are provided. All the previously existing flags are still there and still reflect the same meaning and purpose. A new single bit wind_retrieval_likely_corrupted_flag specifies the approximately 3% of the data which is known to have suboptimal performance due to rain, ice, or a few other rare anomalous cases. Another bit wind_retrieval_possibly_corrupted_flag specifies the approximately 15% of the data near rain, near ice, or near the coast, that is thought to be high quality but may not match up well with numerical wind models due to either remaining rain/ice/land contamination or variability in the winds near ice, rain, and coasts that are not reflected in the NWPs.  In addition to these two new bits, copious quality information is provided in the data to allow users to tailor flags to meet their own needs. There is also an added a global attribute called rev_status that specifies whether the RapidScat Instrument was in the original (highest data quality) high SNR mode, or one of the four low SNR time periods, the latter of which indicates the accuracy of winds below 5 m/s is degraded. This attribute also serves to identify MARGINAL orbits in which there are large gaps in the data record due to suboptimal spacecraft attitude. Other than gaps in the data, the accuracy of the winds in the MARGINAL orbits are similar to other orbits. This dataset is provided in netCDF-4 format and made available via FTP and OPeNDAP. For data access, please click on the \"Data Access\" tab above.",
-            "release-place": "PO.DAAC",
-            "series-name": "RapidScat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints",
             "creator": "RapidScat Project",
-            "title": "RapidScat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints Version 2.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_LEVEL_2B_OWV_CLIM_12_V2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the RapidScat Level 2B 12.5km Version 2.0 Climate quality ocean surface wind vectors. The Level 2B wind vectors are binned on a 12.5 km Wind Vector Cell (WVC) grid and processed using the using the \"full aperture\" normalized radar cross-section (NRCS, a.k.a. Sigma-0) from the L1B dataset. RapidScat is a Ku-band dual beam circular rotating scatterometer retaining much of the same hardware and functionality of QuikSCAT, with exception of the antenna sub-system and digital interface to the International Space Station (ISS) Columbus module, which is where RapidScat is mounted. The NASA mission is officially referred to as ISS-RapidScat. Unlike QuikSCAT, ISS-RapidScat is not in sun-synchronous orbit, and flies at roughly half the altitude with a low inclination angle that restricts data coverage to the tropics and mid-latitude regions; the extent of latitudinal coverage stretches from approximately 61 degrees North to 61 degrees South. Furthermore, there is no consistent local time of day retrieval. The new version has two important improvements over the previous version 1.0. First, an SST-dependent GMF developed by Lucrezia Ricciardulli of Remote Sensing Systems is used in wind retrieval in order to fix persistent speed biases in Ku-band data over cold ocean.  Second, flagging is simplified and extra flags are provided. All the previously existing flags are still there and still reflect the same meaning and purpose. A new single bit wind_retrieval_likely_corrupted_flag specifies the approximately 3% of the data which is known to have suboptimal performance due to rain, ice, or a few other rare anomalous cases. Another bit wind_retrieval_possibly_corrupted_flag specifies the approximately 15% of the data near rain, near ice, or near the coast, that is thought to be high quality but may not match up well with numerical wind models due to either remaining rain/ice/land contamination or variability in the winds near ice, rain, and coasts that are not reflected in the NWPs.  In addition to these two new bits, copious quality information is provided in the data to allow users to tailor flags to meet their own needs. There is also an added a global attribute called rev_status that specifies whether the RapidScat Instrument was in the original (highest data quality) high SNR mode, or one of the four low SNR time periods, the latter of which indicates the accuracy of winds below 5 m/s is degraded. This attribute also serves to identify MARGINAL orbits in which there are large gaps in the data record due to suboptimal spacecraft attitude. Other than gaps in the data, the accuracy of the winds in the MARGINAL orbits are similar to other orbits. This dataset is provided in netCDF-4 format and made available via FTP and OPeNDAP. For data access, please click on the \"Data Access\" tab above.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRSX12-L2C20",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRSX12-L2C20",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2B12/docs/rscat_l2b_user_guide_v2.pdf",
-                    "description": "User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/rapidscat/open/L2B12/docs/rscat_l2b_user_guide_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://manati.star.nesdis.noaa.gov/rscat_images/monitor/RapidScat_Scheduled_Outages.txt",
-                    "description": "Text file containing reverse chronological list of future scheduled outages and past outages. A start/stop date/time and description is provided for each outage. This list is maintained by NOAA/NESDIS to service near-real-time data users.",
                     "@type": "dcat:Distribution",
+                    "description": "Text file containing reverse chronological list of future scheduled outages and past outages. A start/stop date/time and description is provided for each outage. This list is maintained by NOAA/NESDIS to service near-real-time data users.",
+                    "downloadURL": "http://manati.star.nesdis.noaa.gov/rscat_images/monitor/RapidScat_Scheduled_Outages.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/rapidscat/ancillary/revtime.csv",
-                    "description": "ASCII CSV orbital revolution time tables with quality assurance information.",
                     "@type": "dcat:Distribution",
+                    "description": "ASCII CSV orbital revolution time tables with quality assurance information.",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/allData/rapidscat/ancillary/revtime.csv",
+                    "mediaType": "text/csv",
                     "title": "View this dataset's data quality document"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_LEVEL_2B_OWV_CLIM_12_V2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_LEVEL_2B_OWV_CLIM_12_V2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://directory.eoportal.org/web/eoportal/satellite-missions/i/iss-rapidscat",
-                    "description": "Detailed background information on the ISS-RapidScat mission published by the eoPortal.",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed background information on the ISS-RapidScat mission published by the eoPortal.",
+                    "downloadURL": "https://directory.eoportal.org/web/eoportal/satellite-missions/i/iss-rapidscat",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882499-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882499-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882499-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882499-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/RSCAT_LEVEL_2B_OWV_CLIM_12_V2.jpg",
+            "identifier": "C2036882499-POCLOUD",
+            "issued": "2017-02-15",
+            "keyword": [
+                "ocean winds",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/RSX12-L2C20",
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
+            "references": [
+                "https://doi.org/10.1109/TGRS.2012.2235843"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "RapidScat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints",
             "spatial": "-180.0 -61.0 180.0 61.0",
+            "temporal": "2014-10-08T03:05:03Z/2016-08-19T15:01:26Z",
             "theme": [
                 "ISS_RapidScat",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RapidScat Level 2B Climate Ocean Wind Vectors in 12.5km Footprints Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TEMPEST-STPH8-TSDR100",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Jet Propulsion Laboratory / COWVR Project Team. 2024-01-15. TEMPEST STPH8 L1 TSDR. Version 10.0. TEMPEST STP-H8 Antenna and Microwave Brightness Temperatures Version 10.0. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC, CA, USA. https://doi.org/10.5067/TEMPEST-STPH8-TSDR100.",
-            "issued": "2022-01-08",
-            "temporal": "2022-01-08T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-31",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "microwave"
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
-            "identifier": "C3237795822-POCLOUD",
-            "description": "This dataset includes satellite-based observations of calibrated, geo-located antenna temperature and brightness temperatures, along with the sensor telemetry used to derive those values. Brightness temperatures are derived from the microwave band frequencies 87, 164, 174, 178 and 181 GHz. This product is best suited for a cal/val user or sensor expert. These level 1c measurements make up the temperature sensor data record (TSDR) from the TEMPEST (Temporal Experiment for Storms and Tropical Systems) sensor aboard the international space station (ISS), starting in January 2022 forward-streaming to PO.DAAC till the planned mission end in December 2024. TEMPEST swath width is 1400 kilometers and resolution at nadir is 25 km for the 87 GHz channel and 13 km for the 180 GHz channels. Data files in HDF5 format are available at roughly hourly frequency (the ISS orbit period is ~90 minutes), although note that the coverage shown in the thumbnail is for a full day. Files include calibration and flag data in addition to brightness temperatures. Version 10.0 is the first public release, and is named as such to be consistent with the internal version numbering of the project team prior to release.\n<br><br>\nThe TEMPEST instrument is a microwave radiometer deployed as part of the Space Test Program - Houston 8 (STP-H8) technology demonstration mission, with the primary objective of tropical cyclone intensity tracking. It operates nominally on-orbit aboard the ISS and data are non-sun-synchronous. A successful mission will demonstrate a lower-cost, lighter-weight sensor architecture for providing microwave data. TEMPEST was provided by the Jet Propulsion Laboratory and flown by the United States Space Force, Space Systems Command, Development Corps for Innovation and Prototyping.",
-            "series-name": "TEMPEST STPH8 L1 TSDR",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Jet Propulsion Laboratory / COWVR Project Team",
-            "title": "TEMPEST STP-H8 Antenna and Microwave Brightness Temperatures Version 10.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TEMPEST_STPH8_L1_TSDR_V10.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset includes satellite-based observations of calibrated, geo-located antenna temperature and brightness temperatures, along with the sensor telemetry used to derive those values. Brightness temperatures are derived from the microwave band frequencies 87, 164, 174, 178 and 181 GHz. This product is best suited for a cal/val user or sensor expert. These level 1c measurements make up the temperature sensor data record (TSDR) from the TEMPEST (Temporal Experiment for Storms and Tropical Systems) sensor aboard the international space station (ISS), starting in January 2022 forward-streaming to PO.DAAC till the planned mission end in December 2024. TEMPEST swath width is 1400 kilometers and resolution at nadir is 25 km for the 87 GHz channel and 13 km for the 180 GHz channels. Data files in HDF5 format are available at roughly hourly frequency (the ISS orbit period is ~90 minutes), although note that the coverage shown in the thumbnail is for a full day. Files include calibration and flag data in addition to brightness temperatures. Version 10.0 is the first public release, and is named as such to be consistent with the internal version numbering of the project team prior to release.\n<br><br>\nThe TEMPEST instrument is a microwave radiometer deployed as part of the Space Test Program - Houston 8 (STP-H8) technology demonstration mission, with the primary objective of tropical cyclone intensity tracking. It operates nominally on-orbit aboard the ISS and data are non-sun-synchronous. A successful mission will demonstrate a lower-cost, lighter-weight sensor architecture for providing microwave data. TEMPEST was provided by the Jet Propulsion Laboratory and flown by the United States Space Force, Space Systems Command, Development Corps for Innovation and Prototyping.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEMPEST-STPH8-TSDR100",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEMPEST-STPH8-TSDR100",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3237795822-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3237795822-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3237795822-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3237795822-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/COWVR-TEMPEST",
-                    "description": "COWVR-TEMPEST project page at PO.DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "COWVR-TEMPEST project page at PO.DAAC",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/COWVR-TEMPEST",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cowvr-tempest/open/docs/DPDD_TEMPEST_STPH8_L1_TSDR_V10.0.pdf",
-                    "description": "Data Product Development Document providing an overview of the project, instrument, and data product contents",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Development Document providing an overview of the project, instrument, and data product contents",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cowvr-tempest/open/docs/DPDD_TEMPEST_STPH8_L1_TSDR_V10.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TEMPEST_STPH8_L1_TSDR_V10.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TEMPEST_STPH8_L1_TSDR_V10.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/COWVR-TEMPEST",
-                    "description": "COWVR-TEMPEST project page at PO.DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "COWVR-TEMPEST project page at PO.DAAC",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/COWVR-TEMPEST",
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
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TEMPEST_STPH8_L1_TSDR_V10.0.jpg",
+            "identifier": "C3237795822-POCLOUD",
+            "issued": "2022-01-08",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/TEMPEST-STPH8-TSDR100",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "series-name": "TEMPEST STPH8 L1 TSDR",
             "spatial": "-180.0 -61.0 180.0 61.0",
+            "temporal": "2022-01-08T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "COWVR-TEMPEST/STP-H8",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TEMPEST STP-H8 Antenna and Microwave Brightness Temperatures Version 10.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1157-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-05T08:23:00.000 to 2015-11-05T13:00:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1157-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1157-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1157-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-05T08:23:00.000 to 2015-11-05T13:00:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1157 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1157 V1.0"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0052-8-s3os2-v1.0_irps-4v2n",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "746 marlu",
                 "1000 piazzia",
@@ -934809,1041 +934811,1009 @@
                 "asteroid 9219",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0052-8-S3OS2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0052-8-s3os2-v1.0_irps-4v2n",
-            "description": "This dataset contains the visible spectra of 820 asteroids obtained between November 1996 and May 2001 at the 1.52m telescope at ESO (La Silla). The useful spectral range is between about 4900 and 9200 Angstroms. The global spatial distribution of the objects covers the region between 2.2 and 3.3 AU. Some concentrations are apparent, since part of the survey was focused on particuarly interesting groups or families of asteroids. The observed asteroids have been classified according to the Tholen and the Bus taxonomies, with a good agreement between both in most of the cases.",
-            "title": "SMALL SOLAR SYSTEM OBJECTS SPECTROSCOPIC SURVEY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SMALL SOLAR SYSTEM OBJECTS SPECTROSCOPIC SURVEY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-2-EDR-WILD2-V3.0",
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
-                "81p/wild 2 (1978 a2)",
-                "stardust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains EDR (raw) pre-encounter and encounter images taken by the Stardust Navigation Camera of comet 81P/Wild 2 (1978 A2). This is a new version of a subset of an existing data set, based on work done during the Stardust-NExT mission. The updated calibration from the Stardust-NExT mission was applied to these data in a separate data set (similar name:  Level 3; RDR). Changes in the calibration of the NAVCAM instrument, between these prime mission data and those of the Stardust-NExT mission, are a possibility and are addressed in [KLAASENETAL2011B].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-2-edr-wild2-v3.0_irpz-xthh",
+            "issued": "2018-06-26",
+            "keyword": [
+                "81p/wild 2 (1978 a2)",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-2-EDR-WILD2-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-2-edr-wild2-v3.0_irpz-xthh",
-            "description": "This data set contains EDR (raw) pre-encounter and encounter images taken by the Stardust Navigation Camera of comet 81P/Wild 2 (1978 A2). This is a new version of a subset of an existing data set, based on work done during the Stardust-NExT mission. The updated calibration from the Stardust-NExT mission was applied to these data in a separate data set (similar name:  Level 3; RDR). Changes in the calibration of the NAVCAM instrument, between these prime mission data and those of the Stardust-NExT mission, are a possibility and are addressed in [KLAASENETAL2011B].",
-            "title": "STARDUST NAVCAM RAW IMAGES OF WILD 2 - VERSION 3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "STARDUST NAVCAM RAW IMAGES OF WILD 2 - VERSION 3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSIONOFLUXTEC_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSIONOFLUXTEC_001.",
-            "issued": "2014-01-01",
-            "temporal": "2014-01-01T00:00:00Z/2024-01-29T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-31",
-            "keyword": [
-                "tectonics",
-                "earth science",
-                "geodetics",
-                "solid earth",
-                "gravity/gravitational field"
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
-            "identifier": "C1511776721-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System a Ionosphere Vertical Total Electron Content (VTEC) fluctuation measurement product (daily files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. GNSS observations from a global network can be utilized for atmospheric measurements. Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce independently computed VTEC maps. These fluctuations in TEC consists of a rate of TEC change index (ROTI) maps which are constructed with the grid of 2 degrees by 2 degrees resolution as a function of the magnetic local time and corrected magnetic latitude. GNSS data are used to determine ROTI maps, the standard deviation of rate of TEC change over a specified time span; ROTI can be used to describe irregularities in the ionosphere.",
-            "title": "Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Fluctuation Measurement Product from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSIONOFLUXTEC_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSIONOFLUXTEC_001",
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
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSIONOFLUXTEC_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSIONOFLUXTEC_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1511776721-CDDIS",
+            "issued": "2014-01-01",
+            "keyword": [
+                "tectonics",
+                "earth science",
+                "geodetics",
+                "solid earth",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSIONOFLUXTEC_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-01-01T00:00:00Z/2024-01-29T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) Ionosphere Vertical Total Electron Content (VTEC) Fluctuation Measurement Product from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/852",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "TRFIC (Tropical Rain Forest Info Cntr, MI St Univ). 2007. LBA-ECO LC-10 Landsat TM Data for Legal Amazon: 1986-1994. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/852",
-            "issued": "2023-10-03",
-            "temporal": "1986-09-21T00:00:00Z/1994-09-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "land use/land cover",
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
-            "identifier": "C2777339420-ORNL_CLOUD",
             "description": "This data set includes Landsat TM scenes from across the Legal Amazon region.  A single image is provided for each spatial tile, representing the most cloud-free retrieval from 9/21/86 to 9/17/94.  All files are in a single directory, including one band-sequential (bsq) file and one database (ddr) file for each scene.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-10 Landsat TM Data for Legal Amazon: 1986-1994",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F852",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F852",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC10_Landsat_TM/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC10_Landsat_TM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC10_Landsat_TM.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC10_Landsat_TM.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/852",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/852",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC10_Landsat_TM/comp/LC10_Landsat_TM.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC10_Landsat_TM/comp/LC10_Landsat_TM.pdf",
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
+            "identifier": "C2777339420-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "land use/land cover",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/852",
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
             "spatial": "-75.18 -19.68 -42.59 5.23",
+            "temporal": "1986-09-21T00:00:00Z/1994-09-17T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-10 Landsat TM Data for Legal Amazon: 1986-1994"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0857-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-25T21:03:45.000 to 2015-06-26T00:23:01.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0857-v1.0_irtf-zcr4",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0857-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0857-v1.0_irtf-zcr4",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-25T21:03:45.000 to 2015-06-26T00:23:01.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0857 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0857 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECTSD-MSL44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Global Mean Sea Level - Daily Mean (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECTSD-MSL44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Global Mean Sea Level - Daily Mean (Version 4 Release 4); 10.5067/ECTSD-MSL44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-01",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "climate indicators",
-                "atmospheric/ocean indicators",
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
-            "identifier": "C1991543819-POCLOUD",
-            "description": "This dataset provides daily-averaged global mean sea level from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Global Mean Sea Level - Daily Mean (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMSL_TIME_SERIES_DAILY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides daily-averaged global mean sea level from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height and model sea level anomaly (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSD-MSL44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECTSD-MSL44",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMSL_TIME_SERIES_DAILY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMSL_TIME_SERIES_DAILY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECTSD-MSL44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECTSD-MSL44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543819-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543819-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543819-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543819-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_GMSL_TIME_SERIES_DAILY_V4R4.jpg",
+            "identifier": "C1991543819-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "climate indicators",
+                "atmospheric/ocean indicators",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECTSD-MSL44",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-01-01",
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
+            "title": "ECCO Global Mean Sea Level - Daily Mean (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/SMP10-4U7CS",
             "citation": "Oleg Melnichenko. 2021-06-30. Multi-mission Optimally Interpoated Sea Surface Salinity Products. Version 1.0. Multi-mission L4 Optimally Interpoated Sea Surface Salinity. IPRC/SOEST University of Hawaii, Manoa. Archived by National Aeronautics and Space Administration, U.S. Government, PODAAC. https://doi.org/10.5067/SMP10-4U7CS. http://apdrc.soest.hawaii.edu/datadoc/oisss.php. Oleg Melnichenko, PODAAC, 2021-06-30, Multi-Mission Optimally Interpolated Sea Surface Salinity Global Dataset V1, http://apdrc.soest.hawaii.edu/datadoc/oisss.php.",
-            "issued": "2021-06-07",
-            "temporal": "2011-08-24T12:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-07",
-            "references": [
-                "https://doi.org/doi:10.1002/2015JC011343"
-            ],
-            "keyword": [
-                "earth science",
-                "salinity/density",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "identifier": "C2095055342-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This is a level 4 product on a 0.25-degree spatial and 4-day temporal grid. The product is derived from the level 2 swath data of three satellite missions: the Aquarius/SAC-D, Soil Moisture Active Passive (SMAP) and Soil Moisture and Ocean Salinity (SMOS) using Optimal Interpolation (OI) with a 7-day decorrelation time scale. The product offers a continuous record from August 28, 2011 to present by concatenating the measurements from Aquarius (September 2011 - June 2015) and SMAP (April 2015  present). ESAs SMOS data was used to fill the gap in SMAP data between June and July 2019, when the SMAP satellite was in a safe mode. The two-month overlap (April - June 2015) between Aquarius and SMAP was used to ensure consistency and continuity in data record. The product covers the global ocean, including the Arctic and Antarctic in the areas free of sea ice, but does not cover internal seas such as Mediterranean and Baltic Sea. In-situ salinity from Argo floats and moored buoys are used to derive a large-scale bias correction and to ensure consistency and accuracy of the OISSS dataset. This dataset is produced by the International Pacific Research Center (IPRC) of the University of Hawaii at Manoa in collaboration with the Remote Sensing Systems (RSS), Santa Rosa, California. More details can be found in the users guide.",
-            "release-place": "IPRC/SOEST University of Hawaii, Manoa",
-            "series-name": "Multi-mission Optimally Interpoated Sea Surface Salinity Products",
             "creator": "Oleg Melnichenko",
-            "title": "Multi-Mission Optimally Interpolated Sea Surface Salinity Global Dataset V1",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISSS_L4_multimission_7day_v1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This is a level 4 product on a 0.25-degree spatial and 4-day temporal grid. The product is derived from the level 2 swath data of three satellite missions: the Aquarius/SAC-D, Soil Moisture Active Passive (SMAP) and Soil Moisture and Ocean Salinity (SMOS) using Optimal Interpolation (OI) with a 7-day decorrelation time scale. The product offers a continuous record from August 28, 2011 to present by concatenating the measurements from Aquarius (September 2011 - June 2015) and SMAP (April 2015  present). ESAs SMOS data was used to fill the gap in SMAP data between June and July 2019, when the SMAP satellite was in a safe mode. The two-month overlap (April - June 2015) between Aquarius and SMAP was used to ensure consistency and continuity in data record. The product covers the global ocean, including the Arctic and Antarctic in the areas free of sea ice, but does not cover internal seas such as Mediterranean and Baltic Sea. In-situ salinity from Argo floats and moored buoys are used to derive a large-scale bias correction and to ensure consistency and accuracy of the OISSS dataset. This dataset is produced by the International Pacific Research Center (IPRC) of the University of Hawaii at Manoa in collaboration with the Remote Sensing Systems (RSS), Santa Rosa, California. More details can be found in the users guide.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP10-4U7CS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP10-4U7CS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISSS_L4_multimission_7day_v1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISSS_L4_multimission_7day_v1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earth.esa.int/eogateway/missions/smos",
-                    "description": "SMOS Mission Website",
                     "@type": "dcat:Distribution",
+                    "description": "SMOS Mission Website",
+                    "downloadURL": "https://earth.esa.int/eogateway/missions/smos",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://smap.jpl.nasa.gov/",
-                    "description": "NASA SMAP Mission Website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SMAP Mission Website",
+                    "downloadURL": "http://smap.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/OISSS_V1/L4OISSS_MultimissionProductGuide_V1.pdf",
-                    "description": "IPRC/SOEST L4 OISSS Product Guide",
                     "@type": "dcat:Distribution",
+                    "description": "IPRC/SOEST L4 OISSS Product Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/OISSS_V1/L4OISSS_MultimissionProductGuide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/aquarius",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/aquarius",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://aquarius.nasa.gov/",
-                    "description": "NASA Aquarius/SAC-D mission website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Aquarius/SAC-D mission website",
+                    "downloadURL": "http://aquarius.nasa.gov/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2095055342-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2095055342-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2095055342-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2095055342-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISSS_L4_multimission_7day_v1.jpg",
+            "identifier": "C2095055342-POCLOUD",
+            "issued": "2021-06-07",
+            "keyword": [
+                "earth science",
+                "salinity/density",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMP10-4U7CS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-06-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/doi:10.1002/2015JC011343"
+            ],
+            "release-place": "IPRC/SOEST University of Hawaii, Manoa",
+            "series-name": "Multi-mission Optimally Interpoated Sea Surface Salinity Products",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-24T12:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "SMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Multi-Mission Optimally Interpolated Sea Surface Salinity Global Dataset V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-2-PLUTO-V2.0",
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
-                "dust",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains SDC observations taken during the                 the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-2-pluto-v2.0_irw4-9qev",
+            "issued": "2018-09-05",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-2-PLUTO-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-2-pluto-v2.0_irw4-9qev",
-            "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains SDC observations taken during the                 the Approach (Jan-Jul, 2015), Encounter and Departure mission            sub-phases, including flyby observations taken on 14.July, 2015,         and including data through 2015 and into January, 2016; the data are     limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.                            This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  Also, updates were made to the documentation and         catalog files, primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1644",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "dos-Santos, M.N., M.M. Keller, and D.C. Morton. 2019. LiDAR Surveys over Selected Forest Research Sites, Brazilian Amazon, 2008-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1644",
-            "issued": "2024-05-17",
-            "temporal": "2008-01-01T00:00:00Z/2018-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-22",
-            "keyword": [
-                "topography",
-                "vegetation",
-                "earth science",
-                "spectral/engineering",
-                "lidar",
-                "land surface",
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
-            "identifier": "C2398128915-ORNL_CLOUD",
             "description": "This dataset provides the complete catalog of point cloud data collected during LiDAR surveys over selected forest research sites across the Amazon rainforest in Brazil between 2008 and 2018 for the Sustainable Landscapes Brazil Project. Flight lines were selected to overfly key field research sites in the Brazilian states of Acre, Amazonas, Bahia, Goias, Mato Grosso, Para, Rondonia, Santa Catarina, and Sao Paulo. The point clouds have been georeferenced, noise-filtered, and corrected for misalignment of overlapping flight lines. They are provided in 1 km2 tiles. The data were collected to measure forest canopy structure across Amazonian landscapes to monitor the effects of selective logging on forest biomass and carbon balance, and forest recovery over time.",
-            "graphic-preview-description": "Bounding boxes for LiDAR tiles from surveys over western Para, Brazil are depicted in Google Earth from the KMZ file. Each feature in the KMZ provides key metadata about the corresponding tile. Source: cms_brazil_lidar_tile_inventory.kmz",
-            "title": "LiDAR Surveys over Selected Forest Research Sites, Brazilian Amazon, 2008-2018",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/LiDAR_Forest_Inventory_Brazil_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1644",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1644",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/LiDAR_Forest_Inventory_Brazil/data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/cms/LiDAR_Forest_Inventory_Brazil/data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/LiDAR_Forest_Inventory_Brazil.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/LiDAR_Forest_Inventory_Brazil.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1644",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1644",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/LiDAR_Forest_Inventory_Brazil/comp/LiDAR_Forest_Inventory_Brazil.pdf",
-                    "description": "LiDAR Surveys over Selected Forest Research Sites, Brazilian Amazon, 2008-2018: LiDAR_Forest_Inventory_Brazil.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "LiDAR Surveys over Selected Forest Research Sites, Brazilian Amazon, 2008-2018: LiDAR_Forest_Inventory_Brazil.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/LiDAR_Forest_Inventory_Brazil/comp/LiDAR_Forest_Inventory_Brazil.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/LiDAR_Forest_Inventory_Brazil_Fig1.jpg",
-                    "description": "Bounding boxes for LiDAR tiles from surveys over western Para, Brazil are depicted in Google Earth from the KMZ file. Each feature in the KMZ provides key metadata about the corresponding tile. Source: cms_brazil_lidar_tile_inventory.kmz",
                     "@type": "dcat:Distribution",
+                    "description": "Bounding boxes for LiDAR tiles from surveys over western Para, Brazil are depicted in Google Earth from the KMZ file. Each feature in the KMZ provides key metadata about the corresponding tile. Source: cms_brazil_lidar_tile_inventory.kmz",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/LiDAR_Forest_Inventory_Brazil_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Bounding boxes for LiDAR tiles from surveys over western Para, Brazil are depicted in Google Earth from the KMZ file. Each feature in the KMZ provides key metadata about the corresponding tile. Source: cms_brazil_lidar_tile_inventory.kmz",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/LiDAR_Forest_Inventory_Brazil_Fig1.jpg",
+            "identifier": "C2398128915-ORNL_CLOUD",
+            "issued": "2024-05-17",
+            "keyword": [
+                "topography",
+                "vegetation",
+                "earth science",
+                "spectral/engineering",
+                "lidar",
+                "land surface",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1644",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-68.3 -26.7 -39.06 -1.58",
+            "temporal": "2008-01-01T00:00:00Z/2018-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LiDAR Surveys over Selected Forest Research Sites, Brazilian Amazon, 2008-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-PRL-MTP009-V1.0",
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
+            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 9 period of the PRELANDING mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-prl-mtp009-v1.0_is24-nqii",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-SREM-5-PRL-MTP009-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-srem-5-prl-mtp009-v1.0_is24-nqii",
-            "description": "This data set contains derived electron and proton flux energies in MeV from the Standard Radiation Environment Monitor (SREM) instrument on the Rosetta spacecraft, which had the primary target of comet 67P/Churyumov-Gerasimenko. These are CODMAC Level 5 derived data, and measure the radiation in the spacecraft environment during the Medium Term Plan 9 period of the PRELANDING mission phase.",
-            "title": "ROSETTA-ORBITER 67P SREM 5 PRELANDING\n    MTP009 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P SREM 5 PRELANDING\n    MTP009 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-D-GDDS-5-DUST-V3.0",
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
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Detector responses and derived quantities from the Galileo dust detector as well as spacecraft geometry information for reliable impacts from launch through 2001. See Gruen et al. (Plan. Sp. Sci. 43, 953-969, 1995) and Krueger et al. (Plan. Sp. Sci. 47, 85-106, 1999; Plan. Sp. Sci. 49, 1285-1301, 2001) for more information.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-d-gdds-5-dust-v3.0_is4a-pdjc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dust",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-D-GDDS-5-DUST-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-d-gdds-5-dust-v3.0_is4a-pdjc",
-            "description": "Detector responses and derived quantities from the Galileo dust detector as well as spacecraft geometry information for reliable impacts from launch through 2001. See Gruen et al. (Plan. Sp. Sci. 43, 953-969, 1995) and Krueger et al. (Plan. Sp. Sci. 47, 85-106, 1999; Plan. Sp. Sci. 49, 1285-1301, 2001) for more information.",
-            "title": "GALILEO DUST DETECTION SYSTEM V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO DUST DETECTION SYSTEM V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1097",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "de Araujo, A.C., J.P.H.B. Ometto, A.J. Dolman, B. Kruijt, M.J. Waterloo, and J.R. Ehleringer. 2012. LBA-ECO CD-02 C and N Isotopes in Leaves and Atmospheric CO2, Amazonas, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1097",
-            "issued": "2023-10-03",
-            "temporal": "2004-08-02T00:00:00Z/2006-10-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
-            "keyword": [
-                "biosphere",
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C2780153068-ORNL_CLOUD",
             "description": "This data set reports delta 13C/12C results for leaf tissues and atmospheric carbon dioxide (CO2), delta 15N/14N ratios for leaf tissue, and leaf carbon and nitrogen concentrations along a topographical gradient in old-growth forests in the ZF2 Reserve (km 34), Instituto Nacional de Pesquisas da Amazonia (INPA), near Manaus, Amazonas, Brazil. During the dry seasons of 2004 and 2006, leaves were sampled at various heights within the canopy and atmospheric air flask samples were also collected at various heights at three locations along this gradient. Also included are coincident meteorological, atmospheric CO2, and CO2 flux measurements from the plateau KM34 tower. There are 3 comma-delimited data files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-02 C and N Isotopes in Leaves and Atmospheric CO2, Amazonas, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1097",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1097",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD02_C_N_Isotopes/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD02_C_N_Isotopes/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD02_C_N_Isotopes.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD02_C_N_Isotopes.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1097",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1097",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD02_C_N_Isotopes/comp/CDO2_C_N_Isotopes.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD02_C_N_Isotopes/comp/CDO2_C_N_Isotopes.pdf",
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
+            "identifier": "C2780153068-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1097",
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
             "spatial": "-60.21 -2.61 -60.0 -2.5",
+            "temporal": "2004-08-02T00:00:00Z/2006-10-21T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-02 C and N Isotopes in Leaves and Atmospheric CO2, Amazonas, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/728",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Swap, R.J., S.J. Piketh, K.E. Ross, M. Barenbrug, and K.A. Billmark. 2004. SAFARI 2000 Upper Air Meteorological Profiles, Skukuza, Dry Seasons 1999-2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/728",
-            "issued": "2023-10-18",
-            "temporal": "1999-08-14T00:00:00Z/2000-09-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric temperature",
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
-            "identifier": "C2789020292-ORNL_CLOUD",
             "description": "Vaisala RS80 sondes were deployed from Skukuza Airport, South Africa, to collect atmospheric sounding profiles of temperature and moisture data from the surface to 30 km. These sonde launches were coordinated to augment the regional sounding network in the region during the SAFARI 2000 Dry Season Campaigns of 1999 and 2000. The radiosondes were launched from Skukuza Airport between August 14-September 3, 1999, and between August 24-September 23, 2000.  The radiosonde instrument package RS80 measured the following meteorological parameters: pressure in hecto-Pascals (P), ambient temperature in degrees Celsius (T), and relative humidity in percentage (RH). A hydrostatic equation was applied to the recorded data, after error-checking, to calculate the output parameters: height above sea level in meters, dew point temperature in degrees Celsius, and q (g/kg) which is specific humidity in grams per kilogram.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Upper Air Meteorological Profiles, Skukuza, Dry Seasons 1999-2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F728",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F728",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/met_profile_skukuza/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/atmospheric/met_profile_skukuza/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/met_profile_skukuza.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/met_profile_skukuza.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/728",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/728",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/met_profile_skukuza/comp/met_profile_skukuza_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/atmospheric/met_profile_skukuza/comp/met_profile_skukuza_readme.pdf",
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
+            "identifier": "C2789020292-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/728",
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
             "spatial": "-24.97 31.59",
+            "temporal": "1999-08-14T00:00:00Z/2000-09-23T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Upper Air Meteorological Profiles, Skukuza, Dry Seasons 1999-2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR7-V1.0",
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
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 28, 30, March 25, 26 2007 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr7-v1.0_isaz-h2ma",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "titan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR7-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr7-v1.0_isaz-h2ma",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR7) Raw Data Archive is a time-ordered collection of radio science raw data acquired on January 28, 30, March 25, 26 2007 during the Tour subphase of the Cassini mission. DATA_SET_DESC =",
-            "title": "CASSINI RSS RAW DATA SET - TIGR7 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TIGR7 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F15/1C/07",
             "citation": "Wesley Berg. 2021-07-29. GPM_1CF15SSMI. GPM SSMI on F15 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/SSMI/F15/1C/07. https://disc.gsfc.nasa.gov/datacollection/GPM_1CF15SSMI_07.html. Digital Science Data.",
-            "issued": "2021-07-21",
-            "temporal": "2000-02-23T00:00:00Z/2006-08-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-21",
-            "references": [
-                "https://doi.org/10.1175/JTECH-D-16-0100.1",
-                "https://doi.org/10.3390/rs10081306"
-            ],
-            "keyword": [
-                "precipitation",
-                "microwave",
-                "earth science",
-                "atmospheric water vapor",
-                "atmosphere",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WESLEY BERG",
                 "hasEmail": "mailto:berg@atmos.colostate.edu"
             },
+            "creator": "Wesley Berg",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264132856-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "All 1C products have a common L1C data structure, simple and generic. Each L1C swath includes scan time, latitude and longitude, scan status, quality, incidence angle, Sun glint angle, and the intercalibrated brightness temperature (Tc). One or more swaths are included in a product. The radiometer data are recalibrated to a common basis so that precipitation products derived from them are consistent. 1CSSMIS contains common calibrated brightness temperature from the SSMIS passive microwave instruments flown on the DMSP satellites. Swath S1 has 3 low frequency channels (19V 19H 22V). Swath S2 has 2 low frequency channels (37V 37H). Swath S3 has 4 high frequency channels (150H 183+/-1H 183+/-3H 183+/-7H). S4 has 2 high frequency channels (91V 91H). All the above frequencies are in GHz. Earth observations for all four swaths are taken during a 144o segment of the instrument rotation when SSMIS scans in the direction of foreward satellite motion. We define the spacecraft vector (v) at the center of this segment.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "GPM_1CF15SSMI",
-            "creator": "Wesley Berg",
-            "graphic-preview-description": "Common Calibrated Brightness Temperature from F15 SSMI",
-            "title": "GPM SSMI on F15 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF15SSMI) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CF15SSMI.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF15%2F1C%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FSSMI%2FF15%2F1C%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CF15SSMI.png",
-                    "description": "Common Calibrated Brightness Temperature from F15 SSMI",
                     "@type": "dcat:Distribution",
+                    "description": "Common Calibrated Brightness Temperature from F15 SSMI",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CF15SSMI.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CF15SSMI_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_1CF15SSMI_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CF15SSMI.07/",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L1C/GPM_1CF15SSMI.07/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CF15SSMI_07",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_1CF15SSMI_07",
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
@@ -935853,153 +935823,164 @@
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
+            "graphic-preview-description": "Common Calibrated Brightness Temperature from F15 SSMI",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_1CF15SSMI.png",
+            "identifier": "C2264132856-GES_DISC",
+            "issued": "2021-07-21",
+            "keyword": [
+                "precipitation",
+                "microwave",
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/SSMI/F15/1C/07",
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
+            "series-name": "GPM_1CF15SSMI",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-23T00:00:00Z/2006-08-14T23:59:59.999Z",
             "theme": [
                 "GPM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM SSMI on F15 Common Calibrated Brightness Temperatures L1C 1.5 hours 13 km V07 (GPM_1CF15SSMI) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-NAVCAM-2-PRL-COM-V1.1",
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
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Prelanding Phase from 21 Jan 2014 until 30 April 2014 before reaching target 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, adding of the FITS version, clarification of calibration target, document updates and resolve other minor outstanding errata.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-navcam-2-prl-com-v1.1",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-NAVCAM-2-PRL-COM-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-navcam-2-prl-com-v1.1",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Prelanding Phase from 21 Jan 2014 until 30 April 2014 before reaching target 67P/CG. This data set V1.1 supersedes the V1.0. It includes updates of the Browse images, adding of the FITS version, clarification of calibration target, document updates and resolve other minor outstanding errata.",
-            "title": "ROSETTA-ORBITER CHECK NAVCAM 2 PRELANDING COMMISSIONING V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK NAVCAM 2 PRELANDING COMMISSIONING V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-L-TLP-3-CAL-V1.0",
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
-                "lunar crater observation and sensing satellite"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Calibrated data from the Total Luminance Photometer (TLP) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-l-tlp-3-cal-v1.0_isc3-qran",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "lunar crater observation and sensing satellite"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-L-TLP-3-CAL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-l-tlp-3-cal-v1.0_isc3-qran",
-            "description": "Calibrated data from the Total Luminance Photometer (TLP) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS MOON TOTAL LUMINANCE PHOTOMETER 3 CAL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LCROSS MOON TOTAL LUMINANCE PHOTOMETER 3 CAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.doi.org/10.5067/SLR/slr_report_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://www.doi.org/10.5067/SLR/slr_report_001.",
-            "issued": "1983-01-01",
-            "temporal": "1983-01-01T00:00:00Z/2021-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-31",
-            "keyword": [
-                "solid earth",
-                "geodetics",
-                "earth science"
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
-            "identifier": "C2910215423-CDDIS",
             "description": "SLReport is a mail exploder to distribute regular mission related reports (e.g., campaign status reports, weekly LAGEOS reports, etc.).  Each individual message is automatically numbered sequentially and archived for reference.",
-            "title": "Satellite Laser Ranging Report exploder distributing mission related reports, each message automatically numbered sequentially and archived for reference.",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=https%3A%2F%2Fwww.doi.org%2F10.5067%2FSLR%2Fslr_report_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=https%3A%2F%2Fwww.doi.org%2F10.5067%2FSLR%2Fslr_report_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -936009,1213 +935990,1205 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2910215423-CDDIS",
+            "issued": "1983-01-01",
+            "keyword": [
+                "solid earth",
+                "geodetics",
+                "earth science"
+            ],
+            "landingPage": "https://www.doi.org/10.5067/SLR/slr_report_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1983-01-01T00:00:00Z/2021-12-31T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Satellite Laser Ranging Report exploder distributing mission related reports, each message automatically numbered sequentially and archived for reference."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1427",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CARVE Science Team . 2017. CARVE: L1 Daily Flight Path and Winds Data, Alaska, 2015. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1427",
-            "issued": "2017-02-24",
-            "temporal": "2015-04-15T18:14:57Z/2015-11-13T01:12:44Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "atmospheric winds",
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
-            "identifier": "C2236316359-ORNL_CLOUD",
             "description": "This data set provides high-frequency wind speed and direction data for the C-23 Sherpa aircraft during airborne campaigns over the Alaskan and Canadian Arctic as part of the Carbon in Arctic Reservoirs Vulnerability Experiment (CARVE). The data were collected in situ using the Aventech AIMMS-30 Airborne Wind Sensor onboard the aircraft and are presented at 1-second intervals throughout each flight. The Winds instrument was available for flights in year 2015 only. The measurements included in this data set are most useful when paired with the scientific data collected by other CARVE airborne instruments.",
-            "graphic-preview-description": "Browse Image",
-            "title": "CARVE: L1 Daily Flight Path and Winds Data, Alaska, 2015",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1427_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1427",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1427",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/carve/campaign/CARVE_L1_FlightPath_Winds/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/carve/campaign/CARVE_L1_FlightPath_Winds/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_FlightPath_Winds.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CARVE/guides/CARVE_L1_FlightPath_Winds.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1427",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1427",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L1_FlightPath_Winds/comp/CARVE_L1_FlightPath_Winds.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/carve/campaign/CARVE_L1_FlightPath_Winds/comp/CARVE_L1_FlightPath_Winds.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1427_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1427_1_fit.png",
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
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1427/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1427/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1427_1_fit.png",
+            "identifier": "C2236316359-ORNL_CLOUD",
+            "issued": "2017-02-24",
+            "keyword": [
+                "atmospheric winds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1427",
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
             "spatial": "-168.07 58.84 -132.24 71.32",
+            "temporal": "2015-04-15T18:14:57Z/2015-11-13T01:12:44Z",
             "theme": [
                 "CARVE",
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CARVE: L1 Daily Flight Path and Winds Data, Alaska, 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/CPB005XLAIIG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX08 Land Cover Classification Map V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/CPB005XLAIIG.",
-            "issued": "2008-06-01",
-            "temporal": "2008-06-01T00:00:00Z/2008-10-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2008-10-01",
-            "keyword": [
-                "land use/land cover",
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
-            "identifier": "C1000001402-NSIDC_ECS",
             "description": "This data set consists of land cover classification data derived from satellite imagery and of data obtained in the field as part of the Soil Moisture Active Passive Validation Experiment 2008 (SMAPVEX08).",
-            "title": "SMAPVEX08 Land Cover Classification Map V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPB005XLAIIG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCPB005XLAIIG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV08LC.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV08LC.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001402-NSIDC_ECS&m=30.26953125%21-79.224609375%214%211%210%210%2C2&q=SMAPVEX08&ok=SMAPVEX08",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001402-NSIDC_ECS&m=30.26953125%21-79.224609375%214%211%210%210%2C2&q=SMAPVEX08&ok=SMAPVEX08",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV08LC/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV08LC/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CPB005XLAIIG",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/CPB005XLAIIG",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/CPB005XLAIIG",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/CPB005XLAIIG",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001402-NSIDC_ECS",
+            "issued": "2008-06-01",
+            "keyword": [
+                "land use/land cover",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CPB005XLAIIG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2008-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-76.3 38.8 -75.6 39.1",
+            "temporal": "2008-06-01T00:00:00Z/2008-10-31T23:59:59.999Z",
             "theme": [
                 "SMAPVEX08",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX08 Land Cover Classification Map V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/TPS/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A, Patrick N Gatlin and Matthew T. Wingo.2013. GPM GROUND VALIDATION TOTAL PRECIPITATION SENSOR (HOTPLATE) GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/TPS/DATA201",
-            "issued": "2013-11-12",
-            "temporal": "2011-11-07T00:00:00Z/2012-02-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-10",
-            "keyword": [
-                "earth science",
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "precipitation",
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
-            "identifier": "C1979827156-GHRC_DAAC",
             "description": "The GPM Ground Validation Total Precipitation Sensor (HotPlate) GCPEx dataset provides a measure of the liquid precipitation rate and accumulation for snow. Additional data includes measurements of temperature, wind speed, relative humidity, pressure, and solar and infrared radiation flux. These data were gathered during the GPM Cold-season Precipitation Experiment (GCPEx) at the CARE and SkyDive sites in Ontario, Canada during November 7, 2011 - February 21, 2012. These data sets were collected to aid in the achievement of the over arching goal of GCPEx which is to characterize the ability of multi-frequency active and passive microwave sensors to detect and estimate falling snow.",
-            "title": "GPM GROUND VALIDATION TOTAL PRECIPITATION SENSOR (HOTPLATE) GCPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FTPS%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FTPS%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmtpshpgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmtpshpgcpex",
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
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmtpshpgcpex/gpmtpshpgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/gcpex/gpmtpshpgcpex/gpmtpshpgcpex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/disdrometers_and_gauges/tps_hotplate/doc/DataFormat_hotplate_gcpex.pdf",
-                    "description": "Total Precipitation Sensor TPS-3100 (HotPlate), GCPEx Field Campaign  Last updated October 23, 2013",
                     "@type": "dcat:Distribution",
+                    "description": "Total Precipitation Sensor TPS-3100 (HotPlate), GCPEx Field Campaign  Last updated October 23, 2013",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/disdrometers_and_gauges/tps_hotplate/doc/DataFormat_hotplate_gcpex.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1979827156-GHRC_DAAC",
+            "issued": "2013-11-12",
+            "keyword": [
+                "earth science",
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "precipitation",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/TPS/DATA201",
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
             "spatial": "-79.78 44.2 -79.64 44.3",
+            "temporal": "2011-11-07T00:00:00Z/2012-02-21T23:59:59Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION TOTAL PRECIPITATION SENSOR (HOTPLATE) GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ERBE/S4G_SC_NEST10_L3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-06-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ERBE/S4G_SC_NEST10_L3.",
-            "issued": "2001-05-21",
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
-            "identifier": "C1000000774-LARC_ASDC",
             "description": "ERBE_S4G_SC_NEST10_1 is the Earth Radiation Budget Experiment (ERBE) S-4G Scanner (SC) 5 degree nested to 10 degree Regional Averages data set, which in in Hierarchical Data Format. Data collection for this data set is complete.\r\n\r\nERBE was a multi-satellite system designed to measure the Earth's radiation budget. The ERBE instruments flew on a mid-inclination National Aeronautics and Space Administration (NASA) Earth Radiation Budget Satellite (ERBS) and two sun-synchronous National Oceanic and Atmospheric Administration (NOAA) satellites, NOAA-9 and NOAA-10. NOAA-9 and NOAA-10 provided global coverage and the ERBS provided coverage between 67.5 degrees north and south latitude. Each satellite carried both a scanner and a non-scanner instrument package. The scanner instrument package contained three detectors to measure shortwave (0.2 to 5 microns), longwave (5 to 50 microns) and total waveband radiation (.2 to 50 microns). Each detector normally scanned the Earth perpendicular to the satellite ground-track from horizon-to-horizon. The detectors were thermistors which used space views on every scan as a reference point to guard against drift. They were located at the focal point of a f/1.84 Cassegrain telescope, whose aluminum-coated mirrors were overcoated to enhance ultraviolet reflectivity. The total channel had no filter; therefore it absorbed all wavelengths. The shortwave channel was a fused silica filter which transmitted only shortwave radiation. The longwave channel was a multilayer filter on a diamond substrate to reject shortwave energy and accept longwave. To enhance the spectral flatness of the detectors, each thermistor chip was coated with a thin layer of black paint. The effective field of view of the scanner was 3 degrees. The ERBE S-4G product contained averages of radiant flux and albedo on regional, zonal, and global scales. The data for the S-4G product were arranged by parameter values. The various combinations of the satellites reflected the actual duration of the scanners.",
-            "title": "Earth Radiation Budget Experiment (ERBE) S-4G Scanner (SC) 5 degree nested to 10 degree Regional Averages",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS4G_SC_NEST10_L3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS4G_SC_NEST10_L3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ERBE/S4G_SC_NEST10_L3",
-                    "description": "DOI data set landing page for ERBE_S4G_SC_NEST10_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ERBE_S4G_SC_NEST10_1",
+                    "downloadURL": "https://doi.org/10.5067/ERBE/S4G_SC_NEST10_L3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000774-LARC_ASDC",
-                    "description": "Earthdata Search for ERBE_S4G_SC_NEST10_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ERBE_S4G_SC_NEST10_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000774-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s4g_sc_2.5.txt",
-                    "description": "Read Software File for ERBE S-4G HDF Scanner Read Program",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software File for ERBE S-4G HDF Scanner Read Program",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/readme/readme_erbe_s4g_sc_2.5.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/rds4gscnhdf.c",
-                    "description": "Readme to read a monthly S-4G scanner HDF file - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to read a monthly S-4G scanner HDF file - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/rds4gscnhdf.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/rds4gscnhdf.f",
-                    "description": "Program to read D1 HDF format filed produced by ISCCP - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Program to read D1 HDF format filed produced by ISCCP - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/erbe/read_software/rds4gscnhdf.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S4G/SC_NEST10_1/",
-                    "description": "ASDC Direct Data Download for ERBE_S4G_SC_NEST10_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ERBE_S4G_SC_NEST10_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S4G/SC_NEST10_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000774-LARC_ASDC",
+            "issued": "2001-05-21",
+            "keyword": [
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ERBE/S4G_SC_NEST10_L3",
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
+            "title": "Earth Radiation Budget Experiment (ERBE) S-4G Scanner (SC) 5 degree nested to 10 degree Regional Averages"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR19-V1.0",
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
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Saturn Gravity and Ring Occultation experiments (SAGR19) Raw Data Archive is a time-ordered collection of radio science raw data acquired on  July 18 and 19, 2017, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr19-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR19-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr19-v1.0",
-            "description": "The Cassini Radio Science Saturn Gravity and Ring Occultation experiments (SAGR19) Raw Data Archive is a time-ordered collection of radio science raw data acquired on  July 18 and 19, 2017, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR19 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SAGR19 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-PRL-67P-M07-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-prl-67p-m07-geo-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-PRL-67P-M07-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-prl-67p-m07-geo-v1.0",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 PRL-MTP007 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 PRL-MTP007 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1011",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ehleringer, J.R., L.A. Martinelli, C. Cook, T.F. Domingues, L. Flanagan, J.A. Berry, and J.P.H.B. Ometto. 2011. LBA-ECO CD-02 Carbon and Oxygen Isotopes in Atmospheric CO2 in the Amazon: 1999-2004. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1011",
-            "issued": "2023-10-03",
-            "temporal": "1999-03-01T00:00:00Z/2004-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "biosphere",
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
-            "identifier": "C2777837638-ORNL_CLOUD",
             "description": "This data set reports carbon and oxygen stable isotope ratios of atmospheric carbon dioxide (CO2) collected at several forest and pasture sites and in the free troposphere over Amazonia. There are three comma-delimited ASCII files with this data set.Atmospheric CO2 concentrations and isotope signatures were measured at ten different forest and pasture canopy sites across the states of Amazonas, Para, and Rondonia within the Brazilian Amazon between March 1999 and March 2004. Both daytime and nighttime profile samples were collected.Samples of CO2 in the troposphere were collected during aircraft flights over the Amazon/Tapajos Rivers, FLONA Tapajos, and pasture/agriculture areas during five days in May 2003 (wet season). Samples were analyzed for carbon and oxygen isotopes of atmospheric CO2. Flights ranged from low altitudes to above the diurnal tropospheric boundary layer.Measurements of carbon and oxygen stable isotope ratios of atmospheric carbon dioxide (CO2) are a powerful indicator of large-scale CO2 exchange on land across multiple spatial scales. Stable carbon isotope composition of leaf tissue and CO2 released by respiration (delta r) can be used as an estimate of changes in ecosystem isotopic discrimination that occur in response to seasonal and interannual changes in environmental conditions, and land-use change (forest-pasture conversion). Understanding of carbon dioxide stable isotope composition can play a central role in influencing our understanding of the extent to which terrestrial ecosystems are carbon sinks.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-02 Carbon and Oxygen Isotopes in Atmospheric CO2 in the Amazon: 1999-2004",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1011",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1011",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD02_Atmosphere_CO2_Isotopes/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD02_Atmosphere_CO2_Isotopes/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD02_Atmosphere_CO2_Isotopes.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD02_Atmosphere_CO2_Isotopes.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1011",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1011",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD02_Atmosphere_CO2_Isotopes/comp/CD02_Atmosphere_CO2_Isotopes.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD02_Atmosphere_CO2_Isotopes/comp/CD02_Atmosphere_CO2_Isotopes.pdf",
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
+            "identifier": "C2777837638-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "biosphere",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1011",
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
+            "temporal": "1999-03-01T00:00:00Z/2004-03-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-02 Carbon and Oxygen Isotopes in Atmospheric CO2 in the Amazon: 1999-2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D66.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang\r\n. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band5 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D66.061. https://doi.org/10.5067/MODIS/MCD43D66.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "national geospatial data asset",
-                "surface radiative properties",
-                "land surface",
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
-            "identifier": "C2540275742-LPCLOUD",
-            "description": "The MCD43D66 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Nadir BRDF-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D62 through MCD43D68 are the NBAR products of the MCD43D BRDF/Albedo product suite for MODIS bands 1 through 7. The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon.\r\n\r\nMCD43D66 is the NBAR for MODIS band 5. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band5 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D66 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) Nadir BRDF-Adjusted Reflectance (NBAR) dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D62 through MCD43D68 are the NBAR products of the MCD43D BRDF/Albedo product suite for MODIS bands 1 through 7. The NBAR algorithm removes view angle effects from directional reflectances to model the values as if they were collected from a nadir view at local solar noon.\r\n\r\nMCD43D66 is the NBAR for MODIS band 5. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D66.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D66.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D66.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D66.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540275742-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540275742-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D66.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D66.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D66",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D66",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D66.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D66.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540275742-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "national geospatial data asset",
+                "surface radiative properties",
+                "land surface",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D66.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo Nadir BRDF-Adjusted Ref Band5 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-ACCEL-5-PROFILE-V1.0",
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
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-accel-5-profile-v1.0_issv-8stw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars reconnaissance orbiter",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-ACCEL-5-PROFILE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-accel-5-profile-v1.0_issv-8stw",
-            "description": "TBD",
-            "title": "MRO PROFILE DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MRO PROFILE DATA RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/istk-5pvj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "['\"treatment protocol\"' '\"nucleic acid extraction\"' '\"library construction\"' '\"nucleic acid sequencing\"']",
-                "['\"study subject\"' '\"time\"' '\"altered gravity\"']"
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
-            "identifier": "nasa_genelab_GLDS-355_istk-5pvj",
             "description": "['\"Understanding physiologic reactions to weightlessness is an indispensable requirement for safe human space missions. While adaptations of human organ systems in response to weightlessness have been described in former studies, their molecular background needs further elucidation. The study aims to analyse changes in the expression of circulating miRNAs in serum in response to gravitational changes induced by parabolic flight as a spaceflight analogue.\"']",
-            "title": "['\"Next-generation sequencing analysis of circulating micro-RNA expression in response to parabolic flight as a spaceflight analogue\"']",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-355",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-355",
+                    "mediaType": "text/html",
                     "title": "['\"Next-generation sequencing analysis of circulating micro-RNA expression in response to parabolic flight as a spaceflight analogue\"']"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-355_istk-5pvj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "['\"treatment protocol\"' '\"nucleic acid extraction\"' '\"library construction\"' '\"nucleic acid sequencing\"']",
+                "['\"study subject\"' '\"time\"' '\"altered gravity\"']"
+            ],
+            "landingPage": "https://data.nasa.gov/d/istk-5pvj",
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
+            "title": "['\"Next-generation sequencing analysis of circulating micro-RNA expression in response to parabolic flight as a spaceflight analogue\"']"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/BSLOAIYXCLHU",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLPX-Ground: Micrometeorological Data at the Local Scale Observation Site (LSOS), Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/BSLOAIYXCLHU.",
-            "issued": "2002-11-06",
-            "temporal": "2002-11-06T00:00:00Z/2003-05-29T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-05-29",
-            "keyword": [
-                "earth science",
-                "soils",
-                "land surface",
-                "cryosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere",
-                "snow/ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "A.W. England",
                 "hasEmail": "mailto:england@eecs.umich.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386203951-NSIDCV0",
             "description": "This data set includes two sets of soil temperature profiles, two sets of soil moisture profiles, two sets of soil heat flux profiles (in dense pine and open pine areas), and one set of a snow temperature profile, air temperature, and relative humidity measurements. Measurements were made at the Local Scale Observation Site (LSOS) of the Cold Land Processes Field Experiment (CLPX) in northern Colorado.",
-            "title": "CLPX-Ground: Micrometeorological Data at the Local Scale Observation Site (LSOS), Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FBSLOAIYXCLHU",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FBSLOAIYXCLHU",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0168_lsos_micromet/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/ground_data/nsidc0168_lsos_micromet/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/BSLOAIYXCLHU",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/BSLOAIYXCLHU",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/BSLOAIYXCLHU",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/BSLOAIYXCLHU",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386203951-NSIDCV0",
+            "issued": "2002-11-06",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface",
+                "cryosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.5067/BSLOAIYXCLHU",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-05-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-105.88294 0.0 0.0 39.90661",
+            "temporal": "2002-11-06T00:00:00Z/2003-05-29T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLPX-Ground: Micrometeorological Data at the Local Scale Observation Site (LSOS), Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1750",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Elkins, J.W., E.J. Hintsa, and F.L. Moore. 2019. ATom: Measurements from the UAS Chromatograph for Atmospheric Trace Species (UCATS). ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1750",
-            "issued": "2020-03-30",
-            "temporal": "2016-07-12T18:41:00Z/2018-05-21T23:37:58Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
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
-            "identifier": "C2676964600-ORNL_CLOUD",
             "description": "This dataset, collected with the Unmanned Aircraft Systems (UAS) Chromatograph for Atmospheric Trace Species (UCATS), provides atmospheric concentrations of nitrous oxide (N2O), sulfur hexafluoride (SF6), methane (CH4), hydrogen (H2), carbon monoxide (CO), water vapor (H2O), and ozone (O3). The UCATS system is three different instruments in one enclosure: a two-channel chromatograph with electron capture detectors (one measures N2O and SF6, the other measures CH4, H2 and CO), a tunable diode laser instrument for H2O, and a dual-beam O3 photometer.",
-            "graphic-preview-description": "The UCATS system is three different instruments in one enclosure: a two-channel chromatograph with electron capture detectors (one measures N2O and SF6, the other measures CH4, H2 and CO), a tunable diode laser instrument for H2O, and a dual-beam O3 photometer.",
-            "title": "ATom: Measurements from the UAS Chromatograph for Atmospheric Trace Species (UCATS)",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_UCATS_Instrument_Data_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1750",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1750",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_UCATS_Instrument_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_UCATS_Instrument_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_UCATS_Instrument_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_UCATS_Instrument_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1750",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1750",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_UCATS_Instrument_Data/comp/ATom_UCATS_Instrument_Data.pdf",
-                    "description": "ATom: Measurements from the UAS Chromatograph for Atmospheric Trace Species (UCATS): ATom_UCATS_Instrument_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: Measurements from the UAS Chromatograph for Atmospheric Trace Species (UCATS): ATom_UCATS_Instrument_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_UCATS_Instrument_Data/comp/ATom_UCATS_Instrument_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_UCATS_Instrument_Data_Fig1.png",
-                    "description": "The UCATS system is three different instruments in one enclosure: a two-channel chromatograph with electron capture detectors (one measures N2O and SF6, the other measures CH4, H2 and CO), a tunable diode laser instrument for H2O, and a dual-beam O3 photometer.",
                     "@type": "dcat:Distribution",
+                    "description": "The UCATS system is three different instruments in one enclosure: a two-channel chromatograph with electron capture detectors (one measures N2O and SF6, the other measures CH4, H2 and CO), a tunable diode laser instrument for H2O, and a dual-beam O3 photometer.",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_UCATS_Instrument_Data_Fig1.png",
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
+            "graphic-preview-description": "The UCATS system is three different instruments in one enclosure: a two-channel chromatograph with electron capture detectors (one measures N2O and SF6, the other measures CH4, H2 and CO), a tunable diode laser instrument for H2O, and a dual-beam O3 photometer.",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_UCATS_Instrument_Data_Fig1.png",
+            "identifier": "C2676964600-ORNL_CLOUD",
+            "issued": "2020-03-30",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1750",
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
+            "temporal": "2016-07-12T18:41:00Z/2018-05-21T23:37:58Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: Measurements from the UAS Chromatograph for Atmospheric Trace Species (UCATS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPFLX-3-RDR-CROMMELIN-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppflx-3-rdr-crommelin-v1.0_it4h-qett",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPFLX-3-RDR-CROMMELIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppflx-3-rdr-crommelin-v1.0_it4h-qett",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET PPFLX CALIB REDUCED DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET PPFLX CALIB REDUCED DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/373",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Verma, S.B., and A. Suyker. 1999. BOREAS TF-11 SSA-FEN Tower Flux and Meteorological Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/373",
-            "issued": "2023-11-22",
-            "temporal": "1993-08-23T00:00:00Z/1995-10-09T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "land surface",
-                "surface water",
-                "soils",
-                "earth science",
-                "biosphere",
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric chemistry",
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric pressure",
-                "vegetation",
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
-            "identifier": "C2808131174-ORNL_CLOUD",
             "description": "The flux and ancillary data collected at the SSA-Fen tower flux site by the TF-11 group.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-11 SSA-FEN Tower Flux and Meteorological Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F373",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F373",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf11tfx/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf11tfx/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF11_Fen_Flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF11_Fen_Flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/373",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/373",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11tfx/comp/tf11tfx.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11tfx/comp/tf11tfx.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11tfx/comp/TF11_Fen_Flux.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11tfx/comp/TF11_Fen_Flux.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11tfx/comp/TF11_Fen_Flux.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11tfx/comp/TF11_Fen_Flux.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11tfx/comp/TF11_Fen_Flux.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11tfx/comp/TF11_Fen_Flux.txt",
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
+            "identifier": "C2808131174-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "land surface",
+                "surface water",
+                "soils",
+                "earth science",
+                "biosphere",
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric chemistry",
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric pressure",
+                "vegetation",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/373",
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
+            "temporal": "1993-08-23T00:00:00Z/1995-10-09T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-11 SSA-FEN Tower Flux and Meteorological Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2003",
             "citation": "Deborah Stein-Zweers, and Pepijn Veefkind. 2012-03-23. OMAEROZ. Version 003. OMI/Aura Aerosol product Multi-wavelength Algorithm Zoomed 1-Orbit L2 Swath 13x12km V003. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA2003. https://disc.gsfc.nasa.gov/datacollection/OMAEROZ_003.html. Digital Science Data.",
-            "issued": "2012-03-23",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-03-23",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2006.869987",
-                "https://doi.org/10.1109/TGRS.2006.872935",
-                "https://doi.org/10.1117/12.627013"
-            ],
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jerome Alfred",
                 "hasEmail": "mailto:jerome.m.alfred@nasa.gov"
             },
+            "creator": "Deborah Stein-Zweers, and Pepijn Veefkind",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239966783-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The reprocessed OMI/Aura Level-2 Zoomed Aerosol data product OMAEROZ at 13x12 km resolution have been made available from the NASA Goddard Earth Sciences Data and Information Services Center (GES DISC) for public access in March 2012. There are two Level-2 Aura OMI aerosol products OMAERO and OMAERUV. The OMAERUV product uses the near-UV algorithm. The OMAERO (13x24 km resolution) and OMAEROZ (13x12 km resolution) is based on the multi-wavelength algorithm that uses up to 20 wavelength bands between 331 nm and 500 nm. The multi-wavelength retrieval algorithm is developed by the KNMI OMI Team Scientists. Drs. Deborah Stein-Zweers, Martin Sneep and Pepijn Veefkind are now the key investigators of this product. The OMAEROZ products contain Aerosol Optical Depths, Single Scattering Albedo, Aerosol Type, Aerosol Layer Height, and other intermediate and ancillary parameters and geolocation information.\n\nThe OMAEROZ files are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5). Each file contains data from the day lit portion of an orbit (~53 minutes). OMAEROZ data files are based on Zoomed Level 1B radiance observations which are made once a month. Thus there is one day of zoomed data (approximately 14 orbits) per month. The maximum file size for the OMAEROZ data is about 11 Mbytes.\n\nA Readme document containing brief algorithm description and known data quality related issues and file specifications are provided by the OMAERO Algorithm lead.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMAEROZ",
-            "creator": "Deborah Stein-Zweers, and Pepijn Veefkind",
-            "title": "OMI/Aura Aerosol product Multi-wavelength Algorithm Zoomed 1-Orbit L2 Swath 13x12km V003 (OMAEROZ) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMAEROZ_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -937225,73 +937198,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMAEROZ_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMAEROZ_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMAEROZ.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMAEROZ.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Level2/OMAEROZ.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Level2/OMAEROZ.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMAEROZ_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMAEROZ_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMAEROZ.003/doc/README.OMAERO.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMAEROZ.003/doc/README.OMAERO.pdf",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-03.pdf",
-                    "description": "OMI Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithm/ATBD-OMI-03.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/SD-OMIE-KNMI-645_Aerosol_PFS.pdf",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/SD-OMIE-KNMI-645_Aerosol_PFS.pdf",
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
@@ -937301,57 +937274,62 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMAEROZ_003.png",
+            "identifier": "C1239966783-GES_DISC",
+            "issued": "2012-03-23",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-03-23",
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
+            "series-name": "OMAEROZ",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Aerosol product Multi-wavelength Algorithm Zoomed 1-Orbit L2 Swath 13x12km V003 (OMAEROZ) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8Z3QQKHC4R4C",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee. 2020-08-10. OCO2_L2_Standard. Version 11r. OCO-2 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V11r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/8Z3QQKHC4R4C. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Standard_11r.html. Digital Science Data.",
-            "issued": "2020-08-01",
-            "temporal": "2014-09-06T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-01",
-            "keyword": [
-                "earth science",
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
-            "identifier": "C2248652620-GES_DISC",
-            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection is the output from the algorithm retrieving the column-averaged CO2 dry air mole fraction XCO2 and other quantities from the spectra collected by the Orbiting Carbon Observatory-2 (OCO-2).\n\nThis is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_Standard",
             "creator": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee",
-            "title": "OCO-2 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V11r (OCO2_L2_Standard) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Std_10r_Sep2021.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection is the output from the algorithm retrieving the column-averaged CO2 dry air mole fraction XCO2 and other quantities from the spectra collected by the Orbiting Carbon Observatory-2 (OCO-2).\n\nThis is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8Z3QQKHC4R4C",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8Z3QQKHC4R4C",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -937361,52 +937339,52 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Standard_11r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_Standard_11r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Standard.11r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_Standard.11r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_Standard",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_Standard",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Standard.11r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_Standard.11r/contents.html",
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
@@ -937416,1344 +937394,1378 @@
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Standard.V7.pdf",
-                    "description": "Software Interface Specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software Interface Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Standard.V7.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_Std_10r_Sep2021.png",
+            "identifier": "C2248652620-GES_DISC",
+            "issued": "2020-08-01",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/8Z3QQKHC4R4C",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-03-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_L2_Standard",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-09-06T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 geolocated XCO2 retrievals results, physical model, Retrospective Processing V11r (OCO2_L2_Standard) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-PHC-V2.0",
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
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-phc-v2.0_it8e-zntv",
             "description": "This archive contains edited data (CODMAC level 2) from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired  during PHC mission phase (Post Hibernation Commissioning) on its journey to comet 67P/C-G. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.  This data set supersedes RO/RL-CAL-CONSERT-2-PHC-V1.0.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                           2 PHC V2.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-phc-v2.0_it8e-zntv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-PHC-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
             "programCode": [
                 "026:005"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
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
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                           2 PHC V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/L0T5GEG1NYFA",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2T1NXLFO. Version 5.12.4. MERRA-2 tavg1_2d_lfo_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Land Surface Forcings V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/L0T5GEG1NYFA. https://disc.gsfc.nasa.gov/datacollection/M2T1NXLFO_5.12.4.html. Digital Science Data.",
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
-                "terrestrial hydrosphere",
-                "snow/ice",
-                "earth science",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812850-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2T1NXLFO (or  tavg1_2d_lfo_Nx) is an hourly time-averaged 2-dimensional data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of land surface forcing parameters, such as bias corrected precipitation,  shortwave and longwave radiation at surface.  The data field is time-stamped with the central time of an hour starting from 00:30 UTC, e.g.: 00:30, 01:30, \u2026 , 23:30 UTC.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2T1NXLFO",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 tavg1_2d_lfo_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2T1NXLFO) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2T1NXLFO",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL0T5GEG1NYFA",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FL0T5GEG1NYFA",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXLFO_5.12.4.png",
-                    "description": "M2T1NXLFO variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2T1NXLFO variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXLFO_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T1NXLFO_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T1NXLFO_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXLFO.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXLFO.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2T1NXLFO",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2T1NXLFO",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T1NXLFO",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T1NXLFO",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXLFO.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXLFO.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXLFO.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXLFO.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T1NXLFO.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T1NXLFO.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXLFO.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXLFO.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=M2T1NXLFO",
+            "identifier": "C1276812850-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "precipitation",
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "earth science",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/L0T5GEG1NYFA",
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
+            "series-name": "M2T1NXLFO",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavg1_2d_lfo_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Land Surface Forcings 0.625 x 0.5 degree V5.12.4 (M2T1NXLFO) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/doi:10.5067/036VLNHJM106",
             "citation": "Daniel Tong at Geroge Mason University . 2023-04-18. HAQES_NA_PM25_TOT_COUNTY. Version 1. HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration at county level, North America V1.0. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/doi:10.5067/036VLNHJM106. https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_COUNTY_1.html. Digital Science Data.",
-            "issued": "2023-04-15",
-            "temporal": "2022-01-02T00:00:00Z/2023-05-08T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-15",
-            "references": [
-                "https://doi.org/%20http%3A//doi.org/10.1016/j.atmosenv.2015.11.004"
-            ],
-            "keyword": [
-                "human dimensions",
-                "public health",
-                "earth science",
-                "atmosphere",
-                "air quality",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Suhung Shen",
                 "hasEmail": "mailto:suhung.shen-1@nasa.gov"
             },
+            "creator": "Daniel Tong at Geroge Mason University",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2623694345-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product provides HAQES 3-hourly ensemble mean surface total PM2.5 concentration at the county level over the continental United States (CONUS).  \n\nThe Hazardous Air Quality Ensemble System (HAQES) is a real-time ensemble forecast of hazardous air quality events, such as wildfires, dust storms, and Volcanic eruptions. Both regional and global models from multiple agencies are used to create the ensemble, including the Goddard Earth Observing System (GEOS) from the National Aeronautics and Space Administration (NASA), the Navy Aerosol Analysis and Prediction System (NAAPS) from Naval Research Laboratory, the Global Ensemble Forecast System Aerosols (GEFS), High-Resolution Rapid Refresh (HRRR), and National Oceanic and Atmospheric Administration-U.S. Environmental Protection Agency (NOAA-EPA) Atmosphere-Chemistry Coupler-Community Multiscale Air Quality model (NACC-CMAQ) from NOAA.  The prototypes of HAQES products were developed by the George Mason University Air Quality Laboratory as part of the NASA Health Air Quality Applied Science Team (HAQAST).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HAQES_NA_PM25_TOT_COUNTY",
-            "creator": "Daniel Tong at Geroge Mason University",
-            "graphic-preview-description": "Sample image: The surface total PM2.5 concentration at the county level from the HAQES model for November 12, 2022 at 18:00Z.",
-            "title": "HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration at county level, North America V1 (HAQES_NA_PM25_TOT_COUNTY) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_COUNTY_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F036VLNHJM106",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F036VLNHJM106",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_COUNTY_1.png",
-                    "description": "Sample image: The surface total PM2.5 concentration at the county level from the HAQES model for November 12, 2022 at 18:00Z.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image: The surface total PM2.5 concentration at the county level from the HAQES model for November 12, 2022 at 18:00Z.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_COUNTY_1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT_COUNTY.1/doc/README_HAQES_PM25_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT_COUNTY.1/doc/README_HAQES_PM25_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_COUNTY_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQES_NA_PM25_TOT_COUNTY_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT_COUNTY.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQES_NA_PM25_TOT_COUNTY.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQES_NA_PM25_TOT_COUNTY",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQES_NA_PM25_TOT_COUNTY",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Sample image: The surface total PM2.5 concentration at the county level from the HAQES model for November 12, 2022 at 18:00Z.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQES_NA_PM25_TOT_COUNTY_1.png",
+            "identifier": "C2623694345-GES_DISC",
+            "issued": "2023-04-15",
+            "keyword": [
+                "human dimensions",
+                "public health",
+                "earth science",
+                "atmosphere",
+                "air quality",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/doi:10.5067/036VLNHJM106",
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
+            "series-name": "HAQES_NA_PM25_TOT_COUNTY",
             "spatial": "-132.0 21.0 -58.5 53.5",
+            "temporal": "2022-01-02T00:00:00Z/2023-05-08T00:00:00Z",
             "theme": [
                 "HAQAST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HAQES 3-Hourly Ensemble mean surface total PM2.5 concentration at county level, North America V1 (HAQES_NA_PM25_TOT_COUNTY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67PCHURYUMOV-M25-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the ROSETTA EXTENSION 1 phase of the Rosetta mission, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67pchuryumov-m25-v1.0_itd3-tcay",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "zeta cas",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT1-67PCHURYUMOV-M25-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext1-67pchuryumov-m25-v1.0_itd3-tcay",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the ROSETTA EXTENSION 1 phase of the Rosetta mission, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP025 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT1-MTP025 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SurfaceMonitorNetwork/MAIA/SURFACEMONITOR_PM_TOTAL_ANC.C01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/SurfaceMonitorNetwork/MAIA/SURFACEMONITOR_PM_TOTAL_ANC.C01. https://asdc.larc.nasa.gov/project/MAIA/MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01.",
-            "issued": "2024-10-09",
-            "temporal": "2021-01-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amber Jenkins",
                 "hasEmail": "mailto:amber.h.jenkins@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C3271469675-LARC_ASDC",
             "description": "The MAIA Surface Monitor Stage 0 files are an ancillary dataset containing processed particulate matter (PM) measurements collected from a global in-situ surface monitoring network. The files are generated by the MAIA surface monitoring subsystem software at NASA\u2019s Atmospheric Science Data Center (ASDC).",
-            "graphic-preview-description": "Mission Logo",
-            "title": "Ancillary total PM data from the MAIA Surface Monitor Network",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/maia.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSurfaceMonitorNetwork%2FMAIA%2FSURFACEMONITOR_PM_TOTAL_ANC.C01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSurfaceMonitorNetwork%2FMAIA%2FSURFACEMONITOR_PM_TOTAL_ANC.C01",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3271469675-LARC_ASDC",
-                    "description": "Earthdata Search for MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3271469675-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SurfaceMonitorNetwork/MAIA/SURFACEMONITOR_PM_TOTAL_ANC.C01",
-                    "description": "DOI data set landing page for MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01",
+                    "downloadURL": "https://doi.org/10.5067/SurfaceMonitorNetwork/MAIA/SURFACEMONITOR_PM_TOTAL_ANC.C01",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://maia.jpl.nasa.gov/",
-                    "description": "NASA MAIA Project Page",
                     "@type": "dcat:Distribution",
+                    "description": "NASA MAIA Project Page",
+                    "downloadURL": "https://maia.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/maia.png",
-                    "description": "Mission Logo",
                     "@type": "dcat:Distribution",
+                    "description": "Mission Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/maia.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MAIA/ANC/SURFACEMONITOR_PM_TOTAL/",
-                    "description": "ASDC Direct Data Download for MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MAIA/ANC/SURFACEMONITOR_PM_TOTAL/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MAIA/ANC/SURFACEMONITOR_PM_TOTAL/contents.html",
-                    "description": "OPeNDAP data access for MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MAIA_ANC_SURFACEMONITOR_PM_TOTAL_C01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MAIA/ANC/SURFACEMONITOR_PM_TOTAL/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/maia.png",
+            "identifier": "C3271469675-LARC_ASDC",
+            "issued": "2024-10-09",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/SurfaceMonitorNetwork/MAIA/SURFACEMONITOR_PM_TOTAL_ANC.C01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2021-01-01T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "MAIA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ancillary total PM data from the MAIA Surface Monitor Network"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/9UYFIEJSO7MN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAPVEX19-22 Millbrook Lidar Derived Digital Elevation Model V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/9UYFIEJSO7MN.",
-            "issued": "2022-04-03",
-            "temporal": "2022-04-02T00:00:00Z/2022-08-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-09",
-            "keyword": [
-                "earth science",
-                "land surface",
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
-            "identifier": "C2697180532-NSIDC_ECS",
             "description": "These digital elevation model (DEM) data consist of ground surface elevations derived from source lidar measurements collected in April and August 2022 in the vicinity of Millbrook, NY during the SMAPVEX19-22 campaign. This location was chosen due to its forested land cover, as SMAPVEX19-22 aims to validate satellite derived soil moisture estimates in forested areas. The two acquisition periods occurred to characterize differences during \"leaf-off\" and \"leaf-on\" conditions.",
-            "title": "SMAPVEX19-22 Millbrook Lidar Derived Digital Elevation Model V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9UYFIEJSO7MN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9UYFIEJSO7MN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV19MB_DEM.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SMAP_VAL/SV19MB_DEM.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SV19MB_DEM+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SV19MB_DEM+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV19MB_DEM/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SV19MB_DEM/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9UYFIEJSO7MN",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/9UYFIEJSO7MN",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9UYFIEJSO7MN",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/9UYFIEJSO7MN",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2697180532-NSIDC_ECS",
+            "issued": "2022-04-03",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/9UYFIEJSO7MN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-73.81 41.66 -73.42 42.05",
+            "temporal": "2022-04-02T00:00:00Z/2022-08-09T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMAPVEX19-22 Millbrook Lidar Derived Digital Elevation Model V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NIMBUS/NmAVCS3H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus Advanced Vidicon Camera System Remapped Visible Imagery Daily L3, HDF5 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NIMBUS/NmAVCS3H.",
-            "issued": "1964-08-31",
-            "temporal": "1964-08-31T00:00:00Z/1966-09-03T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1966-09-03",
-            "keyword": [
-                "spectral/engineering",
-                "visible wavelengths",
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
-            "identifier": "C191091722-NSIDC_ECS",
             "description": "This data set (NmAVCS3H) consists of daily, global image composites constructed from Nimbus 1 (1964) and Nimbus 2 (1966) Advanced Vidicon Camera System (AVCS) imagery. Each composite is provided as a set of three HDF5-formatted files: separate North and South Polar projections in the 5 km Equal-Area Scalable Earth Grid (EASE-Grid) and an equatorial projection in a 10 km equidistant grid for the region between 60 N and 60 S.",
-            "title": "Nimbus Advanced Vidicon Camera System Remapped Visible Imagery Daily L3, HDF5 V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmAVCS3H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmAVCS3H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmAVCS3H.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmAVCS3H.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C191091722-NSIDC_ECS&m=-31.359375%210.5625%211%211%210%210%2C2&tl=1511800470%214%21%21&q=NmAVCS3H",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C191091722-NSIDC_ECS&m=-31.359375%210.5625%211%211%210%210%2C2&tl=1511800470%214%21%21&q=NmAVCS3H",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmAVCS3H/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmAVCS3H/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmAVCS3H",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmAVCS3H",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmAVCS3H",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmAVCS3H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C191091722-NSIDC_ECS",
+            "issued": "1964-08-31",
+            "keyword": [
+                "spectral/engineering",
+                "visible wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NIMBUS/NmAVCS3H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1966-09-03",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1964-08-31T00:00:00Z/1966-09-03T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus Advanced Vidicon Camera System Remapped Visible Imagery Daily L3, HDF5 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-NNSN-3-EDR-CROMMELIN-V1.0",
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
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-nnsn-3-edr-crommelin-v1.0_itfv-ahnh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-NNSN-3-EDR-CROMMELIN-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-nnsn-3-edr-crommelin-v1.0_itfv-ahnh",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET NNSN CALIB EXPERIMENT DATA RECORD CROMMELIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "IHW COMET NNSN CALIB EXPERIMENT DATA RECORD CROMMELIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Belk, E.L., D. Markewitz, T. Rasmussen, C.J.R. de Carvalho, D.C. Nepstad, and E.A. Davidson. 2012. LBA-ECO ND-02 Soil Volumetric Water Content, Tapajos National Forest, Brazil . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1061",
-            "issued": "2023-10-03",
-            "temporal": "1999-05-19T00:00:00Z/2001-05-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-09",
-            "keyword": [
-                "biosphere",
-                "ecosystems",
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
-            "identifier": "C2779742781-ORNL_CLOUD",
             "description": "This data set reports monthly measured soil volumetric water content (VWC) from a rainfall exclusion experiment that was conducted from 1999-2001 at the km 67 Seca Floresta site, Tapajos National Forest, Brazil. The purpose was to observe the potential effects of severe water stress on a humid Amazonian forest (Nepstad 2002). There are two ASCII comma delimited files with measured VWC, one for the control plot and one for the rainfall exclusion plot.These measured values were used by the authors to develop a model of daily changes in the distribution of water through the soil layers. The simulated daily VWC values are also provided in the file with the measured VWC. For comparison, results of VWC simulation for the control and treatment plots using a STELLA model which incorporates rainfall and plant water uptake are provided. There are two ASCII comma delimited files of simulated results. See Belk et. al., 2007 for details.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-02 Soil Volumetric Water Content, Tapajos National Forest, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND02_REE_Soil_VWC/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND02_REE_Soil_VWC/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND02_REE_Soil_VWC.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND02_REE_Soil_VWC.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1061",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND02_REE_Soil_VWC/comp/ND02_REE_Soil_VWC.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND02_REE_Soil_VWC/comp/ND02_REE_Soil_VWC.pdf",
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
+            "identifier": "C2779742781-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "ecosystems",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1061",
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
             "spatial": "-2.75 -55.0",
+            "temporal": "1999-05-19T00:00:00Z/2001-05-19T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-02 Soil Volumetric Water Content, Tapajos National Forest, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1208",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Takahashi, T., S.C. Sutherland, R.H. Wanninkhof, R.A. Feely, R.F. Weiss, D.W. Chipman, N. Bates, J. Olafsson, C. Sabine, A. Poisson, N. Metzl, B. Tilbrook, Y. Nojiri, C. Sweeney, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2014. ISLSCP II Air-Sea Carbon Dioxide Gas Exchange. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1208",
-            "issued": "2023-10-15",
-            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
-            "keyword": [
-                "atmosphere",
-                "oceans",
-                "ocean chemistry",
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
-            "identifier": "C2785340637-ORNL_CLOUD",
             "description": "This data set contains the calculated net ocean-air carbon dioxide (CO2) flux and sea-air CO2 partial pressure (pCO2) difference. The estimates are based on approximately one million measurements made for the pCO2 in surface waters of the global ocean since the International Geophysical Year, 1956-1959. Only the ocean water pCO2 values measured using direct gas-seawater equilibration methods were used. The results represent the climatological distributions under non-El Nino conditions. Since the measurements were made in different years, during which the atmospheric pCO2 was increasing, they were corrected to a single reference year (arbitrarily chosen to be 1995) on the basis of the following assumptions: -Surface waters in subtropical gyres mix vertically at slow rates with subsurface waters due to the presence of strong stratification at the base of the mixed layer. This will allow a long contact time with the atmosphere to exchange CO2. Therefore, their CO2 chemistry tends to follow the atmospheric CO2 increase. Accordingly, the pCO2 measured in a given month and year is corrected to the same month of the reference year 1995 using changes in the atmospheric CO2 concentration occurred during this period.-Oceanic pCO2 measurements made after the beginning of 1979 have been corrected to 1995 using the atmospheric CO2 concentration data from the GLOBALVIEW-CO2 database (2000), in which the zonal mean atmospheric concentrations (for each 0.05 in sine of latitude) within the planetary boundary layer are summarized for each month since 1979 to 2000.-Pre-1979 oceanic pCO2 data were corrected to 1979 using the annual mean trend for the global mean atmospheric CO2 concentration constructed from the Mauna Loa data of Keeling and Whorf (2000), and then from 1979 to 1995 using the GLOBALVIEW-CO2 database. -Measurements for pCO2 made in the following areas have been corrected for the time of observation; 45 degrees N, 50  degrees S, in the Atlantic Ocean, north of 50 degrees S in the Indian Ocean, 40 degrees N, 50 degrees S in the western Pacific west of the date line, and 40 degrees N, 60 degrees S, in the eastern Pacific east of the date line.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Air-Sea Carbon Dioxide Gas Exchange",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1208",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1208",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/carbon/air_sea_gas_exchange_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/carbon/air_sea_gas_exchange_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/air_sea_gas_exchange_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/air_sea_gas_exchange_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1208",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1208",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/air_sea_gas_exchange_xdeg/comp/0_air_sea_gas_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/air_sea_gas_exchange_xdeg/comp/0_air_sea_gas_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/air_sea_gas_exchange_xdeg/comp/1_air_sea_gas_exchange_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/air_sea_gas_exchange_xdeg/comp/1_air_sea_gas_exchange_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/air_sea_gas_exchange_xdeg/comp/air_sea_gas_exchange_xdeg.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/carbon/air_sea_gas_exchange_xdeg/comp/air_sea_gas_exchange_xdeg.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/islscp_logo_square.png",
+            "identifier": "C2785340637-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "atmosphere",
+                "oceans",
+                "ocean chemistry",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1208",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Air-Sea Carbon Dioxide Gas Exchange"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/231",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kouwen, N., R. Soulis, W. Jenkinson, A. Graham, and T. Neff. 1998. BOREAS 1995 HYD-09 Belfort Rain Gauge Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/231",
-            "issued": "2023-11-22",
-            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-27",
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
-            "identifier": "C2807610000-ORNL_CLOUD",
             "description": "Contains the Belfort rain gauge data that was collected by the HYD09 group at various locations.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS 1995 HYD-09 Belfort Rain Gauge Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F231",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F231",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h9rgbl95/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/HYD/h9rgbl95/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD09_BELF_RG.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/HYD09_BELF_RG.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/231",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/231",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgbl95/comp/h9rgbl95.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgbl95/comp/h9rgbl95.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgbl95/comp/HYD09_BELF_RG.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgbl95/comp/HYD09_BELF_RG.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgbl95/comp/HYD09_BELF_RG.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgbl95/comp/HYD09_BELF_RG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgbl95/comp/HYD09_BELF_RG.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/HYD/h9rgbl95/comp/HYD09_BELF_RG.txt",
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
+            "identifier": "C2807610000-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/231",
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
             "spatial": "-105.04 53.89 -98.34 55.92",
+            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS 1995 HYD-09 Belfort Rain Gauge Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-PLS-4-SUMM-VET-V1.0",
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
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This file is a listing of particle\nenergy spectra from the Galileo Plasma Instrument (PLS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-pls-4-summ-vet-v1.0_itp2-ihep",
+            "issued": "2021-05-21",
+            "keyword": [
+                "galileo",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V-PLS-4-SUMM-VET-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-pls-4-summ-vet-v1.0_itp2-ihep",
-            "description": "This file is a listing of particle\nenergy spectra from the Galileo Plasma Instrument (PLS).",
-            "title": "GO VEN PLS SUMM VENUS ET V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO VEN PLS SUMM VENUS ET V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC4-CALIBRATED-V9.0",
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
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nCOMET ESCORT 4 Phase from October 21, 2015 until January 12, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc4-calibrated-v9.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-3-ESC4-CALIBRATED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-3-esc4-calibrated-v9.0",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the\nCOMET ESCORT 4 Phase from October 21, 2015 until January 12, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC4 CALIBRATED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 3 ESC4 CALIBRATED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0951-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-08T21:30:20.000 to 2015-08-09T05:22:25.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0951-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0951-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0951-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-08T21:30:20.000 to 2015-08-09T05:22:25.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0951 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0951 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V6.0",
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
+            "description": "The data set lists orbital and physical properties for well-observed or suspected binary/multiple minor planets including the Pluto system, as inspired by Richardson and Walsh (2006) and similar reviews (Merline et al., 2003; Noll, 2006; Pravec et al., 2006; Pravec and Harris, 2007; Descamps and Marchis, 2008; Noll et al., 2008; Walsh, 2009). In total 242 companions in 229 systems are included. Data are presented in three tables: one for orbital and physical properties; one for companion designations, discovery information, and reference codes for data values; and one giving full references for each reference code. This data set is complete for binary/multiple components reported through 31 March 2013.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v6.0_itss-ra77",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v6.0_itss-ra77",
-            "description": "The data set lists orbital and physical properties for well-observed or suspected binary/multiple minor planets including the Pluto system, as inspired by Richardson and Walsh (2006) and similar reviews (Merline et al., 2003; Noll, 2006; Pravec et al., 2006; Pravec and Harris, 2007; Descamps and Marchis, 2008; Noll et al., 2008; Walsh, 2009). In total 242 companions in 229 systems are included. Data are presented in three tables: one for orbital and physical properties; one for companion designations, discovery information, and reference codes for data values; and one giving full references for each reference code. This data set is complete for binary/multiple components reported through 31 March 2013.",
-            "title": "BINARY MINOR PLANETS V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "BINARY MINOR PLANETS V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M08-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m08-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67PCHURYUMOV-M08-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67pchuryumov-m08-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-23T10:00:00.000 to 2014-10-24T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP008 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP008 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NIMBUS/NmHRIR1H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus High Resolution Infrared Radiometer Digital Swath Data L1, HDF5 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NIMBUS/NmHRIR1H.",
-            "issued": "1964-08-29",
-            "temporal": "1964-08-29T00:00:00Z/1970-01-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1969-12-23",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
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
-            "identifier": "C1696506410-NSIDC_ECS",
             "description": "The Nimbus High Resolution Infrared Radiometer Digital Swath Data L1, HDF data set (NmHRIR1H) consists of High Resolution Infrared Radiometer (HRIR) brightness temperatures obtained by the Nimbus 1, Nimbus 2, and Nimbus 3 satellites during 1964, 1966, and 1969. A correction has been applied to minimize seemingly random alignment errors that caused clouds edges and land features to appear jagged in the original 1960s data.",
-            "title": "Nimbus High Resolution Infrared Radiometer Digital Swath Data L1, HDF5 V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmHRIR1H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmHRIR1H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmHRIR1H.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmHRIR1H.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C191171281-NSIDC_ECS&m=-32.203125%211.125%211%211%210%210%2C2&q=NmHRIR1H",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C191171281-NSIDC_ECS&m=-32.203125%211.125%211%211%210%210%2C2&q=NmHRIR1H",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmHRIR1H/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmHRIR1H/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmHRIR1H",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmHRIR1H",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmHRIR1H",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmHRIR1H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1696506410-NSIDC_ECS",
+            "issued": "1964-08-29",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/NIMBUS/NmHRIR1H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1969-12-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1964-08-29T00:00:00Z/1970-01-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus High Resolution Infrared Radiometer Digital Swath Data L1, HDF5 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCDWD_L3_F2_NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-03-15. MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 2-day GeoTIFF. Version 6.1. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MCDWD_L3_F2_NRT.061.",
-            "issued": "2021-03-01",
-            "temporal": "2021-03-15T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "surface water",
-                "terrestrial hydrosphere",
-                "national geospatial data asset",
-                "earth science",
-                "ngda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dan Slayback",
                 "hasEmail": "mailto:floodmap@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
-            },
-            "identifier": "C2018695846-LANCEMODIS",
             "description": "The MODIS/Aqua+Terra Global Flood Product L3 Near Real Time (NRT) 250m  2-day GeoTIFF Product (MCDWD_L3_F2_NRT) (beta) provides maps of flooding globally.  The Global Flood product is provided over 3 compositing periods (1-day, 2-day, and 3-day) to minimize the impact of clouds and more rigorously identify flood water (the best composite will depend on the cloudiness for a particular event).  The MCDWD_L3_F2_NRT is 2-day product which is generated from current and previous day\u2019s data.\r\nThe beta version of the product will be updated. For more information, visit product page at:\r\nhttps://earthdata.nasa.gov/earth-observation-data/near-real-time/mcdwd-nrt",
-            "release-place": "MODAPS at NASA/GSFC",
-            "title": "MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 2-day GeoTIFF",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCDWD_L3_F2_NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCDWD_L3_F2_NRT.061",
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
-                    "downloadURL": "http://lance4.modaps.eosdis.nasa.gov/data_products/",
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page.",
+                    "downloadURL": "http://lance4.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt4.modaps.eosdis.nasa.gov/archive/allData/61/MCDWD_L3_F2_NRT",
-                    "description": "Direct access to the download site and directory hosting the MCDWD_L3_F2_NRT C6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MCDWD_L3_F2_NRT C6.1 NRT data set.",
+                    "downloadURL": "https://nrt4.modaps.eosdis.nasa.gov/archive/allData/61/MCDWD_L3_F2_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C2018695846-LANCEMODIS",
+            "issued": "2021-03-01",
+            "keyword": [
+                "surface water",
+                "terrestrial hydrosphere",
+                "national geospatial data asset",
+                "earth science",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCDWD_L3_F2_NRT.061",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2021-03-15T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "Aqua",
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua+Terra Global Flood Product L3 NRT 250m 2-day GeoTIFF"
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
+            "description": "These images display several of Jupiter's moons approved by the International Astronomical Union (IAU).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/thebe.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "OCIO-Fitara-178",
             "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "imagery",
                 "ganymede",
@@ -938769,265 +938781,254 @@
                 "thebe",
                 "moons"
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
-            "identifier": "OCIO-Fitara-178",
-            "description": "These images display several of Jupiter's moons approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Jovian System: Thebe",
-            "programCode": [
-                "026:007"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://planetarynames.wr.usgs.gov/images/thebe.pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Jovian System: Thebe"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-CAPS-5-DDR-SC-POTENTIAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of all of the spacecraft potential data generated from the Cassini Plasma Spectrometer (CAPS) electron spectrometer uncalibrated data. The data set currently contains the spacecraft potential data from the Electron Spectrometer (ELS_SCPOT).  The data is also contained in the electron moments file.  Data was generated using uncalibrated data from the electron spectrometer on Cassini CAPS. The uncalibrated data were acquired in a mix of CAPS operating modes beginning with the first instrument checkout in January 1999 and containing throughout the Cassini Tour and through the end of prime mission.  The data set covers the time period from 1999-004T03:07:47 UT until end of prime mission (July 2008).  In addition, it will cover data received during extended missions.  Sampling rates were variable and depended upon the downlink capabilities and other activities on-board. For times when CAPS is not producing data due to being turned off or due to communication issues, the data set will not contain data. Additionally, there will be no data during times when the calculations are not possible.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-caps-5-ddr-sc-potential-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "saturn",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-E%2FJ%2FS%2FSW-CAPS-5-DDR-SC-POTENTIAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-e-j-s-sw-caps-5-ddr-sc-potential-v1.0",
-            "description": "This data set consists of all of the spacecraft potential data generated from the Cassini Plasma Spectrometer (CAPS) electron spectrometer uncalibrated data. The data set currently contains the spacecraft potential data from the Electron Spectrometer (ELS_SCPOT).  The data is also contained in the electron moments file.  Data was generated using uncalibrated data from the electron spectrometer on Cassini CAPS. The uncalibrated data were acquired in a mix of CAPS operating modes beginning with the first instrument checkout in January 1999 and containing throughout the Cassini Tour and through the end of prime mission.  The data set covers the time period from 1999-004T03:07:47 UT until end of prime mission (July 2008).  In addition, it will cover data received during extended missions.  Sampling rates were variable and depended upon the downlink capabilities and other activities on-board. For times when CAPS is not producing data due to being turned off or due to communication issues, the data set will not contain data. Additionally, there will be no data during times when the calculations are not possible.",
-            "title": "CASSINI ORBITER SAT/SW CAPS DERIVED SC POTENTIAL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER SAT/SW CAPS DERIVED SC POTENTIAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PLS-4-SUMM-IET-V1.0",
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
-                "ida",
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This file is a listing of particle\nenergy spectra from the Galileo Plasma Instrument (PLS) during the Ida Flyby.\nDetector reponses from ion detetors 2P, 4P, and 6P, and from electron detector\n4E are available through the PDS as separate files.  The energy resolution,\nangular fields of view, and nominal geometric factors for the detectors are\nspecified in the Instrument Description file.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pls-4-summ-iet-v1.0_itxh-2khx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "ida",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-PLS-4-SUMM-IET-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-pls-4-summ-iet-v1.0_itxh-2khx",
-            "description": "This file is a listing of particle\nenergy spectra from the Galileo Plasma Instrument (PLS) during the Ida Flyby.\nDetector reponses from ion detetors 2P, 4P, and 6P, and from electron detector\n4E are available through the PDS as separate files.  The energy resolution,\nangular fields of view, and nominal geometric factors for the detectors are\nspecified in the Instrument Description file.",
-            "title": "GO ASTROID PLS SUMM IDA ET V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GO ASTROID PLS SUMM IDA ET V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR11-V1.0",
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
+            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR11) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 29, 30, and 31, 2008, during he Cassini Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr11-v1.0_itza-gr5f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "titan",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TIGR11-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tigr11-v1.0_itza-gr5f",
-            "description": "The Cassini Radio Science Titan Gravity Science Experiment (TIGR11) Raw Data Archive is a time-ordered collection of radio science raw data acquired on July 29, 30, and 31, 2008, during he Cassini Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TIGR11 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - TIGR11 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amgs_accel&version=1.0",
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
-                "mars global surveyor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This version of the MGS ACCEL bundle was created by the PDS Atmospheres node in 2015",
+            "identifier": "urn:nasa:pds:mgs_accel",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amgs_accel&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mgs_accel",
-            "description": "This version of the MGS ACCEL bundle was created by the PDS Atmospheres node in 2015",
-            "title": "MGS Accel Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS Accel Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RDT1MZVS0VG9",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge LVIS L1B Geolocated Return Energy Waveforms V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/RDT1MZVS0VG9.",
-            "issued": "2013-10-30",
-            "temporal": "2013-10-30T00:00:00Z/2017-09-20T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-20",
-            "keyword": [
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "J. Blair",
                 "hasEmail": "mailto:James.B.Blair@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1000000760-NSIDC_ECS",
             "description": "This data set contains return energy waveform data measured over Greenland, Alaska, and Antarctica by the NASA Land, Vegetation, and Ice Sensor (LVIS), an airborne lidar scanning laser altimeter. The data were collected as part of Operation IceBridge funded campaigns.",
-            "title": "IceBridge LVIS L1B Geolocated Return Energy Waveforms V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRDT1MZVS0VG9",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRDT1MZVS0VG9",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILVIS1B.002",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/ILVIS1B.002",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000760-NSIDC_ECS&m=-33.046875%218.15625%211%211%210%210%2C2&tl=1514139373%214%21%21&q=ILVIS1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000760-NSIDC_ECS&m=-33.046875%218.15625%211%211%210%210%2C2&tl=1514139373%214%21%21&q=ILVIS1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILVIS1B/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/ILVIS1B/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/RDT1MZVS0VG9",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/RDT1MZVS0VG9",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/RDT1MZVS0VG9",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/RDT1MZVS0VG9",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000760-NSIDC_ECS",
+            "issued": "2013-10-30",
+            "keyword": [
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/RDT1MZVS0VG9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-09-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2013-10-30T00:00:00Z/2017-09-20T23:59:59.999Z",
             "theme": [
                 "2013_GR_NASA",
                 "2014_AK_ARISE",
@@ -939035,283 +939036,259 @@
                 "2017_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge LVIS L1B Geolocated Return Energy Waveforms V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1166",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Post, W.M., and J. Pastor. 2013. LINKAGES: An Individual-based Forest Ecosystem Biogeochemistry Model. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1166",
-            "issued": "2013-06-17",
-            "temporal": "1973-01-01T00:00:00Z/2008-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-18",
-            "keyword": [
-                "atmospheric temperature",
-                "land surface",
-                "soils",
-                "biosphere",
-                "atmospheric radiation",
-                "atmosphere",
-                "earth science",
-                "vegetation",
-                "ecological dynamics",
-                "atmospheric water vapor",
-                "ecosystems",
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
-            "identifier": "C2768949725-ORNL_CLOUD",
             "description": "This model product contains the source codes for version 1 of the individual-based forest ecosystem biogeochemistry model LINKAGES and two subsequent versions as well as example input and output data. LINKAGES predicts long-term structure and dynamics of forest ecosystems as constrained by nitrogen availability, climate, and soil moisture. Model simulations compare favorably to field data from different geographic areas worldwide. LINKAGES, written in FORTRAN and provided in ASCII format, simulates birth, growth, and death of all trees greater than 1.43-cm dbh. Litter fall and decomposition are also simulated. Sunlight is the driving variable. Growing season degree days, soil water availability, and AET are calculated from precipitation, temperature, soil field moisture capacity, and wilting point. Decomposition and soil N availability are calculated from organic matter quantity and carbon chemistry, evapotranspiration, and degree of canopy closure. Light availability to each tree is a function of leaf biomass of taller trees. Degree days and availabilities of light and water constrain species reproduction. These variables plus soil N constrain tree growth and carbon accumulation in biomass. Tree death probability increases with age and slow growth. Leaf, root, and woody litter are returned to the soil at the end of each year to decay the following year. Climatic and forest data for eastern North America and New South Wales are provided as example model inputs. Modelers may use their own site data within any version of LINKAGES. Example model output is also provided.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LINKAGES: An Individual-based Forest Ecosystem Biogeochemistry Model",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1166",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1166",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/model_archive/LINKAGES/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/model_archive/LINKAGES/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/MODELS/guides/LINKAGES.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/MODELS/guides/LINKAGES.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1166",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1166",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/LINKAGES/comp/LINKAGES.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/LINKAGES/comp/LINKAGES.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/LINKAGES/comp/linkages_v2.2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/LINKAGES/comp/linkages_v2.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/LINKAGES/comp/linkages_v2_2_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/LINKAGES/comp/linkages_v2_2_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/LINKAGES/comp/ORNL_TM-9519.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/model_archive/LINKAGES/comp/ORNL_TM-9519.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/model-archive_logo_square.png",
+            "identifier": "C2768949725-ORNL_CLOUD",
+            "issued": "2013-06-17",
+            "keyword": [
+                "atmospheric temperature",
+                "land surface",
+                "soils",
+                "biosphere",
+                "atmospheric radiation",
+                "atmosphere",
+                "earth science",
+                "vegetation",
+                "ecological dynamics",
+                "atmospheric water vapor",
+                "ecosystems",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1166",
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
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1973-01-01T00:00:00Z/2008-12-31T23:59:59Z",
             "theme": [
                 "Model Archive",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LINKAGES: An Individual-based Forest Ecosystem Biogeochemistry Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L1/GEO/1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/AQUA/MODIS/L1/GEO/1.",
-            "issued": "2018-11-08",
-            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "ngda",
-                "earth science",
-                "sensor characteristics",
-                "spectral/engineering",
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
-            "identifier": "C2526537408-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Aqua MODIS Geolocation Product Data, version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL1%2FGEO%2F1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQUA%2FMODIS%2FL1%2FGEO%2F1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-1A/Aqua-MODIS/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-1A/Aqua-MODIS/",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L1/GEO/1",
-                    "description": "MODIS-Aqua L1 Geolocation Products Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L1 Geolocation Products Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L1/GEO/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2526537408-OB_DAAC",
+            "issued": "2018-11-08",
+            "keyword": [
+                "ngda",
+                "earth science",
+                "sensor characteristics",
+                "spectral/engineering",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQUA/MODIS/L1/GEO/1",
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
+            "title": "Aqua MODIS Geolocation Product Data, version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SR-UVIS-HSP-2%2F4-OCC-V2.0",
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
-                "cassini-huygens",
-                "s rings"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains derived \nradial occultation profiles of the rings of Saturn based on stellar \noccultation observations made with the Cassini UVIS instrument  \nbetween October 2004 and August 2017.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sr-uvis-hsp-2-4-occ-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "s rings"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SR-UVIS-HSP-2%2F4-OCC-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sr-uvis-hsp-2-4-occ-v2.0",
-            "description": "This data set contains derived \nradial occultation profiles of the rings of Saturn based on stellar \noccultation observations made with the Cassini UVIS instrument  \nbetween October 2004 and August 2017.",
-            "title": "CASSINI ORBITER SATURN UVIS STELLAR RING OCC 2004-2017",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI ORBITER SATURN UVIS STELLAR RING OCC 2004-2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/vab-building",
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
-                "3d model",
-                "vehicle assembly building",
-                "building",
-                "shuttle",
-                "vab"
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
-            "identifier": "NASA-418",
             "description": "The Vehicle Assembly Building (VAB) is one of the largest buildings in the world. It was originally built for assembly of Apollo/Saturn vehicles and was later modified to support Space Shuttle operations. Polygons: 3528 Vertices: 3388",
-            "title": "NASA 3D Models: Vehicle Assembly Building (VAB)",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -939319,40 +939296,46 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-418",
+            "issued": "2018-06-25",
+            "keyword": [
+                "3d model",
+                "vehicle assembly building",
+                "building",
+                "shuttle",
+                "vab"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/vab-building",
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
+            "title": "NASA 3D Models: Vehicle Assembly Building (VAB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000017-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "1992-06-14",
-            "temporal": "1992-06-14T00:00:00Z/2022-01-17T00:00:00Z",
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
-            "identifier": "C1000000017-CDDIS",
             "description": "Weekly station positions and velocity solutions in Software INdependent EXchange (SINEX) format derived from analysis of Global Navigation Satellite System (GNSS) data. These products are the generated by analysis centers in support of the International GNSS Service (IGS) and combined by the IGS reference frame coordinator to form the official IGS station position product (weekly).",
-            "title": "CDDIS_GNSS_products_positions",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -939361,61 +939344,92 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000017-CDDIS",
+            "issued": "1992-06-14",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000017-CDDIS.html",
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
+            "temporal": "1992-06-14T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_GNSS_products_positions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-LCS-5-ATMOS-OPTICAL-DEPTH-V1.0",
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
-                "viking",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Viking Lander camera images of the Sun were used to compute total normal atmospheric optical depth at the two landing sites over a period of about 900 Mars days. The data set contains 1044 measurements of optical depth and associated error estimates. The optical depths were derived from Sun diode images, which were obtained by the Lander cameras at a wavelength of 0.67 micrometers. Note that no images of Phobos were used in deriving this data set. Studies of diurnal, seasonal, and annual variations in optical depth, surface-based observations of great dust storms, and analyses of the contributions of ice haze and dust particles to the observed optical depth, have been carried out using these data. See COLBURN_ETAL_1989, POLLACK_ETAL_1977, and POLLACK_ETAL_1977 for further information on the derivation and interpretation of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-lcs-5-atmos-optical-depth-v1.0_iuqz-szqp",
+            "issued": "2021-05-21",
+            "keyword": [
+                "viking",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-LCS-5-ATMOS-OPTICAL-DEPTH-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-lcs-5-atmos-optical-depth-v1.0_iuqz-szqp",
-            "description": "Viking Lander camera images of the Sun were used to compute total normal atmospheric optical depth at the two landing sites over a period of about 900 Mars days. The data set contains 1044 measurements of optical depth and associated error estimates. The optical depths were derived from Sun diode images, which were obtained by the Lander cameras at a wavelength of 0.67 micrometers. Note that no images of Phobos were used in deriving this data set. Studies of diurnal, seasonal, and annual variations in optical depth, surface-based observations of great dust storms, and analyses of the contributions of ice haze and dust particles to the observed optical depth, have been carried out using these data. See COLBURN_ETAL_1989, POLLACK_ETAL_1977, and POLLACK_ETAL_1977 for further information on the derivation and interpretation of this data set.",
-            "title": "VL1/VL2 MARS LCS DERIVED ATMOSPHERIC OPTICAL DEPTH V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VL1/VL2 MARS LCS DERIVED ATMOSPHERIC OPTICAL DEPTH V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/iuth-vryh",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Genome-wide transcriptional profiling shows that reducing gravity levels in the International Space Station (ISS) causes important alterations in Drosophila gene expression. However simulation experiments on ground without space constraints show weaker effects than space environment. A global and integrative analysis using the gene expression dynamics inspector (GEDI) self-organizing maps reveals a subtle response of the transcriptome using different populations and microgravity and hypergravity simulation devices. These results suggest that in addition to behavioural responses that can be detected also at the gene expression level the transcriptome is finely tuned to normal gravity. The alteration of this constant parameter on Earth can have effects on gene expression that depends both on the environmental conditions and the ground based facility used to compensate the gravity vector. Alternative and commons effects of mechanical facilities like the Random Positioning Machine and a centrifuge and strong magnetic field ones like a cryogenically cooled superconductive magnet are discussed. We compare the effects over the gene expression profile of different gender/age Drosophila imagoes in 3-4 days-long experiments under altered gravity conditions into three GBF (Ground Based Facilities for micro/hyper- gravity simulation) using whole genome microarray platforms. Descriptions of different GBFs (treatments): LDC means Large Diameter Centrifuge. Samples can be placed under three conditions: inside LDC (at certain g level) at the LDC rotational control and at external 1g control (outside the LDC). RPM means Random Positioning Machine. Samples can be placed under two conditions: inside RPM (at nearly 0g Microgravity level) and at external 1g control (outside the RPM). At the magnet means INSIDE the Magnetic levitator (another GBF). Samples can be placed under four conditions: inside Magnet 0g* (at microgravity with magnetic field) inside Magnet at 1g* (internal control with magnetic field) or inside the magnet 2g* (at hypergravity with magnetic field) and at external 1g control (outside the magnet)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-34",
+                    "mediaType": "text/html",
+                    "title": "Environmental and simulation facility conditions can modulate a behavioral-driven altered gravity response of Drosophila imagoes transcriptome"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-34_iuth-vryh",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse33801-3",
                 "nucleic acid extraction protocol",
@@ -939437,642 +939451,629 @@
                 "array scanning protocol",
                 "p-gse33801-6"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/iuth-vryh",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-34_iuth-vryh",
-            "description": "Genome-wide transcriptional profiling shows that reducing gravity levels in the International Space Station (ISS) causes important alterations in Drosophila gene expression. However simulation experiments on ground without space constraints show weaker effects than space environment. A global and integrative analysis using the gene expression dynamics inspector (GEDI) self-organizing maps reveals a subtle response of the transcriptome using different populations and microgravity and hypergravity simulation devices. These results suggest that in addition to behavioural responses that can be detected also at the gene expression level the transcriptome is finely tuned to normal gravity. The alteration of this constant parameter on Earth can have effects on gene expression that depends both on the environmental conditions and the ground based facility used to compensate the gravity vector. Alternative and commons effects of mechanical facilities like the Random Positioning Machine and a centrifuge and strong magnetic field ones like a cryogenically cooled superconductive magnet are discussed. We compare the effects over the gene expression profile of different gender/age Drosophila imagoes in 3-4 days-long experiments under altered gravity conditions into three GBF (Ground Based Facilities for micro/hyper- gravity simulation) using whole genome microarray platforms. Descriptions of different GBFs (treatments): LDC means Large Diameter Centrifuge. Samples can be placed under three conditions: inside LDC (at certain g level) at the LDC rotational control and at external 1g control (outside the LDC). RPM means Random Positioning Machine. Samples can be placed under two conditions: inside RPM (at nearly 0g Microgravity level) and at external 1g control (outside the RPM). At the magnet means INSIDE the Magnetic levitator (another GBF). Samples can be placed under four conditions: inside Magnet 0g* (at microgravity with magnetic field) inside Magnet at 1g* (internal control with magnetic field) or inside the magnet 2g* (at hypergravity with magnetic field) and at external 1g control (outside the magnet)",
-            "title": "Environmental and simulation facility conditions can modulate a behavioral-driven altered gravity response of Drosophila imagoes transcriptome",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-34",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Environmental and simulation facility conditions can modulate a behavioral-driven altered gravity response of Drosophila imagoes transcriptome"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Environmental and simulation facility conditions can modulate a behavioral-driven altered gravity response of Drosophila imagoes transcriptome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/EWING/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/EWING/DATA001.",
-            "issued": "2001-08-06",
-            "temporal": "2001-08-06T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "oceans",
-                "salinity/density",
-                "ocean optics",
-                "ocean chemistry",
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
-            "identifier": "C1633360233-OB_DAAC",
             "description": "Measurements made near South Africa in 2001.",
-            "title": "Measurements made near South Africa in 2001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FEWING%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FEWING%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ewing/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ewing/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360233-OB_DAAC",
+            "issued": "2001-08-06",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "salinity/density",
+                "ocean optics",
+                "ocean chemistry",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/EWING/DATA001",
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
+            "temporal": "2001-08-06T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements made near South Africa in 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3O3M.005",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL3O3M.005. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-03T00:00:00Z/2018-01-24T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "air quality",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Scott Gluck",
                 "hasEmail": "mailto:scott.gluck@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1536988712-LARC",
             "description": "TL3O3M_5 is the Tropospheric Emission Spectrometer (TES)/Aura Level 3 Ozone (O3) Monthly Gridded Version 5 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. This product consisted of daily atmospheric temperature and volume mixing ratio (VMR) for the atmospheric species, ozone, which were provided at 2 degree latitude X 4 degree longitude spatial grids and at a subset of TES standard pressure levels. The TES Science Data Processing L3 subsystem interpolated the L2 atmospheric profiles collected in a Global Survey onto a global grid uniform in latitude and longitude to provide a 3-D representation of the distribution of atmospheric gasses. Daily and monthly averages of L2 profiles and browse images are available. The L3 standard data products were composed of L3 HDF-EOS grid data. A separate product file was produced for each different atmospheric species. TES obtained data in two basic observation modes: Limb or Nadir. The product may have contained, in separate folders, limb data, nadir data, or both folders could have been present. \r\rSpecific to L3 processing were the terms Daily and Monthly, representing the approximate time coverage of the L3 products. However, the input data granules to the L3 process were complete Global Surveys; in other words a Global Survey was not split in relation to time when they were input to the L3 processes even if they exceed the usual understood meanings of a day or month. More specifically, Daily L3 products represented a single Global Survey (approximately 26 hours) and Monthly L3 products represented Global Surveys that were initiated within that calendar month. The data granules defined for L3 standard products were daily and monthly. Details of the format of this product can be found in the TES Data Products Specifications (DPS).",
-            "title": "TES/Aura L3 Ozone Monthly Gridded V005",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3O3M.005",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL3O3M.005",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Data_Users_Guide.pdf",
-                    "description": "TES Level 3 (L3) Data/Plot User\u2019s Guide Version 1.0 December 17, 2007",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 3 (L3) Data/Plot User\u2019s Guide Version 1.0 December 17, 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_L3_Data_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L3monthly.cgi",
-                    "description": "Report of TES Level 3 Monthly Data Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 3 Monthly Data Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L3monthly.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3O3M.005",
-                    "description": "DOI data set landing page for TL3O3M_5",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL3O3M_5",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL3O3M.005",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3O3M.005/contents.html",
-                    "description": "OPeNDAP data access for TL3O3M_5",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL3O3M_5",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL3O3M.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536988712-LARC",
-                    "description": "Earthdata Search for TL3O3M_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL3O3M_5 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1536988712-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3O3M.005/",
-                    "description": "ASDC Direct Data Download for TL3O3M_5",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL3O3M_5",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL3O3M.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
+            "identifier": "C1536988712-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL3O3M.005",
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
+            "temporal": "2004-09-03T00:00:00Z/2018-01-24T23:59:59Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L3 Ozone Monthly Gridded V005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/99LHDR3NUM47",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMAP Enhanced L1C Radiometer Half-Orbit 9 km EASE-Grid Brightness Temperatures V004. Version 004. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/99LHDR3NUM47.",
-            "issued": "2015-03-31",
-            "temporal": "2015-03-31T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "microwave"
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
-            "identifier": "C2938663435-NSIDC_CPRD",
             "description": "This enhanced Level-1C (L1C) product contains calibrated and geolocated brightness temperatures acquired by the Soil Moisture Active Passive (SMAP) radiometer during 6:00 a.m. descending and 6:00 p.m. ascending half-orbit passes. This product is derived from SMAP Level-1B (L1B) interpolated antenna temperatures. Backus-Gilbert optimal interpolation techniques are used to extract enhanced information from SMAP antenna temperatures before they are converted to brightness temperatures. The resulting brightness temperatures are posted to an Earth-fixed, 9 km Equal-Area Scalable Earth Grid, Version 2.0 (EASE-Grid 2.0) in three projections: global cylindrical, Northern Hemisphere azimuthal, and Southern Hemisphere azimuthal.",
-            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
-            "title": "SMAP Enhanced L1C Radiometer Half-Orbit 9 km EASE-Grid Brightness Temperatures V004",
-            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-184,-74,162,86&l=SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V_QA(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V_QA(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H_QA(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H_QA(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V_RFI(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V_RFI(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H_RFI(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H_RFI(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V,SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V,SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H,SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F99LHDR3NUM47",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F99LHDR3NUM47",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL1CTB_E+V004",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SPL1CTB_E+V004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938663435-NSIDC_CPRD",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2938663435-NSIDC_CPRD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-184%2C-74%2C162%2C86&l=SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V_QA%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V_QA%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H_QA%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H_QA%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V_RFI%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V_RFI%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H_RFI%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H_RFI%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
-                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
                     "@type": "dcat:Distribution",
+                    "description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+                    "downloadURL": "https://worldview.earthdata.nasa.gov/?v=-184%2C-74%2C162%2C86&l=SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V_QA%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V_QA%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H_QA%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H_QA%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V_RFI%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V_RFI%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H_RFI%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H_RFI%28disabled%3D3%29%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H%2CSMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H%2CCoastlines_15m%2CMODIS_Terra_CorrectedReflectance_TrueColor",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/99LHDR3NUM47",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/99LHDR3NUM47",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/99LHDR3NUM47",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/99LHDR3NUM47",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "This application allows you to interactively browse global satellite imagery within hours of it being acquired. You can also save it, share it, and download the underlying data.",
+            "graphic-preview-file": "https://worldview.earthdata.nasa.gov/?v=-184,-74,162,86&l=SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V_QA(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V_QA(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H_QA(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H_QA(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V_RFI(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V_RFI(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H_RFI(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H_RFI(disabled=3),SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_V,SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_V,SMAP_L1_Passive_Enhanced_Brightness_Temp_Fore_H,SMAP_L1_Passive_Enhanced_Brightness_Temp_Aft_H,Coastlines_15m,MODIS_Terra_CorrectedReflectance_TrueColor",
+            "identifier": "C2938663435-NSIDC_CPRD",
+            "issued": "2015-03-31",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/99LHDR3NUM47",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-08",
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
+            "title": "SMAP Enhanced L1C Radiometer Half-Orbit 9 km EASE-Grid Brightness Temperatures V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0500-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-22T12:35:10.000 to 2014-12-22T20:12:10.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0500-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0500-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0500-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-22T12:35:10.000 to 2014-12-22T20:12:10.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0500 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0500 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CR5-V1.0",
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
+            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR5 (Cruise 5) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cr5-v1.0_iuxm-med6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CR5-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cr5-v1.0_iuxm-med6",
-            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR5 (Cruise 5) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL\n                           CONSERT 2 CR5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL\n                           CONSERT 2 CR5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-PTOLEMY-3-RBD-V1.0",
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
+            "description": "This archive contains calibrated data from the PTOLEMY instrument onboard ROSETTA Lander, acquired during the RBD mission phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the PTOLEMY experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-ptolemy-3-rbd-v1.0_iuxx-8xqv",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-C-PTOLEMY-3-RBD-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-c-ptolemy-3-rbd-v1.0_iuxx-8xqv",
-            "description": "This archive contains calibrated data from the PTOLEMY instrument onboard ROSETTA Lander, acquired during the RBD mission phase. The primary target is the comet 67P/CHURYUMOV-GERASIMENKO. It also contains documentation which describes the PTOLEMY experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER 67P PTOLEMY 3 RBD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-LANDER 67P PTOLEMY 3 RBD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-ALTITUDE-V1.0",
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
-                "mars global surveyor",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-altitude-v1.0_iuzu-7ft6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-ACCEL-5-ALTITUDE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-accel-5-altitude-v1.0_iuzu-7ft6",
-            "description": "not applicable",
-            "title": "MGS ALTITUDE DATA RECORDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MGS ALTITUDE DATA RECORDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/39YO5T544XCC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge DMS L3 Photogrammetric DEM V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/39YO5T544XCC.",
-            "issued": "2011-03-18",
-            "temporal": "2011-03-18T00:00:00Z/2013-11-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-26",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ryan Dotson",
                 "hasEmail": "mailto:rdotson@fireballit.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1000000541-NSIDC_ECS",
             "description": "The IceBridge DMS L3 Photogrammetric DEM (IODMS3) data set contains gridded digital elevation models and orthorectified images of Greenland and Antarctica derived from the Digital Mapping System (DMS). The data were collected as part of Operation IceBridge funded campaigns.",
-            "title": "IceBridge DMS L3 Photogrammetric DEM V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F39YO5T544XCC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F39YO5T544XCC",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODMS3.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODMS3.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000541-NSIDC_ECS&m=-31.921875%2127.28125%211%211%210%210%2C2&q=IODMS3",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000541-NSIDC_ECS&m=-31.921875%2127.28125%211%211%210%210%2C2&q=IODMS3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODMS3/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODMS3/versions/1/",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODMS3.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODMS3.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000541-NSIDC_ECS&m=-31.921875%2127.28125%211%211%210%210%2C2&q=IODMS3",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000541-NSIDC_ECS&m=-31.921875%2127.28125%211%211%210%210%2C2&q=IODMS3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODMS3/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODMS3/versions/1/",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODMS3.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IODMS3.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000541-NSIDC_ECS&m=-31.921875%2127.28125%211%211%210%210%2C2&q=IODMS3",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000541-NSIDC_ECS&m=-31.921875%2127.28125%211%211%210%210%2C2&q=IODMS3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODMS3/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IODMS3/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/39YO5T544XCC",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/39YO5T544XCC",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/39YO5T544XCC",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/39YO5T544XCC",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000000541-NSIDC_ECS",
+            "issued": "2011-03-18",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/39YO5T544XCC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-11-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 60.0 180.0 90.0",
+            "temporal": "2011-03-18T00:00:00Z/2013-11-26T23:59:59.999Z",
             "theme": [
                 "2009_AN_NASA",
                 "2010_AN_NASA",
@@ -940091,56 +940092,69 @@
                 "2016_GR_NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge DMS L3 Photogrammetric DEM V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-ESC1-67P-V1.0",
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
+            "description": "This data set contains Spectroscopic, Continuum, and Geometry level 3 data, in the form of table files, taken during the COMET ESCORT 1 phase of the Rosetta mission by the MIRO instrument. The primary target of this phase of mission is 67P.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-esc1-67p-v1.0_iv3v-umib",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIRO-3-ESC1-67P-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-miro-3-esc1-67p-v1.0_iv3v-umib",
-            "description": "This data set contains Spectroscopic, Continuum, and Geometry level 3 data, in the form of table files, taken during the COMET ESCORT 1 phase of the Rosetta mission by the MIRO instrument. The primary target of this phase of mission is 67P.",
-            "title": "ROSETTA-ORBITER 67P MIRO 3 ESC1 67P V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIRO 3 ESC1 67P V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/iv6h-anhp",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Traveling to nearby extraterrestrial objects having a reduced gravity level (partial gravity) compared to Earth's gravity is becoming a realistic objective for space agencies. The use of plants as part of life support systems will require a better understanding of the interactions among plant growth responses including tropisms, under partial gravity conditions. Here, we present results from our latest space experiments on the ISS, in which seeds of Arabidopsis thaliana were germinated, and seedlings grew for six days under different gravity levels, namely micro-g, several intermediate partial-g levels, and 1g, and were subjected to irradiation with blue light for the last 48 hours. RNA was extracted from 20 samples for subsequent RNAseq analysis. Transcriptomic analysis was performed using the HISAT2-Stringtie-DESeq pipeline. Differentially expressed genes were further characterized for global responses using the GEDI tool, gene networks and for Gene Ontology (GO) enrichment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-251",
+                    "mediaType": "text/html",
+                    "title": "RNAseq analysis of the response of Arabidopsis thaliana to fractional gravity under blue-light stimulation during spaceflight"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-251_iv6h-anhp",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "genelab rnaseq data processing protocol",
                 "spaceflight",
@@ -940152,803 +940166,762 @@
                 "library construction",
                 "sequence analysis data transformation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/iv6h-anhp",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-251_iv6h-anhp",
-            "description": "Traveling to nearby extraterrestrial objects having a reduced gravity level (partial gravity) compared to Earth's gravity is becoming a realistic objective for space agencies. The use of plants as part of life support systems will require a better understanding of the interactions among plant growth responses including tropisms, under partial gravity conditions. Here, we present results from our latest space experiments on the ISS, in which seeds of Arabidopsis thaliana were germinated, and seedlings grew for six days under different gravity levels, namely micro-g, several intermediate partial-g levels, and 1g, and were subjected to irradiation with blue light for the last 48 hours. RNA was extracted from 20 samples for subsequent RNAseq analysis. Transcriptomic analysis was performed using the HISAT2-Stringtie-DESeq pipeline. Differentially expressed genes were further characterized for global responses using the GEDI tool, gene networks and for Gene Ontology (GO) enrichment.",
-            "title": "RNAseq analysis of the response of Arabidopsis thaliana to fractional gravity under blue-light stimulation during spaceflight",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-251",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "RNAseq analysis of the response of Arabidopsis thaliana to fractional gravity under blue-light stimulation during spaceflight"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "RNAseq analysis of the response of Arabidopsis thaliana to fractional gravity under blue-light stimulation during spaceflight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Aerosol_AircraftInSitu_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-08-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Aerosol_AircraftInSitu_DC8_Data_1.",
-            "issued": "1997-10-09",
-            "temporal": "1997-10-07T00:00:00Z/1997-11-12T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1997-11-12",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science",
-                "aerosols",
-                "air quality"
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
-            "identifier": "C2662353694-LARC_ASDC",
             "description": "SONEX_Aerosol_AircraftInSitu_DC8_Data_1 is the in-situ aerosol data collected onboard the DC-8 aircraft during the SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) suborbital campaign. Data was collected via in-situ instrumentation, including multiple condensation nuclei counters (CNCs), ACIR (Aerosol/Cloud Particle Impactor/Replicator), FSSP, PCASP, and SAGA. Data collection for this product is complete.\r\nThe SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) was an international, multi-organizational mission that took place in October-November 1997. NASA was the US sponsor of SONEX that partnered with POLINAT-2 (Pollution from Aircraft Emissions in the North Atlantic Flight Corridor) funded by the German DLR (Deutsches Zentrum f\u00fcr Luft- und Raumfahrt) or German Aerospace Agency. NASA flew the DC-8 aircraft out of NASA/Ames Research Center. DLR operated an instrumented Falcon 20 aircraft. The staging locations for NAFC sampling were primarily Bangor, Maine (US), and Shannon, Ireland. Subsonic aircraft emissions impact several aspects of atmospheric composition: nitrogen oxides (NOx), CO, and hydrocarbons from emissions can perturb upper tropospheric/lower stratospheric (UT/LS) ozone; water vapor, soot, and sulfur oxides (SOx) emitted by aircraft may perturb clouds and aerosols, changing UT/LS radiative forcing and global temperature.\r\nIn SONEX and POLINAT, flights were conducted in the vicinity of the North Atlantic Flight Coordinator (NAFC) to observe the impact of aircraft emissions on NOx and ozone (O3). The DC-8 aircraft payload (Singh et al., 1999) primarily measured in-situ CO, CO2, hydrocarbons/halocarbons, O3, aerosols (Dibb et al., 2000), OH/HO2, water vapor, nitric acid (Talbot et al., 1999), photolysis rates, temperature, pressure, winds, NOx, and NOy.\r\nThree sampling approaches were implemented during SONEX. First, special meteorological (Fuelberg et al., 2000) were developed to allow targeted sampling for air parcels affected by aircraft emissions and various meteorological events, e.g., convection, lightning (Jeker et al., 2000), stratospheric intrusions (Cho et al., 2000). Second, because the NAFC had not been extensively sampled in the past, it was important for SONEX to characterize the climatology of trace species like CN (Wang et al., 2000), NOx and NOy (Koike et al., 2000). Third, tracers (Simpson et al., 2000; Thompson et al., 1999) and model sensitivity studies (Meijer et al., 2000) were employed for Air Mass Identification. This sampling strategy answered the following questions: Where and when are air masses found with the greatest aircraft influence? When and where was stratospheric air sampled? SONEX showed a substantial impact of aircraft emissions on UT/LS NOx and CN in the vicinity of fresh aircraft emissions. However, during October-November 1997 over the NAFC, UT/LS NOx was dominated by surface emissions redistributed by convection and augmented by lightning.",
-            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) DC-8 In-Situ Aerosol Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_Aerosol_AircraftInSitu_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSONEX_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/SONEX_Aerosol_AircraftInSitu_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SONEX_Aerosol_AircraftInSitu_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SONEX_Aerosol_AircraftInSitu_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SONEX/SONEX_Aerosol_AircraftInSitu_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2662353694-LARC_ASDC",
+            "issued": "1997-10-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science",
+                "aerosols",
+                "air quality"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SONEX_Aerosol_AircraftInSitu_DC8_Data_1",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>19.89 -180.0 19.89 49.34 69.127 49.34 69.127 -180.0 19.89 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1997-10-07T00:00:00Z/1997-11-12T23:59:59.999Z",
             "theme": [
                 "SONEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SASS (Subsonics Assessment) Ozone and NOx Experiment (SONEX) DC-8 In-Situ Aerosol Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0856-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-24T11:42:40.000 to 2015-06-24T13:49:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0856-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0856-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0856-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-24T11:42:40.000 to 2015-06-24T13:49:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0856 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0856 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Atno-centaur_diam-albedo-density&version=1.0",
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
-                "none"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set is a compilation of published diameters, albedos, and densities for\nTransneptunian Objects (TNOs) and Centaurs.  A total of 194 objects are listed, many\nwith more than one entry.  This version covers published values through 31 March\n2018.",
+            "identifier": "urn:nasa:pds:tno-centaur_diam-albedo-density",
+            "issued": "2021-05-21",
+            "keyword": [
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Atno-centaur_diam-albedo-density&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:tno-centaur_diam-albedo-density",
-            "description": "This data set is a compilation of published diameters, albedos, and densities for\nTransneptunian Objects (TNOs) and Centaurs.  A total of 194 objects are listed, many\nwith more than one entry.  This version covers published values through 31 March\n2018.",
-            "title": "TNO AND CENTAUR DIAMETERS, ALBEDOS, AND DENSITIES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "TNO AND CENTAUR DIAMETERS, ALBEDOS, AND DENSITIES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9-M-RSS-5-ELEDENPROFILES-V1.0",
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
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains 114 ionospheric electron density profiles (EDS files) derived from Mariner 9 radio occultation data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-m-rss-5-eledenprofiles-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9-M-RSS-5-ELEDENPROFILES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-m-rss-5-eledenprofiles-v1.0",
-            "description": "This dataset contains 114 ionospheric electron density profiles (EDS files) derived from Mariner 9 radio occultation data.",
-            "title": "MARINER 9 RSS DERIVED IONSPHERIC ELECTRON DENSITY PROFILES",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARINER 9 RSS DERIVED IONSPHERIC ELECTRON DENSITY PROFILES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-5-XYZ-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-5-xyz-ops-v1.0_ivap-ye2u",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-NAVCAM-5-XYZ-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-navcam-5-xyz-ops-v1.0_ivap-ye2u",
-            "description": "not applicable",
-            "title": "MER 2 MARS NAVIGATION CAMERA XYZ RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS NAVIGATION CAMERA XYZ RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP02IMG_NRT.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "VCST Team. 2021-12-31. VIIRS/NPP Imagery Resolution 6-Min L1B Swath 375m NRT. Version 2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, LANCEMODIS. https://doi.org/10.5067/VIIRS/VNP02IMG_NRT.002. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/viirs-nrt.",
-            "issued": "2021-12-15",
-            "temporal": "2021-12-15T00:00:00Z/2024-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths"
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
-            "identifier": "C2185504759-LANCEMODIS",
-            "description": "The VIIRS/NPP Imagery Resolution 6-Min L1B Swath  375m Near REal Time (NRT), short-name VNP02IMG_NRT is among the VIIRS Level 1 and Level 2 swath products that are generated from the processing of 6 minutes of VIIRS data acquired during the S-NPP satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 micrometer to 11.45 micrometer. The VNP02IMG product is comprised of 5 bands that are sensitive to visible, near-infrared (NIR), and thermal wavelengths. The spatial resolution of the instrument at viewing nadir is approximately 375 m for the Imagery bands, and 750m for the DNB and the Moderate-resolution Bands.\r\n\r\nThe spatial resolution of the instrument at viewing nadir is approximately 750 m for the Moderate-resolution and Day/Night Bands, and 375 m for the Imagery bands.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "VCST Team",
-            "title": "VIIRS/NPP Imagery Resolution 6-Min L1B Swath 375m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/NPP Imagery Resolution 6-Min L1B Swath  375m Near REal Time (NRT), short-name VNP02IMG_NRT is among the VIIRS Level 1 and Level 2 swath products that are generated from the processing of 6 minutes of VIIRS data acquired during the S-NPP satellite overpass. The VIIRS sensor has 5 high-resolution imagery channels (I-bands) that have 32 detectors (32 rows of pixels per scan), with twice the resolution of the M-bands and the DNB, that span the wavelengths from 0.640 micrometer to 11.45 micrometer. The VNP02IMG product is comprised of 5 bands that are sensitive to visible, near-infrared (NIR), and thermal wavelengths. The spatial resolution of the instrument at viewing nadir is approximately 375 m for the Imagery bands, and 750m for the DNB and the Moderate-resolution Bands.\r\n\r\nThe spatial resolution of the instrument at viewing nadir is approximately 750 m for the Moderate-resolution and Day/Night Bands, and 375 m for the Imagery bands.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP02IMG_NRT.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP02IMG_NRT.002",
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
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP02IMG_NRT",
-                    "description": "Direct access to the download site and directory hosting the VNP02IMG_NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the VNP02IMG_NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/5200/VNP02IMG_NRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2185504759-LANCEMODIS",
+            "issued": "2021-12-15",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP02IMG_NRT.002",
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
+            "title": "VIIRS/NPP Imagery Resolution 6-Min L1B Swath 375m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR00-RFI01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yan Soldo, Paolo De Matthaeis, David Levine. 2018-01-30. Aquarius RFI Products. Version 1. Aquarius RFI Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, Md., 20771. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Goddard Space Flight Center (GSFC). https://doi.org/10.5067/AQR00-RFI01. http://podaac.jpl.nasa.gov/salinity/data.html. Yan Soldo, Paolo De Matthaeis, David Levine, NASA Goddard Space Flight Center (GSFC), 2018-01-30, Aquarius Radio Frequency Interference (RFI) Ancillary Dataset V1.0, http://podaac.jpl.nasa.gov/salinity/data.html.",
-            "issued": "2017-12-19",
-            "temporal": "2011-09-01T00:00:00Z/2015-06-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-19",
-            "keyword": [
-                "oceans",
-                "salinity/density",
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
-            "identifier": "C2617176765-POCLOUD",
-            "description": "Aquarius ancillary Radio Frequency Interference (RFI) product used in ADPS mission processing contains monthly-averaged Radio Frequency Interference (RFI) data for ascending/descending passes as detected by the Aquarius radiometers and scatterometer.  The data is available for ascending (northward) and descending (southward) passes of the satellite only and ascending/descending passes combined.\n\nThe values stored in this product are the percentage of radiometer and scatterometer measurements identified as corrupted by interference by the RFI detection algorithms [1,2] within each data point, averaged over one month. An additional RFI flag [3] is used to identify locations where the measured brightness temperature over land exceeds the expected limits of surface emissivity. This flag is not used to remove samples from further processing, but, in generating the radiometer RFI data, 100% RFI is assigned to points where this flag is raised. \n\nThis product can be used to reproduce the RFI maps available on the Aquarius website at University of Maine (https://aquarius.umaine.edu/cgi/gal_radiometer.htm for the radiometer, and https://aquarius.umaine.edu/cgi/gal_scatterometer.htm for the scatterometer), by plotting the variables Rad_RFI_percent_AscDes_AllBeams and Scat_RFI_percent_AscDes_AllBeams on the latitude/longitude grid. Additionally, the user can generate maps by using only a particular beam or only  ascending passes, for example. All combinations of beams and ascending/descending passes are possible.\n\nThis product contains information about RFI, but it is also relevant for the retrieved Sea Surface Salinity (SSS). Over the ocean, the RFI percentage in this product corresponds to the amount of raw measurements  discarded due to RFI contamination before SSS retrieval. Therefore, maps of the RFI percentage can give the user an indication of where RFI is more likely to have affected the quality of SSS retrievals, for a particular month, or for a series of months.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, Md., 20771",
-            "series-name": "Aquarius RFI Products",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Yan Soldo, Paolo De Matthaeis, David Levine",
-            "title": "Aquarius Radio Frequency Interference (RFI) Ancillary Dataset V1.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_ANCILLARY_RFI_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius ancillary Radio Frequency Interference (RFI) product used in ADPS mission processing contains monthly-averaged Radio Frequency Interference (RFI) data for ascending/descending passes as detected by the Aquarius radiometers and scatterometer.  The data is available for ascending (northward) and descending (southward) passes of the satellite only and ascending/descending passes combined.\n\nThe values stored in this product are the percentage of radiometer and scatterometer measurements identified as corrupted by interference by the RFI detection algorithms [1,2] within each data point, averaged over one month. An additional RFI flag [3] is used to identify locations where the measured brightness temperature over land exceeds the expected limits of surface emissivity. This flag is not used to remove samples from further processing, but, in generating the radiometer RFI data, 100% RFI is assigned to points where this flag is raised. \n\nThis product can be used to reproduce the RFI maps available on the Aquarius website at University of Maine (https://aquarius.umaine.edu/cgi/gal_radiometer.htm for the radiometer, and https://aquarius.umaine.edu/cgi/gal_scatterometer.htm for the scatterometer), by plotting the variables Rad_RFI_percent_AscDes_AllBeams and Scat_RFI_percent_AscDes_AllBeams on the latitude/longitude grid. Additionally, the user can generate maps by using only a particular beam or only  ascending passes, for example. All combinations of beams and ascending/descending passes are possible.\n\nThis product contains information about RFI, but it is also relevant for the retrieved Sea Surface Salinity (SSS). Over the ocean, the RFI percentage in this product corresponds to the amount of raw measurements  discarded due to RFI contamination before SSS retrieval. Therefore, maps of the RFI percentage can give the user an indication of where RFI is more likely to have affected the quality of SSS retrievals, for a particular month, or for a series of months.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR00-RFI01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR00-RFI01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_ANCILLARY_RFI_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_ANCILLARY_RFI_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
-                    "description": "Aquarius RFI Product User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius RFI Product User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aquarius.oceansciences.org/",
-                    "description": "NASA Aquarius/SAC-D mission website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Aquarius/SAC-D mission website",
+                    "downloadURL": "https://aquarius.oceansciences.org/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617176765-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2617176765-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617176765-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2617176765-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/sw/idl/aquarius_IDL_readers.tgz",
-                    "description": "Interactive Data Language read software",
                     "@type": "dcat:Distribution",
+                    "description": "Interactive Data Language read software",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/sw/idl/aquarius_IDL_readers.tgz",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/sw/matlab/aquarius_matlab_readers.tgz",
-                    "description": "MATLAB read software",
                     "@type": "dcat:Distribution",
+                    "description": "MATLAB read software",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/sw/matlab/aquarius_matlab_readers.tgz",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_ANCILLARY_RFI_V1.jpg",
+            "identifier": "C2617176765-POCLOUD",
+            "issued": "2017-12-19",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR00-RFI01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, Md., 20771",
+            "series-name": "Aquarius RFI Products",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-09-01T00:00:00Z/2015-06-01T23:59:59.999Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Radio Frequency Interference (RFI) Ancillary Dataset V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67PCHURYUMOV-M19-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67pchuryumov-m19-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "zeta cas",
                 "vega",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC3-67PCHURYUMOV-M19-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc3-67pchuryumov-m19-v1.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 3 phase of the Rosetta mission, covering the period from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP019 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC3-MTP019 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/730/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-05-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
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
-            "identifier": "DASHLINK_730",
             "description": "Actuator systems are employed widely in aerospace, transportation and industrial processes to provide power to critical loads, such as aircraft control surfaces. They must operate reliably and accurately in order for the vehicle / process to complete successfully its designated mission. Incipient actuator failure conditions may severely endanger the operational integrity of the vehicle / process and compromise its mission. The ability to maintain a stable and credible operation, even in the presence of incipient failures, is of paramount importance to accomplish \u201cmust achieve\u201d mission objectives. This paper introduces a novel methodology for the fault-tolerant design of critical subsystems, such as an ElectroMechanical Actuator (EMA), that takes advantage of on-line, real-time estimates of the Remaining Useful Life (RUL) or Time-to-Failure (TTF) of a failing component and reconfigures the available control authority by trading off system performance with control activity. The primary goal is to complete critical mission objectives within a time window dictated by prognostic algorithms so that the fault mode is accommodated and an acceptable level of performance maintained for the duration of the mission. The proposed fault-tolerant control design is mathematically rigorous, generic and applicable to a variety of application domains. An EMA is used to illustrate the efficacy of the proposed approach.",
-            "title": "Prognostics Enhanced Reconfigurable Control of Electro-Mechanical Actuators",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_PHM_ReconfigurableControl.pdf",
-                    "description": "2009_PHM_ReconfigurableControl.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2009_PHM_ReconfigurableControl.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_PHM_ReconfigurableControl.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2009_PHM_ReconfigurableControl.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_730",
+            "issued": "2013-05-09",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/730/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Prognostics Enhanced Reconfigurable Control of Electro-Mechanical Actuators"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/3Z173KIE2TPD",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2I1NXASM. Version 5.12.4. MERRA-2 inst1_2d_asm_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Single-Level Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/3Z173KIE2TPD. https://disc.gsfc.nasa.gov/datacollection/M2I1NXASM_5.12.4.html. Digital Science Data.",
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
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "clouds",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude",
-                "earth science",
-                "land surface",
-                "surface thermal properties",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812820-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2I1NXASM (or  inst1_2d_asm_Nx) is an instantaneous 2-dimensional hourly data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilations of meteorological diagnostic parameters at the single levels, such as temperature at 2-meter and 10-meter; wind components at 2-meter, 10-meter, and 50-meter; surface pressure, and total precipitable water.  The timestamp of a data field is on each hour starting from 00:00 UTC, e.g.:  00:00, 01:00, \u2026 , 23:00 UTC. \n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2I1NXASM",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "MERRA-2 inst1_2d_asm_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2I1NXASM) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3Z173KIE2TPD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3Z173KIE2TPD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I1NXASM_5.12.4.png",
-                    "description": "M2I1NXASM variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2I1NXASM variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2I1NXASM_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2I1NXASM_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2I1NXASM_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I1NXASM.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I1NXASM.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2I1NXASM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2I1NXASM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2I1NXASM.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2I1NXASM.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2I1NXASM.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2I1NXASM.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2I1NXASM.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS) ",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS) ",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2I1NXASM.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I1NXASM.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I1NXASM.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#variableFacets=dataProductPlatformInstrument%3AMERRA-2%20Model%3B",
+            "identifier": "C1276812820-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "clouds",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude",
+                "earth science",
+                "land surface",
+                "surface thermal properties",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/3Z173KIE2TPD",
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
+            "series-name": "M2I1NXASM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 inst1_2d_asm_Nx: 2d,1-Hourly,Instantaneous,Single-Level,Assimilation,Single-Level Diagnostics 0.625 x 0.5 degree V5.12.4 (M2I1NXASM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA1002",
             "citation": "Marcel Dobber. 2007-09-20. OML1BRUG. Version 003. OMI/Aura Level 1B UV Global Geolocated Earthshine Radiances 1-orbit L2 Swath 13x24 km V003. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA1002. https://disc.gsfc.nasa.gov/datacollection/OML1BRUG_003.html. Digital Science Data.",
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
-                "spectral/engineering",
-                "ultraviolet wavelengths",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JEROME ALFRED",
                 "hasEmail": "mailto:jerome.m.alfred@nasa.gov"
             },
+            "creator": "Marcel Dobber",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239966738-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Aura Ozone Monitoring Instrument (OMI) Level-1B (L1B) Geo-located Earth View UV Radiance, Global-Mode (OML1BRUG) Version-3 product contains geo-located Earth view spectral radiances from the UV detectors in the wavelength range of 264 to 383 nm conducted in the global measurement mode. In the standard global measurement mode, OMI observes 60 ground pixels (13 km x 24 km at nadir) across the swath for each of the 557 channels of UV2 (307-383 nm) and 30 ground pixels (13 km x 48 km at nadir) for the 159 channels of UV1 (264-311 nm). Each file contains data from the day lit portion of an orbit (~53 minutes) and is roughly 180 MB in size. There are approximately 14 orbits per day. Once a month, in one orbit, OMI performs dark measurements, it does not perform radiance measurements. In addition, OMI performs spatial zoom measurements one day per month. For that day, this product also contains UV2 measurements that are rebinned from the spatial zoom-in measurements. In original spatial zoom mode the nadir ground pixel size is 13 x 12 km and measurements are available only for the UV2 and VIS wavelengths (306 to 432 nm). The shortname for this OMI Level-1B Product is OML1BRUG. The lead algorithm scientist for this product is Dr. Marcel Dobber from the Royal Netherlands Meteorological Institude (KNMI).\n\nThe OML1BRUG files are stored in the HDF4 based EOS Hierarchical Data Format (HDF-EOS). The radiances for the earth measurements (also referred as signal) and its precision are stored as a 16 bit mantissa and an 8-bit exponent. The signal can be computed using the equation: signal = mantissa x 10^exponent. For the precision, the same exponent is used as for the signal.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OML1BRUG",
-            "creator": "Marcel Dobber",
-            "title": "OMI/Aura Level 1B UV Global Geolocated Earthshine Radiances 1-orbit L2 Swath 13x24 km V003 (OML1BRUG) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BRUG_003.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA1002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA1002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -940958,73 +940931,73 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BRUG_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BRUG_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRUG.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRUG.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BRUG_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BRUG_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRUG.003/doc/README.OML1B.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRUG.003/doc/README.OML1B.pdf",
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
@@ -941034,138 +941007,174 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BRUG_003.png",
+            "identifier": "C1239966738-GES_DISC",
+            "issued": "2004-08-09",
+            "keyword": [
+                "spectral/engineering",
+                "ultraviolet wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA1002",
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
+            "series-name": "OML1BRUG",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Level 1B UV Global Geolocated Earthshine Radiances 1-orbit L2 Swath 13x24 km V003 (OML1BRUG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa15hfe_calibrated_arcsav&version=1.0",
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
-                "apollo 15"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle contains fixed-width ASCII files contains fully processed, calibrated temperature data for the upper and lower gradient bridge thermal sensors on both probes of the Heat Flow Experiment (HFE) at the Apollo 15 landing site. The time span is 02 April through  30 June 1975. These data were derived from raw measurements extracted from NASA's original Apollo Lunar Surface Experiments Package (ALSEP) archive tapes, also known as ARCSAV tapes.",
+            "identifier": "urn:nasa:pds:a15hfe_calibrated_arcsav",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "apollo 15"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aa15hfe_calibrated_arcsav&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:a15hfe_calibrated_arcsav",
```

