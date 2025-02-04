# Change History for nasa.json (Part 76)

### Changes from 31606f9 to dd2190f (Part 65/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3805-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-01T02:31:58.500 to 2015-09-01T02:55:52.949.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3805-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT5-3805-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext5-3805-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2015-01-01 to 2016-12-31. It is a Occultation measurement and covers the time 2015-09-01T02:31:58.500 to 2015-09-01T02:55:52.949.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3805 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 5 3805 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1682",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rupp, D., and P. Buotte. 2020. NACP: Climate Data Inputs (3-hourly) for Community Land Model, Western USA, 1979-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1682",
-            "issued": "2020-11-18",
-            "temporal": "1979-01-01T00:00:00Z/2016-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-17",
-            "keyword": [
-                "atmospheric winds",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
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
-            "identifier": "C2517357574-ORNL_CLOUD",
             "description": "This dataset provides sub-daily, high-resolution, climate data inputs including temperature, precipitation, near surface specific humidity, incoming short-wave radiation, and near-surface wind speed over 11 states of the western USA. States included are Arizona, California, Colorado, Idaho, Montana, Nevada, New Mexico, Oregon, Utah, Washington, and Wyoming. These data were derived for use in the Community Land Model (CLM v4.5) and are at 3-hourly temporal and 4 x 4 km spatial resolutions for the 1979 through 2015 time period. The source for observational data was METDATA (now called GRIDMET), at a daily resolution. Modeling efforts using these data estimated annual carbon stocks, fluxes, and productivity across the western United States.",
-            "graphic-preview-description": "Four variables for the same 3-hour timestep, December 8, 2015, 12:00 AM to 3:00 AM, a) precipitation flux (kg m-2 s-1) b) air temperature (K) c) shortwave radiation flux (W m-2) d) specific humidity. Source: western_USA_precipitation_3hr_2015-12.nc4",
-            "title": "NACP: Climate Data Inputs (3-hourly) for Community Land Model, Western USA, 1979-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/HighRes_ClimateData_Western_US_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1682",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1682",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/nacp/HighRes_ClimateData_Western_US/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/nacp/HighRes_ClimateData_Western_US/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/HighRes_ClimateData_Western_US.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/HighRes_ClimateData_Western_US.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1682",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1682",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/HighRes_ClimateData_Western_US/comp/Climate_Data_Disaggregation_Methods_CompanionFile.pdf",
-                    "description": "NACP: Climate Data Inputs (3-hourly) for Community Land Model, Western USA, 1979-2015: Climate_Data_Disaggregation_Methods_CompanionFile.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "NACP: Climate Data Inputs (3-hourly) for Community Land Model, Western USA, 1979-2015: Climate_Data_Disaggregation_Methods_CompanionFile.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/HighRes_ClimateData_Western_US/comp/Climate_Data_Disaggregation_Methods_CompanionFile.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/HighRes_ClimateData_Western_US/comp/HighRes_ClimateData_Western_US.pdf",
-                    "description": "NACP: Climate Data Inputs (3-hourly) for Community Land Model, Western USA, 1979-2015: HighRes_ClimateData_Western_US.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "NACP: Climate Data Inputs (3-hourly) for Community Land Model, Western USA, 1979-2015: HighRes_ClimateData_Western_US.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/nacp/HighRes_ClimateData_Western_US/comp/HighRes_ClimateData_Western_US.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/NACP/guides/HighRes_ClimateData_Western_US_Fig1.png",
-                    "description": "Four variables for the same 3-hour timestep, December 8, 2015, 12:00 AM to 3:00 AM, a) precipitation flux (kg m-2 s-1) b) air temperature (K) c) shortwave radiation flux (W m-2) d) specific humidity. Source: western_USA_precipitation_3hr_2015-12.nc4",
                     "@type": "dcat:Distribution",
+                    "description": "Four variables for the same 3-hour timestep, December 8, 2015, 12:00 AM to 3:00 AM, a) precipitation flux (kg m-2 s-1) b) air temperature (K) c) shortwave radiation flux (W m-2) d) specific humidity. Source: western_USA_precipitation_3hr_2015-12.nc4",
+                    "downloadURL": "https://daac.ornl.gov/NACP/guides/HighRes_ClimateData_Western_US_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Four variables for the same 3-hour timestep, December 8, 2015, 12:00 AM to 3:00 AM, a) precipitation flux (kg m-2 s-1) b) air temperature (K) c) shortwave radiation flux (W m-2) d) specific humidity. Source: western_USA_precipitation_3hr_2015-12.nc4",
+            "graphic-preview-file": "https://daac.ornl.gov/NACP/guides/HighRes_ClimateData_Western_US_Fig1.png",
+            "identifier": "C2517357574-ORNL_CLOUD",
+            "issued": "2020-11-18",
+            "keyword": [
+                "atmospheric winds",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1682",
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
             "spatial": "-124.81 31.19 -101.98 49.02",
+            "temporal": "1979-01-01T00:00:00Z/2016-01-01T23:59:59Z",
             "theme": [
                 "NACP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NACP: Climate Data Inputs (3-hourly) for Community Land Model, Western USA, 1979-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR5-V1.0",
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
+            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on October 23 and 24, 2008, during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr5-v1.0_dyzt-vkqb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-RSS-1-SAGR5-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-rss-1-sagr5-v1.0_dyzt-vkqb",
-            "description": "The Cassini Radio Science Saturn Gravity Science Experiment (SAGR5) Raw Data Archive is a time-ordered collection of radio science raw data acquired on October 23 and 24, 2008, during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - SAGR5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-5-DISPARITY-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-5-disparity-ops-v1.0_dz2d-kjb8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-5-DISPARITY-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-5-disparity-ops-v1.0_dz2d-kjb8",
-            "description": "not applicable",
-            "title": "MER 2 MARS HAZARD AVOID CAMERA DISPARITY RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 2 MARS HAZARD AVOID CAMERA DISPARITY RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5880/GFZ.GRACE_06_GAD",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "GRACE. 2018-08-31. GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS GFZ (GAD). Version 6.0. GRACE_GAD_L2_GRAV_GFZ_RL06. JPL PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, GFZ. https://doi.org/10.5880/GFZ.GRACE_06_GAD. https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/. GRACE, GFZ, 2018-08-31, GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAD, https://podaac-tools.jpl.nasa.gov/drive/files/allData/grace/docs/.",
-            "issued": "2018-08-06",
-            "temporal": "2002-04-05T00:00:00Z/2017-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-06",
-            "keyword": [
-                "solid earth",
-                "gravity/gravitational field",
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
-            "identifier": "C2491772129-POCLOUD",
-            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of ocean bottom pressure derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements, produced by the German Research Centre for Geosciences (GFZ).  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
-            "release-place": "JPL PO.DAAC",
-            "series-name": "GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS GFZ (GAD)",
-            "graphic-preview-description": "Thumbnail",
             "creator": "GRACE",
-            "title": "GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAD",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAD_L2_GRAV_GFZ_RL06.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "FOR EXPERT USE ONLY.  This dataset contains estimates of ocean bottom pressure derived from the Gravity Recovery and Climate Experiment (GRACE) mission measurements, produced by the German Research Centre for Geosciences (GFZ).  The data are in spherical harmonics averaged over approximately a month.  The primary objective of the GRACE mission is to obtain accurate estimates of the mean and time-variable components of the gravity field variations.  This objective is achieved by making continuous measurements of the change in distance between twin spacecraft, co-orbiting in about 500 km altitude, near circular, polar orbit, spaced approximately 200 km apart, using a microwave ranging system.  In addition to these range change, the non-gravitional forces are measured on each satellite using a high accuracy electrostatic, room-temperature accelerometer.  The satellite orientation and position (and timing) are precisely measured using twin star cameras and a GPS receiver, respectively.  Spatial and temporal variations in the gravity field affect the orbits (or trajectories) of the twin spacecraft differently.  These differences are manifested as changes in the distance between the spacecraft, as they orbit the Earth.  This change in distance is reflected in the time-of-flight of microwave signals transmitted and received nearly simultaneously between the two spacecraft.  The change in this time of fight is continuously measured by tracking the phase of the microwave carrier signals.  The so called dual-one-way range change measurements can be reconstructed from these phase measurements.  This range change (or its numerically derived derivatives), along with other mission and ancillary data, is subsequently analyzed to extract the parameters of an Earth gravity field model.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5880%2FGFZ.GRACE_06_GAD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5880%2FGFZ.GRACE_06_GAD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ProdSpecDoc_v4.6.pdf",
-                    "description": "Product Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product Specification Document",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/open/L1B/GFZ/AOD1B/RL04/docs/ProdSpecDoc_v4.6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAD_L2_GRAV_GFZ_RL06.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAD_L2_GRAV_GFZ_RL06.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/retired/docs/L2-GFZ_ProcStds_RL06_DRAFT.pdf",
-                    "description": "GFZLevel-2 Processing Standards Document For Level-2 Product RL06",
                     "@type": "dcat:Distribution",
+                    "description": "GFZLevel-2 Processing Standards Document For Level-2 Product RL06",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/grace/retired/docs/L2-GFZ_ProcStds_RL06_DRAFT.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772129-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772129-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772129-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772129-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/GRACE_GAD_L2_GRAV_GFZ_RL06.jpg",
+            "identifier": "C2491772129-POCLOUD",
+            "issued": "2018-08-06",
+            "keyword": [
+                "solid earth",
+                "gravity/gravitational field",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5880/GFZ.GRACE_06_GAD",
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
+            "series-name": "GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS GFZ (GAD)",
             "spatial": "-180.0 -88.0 180.0 88.0",
+            "temporal": "2002-04-05T00:00:00Z/2017-07-01T00:00:00Z",
             "theme": [
                 "GRACE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GRACE OCEAN BOTTOM GEOPOTENTIAL COEFFICIENTS GFZ RELEASE 6.0 GAD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3120",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Read, W., Livesey, N., and Fuller, R.. 2020-04-20. ML3DBSO2. Version 004. MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3120. https://disc.gsfc.nasa.gov/datacollection/ML3DBSO2_004.html. Digital Science Data.",
-            "issued": "2020-03-06",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-06",
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
-            "identifier": "C1725333619-GES_DISC",
-            "description": "ML3DBSO2 is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for sulfur dioxide (SO2) derived from radiances measured by the 240 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 215 to 10 hPa, and the vertical resolution is about 3 km. Users of the ML3DBSO2 data product should read chapter 4 and section 3.21 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DBSO2",
             "creator": "Read, W., Livesey, N., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V004 (ML3DBSO2) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBSO2_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DBSO2 is the EOS Aura Microwave Limb Sounder (MLS) daily binned on various vertical grids product for sulfur dioxide (SO2) derived from radiances measured by the 240 GHz radiometer. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is from 215 to 10 hPa, and the vertical resolution is about 3 km. Users of the ML3DBSO2 data product should read chapter 4 and section 3.21 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3120",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3120",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -675895,547 +675873,541 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBSO2_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DBSO2_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBSO2.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DBSO2.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBSO2.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DBSO2.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBSO2_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DBSO2_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DBSO2_004.png",
+            "identifier": "C1725333619-GES_DISC",
+            "issued": "2020-03-06",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3120",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-06",
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
+            "title": "MLS/Aura Level 3 Daily Binned Sulfur Dioxide (SO2) Mixing Ratio on Assorted Grids V004 (ML3DBSO2) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alowell_uranus-neptune-photometry&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Photometric observations of Uranus and Neptune (1972-2016) in the b (472 nm) and y (551 nm) filters of the Str\u00f6mgren photometric system at Lowell Observatory. Observations recorded mainly seasonal variations of disk-integrated albedos of these objects. This bundle includes 360 observations of Uranus and 433 observations of Neptune from 1972-2016.",
+            "identifier": "urn:nasa:pds:lowell_uranus-neptune-photometry",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "uranus neptune photometry",
                 "neptune",
                 "uranus",
                 "uranus and neptune photometry"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Alowell_uranus-neptune-photometry&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:lowell_uranus-neptune-photometry",
-            "description": "Photometric observations of Uranus and Neptune (1972-2016) in the b (472 nm) and y (551 nm) filters of the Str\u00f6mgren photometric system at Lowell Observatory. Observations recorded mainly seasonal variations of disk-integrated albedos of these objects. This bundle includes 360 observations of Uranus and 433 observations of Neptune from 1972-2016.",
-            "title": "Lowell Observatory Uranus and Neptune b (472 nm) and y (551 nm) Photometry (1972-2016) Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Lowell Observatory Uranus and Neptune b (472 nm) and y (551 nm) Photometry (1972-2016) Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-REX-2-JUPITER-V1.0",
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
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons                Radio Science Experiment                                               instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-rex-2-jupiter-v1.0_dza4-xswj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-REX-2-JUPITER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-rex-2-jupiter-v1.0_dza4-xswj",
-            "description": "This data set contains Raw data taken by the New Horizons                Radio Science Experiment                                               instrument during the                                                    Jupiter encounter                                                      mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      REX JUPITER ENCOUNTER                                                   \n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS                            \n      REX JUPITER ENCOUNTER                                                   \n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHMTB-2PS28",
             "citation": "NOAA/STAR. 2021-04-05. AVHRRF_MB-STAR-L2P-v2.80. Version 2.80. GHRSST L2P Metop-B AVHRR FRAC ACSPO v2.80 1km Dataset. Camp Springs, MD (USA). Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHMTB-2PS28. https://podaac.jpl.nasa.gov/GHRSST. NOAA/STAR, The GHRSST Project Office, 2021-04-05, GHRSST NOAA/STAR Metop-B AVHRR FRAC ACSPO v2.80 1km L2P Dataset (GDS v2), https://podaac.jpl.nasa.gov/GHRSST.",
-            "issued": "2021-03-19",
-            "temporal": "2012-10-19T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-19",
-            "references": [
-                "https://doi.org/10.3390/rs13204046"
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
-            "identifier": "C2205121394-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The MetOp First Generation (FG) is a European multi-satellite program jointly established by ESA and EUMETSAT, comprising three satellites, MetOp-A, -B and -C. The primary sensor onboard MetOp-FG, the Advanced Very High Resolution Radiometer/3 (AVHRR/3) contributed by NOAA, measures Earth emissions and reflectances in 5 out of 6 available bands (centered at 0.63, 0.83, 1.61, 3.7, 11 and 12 microns), in a swath of 2,600km from an 817km altitude. These data are collected in a Full Resolution Area Coverage (FRAC) mode, with pixel size of 1.1km at nadir. Metop-B launched on 17 September 2012 is the second in the MetOp-FG series. The NOAA Advanced Clear-Sky Processor for Ocean (ACSPO) Level 2 Preprocessed (L2P) SST product is derived at the full AVHRR FRAC resolution and reported in 10 minute granules in NetCDF4 format, compliant with the GHRSST Data Specification version 2 (GDS2). Subskin SSTs are derived using the regression Nonlinear SST (NLSST) algorithm, which employs three bands (3.7, 11 and 12 microns) at night and two bands (11 and 12 microns) during the day. The ACSPO AVHRR FRAC L2P product is monitored and validated against quality controlled in situ data, provided by the NOAA in situ SST Quality Monitor system (iQuam; Xu and Ignatov, 2014, https://doi.org/10.1175/JTECH-D-13-00121.1 ), in another NOAA system, SST Quality Monitor (SQUAM; Dash et al, 2010, https://doi.org/10.1175/2010JTECHO756.1 ). SST imagery and clear-sky masking are continuously evaluated, and checked for consistency with other sensors and platforms, in the ACSPO Regional Monitor for SST (ARMS) system. MetOp-A orbital characteristics and AVHRR/3 sensor performance are tracked in the NOAA 3S system (He et al., 2016, https://doi.org/10.3390/rs8040346 ).The L2P Near Real Time (NRT) SST files are archived at PO.DAAC with 3-6 hours latency, and then replaced by the Re-ANalysis (RAN) SST after about 2 months later with identical file names. Two features can be used to identify them: different file name time stamps and netCDF global attribute metadata source=NOAA-NCEP-GFS for NRT and source=MERRA-2 for RAN.  A reduced size (0.45GB/day), equal-angle gridded (0.02-deg resolution) ACSPO L3U product is available at https://doi.org/10.5067/GHMTB-3US28",
-            "release-place": "Camp Springs, MD (USA)",
-            "series-name": "AVHRRF_MB-STAR-L2P-v2.80",
             "creator": "NOAA/STAR",
-            "title": "GHRSST NOAA/STAR Metop-B AVHRR FRAC ACSPO v2.80 1km L2P Dataset (GDS v2)",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRF_MB-STAR-L2P-v2.80.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MetOp First Generation (FG) is a European multi-satellite program jointly established by ESA and EUMETSAT, comprising three satellites, MetOp-A, -B and -C. The primary sensor onboard MetOp-FG, the Advanced Very High Resolution Radiometer/3 (AVHRR/3) contributed by NOAA, measures Earth emissions and reflectances in 5 out of 6 available bands (centered at 0.63, 0.83, 1.61, 3.7, 11 and 12 microns), in a swath of 2,600km from an 817km altitude. These data are collected in a Full Resolution Area Coverage (FRAC) mode, with pixel size of 1.1km at nadir. Metop-B launched on 17 September 2012 is the second in the MetOp-FG series. The NOAA Advanced Clear-Sky Processor for Ocean (ACSPO) Level 2 Preprocessed (L2P) SST product is derived at the full AVHRR FRAC resolution and reported in 10 minute granules in NetCDF4 format, compliant with the GHRSST Data Specification version 2 (GDS2). Subskin SSTs are derived using the regression Nonlinear SST (NLSST) algorithm, which employs three bands (3.7, 11 and 12 microns) at night and two bands (11 and 12 microns) during the day. The ACSPO AVHRR FRAC L2P product is monitored and validated against quality controlled in situ data, provided by the NOAA in situ SST Quality Monitor system (iQuam; Xu and Ignatov, 2014, https://doi.org/10.1175/JTECH-D-13-00121.1 ), in another NOAA system, SST Quality Monitor (SQUAM; Dash et al, 2010, https://doi.org/10.1175/2010JTECHO756.1 ). SST imagery and clear-sky masking are continuously evaluated, and checked for consistency with other sensors and platforms, in the ACSPO Regional Monitor for SST (ARMS) system. MetOp-A orbital characteristics and AVHRR/3 sensor performance are tracked in the NOAA 3S system (He et al., 2016, https://doi.org/10.3390/rs8040346 ).The L2P Near Real Time (NRT) SST files are archived at PO.DAAC with 3-6 hours latency, and then replaced by the Re-ANalysis (RAN) SST after about 2 months later with identical file names. Two features can be used to identify them: different file name time stamps and netCDF global attribute metadata source=NOAA-NCEP-GFS for NRT and source=MERRA-2 for RAN.  A reduced size (0.45GB/day), equal-angle gridded (0.02-deg resolution) ACSPO L3U product is available at https://doi.org/10.5067/GHMTB-3US28",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMTB-2PS28",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHMTB-2PS28",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1117/1.JRS.11.032405",
-                    "description": "JPSS VIIRS level 3 uncollated sea surface temperature product at NOAA",
                     "@type": "dcat:Distribution",
+                    "description": "JPSS VIIRS level 3 uncollated sea surface temperature product at NOAA",
+                    "downloadURL": "https://doi.org/10.1117/1.JRS.11.032405",
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
-                    "downloadURL": "https://doi.org/10.1002/2013JD020637",
-                    "description": "Evaluation and Selection of SST Regression Algorithms for JPSS VIIRS",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation and Selection of SST Regression Algorithms for JPSS VIIRS",
+                    "downloadURL": "https://doi.org/10.1002/2013JD020637",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-15-0166.1",
-                    "description": "Sensor-Specific Error Statistics for SST in the Advanced Clear-Sky Processor for Oceans",
                     "@type": "dcat:Distribution",
+                    "description": "Sensor-Specific Error Statistics for SST in the Advanced Clear-Sky Processor for Oceans",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-15-0166.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRF_MB-STAR-L2P-v2.80.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRF_MB-STAR-L2P-v2.80.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205121394-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2205121394-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205121394-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2205121394-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRRF_MB-STAR-L2P-v2.80.jpg",
+            "identifier": "C2205121394-POCLOUD",
+            "issued": "2021-03-19",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHMTB-2PS28",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-19",
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
+            "series-name": "AVHRRF_MB-STAR-L2P-v2.80",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-10-19T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST NOAA/STAR Metop-B AVHRR FRAC ACSPO v2.80 1km L2P Dataset (GDS v2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0652-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-17T10:16:40.000 to 2015-03-17T13:48:31.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0652-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0652-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0652-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-17T10:16:40.000 to 2015-03-17T13:48:31.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0652 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0652 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/SMP20-4U7CS",
             "citation": "Oleg Melnichenko. 2023-03-31. Multi-Mission Optimally Interpolated Sea Surface Salinity Global 7-Day Dataset V2. Version 2.0. Multi-mission L4 Optimally Interpoated Sea Surface Salinity. Earth and Space Research (ESR), Seattle WA. Archived by National Aeronautics and Space Administration, U.S. Government, PODAAC. https://doi.org/10.5067/SMP20-4U7CS. https://www.esr.org/data-products/oisss. Oleg Melnichenko, PODAAC, 2021-06-30, Multi-Mission Optimally Interpolated Sea Surface Salinity Global Dataset V1, http://apdrc.soest.hawaii.edu/datadoc/oisss.php.",
-            "issued": "2021-06-07",
-            "temporal": "2011-08-24T12:00:00Z/2023-03-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-07",
-            "references": [
-                "https://doi.org/doi:10.1002/2015JC011343"
-            ],
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "identifier": "C2589160971-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This is a level 4 product on a 0.25-degree spatial and 4-day temporal grid. The product is derived from the level 2 swath data of three satellite missions: the Aquarius/SAC-D, Soil Moisture Active Passive (SMAP) and Soil Moisture and Ocean Salinity (SMOS) using Optimal Interpolation (OI) with a 7-day decorrelation time scale. The product offers a continuous record from August 28, 2011 to present by concatenating the measurements from Aquarius (September 2011 - June 2015) and SMAP (April 2015  present). ESAs SMOS data was used to fill the gap in SMAP data between June and July 2019, when the SMAP satellite was in a safe mode. The two-month overlap (April - June 2015) between Aquarius and SMAP was used to ensure consistency and continuity in data record. The product covers the global ocean, including the Arctic and Antarctic in the areas free of sea ice, but does not cover internal seas such as Mediterranean and Baltic Sea. In-situ salinity from Argo floats and moored buoys are used to derive a large-scale bias correction and to ensure consistency and accuracy of the OISSS dataset. This dataset is produced by the International Pacific Research Center (IPRC) of the University of Hawaii at Manoa in collaboration with the Remote Sensing Systems (RSS), Santa Rosa, California. More details can be found in the users guide.",
-            "release-place": "Earth and Space Research (ESR), Seattle WA",
-            "series-name": "Multi-Mission Optimally Interpolated Sea Surface Salinity Global 7-Day Dataset V2",
             "creator": "Oleg Melnichenko",
-            "title": "Multi-Mission Optimally Interpolated Sea Surface Salinity Global Dataset V2",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISSS_L4_multimission_7day_v2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This is a level 4 product on a 0.25-degree spatial and 4-day temporal grid. The product is derived from the level 2 swath data of three satellite missions: the Aquarius/SAC-D, Soil Moisture Active Passive (SMAP) and Soil Moisture and Ocean Salinity (SMOS) using Optimal Interpolation (OI) with a 7-day decorrelation time scale. The product offers a continuous record from August 28, 2011 to present by concatenating the measurements from Aquarius (September 2011 - June 2015) and SMAP (April 2015  present). ESAs SMOS data was used to fill the gap in SMAP data between June and July 2019, when the SMAP satellite was in a safe mode. The two-month overlap (April - June 2015) between Aquarius and SMAP was used to ensure consistency and continuity in data record. The product covers the global ocean, including the Arctic and Antarctic in the areas free of sea ice, but does not cover internal seas such as Mediterranean and Baltic Sea. In-situ salinity from Argo floats and moored buoys are used to derive a large-scale bias correction and to ensure consistency and accuracy of the OISSS dataset. This dataset is produced by the International Pacific Research Center (IPRC) of the University of Hawaii at Manoa in collaboration with the Remote Sensing Systems (RSS), Santa Rosa, California. More details can be found in the users guide.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP20-4U7CS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSMP20-4U7CS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISSS_L4_multimission_7day_v2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISSS_L4_multimission_7day_v2.jpg",
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/OISSS_V2/OISSS_Product_Notes_v2.pdf",
-                    "description": "OISSS Level 4 Product Guide",
                     "@type": "dcat:Distribution",
+                    "description": "OISSS Level 4 Product Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/smap/open/docs/OISSS_V2/OISSS_Product_Notes_v2.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2589160971-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2589160971-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2589160971-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2589160971-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/OISSS_L4_multimission_7day_v2.jpg",
+            "identifier": "C2589160971-POCLOUD",
+            "issued": "2021-06-07",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SMP20-4U7CS",
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
+            "release-place": "Earth and Space Research (ESR), Seattle WA",
+            "series-name": "Multi-Mission Optimally Interpolated Sea Surface Salinity Global 7-Day Dataset V2",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-24T12:00:00Z/2023-03-27T00:00:00Z",
             "theme": [
                 "SMAP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Multi-Mission Optimally Interpolated Sea Surface Salinity Global Dataset V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10881",
             "bureauCode": [
                 "026:00"
             ],
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
-                "project",
-                "glenn research center",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Gordon Johnston",
                 "hasEmail": "mailto:gordon.johnston@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10881",
             "description": "Technologies include, but are not limited to, electric and advanced chemical propulsion, propellantless propulsion such as aerocapture and solar sails, sample return ascent vehicles, and Earth return systems. \n\nISP will enable access to more challenging and interesting science destinations, including enabling sample return missions. ISP continues to advance several propulsion technologies in support of future Flagship, Discovery, Mars, and New Frontiers missions. The ISP portfolio continues to invest in high-priority technology areas such as the electric propulsion and aerocapture/Earth entry, descent, and landing technologies identified in the Solar System Exploration Roadmap, the 2010 SMD Science Plan, and the 2011 Planetary Decadal Survey.  The ISP project is highly responsive to the Decadal Survey.\n\nThe ISP project will complete the 7kW NASA's Evolutionary Xenon Thruster (NEXT) Power Processing Unit (PPU) repair in 2012, and will complete NEXT PPU characterization and integration testing and long duration validation testing of the NEXT thruster in 2013. ISP is completing the electric propulsion 4kW High Voltage Hall Accelerator (HiVHAC) thruster development task, is assessing commercial Hall systems, and will start long duration testing of the HIVHAC thruster in 2012. The Hall system power processing unit (PPU) and other subsystem technology development starts development in FY 2012.  High Voltage Hall Accelerator (HiVHAC) thruster technology is applicable to Earth return vehicles (ERV), transfer stages, and low-cost electric propulsion systems for Discovery-class missions. In FY 2012 ISP will continue development of NDI techniques and a detailed design for a lightweight propellant tank applicable to the Skycrane. ISP will continue completing Earth Entry Vehicle (EEV ) heat shield micro-meteoroid/orbital debris characteristics studies, a preliminary design of a multi-mission Earth entry vehicle (MMEEV) concept and continuing MMEEV technology development.",
-            "title": "In-Space Propulsion (346620) Technology Project",
-            "programCode": [
-                "026:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -676443,201 +676415,209 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "TECHPORT_10881",
+            "issued": "2018-06-25",
+            "keyword": [
+                "project",
+                "glenn research center",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10881",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:013"
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
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "In-Space Propulsion (346620) Technology Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1854",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Tang, H., L. Ma, A.J. Lister, J. O'Neil-Dunne, J. Lu, R. Lamb, R.O. Dubayah, and G.C. Hurtt. 2021. LiDAR Derived Biomass, Canopy Height, and Cover for New England Region, USA, 2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1854",
-            "issued": "2022-11-28",
-            "temporal": "2010-01-01T00:00:00Z/2015-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "vegetation",
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
-            "identifier": "C2345879771-ORNL_CLOUD",
             "description": "This dataset provides 30 m gridded estimates of aboveground biomass density (AGBD), forest canopy height, and tree canopy coverage for the New England Region of the U.S., including the state of Maine, Vermont, New Hampshire, Massachusetts, Connecticut, and Rhode Island, for the nominal year 2015. It is based on inputs from 1 m resolution Leaf-off LiDAR data collected from 2010 through 2015, high-resolution leaf-on agricultural imagery, and FIA plot-level measurements. Canopy height and tree cover were derived directly from LiDAR data while AGBD was estimated by statistical models that link remote sensing data and FIA plots at the pixel level. Error in AGBD was calculated at the 90% confidence interval. This approach can directly contribute to the formation of a cohesive forest carbon accounting system at national and even international levels, especially via future integrations with NASA's spaceborne LiDAR missions.",
-            "graphic-preview-description": "30 m resolution maps of aboveground biomass density (AGBD) over the\nNew England region in 2015. a) The mean of the posterior\ndistribution sampled from a Markov chain Monte Carlo (MCMC) model. b)\nThe AGBD estimate over an entire pixel adjusted by canopy cover (i.e.,\nAGBD multiplied by canopy cover percentage). Despite similar forest carbon density values between forests and suburban areas, their total carbon stock per unit area can differ by one order of magnitude, highlighting the requirement for high-resolution mapping of both forest density and extent in a carbon accounting framework. Source: Tang et al., 2021",
-            "title": "LiDAR Derived Biomass, Canopy Height, and Cover for New England Region, USA, 2015",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/AGB_CanopyHt_Cover_NewEngland_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1854",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1854",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/AGB_CanopyHt_Cover_NewEngland/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/AGB_CanopyHt_Cover_NewEngland/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/AGB_CanopyHt_Cover_NewEngland.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/AGB_CanopyHt_Cover_NewEngland.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1854",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1854",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/AGB_CanopyHt_Cover_NewEngland/comp/AGB_CanopyHt_Cover_NewEngland.pdf",
-                    "description": "LiDAR Derived Biomass, Canopy Height, and Cover for New England Region, USA, 2015: AGB_CanopyHt_Cover_NewEngland.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "LiDAR Derived Biomass, Canopy Height, and Cover for New England Region, USA, 2015: AGB_CanopyHt_Cover_NewEngland.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/AGB_CanopyHt_Cover_NewEngland/comp/AGB_CanopyHt_Cover_NewEngland.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/AGB_CanopyHt_Cover_NewEngland_Fig1.png",
-                    "description": "30 m resolution maps of aboveground biomass density (AGBD) over the\nNew England region in 2015. a) The mean of the posterior\ndistribution sampled from a Markov chain Monte Carlo (MCMC) model. b)\nThe AGBD estimate over an entire pixel adjusted by canopy cover (i.e.,\nAGBD multiplied by canopy cover percentage). Despite similar forest carbon density values between forests and suburban areas, their total carbon stock per unit area can differ by one order of magnitude, highlighting the requirement for high-resolution mapping of both forest density and extent in a carbon accounting framework. Source: Tang et al., 2021",
                     "@type": "dcat:Distribution",
+                    "description": "30 m resolution maps of aboveground biomass density (AGBD) over the\nNew England region in 2015. a) The mean of the posterior\ndistribution sampled from a Markov chain Monte Carlo (MCMC) model. b)\nThe AGBD estimate over an entire pixel adjusted by canopy cover (i.e.,\nAGBD multiplied by canopy cover percentage). Despite similar forest carbon density values between forests and suburban areas, their total carbon stock per unit area can differ by one order of magnitude, highlighting the requirement for high-resolution mapping of both forest density and extent in a carbon accounting framework. Source: Tang et al., 2021",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/AGB_CanopyHt_Cover_NewEngland_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "30 m resolution maps of aboveground biomass density (AGBD) over the\nNew England region in 2015. a) The mean of the posterior\ndistribution sampled from a Markov chain Monte Carlo (MCMC) model. b)\nThe AGBD estimate over an entire pixel adjusted by canopy cover (i.e.,\nAGBD multiplied by canopy cover percentage). Despite similar forest carbon density values between forests and suburban areas, their total carbon stock per unit area can differ by one order of magnitude, highlighting the requirement for high-resolution mapping of both forest density and extent in a carbon accounting framework. Source: Tang et al., 2021",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/AGB_CanopyHt_Cover_NewEngland_Fig1.png",
+            "identifier": "C2345879771-ORNL_CLOUD",
+            "issued": "2022-11-28",
+            "keyword": [
+                "vegetation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1854",
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
             "spatial": "-74.8 39.96 -66.36 46.76",
+            "temporal": "2010-01-01T00:00:00Z/2015-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LiDAR Derived Biomass, Canopy Height, and Cover for New England Region, USA, 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-SHARAD-3-EDR-V1.0",
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
+            "description": "This dataset contains EDR (raw) data\nfrom the SHARAD (Shallow Radar) instrument on Mars Reconnaissance\nOrbiter. SHARAD is the sub-surface sounding radar provided by the\nItalian Space Agency (ASI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-sharad-3-edr-v1.0_dzm5-nds7",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-SHARAD-3-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-sharad-3-edr-v1.0_dzm5-nds7",
-            "description": "This dataset contains EDR (raw) data\nfrom the SHARAD (Shallow Radar) instrument on Mars Reconnaissance\nOrbiter. SHARAD is the sub-surface sounding radar provided by the\nItalian Space Agency (ASI).",
-            "title": "MRO SHARAD EXPERIMENT DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO SHARAD EXPERIMENT DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0553-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-29T01:10:15.000 to 2015-01-29T02:42:55.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0553-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0553-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0553-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-01-29T01:10:15.000 to 2015-01-29T02:42:55.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0553 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0553 V1.0"
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
-                "lgrs",
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
-            "identifier": "NASA-438",
             "description": "LGRS",
-            "title": "PDS GRAIL (Gravity Recovery and Interior Laboratory) Release 5",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -676645,21 +676625,52 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-438",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "lgrs",
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
+            "title": "PDS GRAIL (Gravity Recovery and Interior Laboratory) Release 5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/dzrc-vpkg",
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
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_wfc_l1_125m-valstage1-v3-01_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000200",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2011-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "cloud",
                 "climate",
@@ -676669,130 +676680,121 @@
                 "radiation",
                 "eos"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/dzrc-vpkg",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000200",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Wide Field Camera (WFC) L1B Science 125 m Native Science Data V3-01",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_wfc_l1_125m-valstage1-v3-01_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2011-10-31",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Wide Field Camera (WFC) L1B Science 125 m Native Science Data V3-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0664-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-21T21:52:00.000 to 2015-03-22T08:59:44.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0664-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0664-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0664-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-21T21:52:00.000 to 2015-03-22T08:59:44.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0664 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0664 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/17352",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-09-01",
-            "temporal": "2013-09-01T00:00:00Z/2014-12-01T00:00:00Z",
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
-                "stennis space center",
-                "project",
-                "completed"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ramona Travis",
                 "hasEmail": "mailto:ramona.e.travis@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Chief Technologist"
-            },
-            "identifier": "TECHPORT_17352",
             "description": "&lt;p&gt;&lt;strong&gt;LED light sources are ideal for plant growth systems. However, commercially available multi-color LED illumination panels are designed and manufactured to produce a single particular illumination. These panels have very specific LED colors arranged in a very specific fashion. This limits the amount of color mixing, intensity variation, and spatial arrangement that is possible, precluding passive precision illumination. There is no feedback mechanism to detect spectral shifts caused by LED aging and additionally, there is no mechanism to modulate LEDs. It is also not possible to integrate an imaging system into these panels. Furthermore, these panels are commonly operated using high voltage AC power sources, which is not ideal in a potentially wet environment. Therefore, to address these issues, custom LED illumination panels were designed and developed for this project&amp;rsquo;s plant growth chamber.&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;&lt;strong&gt;A systematic approach was taken to determine the general size, specifications, and shape of a portable plant growth unit. Once the general size and shape were finalized, the detailed design of the support structure, aeroponics, and lighting subsystems were developed. Particular attention was given to heat transfer and the expected LED thermal environment.&amp;nbsp; Additionally, a&amp;nbsp;&lt;/strong&gt;&lt;strong&gt;computational analysis was performed to determine optimal LED nodes placement so that two different uniform illumination fields could be yielded:&amp;nbsp; (1) for germinating plants, lower intensity light, and (2) for larger maturing plants, a brighter one.&amp;nbsp; Also, aeroponic studies were reviewed to identify an efficient and user-friendly system that would require minimal user involvement.&lt;/strong&gt;&lt;/p&gt;",
-            "title": "Integrated LED/Imaging Illumination Panels Demonstrated within a Small Plant Growth Chamber Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/17352",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_17352",
+            "issued": "2013-09-01",
+            "keyword": [
+                "stennis space center",
+                "project",
+                "completed"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/17352",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Chief Technologist"
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
+            "temporal": "2013-09-01T00:00:00Z/2014-12-01T00:00:00Z",
+            "title": "Integrated LED/Imaging Illumination Panels Demonstrated within a Small Plant Growth Chamber Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M03-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m03-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "starfield",
                 "16 cyg b",
@@ -676802,522 +676804,522 @@
                 "vega",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M03-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m03-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-05-07T12:48:00.000 to 2014-06-04T10:49:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP003 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP003 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_G_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, High-rate GLONASS broadcast ephemeris data, Greenbelt, MD, USA: NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GNSS/gnss_highrate_g_001",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
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
-            "identifier": "C1422104643-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS) GLObal NAvigation Satellite System (GLONASS) Broadcast Ephemeris Data (sub-hourly files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLONASS. Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The sub-hourly GLONASS broadcast ephemeris files contain 15 minutes of GLONASS broadcast navigation data in RINEX format from a global permanent network of ground-based receivers, one file per 15 minutes per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/high-rate_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) GLONASS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HIGHRATE_G_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_HIGHRATE_G_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/highrate",
-                    "description": "URL for retrieval of GNSS sub-hourly data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS sub-hourly data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/gnss/data/highrate",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
-                    "description": "URL for more information about GNSS hourly GLONASS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS hourly GLONASS broadcast navigation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/broadcast_ephemeris_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_G_001",
-                    "description": "URL for more information about GNSS sub-hourly GLONASS broadcast navigation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS sub-hourly GLONASS broadcast navigation data",
+                    "downloadURL": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_G_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1422104643-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "geodetics",
+                "gravity/gravitational field",
+                "tectonics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_HIGHRATE_G_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-24",
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
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) GLONASS Broadcast Ephemeris Data (sub-hourly files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-LECP-3-RDR-FAR-ENC-400MSEC-V1.0",
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
+            "description": "This far encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 1 while the spacecraft was within the vicinity of Saturn. This instrument measures the intensities of in-situ charged particles ( >15 keV electrons and >30 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Saturn far encounter, the entire LEPT (Low Energy Particle Telescope) and part of the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystems were turned on for data collection. Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 0.4 second rate measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-lecp-3-rdr-far-enc-400msec-v1.0_dzvi-tb7t",
+            "issued": "2018-06-26",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-LECP-3-RDR-FAR-ENC-400MSEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-lecp-3-rdr-far-enc-400msec-v1.0_dzvi-tb7t",
-            "description": "This far encounter data set consists of electron and ion counting rate data from the Low Energy Charged Particle (LECP) experiment on Voyager 1 while the spacecraft was within the vicinity of Saturn. This instrument measures the intensities of in-situ charged particles ( >15 keV electrons and >30 keV ions) with various levels of discrimination based on energy range and mass species. A subset of almost 100 LECP channels are included in this data set. The LECP data are globally calibrated to the extent possible.  During Saturn far encounter, the entire LEPT (Low Energy Particle Telescope) and part of the LEMPA (Low Energy Magnetospheric Particle Analyzer) subsystems were turned on for data collection. Particles include electrons, protons, alpha particles, and light, medium, and heavy nuclei particles.  The far encounter data are 0.4 second rate measurements within 1/8 of the LECP instrumental motor rotation period (the angular scanning periods, or step period).",
-            "title": "VG1 LECP 0.4S HIGH RESOLUTION SATURN FAR ENCOUNTER DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 LECP 0.4S HIGH RESOLUTION SATURN FAR ENCOUNTER DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/WYQ11GOFIQSI",
             "citation": "NASA/GSFC. 2021-04-22. TIROS4L1FMRT. Version 001. TIROS-4 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/WYQ11GOFIQSI. https://disc.gsfc.nasa.gov/datacollection/TIROS4L1FMRT_001.html. Digital Science Data.",
-            "issued": "2021-04-01",
-            "temporal": "1962-02-08T00:00:00Z/1962-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-01",
-            "keyword": [
-                "visible wavelengths",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA/GSFC",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2038742346-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "TIROS-4 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data (FMRT) product contains radiances expressed in five infrared/visible wavelength regions, expressed in either equivalent blackbody temperature (IR channels 1 and 2) or effective radiant emmitance (visible channels 3 and 5). The data will trace an elliptical, parabolic, or hyperbolic pattern on the ground due to the rotating of the instrument about the satellite spin axis. There is one orbit per file. The data were originally written on IBM 7094 machines, and these have been recovered from magnetic tapes, referred to as the Final Meteorological Radiation Tapes (FMRT). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe TIROS-4 satellite was successfully launched on February 8, 1962. The Medium-Resolution Scanning Radiometer experiment successfully returned data for about five months, continuing the measurements made by its predecessors flown on TIROS-2, and -3. A follow-on instrument was flown on TIROS-7. Degradation of the instrument after launch results in a departure of the data from the pre-launch calibration. The instrument is a five channel radiometer with a 55 km footprint at nadir with the following characteristics:\n\nChannel 1: 6.0 to 6.5 microns - water vapor absorption\nChannel 2: 8.0 to 12.0 microns - atmospheric window\nChannel 3: 0.2 to 6.0 microns - reflected solar radiation\nChannel 4: unused - transmitted redundant time reference signals\nChannel 5: 0.55 to 0.75 microns - response to the TV system\n\nThe Principal Investigator for these data was Joseph D. Barksdale from NASA Goddard Space Flight Center. This product was previously available from the NSSDC with the identifier ESAD-00139 (old ID 62-002A-03A).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TIROS4L1FMRT",
-            "creator": "NASA/GSFC",
-            "title": "TIROS-4 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS4L1FMRT) at GES DISC",
-            "graphic-preview-description": "TIROS-4 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on February 8, 1962.",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS4L1FMRT_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWYQ11GOFIQSI",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWYQ11GOFIQSI",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS4L1FMRT_Sample.png",
-                    "description": "TIROS-4 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on February 8, 1962.",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS-4 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on February 8, 1962.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS4L1FMRT_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS4L1FMRT.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS4L1FMRT.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TIROS4L1FMRT",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TIROS4L1FMRT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS4L1FMRT.001/doc/README.TIROS4FMRT.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/TIROS/TIROS4L1FMRT.001/doc/README.TIROS4FMRT.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/TirosIV_CatalogandUserManual.pdf",
-                    "description": "TIROS IV Radiation Data Catalog and Users' Manual",
                     "@type": "dcat:Distribution",
+                    "description": "TIROS IV Radiation Data Catalog and Users' Manual",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/TirosIV_CatalogandUserManual.pdf",
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
+            "graphic-preview-description": "TIROS-4 L1 FMRT data showing data coverage from the scanning radiometer channel 2 (8-12 microns) for the first orbit on February 8, 1962.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/TIROS4L1FMRT_Sample.png",
+            "identifier": "C2038742346-GES_DISC",
+            "issued": "2021-04-01",
+            "keyword": [
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/WYQ11GOFIQSI",
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
+            "series-name": "TIROS4L1FMRT",
             "spatial": "-180.0 -66.0 180.0 66.0",
+            "temporal": "1962-02-08T00:00:00Z/1962-06-30T23:59:59.999Z",
             "theme": [
                 "TIROS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TIROS-4 Medium-Resolution Scanning Radiometer Level 1 Final Meteorological Radiation Data V001 (TIROS4L1FMRT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1094-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-11T10:17:05.000 to 2015-10-11T17:28:21.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1094-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1094-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1094-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-11T10:17:05.000 to 2015-10-11T17:28:21.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1094 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1094 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-SW-MAG-4-SUMM-HGCOORDS-48SEC-V1.0",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains Voyager 2 magnetometer data from the interplanetary cruise averaged to 48 second samples in Heliographic coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-sw-mag-4-summ-hgcoords-48sec-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-SW-MAG-4-SUMM-HGCOORDS-48SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-sw-mag-4-summ-hgcoords-48sec-v1.0",
-            "description": "This dataset contains Voyager 2 magnetometer data from the interplanetary cruise averaged to 48 second samples in Heliographic coordinates.",
-            "title": "VOYAGER 2 SOLAR WIND MAGNETIC FIELD HGCOORDS 48SEC AVG V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 2 SOLAR WIND MAGNETIC FIELD HGCOORDS 48SEC AVG V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/ASIRI/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/ASIRI/DATA001.",
-            "issued": "2013-11-29",
-            "temporal": "2013-11-29T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "oceans",
-                "salinity/density",
-                "ocean optics",
-                "earth science",
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
-            "identifier": "C1633360112-OB_DAAC",
             "description": "Air-Sea Interaction Research Initiative (ASIRI) is an ONR research initiative involving multiple institutions and scientists, which, in partnership with India and Sri Lanka, aims to improve our understanding of the upper ocean and its atmospheric interactions",
-            "title": "Air-Sea Interaction Research Initiative (ASIRI), Bay of Bengal",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FASIRI%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FASIRI%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ASIRI/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/ASIRI/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360112-OB_DAAC",
+            "issued": "2013-11-29",
+            "keyword": [
+                "oceans",
+                "salinity/density",
+                "ocean optics",
+                "earth science",
+                "ocean chemistry",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/ASIRI/DATA001",
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
+            "temporal": "2013-11-29T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Air-Sea Interaction Research Initiative (ASIRI), Bay of Bengal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-ARGO0",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stephen Riser & Jie Yang. 2019-03-28. SPURS-2 Argo float CTD profile data from the E. Tropical Pacific field campaign. Version 1.0. SPURS Field Campaign ARGO float Products. Applied Physics Laboratory, University of Washington, Seattle, WA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-ARGO0. http://podaac.jpl.nasa.gov/SPURS. Stephen Riser & Jie Yang, SPURS Data Management PI, Fred Bingham, 2019-03-28, SPURS-2 Argo float CTD profile data from the E. Tropical Pacific field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-03-15",
-            "temporal": "2016-08-27T05:47:58Z/2019-03-11T23:42:58Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-03-15",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
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
-            "identifier": "C2491772323-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. Part of the Argo global network of autonomous, self-reporting samplers, Argo floats drift horizontally and move vertically through the water column generally on 10 day cycles, collecting high-quality temperature, conductivity and salinity depth (CTD) profiles from the upper 2000m. Twenty five floats were deployed during SPURS-2 within the campaign spatial domain and time period, yielding approximately 1,893 profiles. These were standard Argo floats with the addition of acoustic rain gauges (PAL) in some cases. SPURS-2 ARGO data files are organized per float and profile with the vertical conductivity, salinity, temperature, pressure, depth observations per the netCDF ARGO file specification with some augmented global metadata attributes.",
-            "release-place": "Applied Physics Laboratory, University of Washington, Seattle, WA, USA",
-            "series-name": "SPURS-2 Argo float CTD profile data from the E. Tropical Pacific field campaign",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Stephen Riser & Jie Yang",
-            "title": "SPURS-2 Argo float CTD profile data from the E. Tropical Pacific field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_ARGO.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project is comprised of two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent. Part of the Argo global network of autonomous, self-reporting samplers, Argo floats drift horizontally and move vertically through the water column generally on 10 day cycles, collecting high-quality temperature, conductivity and salinity depth (CTD) profiles from the upper 2000m. Twenty five floats were deployed during SPURS-2 within the campaign spatial domain and time period, yielding approximately 1,893 profiles. These were standard Argo floats with the addition of acoustic rain gauges (PAL) in some cases. SPURS-2 ARGO data files are organized per float and profile with the vertical conductivity, salinity, temperature, pressure, depth observations per the netCDF ARGO file specification with some augmented global metadata attributes.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-ARGO0",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-ARGO0",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/spurs",
-                    "description": "Project Website for SPURS",
                     "@type": "dcat:Distribution",
+                    "description": "Project Website for SPURS",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_ARGO.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_ARGO.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772323-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772323-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772323-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772323-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_ARGO.jpg",
+            "identifier": "C2491772323-POCLOUD",
+            "issued": "2019-03-15",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-ARGO0",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-03-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Applied Physics Laboratory, University of Washington, Seattle, WA, USA",
+            "series-name": "SPURS-2 Argo float CTD profile data from the E. Tropical Pacific field campaign",
             "spatial": "-157.88 5.06 -118.32 21.26",
+            "temporal": "2016-08-27T05:47:58Z/2019-03-11T23:42:58Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 Argo float CTD profile data from the E. Tropical Pacific field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0942%2FI0943-3-BELSKAYAPOL-V1.0",
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
+            "description": "This data set contains UBVRI polarimetric measurements of ten main belt asteroids and one potentially hazardous near-Earth asteroid (NEA), from Belskaya et al. (2009) and Belskaya et al. (2009b).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0942-i0943-3-belskayapol-v1.0_e2es-r8gj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0942%2FI0943-3-BELSKAYAPOL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0942-i0943-3-belskayapol-v1.0_e2es-r8gj",
-            "description": "This data set contains UBVRI polarimetric measurements of ten main belt asteroids and one potentially hazardous near-Earth asteroid (NEA), from Belskaya et al. (2009) and Belskaya et al. (2009b).",
-            "title": "BELSKAYA ASTEROID POLARIMETRY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "BELSKAYA ASTEROID POLARIMETRY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-2-UVVS-EDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Abstract ======== This data set consists of the MESSENGER MASCS UVVS uncalibrated observations, also known as EDRs. The MASCS UVVS experiment is a scanning grating monochromator equipped with three photomultiplier tubes. There are three UUVS EDR data products, one for each detector, which cover the wavelength ranges of the far ultraviolet (FUV), middle ultraviolet (MUV), and visible (VIS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-2-uvvs-edr-v1.0_e2gb-vdpf",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "messenger",
                 "calibration",
@@ -677325,279 +677327,256 @@
                 "earth",
                 "venus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-E%2FV%2FH-MASCS-2-UVVS-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-e-v-h-mascs-2-uvvs-edr-v1.0_e2gb-vdpf",
-            "description": "Abstract ======== This data set consists of the MESSENGER MASCS UVVS uncalibrated observations, also known as EDRs. The MASCS UVVS experiment is a scanning grating monochromator equipped with three photomultiplier tubes. There are three UUVS EDR data products, one for each detector, which cover the wavelength ranges of the far ultraviolet (FUV), middle ultraviolet (MUV), and visible (VIS).",
-            "title": "MESSENGER E/V/H MASCS 2 UVVS UNCALIBRATED DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER E/V/H MASCS 2 UVVS UNCALIBRATED DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ERBE/S4G_WFOV_NF_ZG_L3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-06-28. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ERBE/S4G_WFOV_NF_ZG_L3.",
-            "issued": "1999-06-15",
-            "temporal": "1984-11-05T00:00:00Z/1990-02-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-12",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C1000000779-LARC_ASDC",
             "description": "ERBE_S4G_WFOV_NF_ZG_1 is the Earth Radiation Budget Experiment (ERBE) S-4G Non-scanner, Wide Field of View (WFOV) Numerical Filter (NF) 5 and 10 degree Zonal and Global Averages in HDF data product. Data collection for this product is complete. This data set consists of non-scanner, wide field-of-view data, which was processed using the numerical filter data reduction technique. The data were averaged over latitudinal bands(zones) as well as on a global level in which each parameter is averaged over the entire globe. The zonal averages are available in 5.0 and 10.0 degree resolutions. Monthly (day), monthly (hour), daily, and monthly hourly averages are determined for each region. The data are represented as 8-bit, 16-bit, and 32-bit integers.\r\n\r\nEarth Radiation Budget Experiment (ERBE) was a multi-satellite system designed to measure the Earth's radiation budget. ERBE instruments flew on a mid-inclination National Aeronautics and Space Administration (NASA) Earth Radiation Budget Satellite (ERBS) and two sun-synchronous National Oceanic and Atmospheric Administration (NOAA) satellites, NOAA-9 and NOAA-10. NOAA-9 and NOAA-10 provided global coverage and the ERBS provided coverage between 67.5 degrees north and south latitude. Each satellite carried both a scanner and a non-scanner instrument package. The non-scanner instrument contained four Earth-viewing channels and a solar monitor. The Earth-viewing channels had two spatial resolutions: a horizon-to-horizon view of the Earth, and a field-of-view limited to about 1000 km in diameter. The former was called the wide field-of-view (WFOV) and the latter the medium field of view (MFOV) channels. For each of the two fields of view, there was a total spectral channel which is sensitive to all wavelengths and a shortwave channel which used a high purity, fused silica filter dome to transmit only the shortwave radiation from 0.2 to 5 microns. Because of the concern for spectral flatness and high accuracy, all five channels on the non-scanner package were active cavity radiometers. The ERBE S-4G product contained averages of radiant flux and albedo on regional, zonal, and global scales. The data for the S-4G product were arranged by parameter values. The ERBE S-4G WFOV product was available as a combination of all operational spacecraft. Products have been archived from November 1984 - January 1985 and June 1989 - February 1990 for ERBS; February 1985 - October 1986 for ERBS/NOAA-9; November 1986 - January 1987 for ERBS/NOAA-9/NOAA-10; and February 1987 - May 1989 for ERBS/NOAA-10. The various combinations of the satellites reflected the actual duration of the scanners.",
-            "title": "Earth Radiation Budget Experiment (ERBE) S-4G Nonscanner,Wide Field of View (WFOV) Numerical Filter (NF) 5 and 10 degree Zonal and Global Averages in HDF",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS4G_WFOV_NF_ZG_L3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FERBE%2FS4G_WFOV_NF_ZG_L3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ERBE/S4G_WFOV_NF_ZG_L3",
-                    "description": "DOI data set landing page for ERBE_S4G_WFOV_NF_ZG_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ERBE_S4G_WFOV_NF_ZG_1",
+                    "downloadURL": "https://doi.org/10.5067/ERBE/S4G_WFOV_NF_ZG_L3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000779-LARC_ASDC",
-                    "description": "Earthdata Search for ERBE_S4G_WFOV_NF_ZG_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for ERBE_S4G_WFOV_NF_ZG_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000779-LARC_ASDC",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S4G/WFOV_NF_ZG_1/",
-                    "description": "ASDC Direct Data Download for ERBE_S4G_WFOV_NF_ZG_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ERBE_S4G_WFOV_NF_ZG_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ERBE/S4G/WFOV_NF_ZG_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000779-LARC_ASDC",
+            "issued": "1999-06-15",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ERBE/S4G_WFOV_NF_ZG_L3",
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
+            "title": "Earth Radiation Budget Experiment (ERBE) S-4G Nonscanner,Wide Field of View (WFOV) Numerical Filter (NF) 5 and 10 degree Zonal and Global Averages in HDF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M06-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m06-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "16 cyg b",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-PRL-67PCHURYUMOV-M06-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-prl-67pchuryumov-m06-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-08-01T10:00:00.000 to 2014-09-02T09:59:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 3 RDR MTP006 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 3 RDR MTP006 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://planetarynames.wr.usgs.gov/Page/mars1to5mTHEMIS",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "1979-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "images",
-                "themis",
-                "working group for planetary system nomenclature",
-                "usgs",
-                "mars",
-                "imagery",
-                "planets"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Kelly",
                 "hasEmail": "mailto:Michael.S.Kelley@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
-            },
-            "identifier": "OCIO-Fitara-162",
             "description": "THEMIS imagery of Mars approved by the International Astronomical Union (IAU).",
-            "title": "Gazetteer of Planetary Nomenclature: Mars: 1:5 million-scale THEMIS Images",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -677750,121 +677729,120 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "OCIO-Fitara-162",
+            "issued": "1979-12-31",
+            "keyword": [
+                "images",
+                "themis",
+                "working group for planetary system nomenclature",
+                "usgs",
+                "mars",
+                "imagery",
+                "planets"
+            ],
+            "landingPage": "http://planetarynames.wr.usgs.gov/Page/mars1to5mTHEMIS",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "International Astronomical Union (IAU) Working Group for Planetary System Nomenclature (WGPSN)"
+            },
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "Gazetteer of Planetary Nomenclature: Mars: 1:5 million-scale THEMIS Images"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5G15XSR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AWI Moored ULS Data, Greenland Sea and Fram Strait, 1991-2002, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5G15XSR.",
-            "issued": "1991-08-01",
-            "temporal": "1991-08-01T00:00:00Z/2002-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-09-30",
-            "keyword": [
-                "ocean temperature",
-                "cryosphere",
-                "earth science",
-                "oceans",
-                "ocean pressure",
-                "terrestrial hydrosphere",
-                "sea ice",
-                "surface water"
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
-            "identifier": "C1386246251-NSIDCV0",
             "description": "This data set consists of Upward Looking Sonar (ULS) data from 11 moorings in the Greenland Sea. Parameters in the processed data files include ice draft, water pressure, and water temperature. Raw data files with sonar travel time, and files with draft frequency of occurrence, are available as well. A single statistical file for each mooring summarizes that mooring's record. These data were contributed by the Alfred Wegener Institute for Polar and Marine Research, Bremerhaven, Germany, in 2002 and 2004, as a contribution to the World Climate Research Programme's Arctic Climate System Study/Climate and Cryosphere (ACSYS/CliC) Project. Data are available via FTP.\n\nNSIDC strongly encourages you to register as a user of this data product. As a registered user, you will be notified of updates and corrections. When registering, please include the title of this data set, AWI Moored ULS Data, Greenland Sea and Fram Strait, 1991-2002.",
-            "title": "AWI Moored ULS Data, Greenland Sea and Fram Strait, 1991-2002, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5G15XSR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5G15XSR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02139_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02139_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5G15XSR",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5G15XSR",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5G15XSR",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5G15XSR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246251-NSIDCV0",
+            "issued": "1991-08-01",
+            "keyword": [
+                "ocean temperature",
+                "cryosphere",
+                "earth science",
+                "oceans",
+                "ocean pressure",
+                "terrestrial hydrosphere",
+                "sea ice",
+                "surface water"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5G15XSR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "2.0 74.4 12.98333 79.0",
+            "temporal": "1991-08-01T00:00:00Z/2002-09-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AWI Moored ULS Data, Greenland Sea and Fram Strait, 1991-2002, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652196-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "McCulloch, Andrew W., et al.. 2014-12-23. MRIRN3L1. Version 001. MRIR/Nimbus-3 Level 1 Meteorological Radiation Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/MRIRN3L1_001.html. Digital Science Data.",
-            "issued": "1969-04-15",
-            "temporal": "1969-04-15T00:00:00Z/1970-02-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1970-02-04",
-            "keyword": [
-                "infrared wavelengths",
-                "spectral/engineering",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1273652196-GES_DISC",
-            "description": "MRIRN3L1 is the Nimbus-3 Medium-Resolution Infrared Radiometer (MRIR) Level 1 Meteorological Radiance Data product and contain radiances expressed as equivalent blackbody temperature or \"brightness\" temperature, along with geolocation, time and other housekeeping information. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as Nimbus Meteorological Radiation Tapes (NMRT). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe MRIR instrument was designed to measure infrared electromagnetic radiation emitted and reflected from the Earth and its atmosphere at 5 wavelengths. The five wavelengths regions are as follows:\n\n(1) 6.5 to 7.0 microns - This channel covers the 6.7 micron water vapor absorption band. Its purpose is to provide information on water vapor distribution in the upper troposphere and, in conjunction with the other channels to provide data concerning relative humidities at these altitudes.\n(2) 10 to 11 microns - Operating in an atmospheric \"window,\" this channel measures surface or near-surface temperatures over clear portions of the atmosphere.  It also provides cloud cover and cloud height information (day and night).\n(3) 14.5 to 15.5 microns - This channel, centered about the strong absorption band of C02 at 15 microns, measures radiation which emanates primarily from the stratosphere. The information gained here is of primary importance to in following seasonal stratospheric temperature changes.\n(4) 20 to 23 microns - This channel yields data from the spectral region containing the broad rotational absorption bands of water vapor. It will provide information similar to that of the 6.5 to 7.0 micron channel except that the flux will largely be radiated from lower in the atmosphere.\n(5) 0.2 to 4.0 microns - This channel covers more than 99% of the solar spectrum and yields information on the intensity of the reflected solar energy from the earth and its atmosphere.\n\nThese data were previously archived at NASA NSSDC as product NMRT-MRIR under the entry ID ESAD-00183 (originally 69-037A-05B).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "MRIRN3L1",
             "creator": "McCulloch, Andrew W., et al.",
-            "title": "MRIR/Nimbus-3 Level 1 Meteorological Radiation Data V001 (MRIRN3L1) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MRIRN3L1_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "MRIRN3L1 is the Nimbus-3 Medium-Resolution Infrared Radiometer (MRIR) Level 1 Meteorological Radiance Data product and contain radiances expressed as equivalent blackbody temperature or \"brightness\" temperature, along with geolocation, time and other housekeeping information. The data, originally written on IBM 360 machines, were recovered from magnetic tapes, also referred to as Nimbus Meteorological Radiation Tapes (NMRT). The data are archived in their original IBM 36-bit word proprietary format, also referred to as a binary TAP file.\n\nThe MRIR instrument was designed to measure infrared electromagnetic radiation emitted and reflected from the Earth and its atmosphere at 5 wavelengths. The five wavelengths regions are as follows:\n\n(1) 6.5 to 7.0 microns - This channel covers the 6.7 micron water vapor absorption band. Its purpose is to provide information on water vapor distribution in the upper troposphere and, in conjunction with the other channels to provide data concerning relative humidities at these altitudes.\n(2) 10 to 11 microns - Operating in an atmospheric \"window,\" this channel measures surface or near-surface temperatures over clear portions of the atmosphere.  It also provides cloud cover and cloud height information (day and night).\n(3) 14.5 to 15.5 microns - This channel, centered about the strong absorption band of C02 at 15 microns, measures radiation which emanates primarily from the stratosphere. The information gained here is of primary importance to in following seasonal stratospheric temperature changes.\n(4) 20 to 23 microns - This channel yields data from the spectral region containing the broad rotational absorption bands of water vapor. It will provide information similar to that of the 6.5 to 7.0 micron channel except that the flux will largely be radiated from lower in the atmosphere.\n(5) 0.2 to 4.0 microns - This channel covers more than 99% of the solar spectrum and yields information on the intensity of the reflected solar energy from the earth and its atmosphere.\n\nThese data were previously archived at NASA NSSDC as product NMRT-MRIR under the entry ID ESAD-00183 (originally 69-037A-05B).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -677873,201 +677851,225 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MRIRN3L1_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/MRIRN3L1_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_MRIR_Level1/MRIRN3L1.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_MRIR_Level1/MRIRN3L1.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MRIRN3L1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MRIRN3L1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_MRIR_Level1/MRIRN3IM.001/doc/README.MRIRN3L1.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus3_MRIR_Level1/MRIRN3IM.001/doc/README.MRIRN3L1.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIIIUG.pdf",
-                    "description": "Nimbus 3 Users Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 3 Users Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/NimbusIIIUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/gzip",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus3.tar.gz",
-                    "description": "Nimbus 3 Data Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 3 Data Catalog",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/DataCatalogNimbus3.tar.gz",
+                    "mediaType": "application/gzip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/nimbus/data-sets.html",
-                    "description": "Additional Nimbus data and images can be found at NSIDC",
                     "@type": "dcat:Distribution",
+                    "description": "Additional Nimbus data and images can be found at NSIDC",
+                    "downloadURL": "https://nsidc.org/data/nimbus/data-sets.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N3_MRIR_Inventory.xlsx",
-                    "description": "N3 MRIR Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N3 MRIR Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N3_MRIR_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/MRIRN3L1_001.png",
+            "identifier": "C1273652196-GES_DISC",
+            "issued": "1969-04-15",
+            "keyword": [
+                "infrared wavelengths",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273652196-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1970-02-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "MRIRN3L1",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1969-04-15T00:00:00Z/1970-02-04T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MRIR/Nimbus-3 Level 1 Meteorological Radiation Data V001 (MRIRN3L1) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-1-TRACKING-V1.0",
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
+            "description": "Archival Tracking Data Files (ATDFs, also sometimes known as TRK-2-25 data) from the MAGELLAN mission to Venus (1989-1994) and Orbit Data Files (ODFs, also known as TRK-2-18 data) from the final 2-3 years of the MAGELLAN mission (1992-1994). These data include range and Doppler measurements from the radio tracking system of the NASA Deep Space Network (DSN).  The measurements can be used to derive a spherical harmonic model of the Venus gravity field.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-1-tracking-v1.0_e2ke-tx72",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RSS-1-TRACKING-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rss-1-tracking-v1.0_e2ke-tx72",
-            "description": "Archival Tracking Data Files (ATDFs, also sometimes known as TRK-2-25 data) from the MAGELLAN mission to Venus (1989-1994) and Orbit Data Files (ODFs, also known as TRK-2-18 data) from the final 2-3 years of the MAGELLAN mission (1992-1994). These data include range and Doppler measurements from the radio tracking system of the NASA Deep Space Network (DSN).  The measurements can be used to derive a spherical harmonic model of the Venus gravity field.",
-            "title": "MAGELLAN RAW RADIO TRACKING\n                                      DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MAGELLAN RAW RADIO TRACKING\n                                      DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD09A1G_NDVI.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Land Science Team. 2021-04-01. MODIS/Terra Gap-Filled, Smoothed NDVI 8-Day L4 500m SIN Grid. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MOD09A1G_NDVI.006. https://doi.org/10.5067/MODIS/MOD09A1G_NDVI.006.",
-            "issued": "2018-10-05",
-            "temporal": "2001-01-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-21",
-            "keyword": [
-                "land surface",
-                "ngda",
-                "earth science",
-                "national geospatial data asset",
-                "land use/land cover"
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
-            "identifier": "C2054607066-LAADS",
-            "description": "The MODIS/Terra Gap-Filled, Smoothed NDVI 8-Day L4 500m SIN Grid product, with short-name MOD09A1G_NDVI is calculated from MODIS surface reflectance products (MOD09), at 500-m resolution. MODIS time series contains occasional lower quality data, gaps from persistent clouds, cloud contamination, and other gaps. Many modeling efforts, such as those used in NACP, that use MODIS data as input, require gap-free data. The procedure contains two algorithm stages, one for smoothing and one for gap filling, which attempt to maximize the use of high-quality data to replace missing or poor-quality observations.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Land Science Team",
-            "title": "MODIS/Terra Gap-Filled, Smoothed NDVI 8-Day L4 500m SIN Grid",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Terra Gap-Filled, Smoothed NDVI 8-Day L4 500m SIN Grid product, with short-name MOD09A1G_NDVI is calculated from MODIS surface reflectance products (MOD09), at 500-m resolution. MODIS time series contains occasional lower quality data, gaps from persistent clouds, cloud contamination, and other gaps. Many modeling efforts, such as those used in NACP, that use MODIS data as input, require gap-free data. The procedure contains two algorithm stages, one for smoothing and one for gap filling, which attempt to maximize the use of high-quality data to replace missing or poor-quality observations.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09A1G_NDVI.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD09A1G_NDVI.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/MOD09A1G_NDVI--6",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/MOD09A1G_NDVI--6",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD09A1G_NDVI/",
-                    "description": "Direct access to MOD09A1G_NDVI data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MOD09A1G_NDVI data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD09A1G_NDVI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://accweb.nascom.nasa.gov/project/docs/User_guide_C5_GFS.pdf",
-                    "description": "User Guide for MOD09GFS and MOD15GFS Version 2.0",
                     "@type": "dcat:Distribution",
+                    "description": "User Guide for MOD09GFS and MOD15GFS Version 2.0",
+                    "downloadURL": "http://accweb.nascom.nasa.gov/project/docs/User_guide_C5_GFS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/6/MOD09A1G_NDVI/contents.html",
-                    "description": "Direct link to Collection's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct link to Collection's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/6/MOD09A1G_NDVI/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2054607066-LAADS",
+            "issued": "2018-10-05",
+            "keyword": [
+                "land surface",
+                "ngda",
+                "earth science",
+                "national geospatial data asset",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD09A1G_NDVI.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2001-01-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Gap-Filled, Smoothed NDVI 8-Day L4 500m SIN Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-2-JUPITER-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.  This is VERSION 2.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-2-jupiter-v2.0_e2p8-bjjy",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "j6 himalia",
                 "new horizons",
@@ -678081,35 +678083,47 @@
                 "callisto",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-2-JUPITER-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-2-jupiter-v2.0_e2p8-bjjy",
-            "description": "This data set contains Raw data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.  This is VERSION 2.0 of this data set.",
-            "title": "NEW HORIZONS\n      LORRI JUPITER ENCOUNTER\n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS\n      LORRI JUPITER ENCOUNTER\n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/e2p8-wzkw",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "The Cosmic Ray Exposure Sequencing Science (CRESS) payload system is a proof of concept experiment to assess the genomic impact of space radiation on seeds. CRESS was designed as a secondary payload for the December 2016 high-altitude high-latitude and long-duration balloon flight carrying the Boron And Carbon Cosmic Rays in the Upper Stratosphere (BACCUS) experimental hardware. Investigation of the biological effects of Galactic Cosmic Radiation (GCR) particularly those of ions with High-Z and Energy (HZE) is of interest due to the genomic damage this type of radiation inflicts. The biological effects of upper-stratospheric mixed radiation above Antarctica (ANT) were sampled using Arabidopsis thaliana seeds and were compared to those resulting from a controlled simulation of GCR at Brookhaven National Laboratory (BNL) and to laboratory control seed. The payload developed for Antarctica exposure was broadly designed to 1U CubeSat specifications (10cmx10cmx10cm <1.33kg) maintained 1 atm internal pressure and carried an internal cargo of four seed trays (about 580,000 seeds) and twelve CR-39 Solid-State Nuclear Track Detectors (SSNTDs). The irradiated seeds were recovered sterilized and grown on Petri plates for phenotypic screening. BNL and ANT M0 seeds showed significantly reduced germination rates and elevated somatic mutation rates when compared to non-irradiated controls with the BNL mutation rate also being significantly higher than that of ANT. Genomic DNA from mutants of interest was evaluated with whole-genome sequencing using PacBio SMRT technology. Sequence data revealed the presence of an array of genome structural variants in the genomes of M0 and M1 mutant plants.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-210",
+                    "mediaType": "text/html",
+                    "title": "Approaches for Surveying Cosmic Radiation Damage in Large Populations of Arabidopsis thaliana Seeds- an Antarctic Example"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-210_e2p8-wzkw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "treatment protocol",
                 "cosmic radiation",
@@ -678119,162 +678133,150 @@
                 "genotype",
                 "nucleic acid extraction"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/e2p8-wzkw",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-210_e2p8-wzkw",
-            "description": "The Cosmic Ray Exposure Sequencing Science (CRESS) payload system is a proof of concept experiment to assess the genomic impact of space radiation on seeds. CRESS was designed as a secondary payload for the December 2016 high-altitude high-latitude and long-duration balloon flight carrying the Boron And Carbon Cosmic Rays in the Upper Stratosphere (BACCUS) experimental hardware. Investigation of the biological effects of Galactic Cosmic Radiation (GCR) particularly those of ions with High-Z and Energy (HZE) is of interest due to the genomic damage this type of radiation inflicts. The biological effects of upper-stratospheric mixed radiation above Antarctica (ANT) were sampled using Arabidopsis thaliana seeds and were compared to those resulting from a controlled simulation of GCR at Brookhaven National Laboratory (BNL) and to laboratory control seed. The payload developed for Antarctica exposure was broadly designed to 1U CubeSat specifications (10cmx10cmx10cm <1.33kg) maintained 1 atm internal pressure and carried an internal cargo of four seed trays (about 580,000 seeds) and twelve CR-39 Solid-State Nuclear Track Detectors (SSNTDs). The irradiated seeds were recovered sterilized and grown on Petri plates for phenotypic screening. BNL and ANT M0 seeds showed significantly reduced germination rates and elevated somatic mutation rates when compared to non-irradiated controls with the BNL mutation rate also being significantly higher than that of ANT. Genomic DNA from mutants of interest was evaluated with whole-genome sequencing using PacBio SMRT technology. Sequence data revealed the presence of an array of genome structural variants in the genomes of M0 and M1 mutant plants.",
-            "title": "Approaches for Surveying Cosmic Radiation Damage in Large Populations of Arabidopsis thaliana Seeds- an Antarctic Example",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-210",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Approaches for Surveying Cosmic Radiation Damage in Large Populations of Arabidopsis thaliana Seeds- an Antarctic Example"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Approaches for Surveying Cosmic Radiation Damage in Large Populations of Arabidopsis thaliana Seeds- an Antarctic Example"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/329/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-03-20",
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
-            "identifier": "DASHLINK_329",
             "description": "Table explaining the naming convention and parameters of FLEA experiments performed in the laboratory.",
-            "title": "Laboratory Scenarios Description",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/x-pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/FLEA_test_profiles.pdf",
-                    "description": "FLEA test profiles.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "FLEA test profiles.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/FLEA_test_profiles.pdf",
+                    "mediaType": "application/x-pdf",
                     "title": "FLEA test profiles.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_329",
+            "issued": "2011-03-20",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/329/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Laboratory Scenarios Description"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-RWL-V1.0",
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
+            "description": "This CODMAC level 3 data set contains the key parameters of the four     Reaction wheel housekeeping.                                             In particular, it provides information on the Reaction wheel friction,   measured angular momentum & wheel direction.                             It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-rwl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-HK-3-RWL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-hk-3-rwl-v1.0",
-            "description": "This CODMAC level 3 data set contains the key parameters of the four     Reaction wheel housekeeping.                                             In particular, it provides information on the Reaction wheel friction,   measured angular momentum & wheel direction.                             It covers the period from launch in 2004, through the 3 Earth and        1 Mars flyby, plus the hibernation phases, plus the asteroid flybys      and finally covers the Prelanding, comet escort & Extension phases       of the prime target of the mission.                                      The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1).         This version V1.0 is the first version of this dataset.",
-            "title": "ROSETTA REACTION WHEEL ENGINEERING                    \n                       DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA REACTION WHEEL ENGINEERING                    \n                       DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-SCE-3-RDR-DOPPLER-HIRES-V1.0",
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
-                "ulysses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Ulysses spacecraft was occulted by the Io Plasma Torus (IPT) during its Jupiter encounter on 8 February 1992. The Ulysses dual-frequency radio subsystem used by the Ulysses Solar Corona Experiment (SCE) was utilized to measure the electron content (column density) of the IPT. In the nominal mode for radio-sounding observations, both downlinks (S-band: f_s = 2.3 GHz X-band: f_x = 8.4 GHz) are phase coherent with the uplink (S-band: f_u = 2.1 GHz). The dual-frequency radio-sounding technique exploits the dispersive nature of ionized media on the propagation of the two downlinks. The tiny Doppler shift due to plasma moving in and out of the ray path is greater at S-band than at the higher frequency X-band.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-sce-3-rdr-doppler-hires-v1.0_e2r2-grgq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-SCE-3-RDR-DOPPLER-HIRES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-sce-3-rdr-doppler-hires-v1.0_e2r2-grgq",
-            "description": "The Ulysses spacecraft was occulted by the Io Plasma Torus (IPT) during its Jupiter encounter on 8 February 1992. The Ulysses dual-frequency radio subsystem used by the Ulysses Solar Corona Experiment (SCE) was utilized to measure the electron content (column density) of the IPT. In the nominal mode for radio-sounding observations, both downlinks (S-band: f_s = 2.3 GHz X-band: f_x = 8.4 GHz) are phase coherent with the uplink (S-band: f_u = 2.1 GHz). The dual-frequency radio-sounding technique exploits the dispersive nature of ionized media on the propagation of the two downlinks. The tiny Doppler shift due to plasma moving in and out of the ray path is greater at S-band than at the higher frequency X-band.",
-            "title": "ULY JUP SCE DOPPLER HI-RES DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ULY JUP SCE DOPPLER HI-RES DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI-C-HRII%2FHRIV%2FMRI%2FITS-6-DOC-SET-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains version 3.0 of the updated collection of documentation for the raw and calibrated science data sets for the Deep Impact and EPOXI missions. This data set supersedes version 2.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-c-hrii-hriv-mri-its-6-doc-set-v3.0_e2s3-e37h",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "103p/hartley 2 (1986 e2)",
                 "hat-p-7",
@@ -678293,97 +678295,74 @@
                 "earth",
                 "deep impact"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI-C-HRII%2FHRIV%2FMRI%2FITS-6-DOC-SET-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-c-hrii-hriv-mri-its-6-doc-set-v3.0_e2s3-e37h",
-            "description": "This data set contains version 3.0 of the updated collection of documentation for the raw and calibrated science data sets for the Deep Impact and EPOXI missions. This data set supersedes version 2.0.",
-            "title": "DEEP IMPACT/EPOXI DOCUMENTATION SET V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "DEEP IMPACT/EPOXI DOCUMENTATION SET V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0834-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-08T20:58:40.000 to 2015-06-09T06:15:34.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0834-v1.0_e2s8-3bfq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0834-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0834-v1.0_e2s8-3bfq",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-08T20:58:40.000 to 2015-06-09T06:15:34.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0834 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0834 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1291967305-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS.",
-            "issued": "2016-08-03",
-            "temporal": "1992-01-01T00:00:00Z/2024-11-18T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "gravity/gravitational field",
-                "geodetics",
-                "earth science",
-                "solid earth",
-                "tectonics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carey Noll",
                 "hasEmail": "mailto:Carey.Noll@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDDIS"
-            },
-            "identifier": "C1291967305-CDDIS",
             "description": "Global Navigation Satellite System (GNSS) real-time 1 to multi-second sampled data available from the Crustal Dynamics Data Information System (CDDIS). Global Navigation Satellite System (GNSS) provide autonomous geo-spatial positioning with global coverage. GNSS real-time data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs) are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure; CDDIS began streaming real-time data from these systems in 2015. The real-time observation data from a global permanent network of ground-based receivers are transmitted from the CDDIS in 1 to multi-second intervals in raw receiver or RTCM (Radio Technical Commission for Maritime Services) format.",
-            "title": "Ground-Based Global Navigation Satellite System Data (1-second sampling, real-time streams) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -678392,672 +678371,695 @@
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_REALTIME_D_001",
-                    "description": "URL for more information about GNSS real-time data streams",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS real-time data streams",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_REALTIME_D_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1291967305-CDDIS",
+            "issued": "2016-08-03",
+            "keyword": [
+                "gravity/gravitational field",
+                "geodetics",
+                "earth science",
+                "solid earth",
+                "tectonics"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1291967305-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2024-11-18T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System Data (1-second sampling, real-time streams) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SDC-2-KEM1-V2.0",
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
-                "dust",
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-sdc-2-kem1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "dust",
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-SDC-2-KEM1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-sdc-2-kem1-v2.0",
-            "description": "This data set contains Raw data taken by the New Horizons Student Dust Counter instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019.",
-            "title": "NEW HORIZONS\n      SDC KEM1\n      RAW V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      SDC KEM1\n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V6.0",
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
+            "description": "Names, designations, and discovery circumstances for the numbered asteroids.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v6.0_e2uv-rp9f",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTNAMES-DISCOVERY-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-astnames-discovery-v6.0_e2uv-rp9f",
-            "description": "Names, designations, and discovery circumstances for the numbered asteroids.",
-            "title": "ASTEROID NAMES AND DISCOVERY V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID NAMES AND DISCOVERY V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_rmc&version=1.0",
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
+            "description": "This bundle contains rover motion counter data for Mars Exploration Rover 1 (Opportunity).",
+            "identifier": "urn:nasa:pds:mer1_rmc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amer1_rmc&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:mer1_rmc",
-            "description": "This bundle contains rover motion counter data for Mars Exploration Rover 1 (Opportunity).",
-            "title": "MER1 Rover Motion Counter Data Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER1 Rover Motion Counter Data Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0402-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-02T16:26:10.000 to 2014-11-02T21:10:38.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0402-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0402-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0402-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-02T16:26:10.000 to 2014-11-02T21:10:38.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0402 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0402 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_D_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International GNSS Service, Daily 30-second Hatanaka-compressed observation data, Greenbelt, MD, U.S.A: NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi:10.5067/GLONASS/glonass_daily_d_001",
-            "issued": "1998-01-01",
-            "temporal": "1998-01-01T00:00:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "gravity/gravitational field",
-                "earth science",
-                "solid earth",
-                "tectonics",
-                "geodetics"
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
-            "identifier": "C1419745913-CDDIS",
             "description": "This dataset consists of ground-based Global Navigation Satellite System (GNSS) GLONASS Compact Observation Data (30-second sampling, daily files) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. The GLONASS data sets from ground receivers at the CDDIS consist of observations from the Russian GLObal NAvigation Satellite System (GLONASS); Russia's GLONASS is similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure. The daily GLONASS GNSS observation files (compact) contain one day of GLONASS observation (30-second sampling) data in RINEX format from a global permanent network of ground-based receivers, one file per site. More information about these data is available on the CDDIS website at https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html.",
-            "title": "Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Compact Observation Data (30-second sampling, daily files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGLONASS_DAILY_D_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGLONASS_DAILY_D_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/glonass/data/daily",
-                    "description": "URL for retrieval of GNSS GLONASS daily compact observation data through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS GLONASS daily compact observation data through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/glonass/data/daily",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html",
-                    "description": "URL for more information about daily GNSS GLONASS compact observation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about daily GNSS GLONASS compact observation data",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/10.5067/GNSS/GLONASS_DAILY_D_001",
-                    "description": "URL for more information about daily GNSS GLONASS compact observation data",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about daily GNSS GLONASS compact observation data",
+                    "downloadURL": "http://doi.org/10.5067/GNSS/GLONASS_DAILY_D_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1419745913-CDDIS",
+            "issued": "1998-01-01",
+            "keyword": [
+                "gravity/gravitational field",
+                "earth science",
+                "solid earth",
+                "tectonics",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GLONASS_DAILY_D_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1998-01-01T00:00:00Z/2025-01-20T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System GLONASS (GLObal NAvigation Satellite System) Compact Observation Data (30-second sampling, daily files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L1C10",
             "citation": "CYGNSS. 2024-06-28. CYGNSS Level 1 Calibrated Raw IF Data Record. Version 1.0. CYGNSS Level 1 Calibrated Raw IF Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-L1C10. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2020-08-21, CYGNSS Level 1 Raw Intermediate Frequency Data Record, http://clasp-research.engin.umich.edu/missions/cygnss/.",
-            "issued": "2020-07-24",
-            "temporal": "2017-02-19T23:12:08Z/2024-06-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-24",
-            "references": [
-                "https://doi.org/10.1109/JSTARS.2018.2832981"
-            ],
-            "keyword": [
-                "earth science",
-                "radar",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tim Butler",
                 "hasEmail": "mailto:butlerti@umich.edu"
             },
-            "identifier": "C2927929087-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains the first release, Version 1.0, of the CYGNSS Calibrated Raw Intermediate Frequency (IF) based L1 Product. This product includes several established signal coherence detectors, including the power-ratio P<sub>ratio</sub>, complex zero-Doppler delay waveform and full entropy E<sub>full</sub>, and a novel fast entropy detector E<sub>fast</sub>. Both entropy detectors are provided with two temporal resolutions: 2 ms and 50 ms. Several scattered signal strength products are included: Signal-to-Noise Ratio SNR, reflected power P<sub>g</sub>, reflectivity \u0393, and Normalized Bistatic Radar Cross-Section NBRCS.  Each of these products is derived using a coherent integration time of T<sub>c </sub>= 1 ms and incoherent integration times of N<sub>inc</sub> = 1000, 500, 250, 100, 50, and 2 ms. Signal strength time series at the shorter (2 and 50 ms) times provides excellent detection of land-water transitions in heterogeneous scenes. Delay Doppler Maps (DDMs) are also generated with high delay (\u2206\u03c4 = 1/16 chip) and Doppler (\u2206f= 50 Hz) resolution.  This suite of coherence detection methods can be used to detect the presence of small inland water bodies.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 1 Calibrated Raw IF Data Record",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 1 Calibrated Raw IF Version 1.0",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_CAL_RAW_IF_V1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the first release, Version 1.0, of the CYGNSS Calibrated Raw Intermediate Frequency (IF) based L1 Product. This product includes several established signal coherence detectors, including the power-ratio P<sub>ratio</sub>, complex zero-Doppler delay waveform and full entropy E<sub>full</sub>, and a novel fast entropy detector E<sub>fast</sub>. Both entropy detectors are provided with two temporal resolutions: 2 ms and 50 ms. Several scattered signal strength products are included: Signal-to-Noise Ratio SNR, reflected power P<sub>g</sub>, reflectivity \u0393, and Normalized Bistatic Radar Cross-Section NBRCS.  Each of these products is derived using a coherent integration time of T<sub>c </sub>= 1 ms and incoherent integration times of N<sub>inc</sub> = 1000, 500, 250, 100, 50, and 2 ms. Signal strength time series at the shorter (2 and 50 ms) times provides excellent detection of land-water transitions in heterogeneous scenes. Delay Doppler Maps (DDMs) are also generated with high delay (\u2206\u03c4 = 1/16 chip) and Doppler (\u2206f= 50 Hz) resolution.  This suite of coherence detection methods can be used to detect the presence of small inland water bodies.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L1C10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L1C10",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/post_processing_script/Plot_rawIF_Tracks_land.m",
-                    "description": "Matlab code to plot Raw IF Data over the land.",
                     "@type": "dcat:Distribution",
+                    "description": "Matlab code to plot Raw IF Data over the land.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/post_processing_script/Plot_rawIF_Tracks_land.m",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/07/148-0136_ATBD_L1A_DDMCalibration_Rev2_Aug2018_release.pdf",
-                    "description": "Level 1A DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0136, Rev 2, 20 Aug. 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1A DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0136, Rev 2, 20 Aug. 2018.",
+                    "downloadURL": "http://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/07/148-0136_ATBD_L1A_DDMCalibration_Rev2_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0417-1_ATBD_Calibrated_IF.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Calibrated Raw IF based L1 Data Product",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Calibrated Raw IF based L1 Data Product",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0417-1_ATBD_Calibrated_IF.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/post_processing_script/Plot_rawIF_Tracks.m",
-                    "description": "Matlab code to plot Raw IF Data over the globe.",
                     "@type": "dcat:Distribution",
+                    "description": "Matlab code to plot Raw IF Data over the globe.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/post_processing_script/Plot_rawIF_Tracks.m",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docs.google.com/spreadsheets/d/1kS6XC5JPzILl8w0ZnOn5JyFvkD9hcDxFe18rjgd6ylo/edit?usp=sharing",
-                    "description": "CYGNSS Targeting Information for Raw IF Data",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Targeting Information for Raw IF Data",
+                    "downloadURL": "https://docs.google.com/spreadsheets/d/1kS6XC5JPzILl8w0ZnOn5JyFvkD9hcDxFe18rjgd6ylo/edit?usp=sharing",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=16&t=1261",
-                    "description": "Forum Post Capturing Changes to CYGNSS Sampling Rate",
                     "@type": "dcat:Distribution",
+                    "description": "Forum Post Capturing Changes to CYGNSS Sampling Rate",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=16&t=1261",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/post_processing_script/process_rawIF_metadata.m",
-                    "description": "Matlab code to read Raw IF Metadata files.",
                     "@type": "dcat:Distribution",
+                    "description": "Matlab code to read Raw IF Metadata files.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/post_processing_script/process_rawIF_metadata.m",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/Processing_CYGNSS_RawIF_Collection_Example.pdf",
-                    "description": "60 second FM8 Raw IF data collection over Hurricane Harvey Example",
                     "@type": "dcat:Distribution",
+                    "description": "60 second FM8 Raw IF data collection over Hurricane Harvey Example",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/sw/Processing_CYGNSS_RawIF_Collection_Example.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_CAL_RAW_IF_V1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_CAL_RAW_IF_V1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0354-2_CYGNSS_RawIF_Data_File_Format.docx",
-                    "description": "CYGNSS Raw IF Dataset File Formatting and Specifications Document",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Raw IF Dataset File Formatting and Specifications Document",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0354-2_CYGNSS_RawIF_Data_File_Format.docx",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2927929087-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2927929087-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2927929087-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2927929087-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://github.com/podaac/CYGNSS-Raw-IF-Code",
-                    "description": "Complete set of C and Matlab processing code",
                     "@type": "dcat:Distribution",
+                    "description": "Complete set of C and Matlab processing code",
+                    "downloadURL": "https://github.com/podaac/CYGNSS-Raw-IF-Code",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0416-1_L1_Processed_Raw_IF_DDM_netCDF_Data_Dictionary_v1.1.xlsx",
-                    "description": "Data Dictionary",
                     "@type": "dcat:Distribution",
+                    "description": "Data Dictionary",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0416-1_L1_Processed_Raw_IF_DDM_netCDF_Data_Dictionary_v1.1.xlsx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.github.io/tutorials/",
-                    "description": "PO.DAAC Cookbook",
+                {
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC Cookbook",
+                    "downloadURL": "https://podaac.github.io/tutorials/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ieeexplore.ieee.org/abstract/document/10262085",
-                    "description": "H. Carreno-Luengo, C. S. Ruf, S. Gleason and A. Russel, \"A New Multiresolution CYGNSS Data Product for Fully and Partially Coherent Scattering,\" in IEEE Transactions on Geoscience and Remote Sensing, vol. 61, pp. 1-18, 2023, Art no. 4408118, doi: 10.1109/TGRS.2023.3318639.",
                     "@type": "dcat:Distribution",
+                    "description": "H. Carreno-Luengo, C. S. Ruf, S. Gleason and A. Russel, \"A New Multiresolution CYGNSS Data Product for Fully and Partially Coherent Scattering,\" in IEEE Transactions on Geoscience and Remote Sensing, vol. 61, pp. 1-18, 2023, Art no. 4408118, doi: 10.1109/TGRS.2023.3318639.",
+                    "downloadURL": "https://ieeexplore.ieee.org/abstract/document/10262085",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.sciencedirect.com/science/article/pii/S0034425723004479",
-                    "description": "Hugo Carreno-Luengo, Christopher S. Ruf, Scott Gleason, Anthony Russel, Detection of inland water bodies under dense biomass by CYGNSS, Remote Sensing of Environment, Volume 301, 2024, 113896, ISSN 0034-4257, https://doi.org/10.1016/j.rse.2023.113896.",
                     "@type": "dcat:Distribution",
+                    "description": "Hugo Carreno-Luengo, Christopher S. Ruf, Scott Gleason, Anthony Russel, Detection of inland water bodies under dense biomass by CYGNSS, Remote Sensing of Environment, Volume 301, 2024, 113896, ISSN 0034-4257, https://doi.org/10.1016/j.rse.2023.113896.",
+                    "downloadURL": "https://www.sciencedirect.com/science/article/pii/S0034425723004479",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_CAL_RAW_IF_V1.0.jpg",
+            "identifier": "C2927929087-POCLOUD",
+            "issued": "2020-07-24",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L1C10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-07-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1109/JSTARS.2018.2832981"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 1 Calibrated Raw IF Data Record",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2017-02-19T23:12:08Z/2024-06-17T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 1 Calibrated Raw IF Version 1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO4ESIPTJPL.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Joshua Fisher. 2019-06-20. ECO4ESIPTJPL.001. ECOSTRESS Evaporative Stress Index PT-JPL Daily L4 Global 70 m V001. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/ECOSTRESS/ECO4ESIPTJPL.001. https://doi.org/10.5067/ECOSTRESS/ECO4ESIPTJPL.001. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2018-07-15",
-            "temporal": "2018-07-15T00:00:00Z/2023-03-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-25",
-            "keyword": [
-                "atmospheric water vapor",
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
-            "identifier": "C1534730762-LPDAAC_ECS",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data over the conterminous United States (CONUS) as well as key biomes and agricultural zones around the world and selected FLUXNET (http://fluxnet.fluxdata.org/about/) validation sites. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO4ESIPTJPL Version 1 data product provides Evaporative Stress Index (ESI) data generated according to the Priestley-Taylor Jet Propulsion Laboratory (PT-JPL) algorithm described in the ECOSTRESS Level 4 (ESI_PT-JPL) Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/342/ECO4ESIPTJPL_ATBD_V1.pdf). The ESI product is derived from the ratio of the Level 3 actual evapotranspiration (ET) to potential ET (PET) calculated as part of the algorithm. The ESI is an indicator of potential drought and plant water stress emphasizing areas of sub-optimal plant productivity.\r\n\r\nThe ECO4ESIPTJPL Version 1 data product contains layers of ESI and PET.\r\n\r\nData acquisition gaps:  ECOSTRESS was launched on June 29, 2018 and moved to autonomous science operations on August 20, 2018 following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity).",
-            "series-name": "ECO4ESIPTJPL.001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Simon Hook, Joshua Fisher",
-            "title": "ECOSTRESS Evaporative Stress Index PT-JPL Daily L4 Global 70m V001",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.10.28/ECOSTRESS_L4_ESI_PT-JPL_13099_019_20201027T175647_0601_01.1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data over the conterminous United States (CONUS) as well as key biomes and agricultural zones around the world and selected FLUXNET (http://fluxnet.fluxdata.org/about/) validation sites. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO4ESIPTJPL Version 1 data product provides Evaporative Stress Index (ESI) data generated according to the Priestley-Taylor Jet Propulsion Laboratory (PT-JPL) algorithm described in the ECOSTRESS Level 4 (ESI_PT-JPL) Algorithm Theoretical Basis Document (ATBD) (https://lpdaac.usgs.gov/documents/342/ECO4ESIPTJPL_ATBD_V1.pdf). The ESI product is derived from the ratio of the Level 3 actual evapotranspiration (ET) to potential ET (PET) calculated as part of the algorithm. The ESI is an indicator of potential drought and plant water stress emphasizing areas of sub-optimal plant productivity.\r\n\r\nThe ECO4ESIPTJPL Version 1 data product contains layers of ESI and PET.\r\n\r\nData acquisition gaps:  ECOSTRESS was launched on June 29, 2018 and moved to autonomous science operations on August 20, 2018 following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO4ESIPTJPL.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO4ESIPTJPL.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534730762-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534730762-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO4ESIPTJPL.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO4ESIPTJPL.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO4ESIPTJPL.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO4ESIPTJPL.001",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/425/ECO4ESIPTJPL_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/425/ECO4ESIPTJPL_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/342/ECO4ESIPTJPL_ATBD_V1.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/342/ECO4ESIPTJPL_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO4ESIPTJPL.001",
-                    "description": "Digital Object Identifier",
                     "@type": "dcat:Distribution",
+                    "description": "Digital Object Identifier",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO4ESIPTJPL.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/341/ECO4ESIPTJPL_ASD_V1.pdf",
-                    "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECO4ESIPTJPL product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Algorithm Specification Document (ASD) describes the computer processing used to generate the ECO4ESIPTJPL product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/341/ECO4ESIPTJPL_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.10.28/ECOSTRESS_L4_ESI_PT-JPL_13099_019_20201027T175647_0601_01.1.jpg",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.10.28/ECOSTRESS_L4_ESI_PT-JPL_13099_019_20201027T175647_0601_01.1.jpg",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOB/ECOSTRESS/ECO4ESIPTJPL.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOB/ECOSTRESS/ECO4ESIPTJPL.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2020.10.28/ECOSTRESS_L4_ESI_PT-JPL_13099_019_20201027T175647_0601_01.1.jpg",
+            "identifier": "C1534730762-LPDAAC_ECS",
+            "issued": "2018-07-15",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO4ESIPTJPL.001",
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
+            "series-name": "ECO4ESIPTJPL.001",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-07-15T00:00:00Z/2023-03-06T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Evaporative Stress Index PT-JPL Daily L4 Global 70m V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-3-JUPITER-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Alice UV Spectrograph instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-3-jupiter-v2.0_e35a-k9xz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "callisto",
                 "j2 europa",
@@ -679068,634 +679070,634 @@
                 "ganymede",
                 "j1 io"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-3-JUPITER-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-3-jupiter-v2.0_e35a-k9xz",
-            "description": "This data set contains Calibrated data taken by the New Horizons Alice UV Spectrograph instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-WAMOS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kyla Druska. 2019-03-28. SPURS-2 research vessel along track WAMOS wave radar data for the second R/V Revelle cruise in the E. Tropical Pacific. Version 1.0. SPURS Field Campaign WAMOS Products. Applied Physics Laboratory, University of Washington, Seattle, WA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-WAMOS. http://podaac.jpl.nasa.gov/SPURS. Kyla Druska, SPURS Data Management PI, Fred Bingham, 2019-03-28, SPURS-2 research vessel along track WAMOS wave radar data for the second R/V Revelle cruise in the E. Tropical Pacific, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-02-26",
-            "temporal": "2017-10-05T20:13:15Z/2017-11-16T23:26:01Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-02-26",
-            "keyword": [
-                "earth science",
-                "ocean circulation",
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
-            "identifier": "C2491772361-POCLOUD",
-            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent.  The WaMoS wave radar instrument was available during the second R/V Revelle cruise of SPURS-2.  WaMoS is a radar-based wave and surface current monitoring system providing wave field imagery and station time series or along track data series for key wave parameter in near near-real time. The single resulting SPURS-2 WaMos data file contains along track wave measurement from the R/V Revelle over the duration of this cruise (5 Oct. to 16 Nov. 2017) for the following essential wave field parameters: wave period, wave length, and wave direction, as well as surface current speed and direction.",
-            "release-place": "Applied Physics Laboratory, University of Washington, Seattle, WA, USA",
-            "series-name": "SPURS-2 research vessel along track WAMOS wave radar data for the second R/V Revelle cruise in the E. Tropical Pacific",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Kyla Druska",
-            "title": "SPURS-2 research vessel along track WAMOS wave radar data for the second R/V Revelle cruise in the E. Tropical Pacific",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_WAMOS.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is NASA-funded oceanographic process study and associated field program that aim to elucidate key mechanisms responsible for near-surface salinity variations in the oceans. The project involves two field campaigns and a series of cruises in regions of the Atlantic and Pacific Oceans exhibiting salinity extremes. SPURS employs a suite of state-of-the-art in-situ sampling technologies that, combined with remotely sensed salinity fields from the Aquarius/SAC-D, SMAP and SMOS satellites, provide a detailed characterization of salinity structure over a continuum of spatio-temporal scales. The SPURS-2 campaign involved two month-long cruises by the R/V Revelle in August 2016 and October 2017 combined with complementary sampling on a more continuous basis over this period by the schooner Lady Amber. Focused around a central mooring located near 10N,125W, the objective of SPURS-2 was to study the dynamics of the rainfall-dominated surface ocean at the western edge of the eastern Pacific fresh pool subject to high seasonal variability and strong zonal flows associated with the North Equatorial Current and Countercurrent.  The WaMoS wave radar instrument was available during the second R/V Revelle cruise of SPURS-2.  WaMoS is a radar-based wave and surface current monitoring system providing wave field imagery and station time series or along track data series for key wave parameter in near near-real time. The single resulting SPURS-2 WaMos data file contains along track wave measurement from the R/V Revelle over the duration of this cruise (5 Oct. to 16 Nov. 2017) for the following essential wave field parameters: wave period, wave length, and wave direction, as well as surface current speed and direction.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-WAMOS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-WAMOS",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_WAMOS.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_WAMOS.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772361-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491772361-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772361-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491772361-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_WAMOS.jpg",
+            "identifier": "C2491772361-POCLOUD",
+            "issued": "2019-02-26",
+            "keyword": [
+                "earth science",
+                "ocean circulation",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-WAMOS",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-02-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Applied Physics Laboratory, University of Washington, Seattle, WA, USA",
+            "series-name": "SPURS-2 research vessel along track WAMOS wave radar data for the second R/V Revelle cruise in the E. Tropical Pacific",
             "spatial": "-125.57 5.06 -119.89 24.2",
+            "temporal": "2017-10-05T20:13:15Z/2017-11-16T23:26:01Z",
             "theme": [
                 "SPURS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 research vessel along track WAMOS wave radar data for the second R/V Revelle cruise in the E. Tropical Pacific"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/HSRL2_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2024-08-09. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/HSRL2_1.",
-            "issued": "2023-06-24",
-            "temporal": "2023-06-24T00:00:00Z/2023-08-16T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-15",
-            "keyword": [
-                "spectral/engineering",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "aerosols",
-                "clouds",
-                "earth science",
-                "lidar"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Johnathan Hair",
                 "hasEmail": "mailto:john.t.mcgrath@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2862479332-LARC_CLOUD",
             "description": "STAQS_AircraftRemoteSensing_JSC-GV_HSRL2_Data is the remotely sensed trace gas data for the JSC Gulfstream V aircraft taken by the High Spectral Resolution Lidar-2 (HSRL-2) as part of the Synergistic TEMPO Air Quality Science (STAQS) mission. Data collection for this product is complete.\r\n\r\nLaunched in April 2023, NASA\u2019s Tropospheric Emissions: Monitoring of Pollution (TEMPO) satellite monitors major air pollutants across North America every daylight hour at high spatial resolution at a geostationary orbit (GEO). With these measurements, NASA\u2019s STAQS mission seeks to integrate TEMPO satellite observations with traditional air quality monitoring to improve understanding of air quality science and enhance societal benefit. STAQS is being conducted during summer 2023, targeting urban areas, including Los Angeles, New York City, and Chicago. As part of the mission two aircraft will be outfitted with various remote sensing payloads. The Johnson Space Center (JSC) Gulfstream-V (G-V) aircraft will feature the GeoCAPE Airborne Simulator (GCAS) and combined High Spectral Resolution Lidar-2 (HSRL-2) and Ozone Differential Absorption Lidar (DIAL). This payload provides repeated high-resolution mapping of NO2, HCHO, ozone, and aerosols up to 3x per day over targeted cities. NASA Langley Research Center\u2019s (LaRC\u2019s) Gulfstream-III will measure city-scale emissions 2x per day over the targeted cities with the High-Altitude Lidar Observatory (HALO) and Airborne Visible InfraRed Imaging Spectrometer \u2013 Next Generation (AVIRS-NG). STAQS will also incorporate ground-based tropospheric ozone profiles from the NASA Tropospheric Ozone Lidar Network (TOLNet), NO2, HCHO, and ozone measurements from Pandora spectrometers, and will leverage existing networks operated by the EPA and state air quality agencies. The primary goal of STAQS is to improve our current understanding of air quality science under the TEMPO field of regard. Further goals include evaluating TEMPO level 2 data products, interpreting the temporal and spatial evolution of air quality events tracked by TEMPO, improving temporal estimates of anthropogenic, biogenic, and greenhouse gas emissions, assessing the benefit of assimilating TEMPO data into chemical transport models, and linking air quality patterns to socio-demographic data.",
-            "title": "STAQS JSC GV High Spectral Resolution Lidar-2 Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTAQS%2FDATA001%2FGV%2FAircraftRemoteSensing%2FHSRL2_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSTAQS%2FDATA001%2FGV%2FAircraftRemoteSensing%2FHSRL2_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/staqs/",
-                    "description": "STAQS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "STAQS Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/staqs/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/staqs/content/STAQS",
-                    "description": "STAQS ESPO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "STAQS ESPO Home Page",
+                    "downloadURL": "https://espo.nasa.gov/staqs/content/STAQS",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://csl.noaa.gov/projects/ages/staqs/",
-                    "description": "NOAA CSL Overview of STAQS",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA CSL Overview of STAQS",
+                    "downloadURL": "https://csl.noaa.gov/projects/ages/staqs/",
+                    "mediaType": "text/html",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2862479332-LARC_CLOUD",
-                    "description": "Earthdata Search for STAQS_AircraftRemoteSensing_JSC-GV_HSRL2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for STAQS_AircraftRemoteSensing_JSC-GV_HSRL2_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2862479332-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/HSRL2_1",
-                    "description": "DOI data set landing page for STAQS_AircraftRemoteSensing_JSC-GV_HSRL2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for STAQS_AircraftRemoteSensing_JSC-GV_HSRL2_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/HSRL2_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2862479332-LARC_CLOUD",
+            "issued": "2023-06-24",
+            "keyword": [
+                "spectral/engineering",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "aerosols",
+                "clouds",
+                "earth science",
+                "lidar"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/STAQS/DATA001/GV/AircraftRemoteSensing/HSRL2_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-119.8 29.25 -72.1 44.22",
+            "temporal": "2023-06-24T00:00:00Z/2023-08-16T00:00:00Z",
             "theme": [
                 "STAQS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "STAQS JSC GV High Spectral Resolution Lidar-2 Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC2-67PCHURYUMOV-M17-V3.0",
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
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc2-67pchuryumov-m17-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC2-67PCHURYUMOV-M17-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc2-67pchuryumov-m17-v3.0",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 2 mission phase, covering the period from 2015-06-02T23:25:00.000 to 2015-06-30T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 3 ESC2-MTP017 RDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 3 ESC2-MTP017 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2SUPS_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2SUPS_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmospheric temperature",
-                "air quality",
-                "atmospheric water vapor",
-                "earth science",
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
-            "identifier": "C1331182616-LARC",
             "description": "TL2SUPS_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Supplemental Profiles Special Observation Version 7 data product. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits. \r\rNadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations\u201d\r\rThe organization of data within the Swath object was based on a superset of the Upper Atmosphere Research Satellite (UARS) pressure levels used to report concentrations of trace atmospheric gases. The reporting grid was the same pressure grid used for modeling. There were 67 reporting levels from 1211.53 hPa, which allowed for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products reported values directly at the surface when possible or at the observed cloud top level. Thus in the Standard Product files, each observation could potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels were not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altitudes below the cloud top or surface, where measurements were not possible, a fill value was applied.\r\rTo minimize the duplication of information between the individual species standard products, data fields common to each species (such as spacecraft",
-            "title": "TES/Aura L2 Supplemental Profiles Special Observation V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2SUPS_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2SUPS_L2.007",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182616-LARC",
-                    "description": "Earthdata Search for TL2SUPS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2SUPS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182616-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
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
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2SUPS_L2.007",
-                    "description": "DOI data set landing page for TL2SUPS_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2SUPS_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2SUPS_L2.007",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2Limb.cgi",
-                    "description": "Report of TES Level 2 Limb Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Limb Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/tes_L2Limb.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV7_0_Sep_27_2018_FV-2.pdf",
-                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Level 2 (L2) Data User\u2019s Guide (Up to & including Version 7 data) - Version 7.0",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System (EOS) Tropospheric Emission Spectrometer (TES) Level 2 (L2) Data User\u2019s Guide (Up to & including Version 7 data) - Version 7.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV7_0_Sep_27_2018_FV-2.pdf",
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
-                    "downloadURL": "https://aura.gsfc.nasa.gov/",
-                    "description": "AURA Instrument Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "AURA Instrument Home Page",
+                    "downloadURL": "https://aura.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gs614-avdc1-pz.gsfc.nasa.gov/Overview/",
-                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena, CA, USA",
                     "@type": "dcat:Distribution",
+                    "description": "EOS Aura Science Team Meeting AGENDA, August 27 - August 29, 2019 Pasadena, CA, USA",
+                    "downloadURL": "https://gs614-avdc1-pz.gsfc.nasa.gov/Overview/",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1251/NASA_SOP_2006_On_the_trail_of_global_pollution_drift.pdf",
-                    "description": "Earth Observing System Data and Information System (EOSDIS) Article: On the trail of global pollution drift",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Observing System Data and Information System (EOSDIS) Article: On the trail of global pollution drift",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1251/NASA_SOP_2006_On_the_trail_of_global_pollution_drift.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/ASDC_TES_Overview_2015.pdf",
-                    "description": "Overview of TES Data at the ASDC - 2015",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of TES Data at the ASDC - 2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/ASDC_TES_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tes.jpl.nasa.gov/data/processing-calendar/",
-                    "description": "TES Data Processing Calendar",
                     "@type": "dcat:Distribution",
+                    "description": "TES Data Processing Calendar",
+                    "downloadURL": "https://tes.jpl.nasa.gov/data/processing-calendar/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
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
-                    "downloadURL": "https://subset.larc.nasa.gov/tes/login.php",
-                    "description": "TES Search and Subsetting Web Application",
                     "@type": "dcat:Distribution",
+                    "description": "TES Search and Subsetting Web Application",
+                    "downloadURL": "https://subset.larc.nasa.gov/tes/login.php",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2SUPS.007/",
-                    "description": "ASDC Direct Data Download for TL2SUPS.007",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2SUPS.007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2SUPS.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2SUPS.007/contents.html",
-                    "description": "OPeNDAP data access for TL2SUPS.007",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2SUPS.007",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2SUPS.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://portal.hdfgroup.org/display/support",
-                    "description": "HDF Support Portal",
                     "@type": "dcat:Distribution",
+                    "description": "HDF Support Portal",
+                    "downloadURL": "https://portal.hdfgroup.org/display/support",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 }
             ],
+            "identifier": "C1331182616-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmospheric temperature",
+                "air quality",
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2SUPS_L2.007",
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
+            "title": "TES/Aura L2 Supplemental Profiles Special Observation V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/METSTATION/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Williams, Christopher.2012. GPM GROUND VALIDATION NOAA SURFACE METEOROLOGICAL STATION MC3E [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/MC3E/METSTATION/DATA001",
-            "issued": "2012-08-28",
-            "temporal": "2011-04-05T00:00:00Z/2011-06-07T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-24",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "earth science",
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
-            "identifier": "C1979815678-GHRC_DAAC",
             "description": "The GPM Ground Validation NOAA Surface Meteorological Station MC3E dataset was collected at the NOAA Southern Great Plains Facility for the Midlatitude Continental Convective Clouds Experiment (MC3E) and includes measurements of wind speed, wind direction, temperature, humidity and precipitation. The overarching goal was to provide the most complete characterization of convective cloud systems, precipitation, and the environment that has ever been obtained, providing constraints for model cumulus parameterizations and space-based rainfall retrieval algorithms over land that had never before been available. The instruments gathering this data were respectively a propeller wind monitor located 10 meters above the ground, a temperature and humidity sensor at the ground, and a tipping rain gauge at the ground. These data were collected from April 5, 2011 to June 7, 2011.",
-            "title": "GPM GROUND VALIDATION NOAA SURFACE METEOROLOGICAL STATION MC3E V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FMETSTATION%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FMC3E%2FMETSTATION%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsurmetmc3e",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmsurmetmc3e",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/MC3E/DATA101",
-                    "description": "MC3E Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "MC3E Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/MC3E/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmsurmetmc3e/gpmsurmetmc3e_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/gpmgv/mc3e/gpmsurmetmc3e/gpmsurmetmc3e_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/mc3e/gpmsurmetmc3e/MC3E_NOAA_Surface_Met_Description_2012_08_23v1.pdf",
-                    "description": "PI Readme",
                     "@type": "dcat:Distribution",
+                    "description": "PI Readme",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/gpmgv/mc3e/gpmsurmetmc3e/MC3E_NOAA_Surface_Met_Description_2012_08_23v1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/mc3e",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/mc3e",
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
+            "identifier": "C1979815678-GHRC_DAAC",
+            "issued": "2012-08-28",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "earth science",
+                "precipitation",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/MC3E/METSTATION/DATA001",
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
             "spatial": "-97.49 36.61 -97.49 36.61",
+            "temporal": "2011-04-05T00:00:00Z/2011-06-07T23:59:59Z",
             "theme": [
                 "MC3E",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION NOAA SURFACE METEOROLOGICAL STATION MC3E V1"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-e-ssi-2-redr-v1.0_e3qh-3kga",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "earth",
                 "comet sl9/jupiter collision",
@@ -679704,151 +679706,127 @@
                 "black sky",
                 "moon"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V%2FE-SSI-2-REDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-e-ssi-2-redr-v1.0_e3qh-3kga",
-            "description": "not applicable",
-            "title": "GALILEO VENUS AND EARTH SOLID STATE IMAGING 2 RAW EDR V1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO VENUS AND EARTH SOLID STATE IMAGING 2 RAW EDR V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000484-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "2009-03-03",
-            "temporal": "2006-02-15T00:00:00Z/2006-05-15T23:59:59Z",
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
-            "identifier": "C1000000484-LARC_ASDC",
             "description": "INTEX-B C-130 Aircraft data.",
-            "title": "INTEXB_C130_AIRCRAFT",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000484-LARC_ASDC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000484-LARC_ASDC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1000000484-LARC_ASDC",
+            "issued": "2009-03-03",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000484-LARC_ASDC.html",
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
+            "temporal": "2006-02-15T00:00:00Z/2006-05-15T23:59:59Z",
             "theme": [
                 "INTEXB",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "INTEXB_C130_AIRCRAFT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-DIGR3-V1.0",
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
+            "description": "The Cassini Radio Science Dione Gravity Science Experiment (DIGR3) Raw Data Archive is a time-ordered collection of radio science raw data acquired on December 11 and 12, 2011, during the Cassini Extended-Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-digr3-v1.0_e3sf-c2pa",
+            "issued": "2018-06-26",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-DIGR3-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-digr3-v1.0_e3sf-c2pa",
-            "description": "The Cassini Radio Science Dione Gravity Science Experiment (DIGR3) Raw Data Archive is a time-ordered collection of radio science raw data acquired on December 11 and 12, 2011, during the Cassini Extended-Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - SAGR12 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI RSS RAW DATA SET - SAGR12 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3321",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schwartz, M., Livesey, N., Read, W., and Fuller, R.. 2020-04-20. ML3DZT. Version 004. MLS/Aura Level 3 Daily Binned Temperature on Zonal and Similar Grids V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3321. https://disc.gsfc.nasa.gov/datacollection/ML3DZT_004.html. Digital Science Data.",
-            "issued": "2020-03-06",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-06",
-            "keyword": [
-                "atmosphere",
-                "atmospheric temperature",
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
-            "identifier": "C1725338316-GES_DISC",
-            "description": "ML3DZT is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for temperature derived from radiances measured by the 118 and 240 GHz radiometers. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is from 261 to 0.001 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3DZT data product should read chapter 4 and section 3.22 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3DZT",
             "creator": "Schwartz, M., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Daily Binned Temperature on Zonal and Similar Grids V004 (ML3DZT) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZT_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3DZT is the EOS Aura Microwave Limb Sounder (MLS) daily binned on zonal and assorted vertical grids product for temperature derived from radiances measured by the 118 and 240 GHz radiometers. The data version is 4.2. Spatial coverage is near-global (-82 to +82 degrees latitude) at 4 degree latitude zonal increments. The recommended useful vertical range is from 261 to 0.001 hPa, and the vertical resolution is between 3 and 6 km. Users of the ML3DZT data product should read chapter 4 and section 3.22 of the EOS MLS Level 2 Version 4 Quality Document for more information.\n\nThe data files contain one year of data and are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains four group objects: lat vs pressure zonal mean, lat vs \"potential temperature\" zonal mean, \"equivalent latitude\" vs \"potential temperature\" zonal mean, and vortex average vs \"potential temperature\". Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3321",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3321",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -679858,349 +679836,349 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZT_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3DZT_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZT.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3DZT.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZT.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3DZT.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZT_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3DZT_004",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3DZT_004.png",
+            "identifier": "C1725338316-GES_DISC",
+            "issued": "2020-03-06",
+            "keyword": [
+                "atmosphere",
+                "atmospheric temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3321",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML3DZT",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Daily Binned Temperature on Zonal and Similar Grids V004 (ML3DZT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SPUR2-XBIMG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Elizabeth J. Thompson, Haonan Chen. 2019-10-24. SPURS-2 X-band radar backscatter data for the E. Tropical Pacific field campaign. Version 1.0. Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA. Archived by National Aeronautics and Space Administration, U.S. Government, SPURS Data Management PI, Fred Bingham. https://doi.org/10.5067/SPUR2-XBIMG. http://podaac.jpl.nasa.gov/SPURS. Elizabeth J. Thompson, Haonan Chen, SPURS Data Management PI, Fred Bingham, 2019-10-24, SPURS-2 PICO mooring data for the E. Tropical Pacific field campaign, http://podaac.jpl.nasa.gov/SPURS.",
-            "issued": "2019-05-30",
-            "temporal": "2016-08-31T00:00:00Z/2016-09-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-22",
-            "references": [
-                "https://doi.org/10.5670/oceanog.2019.213"
-            ],
-            "keyword": [
-                "earth science",
-                "precipitation",
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
-            "identifier": "C2931233351-POCLOUD",
-            "description": "The SPURS-2 X-band marine navigation radar image dataset was collected from the ship during both the 2016 and 2017 cruises. The dataset consists of screenshots of rain echoes captured directly from the science-use X-band marine navigation radar. Raw data could not be saved. The screenshots show qualitative (uncalibrated) echoes of backscatter from rain. For full details on the screenshots, how they should be used, and what they show about rainfall, please refer to our publication: Thompson, E.J., W.E. Asher, A.T. Jessup, and K. Drushka. 2019. High-Resolution Rain Maps from an X-band Marine Radar and Their Use in Understanding Ocean Freshening. Oceanography 32(2):58\u201365, https://doi.org/10.5670/oceanog.2019.213 . The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aims to elucidate key mechanisms responsible for near-surface salinity variations in the oceans.",
-            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Elizabeth J. Thompson, Haonan Chen",
-            "title": "SPURS-2 shipboard X-band radar backscatter images for the 2016 E. Tropical Pacific field campaign",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_MOORING_PICO.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The SPURS-2 X-band marine navigation radar image dataset was collected from the ship during both the 2016 and 2017 cruises. The dataset consists of screenshots of rain echoes captured directly from the science-use X-band marine navigation radar. Raw data could not be saved. The screenshots show qualitative (uncalibrated) echoes of backscatter from rain. For full details on the screenshots, how they should be used, and what they show about rainfall, please refer to our publication: Thompson, E.J., W.E. Asher, A.T. Jessup, and K. Drushka. 2019. High-Resolution Rain Maps from an X-band Marine Radar and Their Use in Understanding Ocean Freshening. Oceanography 32(2):58\u201365, https://doi.org/10.5670/oceanog.2019.213 . The SPURS (Salinity Processes in the Upper Ocean Regional Study) project is a NASA-funded oceanographic process study and associated field program that aims to elucidate key mechanisms responsible for near-surface salinity variations in the oceans.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-XBIMG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSPUR2-XBIMG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2016-Cruise-Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2017-cruise-report-v1.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2017-cruise-report-v1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_MOORING_PICO.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_MOORING_PICO.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2017-cruise-report-v1.pdf",
-                    "description": "Cruise Reports",
                     "@type": "dcat:Distribution",
+                    "description": "Cruise Reports",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/CruiseReports/SPURS2-2017-cruise-report-v1.pdf",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2931233351-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2931233351-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2931233351-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2931233351-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/SPURS-2_Data_Report.pdf",
-                    "description": "SPURS-2 Data Report",
                     "@type": "dcat:Distribution",
+                    "description": "SPURS-2 Data Report",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/insitu/open/L2/spurs2/docs/DataDocumentation/SPURS-2_Data_Report.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SPURS2_MOORING_PICO.jpg",
+            "identifier": "C2931233351-POCLOUD",
+            "issued": "2019-05-30",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SPUR2-XBIMG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-09-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.5670/oceanog.2019.213"
+            ],
+            "release-place": "Department of Physics and Physical Oceanography, University on North Carolina, Wilmington, NC, USA",
             "spatial": "-129.131 8.927 -122.151 10.355",
+            "temporal": "2016-08-31T00:00:00Z/2016-09-22T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SPURS-2 shipboard X-band radar backscatter images for the 2016 E. Tropical Pacific field campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-2-EDR-CRUISE4-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-2-edr-cruise4-v1.0_e45t-3gk7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar system",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-2-EDR-CRUISE4-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-2-edr-cruise4-v1.0_e45t-3gk7",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR NLR DATA FOR CRUISE4",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEAR NLR DATA FOR CRUISE4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9%2FVO1%2FVO2-M-ISS%2FVIS-5-CLOUD-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of a catalog of clouds observed in Mariner 9 and Viking Orbiter images. Seven 'cloud types' were defined according to easily observable objective morphologic criteria. The entire Mariner 9 and Viking Orbiter image data sets (approximately 7400 and over 50000 images, respectively) were examined at least twice, by two separate observers. Cloud occurrences were compiled by examining images for specific cloud morphologies, examining the same area at different times, utilizing limb images, and consulting photomosaics to determine the spatial relations of cloud obscurations.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-vo1-vo2-m-iss-vis-5-cloud-v1.0_e47k-j3hs",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mariner71",
                 "mars",
                 "viking"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9%2FVO1%2FVO2-M-ISS%2FVIS-5-CLOUD-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-vo1-vo2-m-iss-vis-5-cloud-v1.0_e47k-j3hs",
-            "description": "This data set consists of a catalog of clouds observed in Mariner 9 and Viking Orbiter images. Seven 'cloud types' were defined according to easily observable objective morphologic criteria. The entire Mariner 9 and Viking Orbiter image data sets (approximately 7400 and over 50000 images, respectively) were examined at least twice, by two separate observers. Cloud occurrences were compiled by examining images for specific cloud morphologies, examining the same area at different times, utilizing limb images, and consulting photomosaics to determine the spatial relations of cloud obscurations.",
-            "title": "MR9/VO1/VO2 MARS IMAGING SCIENCE SUBSYSTEM/VIS 5 CLOUD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MR9/VO1/VO2 MARS IMAGING SCIENCE SUBSYSTEM/VIS 5 CLOUD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0595-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-21T22:31:25.000 to 2015-02-22T00:42:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0595-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0595-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0595-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2015-02-21T22:31:25.000 to 2015-02-22T00:42:59.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0595 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0595 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/T65MHVFVK1J1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee. 2024-06-01. OCO2_L2_IMAPDOAS. Version 11.2r. OCO-2 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP) V11.2r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/T65MHVFVK1J1. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_IMAPDOAS_11.2r.html. Digital Science Data.",
-            "issued": "2024-04-01",
-            "temporal": "2019-11-30T00:00:00Z/2024-10-07T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-01",
-            "keyword": [
-                "atmosphere",
-                "earth science",
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
-            "identifier": "C3090466573-GES_DISC",
-            "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection encompass the output from the IMAP-DOAS preprocessor, which is used for both screening of the official XCO2 product as well as for the retrieval of Solar-Induced Fluorescence from the 0.76 micrometer O2 A-band. The IMAP-DOAS preprocessor, just as the ABO2 cloud screen, is implemented in the operational OCO-2 processing pipeline.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_IMAPDOAS",
             "creator": "OCO-2/OCO-3 Science Team, Vivienne Payne, Abhishek Chatterjee",
-            "title": "OCO-2 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP) Retrospective Processing V11.2r (OCO2_L2_IMAPDOAS) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11.2r is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.2r.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. This collection encompass the output from the IMAP-DOAS preprocessor, which is used for both screening of the official XCO2 product as well as for the retrieval of Solar-Induced Fluorescence from the 0.76 micrometer O2 A-band. The IMAP-DOAS preprocessor, just as the ABO2 cloud screen, is implemented in the operational OCO-2 processing pipeline.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FT65MHVFVK1J1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FT65MHVFVK1J1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -680210,59 +680188,59 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_IMAPDOAS_11.2r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_IMAPDOAS_11.2r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_IMAPDOAS.11.2r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_IMAPDOAS.11.2r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_IMAPDOAS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_IMAPDOAS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_IMAPDOAS.11.2r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_IMAPDOAS.11.2r/contents.html",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_DQ_Statement_v11.2.pdf",
-                    "description": "Data Quality document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_L2_DQ_Statement_v11.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
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
@@ -680272,79 +680250,79 @@
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
+            "identifier": "C3090466573-GES_DISC",
+            "issued": "2024-04-01",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/T65MHVFVK1J1",
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
+            "series-name": "OCO2_L2_IMAPDOAS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2024-10-07T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 spatially ordered geolocated retrievals screened using the IMAP-DOAS Preprocessor (IDP) Retrospective Processing V11.2r (OCO2_L2_IMAPDOAS) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2237418345-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2022-03-01. OCO2_Eph. Version 11. OCO-2 Level 0 spacecraft ephemerides V11. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_11.html. Digital Science Data.",
-            "issued": "2022-03-01",
-            "temporal": "2019-11-30T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-01",
-            "keyword": [
-                "spectral/engineering",
-                "platform characteristics",
-                "earth science"
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
-            "identifier": "C2237418345-GES_DISC",
-            "description": "Version 11 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectral elements.This product contains the position and velocity of the spacecraft for each orbit. It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_Eph",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 0 spacecraft ephemerides V11 (OCO2_Eph) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 11 is the current version of the data set. Older versions will no longer be available and are superseded by Version 11.\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers . Each band has 1016 spectral elements.This product contains the position and velocity of the spacecraft for each orbit. It is generated using the following input data:+ APID 20 telemetry+ Orbit Boundary File.It is essential in generating the Geolocations of the science data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -680353,1332 +680331,1333 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_11.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_Eph_11.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_Eph",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_Eph",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Eph.11/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_Eph.11/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Eph.11/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_Eph.11/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_Ephem.V5.pdf",
-                    "description": "Software Interface Specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software Interface Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_Ephem.V5.pdf",
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
+            "identifier": "C2237418345-GES_DISC",
+            "issued": "2022-03-01",
+            "keyword": [
+                "spectral/engineering",
+                "platform characteristics",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2237418345-GES_DISC.html",
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
+            "series-name": "OCO2_Eph",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2019-11-30T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 0 spacecraft ephemerides V11 (OCO2_Eph) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-ROUGHNESS-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-roughness-ops-v1.0_e4fb-jzbi",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-ROUGHNESS-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-roughness-ops-v1.0_e4fb-jzbi",
-            "description": "NULL",
-            "title": "MER 1 MARS NAVIGATION CAMERA \n                                     SURFACE ROUGH RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS NAVIGATION CAMERA \n                                     SURFACE ROUGH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHAM2-3TR82",
             "citation": "Remote Sensing Systems. 2023-02-01. GHRSST Level 3U Global Subskin Sea Surface Temperature from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite. Version 8.2. GHRSST Level 3U Global Subskin Sea Surface Temperature version 8.2 from AMSR2 on the GCOM-W satellite. Santa Rosa, CA, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Remote Sensing Systems. https://doi.org/10.5067/GHAM2-3TR82. http://www.remss.com. Remote Sensing Systems, Remote Sensing Systems, 2017-11-30, GHRSST Level 3U Global Subskin Sea Surface Temperature version 8a from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite, http://www.remss.com.",
-            "issued": "2017-09-08",
-            "temporal": "2012-07-02T23:24:00Z/2023-05-29T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-09-08",
-            "references": [
-                "https://doi.org/10.1109/IGARSS.2005.1526780"
-            ],
-            "keyword": [
-                "ocean temperature",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2600797908-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This product contains a near-real-time (NRT) Level-3U Sea Surface Temperature (SST) (identified by \"_rt_\" within the file name) for the Group for High Resolution Sea Surface Temperature (GHRSST) Project, which is derived from the Advanced Microwave Scanning Radiometer 2 (AMSR2) by Remote Sensing Systems (RSS, or REMSS). AMSR2 was launched on 18 May 2012, onboard the Global Change Observation Mission - Water (GCOM-W) satellite developed by the Japan Aerospace Exploration Agency (JAXA). The GCOM-W mission aims to establish the global and long-term observation system to collect data, which is needed to understand mechanisms of climate and water cycle variations, and demonstrate its utilization. AMSR2 onboard the first generation of the GCOM-W satellite will continue Aqua/AMSR-E observations of water vapor, cloud liquid water, precipitation, SST, sea surface wind speed, sea ice concentration, snow depth, and soil moisture. AMSR2 is a remote sensing instrument for measuring weak microwave emission from the surface and the atmosphere of the Earth. The antenna of AMSR2 rotates once per 1.5 seconds and obtains data over a 1450 km swath. This conical scan mechanism enables AMSR2 to acquire a set of daytime and nighttime data with more than 99% coverage of the Earth every 2 days. The NRT SST is made as available as soon as possible, generally within 3 hours latency. The v8.2 supersedes the previous v8a dataset which can be found at https://www.doi.org/10.5067/GHAM2-3TR8A.",
-            "release-place": "Santa Rosa, CA, USA",
-            "series-name": "GHRSST Level 3U Global Subskin Sea Surface Temperature from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite",
             "creator": "Remote Sensing Systems",
-            "title": "GHRSST Level 3U Global Global Near-Real Subskin Sea Surface Temperature version 8.2 (v8.2) from the Advanced Microwave Scanning Radiometer 2 (AMSR2) on the GCOM-W satellite by REMSS",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AMSR2-REMSS-L3U-v8a.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This product contains a near-real-time (NRT) Level-3U Sea Surface Temperature (SST) (identified by \"_rt_\" within the file name) for the Group for High Resolution Sea Surface Temperature (GHRSST) Project, which is derived from the Advanced Microwave Scanning Radiometer 2 (AMSR2) by Remote Sensing Systems (RSS, or REMSS). AMSR2 was launched on 18 May 2012, onboard the Global Change Observation Mission - Water (GCOM-W) satellite developed by the Japan Aerospace Exploration Agency (JAXA). The GCOM-W mission aims to establish the global and long-term observation system to collect data, which is needed to understand mechanisms of climate and water cycle variations, and demonstrate its utilization. AMSR2 onboard the first generation of the GCOM-W satellite will continue Aqua/AMSR-E observations of water vapor, cloud liquid water, precipitation, SST, sea surface wind speed, sea ice concentration, snow depth, and soil moisture. AMSR2 is a remote sensing instrument for measuring weak microwave emission from the surface and the atmosphere of the Earth. The antenna of AMSR2 rotates once per 1.5 seconds and obtains data over a 1450 km swath. This conical scan mechanism enables AMSR2 to acquire a set of daytime and nighttime data with more than 99% coverage of the Earth every 2 days. The NRT SST is made as available as soon as possible, generally within 3 hours latency. The v8.2 supersedes the previous v8a dataset which can be found at https://www.doi.org/10.5067/GHAM2-3TR8A.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHAM2-3TR82",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHAM2-3TR82",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AMSR2-REMSS-L3U-v8a.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AMSR2-REMSS-L3U-v8a.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/SeaSurfaceTemperature",
-                    "description": "Sea Surface Temperature measurement description.",
                     "@type": "dcat:Distribution",
+                    "description": "Sea Surface Temperature measurement description.",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/SeaSurfaceTemperature",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "http://suzaku.eorc.jaxa.jp/GCOM_W/w_amsr2/whats_amsr2.html",
-                    "description": "Full details of the AMSR2",
                     "@type": "dcat:Distribution",
+                    "description": "Full details of the AMSR2",
+                    "downloadURL": "http://suzaku.eorc.jaxa.jp/GCOM_W/w_amsr2/whats_amsr2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.remss.com/missions/amsr/",
-                    "description": "Samples, Interface Control Document describing file contents, background ppt and other info",
                     "@type": "dcat:Distribution",
+                    "description": "Samples, Interface Control Document describing file contents, background ppt and other info",
+                    "downloadURL": "http://www.remss.com/missions/amsr/",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2600797908-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2600797908-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2600797908-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2600797908-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AMSR2-REMSS-L3U-v8a.jpg",
+            "identifier": "C2600797908-POCLOUD",
+            "issued": "2017-09-08",
+            "keyword": [
+                "ocean temperature",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHAM2-3TR82",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-09-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1109/IGARSS.2005.1526780"
+            ],
+            "release-place": "Santa Rosa, CA, USA",
+            "series-name": "GHRSST Level 3U Global Subskin Sea Surface Temperature from the Advanced Microwave Scanning Radiometer 2 on the GCOM-W satellite",
             "spatial": "-179.0 -90.0 180.0 90.0",
+            "temporal": "2012-07-02T23:24:00Z/2023-05-29T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 3U Global Global Near-Real Subskin Sea Surface Temperature version 8.2 (v8.2) from the Advanced Microwave Scanning Radiometer 2 (AMSR2) on the GCOM-W satellite by REMSS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/923",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Keller, M.M., and M.W. Palace. 2009. LBA-ECO TG-07 Ground-based Biometry Data at km 83 Site, Tapajos National Forest: 1997. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/923",
-            "issued": "2023-10-03",
-            "temporal": "1997-03-01T00:00:00Z/1997-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
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
-            "identifier": "C2777750285-ORNL_CLOUD",
             "description": "A field inventory of trees was conducted in March of 1997 in a logging concession at the Tapajos National Forest, south of Santarem, Para, Brazil. The inventory was conducted by the foresters and technicians of the Tropical Forest Foundation (FFT) and included all trees with diameter at breast height greater than or equal to 35 cm. Four blocks of approximately 100 ha each within the 3,200 ha concession were inventoried. Within each block, parallel trails 50 m apart were established, and the location of each tree measured was recorded to the nearest meter using an orthogonal coordinate system based on these trails. Field data for each tree includes: identification number, ground position, diameter, common name, scientific name and qualitative estimates of bole and canopy quality. Data are provided in one ASCII comma separated file. These data were used to calculate above-ground live biomass as described in Keller et al. (2001), but biomass data are not included in this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO TG-07 Ground-based Biometry Data at km 83 Site, Tapajos National Forest: 1997",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F923",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F923",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/trace_gases/TG07_FFT_Survey_Km83/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/trace_gases/TG07_FFT_Survey_Km83/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/TG07_FFT_Survey_Km83.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/TG07_FFT_Survey_Km83.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/923",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/923",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/trace_gases/TG07_FFT_Survey_Km83/comp/TG07_FFT_Survey_Km83.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/trace_gases/TG07_FFT_Survey_Km83/comp/TG07_FFT_Survey_Km83.pdf",
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
+            "identifier": "C2777750285-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/923",
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
             "spatial": "-3.02 -54.97",
+            "temporal": "1997-03-01T00:00:00Z/1997-03-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO TG-07 Ground-based Biometry Data at km 83 Site, Tapajos National Forest: 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/484",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Way, J., R. Zimmerman, K. McDonald, and E. Rignot. 1999. BOREAS RSS-17 1994 ERS-1 Level-3 Freeze/Thaw Backscatter Change Images. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/484",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-03T00:00:00Z/1994-03-19T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-11",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "snow/ice"
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
-            "identifier": "C2929141520-ORNL_CLOUD",
             "description": "The BOREAS RSS-17 team acquired and analyzed imaging radar data from the ESA's ERS-1 over a complete annual cycle at the BOREAS sites in Canada in 1994 to detect shifts in radar backscatter related to varying environmental conditions. Two independent transitions corresponding to soil thaw and possible canopy thaw were revealed by the data.  The results demonstrated that radar provides an ability to observe thaw transitions at the beginning of the growing season, which in turn helps constrain the length of the growing season.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-17 1994 ERS-1 Level-3 Freeze/Thaw Backscatter Change Images",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F484",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F484",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rss17fth/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/rss17fth/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS17_FreezeThaw_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS17_FreezeThaw_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/484",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/484",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/restricted_readme",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/restricted_readme",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/RSS17_FreezeThaw_Maps.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/RSS17_FreezeThaw_Maps.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/RSS17_FreezeThaw_Maps.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/RSS17_FreezeThaw_Maps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/RSS17_FreezeThaw_Maps.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/rss17fth/comp/RSS17_FreezeThaw_Maps.txt",
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
+            "identifier": "C2929141520-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/484",
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
+            "temporal": "1994-01-03T00:00:00Z/1994-03-19T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-17 1994 ERS-1 Level-3 Freeze/Thaw Backscatter Change Images"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image. Note that the two datasets RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07-V1.0 and RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07B-V1.0 have been merged into one dataset: RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m07-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "bias",
                 "international rosetta mission",
                 "dark"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m07-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the PRELANDING mission phase, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image. Note that the two datasets RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07-V1.0 and RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07B-V1.0 have been merged into one dataset: RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M07-V2.0 (and higher), that covers the full time period spanned by the two previously delivered datasets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 2 PRL-MTP007 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 2 PRL-MTP007 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/760/",
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
-            "identifier": "DASHLINK_760",
             "description": "Structural damage to ball grid array interconnects incurred during vibration testing has been monitored in the prefailure space using resistance spectroscopy-based state space vectors, rate of change of the state variable, and acceleration of the state variable. The technique is intended for condition monitoring in high reliability applications where the knowledge of impending failure is critical and the risks in terms of loss of functionality are too high to bear. Future state of the system has been estimated based on a second-order Kalman Filter model and a Bayesian Framework. The measured state variable has been related to the underlying interconnect damage in the form of inelastic strain energy density. Performance of the prognostic health management algorithm during the vibration test has been quantified using performance evaluation metrics. The method- ology has been demonstrated on leadfree area-array electronic assemblies subjected to vibration. Model predictions have been correlated with experimental data. The presented approach is applicable to functional systems where corner interconnects in area-array packages may be often redundant. Prognostic metrics including \u03b1 \u2212 \u03bb precision, \u03b2 accuracy, and relative accuracy have been used to assess the performance of the damage proxies. The presented approach enables the estimation of residual life based on level of risk averseness.",
-            "title": "Prognostics Health Management of Electronic Systems Under Mechanical Shock and Vibration Using Kalman Filter Models and Metrics",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_IEEE_TIE_shock.pdf",
-                    "description": "2012_IEEE_TIE_shock.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2012_IEEE_TIE_shock.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2012_IEEE_TIE_shock.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2012_IEEE_TIE_shock.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_760",
+            "issued": "2013-06-19",
+            "keyword": [
+                "nasa",
+                "ames",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/760/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Prognostics Health Management of Electronic Systems Under Mechanical Shock and Vibration Using Kalman Filter Models and Metrics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-IOF-SCI-V1.0",
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
+            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Science RDR  data set contains Incidence Over Flux (IOF) data from the Surface  Stereo Imager (SSI).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-iof-sci-v1.0_e4tb-6iku",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-SSI-5-IOF-SCI-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-ssi-5-iof-sci-v1.0_e4tb-6iku",
-            "description": "The Surface Stereo Imager (SSI)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This SSI Imaging Science RDR  data set contains Incidence Over Flux (IOF) data from the Surface  Stereo Imager (SSI).",
-            "title": "PHOENIX MARS SURFACE STEREO IMAGER \n                                      5 INCID OVER FLX SCI V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PHOENIX MARS SURFACE STEREO IMAGER \n                                      5 INCID OVER FLX SCI V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-TNOCENALB-V1.0",
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
+            "description": "This data set is a compilation of published diameters, albedos, and densities for Transneptunian Objects (TNOs) and Centaurs. A total of 129 objects are listed, many with more than one entry. This version covers published values through 31 March 2013.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-tnocenalb-v1.0_e4u8-vs2y",
+            "issued": "2021-05-21",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-TNOCENALB-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-tnocenalb-v1.0_e4u8-vs2y",
-            "description": "This data set is a compilation of published diameters, albedos, and densities for Transneptunian Objects (TNOs) and Centaurs. A total of 129 objects are listed, many with more than one entry. This version covers published values through 31 March 2013.",
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
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD10_L2.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-02-07. MODIS/Terra Near Real Time (NRT) Snow Cover 5-Min L2 Swath 500m NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD10_L2.NRT.061. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/modis-nrt.",
-            "issued": "2021-02-07",
-            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "cryosphere",
-                "snow/ice",
-                "earth science",
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
-                "name": "NASA/GSFC/EOS/ESDIS/LANCE MODIS"
-            },
-            "identifier": "C2007659515-LANCEMODIS",
-            "description": "MODIS/Terra Near Real Time (NRT) Snow Cover 5-Min L2 Swath 500m (MOD10_L2) contains snow cover and quality assurance (QA) data, latitudes, and longitudes in HDF-EOS format, along with corresponding metadata. Latitude and longitude geolocation fields are at 5 km resolution, while all other fields are at 500 m resolution. MODIS snow cover data are based on a snow mapping algorithm that employs a Normalized Difference Snow Index (NDSI) and other criteria tests.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Terra Snow Cover 5-Min L2 Swath 500m NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "MODIS/Terra Near Real Time (NRT) Snow Cover 5-Min L2 Swath 500m (MOD10_L2) contains snow cover and quality assurance (QA) data, latitudes, and longitudes in HDF-EOS format, along with corresponding metadata. Latitude and longitude geolocation fields are at 5 km resolution, while all other fields are at 500 m resolution. MODIS snow cover data are based on a snow mapping algorithm that employs a Normalized Difference Snow Index (NDSI) and other criteria tests.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD10_L2.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD10_L2.NRT.061",
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
-                    "description": "Access Collection 6 descriptions and data sets from the MODAPS LANCE-MODIS page(DOWNLOAD server).",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6 descriptions and data sets from the MODAPS LANCE-MODIS page(DOWNLOAD server).",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LANCE"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD10_L2/",
-                    "description": "Direct access to the download site and directory hosting the MOD10_L2 6.1NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD10_L2 6.1NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD10_L2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C2007659515-LANCEMODIS",
+            "issued": "2021-02-07",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "cryosphere",
+                "snow/ice",
+                "earth science",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD10_L2.NRT.061",
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
+            "temporal": "2021-02-07T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Snow Cover 5-Min L2 Swath 500m NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/457",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Arkebauer, T.J., and S.B. Verma. 1999. BOREAS TF-11 SSA Fen Soil Surface CO2 Flux Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/457",
-            "issued": "2023-11-22",
-            "temporal": "1994-05-27T00:00:00Z/1995-10-03T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "land surface",
-                "atmospheric chemistry",
-                "atmosphere",
-                "terrestrial hydrosphere",
-                "soils",
-                "ground water",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2808091100-ORNL_CLOUD",
-            "description": "Contains the TF-11 soil surface CO2 flux data that were measured using a portable gas exchange system.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TF-11 SSA Fen Soil Surface CO2 Flux Data",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
+            },
+            "description": "Contains the TF-11 soil surface CO2 flux data that were measured using a portable gas exchange system.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F457",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F457",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf11soil/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TF/tf11soil/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF11_Soil_Surf_CO2.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TF11_Soil_Surf_CO2.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/457",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/457",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11soil/comp/tf11soil.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11soil/comp/tf11soil.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11soil/comp/TF11_Soil_Surf_CO2.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11soil/comp/TF11_Soil_Surf_CO2.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11soil/comp/TF11_Soil_Surf_CO2.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11soil/comp/TF11_Soil_Surf_CO2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11soil/comp/TF11_Soil_Surf_CO2.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TF/tf11soil/comp/TF11_Soil_Surf_CO2.txt",
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
+            "identifier": "C2808091100-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "land surface",
+                "atmospheric chemistry",
+                "atmosphere",
+                "terrestrial hydrosphere",
+                "soils",
+                "ground water",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/457",
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
+            "temporal": "1994-05-27T00:00:00Z/1995-10-03T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TF-11 SSA Fen Soil Surface CO2 Flux Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/782",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Privette, J.L., and M.M. Mukelabai. 2005. SAFARI 2000 Surface Irradiance Measurements, Mongu Tower Site, Zambia, 2000-2002. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/782",
-            "issued": "2023-10-18",
-            "temporal": "2000-09-04T00:00:00Z/2002-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-25",
-            "keyword": [
-                "atmospheric radiation",
-                "vegetation",
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
-            "identifier": "C2789647857-ORNL_CLOUD",
             "description": "This data set contains the top-of-canopy irradiance in the shortwave (0.3-2.8 micron) and photosynthetically active radiation (PAR; 0.4-0.7 micron) wavebands collected with an Eppley Precision Spectral Pyranometer (PSP) and a Skye SKE510 pyranometer, respectively. The instruments were deployed at the top of the 30-m tower in the Kataba Local Forest approximately 20 km south of Mongu in Western Province, Zambia. The data include the hourly mean and maximum values from 0500-1600 GMT (7 a.m. - 6 p.m. local time) and cover the period from September 4, 2000 to December 31, 2002. The data were obtained primarily for EOS validation and energy budget modeling.The Skye SKE510 uses a blue enhanced planar diffused silicon detector and has a fairly even response from 400 to 700 nm. The Eppley PSP is a World Meteorological Organization First Class Radiometer designed for the measurement of sun and sky radiation, totally or in defined broad wavelength bands. It comprises a circular multi-junction wire-wound thermopile. A data logger sampled the sensors at 60-second intervals and recorded the maximum and mean values every 60 minutes throughout the day.The data are contained within a single ASCII text file, in comma-separated-value format, with associated date, time, and QA information.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Surface Irradiance Measurements, Mongu Tower Site, Zambia, 2000-2002",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F782",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F782",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/mongu_irradiance/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/field_campaign/mongu_irradiance/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/mongu_irradiance.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/mongu_irradiance.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/782",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/782",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_irradiance/comp/mongu_irradiance_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/field_campaign/mongu_irradiance/comp/mongu_irradiance_readme.pdf",
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
+            "identifier": "C2789647857-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "atmospheric radiation",
+                "vegetation",
+                "earth science",
+                "biosphere",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/782",
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
             "spatial": "22.03 -16.87 24.28 -14.93",
+            "temporal": "2000-09-04T00:00:00Z/2002-12-31T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Surface Irradiance Measurements, Mongu Tower Site, Zambia, 2000-2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-2%2F3-EDR%2FRDR-NPI-EXT2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Mars Express ASPERA-3 Neutral Particle Imager (NPI) data for the second mission extension (October 1, 2007 - May 31, 2009). These data are provided in units of count rate (counts/second).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-2-3-edr-rdr-npi-ext2-v1.0_e4yn-6hxz",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars express",
                 "solar wind",
                 "mars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-2%2F3-EDR%2FRDR-NPI-EXT2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-2-3-edr-rdr-npi-ext2-v1.0_e4yn-6hxz",
-            "description": "This data set contains Mars Express ASPERA-3 Neutral Particle Imager (NPI) data for the second mission extension (October 1, 2007 - May 31, 2009). These data are provided in units of count rate (counts/second).",
-            "title": "MARS EXPRESS ASPERA-3 RAW-CAL NTRL PARTICLE IMAGER EXT2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MARS EXPRESS ASPERA-3 RAW-CAL NTRL PARTICLE IMAGER EXT2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1568",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Miles, N.L., S.J. Richardson, D.K. Martins, K.J. Davis, T. Lauvaux, B.J. Haupt, and S.K. Miller. 2018. ACT-America: L2 In Situ CO2, CO, and CH4 Concentrations from Towers, Eastern USA. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1568",
-            "issued": "2018-06-21",
-            "temporal": "2015-01-01T00:00:00Z/2017-12-31T23:59:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
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
-            "identifier": "C2706398349-ORNL_CLOUD",
             "description": "This dataset provides atmospheric carbon dioxide (CO2), carbon monoxide (CO), and methane (CH4) concentrations as measured on a network of instrumented communications towers operated by the Atmospheric Carbon and Transport-America (ACT-America) project. ACT-America's mission spans five years and includes five 6-week intensive field campaigns covering all 4 seasons and 3 regions of the central and eastern United States. Tower-based measurements began in early 2015 and are continuously collecting CO2, CO, and CH4 data to characterize ground-level (>100 m) carbon background conditions to support the periodic airborne measurement campaigns and transport modeling conducted by ACT-America. The towers are instrumented with infrared cavity ring-down spectrometer systems (CRDS; Picarro Inc.). Data are reported for the highest sampling port on each tower. The averaging interval standard deviation and uncertainty derived from periodic flask sample to in-situ measurement comparisons are provided. Complete tower location, elevation, instrument height, and date/time information are also provided.",
-            "graphic-preview-description": "Figure 1: ACT-America 2016 campaign ground tower locations.",
-            "title": "ACT-America: L2 In Situ CO2, CO, and CH4 Concentrations from Towers, Eastern USA",
-            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA-PICARRO_Ground_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1568",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1568",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/actamerica/ACTAMERICA-PICARRO_Ground/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/actamerica/ACTAMERICA-PICARRO_Ground/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA-PICARRO_Ground.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA-PICARRO_Ground.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1568",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1568",
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
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA-PICARRO_Ground/comp/ACTAMERICA-PICARRO_Ground.pdf",
-                    "description": "ACT-America: L2 In Situ CO2, CO, and CH4 Concentrations from Towers, Eastern USA: ACTAMERICA-PICARRO_Ground.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ACT-America: L2 In Situ CO2, CO, and CH4 Concentrations from Towers, Eastern USA: ACTAMERICA-PICARRO_Ground.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/actamerica/ACTAMERICA-PICARRO_Ground/comp/ACTAMERICA-PICARRO_Ground.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA-PICARRO_Ground_Fig1.png",
-                    "description": "Figure 1: ACT-America 2016 campaign ground tower locations.",
                     "@type": "dcat:Distribution",
+                    "description": "Figure 1: ACT-America 2016 campaign ground tower locations.",
+                    "downloadURL": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA-PICARRO_Ground_Fig1.png",
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
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1568/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/1568/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Figure 1: ACT-America 2016 campaign ground tower locations.",
+            "graphic-preview-file": "https://daac.ornl.gov/ACTAMERICA/guides/ACTAMERICA-PICARRO_Ground_Fig1.png",
+            "identifier": "C2706398349-ORNL_CLOUD",
+            "issued": "2018-06-21",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1568",
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
             "spatial": "-98.59 30.2 -76.42 44.05",
+            "temporal": "2015-01-01T00:00:00Z/2017-12-31T23:59:00Z",
             "theme": [
                 "ACT-America",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACT-America: L2 In Situ CO2, CO, and CH4 Concentrations from Towers, Eastern USA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3WMDS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3WMDS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "earth science",
-                "ocean winds",
-                "oceans"
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
-            "identifier": "C2491757218-POCLOUD",
-            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the\nMonthly, Descending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the\nMonthly, Descending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WMDS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3WMDS",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY_V5.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757218-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757218-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757218-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757218-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_MONTHLY_V5.jpg",
+            "identifier": "C2491757218-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "earth science",
+                "ocean winds",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3WMDS",
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
+            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Monthly Data V5.0"
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
-                "themis",
-                "accel",
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
-            "identifier": "NASA-671",
             "description": "ACCEL, THEMIS, SPICE",
-            "title": "PDS Odyssey Data Release 28",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -681686,93 +681665,89 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-671",
+            "issued": "2018-06-25",
+            "keyword": [
+                "themis",
+                "accel",
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
+            "title": "PDS Odyssey Data Release 28"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-PRL-MTP008-V1.0",
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
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Prelanding Phase from 23rd Sep 2014 to 24th Oct 2014 before reaching target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-prl-mtp008-v1.0_e55x-y88h",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-PRL-MTP008-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-prl-mtp008-v1.0_e55x-y88h",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Prelanding Phase from 23rd Sep 2014 to 24th Oct 2014 before reaching target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 PRELANDING MTP008 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 PRELANDING MTP008 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GPM/PR/TRMM/SLH/3A-DAY/07",
             "citation": "Tropical Rainfall Measuring Mission (TRMM). 2021-07-29. GPM_3HSLH_TRMM_DAY. GPM PR on TRMM Spectral Latent Heating Profiles L3 1 Day 0.5x0.5 degree V07. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GPM/PR/TRMM/SLH/3A-DAY/07. https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_TRMM_DAY_07.html. Digital Science Data.",
-            "issued": "2021-07-21",
-            "temporal": "1997-12-07T00:00:00Z/2015-04-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-21",
-            "references": [
-                "https://doi.org/10.1175/AMSMONOGRAPHS-D-15-0013.1"
-            ],
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "Tropical Rainfall Measuring Mission (TRMM)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2264132414-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This a new (GPM-formated) TRMM product. There is no equivalent in the old TRMM suite of products.\n\nVersion 07 is the current version of the data set. Older versions will no longer be available and have been superseded by Version 07.\n\nEstimating vertical profiles of latent heating released by precipitating cloud systems is one of the key objectives of TRMM, together with accurately measuring the horizontal distribution of tropical rainfall.\n\nThe method uses TRMM PR information [precipitation-top height (PTH), precipitation rates at the surface and melting level, and rain type] to select heating profiles from lookup tables. Heating-profile lookup tables for the three rain types\u2014convective, shallow stratiform, and anvil rain (deep stratiform with a melting level)\u2014were derived from numerical simulations of tropical cloud systems from the Tropical Ocean and Global Atmosphere Coupled Ocean\u2013Atmosphere Response Experiment (TOGA COARE) utilizing a cloud-resolving model (CRM). The SLH algorithm is severely limited by the inherent sensitivity of the TRMM PR. For latent heating, the quantity required is actually cloud top, but the PR can detect only precipitation-sized particles.\n\nBecause observed information on precipitation depth is used in addition to precipitation type and intensity, differences between shallow and deep convection are more distinct in the SLH algorithm in comparison with the CSH algorithm.\n\nDaily Spectral Latent Heating produces 0.5 degree x 0.5 degree grid of latent heating profiles from the TRMM PR rain. The grids are in the Planetary Grid 2 structure matching the Dual-frequency PR on the core GPM observatory that covers 67S to 67N degrees of latitudes. Areas beyond the \u00b140 degrees of latitudes are padded with empty grid cells.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "GPM_3HSLH_TRMM_DAY",
-            "creator": "Tropical Rainfall Measuring Mission (TRMM)",
-            "title": "GPM PR on TRMM Spectral Latent Heating Profiles L3 1 Day 0.5x0.5 degree V07 (GPM_3HSLH_TRMM_DAY) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3HSLH_TRMM_DAY.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FPR%2FTRMM%2FSLH%2F3A-DAY%2F07",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPM%2FPR%2FTRMM%2FSLH%2F3A-DAY%2F07",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -681782,394 +681757,398 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_TRMM_DAY_07.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GPM_3HSLH_TRMM_DAY_07.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/GPM_3HSLH_TRMM_DAY.07",
-                    "description": "Access the data via HTTPS",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/data/TRMM_L3/GPM_3HSLH_TRMM_DAY.07",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/GPM_3HSLH_TRMM_DAY.07/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://disc2.gesdisc.eosdis.nasa.gov/opendap/TRMM_L3/GPM_3HSLH_TRMM_DAY.07/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3HSLH_TRMM_DAY",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GPM_3HSLH_TRMM_DAY",
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
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/README.TRMM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/README.TRMM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/CSH_ATBD.pdf",
-                    "description": "Details of the caveats to consider in this product.",
                     "@type": "dcat:Distribution",
+                    "description": "Details of the caveats to consider in this product.",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/CSH_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/V7A_SLH_caveats.pdf",
-                    "description": "Details of the caveats to consider in this product.",
                     "@type": "dcat:Distribution",
+                    "description": "Details of the caveats to consider in this product.",
+                    "downloadURL": "https://pps.gsfc.nasa.gov/Documents/V7A_SLH_caveats.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/GPM/browse/GPM_3HSLH_TRMM_DAY.png",
+            "identifier": "C2264132414-GES_DISC",
+            "issued": "2021-07-21",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPM/PR/TRMM/SLH/3A-DAY/07",
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
+                "https://doi.org/10.1175/AMSMONOGRAPHS-D-15-0013.1"
+            ],
+            "release-place": "Greenbelt, MD",
+            "series-name": "GPM_3HSLH_TRMM_DAY",
             "spatial": "-180.0 -67.0 180.0 67.0",
+            "temporal": "1997-12-07T00:00:00Z/2015-04-01T23:59:59.999Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM PR on TRMM Spectral Latent Heating Profiles L3 1 Day 0.5x0.5 degree V07 (GPM_3HSLH_TRMM_DAY) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2792582387-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, CDDIS.",
-            "issued": "1992-01-01",
-            "temporal": "2023-10-01T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-06",
-            "keyword": [
-                "earth science",
-                "geodetics",
-                "solid earth",
-                "tectonics",
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
-            "identifier": "C2792582387-CDDIS",
             "description": "This product contains a time series of attitude quaternion components for healthy satellites in the GLONASS constellation that are accumulated every minute throughout the day. The product is generated at JPL's Global Differential GPS Operations Centers in real-time. The data in this product can be concatenated with other daily products to provide larger coverage in time.",
-            "title": "Ground-Based Global Navigation Satellite System (GNSS) GLONASS real-time POD Attitude Quaternions (30-second sampling, 60-second files) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C2792582387-CDDIS.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C2792582387-CDDIS.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C2792582387-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "earth science",
+                "geodetics",
+                "solid earth",
+                "tectonics",
+                "gravity/gravitational field"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2792582387-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-10-01T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ground-Based Global Navigation Satellite System (GNSS) GLONASS real-time POD Attitude Quaternions (30-second sampling, 60-second files) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L3C10",
             "citation": "CYGNSS. 2020-05-22. CYGNSS Level 3 Climate Data Record. Version 1.0. CYGNSS Level 3 Climate Data Record Version 1.0. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/CYGNS-L3C10. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2020-05-22, CYGNSS Level 3 Climate Data Record Version 1.0, https://cygnss.engin.umich.edu/.",
-            "issued": "2019-12-09",
-            "temporal": "2017-03-18T00:00:00Z/2021-02-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-09",
-            "references": [
-                "https://doi.org/10.1038/s41598-018-27127-4"
-            ],
-            "keyword": [
-                "oceans",
-                "ocean winds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "identifier": "C2036882064-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset contains the Version 1.0 CYGNSS Level 3 Climate Data Record which provides the average wind speed and mean square slope (MSS) on a 0.2x0.2 degree latitude by longitude equirectangular grid obtained from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. The Level 2 Delay Doppler Map (DDM) data are used in the direct processing of the average wind speed and MSS data that are binned on the Level 3 grid. A subset of DDM data used in the direct processing of the average wind speed and MSS is co-located inside of the Level 2 data files. A single netCDF-4 data file is produced for each day of operation with an approximate 2 month latency. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). The Version 1.0 CDR represents the first climate-quality release and is a collection of reanalysis products derived from the SDR v2.1 Level 1 data. Calibration accuracy and long term stability are improved relative to the SDR v2.1 using a new trackwise correction algorithm which constrains the average value of the L1 data using MERRA-2 reanalysis wind speeds. Details of the algorithm are provided in the Trackwise Corrected CDR Algorithm Theoretical Basis Document. CDR Level 2 and 3 products (ocean surface wind speed, mean square slope, and latent and sensible heat flux) are generated from the CDR L1 data using the v2.1 SDR data processing algorithms. These products also exhibit improved calibration accuracy and stability over SDR v2.1. Trackwise correction is applied to the two primary CYGNSS L1 science data products  the normalized bistatic radar cross section (NBRCS) and the leading edge slope of the Doppler-integrated delay waveform (LES). The correction compensates for variations in the transmit power level of the GPS signals measured by the CYGNSS bistatic radar receivers. The SDR v2.1 L1 algorithm assumes a constant GPS transmit power and variations in it can be misinterpreted as variations in the L1 data and in subsequent L2 science data products derived from them. The GPS constellation consists of several different satellite models (a.k.a. block types) and the level of transmit power variation differs between them. The more recent Block IIF models (which account for ~37% of the GPS constellation) have significantly larger variations than the older models and, for this reason, they have been screened out and not used to produce SDR v2.1 L2 or L3 science data products. Trackwise correction eliminates the need for this screening so CDR L2 and L3 data products now include Block IIF samples. It should be noted that the trackwise correction algorithm cannot be successfully applied to all SDR v2.1 L1 data so there is also some loss of samples that were present in SDR v2.1. Overall, there is a significant increase in sampling and improvement in spatial coverage with the CDR products.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 3 Climate Data Record",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 3 Climate Data Record Version 1.0",
-            "graphic-preview-description": "SOTO (State Of The Ocean) Visualization of CYGNSS Wind Speed",
-            "graphic-preview-file": "https://soto.podaac.earthdatacloud.nasa.gov/?l=CYGNSS_L3_Wind_Speed_Daily,BlueMarble_ShadedRelief_Bathymetry,Coastlines_15m",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains the Version 1.0 CYGNSS Level 3 Climate Data Record which provides the average wind speed and mean square slope (MSS) on a 0.2x0.2 degree latitude by longitude equirectangular grid obtained from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. The Level 2 Delay Doppler Map (DDM) data are used in the direct processing of the average wind speed and MSS data that are binned on the Level 3 grid. A subset of DDM data used in the direct processing of the average wind speed and MSS is co-located inside of the Level 2 data files. A single netCDF-4 data file is produced for each day of operation with an approximate 2 month latency. The reported sample locations are determined by the specular points corresponding to the Delay Doppler Maps (DDMs). The Version 1.0 CDR represents the first climate-quality release and is a collection of reanalysis products derived from the SDR v2.1 Level 1 data. Calibration accuracy and long term stability are improved relative to the SDR v2.1 using a new trackwise correction algorithm which constrains the average value of the L1 data using MERRA-2 reanalysis wind speeds. Details of the algorithm are provided in the Trackwise Corrected CDR Algorithm Theoretical Basis Document. CDR Level 2 and 3 products (ocean surface wind speed, mean square slope, and latent and sensible heat flux) are generated from the CDR L1 data using the v2.1 SDR data processing algorithms. These products also exhibit improved calibration accuracy and stability over SDR v2.1. Trackwise correction is applied to the two primary CYGNSS L1 science data products  the normalized bistatic radar cross section (NBRCS) and the leading edge slope of the Doppler-integrated delay waveform (LES). The correction compensates for variations in the transmit power level of the GPS signals measured by the CYGNSS bistatic radar receivers. The SDR v2.1 L1 algorithm assumes a constant GPS transmit power and variations in it can be misinterpreted as variations in the L1 data and in subsequent L2 science data products derived from them. The GPS constellation consists of several different satellite models (a.k.a. block types) and the level of transmit power variation differs between them. The more recent Block IIF models (which account for ~37% of the GPS constellation) have significantly larger variations than the older models and, for this reason, they have been screened out and not used to produce SDR v2.1 L2 or L3 science data products. Trackwise correction eliminates the need for this screening so CDR L2 and L3 data products now include Block IIF samples. It should be noted that the trackwise correction algorithm cannot be successfully applied to all SDR v2.1 L1 data so there is also some loss of samples that were present in SDR v2.1. Overall, there is a significant increase in sampling and improvement in spatial coverage with the CDR products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L3C10",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L3C10",
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
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_CDR_V1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L3_CDR_V1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
-                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser. (2019). In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser. (2019). In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0390-1_L3_v1.0_CDR_netCDF_Data_Dictionary.xlsx",
-                    "description": "Look-up table to define the Level 3 data variables",
                     "@type": "dcat:Distribution",
+                    "description": "Look-up table to define the Level 3 data variables",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0390-1_L3_v1.0_CDR_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0319_ATBD_L3_Gridded_Wind_Speed_Rev1_Aug2018_release.pdf",
-                    "description": "Level 3 Gridded Wind Speed Algorithm Theoretical Basis Document, C. Ruf, CYGNSS Project Document 148-0319, Rev 1, 20 Aug. 2018.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 3 Gridded Wind Speed Algorithm Theoretical Basis Document, C. Ruf, CYGNSS Project Document 148-0319, Rev 1, 20 Aug. 2018.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0319_ATBD_L3_Gridded_Wind_Speed_Rev1_Aug2018_release.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00218.1",
-                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-14-00218.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0389-1_ATBD_Trackwise_Corrected_CDR.pdf",
-                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Climate Data Record (CDR)",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document (ATBD) for the CYGNSS Climate Data Record (CDR)",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L3/docs/148-0389-1_ATBD_Trackwise_Corrected_CDR.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
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
-                    "downloadURL": "https://cygnss.engin.umich.edu/",
-                    "description": "CYGNSS Mission Page at University of Michigan",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Mission Page at University of Michigan",
+                    "downloadURL": "https://cygnss.engin.umich.edu/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882064-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2036882064-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882064-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2036882064-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/OPeNDAP-in-the-Cloud",
-                    "description": "OPeNDAP Access for Data in the Cloud",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP Access for Data in the Cloud",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/OPeNDAP-in-the-Cloud",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
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
-                    "downloadURL": "https://soto.podaac.earthdatacloud.nasa.gov/?l=CYGNSS_L3_Wind_Speed_Daily%2CBlueMarble_ShadedRelief_Bathymetry%2CCoastlines_15m",
-                    "description": "SOTO (State Of The Ocean) Visualization of CYGNSS Wind Speed",
                     "@type": "dcat:Distribution",
+                    "description": "SOTO (State Of The Ocean) Visualization of CYGNSS Wind Speed",
+                    "downloadURL": "https://soto.podaac.earthdatacloud.nasa.gov/?l=CYGNSS_L3_Wind_Speed_Daily%2CBlueMarble_ShadedRelief_Bathymetry%2CCoastlines_15m",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
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
                 }
             ],
+            "graphic-preview-description": "SOTO (State Of The Ocean) Visualization of CYGNSS Wind Speed",
+            "graphic-preview-file": "https://soto.podaac.earthdatacloud.nasa.gov/?l=CYGNSS_L3_Wind_Speed_Daily,BlueMarble_ShadedRelief_Bathymetry,Coastlines_15m",
+            "identifier": "C2036882064-POCLOUD",
+            "issued": "2019-12-09",
+            "keyword": [
+                "oceans",
+                "ocean winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L3C10",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1038/s41598-018-27127-4"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 3 Climate Data Record",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2017-03-18T00:00:00Z/2021-02-28T23:59:59.999Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 3 Climate Data Record Version 1.0"
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
-                "dictionary",
-                "index",
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
-            "identifier": "NASA-557",
             "description": "Data Dictionary and Index Files",
-            "title": "PDS Data Dictionary (1r81)",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -682177,683 +682156,706 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-557",
+            "issued": "2018-06-25",
+            "keyword": [
+                "pds",
+                "dictionary",
+                "index",
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
+            "title": "PDS Data Dictionary (1r81)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1423-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-14T14:16:05.000 to 2016-02-14T21:15:56.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1423-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-EXT1-1423-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-ext1-1423-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the ROSETTA EXTENSION 1 phase 2016-01-01 to 2016-04-05. It is a Global Gravity measurement at the comet 67P and covers the time 2016-02-14T14:16:05.000 to 2016-02-14T21:15:56.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1423 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     ROSETTA EXTENSION 1 1423 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M07-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m07-v1.0_e5a5-bh43",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67PCHURYUMOV-M07-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67pchuryumov-m07-v1.0_e5a5-bh43",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Narrow Angle Camera during the PRELANDING phase of the Rosetta mission, covering the period from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP007 RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP007 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-RANGE-OPS-V1.0",
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-range-ops-v1.0_e5af-gunh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-RANGE-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-range-ops-v1.0_e5af-gunh",
-            "description": "NULL",
-            "title": "MER 1 MARS NAVIGATION CAMERA\n                                      RANGE RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS NAVIGATION CAMERA\n                                      RANGE RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1248-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-10T07:29:50.000 to 2015-12-10T16:04:08.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1248-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1248-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1248-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-10T07:29:50.000 to 2015-12-10T16:04:08.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1248 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1248 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2MTLNS_L2.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2MTLNS_L2.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-08-27",
-            "temporal": "2004-09-13T00:00:00Z/2018-01-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "air quality",
-                "earth science",
-                "clouds",
-                "atmospheric temperature",
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
-            "identifier": "C1331182613-LARC",
             "description": "TL2MTLNS_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Methanol Nadir Special Observation Version 7 data product. It consists of information for one molecular species for an entire Global Survey or Special Observation. TES was an instrument aboard NASA's Aura satellite and was launched from California on July 15, 2004. Data collection for TES is complete. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality, and other data (e.g., surface characteristics for nadir observations) were also provided. L2 modeled spectra were evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compared observed spectra to the modeled spectra and iteratively updated the atmospheric parameters. L2 standard product files included information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consisted of a maximum of 16 consecutive orbits.\r\rNadir observations, which point directly to the surface of the Earth, are different from limb observations, which are pointed at various off-nadir angles into the atmosphere. Nadir and limb observations were added to separate L2 files, and a single ancillary file was composed of data that are common to both nadir and limb files. A Nadir sequence within the TES Global Survey was a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations only used a single set of filter mix. \r\rA Global Survey consisted of observations along 16 consecutive orbits at the start of a two day cycle, over which 4,608 retrievals were performed. Each observation was the input for retrievals of species Volume Mixing Ratios (VMRs), temperature profiles, surface temperature, and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density, and other diagnostic quantities. Each TES Level 2 standard product reported information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object was bounded by the number of observations in a global survey and a predefined set of pressure levels, representing slices through the atmosphere. Each standard product could have had a variable number of observations depending upon the Global Survey configuration and whether averaging was employed. Also, missing or bad retrievals were not reported. Further, observations were occasionally scheduled on non-global survey days. In general they were measurements made for validation purposes or with highly focused science objectives. Those non-global survey measurements were referred to as \u201cspecial observations.\u201d\r\rA Limb sequence within the TES Global Survey was three high-resolution scans over the same limb locations. The Limb standard product consists of four files, where each file is composed of the Global Survey Limb observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Limb observations used a repeating sequence of filter wheel positions. Special Observations could only be scheduled during the 9 or 10 orbit gaps in the Global Surveys, and were conducted in any of three basic modes: stare, transect, step-and-stare. The mode used depended on the science requirement. Each limb observation Limb 1, Limb 2 and Limb 3, were processed independently. Thus, each limb standard product consisted of three sets where each set consisted of 1,152 observations. For TES, the swath object represented one of these sets.",
-            "title": "TES/Aura L2 Methanol Nadir Special Observation V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2MTLNS_L2.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2MTLNS_L2.007",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182613-LARC",
-                    "description": "Earthdata Search for TL2MTLNS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2MTLNS_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1331182613-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2MTLNS_L2.007",
-                    "description": "DOI data set landing page for TL2MTLNS_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2MTLNS_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2MTLNS_L2.007",
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
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2MTLNS.007/contents.html",
-                    "description": "OPeNDAP data access for TL2MTLNS_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2MTLNS_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2MTLNS.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2MTLNS.007/",
-                    "description": "ASDC Direct Data Download for TL2MTLNS_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2MTLNS_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2MTLNS.007/",
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
+            "identifier": "C1331182613-LARC",
+            "issued": "2015-08-27",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "clouds",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2MTLNS_L2.007",
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
+            "title": "TES/Aura L2 Methanol Nadir Special Observation V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/UZUYZGCBVA4F",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRAERSO4M3D. Version 1. TROPESS Chemical Reanalysis Aerosol SO4 Monthly 3-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/UZUYZGCBVA4F. https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO4M3D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2837624956-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Surface Aerosol SO4 Monthly 3-dimensional Product contains vertical concentrations of sulfate aerosols. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at monthly resolution, and a spatial resolution of 1.125 x 1.125 degrees at 27 pressure levels between 1000 and 60 hPa. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRAERSO4M3D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Aerosol SO4 Monthly 3-dimensional Product V1 (TRPSCRAERSO4M3D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO4M3D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUZUYZGCBVA4F",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FUZUYZGCBVA4F",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO4M3D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO4M3D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO4M3D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRAERSO4M3D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRAERSO4M3D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRAERSO4M3D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRAERSO4M3D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRAERSO4M3D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRAERSO4M3D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRAERSO4M3D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRAERSO4M3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRAERSO4M3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRAERSO4M3D_Sample.png",
+            "identifier": "C2837624956-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/UZUYZGCBVA4F",
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
+            "series-name": "TRPSCRAERSO4M3D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Aerosol SO4 Monthly 3-dimensional Product V1 (TRPSCRAERSO4M3D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/508",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Harding, D. 2016. BOREAS Scanning Lidar Imager of Canopies by Echo Recovery (SLICER): Level-3 Data. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/508",
-            "issued": "2016-09-21",
-            "temporal": "1996-07-18T00:00:00Z/1996-07-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "biosphere",
-                "vegetation",
-                "topography"
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
-            "identifier": "C2761666619-ORNL_CLOUD",
             "description": "Scanning Lidar Imager of Canopies by Echo Recovery (SLICER) data were acquired in support of BOReal Ecosystem-Atmosphere Study (BOREAS) at all of the Tower Flux (TF) sites in the Southern and Northern Study Areas (SSA and NSA, respectively) and along transects between the study areas.  Data were acquired on 5 days between 18 and 30 July 1996. Each coverage of a tower site is typically 40 km in length, with a minimum of 3 and a maximum of 10 lines across each tower oriented in a variety of azimuths. The SLICER data were acquired simultaneously with Advanced Solid-State Array Spectroradiometer (ASAS) hyperspectral, multiview angle images. The SLICER Level 3 products consist of binary files for each flight line with a data record for each laser shot composed of 13 parameters and a 600-byte waveform that is the raw record of the back scatter laser energy reflected from Earth's surface.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Scanning Lidar Imager of Canopies by Echo Recovery (SLICER): Level-3 Data",
-            "graphic-preview-file": "https://daac.ornl.gov/BOREAS/guides/BOREAS_SLICER_Fig1.GIF",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F508",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F508",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/BOREAS_SLICER/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/BOREAS_SLICER/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/BOREAS_SLICER.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/BOREAS_SLICER.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/508",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/508",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/BOREAS_SLICER.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/BOREAS_SLICER.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/BOREAS_SLICER_NASA-LAPF_Instrument_and_DataDescription.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/BOREAS_SLICER_NASA-LAPF_Instrument_and_DataDescription.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/BOREAS_SLICER_NASA-LAPG_TechnicalOverview.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/BOREAS_SLICER_NASA-LAPG_TechnicalOverview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Code_PRO.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Code_PRO.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/ELEVDIFF_Readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/ELEVDIFF_Readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Flight_Line_Plots.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Flight_Line_Plots.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Flight_Transect_Files.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Flight_Transect_Files.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/FLUXTOWR_SUMMARY.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/FLUXTOWR_SUMMARY.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Log_Notes.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Log_Notes.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/SLICER_Inventory.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/SLICER_Inventory.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Trajectory_Files_and_Plots.zip",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/BOREAS_SLICER/comp/Trajectory_Files_and_Plots.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/BOREAS_SLICER_Fig1.GIF",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/BOREAS_SLICER_Fig1.GIF",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/BOREAS/guides/BOREAS_SLICER_Fig1.GIF",
+            "identifier": "C2761666619-ORNL_CLOUD",
+            "issued": "2016-09-21",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "biosphere",
+                "vegetation",
+                "topography"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/508",
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
             "spatial": "-106.2 53.63 -98.03 55.93",
+            "temporal": "1996-07-18T00:00:00Z/1996-07-30T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Scanning Lidar Imager of Canopies by Echo Recovery (SLICER): Level-3 Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-MIDAS-3-AST2-LUTE-V1.0",
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
-                "21 lutetia",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles hitting the detector. This data set\nincludes all data from the LUTETIA FLY-BY mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-midas-3-ast2-lute-v1.0_e5f4-3ca2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "21 lutetia",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-MIDAS-3-AST2-LUTE-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-midas-3-ast2-lute-v1.0_e5f4-3ca2",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles hitting the detector. This data set\nincludes all data from the LUTETIA FLY-BY mission phase.",
-            "title": "ROSETTA-ORBITER LUTETIA MIDAS 3 AST2 LUTE V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER LUTETIA MIDAS 3 AST2 LUTE V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC3-67PCHURYUMOV-M18-V1.0",
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
+            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-06-30 to 2015-07-28.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc3-67pchuryumov-m18-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC3-67PCHURYUMOV-M18-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc3-67pchuryumov-m18-v1.0",
-            "description": "This data set contains raw EDR images acquired by the OSIRIS Narrow Angle\nCamera during the escort phase of the Rosetta mission at the comet 67P,\ncovering the period from 2015-06-30 to 2015-07-28.",
-            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 2 EDR MTP 018 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT OSINAC 2 EDR MTP 018 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-3-RDR-ELS-EXT3-V1.0",
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
+            "description": "This data set contains calibrated Mars Express ASPERA-3 Electron Spectrometer (ELS) data for the third mission extension (January 1, 2010 - Dec. 31, 2012).  These data are provided in units of Differential Number Flux (DNF): cnts/(cm**2-sr-sec-eV)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-3-rdr-els-ext3-v1.0_e5hc-m4r6",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-ASPERA3-3-RDR-ELS-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-aspera3-3-rdr-els-ext3-v1.0_e5hc-m4r6",
-            "description": "This data set contains calibrated Mars Express ASPERA-3 Electron Spectrometer (ELS) data for the third mission extension (January 1, 2010 - Dec. 31, 2012).  These data are provided in units of Differential Number Flux (DNF): cnts/(cm**2-sr-sec-eV)",
-            "title": "MARS EXPRESS ASPERA-3 CAL RDR ELECTRON SPECTROMTR EXT3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS EXPRESS ASPERA-3 CAL RDR ELECTRON SPECTROMTR EXT3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-EXT2-67PCHURYUMOV-M29-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-ext2-67pchuryumov-m29-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "vega",
@@ -682862,74 +682864,45 @@
                 "dark",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-EXT2-67PCHURYUMOV-M29-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-ext2-67pchuryumov-m29-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-03T23:25:00.000 to 2016-05-31T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 2 EXT2-MTP029 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 2 EXT2-MTP029 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA304",
             "citation": "Richard D. McPeters. 2012-08-01. SBUV2N11L3zm. Version 1. SBUV2/NOAA-11 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/OZONE/DATA304. https://disc.gsfc.nasa.gov/datacollection/SBUV2N11L3zm_1.html. Digital Science Data.",
-            "issued": "2013-06-13",
-            "temporal": "1989-01-01T00:00:00Z/2001-03-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-06-13",
-            "references": [
-                "https://doi.org/doi:10.5194/amt-5-2951-2012",
-                "https://doi.org/doi:10.5194/amt-6-2533-2013",
-                "https://doi.org/doi:10.1002/jgrd.50597"
-            ],
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RICHARD MCPETERS, PH. D",
                 "hasEmail": "mailto:richard.d.mcpeters@nasa.gov"
             },
+            "creator": "Richard D. McPeters",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1251051529-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Solar Backscattered Ultraviolet (SBUV) from NOAA-11 Level-3 monthly zonal mean (MZM) product (SBUV2N11L3zm) is derived from the Level-2 retrieved ozone profiles. Ozone retrievals are generated from the v8.6 SBUV algorithm. A Level-3 MZM file computes zonal means covering 5 degree latitude bands for each calendar month. For this product there are 147 months of data from January 1989 through March 2001. There are a total of 36 latitudinal bands, 18 in each hemisphere. Profile data are provided at 21 layers from 1013.25, 639.318, 403.382,254.517, 160.589, 101.325,63.9317, 40.3382, 25.4517, 16.0589, 10.1325, 6.39317,4.03382, 2.54517, 1.60589, 1.01325,0.639317, 0.403382, 0.254517, 0.160589 and 0.101325 hPa (measured at bottom of layer). NOTE: Some profiles have 20 layers and do not report the top most layer. Mixing ratios are reported at 15 layers from 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0, 40.0 and 50.0 hPa (measured at middle of layer). \n\nThe MZM product averages retrievals that meet the criteria for a good retrieval as determined by error flags in the Level 2 data. A good retrieval is defined as satisfying the following conditions:\n\n 1) Profile Error Flag = 0 or 1 (0 = good retrieval; 1 = solar zenith angle > 84 degrees).\n 2) Total Error Flags = 0, 1, 2 or 5 (0 = good retrieval; 1 = not used; 2 = solar zenith angle > 84 degrees; large discrepancy between profile total and best total ozone).\n\nNOTE - Total error flag = 5 is anomalously applied at high latitudes and high solar zenith angles where the B-Pair total ozone estimate is not as reliable as the ozone profile under these conditions. This error flag may be removed in future version of algorithm.\n\nThe zonal means computed for each month are screened according to the following statistical criteria:\n\n 1) Number of good retrievals for the month greater than or equal to 2/3 of the samples for a nominal month.\n 2) Mean latitude of good retrievals less than or equal to 1 degree from center of latitude band.\n 3) Mean time of good retrievals less than or equal to 4 days from center of month (i.e., day = 15).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SBUV2N11L3zm",
-            "creator": "Richard D. McPeters",
-            "title": "SBUV2/NOAA-11 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N11L3zm) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N11L3zm_1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA304",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FOZONE%2FDATA304",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -682939,328 +682912,331 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N11L3zm_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SBUV2N11L3zm_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N11L3zm.1/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N11L3zm.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N11L3zm.1/SBUV2-NOAA11_L3zm_v01-02-2013m0422t101514.h5.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N11L3zm.1/SBUV2-NOAA11_L3zm_v01-02-2013m0422t101514.h5.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N11L3zm.1/catalog.xml",
-                    "description": "Access the data using the THREDDS Catalog.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data using the THREDDS Catalog.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/Ozone/SBUV2N11L3zm.1/catalog.xml",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N11L3zm.1/doc/README.SBUVL3MZM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/Ozone/SBUV2N11L3zm.1/doc/README.SBUVL3MZM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SBUV2N11L3zm_1.png",
+            "identifier": "C1251051529-GES_DISC",
+            "issued": "2013-06-13",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/OZONE/DATA304",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-06-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/doi:10.5194/amt-5-2951-2012",
+                "https://doi.org/doi:10.5194/amt-6-2533-2013",
+                "https://doi.org/doi:10.1002/jgrd.50597"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SBUV2N11L3zm",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1989-01-01T00:00:00Z/2001-03-27T23:59:59.999Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SBUV2/NOAA-11 Ozone (O3) Profile and Total Column Ozone 1 Month Zonal Mean L3 Global 5.0 degree Latitude Zones V1 (SBUV2N11L3zm) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCMAG-2-AST1-RAW-V3.0",
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
-                "2867 steins"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains EDITED RAW DATA of the STEINS flyby Phase from\nSeptember 1 until September 10, 2008.\nThe closest approach (CA) took place on September 5, 2008 at 18:38",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpcmag-2-ast1-raw-v3.0_e5py-a7j9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "2867 steins"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A-RPCMAG-2-AST1-RAW-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-rpcmag-2-ast1-raw-v3.0_e5py-a7j9",
-            "description": "This dataset contains EDITED RAW DATA of the STEINS flyby Phase from\nSeptember 1 until September 10, 2008.\nThe closest approach (CA) took place on September 5, 2008 at 18:38",
-            "title": "ROSETTA-ORBITER STEINS RPCMAG 2 AST1 RAW V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER STEINS RPCMAG 2 AST1 RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-3-RADIOMETRIC-OPS-V1.0",
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
+            "description": "The Robotic Arm Camera (RAC) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This RAC Imaging Operations RDR data set contains radiometric data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-3-radiometric-ops-v1.0_e5q2-h8jd",
+            "issued": "2018-06-26",
+            "keyword": [
+                "phoenix",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-3-RADIOMETRIC-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-3-radiometric-ops-v1.0_e5q2-h8jd",
-            "description": "The Robotic Arm Camera (RAC) experiment on the Mars Phoenix Lander consists of one instrument component plus command electronics. This RAC Imaging Operations RDR data set contains radiometric data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 3 RADIOMETRIC OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 3 RADIOMETRIC OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-MAG-4-RDR-U1COORDS-1.92SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes data from the Low Field Magnetometer (LFM) in the during the Uranus encounter. The encounter data (1986-01-24T07:00:00 -> 1986-01-25T04:00:00) have been averaged from the 60ms instrument sample rate to a 1.92 second resampled rate and are provided in the Uranus Longitude (U1) coordinate system. Magnetometer data in the solar wind are given in Heliographic coordinates and are",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-mag-4-rdr-u1coords-1.92sec-v1.0_e5ri-qrd2",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "uranus",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-MAG-4-RDR-U1COORDS-1.92SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-mag-4-rdr-u1coords-1.92sec-v1.0_e5ri-qrd2",
-            "description": "This data set includes data from the Low Field Magnetometer (LFM) in the during the Uranus encounter. The encounter data (1986-01-24T07:00:00 -> 1986-01-25T04:00:00) have been averaged from the 60ms instrument sample rate to a 1.92 second resampled rate and are provided in the Uranus Longitude (U1) coordinate system. Magnetometer data in the solar wind are given in Heliographic coordinates and are",
-            "title": "VG2 URA MAG RESAMPLED RDR U1 COORDINATES 1.92SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 URA MAG RESAMPLED RDR U1 COORDINATES 1.92SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D41.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo QA Uncertainty Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D41.061. https://doi.org/10.5067/MODIS/MCD43D41.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "surface radiative properties",
-                "national geospatial data asset",
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
-            "identifier": "C2540271801-LPCLOUD",
-            "description": "The MCD43D41 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) QA Uncertainty dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. MCD43D41 provides BRDF inversion information for the MCD43D products. \r\n\r\nMCD43D41 layer contains the uncertainty range of each BRDF/Albedo pixel for the retrieval period.  \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo QA Uncertainty Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D41 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) QA Uncertainty dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. MCD43D41 provides BRDF inversion information for the MCD43D products. \r\n\r\nMCD43D41 layer contains the uncertainty range of each BRDF/Albedo pixel for the retrieval period.  \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D41.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D41.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D41.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D41.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540271801-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540271801-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D41.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D41.061",
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
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D41",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D41",
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
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D41.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D41.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540271801-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "surface radiative properties",
+                "national geospatial data asset",
+                "earth science",
+                "ngda",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D41.061",
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
+            "title": "MODIS/Terra+Aqua BRDF/Albedo QA Uncertainty Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/8VKQDQFFOTS3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Thomas A. Stanley, Dalia B. Kirschbaum, Garrett Benz, Robert A. Emberson, Pukar M. Amatya, William Medwedeff, and Marin K. Clark, NASA GSFC. Global_Landslide_Nowcast. Version 2.0.0. Global Landslide Nowcasts from LHASA L4 1 day 1 km x 1 km version 2.0.0 (Global_Landslide_Nowcast) at GES DISC. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/8VKQDQFFOTS3. https://disc.gsfc.nasa.gov/datacollection/Global_Landslide_Nowcast_2.0.0.html. Digital Science Data.",
-            "issued": "2023-03-24",
-            "temporal": "2015-04-03T00:00:00Z/2021-02-09T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-24",
-            "references": [
-                "https://doi.org/10.3389/feart.2021.640043"
-            ],
-            "keyword": [
-                "natural hazards",
-                "earth science",
-                "human dimensions"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashley Heath",
                 "hasEmail": "mailto:ashley.l.heath@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2654319036-GES_DISC",
-            "description": "The Global Landslide Nowcast addresses the need for real-time situational awareness of landslide hazard. The Landslide Hazard Assessment for Situational Awareness model (LHASA) combines satellite rainfall estimates from the Global Precipitation Measurement mission (GPM) with soil moisture estimates from the Soil Moisture Active Passive (SMAP) satellite and other factors to produce a map of locations where rainfall-triggered landslide activity is probable. Due to the latency of the rainfall data, the nowcast is a near-real time product with a minimum latency of 5 hours. Although the model could be run every half hour, this archive contains a daily record derived from a retrospective model run.",
-            "series-name": "Global_Landslide_Nowcast",
             "creator": "Thomas A. Stanley, Dalia B. Kirschbaum, Garrett Benz, Robert A. Emberson, Pukar M. Amatya, William Medwedeff, and Marin K. Clark, NASA GSFC",
-            "title": "Global Landslide Nowcast from LHASA L4 1 day 1 km x 1 km version 2.0.0 (Global_Landslide_Nowcast) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/Global_Landslide_Nowcast_2.0.0.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Global Landslide Nowcast addresses the need for real-time situational awareness of landslide hazard. The Landslide Hazard Assessment for Situational Awareness model (LHASA) combines satellite rainfall estimates from the Global Precipitation Measurement mission (GPM) with soil moisture estimates from the Soil Moisture Active Passive (SMAP) satellite and other factors to produce a map of locations where rainfall-triggered landslide activity is probable. Due to the latency of the rainfall data, the nowcast is a near-real time product with a minimum latency of 5 hours. Although the model could be run every half hour, this archive contains a daily record derived from a retrospective model run.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8VKQDQFFOTS3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F8VKQDQFFOTS3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -683270,31 +683246,31 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/Global_Landslide_Nowcast_2.0.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/Global_Landslide_Nowcast_2.0.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Landslide/Global_Landslide_Nowcast.2.0.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Landslide/Global_Landslide_Nowcast.2.0.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Community/LHASA/README.Global_Landslide_Nowcast2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Community/LHASA/README.Global_Landslide_Nowcast2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landslides.nasa.gov/",
-                    "description": "Introduction to NASA landslides research.",
                     "@type": "dcat:Distribution",
+                    "description": "Introduction to NASA landslides research.",
+                    "downloadURL": "https://landslides.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
@@ -683304,53 +683280,53 @@
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/Global_Landslide_Nowcast_2.0.0.png",
+            "identifier": "C2654319036-GES_DISC",
+            "issued": "2023-03-24",
+            "keyword": [
+                "natural hazards",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.5067/8VKQDQFFOTS3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.3389/feart.2021.640043"
+            ],
+            "series-name": "Global_Landslide_Nowcast",
             "spatial": "-180.0 -60.0 180.0 60.0",
+            "temporal": "2015-04-03T00:00:00Z/2021-02-09T23:59:59.999Z",
             "theme": [
                 "Landslide Project",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Landslide Nowcast from LHASA L4 1 day 1 km x 1 km version 2.0.0 (Global_Landslide_Nowcast) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1685783873-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2019-07-01. OCO2_L1aIn_Sample. Version 10r. OCO-2 Level 1A collated, parsed, science or calibration data, Retrospective Processing V10r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_10r.html. Digital Science Data.",
-            "issued": "2019-06-27",
-            "temporal": "2014-07-03T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-17",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry",
-                "spectral/engineering",
-                "infrared wavelengths"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ARIF ALBAYRAK",
                 "hasEmail": "mailto:arif.albayrak@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1685783873-GES_DISC",
-            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nVersion 8r is the current version of the data set. Version 7r has been superseded by Version 8r.\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Sample Mode of operation.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L1aIn_Sample",
             "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "OCO-2 Level 1A collated, parsed, science or calibration data, Retrospective Processing V10r (OCO2_L1aIn_Sample) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L1aIn_Sample_8r.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nVersion 8r is the current version of the data set. Version 7r has been superseded by Version 8r.\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers. The three spectrometers have different characteristics and are calibrated independently. Their raw data numbers (DN) are delivered correlated in time to the Level 1B process as Level 1A products. Each band has 1016 spectral elements, although some are masked out in the L2 retrieval.This product is the input to the Level 1B process. It is depacketized raw data formatted into a standard granularity with calibrated engineering data (for both science and calibration observations), in the Sample Mode of operation.This is the retrospective processing where the calibration data is estimated from the full timeseries of data (before, during, and after the measurements), and is expected to be of slightly higher quality.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -683359,118 +683335,151 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_10r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L1aIn_Sample_10r.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Sample.10r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L1aIn_Sample.10r/contents.html",
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
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Sample.10r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L1aIn_Sample.10r/",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OCO2_L1aIn_Sample_8r.jpeg",
+            "identifier": "C1685783873-GES_DISC",
+            "issued": "2019-06-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1685783873-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-06-17",
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
+            "temporal": "2014-07-03T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 1A collated, parsed, science or calibration data, Retrospective Processing V10r (OCO2_L1aIn_Sample) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/orbiter",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Beth Beck",
+                "hasEmail": "mailto:beth.beck@nasa.gov"
+            },
+            "description": "Polygons: 5054 Vertices: 3441",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/orbiter/Orbiter.3ds.zip",
+                    "mediaType": "image/x-3ds"
+                }
             ],
+            "identifier": "NASA-403",
+            "issued": "2018-06-25",
             "keyword": [
                 "space shuttle",
                 "spacecraft",
@@ -683479,622 +683488,627 @@
                 "space shuttle orbiter",
                 "3d model"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Beth Beck",
-                "hasEmail": "mailto:beth.beck@nasa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-403",
-            "description": "Polygons: 5054 Vertices: 3441",
-            "title": "NASA 3D Models: Shuttle Model 2",
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/orbiter",
+            "modified": "2020-01-29",
             "programCode": [
                 "026:045",
                 "026:046"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://nasa3d.arc.nasa.gov/shared_assets/models/orbiter/Orbiter.3ds.zip",
-                    "mediaType": "image/x-3ds"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Shuttle Model 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0276-2%2F3-MARTIR15M-TMPL1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The presented dataset represents 4 half-nights of observing at San Pedro Martir, Baja, Mexico. The target, Comet 9P/Tempel 1, was impacted by the Deep Impact impactor on the third night of observing, 4 July UT. The observations are optical broadband imaging (BVRI filters), on a 1.5 m telescope, with a time resolution around 10 sec near impact and 20 sec at most other times.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0276-2-3-martir15m-tmpl1-v1.0_e62c-3tu7",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "9p/tempel 1 (1867 g1)",
                 "calibration",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI%2FEAR-C-I0276-2%2F3-MARTIR15M-TMPL1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-ear-c-i0276-2-3-martir15m-tmpl1-v1.0_e62c-3tu7",
-            "description": "The presented dataset represents 4 half-nights of observing at San Pedro Martir, Baja, Mexico. The target, Comet 9P/Tempel 1, was impacted by the Deep Impact impactor on the third night of observing, 4 July UT. The observations are optical broadband imaging (BVRI filters), on a 1.5 m telescope, with a time resolution around 10 sec near impact and 20 sec at most other times.",
-            "title": "SAN PEDRO MARTIR OPTICAL IMAGING OF 9P/TEMPEL 1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SAN PEDRO MARTIR OPTICAL IMAGING OF 9P/TEMPEL 1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/3RQ5YS674DGQ",
             "citation": "Global Modeling and Assimilation Office (GMAO). 2015-06-30. M2T1NXCHM. Version 5.12.4. MERRA-2 tavg1_2d_chm_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Carbon Monoxide and Ozone Diagnostics V5.12.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/3RQ5YS674DGQ. https://disc.gsfc.nasa.gov/datacollection/M2T1NXCHM_5.12.4.html. Digital Science Data.",
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
-                "air quality",
-                "atmosphere",
-                "atmospheric chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DANA OSTRENGA",
                 "hasEmail": "mailto:dana.ostrenga@nasa.gov"
             },
+            "creator": "Global Modeling and Assimilation Office (GMAO)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1276812831-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "M2T1NXCHM (or  tavg1_2d_chm_Nx) is an hourly time-averaged 2-dimensional data collection in Modern-Era Retrospective analysis for Research and Applications version 2 (MERRA-2).  This collection consists of assimilated carbon monoxide and ozone diagnostics, such as properties of carbon monoxide (column burden, emission, chemical production, and surface concentration), and total column ozone.  The data field is time-stamped with the central time of an hour starting from 00:30 UTC, e.g.: 00:30, 01:30, \u2026 , 23:30 UTC.\n\nMERRA-2 is the latest version of global atmospheric reanalysis for the satellite era produced by NASA Global Modeling and Assimilation Office (GMAO) using the Goddard Earth Observing System Model (GEOS) version 5.12.4.  The dataset covers the period of 1980-present with the latency of ~3 weeks after the end of a month. \n\nData Reprocessing:  Please check \u201cRecords of MERRA-2 Data Reprocessing and Service Changes\u201d linked from the \u201cDocumentation\u201d tab on this page.  Note that a reprocessed data filename is different from the original file.\n\nMERRA-2 Mailing List: Sign up to receive information on reprocessing of data, changing of tools and services, as well as data announcements from GMAO. Contact the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov) to be added to the list.\n\nQuestions: If you have a question, please read \"MERRA-2 File Specification Document\",  \u201cMERRA-2 Data Access \u2013 Quick Start Guide\u201d, and FAQs linked from the \u201dDocumentation\u201d tab on this page.  If that does not answer your question, you may email the question on data access to the GES DISC Help Desk (gsfc-dl-help-disc@mail.nasa.gov), or the question on science to the MERRA-2 science team (merra-questions@lists.nasa.gov).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "M2T1NXCHM",
-            "creator": "Global Modeling and Assimilation Office (GMAO)",
-            "graphic-preview-description": "M2T1NXCHM variable",
-            "title": "MERRA-2 tavg1_2d_chm_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Carbon Monoxide and Ozone Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXCHM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXCHM_5.12.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3RQ5YS674DGQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F3RQ5YS674DGQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXCHM_5.12.4.png",
-                    "description": "M2T1NXCHM variable",
                     "@type": "dcat:Distribution",
+                    "description": "M2T1NXCHM variable",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXCHM_5.12.4.png",
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
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T1NXCHM_5.12.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/M2T1NXCHM_5.12.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXCHM.5.12.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXCHM.5.12.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T1NXCHM",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=M2T1NXCHM",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXCHM.info",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/dods/M2T1NXCHM.info",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXCHM.5.12.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXCHM.5.12.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T1NXCHM.5.12.4/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/thredds/catalog/MERRA2_aggregation/M2T1NXCHM.5.12.4/catalog.html",
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
-                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXCHM.5.12.4/doc/MERRA2.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://goldsmr4.gesdisc.eosdis.nasa.gov/data/MERRA2/M2T1NXCHM.5.12.4/doc/MERRA2.README.pdf",
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
+            "graphic-preview-description": "M2T1NXCHM variable",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/M2T1NXCHM_5.12.4.png",
+            "identifier": "C1276812831-GES_DISC",
+            "issued": "2007-06-14",
+            "keyword": [
+                "air quality",
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/3RQ5YS674DGQ",
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
+            "series-name": "M2T1NXCHM",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1980-01-01T00:00:00Z/2024-03-27T00:00:00Z",
             "theme": [
                 "MERRA-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MERRA-2 tavg1_2d_chm_Nx: 2d,1-Hourly,Time-Averaged,Single-Level,Assimilation,Carbon Monoxide and Ozone Diagnostics 0.625 x 0.5 degree V5.12.4 (M2T1NXCHM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1715",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Huey, L.G., J.B. Nowak, D. Tanner, and S. Kim. 2019. ATom: L2 In Situ Peroxyacetyl Nitrate (PAN) Measurements from Georgia Tech CIMS. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1715",
-            "issued": "2019-09-30",
-            "temporal": "2017-01-26T17:11:51Z/2017-10-28T00:53:16Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "atmospheric chemistry",
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
-            "identifier": "C2676891839-ORNL_CLOUD",
             "description": "This dataset provides measurements of two important components of photochemical smog - peroxyacetyl nitrate (PAN) and peroxyl propionyl nitrate (PPN)- measured by the Georgia Tech Chemical Ionization Mass Spectrometer (GT-CIMS) during airborne campaigns conducted by NASA's Atmospheric Tomography (ATom) mission. The GT-CIMS measures reactive nitrogen species in the lower atmosphere. ATom deploys an extensive gas and aerosol payload on the NASA DC-8 aircraft for systematic, global-scale sampling of the atmosphere, profiling continuously from 0.2 to 12 km altitude. Flights occurred in each of 4 seasons from 2016 to 2018. Flights originate from the Armstrong Flight Research Center in Palmdale, California, fly north to the western Arctic, south to the South Pacific, east to the Atlantic, north to Greenland, and return to California across central North America. ATom establishes a single, contiguous, global-scale dataset. This comprehensive dataset will be used to improve the representation of chemically reactive gases and short-lived climate forcers in global models of atmospheric chemistry and climate.",
-            "graphic-preview-description": "The Georgia Tech Chemical Ionization Mass Spectrometer (CIMS).",
-            "title": "ATom: L2 In Situ Peroxyacetyl Nitrate (PAN) Measurements from Georgia Tech CIMS",
-            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_GT_CIMS_Instrument_Data_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1715",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1715",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/atom/ATom_GT_CIMS_Instrument_Data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/atom/ATom_GT_CIMS_Instrument_Data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_GT_CIMS_Instrument_Data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_GT_CIMS_Instrument_Data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1715",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1715",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_GT_CIMS_Instrument_Data/comp/ATom_GT_CIMS_Instrument_Data.pdf",
-                    "description": "ATom: L2 Measurements from the Chemical Ionization Mass Spectrometer (GT-CIMS): ATom_GT_CIMS_Instrument_Data.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ATom: L2 Measurements from the Chemical Ionization Mass Spectrometer (GT-CIMS): ATom_GT_CIMS_Instrument_Data.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/atom/ATom_GT_CIMS_Instrument_Data/comp/ATom_GT_CIMS_Instrument_Data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_GT_CIMS_Instrument_Data_Fig1.jpg",
-                    "description": "The Georgia Tech Chemical Ionization Mass Spectrometer (CIMS).",
                     "@type": "dcat:Distribution",
+                    "description": "The Georgia Tech Chemical Ionization Mass Spectrometer (CIMS).",
+                    "downloadURL": "https://daac.ornl.gov/ATOM/guides/ATom_GT_CIMS_Instrument_Data_Fig1.jpg",
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
+            "graphic-preview-description": "The Georgia Tech Chemical Ionization Mass Spectrometer (CIMS).",
+            "graphic-preview-file": "https://daac.ornl.gov/ATOM/guides/ATom_GT_CIMS_Instrument_Data_Fig1.jpg",
+            "identifier": "C2676891839-ORNL_CLOUD",
+            "issued": "2019-09-30",
+            "keyword": [
+                "earth science",
+                "atmospheric chemistry",
+                "air quality",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1715",
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
+            "temporal": "2017-01-26T17:11:51Z/2017-10-28T00:53:16Z",
             "theme": [
                 "ATom",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ATom: L2 In Situ Peroxyacetyl Nitrate (PAN) Measurements from Georgia Tech CIMS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/974",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Yetman, G., S. Gaffin, D. Balk, F.G. Hall, G.J. Collatz, B.W. Meeson, S.O. Los, E.Brown De Colstoun, and D.R. Landis. 2010. ISLSCP II Global Gridded Gross Domestic Product (GDP), 1990. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/974",
-            "issued": "2023-10-15",
-            "temporal": "1990-01-01T00:00:00Z/1990-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-17",
-            "keyword": [
-                "land surface",
-                "national geospatial data asset",
-                "population",
-                "human dimensions",
-                "land use/land cover",
-                "ngda",
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
-            "identifier": "C2784894332-ORNL_CLOUD",
             "description": "The data sets in this directory were provided by Mr. Gregory Yetman and Drs. Stuart Gaffin and Deborah Balk from the Center for International Earth Science Information Network (CIESIN) at Columbia University. There are three data files at three spatial resolutions of 0.25, 0.5 and 1.0 degree in both latitude and longitude and for the reference year of 1990.Estimates of Gross Domestic Product (GDP) are commonly given for nations as a single aggregated number. This data set generates estimates of GDP density distributed subnationally to facilitate the integration of GDP with other data at a sub-national level and to promote interdisciplinary studies that include socioeconomic aspects.  This is one of two coarse resolution Socioeconomic data sets included in the International Satellite Land Surface Climatology Project (ISLSCP) Initiative II data collection, the other being the Gridded Population of the World (GPW), also produced by CIESIN.",
-            "graphic-preview-description": "Browse Image",
-            "title": "ISLSCP II Global Gridded Gross Domestic Product (GDP), 1990",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/974_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F974",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F974",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/socioeconomic/gdp_xdeg/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/islscp_ii/socioeconomic/gdp_xdeg/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/gdp_xdeg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ISLSCP_II/guides/gdp_xdeg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/974",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/974",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/socioeconomic/gdp_xdeg/comp/0_gdp_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/socioeconomic/gdp_xdeg/comp/0_gdp_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/socioeconomic/gdp_xdeg/comp/1_gdp_doc.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/islscp_ii/socioeconomic/gdp_xdeg/comp/1_gdp_doc.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/974_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/974_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=974",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=974",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/974/catalog.html",
-                    "description": "The THREDDS location for this Collection.",
                     "@type": "dcat:Distribution",
+                    "description": "The THREDDS location for this Collection.",
+                    "downloadURL": "https://thredds.daac.ornl.gov/thredds/catalog/ornldaac/974/catalog.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/974_1_fit.png",
+            "identifier": "C2784894332-ORNL_CLOUD",
+            "issued": "2023-10-15",
+            "keyword": [
+                "land surface",
+                "national geospatial data asset",
+                "population",
+                "human dimensions",
+                "land use/land cover",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/974",
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
+            "temporal": "1990-01-01T00:00:00Z/1990-12-31T23:59:59Z",
             "theme": [
                 "ISLSCP II",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISLSCP II Global Gridded Gross Domestic Product (GDP), 1990"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC4-67PCHURYUMOV-M23-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc4-67pchuryumov-m23-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "zeta cas",
                 "vega",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-3-ESC4-67PCHURYUMOV-M23-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-3-esc4-67pchuryumov-m23-v1.0",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera during the COMET ESCORT 4 phase of the Rosetta mission at the comet 67P, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000.",
-            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSINAC 3 RDR MTP023 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER COMET ESCORT 4 OSINAC 3 RDR MTP023 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M05-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m05-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "bias",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "dark"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-2-PRL-67PCHURYUMOV-M05-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-2-prl-67pchuryumov-m05-v2.0",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera during the PRELANDING phase of the Rosetta mission at the comet 67P, covering the period from 2014-07-02T08:35:00.000 to 2014-08-01T09:59:59.000. This version V2.0 supersedes previous deliveries of the same dataset.",
-            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 2 EDR MTP005 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER PRELANDING OSIWAC 2 EDR MTP005 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2069",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Wang, C., T.M. Pavelsky, E.D. Kyzivat, F. Garcia-Tigreros, F. Yao, X. Yang, S. Zhang, C. Song, T. Langhorst, W. Dolan, M. Kurek, M.E. Harlan, L.C. Smith, D. Butman, R.G.M. Spencer, C.J. Gleason, and D.L. Peters. 2022. ABoVE: Wetland Vegetation Classification for Peace-Athabasca Delta, Canada, 2019. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2069",
-            "issued": "2022-06-24",
-            "temporal": "2019-07-15T00:00:00Z/2019-09-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "terrestrial hydrosphere",
-                "surface water",
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
-            "identifier": "C2308233855-ORNL_CLOUD",
             "description": "This dataset contains land cover classification focused on water and wetland vegetation communities over the Peace-Athabasca Delta, Canada. Four classification maps with 5-m resolution were derived various combinations of Airborne Visible/Infrared Imaging Spectrometer-Next Generation (AVIRIS-NG) and Uninhabited Aerial Vehicle Synthetic Aperture Radar (UAVSAR) acquired in July and September 2019, and a historical LiDAR archive data. The maps include 10 land cover classes, including open water, emergent aquatic vegetation types, terrestrial vegetation, and forest. Based on field data, the best performing model, which combined all three data sources, achieved an overall accuracy of 93.5%. The land cover maps are provided in GeoTIFF format along with polygons of AVIRIS-NG, UAVSAR, and LiDAR footprints in shapefile and KML formats.",
-            "graphic-preview-description": "The wetland vegetation community classification for the Peace-Athabasca Delta, Alberta, Canada created from AVIRIS-NG derived features.",
-            "title": "ABoVE: Wetland Vegetation Classification for Peace-Athabasca Delta, Canada, 2019",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Wetland_VegClassification_PAD_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2069",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2069",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Wetland_VegClassification_PAD/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Wetland_VegClassification_PAD/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wetland_VegClassification_PAD.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wetland_VegClassification_PAD.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2069",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2069",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Wetland_VegClassification_PAD/comp/Wetland_VegClassification_PAD.pdf",
-                    "description": "ABoVE: Wetland Vegetation Classification for Peace-Athabasca Delta, Canada, 2019: Wetland_VegClassification_PAD.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Wetland Vegetation Classification for Peace-Athabasca Delta, Canada, 2019: Wetland_VegClassification_PAD.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Wetland_VegClassification_PAD/comp/Wetland_VegClassification_PAD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wetland_VegClassification_PAD_Fig1.jpg",
-                    "description": "The wetland vegetation community classification for the Peace-Athabasca Delta, Alberta, Canada created from AVIRIS-NG derived features.",
                     "@type": "dcat:Distribution",
+                    "description": "The wetland vegetation community classification for the Peace-Athabasca Delta, Alberta, Canada created from AVIRIS-NG derived features.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Wetland_VegClassification_PAD_Fig1.jpg",
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
+            "graphic-preview-description": "The wetland vegetation community classification for the Peace-Athabasca Delta, Alberta, Canada created from AVIRIS-NG derived features.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Wetland_VegClassification_PAD_Fig1.jpg",
+            "identifier": "C2308233855-ORNL_CLOUD",
+            "issued": "2022-06-24",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "terrestrial hydrosphere",
+                "surface water",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2069",
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
             "spatial": "-112.11 58.21 -110.83 59.14",
+            "temporal": "2019-07-15T00:00:00Z/2019-09-15T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Wetland Vegetation Classification for Peace-Athabasca Delta, Canada, 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/e69m-jnk9",
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
+            "identifier": "nasa_genelab_GLDS-41_e69m-jnk9",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "gravity",
                 "p-gse27338-4",
@@ -684112,188 +684126,175 @@
                 "p-gse27338-7",
                 "image_aquisition"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/e69m-jnk9",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-41_e69m-jnk9",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC1-MTP013-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT  1 MTP013 phase, which occurred from 2015-02-11 to 2015-03-11 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc1-mtp013-v2.0_e69u-k5g8",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-3-ESC1-MTP013-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-3-esc1-mtp013-v2.0_e69u-k5g8",
-            "description": "This release contains the calibrated data of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data from the ESCORT  1 MTP013 phase, which occurred from 2015-02-11 to 2015-03-11 when at the vicinity of comet 67P. This data set V2.0 supersedes V1.0. It includes major updates on the data and documentation.",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 1 MTP013 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P VIRTIS 3 ESCORT 1 MTP013 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0028-V1.0",
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
-                "sun"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Solar Conjunction measurement covering the time 2006-04-06T06:56:54.500 to 2006-04-06T09:14:58.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0028-v1.0_e6be-ir76",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "sun"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0028-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0028-v1.0_e6be-ir76",
-            "description": "This is a Solar Conjunction measurement covering the time 2006-04-06T06:56:54.500 to 2006-04-06T09:14:58.500.",
-            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0028 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER SUN RSI 1/2/3 CRUISE 2 0028 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC4-67P-M23-GEO-V1.0",
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
+            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc4-67p-m23-geo-v1.0_e6cg-twx8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-5-ESC4-67P-M23-GEO-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-5-esc4-67p-m23-geo-v1.0_e6cg-twx8",
-            "description": "This CODMAC level 5 data set contains derived data products that include pixel-precise georeferencing information, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-11-17T23:25:00.000 to 2015-12-15T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC4-MTP023 DDR-GEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 5 ESC4-MTP023 DDR-GEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1213925022-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
-            "issued": "2012-02-20",
-            "temporal": "1993-06-08T00:00:00Z/2004-12-04T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-02-20",
-            "keyword": [
-                "land surface",
-                "land use/land cover",
-                "earth science"
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
-            "identifier": "C1213925022-ASF",
             "description": "AIRSAR topographic SAR digital elevation model CTIF product",
-            "title": "AIRSAR_TOPSAR_DEM_C",
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
+            "identifier": "C1213925022-ASF",
+            "issued": "2012-02-20",
+            "keyword": [
+                "land surface",
+                "land use/land cover",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1213925022-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-02-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ASF"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-26.198199 -143.26613 -23.096323 -62.958179 -18.867366 -62.30596 69.178089 -49.704356 69.25925 -49.871916 64.601354 -147.320616 64.503195 -147.324715 -27.021632 -172.880269 -27.388834 -172.532316 -26.198199 -143.26613</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1993-06-08T00:00:00Z/2004-12-04T23:59:59Z",
             "theme": [
                 "St. Charles, MO",
                 "Web County, TX",
@@ -684594,136 +684595,137 @@
                 "Uthai Thani, Thailand",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRSAR_TOPSAR_DEM_C"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENOC1-V1.0",
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
-                "enceladus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Enceladus Occultation Experiment (ENOC1) Raw Data Archive is a time-ordered collection of radio science raw data acquired on September 15, 2006, during the Tour subphase of the Cassini mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-enoc1-v1.0_e6d3-593k",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "enceladus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-ENOC1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-enoc1-v1.0_e6d3-593k",
-            "description": "The Cassini Radio Science Enceladus Occultation Experiment (ENOC1) Raw Data Archive is a time-ordered collection of radio science raw data acquired on September 15, 2006, during the Tour subphase of the Cassini mission.",
-            "title": "CASSINI RSS RAW DATA SET - ENOC1 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CASSINI RSS RAW DATA SET - ENOC1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MTIF60G86H86",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Seasat and GEOSAT Altimetry for the Antarctic and Greenland Ice Sheets, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MTIF60G86H86.",
-            "issued": "1978-06-01",
-            "temporal": "1978-06-01T00:00:00Z/1986-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1986-09-30",
-            "keyword": [
-                "glaciers/ice sheets",
-                "cryosphere",
-                "earth science",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "H. Zwally",
                 "hasEmail": "mailto:Jay.Zwally@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386206961-NSIDCV0",
             "description": "<p><font color=\"#FF0000\">Note: This data set is now on HTTPS so references to CD-ROM are historic and no longer applicable.</font></p>\n\nThe Ice Altimetry System (IAS) data seet contains surface elevations of the Antarctic and Greenland ice sheets derived from Seasat and GEOSAT radar altimetry data. The Seasat data were collected for a continuous 90 days in 1978, at latitudes between 72 degrees South and 72 degrees North. GEOSAT was launched in 1985 and placed in a nearly identical orbit to Seasat, also at latitudes of between 72 degrees South and 72 degrees North. The orbit was designed to provide high-density measurements over the Earth's surface, at a maximum grid spacing of 2.7 kilometers at the equator and much denser spacing over polar ice sheets. Data were acquired between April 1985 and September 1986.\n\nInitially acquired by the Johns Hopkins APL (Applied Physics Lab) satellite tracking facility, the raw altimetry satellite data from Seasat and GEOSAT were passed on to NASA, via the US Navy. NASA developed slope correction routines for the higher slopes over the ice sheets, relative to ocean surfaces. The data are height profile Level 3 data and gridded height Level 4 data provided by the Oceans and Ice branch of the Laboratory for Hydrospheric Physics of Goddard Space Flight Center. Elevations from the full data rate (i.e., one measurement every 662.5 m) are provided in georeferenced databases. These elevations are relative to the WGS-84 ellipsoid. Gridded elevations at 10-kilometer and 20-kilometer spacing are provided in the gridded data sets created from the GEOSAT and Seasat data, respectively. Software to extract and browse subsets of these data is included. The IAS software also allows the user to view contours created from the gridded data and groundtracks of the full-rate data.",
-            "title": "Seasat and GEOSAT Altimetry for the Antarctic and Greenland Ice Sheets, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMTIF60G86H86",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMTIF60G86H86",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0053_icesheets_surf_elev_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0053_icesheets_surf_elev_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0053_icesheets_surf_elev_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0053_icesheets_surf_elev_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MTIF60G86H86",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MTIF60G86H86",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MTIF60G86H86",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MTIF60G86H86",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206961-NSIDCV0",
+            "issued": "1978-06-01",
+            "keyword": [
+                "glaciers/ice sheets",
+                "cryosphere",
+                "earth science",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MTIF60G86H86",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1986-09-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-60.0 60.0 -20.0 72.0",
+            "temporal": "1978-06-01T00:00:00Z/1986-09-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Seasat and GEOSAT Altimetry for the Antarctic and Greenland Ice Sheets, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNOLC-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes a collection of published lightcurves of trans-Neptunian objects published through December 2002. The collection includes lightcurves of 18 TNOs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tnolc-v1.1_e6d7-fp6m",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid 19255",
                 "asteroid 19308",
@@ -684744,38 +684746,38 @@
                 "asteroid",
                 "asteroid 15875"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNOLC-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tnolc-v1.1_e6d7-fp6m",
-            "description": "This data set includes a collection of published lightcurves of trans-Neptunian objects published through December 2002. The collection includes lightcurves of 18 TNOs.",
-            "title": "TRANS-NEPTUNIAN OBJECT LIGHTCURVES V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "TRANS-NEPTUNIAN OBJECT LIGHTCURVES V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0387-3-SUBMMLC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Submillimeter lightcurves of large asteroids Ceres, Davida, Io, Juno, Pallas, Vesta, and Victoria, observed at the Heinrich-Hertz Submillimeter Telescope from January 2003 through May 2004.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0387-3-submmlc-v1.0_e6dr-3qjr",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "asteroid",
                 "85 io",
@@ -684787,57 +684789,36 @@
                 "12 victoria",
                 "support archives"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0387-3-SUBMMLC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0387-3-submmlc-v1.0_e6dr-3qjr",
-            "description": "Submillimeter lightcurves of large asteroids Ceres, Davida, Io, Juno, Pallas, Vesta, and Victoria, observed at the Heinrich-Hertz Submillimeter Telescope from January 2003 through May 2004.",
-            "title": "SUBMILLIMETER LIGHTCURVES OF ASTEROIDS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SUBMILLIMETER LIGHTCURVES OF ASTEROIDS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://eros.usgs.gov/imagegallery/journey-lewis-and-clark",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "imagery",
-                "landsat",
-                "earth science",
-                "images",
-                "usgs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Charles Ichoku",
                 "hasEmail": "mailto:james.r.irons@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-915",
             "description": "The Earth Resources Observation and Science (EROS) Center manages the this gallery of Landsat-derived images of one of the most remarkable and productive scientific explorations in American history. The Corps of Discovery expedition crossed the territory of the newly acquired but uncharted Louisiana Purchase.",
-            "title": "Earth Resources Observation and Science (EROS) Center's Journey of Lewis and Clark Gallery",
-            "programCode": [
-                "026:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -684845,955 +684826,976 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-915",
+            "issued": "2014-04-29",
+            "keyword": [
+                "imagery",
+                "landsat",
+                "earth science",
+                "images",
+                "usgs"
+            ],
+            "landingPage": "http://eros.usgs.gov/imagegallery/journey-lewis-and-clark",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:035"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "title": "Earth Resources Observation and Science (EROS) Center's Journey of Lewis and Clark Gallery"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-2-PLUTO-V1.0",
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
+            "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-2-pluto-v1.0_e6g5-xq4v",
+            "issued": "2018-09-05",
+            "keyword": [
+                "dust",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-SDC-2-PLUTO-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-sdc-2-pluto-v1.0_e6g5-xq4v",
-            "description": "This data set contains Raw data taken by the New Horizons                Student Dust Counter                                                   instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      RAW V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      SDC PLUTO ENCOUNTER                                                     \n      RAW V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NPP/CERES/ES4-FM5_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-04-30. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NPP/CERES/ES4-FM5_L3.002.",
-            "issued": "2020-03-05",
-            "temporal": "2012-02-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-03-05",
-            "keyword": [
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
-            "identifier": "C2246001726-LARC_ASDC",
             "description": "The ERBE-like Monthly Geographical Averages (ES-4) product contains a month of space and time averaged Clouds and the Earth's Radiant Energy System (CERES) data for a single satellite using measurements from the primary crosstrack instrument. For each observed 2.5-degree spatial region, the daily average, the hourly average over the month, and the overall monthly average of shortwave and longwave fluxes at the Top-of-the-Atmosphere (TOA) from the CERES ES-9 product are spatially nested up from 2.5-degree regions to 5- and 10-degree regions, to 2.5-, 5-, and 10-degree zonal averages, and to global monthly averages. For each nested area, the albedo and net flux are given. For each region, the daily average flux is estimated from an algorithm that uses the available hourly data, scene identification data, and diurnal models. This algorithm is \"like\" the algorithm used for the Earth Radiation Budget Experiment (ERBE).\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. The CERES instrument (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The last CERES instrument (FM6) was launched on board the Joint Polar Satellite System 1 (JPSS-1) satellite on November 18, 2017.",
-            "title": "CERES ERBE-like Time-Interpolated TOA Fluxes (ES4) NPP FM-5 Edition2",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNPP%2FCERES%2FES4-FM5_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNPP%2FCERES%2FES4-FM5_L3.002",
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
-                    "downloadURL": "https://doi.org/10.5067/NPP/CERES/ES4-FM5_L3.002",
-                    "description": "DOI data set landing page for CER_ES4_NPP-FM5_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_ES4_NPP-FM5_Edition2",
+                    "downloadURL": "https://doi.org/10.5067/NPP/CERES/ES4-FM5_L3.002",
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/ES4_CG_R1V1.pdf",
-                    "description": "ES-4 Collection Guide Release 1 Version 1",
                     "@type": "dcat:Distribution",
+                    "description": "ES-4 Collection Guide Release 1 Version 1",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/collect_guide/pdf/ES4_CG_R1V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ES4_R7V1.pdf",
-                    "description": "CERES Data Products Catalog R7V1 November 2013 ERBE-like Monthly Regional Averages (ES-4)",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog R7V1 November 2013 ERBE-like Monthly Regional Averages (ES-4)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/DPC_ES4_R7V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_es4.pdf",
-                    "description": "CERES ERBE-like Monthly Geographic Averages (ES-4) Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES ERBE-like Monthly Geographic Averages (ES-4) Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_es4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES4_NPP_Edition2.pdf",
-                    "description": "Quality Summary: CERES ES4 NPP Edition 2",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES ES4 NPP Edition 2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_ES4_NPP_Edition2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_es9_SampleRead_R6V1-895.txt",
-                    "description": "Readme to read several ES-9 data sets",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to read several ES-9 data sets",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/readme_cer_es9_SampleRead_R6V1-895.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/erbelike_SampleRead_ES9_R6V1-895.zip",
-                    "description": "Read Software Package - CERES ES9 Aqua-FM3 - Direct File Download (.zip)",
                     "@type": "dcat:Distribution",
+                    "description": "Read Software Package - CERES ES9 Aqua-FM3 - Direct File Download (.zip)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/read_software/erbelike_SampleRead_ES9_R6V1-895.zip",
+                    "mediaType": "application/zip",
                     "title": "View this dataset's science data product software documentation"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/",
-                    "description": "CERES Data Products Browse, Subset, and Order",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Browse, Subset, and Order",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
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
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#npp",
-                    "description": "CERES Overview of NPP",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of NPP",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#npp",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001726-LARC_ASDC",
-                    "description": "Earthdata Search for CER_ES4_NPP-FM5_Edition2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_ES4_NPP-FM5_Edition2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001726-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES4/NPP-FM5_Edition2/",
-                    "description": "ASDC Direct Data Download for CER_ES4_NPP-FM5_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_ES4_NPP-FM5_Edition2",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/ES4/NPP-FM5_Edition2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES4/NPP-FM5_Edition2/contents.html",
-                    "description": "OPeNDAP data access for CER_ES4_NPP-FM5_Edition2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_ES4_NPP-FM5_Edition2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/ES4/NPP-FM5_Edition2/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2246001726-LARC_ASDC",
+            "issued": "2020-03-05",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/NPP/CERES/ES4-FM5_L3.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-03-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2012-02-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES ERBE-like Time-Interpolated TOA Fluxes (ES4) NPP FM-5 Edition2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/KDNRYQC7V2CD",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge CMG 1A Dynamic Gravity Meter Time-Tagged L1B Vertical Accelerations V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/KDNRYQC7V2CD.",
-            "issued": "2012-11-13",
-            "temporal": "2012-11-13T00:00:00Z/2013-01-14T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-01-14",
-            "keyword": [
-                "solid earth",
-                "gravity/gravitational field",
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
-            "identifier": "C1000001541-NSIDC_ECS",
             "description": "This data set contains vertical acceleration values for Antarctica using the CMG 1A dynamic gravity meter. The data were collected by scientists working on the Investigating the Cryospheric Evolution of the Central Antarctic Plate (ICECAP) project, which is funded by the National Science Foundation (NSF) and the Natural Environment Research Council (NERC) with additional support from NASA Operation IceBridge.",
-            "title": "IceBridge CMG 1A Dynamic Gravity Meter Time-Tagged L1B Vertical Accelerations V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKDNRYQC7V2CD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKDNRYQC7V2CD",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGCMG1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGCMG1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001541-NSIDC_ECS&m=-65.33137367932665%21151.0040404858816%210%212%210%210%2C2&q=IGCMG1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001541-NSIDC_ECS&m=-65.33137367932665%21151.0040404858816%210%212%210%210%2C2&q=IGCMG1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGCMG1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGCMG1B/versions/1/",
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
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGCMG1B.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/ICEBRIDGE/IGCMG1B.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001541-NSIDC_ECS&m=-65.33137367932665%21151.0040404858816%210%212%210%210%2C2&q=IGCMG1B",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001541-NSIDC_ECS&m=-65.33137367932665%21151.0040404858816%210%212%210%210%2C2&q=IGCMG1B",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGCMG1B/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/IGCMG1B/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KDNRYQC7V2CD",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/KDNRYQC7V2CD",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KDNRYQC7V2CD",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/KDNRYQC7V2CD",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1000001541-NSIDC_ECS",
+            "issued": "2012-11-13",
+            "keyword": [
+                "solid earth",
+                "gravity/gravitational field",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/KDNRYQC7V2CD",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-01-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -53.0",
+            "temporal": "2012-11-13T00:00:00Z/2013-01-14T23:59:59.999Z",
             "theme": [
                 "2012_AN_UTIG",
                 "2013_AN_UTIG",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge CMG 1A Dynamic Gravity Meter Time-Tagged L1B Vertical Accelerations V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-RDR-HGCOORDS-1.92SEC-V1.1",
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
-                "saturn",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-rdr-hgcoords-1.92sec-v1.1_e6jm-q29f",
+            "issued": "2018-06-26",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-S-MAG-4-RDR-HGCOORDS-1.92SEC-V1.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-s-mag-4-rdr-hgcoords-1.92sec-v1.1_e6jm-q29f",
-            "description": "not applicable",
-            "title": "VG2 SAT MAG RESAMPLED HELIOGRAPHIC (RTN) COORDS 1.92SEC V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 SAT MAG RESAMPLED HELIOGRAPHIC (RTN) COORDS 1.92SEC V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VGIDSZVEXMSQ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx23 Colorado State University Ground Penetrating Radar Raw V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/VGIDSZVEXMSQ.",
-            "issued": "2023-03-07",
-            "temporal": "2023-03-07T00:00:00Z/2023-03-16T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-16",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "radar"
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
-            "identifier": "C3184787416-NSIDC_ECS",
             "description": "This data set contains the raw results of 1 GHz ground-penetrating radar surveys conducted as part of the NASA SnowEx23 field campaign in Alaska, USA. Surveys were conducted at three different field sites between 07 March 2023 and 16 March 2023: 1) Farmers Loop/Creamers Field, 2) the Bonanza Creek Experimental Forest, and 3) the Caribou/Poker Creek Research Watershed.",
-            "title": "SnowEx23 Colorado State University Ground Penetrating Radar Raw V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVGIDSZVEXMSQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVGIDSZVEXMSQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_CSU_GPR_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_CSU_GPR_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_CSU_GPR_Raw/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_CSU_GPR_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_CSU_GPR_Raw+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_CSU_GPR_Raw+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_CSU_GPR_Raw.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX23_CSU_GPR_Raw.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_CSU_GPR_Raw/versions/1/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX23_CSU_GPR_Raw/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_CSU_GPR_Raw+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX23_CSU_GPR_Raw+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VGIDSZVEXMSQ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/VGIDSZVEXMSQ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VGIDSZVEXMSQ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VGIDSZVEXMSQ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C3184787416-NSIDC_ECS",
+            "issued": "2023-03-07",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/VGIDSZVEXMSQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-148.3296 64.6992 -148.2842 64.714",
+            "temporal": "2023-03-07T00:00:00Z/2023-03-16T23:59:59.999Z",
             "theme": [
                 "SnowEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx23 Colorado State University Ground Penetrating Radar Raw V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-5-SURFACE-FIELD-MAP-V1.0",
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
-                "lunar prospector"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-5-surface-field-map-v1.0_e6pa-xqh6",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-5-SURFACE-FIELD-MAP-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-5-surface-field-map-v1.0_e6pa-xqh6",
-            "description": "not applicable",
-            "title": "LP MOON MAG LEVEL 5 SURFACE MAGNETIC FIELD MAPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LP MOON MAG LEVEL 5 SURFACE MAGNETIC FIELD MAPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-2-EDR-WILD2-V1.0",
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
-                "81p/wild 2 (1978 a2)",
-                "stardust"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains raw pre-encounter and encounter images taken by the Stardust Navigation Camera during the encounter with comet Wild 2.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-2-edr-wild2-v1.0_e6pr-h8jz",
+            "issued": "2021-05-21",
+            "keyword": [
+                "81p/wild 2 (1978 a2)",
+                "stardust"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=SDU-C-NAVCAM-2-EDR-WILD2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.sdu-c-navcam-2-edr-wild2-v1.0_e6pr-h8jz",
-            "description": "This data set contains raw pre-encounter and encounter images taken by the Stardust Navigation Camera during the encounter with comet Wild 2.",
-            "title": "STARDUST NAVCAM IMAGES OF WILD 2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "STARDUST NAVCAM IMAGES OF WILD 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67PCHURYUMOV-M10-V2.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67pchuryumov-m10-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC1-67PCHURYUMOV-M10-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc1-67pchuryumov-m10-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP010 RDR V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC1-MTP010 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M10-V3.0",
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
+            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m10-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-2-ESC1-67PCHURYUMOV-M10-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-2-esc1-67pchuryumov-m10-v3.0",
-            "description": "This CODMAC level 2 data set contains uncalibrated image data in DN unit, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2014-11-21T23:25:00.000 to 2014-12-19T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 2 ESC1-MTP010 EDR V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSINAC 2 ESC1-MTP010 EDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1312",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hurtt, G.C., R.Q. Thomas, J. Fisk, R.O. Dubayah, and S.L. Sheldon. 2016. Canopy Height and Biomass from LiDAR Surveys at La Selva, Costa Rica, 1998 and 2005. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1312",
-            "issued": "2016-03-30",
-            "temporal": "1998-03-01T00:00:00Z/2005-03-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-26",
-            "keyword": [
-                "earth science",
-                "vegetation",
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
-            "identifier": "C2773258088-ORNL_CLOUD",
             "description": "This data set contains land-use, canopy height, and aboveground carbon estimates derived from LiDAR data collected at La Selva Biological Station in Costa Rica in March 1998 and March 2005. The data are provided as GeoTIFFs (*.tif) of 100-m (1-ha) resolution. A look-up table is provided that relates modeled changes in height to changes in stand characteristics (including age and carbon content). The data were used to test the accuracy and scale-dependency of high-resolution predictions of vegetation dynamics and carbon flux by the Ecosystem Demography (ED). The ED model is an individual-based terrestrial ecosystem model that predicts both ecosystem structure and corresponding ecosystem fluxes from climate, soil, and land-use inputs.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Canopy Height and Biomass from LiDAR Surveys at La Selva, Costa Rica, 1998 and 2005",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1312_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1312",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1312",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/LaSelva_Land_Use/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/LaSelva_Land_Use/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/LaSelva_Land_Use.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/VEGETATION/guides/LaSelva_Land_Use.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1312",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1312",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/LaSelva_Land_Use/comp/CMS_LaSelva_Land_Use.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/LaSelva_Land_Use/comp/CMS_LaSelva_Land_Use.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1312_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1312_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1312",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1312",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1312_1_fit.png",
+            "identifier": "C2773258088-ORNL_CLOUD",
+            "issued": "2016-03-30",
+            "keyword": [
+                "earth science",
+                "vegetation",
+                "biosphere",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1312",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-84.05 10.4 -84.0 10.45",
+            "temporal": "1998-03-01T00:00:00Z/2005-03-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Canopy Height and Biomass from LiDAR Surveys at La Selva, Costa Rica, 1998 and 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0012-V1.0",
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
+            "description": "This is a Checkout measurement covering the time 2005-04-06T13:20:12.500 to 2005-04-06T15:45:04.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0012-v1.0_e6v8-ts9n",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CR2-0012-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cr2-0012-v1.0_e6v8-ts9n",
-            "description": "This is a Checkout measurement covering the time 2005-04-06T13:20:12.500 to 2005-04-06T15:45:04.000.",
-            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 CRUISE 2 0012 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 CRUISE 2 0012 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-CR4A-PC8-V3.0",
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
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCRUISE 4-1 mission phase. This release supersedes version 1.0. Version 2.0 was never generated\nfor pre-comet phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-cr4a-pc8-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-MIDAS-3-CR4A-PC8-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-midas-3-cr4a-pc8-v3.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCRUISE 4-1 mission phase. This release supersedes version 1.0. Version 2.0 was never generated\nfor pre-comet phases.",
-            "title": "ROSETTA-ORBITER CHECK MIDAS 3 CR4A PC8 V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK MIDAS 3 CR4A PC8 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-VILAS-ASTEROID-SPECTRA-V1.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains 81 published spectra of asteroids obtained by Faith Vilas during the years 1982 - 1992.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-vilas-asteroid-spectra-v1.1_e6w6-fepb",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "940 kordula",
                 "asteroid",
@@ -685873,54 +685875,36 @@
                 "2241 alcathous",
                 "65 cybele"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-VILAS-ASTEROID-SPECTRA-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-vilas-asteroid-spectra-v1.1_e6w6-fepb",
-            "description": "This data set contains 81 published spectra of asteroids obtained by Faith Vilas during the years 1982 - 1992.",
-            "title": "VILAS ASTEROID SPECTRA V1.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VILAS ASTEROID SPECTRA V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://data.nasa.gov/d/e6wj-e2uc",
-            "issued": "2019-11-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-15",
-            "keyword": [
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allen Anderson",
                 "hasEmail": "mailto:allen.j.andersen@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Allen Anderson"
-            },
-            "identifier": "https://data.nasa.gov/api/views/e6wj-e2uc",
             "description": "These data were used to create Fig. 1 of \u201cMonte Carlo Evaluation of the Europa Clipper TID Margin based on the Variability of the Jovian Radiation Environment with Application for Mission Design\u201d by Allen Andersen, Wousik Kim, Steven McClure, and Insoo Jun of the Jet Propulsion Laboratory, California Institute of Technology. \n\nThis data set contains Galileo Energetic Particle Detector (EPD) average counts per second measurements of 3.2-10.1 MeV protons (B0), 1.5-10.5 MeV electrons (B1), and >11 MeV electrons (DC3) between 8-10 Jovian Radii (Rj) only. Each entry has a corresponding time stamp and orbit name. Further details regarding these data can be found in \n\nJun, I., Garrett, H. B., Swimm, R., Evans, R. W., and Clough, G. (2005), Statistics of the variations of the high-energy electron population between 7 and 28 jovian radii as measured by the Galileo spacecraft, Icarus, 178(2), 386-394. https://doi.org/10.1016/j.icarus.2005.01.022\n\nThe research was carried out at the Jet Propulsion Laboratory, California Institute of Technology, under a contract with the National Aeronautics and Space Administration.",
-            "title": "Andersen et al 2020 SWJ Fig 1 data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -685928,281 +685912,306 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/e6wj-e2uc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/e6wj-e2uc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/e6wj-e2uc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.nasa.gov/api/views/e6wj-e2uc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/e6wj-e2uc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/e6wj-e2uc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.nasa.gov/api/views/e6wj-e2uc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.nasa.gov/api/views/e6wj-e2uc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.nasa.gov/api/views/e6wj-e2uc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.nasa.gov/api/views/e6wj-e2uc",
+            "issued": "2019-11-25",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://data.nasa.gov/d/e6wj-e2uc",
+            "modified": "2024-05-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Allen Anderson"
+            },
+            "title": "Andersen et al 2020 SWJ Fig 1 data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/MCR_LTER/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/MCR_LTER/DATA001.",
-            "issued": "2014-07-19",
-            "temporal": "2014-07-19T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "salinity/density",
-                "ocean temperature",
-                "ocean optics",
-                "ocean chemistry",
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
-            "identifier": "C1633360475-OB_DAAC",
             "description": "Water quality measurements taken near the island of Moorea, French Polynesia, as part of the Moorea Coral Reef Long-Term Ecological Research site (MCR LTER).",
-            "title": "Moorea Coral Reef Long-Term Ecological Research site (MCR LTER)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMCR_LTER%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMCR_LTER%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MCR_LTER/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MCR_LTER/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360475-OB_DAAC",
+            "issued": "2014-07-19",
+            "keyword": [
+                "earth science",
+                "salinity/density",
+                "ocean temperature",
+                "ocean optics",
+                "ocean chemistry",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/MCR_LTER/DATA001",
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
+            "temporal": "2014-07-19T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Moorea Coral Reef Long-Term Ecological Research site (MCR LTER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/APU/DATA301",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A, Ali  Tokay, Patrick N Gatlin and Matthew T. Wingo.2011. GPM GROUND VALIDATION AUTONOMOUS PARSIVEL UNIT (APU) LPVEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/LPVEX/APU/DATA301",
-            "issued": "2011-01-28",
-            "temporal": "2010-09-15T00:00:00Z/2011-01-12T13:15:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
-            "keyword": [
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
-            "identifier": "C1979661779-GHRC_DAAC",
             "description": "The GPM Ground Validation Autonomous Parsivel Unit (APU) LPVEx dataset provides rainfall data for the Global Precipitation Measurement (GPM) Misson Ground Validation Experiment collected at four sites in Finland: Harmaja, Emasalo, Jarvenpaa, and the Gulf of Finland (Aranda) during the Light Precipitation Validation Experiment (LPVEx), which took place during September and October of 2010. The experiment leveraged in situ microphysical property measurements, coordinated remote sensing observations, and cloud resolving model simulations of high latitude precipitation systems to conduct a comprehensive evaluation of precipitation algorithms for current and future satellite platforms.",
-            "title": "GPM GROUND VALIDATION AUTONOMOUS PARSIVEL UNIT (APU) LPVEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FAPU%2FDATA301",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FLPVEX%2FAPU%2FDATA301",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmpalpvex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmpalpvex",
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
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/disdrometers_and_gauges/parsivel/doc/gpm_parsivel_campaign.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/mc3e/disdrometers_and_gauges/parsivel/doc/gpm_parsivel_campaign.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
+            "identifier": "C1979661779-GHRC_DAAC",
+            "issued": "2011-01-28",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/LPVEX/APU/DATA301",
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
             "spatial": "21.5013 59.3335 27.4909 60.4864",
+            "temporal": "2010-09-15T00:00:00Z/2011-01-12T13:15:00Z",
             "theme": [
                 "LPVEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION AUTONOMOUS PARSIVEL UNIT (APU) LPVEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206914-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Boreholes and temperature logs from the Tibetan Plateau and Northeast China, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "1962-08-31",
-            "temporal": "1962-08-31T00:00:00Z/1995-06-15T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1995-06-15",
-            "keyword": [
-                "cryosphere",
-                "land surface",
-                "frozen ground",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shaoling Wang",
                 "hasEmail": "mailto:ggcheng@bepc2.ihep.ac.cn"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206914-NSIDCV0",
             "description": "Four groups of borehole data from the Qinghai-Xizang (Tibet) Plateau are presented. \n1) Boreholes at three sites, with sand surface, natural surface, and near a sand dune, at 66 Road Station - 1994 and 1995 measurements to about 17 meters. \n2) Borehole temperatures at Borehole CK123 - 1979, 1984, 1994 measurements to 60 meters.\n3) Borehole temperatures at five sites in Fenghuoshan Station area - 1962, 1967, 1980, 1984, 1989, 1994, 1995 measurements to 35 meters. \n4) Boreholes at Xidatan-Kunlun Pass area - 1994 and 1995 measurements to 17.5 meters; 1994 and 1995 measurements to 25 meters; and 1975, 1976, 1979, 1985, 1989, 1994 and 1995 to 30 meters. Data provided by Wang Shaoling and Cheng Guodong, Lanzhou Institute of Glaciology and Geocryology. Some of these data are presented on the CAPS Version 1.0 CD-ROM, June 1998.",
-            "title": "Boreholes and temperature logs from the Tibetan Plateau and Northeast China, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/GGD700_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/GGD700_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD700/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/GGD700/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/GGD700/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/GGD700/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C1386206914-NSIDCV0",
+            "issued": "1962-08-31",
+            "keyword": [
+                "cryosphere",
+                "land surface",
+                "frozen ground",
+                "earth science"
             ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386206914-NSIDCV0.html",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "1995-06-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
+            "temporal": "1962-08-31T00:00:00Z/1995-06-15T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Boreholes and temperature logs from the Tibetan Plateau and Northeast China, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0367-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-18T04:27:05.000 to 2014-10-18T15:00:42.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0367-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0367-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0367-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-18T04:27:05.000 to 2014-10-18T15:00:42.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0367 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0367 V1.0"
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
```

